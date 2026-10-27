"""Convierte el texto bruto de la politica de privacidad (copiado de la web actual) en tools/content/privacy.html.

Se ejecuta una sola vez; el resultado se versiona. Uso: python tools/clean_privacy.py ruta/al/fragmento.html
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
src = src[src.index("<h1"):]                                   # descarta la etiqueta inicial incompleta
src = re.sub(r"<h1>.*?</h1>", "", src)                        # el h1 lo pone la plantilla
src = re.sub(r'<a href="https://www.wimprove.com/" rel="noopener">.*?</a>', "", src)  # "Volver al inicio"
src = src.replace("003-2013.JUS", "003-2013-JUS")             # errata de la fuente
src = src.replace("<b></b>", "")
# Las frases venian pegadas (".Nos", ".WIMPROVE", ".De acuerdo"): cada una pasa a su propio parrafo
src = re.sub(r"([^\s.])\.(?=[A-ZÁÉÍÓÚÑ])", r"\1.</p><p>", src)
src = re.sub(r"<p>\s*</p>", "", src)
src = re.sub(r"\s+", " ", src).strip()
# Los tres titulos venian como listas ordenadas de un solo elemento
src = re.sub(r"<ol> <li><strong> ?(.*?)</strong></li> </ol>", r"<h2>\1</h2>", src)

out = Path(__file__).parent / "content" / "privacy.html"
out.write_text(src, encoding="utf-8")
print(f"{len(src)} caracteres -> {out}")
