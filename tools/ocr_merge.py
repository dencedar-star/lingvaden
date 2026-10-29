"""Дораспознать область страницы (OCR кадра крупнее) и добавить пропущенные строки в sources/ocr/pNN.json.
Использование: python3 tools/ocr_merge.py PAGE x0 y0 x1 y1  (координаты в масштабе 794x1123)."""
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OCR_BIN = sys.argv[6] if len(sys.argv) > 6 else "ocr"
K = 2481 / 794
p, x0, y0, x1, y1 = int(sys.argv[1]), *map(float, sys.argv[2:6])
d = tempfile.mkdtemp()
subprocess.run(["pdftoppm", "-r", "300", "-f", str(p), "-l", str(p), "-png",
                str(ROOT / "sources" / "Outcomes_Intermediate_SB.pdf"), d + "/hi"], check=True)
im = Image.open(next(Path(d).glob("hi*.png")))
ox, oy = int(x0 * K), int(y0 * K)
im.crop((ox, oy, int(x1 * K), int(y1 * K))).save(d + "/c.png")
new = json.loads(subprocess.run([OCR_BIN, d + "/c.png"], capture_output=True, text=True, check=True).stdout)
f = ROOT / "sources" / "ocr" / f"p{p}.json"
old = json.loads(f.read_text())
added = 0
for l in new:
    l = dict(l, x=l["x"] + ox, y=l["y"] + oy)
    cy, cx = l["y"] + l["h"] / 2, l["x"] + l["w"] / 2
    if any(o["y"] <= cy <= o["y"] + o["h"] and o["x"] - 20 <= cx <= o["x"] + o["w"] + 20 for o in old):
        continue
    old.append(l); added += 1
    print("+", int(l["x"] / K), int(l["y"] / K), l["t"])
f.write_text(json.dumps(old, ensure_ascii=False))
print("added", added)
