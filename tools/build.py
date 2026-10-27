#!/usr/bin/env python3
"""Genera las páginas internas de Wimprove y mantiene sincronizados el header y el footer de la Home.

Uso (desde cualquier carpeta):  python tools/build.py

- Escribe productos/, soluciones/, nosotros/, servicios/, contactanos/, catalogo/... y 404.html
- Reemplaza el header y el footer de index.html (entre los marcadores <!-- build:header --> y <!-- build:footer -->)
- Genera sitemap.xml y robots.txt

El contenido de las páginas está en tools/pages.py; los datos de productos y soluciones, en tools/data.py;
el header, footer y componentes, en tools/layout.py.
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data import SITE  # noqa: E402
from layout import footer, header, render  # noqa: E402
from pages import ALL_PAGES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def replace_block(text, name, content):
    pattern = re.compile(rf"(<!-- build:{name} -->).*?(<!-- /build:{name} -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"Falta el marcador <!-- build:{name} --> en index.html")
    return pattern.sub(lambda m: f"{m.group(1)}\n  {content}\n  {m.group(2)}", text)


def update_home():
    home = ROOT / "index.html"
    text = home.read_text(encoding="utf-8")
    text = replace_block(text, "header", header("", "", home=True))
    text = replace_block(text, "footer", footer(""))
    home.write_text(text, encoding="utf-8", newline="\n")


def main():
    update_home()
    urls = [f"{SITE}/"]
    for build_page in ALL_PAGES:
        p = build_page()
        html = render(p["path"], p["title"], p["desc"], p["body"], p.get("section", ""), p.get("noindex", False), p.get("root"))
        if p["path"].endswith(".html"):
            target = ROOT / p["path"]
        else:
            target = ROOT / p["path"].strip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8", newline="\n")
        if not p.get("noindex"):
            urls.append(f"{SITE}/{p['path'].strip('/')}/")

    today = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8", newline="\n")
    print(f"{len(ALL_PAGES)} páginas generadas + index.html (header/footer), sitemap.xml y robots.txt")


if __name__ == "__main__":
    main()
