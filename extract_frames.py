"""Extrae los fotogramas del video del hero para la animación por scroll.

El video original tiene 240 fotogramas a 1920x1080. Para la web se guarda
1 de cada STEP fotogramas, reescalados a WIDTH px, en assets/frames/.
En móvil el script de la web usa la mitad de estos fotogramas.
"""
import shutil
from pathlib import Path

import cv2

ROOT = Path(__file__).parent
VIDEO = ROOT / "Laptop_morphing_into_robot_and_20260911101613.mp4"
OUT = ROOT / "assets" / "frames"

STEP = 2        # 240 fotogramas -> 120
WIDTH = 1600    # ancho en px (alto proporcional)
QUALITY = 70    # calidad WebP

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

print(f"Extrayendo fotogramas de {VIDEO.name}...")

cap = cv2.VideoCapture(str(VIDEO))
read = saved = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    if read % STEP == 0:
        h, w = frame.shape[:2]
        frame = cv2.resize(frame, (WIDTH, round(h * WIDTH / w)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(OUT / f"f_{saved:03d}.webp"), frame, [cv2.IMWRITE_WEBP_QUALITY, QUALITY])
        saved += 1
    read += 1
cap.release()

print(f"Leídos {read} fotogramas, guardados {saved} en {OUT}")
