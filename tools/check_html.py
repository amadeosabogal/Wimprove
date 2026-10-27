#!/usr/bin/env python3
"""Revisión estática de las páginas: etiquetas sin cerrar, ids duplicados y un solo <h1> por página.

Uso: python tools/check_html.py
"""
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"assets", "frames", "tools", "css", "js", ".git"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.ids, self.errors, self.h1 = [], Counter(), [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids[a["id"]] += 1
        if tag == "h1":
            self.h1 += 1
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1][0] != tag:
            top = self.stack[-1] if self.stack else None
            self.errors.append(f"</{tag}> en línea {self.getpos()[0]} no coincide con {top}")
            if any(t == tag for t, _ in self.stack):
                while self.stack and self.stack.pop()[0] != tag:
                    pass
            return
        self.stack.pop()


bad = 0
pages = [p for p in sorted(ROOT.rglob("*.html")) if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]
for page in pages:
    c = Check()
    c.feed(page.read_text(encoding="utf-8"))
    problems = list(c.errors[:5])
    problems += [f"quedó sin cerrar <{t}> de la línea {n}" for t, n in c.stack[:3]]
    problems += [f"id duplicado: {i} ({n})" for i, n in c.ids.items() if n > 1]
    if c.h1 != 1:
        problems.append(f"{c.h1} etiquetas <h1>")
    if problems:
        bad += 1
        print(f"\n{page.relative_to(ROOT)}")
        for p in problems:
            print("  -", p)
print(f"\n{len(pages)} páginas revisadas, {bad} con observaciones")
sys.exit(1 if bad else 0)
