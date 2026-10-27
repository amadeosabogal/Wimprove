#!/usr/bin/env python3
"""Comprueba que todos los iconos Phosphor usados en las páginas existen en la versión que carga el sitio (2.1.1).

Uso: python tools/check_icons.py   (necesita conexión a internet)
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"assets", "frames", "tools", "css", "js", ".git"}
BASE = "https://unpkg.com/@phosphor-icons/web@2.1.1/src"


def available(weight):
    req = urllib.request.Request(f"{BASE}/{weight}/style.css", headers={"User-Agent": "Mozilla/5.0"})
    css = urllib.request.urlopen(req, timeout=30).read().decode()
    return set(re.findall(r"\.ph-" + weight + r"\.ph-([a-z0-9-]+):before", css))


have = {w: available(w) for w in ("bold", "fill")}
used = {}
for page in ROOT.rglob("*.html"):
    if set(page.relative_to(ROOT).parts) & SKIP_DIRS:
        continue
    text = page.read_text(encoding="utf-8")
    for weight in ("bold", "fill"):
        for name in re.findall(r"ph-" + weight + r" ph-([a-z0-9-]+)", text):
            used.setdefault((weight, name), page.relative_to(ROOT).as_posix())

missing = sorted((w, n, src) for (w, n), src in used.items() if n not in have[w])
print(f"{len(used)} iconos distintos revisados")
if missing:
    print("Iconos que no existen:")
    for w, n, src in missing:
        print(f"  ph-{w} ph-{n}  (primera vez en {src})")
    sys.exit(1)
print("Todos existen")
