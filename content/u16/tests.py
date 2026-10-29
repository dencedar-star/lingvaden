"""Страница «Тесты»: упражнения Grammar reference p. 155 (ключи — Grammar Reference, 16) и итоговый тест."""
from lib import G, S, EX, OL
from ocrtext import lines, fixed, _fix
from . import shared as X

STARTS = ["Did you apply for that job", "Did you read about that guy", "What’s the name of that company", "We met that woman",
          "We went to that bar", "He’s the writer"]
PAIRS = ["you recommended. It was really good! / where all the stars go, but we didn’t see anyone famous!",
         "which went bankrupt last week? / Maria works for?",
         "whose novel was banned by government. / who won the Nobel prize a couple of years ago.",
         "you were telling me about? / that was advertised in the paper yesterday?",
         "who works with you. I’ve forgotten her name! / you said you’re interested in.",
         "they arrested for that big robbery? / who was awarded the Nobel peace prize?"]


def rel1():
    key = "d f b e a c".split()
    return EX("t16-r1", "1", "Match the sentence starters 1–6 with the pairs of relative clauses a–f.",
              OL([f"{q} … {S(k, list('abcdef'))}" for q, k in zip(STARTS, key)]) + OL(PAIRS, "items alpha"))


def rel2():
    g = lambda n, a: f"<sup>{n}</sup>{G(a)}"
    text = (f"<i>Lorenzo’s Oil</i> is a film {g(1, 'which|that')} tells the true story of a couple {g(2, 'whose')} child "
            f"develops medical problems at the age of 7. The first doctors {g(3, 'who|that')} see him have no idea what is "
            f"causing the problem, but he is eventually diagnosed with a disease {g(4, 'which|that')} is called ALD and is "
            f"incurable. They ask about hospitals {g(5, 'where')} they are doing research on this disease, but they are told it "
            f"is so rare that no one will pay the money {g(6, 'which|that')} is needed to investigate it. The couple, who have "
            f"no medical training, then start to study medical literature to find something {g(7, 'which|that')} will help "
            f"their son. I love this film because at the time {g(8, 'when|that')} I saw it I was also quite ill, and it was very "
            "uplifting. Like the boy in the film, I eventually got better.")
    return EX("t16-r2", "2", "Complete the film review with appropriate relative pronouns. Which one of the pronouns in 1–8 "
              "could be left out?", f'<div class="story"><p>{text}</p></div>'
              '<p class="note-s">Ключ: опустить можно местоимение 8 (<i>when</i>).</p>')


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip()
        if t.startswith("Glossary") or set(t) <= set(". "):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part1 = ('<article class="page" id="t155"><span class="page-no">Учебник, с. 155</span>'
             '<h2>Grammar reference: Defining relative clauses</h2>'
             '<p><a href="theory.html#gr155">Правило — в разделе «Теория»</a></p>' + rel1() + rel2() +
             gloss(155, (448, 825, 745, 995)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 110–115</span>'
             '<h2>Итоговый тест по модулю 16</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.news_pairs("t16-f1", "1", "Match the pairs of words from the news stories in <i>Listening</i> 16.1.") +
             X.who_people("t16-f2", "2", "Complete the descriptions of famous people with the words in the box.") +
             X.rel_cross("t16-f3", "3") +
             X.sections("t16-f4", "4", "In which of the six sections of the article <i>Seeking fame and fortune</i> were the "
                                       "following mentioned?") +
             X.fame_words("t16-f5", "5") + "</article>")
    toc = '<nav class="toc"><a href="#t155">Defining relative clauses</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
