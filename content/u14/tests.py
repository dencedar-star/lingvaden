"""Страница «Тесты»: упражнения Grammar reference p. 153 (ключи — Grammar Reference, 14) и итоговый тест."""
from lib import G, C, EX, OL
from ocrtext import lines, fixed, _fix, FIX
from . import shared as X

FIX[153] = [("something. it has", "something, it has")]


def ing1():
    rows = [f"There’s nothing wrong {G('in letting|with letting')} kids play computer games so long as you control it a bit.",
            f"I was involved {G('in setting up')} the website at work.",
            f"He always has to travel by train because he’s so scared {G('of flying')}.",
            f"My parents pushed me {G('into studying')} Computer Engineering, but personally I would’ve preferred to study "
            "Chemistry.",
            f"I’m thinking {G('of giving up')} basketball because I can’t get into the team.",
            f"She’s apologised {G('for shouting')} at me now, so we’ve made up and we’re friends again.",
            f"The phone is capable {G('of storing')} 500 photos.",
            f"I’m fed up {G('with working')} weekends! It’s too much.",
            f"She always blames me {G('for being')} late, but it’s often her fault.",
            f"I can’t cope {G('with organising')} the wedding all on my own.",
            f"He’s useless {G('at talking')} to people. It’s embarrassing.",
            f"My son even complains {G('about having to')} tidy his room."]
    return EX("t14-i1", "1", "Complete each sentence with the correct preposition and a verb in an <i>-ing</i> form.",
              X.wordbox(["study", "fly", "let", "set up", "shout", "give up"]) + OL(rows[:6]) +
              X.wordbox(["organise", "talk", "work", "be", "store", "have to"]) + OL(rows[6:], start=7))


def ing2():
    rows = [("My job involves {} a lot.", "travelling", "to travel"),
            ("Do you fancy {} somewhere this evening?", "going out", "to go out"),
            ("Sorry. I’ve arranged {} a friend.", "to meet", "meeting"),
            ("I’d rather stay in. I don’t feel like {} out.", "going", "to go"),
            ("They finally agreed {} the staff more after three days of negotiations.", "to pay", "paying"),
            ("He played well. He didn’t deserve {}.", "to lose", "losing"),
            ("I asked her very politely {} me a response, but I still haven’t heard back from her.", "to email", "emailing"),
            ("I avoid {} to him as much as I can.", "talking", "to talk"),
            ("Unless you want to risk {} your work, you should set your computer to save automatically.", "losing", "to lose"),
            ("They’re threatening {} anyone who’s caught surfing the Internet at work.", "to fire", "firing")]
    out = []
    for t, a, b in rows:
        ing, inf = (a, b) if not a.startswith("to ") else (b, a)
        out.append(t.format(C(a, ing, inf)))
    return EX("t14-i2", "2", "Choose the correct form.", OL(out))


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
    part1 = ('<article class="page" id="t153"><span class="page-no">Учебник, с. 153</span>'
             '<h2>Grammar reference: -ing forms and to-infinitives</h2>'
             '<p><a href="theory.html#gr153">Правило — в разделе «Теория»</a></p>' + ing1() + ing2() +
             gloss(153, (440, 870, 748, 1045)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 98–103, 134–135</span>'
             '<h2>Итоговый тест по модулю 14</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.pc_nouns("t14-f1", "1", "Complete the sentences with the computer words in the box.") +
             X.article_tf("t14-f2", "2", "Decide if these sentences about the article <i>Here today, gone tomorrow!</i> are "
                                         "true or false.") +
             X.gadgets("t14-f3", "3") + X.ing_rules("t14-f4", "4") + X.ing_correct("t14-f5", "5") +
             X.film_adj("t14-f6", "6") + X.film_part("t14-f7", "7") + X.while_during("t14-f8", "8") + "</article>")
    toc = '<nav class="toc"><a href="#t153">-ing forms and to-infinitives</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
