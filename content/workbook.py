"""Страница «Тетрадь» модуля: аудио рабочей тетради (Workbook) для домашних работ.
Текста тетради в материалах нет — к каждой записи задание «послушайте и заполните пропуски» по её расшифровке.
Расшифровка — распознавание речи двумя моделями (tools/media.py: text2 — small.en по трекам, text — large-v3-turbo по склеенной записи);
пропуски ставятся только в словах, где обе модели совпали вместе с соседними словами."""
import re
from difflib import SequenceMatcher
from html import escape
from lib import EX, AUDIO, MEDIA, G, SEC

STOP = set("""about after again also always another anything because been before being could didn does doesn doing done don't
down even every from going gonna have having here into just know like look made make many more most much must never none
only other over really right said same should since some something still such sure than that that's their them then there
these they thing things think this those though thought through told very want wanted wasn't well went were what when where
which while will with without would yeah your you're you've yes okay erm i'm it's i've i'd we're they're there's what's
part speaker point""".split())


NUM = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]


def _w(t):
    return [w.lower() for w in re.findall(r"[A-Za-z']+|\d+", t)]


def cloze(main, check, dur):
    """main — показываемый текст; check — вторая расшифровка. Возвращает html с пропусками и их число."""
    spans = list(re.finditer(r"[A-Za-z']+|\d+", main))
    a, b = [m.group(0).lower() for m in spans], _w(check)
    ok = set()
    for blk in SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        ok.update(range(blk.a + 1, blk.a + blk.size - 1))       # слово с совпавшими соседями слева и справа
    cand = [k for k in sorted(ok) if len(a[k]) >= 4 and a[k] not in STOP and "'" not in a[k] and a[k].isalpha()
            and spans[k].group(0).islower()]                    # без имён собственных и первых слов фраз
    want = max(4, min(12, int(dur // 14)))
    pick, last = [], -99
    step = len(a) / want
    for j in range(want):
        target = step * (j + 0.5)
        best = min((k for k in cand if k - last >= 4), key=lambda k: abs(k - target), default=None)
        if best is None:
            break
        pick.append(best); last = best
    out, pos = [], 0
    for k in pick:
        m = spans[k]
        out += [escape(main[pos:m.start()]), G(a[k])]
        pos = m.end()
    out.append(escape(main[pos:]))
    html = "".join(out)
    # нумерованные фразы и реплики говорящих — с новой строки
    html = re.sub(r"(?:(?<=^)|(?<=[.?!] ))(\d{1,2})\.? (?=[A-Z])", r"<br><b>\1</b> ", html)
    html = re.sub(r"(?<=[.?!] )(Speaker \d|Part \d)", r"<br>\1", html)
    return re.sub(r"^<br>", "", html), len(pick)


def build_unit(n):
    keys = [k for k in MEDIA["wb"] if k.split(".")[0] == str(n)]
    keys.sort(key=lambda k: int(k.split(".")[1]))
    if not keys:
        return '<article class="page"><p>Аудио рабочей тетради к этому модулю нет.</p></article>'
    body = ""
    for k in keys:
        e = MEDIA["wb"][k]
        main = re.sub(r"^\s*\d+\.\d+\.?\s*", "", e["text2"])       # номер записи диктор называет вслух — в тексте не нужен
        main = re.sub(r"(^|[.?!] )(%s)\.? " % "|".join(NUM), lambda m: m.group(1) + str(NUM.index(m.group(2)) + 2) + " ", main)
        main = re.sub(r"\bSpeaker (%s)\b" % "|".join(NUM), lambda m: "Speaker " + str(NUM.index(m.group(1)) + 2), main)
        check = e["text"]
        html, gaps = cloze(main, check, e["dur"])
        eid = f"wb{n}-{k.split('.')[1]}"
        if gaps:
            body += EX(eid, "", f'<span class="audio-ic">♪</span> Workbook {k}. Listen and complete the gaps.',
                       AUDIO("wb", k) + f'<div class="wb-text">{html}</div>')
        else:   # записи без связного текста (звуки, отдельные буквы) — только прослушать и повторить
            body += (f'<div class="ex" id="{eid}"><p class="ins"><span class="audio-ic">♪</span> Workbook {k}. Listen and repeat.</p>'
                     + AUDIO("wb", k) + "</div>")
    return SEC("Workbook", "аудиозаписи рабочей тетради", f'<article class="page">{body}</article>', id="wb")
