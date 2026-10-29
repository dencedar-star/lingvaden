"""Сборка lingvaden.ru в output/. Запуск: python3 build.py"""
import hashlib, importlib, os, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT), str(ROOT / "content")]

import json
import lib
from lib import layout, progress_json, COURSE
import platform_pages

OUT = Path(os.environ["EN_OUT"]) if os.environ.get("EN_OUT") else ROOT / "output"   # EN_OUT — пробная сборка в другую папку
UNITS = ["u01", "u02", "u03", "u04", "u05", "u06", "u07", "u08", "u09", "u10", "u11", "u12", "u13", "u14", "u15", "u16"]  # пакеты content/uNN: meta, book, writing, theory, tests
if os.environ.get("EN_UNITS"):   # пробная сборка: EN_UNITS=u01,u04
    UNITS = os.environ["EN_UNITS"].split(",")

PAGES = [("book.html", "Учебник", "book"), ("writing.html", "Письмо", "writing"),
         ("theory.html", "Теория", "theory"), ("tests.html", "Тесты", "tests"), ("workbook.html", "Тетрадь", "workbook")]
ORDER = ["index.html", "theory.html", "book.html", "writing.html", "tests.html", "workbook.html"]
NAMES = {"index.html": "Обзор", "theory.html": "Теория", "book.html": "Учебник", "writing.html": "Письмо", "tests.html": "Тесты",
         "workbook.html": "Тетрадь"}
WB_LEAD = ("Аудиозаписи рабочей тетради (Workbook) к модулю: послушайте запись и заполните пропуски в её тексте. "
           "Эти задания удобно давать в домашние работы.")
WB_CARD = "Аудио рабочей тетради: слушаем и заполняем пропуски — для домашних работ."


def overview(pkg, m):
    img = f"../assets/img/unit{m.N}/"
    hero = (f'<section class="hero"><div class="hero-txt"><div class="hero-num">{m.N}</div><h1>{m.TITLE}</h1>{m.LEARN}</div>'
            f'<img src="{img}{m.HERO}" alt=""></section>')
    cards = [("theory.html", "📘", "Теория", "theory"), ("book.html", "📖", "Учебник", "book"),
             ("writing.html", "✍️", "Письмо", "writing"), ("tests.html", "✅", "Тесты", "tests"),
             ("workbook.html", "🎧", "Тетрадь", "workbook")]
    html = '<div class="cards">'
    for href, ic, t, mod in cards:
        key = f"{pkg}/{mod}"
        prog = (f'<div data-progress="{progress_json([key])}"><div class="bar"><i></i></div><div class="bar-l"></div></div>'
                if lib.REGISTRY.get(key) else "")
        html += f'<a class="card" href="{href}"><div class="ic">{ic}</div><h3>{t}</h3><p>{m.CARDS.get(mod, WB_CARD)}</p>{prog}</a>'
    html += "</div>"
    allp = (f'<div class="page" style="margin-top:22px" data-progress="{progress_json([f"{pkg}/{x}" for x in ("book", "writing", "tests", "workbook")])}">'
            f'<h3>Общий прогресс по модулю</h3><div class="bar"><i></i></div><div class="bar-l"></div></div>')
    return hero + html + allp


COURSE_TITLE = "Outcomes Intermediate"


def home():
    """Главная без входа — только вопрос «кто вы»: код из 6 цифр (по нему понятно, учитель это или ученик)."""
    return ('<section class="gate"><div class="gate-box">' + lib.MARK.replace('class="mark"', 'class="mark big"') +
            '<h1>Lingvaden English</h1><p class="lead">Введите ваш код</p>'
            '<form id="login-form" class="gate-form" autocomplete="off"><input class="code-in" name="code" inputmode="numeric" '
            'autocomplete="one-time-code" pattern="[0-9]{6}" maxlength="6" placeholder="000000" aria-label="Код из 6 цифр" required autofocus>'
            '<button class="btn" type="submit">Войти</button></form><div class="err" id="login-err" hidden></div>'
            '<p class="note-s">Код из 6 цифр выдаёт преподаватель (ученикам) или администрация (преподавателям). '
            'По коду сайт сам поймёт, кто вы. Ученик может войти и по личной ссылке от преподавателя.</p></div></section>')


def nav_next(name):
    k = ORDER.index(name)
    prev = f'<a href="{ORDER[k - 1]}">← {NAMES[ORDER[k - 1]]}</a>' if k > 0 else "<span></span>"
    nxt = f'<a href="{ORDER[k + 1]}">{NAMES[ORDER[k + 1]]} →</a>' if k + 1 < len(ORDER) else "<span></span>"
    return f'<div class="next">{prev}{nxt}</div>'


def build_unit(pkg, ver):
    m = importlib.import_module(f"{pkg}.meta")
    unit_dir = OUT / f"unit{m.N}"
    unit_dir.mkdir(parents=True, exist_ok=True)
    name = f"Unit {m.N} {m.TITLE}"
    crumbs = f'<div class="crumbs"><a href="../me/#courses">Outcomes Intermediate</a> › <a href="./">{name}</a></div>'
    out = {}
    for fname, label, mod in PAGES:
        lib.set_page(f"{pkg}/{mod}")
        if mod == "workbook":   # общий генератор: аудио рабочей тетради из media/index.json
            body = importlib.import_module("workbook").build_unit(int(m.N))
        else:
            body = importlib.import_module(f"{pkg}.{mod}").build()
        title = f"{label} — {m.WRITING if mod == 'writing' else name}"
        lead = m.LEADS.get(mod, WB_LEAD)
        head = f'{crumbs}<h1 class="page-title">{label}</h1><p class="lead">{lead}</p>'
        tail = ""
        if mod == "tests":
            tail = (f'<div class="total" data-progress="{progress_json([f"{pkg}/tests"])}"><button class="btn" type="button" '
                    'data-check-all>Проверить всё</button><div class="bar"><i></i></div><div class="bar-l"></div></div>')
        out[fname] = layout(title + " · Outcomes Intermediate", lead, head + body + tail + nav_next(fname), fname,
                            ctx={"unit": f"unit{m.N}", "page": mod})
    out["index.html"] = layout(f"{name} · Outcomes Intermediate",
                               f"Модуль {int(m.N)} курса Outcomes Intermediate: теория, учебник, письмо, тесты и рабочая тетрадь.",
                               '<div class="crumbs"><a href="../me/#courses">Outcomes Intermediate</a></div>' + overview(pkg, m) +
                               nav_next("index.html"), "index.html", ctx={"unit": f"unit{m.N}", "page": "index"})
    for f, h in out.items():
        (unit_dir / f).write_text(h.replace("{V}", ver), encoding="utf-8")
    return m


def catalog(metas):
    """Каталог курса для кабинетов: модули → страницы → задания (id, число полей, подпись)."""
    units = []
    for pkg, m in metas:
        pages = []
        for fname, label, mod in PAGES:
            ex = [[i, n, lib.EXINFO[i]["let"], lib.EXINFO[i]["ins"]] for i, n in lib.REGISTRY.get(f"{pkg}/{mod}", [])]
            pages.append({"id": mod, "title": label, "url": f"/unit{m.N}/{fname}", "ex": ex})
        units.append({"id": f"unit{m.N}", "n": m.N, "title": m.TITLE, "url": f"/unit{m.N}/", "pages": pages})
    return {"courses": [{"id": COURSE, "title": COURSE_TITLE, "units": units, "planned": 16, "cover": f"/assets/covers/{COURSE}.jpg",
                         "level": "B1+ · Student’s Book"}]}


def main():
    if OUT.exists():
        for p in OUT.iterdir():
            if p.name != "assets":
                shutil.rmtree(p) if p.is_dir() else p.unlink()
    assets = OUT / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    if OUT != ROOT / "output" and not (assets / "img").exists():
        (assets / "img").symlink_to(ROOT / "output" / "assets" / "img")
    for f in ["app.css", "app.js", "teacher.js", "student.js", "favicon.svg"]:
        shutil.copy(ROOT / "site" / f, assets / f)
    for d in ["fonts", "brand", "vendor", "covers"]:
        shutil.copytree(ROOT / "site" / d, assets / d, dirs_exist_ok=True)
    for f in [".htaccess", "sw.js", "site.webmanifest"]:
        shutil.copy(ROOT / "site" / f, OUT / f)
    shutil.copytree(ROOT / "server", OUT, dirs_exist_ok=True)   # api/*.php
    # аудио и видео (готовит tools/media.py): жёсткие ссылки, без копирования; отдаёт api/media.php только вошедшим
    for kind in ("sb", "wb", "video"):
        src = ROOT / "media" / kind
        if src.is_dir():
            (OUT / "media" / kind).mkdir(parents=True, exist_ok=True)
            for f in src.iterdir():
                os.link(f, OUT / "media" / kind / f.name)
    ver = hashlib.md5(b"".join((assets / f).read_bytes() for f in ("app.css", "app.js", "teacher.js", "student.js"))).hexdigest()[:8]

    metas = [(pkg, build_unit(pkg, ver)) for pkg in UNITS]
    (OUT / "index.html").write_text(layout("Lingvaden English — вход по коду",
                                           "Интерактивные курсы английского: вход для преподавателей и учеников по личному коду.",
                                           home(), root="", unit_nav=False, app="home")
                                    .replace("{V}", ver), encoding="utf-8")
    cat = catalog(metas)
    (assets / "catalog.json").write_text(json.dumps(cat, ensure_ascii=False), encoding="utf-8")
    for path, (title, desc, body, site, scripts) in platform_pages.pages(cat).items():
        f = OUT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        root = "../" * path.count("/")
        f.write_text(layout(title, desc, body.replace("{ROOT}", root), root=root, unit_nav=False, app=site, scripts=scripts)
                     .replace("{V}", ver), encoding="utf-8")
    # service worker: версия кеша = версия сборки
    sw = OUT / "sw.js"
    sw.write_text(sw.read_text(encoding="utf-8").replace("{V}", ver), encoding="utf-8")
    print("ok:", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*.html")))
    print({k: (len(v), sum(n for _, n in v)) for k, v in lib.REGISTRY.items()})


if __name__ == "__main__":
    main()
