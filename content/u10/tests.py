"""Страница «Тесты»: упражнения Grammar reference p. 149 (ключи — Grammar Reference, 10) и итоговый тест."""
from lib import G, S, EX, OL
from ocrtext import lines, fixed, _fix
from . import shared as X

FIP_START = ["I only expected there to be about 20 people,", "I was going to buy her a present,", "I was going to call you,",
             "I was about to leave the house,", "I was about to say yes,", "I thought it’d be rubbish,",
             "He promised he’d be there,", "He said he’d pay me back,"]
FIP_END = ["but I’m still waiting for the money.", "but he never turned up.", "but I actually really enjoyed it.",
           "but I wasn’t sure what she’d want.", "but then he said something which put me off.", "but the place was packed.",
           "but I had my mobile stolen.", "when they called to say the meeting had been cancelled."]


def ex1():
    """Ключ: 1 f 2 d 3 g 4 h 5 e 6 c 7 b 8 a."""
    key = "f d g h e c b a".split()
    return EX("t10-g1", "1", "Match 1–8 with a–h to make complete sentences.",
              OL([f"{q} … {S(k, X.AH)}" for q, k in zip(FIP_START, key)]) + OL(FIP_END, "items alpha"))


def ex2():
    """Ответы — ключ (полные предложения), в пропуск — часть между данными словами."""
    W = lambda a: G(a, "wide")
    rows = [("He promised to help me later.", "said", f"He {W('said he would help|said he’d help')} me later."),
            ("We hadn’t planned to return now, but we ran out of money.", "stay",
             f"We {W('wanted to stay')} longer, but we ran out of money."),
            ("Just before I was going to phone him, he called me!", "about",
             f"I {W('was just about to phone him')} when he called me!"),
            ("I expected him to be rubbish, but he was quite good.", "thought",
             f"His performance was much better {W('than I thought it would')} be."),
            ("I was surprised how much it cost.", "expect", f"I {W('wasn’t expecting it to cost|was not expecting it to cost')} so much."),
            ("It’s so sunny! The forecast was for rain.", "to",
             f"They said {W('it was going to rain')}, but it’s turned out really nice.")]
    return EX("t10-g2", "2", "Rewrite 1–6 using the words in bold and three or four other words, so the sentences have a similar "
              "meaning.", OL([f"{a}<br><b>{b}</b><br>{c}" for a, b, c in rows]))


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip().replace(" - ", " – ")
        if t.startswith("Glossary") or set(t) <= set(". "):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part = ('<article class="page" id="t149"><span class="page-no">Учебник, с. 149</span>'
            '<h2>Grammar reference: The future in the past</h2>'
            '<p><a href="theory.html#gr149">Правило — в разделе «Теория»</a></p>' + ex1() + ex2() +
            gloss(149, (450, 910, 745, 1035)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 70–75</span><h2>Итоговый тест по модулю 10</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.odd_one("t10-f1", "1") + X.whats_on("t10-f2", "2") + X.directions("t10-f3", "3") + X.adjectives("t10-f4", "4") +
             X.bold_words("t10-f5", "5", "Match the words from <i>What’s on in Buenos Aires?</i> with their meanings.") +
             X.bold_gaps("t10-f6", "6", "Complete the sentences with the words from exercise 5.") +
             X.expressions("t10-f7", "7") + X.event("t10-f8", "8") +
             X.kinds("t10-f9", "9", "What kind of event did each person in <i>Listening</i> 10.5 go to?") +
             X.fip_gaps("t10-f10", "10") + X.fip_rewrite("t10-f11", "11") + "</article>")
    toc = '<nav class="toc"><a href="#t149">The future in the past</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part + final
