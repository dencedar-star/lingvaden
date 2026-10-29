"""Страница «Тесты»: упражнения Grammar reference p. 144 (ключи — Grammar Reference, 05) и итоговый тест."""
from lib import G, C, EX, OL, REVEAL
from ocrtext import lines, fixed, _fix
from . import shared as X

MIST = [("I’m really sorry, but you can’t to leave your car here.", "you can’t leave your car"),
        ("You’re really lucky that you don’t have to take work home with you.", None),
        ("She’s really behind with her work so she have to work late this evening.", "she has to work"),
        ("I don’t usually have to spend more than thirty minutes on lunch. I just don’t have time!", "I don’t usually spend more"),
        ("I’m so sorry I can’t go out with you all last night, but I have to start work really early this morning. I was up at "
         "five!", "I couldn’t go out … I had to start"),
        ("I left my last job because I have to travel too much. I missed my family.", "I had to travel"),
        ("Can you take your lunch break whenever you want?", None),
        ("I can’t come to the class next week. I have to take some important clients out for dinner.", None),
        ("Have you to wear any kind of uniform or can you wear what you like?", "Do you have to wear any")]


def ht1():
    rows = [f"{s} {C('mistake' if k else 'correct', 'correct', 'mistake')}" +
            (REVEAL(k, "Исправление (ключ)") if k else "") for s, k in MIST]
    return EX("t5-ht1", "1", "Correct the mistakes in six of the sentences below. <span style=\"font-weight:400\">Отметьте, есть "
              "ли ошибка; исправление — под ключом.</span>", OL(rows))


def ru1():
    rows = [f"{G('Are')} children allowed to watch this film?",
            f"I’m afraid students aren’t {G('allowed|permitted')} to log on to these computers. You have to go downstairs.",
            f"I {G('should')} really do 35 hours a week, but I often do less.",
            f"Smoking is not {G('allowed|permitted')} in any work area.",
            f"Slow down! You’re only supposed {G('to')} do sixty on this road. I hate it when you drive so fast.",
            f"I shouldn’t {G('really')} help you. It’s against the rules, but for you, I’ll make an exception.",
            f"We{G('’re|are')} not really supposed to let visitors in, but I’ll make an exception for you.",
            f"He can be a difficult guy to work for, but at least we’re {G('allowed')} to disagree with him!"]
    return EX("t5-ru1", "1", "Complete the sentences with one word in each space. Sometimes there is more than one possible "
              "answer.", OL(rows))


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
    part1 = ('<article class="page" id="t144a"><span class="page-no">Учебник, с. 144</span>'
             '<h2>Grammar reference: <i>have to, don’t have to, can</i></h2>'
             '<p><a href="theory.html#gr144">Правило — в разделе «Теория»</a></p>' + ht1() + "</article>")
    part2 = ('<article class="page" id="t144b"><span class="page-no">Учебник, с. 144</span>'
             '<h2>Grammar reference: Talking about rules</h2>'
             '<p><a href="theory.html#gr144">Правило — в разделе «Теория»</a></p>' + ru1() +
             gloss(144, (398, 845, 716, 1066)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 36–41, 128–129</span>'
             '<h2>Итоговый тест по модулю 5</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.jobs("t5-f1", "1") + X.ivan("t5-f2", "2", "Choose the words Ivan and Amanda used (<i>Listening</i> 5.1).") +
             X.workplaces("t5-f3", "3") + X.have_to("t5-f4", "4") +
             X.pic_jobs("t5-f5", "5", "Which jobs can you see in the pictures?") +
             X.rules_conv("t5-f6", "6", "Which of the rules did the speakers talk about in each conversation (<i>Listening</i> "
                          "5.3)?") +
             X.collocations("t5-f7", "7", "Match the words used in the conversations about rules at work.") +
             X.rules_choose("t5-f8", "8") +
             X.art_jobs("t5-f9", "9", "Which job in the article <i>Terrible jobs not a thing of the past</i> involves each "
                        "problem?") +
             X.art_words("t5-f10", "10") + X.used_to("t5-f11", "11") + X.programme("t5-f12", "12") +
             X.hab_rules("t5-f13", "13") + X.hab_complete("t5-f14", "14") + "</article>")
    toc = ('<nav class="toc"><a href="#t144a">Have to, don’t have to, can</a><a href="#t144b">Talking about rules</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
