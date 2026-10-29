"""Вырезает иллюстрации модулей из страниц учебника (скан 794x1123) в output/assets/img/unitNN.
Запуск: python3 tools/crop_images.py unit02 [имя ...]"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "sources" / "Outcomes_Intermediate_SB.pdf"
IMG = ROOT / "output" / "assets" / "img"

# имя: (страница учебника, (x0, y0, x1, y1))
CROPS = {"unit01": {
    "p08-banner": (8, (0, 40, 794, 305)),
    "p08-couple": (8, (0, 340, 252, 830)),
    "p09-students": (9, (0, 46, 384, 322)),
    "p09-person1": (9, (453, 882, 532, 960)),
    "p09-person2": (9, (537, 882, 616, 960)),
    "p09-person3": (9, (622, 882, 702, 960)),
    "p09-person4": (9, (713, 882, 788, 960)),
    "p09-person5": (9, (453, 962, 532, 1040)),
    "p09-person6": (9, (537, 962, 616, 1040)),
    "p09-person7": (9, (622, 962, 702, 1040)),
    "p09-person8": (9, (713, 962, 788, 1040)),
    "p10-classroom": (10, (292, 864, 786, 1100)),
    "p11-cartoon": (11, (410, 445, 776, 722)),
    "p13-steve": (13, (58, 478, 692, 1058)),
    "p120-banner": (120, (0, 40, 794, 175)),
    "p120-kay": (120, (408, 300, 492, 412)),
    "p120-act1": (120, (48, 572, 188, 718)),
    "p120-act2": (120, (202, 572, 341, 718)),
    "p120-act3": (120, (48, 732, 188, 878)),
    "p120-act4": (120, (202, 732, 341, 878)),
    "p120-act5": (120, (48, 892, 188, 1040)),
    "p120-act6": (120, (202, 892, 341, 1040)),
    "p121-kickboxing": (121, (380, 805, 760, 1052)),
}, "unit02": {
    "p14-banner": (14, (0, 40, 794, 318)),
    "p14-shop": (14, (25, 545, 385, 728)),
    "p14-retirement": (14, (25, 742, 385, 932)),
    "p15-boy": (15, (25, 40, 395, 322)),
    "p15-friends": (15, (458, 410, 760, 655)),
    "p15-worried": (15, (25, 885, 215, 1085)),
    "p16-couple": (16, (10, 40, 250, 200)),
    "p16-title": (16, (425, 85, 790, 415)),
    "p16-sign": (16, (426, 432, 514, 540)),
    "p16-hug": (16, (420, 765, 778, 1078)),
    "p17-hug": (17, (25, 85, 342, 415)),
    "p17-class": (17, (400, 680, 792, 830)),
    "p18-friends": (18, (0, 40, 372, 272)),
    "p19-heaven": (19, (20, 530, 266, 692)),
    "p19-hell": (19, (530, 530, 794, 692)),
    "p122-banner": (122, (0, 40, 794, 178)),
    "p123-prague": (123, (440, 815, 737, 1042)),
}, "unit03": {
    "p20-banner": (20, (0, 40, 794, 322)),
    "p20-places1": (20, (15, 333, 380, 628)),
    "p20-places2": (20, (385, 333, 792, 566)),
    "p21-friends": (21, (20, 40, 398, 320)),
    "p21-krakow": (21, (40, 770, 385, 890)),
    "p22-problems": (22, (55, 52, 790, 312)),
    "p23-traffic": (23, (30, 880, 416, 1085)),
    "p24-landscape": (24, (66, 645, 358, 842)),
    "p24-island": (24, (20, 840, 794, 1058)),
    "p25-couple": (25, (88, 40, 400, 198)),
    "p25-calendar": (25, (412, 806, 788, 1056)),
    "p124-banner": (124, (0, 40, 794, 182)),
    "p124-parachute": (124, (48, 815, 343, 1042)),
    "p125-banner": (125, (0, 40, 794, 182)),
    "p32-banner": (32, (0, 38, 794, 174)),
    "p32-game": (32, (0, 522, 794, 1058)),
}}

def page_image(n, tmp):
    prefix = Path(tmp) / f"p{n}"
    subprocess.run(["pdfimages", "-f", str(n), "-l", str(n), "-png", str(PDF), str(prefix)], check=True)
    return Image.open(f"{prefix}-000.png").convert("RGB")

def main():
    unit = sys.argv[1] if len(sys.argv) > 1 else "unit01"
    OUT = IMG / unit
    OUT.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[2:])
    if unit not in CROPS:   # новые модули держат свои вырезки в content/uNN/crops.py (CROPS = {имя: (стр, box)})
        import importlib.util
        f = ROOT / "content" / ("u" + unit[4:]) / "crops.py"
        spec = importlib.util.spec_from_file_location("crops", f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        CROPS[unit] = mod.CROPS
    with tempfile.TemporaryDirectory() as tmp:
        cache = {}
        for name, (page, box) in CROPS[unit].items():
            if only and name not in only:
                continue
            if page not in cache:
                cache[page] = page_image(page, tmp)
            im = cache[page].crop(box)
            # скан 96 dpi: увеличиваем мелкие картинки вдвое, чтобы не «мылились» на ретине
            if im.width < 400:
                im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
            im.save(OUT / f"{name}.jpg", quality=88, optimize=True)
            print(name, im.size)

if __name__ == "__main__":
    main()
