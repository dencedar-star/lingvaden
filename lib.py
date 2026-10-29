"""Общие помощники генератора: поля заданий, упражнения, аудиоскрипты, каркас страницы."""
import json, re
from html import escape
from pathlib import Path

# аудио и видео курса: media/index.json готовит tools/media.py из sources/ (файлы отдаёт api/media.php только вошедшим)
_MI = Path(__file__).resolve().parent / "media" / "index.json"
MEDIA = json.loads(_MI.read_text(encoding="utf-8")) if _MI.exists() else {"sb": {}, "wb": {}, "video": {}}
_ALAB = re.compile(r"♪</span>\s*(R\s?)?(\d+\.\d+)")
_last_audio = {}   # страница -> последняя названная в задании запись (для «Listen again»)
# видео к урокам: после задания с этим id (ролик повторяет разговор урока, во второй раз одна роль без звука)
VIDEOS = {"b9-dc": "1", "b15-pa": "2", "b21-lb": "3", "b26-pa": "4", "b37-db": "5"}


def AUDIO(kind, key, note=""):
    """Плеер записи: kind sb — учебник, wb — рабочая тетрадь; key — 1.1, R4.2 …"""
    e = MEDIA[kind].get(key)
    if not e:
        return ""
    name = ("Review " + key[1:] if key.startswith("R") else key)
    name = ("Workbook " if kind == "wb" else "") + name
    parts = "".join(f'<button type="button" data-t="{t}" title="Часть {i + 1}">{i + 1}</button>' for i, t in enumerate(e["parts"]))
    parts = f'<span class="aud-parts">части: {parts}</span>' if parts else ""
    return (f'<div class="aud"><span class="aud-l">♪ {name}{note}</span>'
            f'<audio controls preload="none" controlslist="nodownload" src="/media/{e["f"]}"></audio>{parts}</div>')


def VIDEO(n):
    e = MEDIA["video"].get(n)
    if not e:
        return ""
    return (f'<figure class="vid"><figcaption><b>▶ Видео {n}</b> — посмотрите разговор из урока. Во второй половине ролика '
            'реплики одного из собеседников идут без звука: остановите видео и скажите их сами.</figcaption>'
            f'<video controls preload="none" playsinline controlslist="nodownload" src="/media/{e["f"]}"></video></figure>')

# реестр заданий: страница -> [(id, число проверяемых элементов)]
REGISTRY = {}
_current_page = ["?"]


def set_page(name):
    _current_page[0] = name
    REGISTRY.setdefault(name, [])


def G(ans, cls=""):
    """Пропуск со вводом. ans — варианты через |."""
    n = max(len(a) for a in ans.split("|"))
    w = "" if "wide" in cls else f' style="width:{max(4, n + 2)}ch"'
    return f'<input class="gap {cls}" data-a="{escape(ans)}" autocomplete="off" autocapitalize="off" spellcheck="false"{w} aria-label="ответ">'


def S(ans, opts):
    return f'<select class="sel" data-a="{escape(ans)}" data-opts="{escape("|".join(opts))}" aria-label="ответ"></select>'


def C(ans, *opts):
    bs = "".join(f"<button>{o}</button>" for o in opts)
    return f'<span class="choice" data-a="{escape(ans)}">{bs}</span>'


def TF(ans):
    return '<span class="tf">' + C("True" if ans == "T" else "False", "True", "False") + "</span>"


def INS(correct, word):
    """Вставка слова кликом: correct — правильное предложение, word — слово из скобок."""
    end = correct[-1] if correct[-1] in ".?!" else ""
    body = correct[:-1] if end else correct
    toks = body.split(" ")
    wt = word.split(" ")
    pos = next(i for i in range(len(toks)) if toks[i:i + len(wt)] == wt)
    rest = toks[:pos] + toks[pos + len(wt):]
    out = []
    for i, t in enumerate(rest):
        out.append(escape(t))
        out.append('<span class="slot"></span>')
    html = " ".join(out) + end
    return f'<div class="ins-row" data-word="{escape(word)}" data-a="{pos - 1}">{html} <span class="word-tag">({escape(word)})</span></div>'


_TOK = re.compile(r"[^\s.,?!;]+|[.,?!;]")


def INS2(correct, word, alts=()):
    """Вставка слова, где возможна позиция в начале и перед знаком препинания.
    alts — другие правильные варианты того же предложения (например, слово в начале)."""
    def split(s):
        toks = _TOK.findall(s)
        wt = word.lower().split()
        low = [t.lower() for t in toks]
        i = next(k for k in range(len(toks)) if low[k:k + len(wt)] == wt)
        return toks[:i] + toks[i + len(wt):], i
    rest, pos = split(correct)
    ok = [pos] + [split(a)[1] for a in alts]
    out = []
    for j, t in enumerate(rest):
        punct = t in ".,?!;"
        if j:
            out.append("" if punct else " ")
        out.append('<span class="slot"></span>')
        out.append(escape(t))
    return (f'<div class="ins-row" data-word="{escape(word)}" data-a="{"|".join(map(str, ok))}">{"".join(out)} '
            f'<span class="word-tag">({escape(word)})</span></div>')


def ORDER(scrambled, answer):
    words = scrambled.replace("?", "").split()
    return (f'<div class="order" data-words="{escape("|".join(words))}" data-a="{escape(answer)}">'
            f'<div class="line"></div><div class="bank"></div><div class="ans" hidden>{escape(answer)}</div></div>')


def REVEAL(html, label="Показать ответ"):
    return f'<details class="reveal"><summary>{label}</summary><div class="key">{html}</div></details>'


_GRADE = re.compile(r'class="(gap|sel|choice|ins-row|order)[ "]')


# сведения о заданиях для каталога курса (кабинеты учителя и ученика): id -> страница, число полей, подпись
EXINFO = {}


def _plain(html, n=160):
    t = re.sub(r"<[^>]+>", "", html).replace("&nbsp;", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def EX(id, letter, instr, body):
    n = len(_GRADE.findall(body))
    if n:
        assert id not in EXINFO, f"повтор id задания: {id}"
        REGISTRY[_current_page[0]].append((id, n))
        EXINFO[id] = {"page": _current_page[0], "n": n, "let": letter, "ins": _plain(instr)}
    let = f'<b class="let">{letter}</b> ' if letter else ""
    m, page, aud = _ALAB.search(instr), _current_page[0], ""
    if m:
        key = ("R" if m.group(1) else "") + m.group(2)
        _last_audio[page] = key
        aud = AUDIO("sb", key)
    elif re.search(r"\bListen\b", instr) and page in _last_audio:
        aud = AUDIO("sb", _last_audio[page])
    if aud:
        body = body.replace(aud, "")   # аудиоскрипт внутри задания: плеер уже стоит под заданием
    vid = VIDEO(VIDEOS[id]) if id in VIDEOS else ""
    return f'<div class="ex" data-ex="{id}" id="{id}"><p class="ins">{let}{instr}</p>{aud}{body}</div>{vid}'


def OL(items, cls="items", start=1):
    st = f' start="{start}"' if start != 1 else ""
    return f'<ol class="{cls}"{st}>' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def UL(items):
    return '<ul class="dots">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def DLG(*pairs):
    return '<div class="dlg">' + "".join(f"<b>{s}:</b><span>{t}</span>" for s, t in pairs) + "</div>"


def SCRIPT(num, title, lines, page="160"):
    """lines: (говорящий, реплика) или ('#', заголовок)."""
    out = []
    for sp, t in lines:
        if sp == "#":
            out.append(f"<h5>{t}</h5>")
        else:
            out.append(f'<p class="line" data-sp="{escape(sp)}"><b>{sp}:</b><span>{t}</span></p>')
    aud = AUDIO("sb", re.sub(r"^R\s+", "R", str(num)))
    tts = ('<div class="tts"><button type="button" class="btn ghost" data-play>▶ Озвучить</button>'
            '<button type="button" class="btn plain" data-stop>■ Стоп</button>'
            '<span>синтезатор речи браузера</span></div>')
    return (f'<details class="script"><summary><span class="audio-ic">♪</span> Аудиоскрипт {num}{" — " + title if title else ""}'
            f' <small>(учебник, с. {page})</small></summary>' + (aud or tts) +
            f'<div class="lines">{"".join(out)}</div></details>')


def SEC(title, sub, body, id=None):
    a = f' id="{id}"' if id else ""
    h = f"<h2>{title}" + (f" <span>{sub}</span>" if sub else "") + "</h2>"
    return f'<section class="sec"{a}>{h}{body}</section>'


def PAGE_BOX(no, body):
    return f'<article class="page" id="p{no}"><span class="page-no">Учебник, с. {no}</span>{body}</article>'


def IMG(src, alt, cap="", cls=""):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="fig{" " + cls if cls else ""}"><img src="{src}" alt="{escape(alt)}" loading="lazy">{c}</figure>'


HELP = lambda p: f'<p class="help">▶ Need help? Read the <a href="theory.html#gr{p}">grammar reference on p. {p}</a></p>'

TABS = [("index.html", "Обзор"), ("theory.html", "Теория"), ("book.html", "Учебник"),
        ("writing.html", "Письмо"), ("tests.html", "Тесты"), ("workbook.html", "Тетрадь")]

# по умолчанию — светлая тема; тёмная — только если человек сам её выбрал
THEME_JS = ("<script>(function(){var t='light';try{if(localStorage.getItem('en_theme')==='dark')t='dark'}catch(e){}"
            "document.documentElement.setAttribute('data-theme',t)})();</script>")


COURSE = "outcomes-int"   # id курса в БД и каталоге; следующий учебник — другой id
MARK = ""
# без входа сайт закрыт: в шапке только логотип; у вошедших — своё меню слева (рисует app.js)


def footer(root):
    links = [("how/", "Как это работает"), ("legal/", "Правовая информация"), ("legal/privacy.html", "Персональные данные"),
             ("legal/cookies.html", "Cookies")]
    nav = " · ".join(f'<a href="{root}{h}">{t}</a>' for h, t in links)
    return (f'<footer class="site-foot"><div class="foot-in">'
            f'<a class="foot-brand" href="https://lingvaden.ru/">{MARK}<span>Lingvaden<b>·</b>English</span></a>'
            f'<nav class="foot-nav">{nav}</nav>'
            '<p class="foot-src">Материалы курса: <i>Outcomes Intermediate</i> Student’s Book (Hugh Dellar, Andrew Walkley; '
            'Heinle, Cengage Learning) и ключи к нему; права на них принадлежат правообладателям. Занятия — только по личному '
            'коду: ответы ученика хранятся на сервере, и их видит его преподаватель.</p>'
            '<p class="foot-src">© 2026 lingvaden.ru · <a href="mailto:info@lingvaden.ru">info@lingvaden.ru</a></p>'
            '</div></footer>')


def layout(title, desc, body, active=None, root="../", unit_nav=True, ctx=None, site=None, scripts=(), app=None):
    """ctx — {'unit': 'unit01', 'page': 'book'} для страниц курса; app — home | teacher | student | info (для app.js)."""
    on = ' class="on"'
    if unit_nav:
        tabs = '<nav class="tabs">' + "".join(
            f'<a href="{h}"{on if h == active else ""}>{t}</a>' for h, t in TABS) + "</nav>"
    else:
        tabs = '<nav class="tabs"></nav>'
    ctx = ctx or {}
    data = f' data-course="{COURSE}"' if ctx else ""
    data += "".join(f' data-{k}="{escape(v)}"' for k, v in ctx.items())
    if app:
        data += f' data-app="{app}"'
    extra = "".join(f'\n<script src="{root}assets/{s}?v={{V}}"></script>' for s in scripts)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
{THEME_JS}
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#17213B">
<link rel="manifest" href="{root}site.webmanifest">
<meta name="apple-mobile-web-app-title" content="Lingvaden English">
<link rel="stylesheet" href="{root}assets/fonts/fonts.css">
<link rel="stylesheet" href="{root}assets/app.css?v={{V}}">
<link rel="icon" href="{root}assets/favicon.svg?v={{V}}" type="image/svg+xml">
</head>
<body data-root="{root}"{data}>
<header class="top"><div class="top-in">
<a class="logo" href="{root}">{MARK}<span>Lingvaden<b>·</b>English</span></a>
{tabs}
<div class="who" id="who" hidden></div>
<button class="theme" type="button" aria-label="Сменить тему"></button>
</div></header>
<div class="hello" id="hello" hidden></div>
<div class="shell"><aside class="side" id="side" hidden></aside>
<main class="wrap">
{body}
</main></div>
{footer(root)}
<script src="{root}assets/app.js?v={{V}}"></script>{extra}
</body>
</html>
"""


def progress_json(pages):
    ids = []
    for p in pages:
        ids += REGISTRY.get(p, [])
    return escape(json.dumps(ids))
