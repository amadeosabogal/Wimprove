#!/usr/bin/env python3
"""Revisa que los enlaces y recursos locales de todas las páginas existan (archivos y anclas).

Uso: python tools/check_links.py
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"assets", "frames", "tools", "css", "js", ".git"}
ATTR = re.compile(r'(?:href|src)="([^"]*)"')
IDS = re.compile(r'\bid="([^"]+)"')

pages = [p for p in ROOT.rglob("*.html") if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]
ids = {p: set(IDS.findall(p.read_text(encoding="utf-8"))) for p in pages}
problems, checked = [], 0

for page in sorted(pages):
    html = page.read_text(encoding="utf-8")
    is_404 = page.name == "404.html"
    for ref in ATTR.findall(html):
        if not ref or ref.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//", "javascript:")):
            continue
        parsed = urlparse(ref)
        checked += 1
        if ref.startswith("/"):
            target = ROOT / unquote(parsed.path).lstrip("/")
        elif parsed.path:
            target = (page.parent / unquote(parsed.path)).resolve()
        else:
            target = page
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            problems.append(f"{page.relative_to(ROOT)}: falta {ref}")
            continue
        if parsed.fragment and target.suffix == ".html" and target in ids and parsed.fragment not in ids[target]:
            problems.append(f"{page.relative_to(ROOT)}: ancla #{parsed.fragment} no existe en {target.relative_to(ROOT)}")

print(f"{len(pages)} páginas, {checked} referencias locales revisadas")
if problems:
    print(f"\n{len(problems)} problemas:")
    print("\n".join(sorted(set(problems))))
    sys.exit(1)
print("Sin problemas")
