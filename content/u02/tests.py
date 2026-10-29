"""Страница «Тесты»: упражнения Grammar reference pp. 138–139 (ключи — Grammar Reference, 02) и итоговый тест."""
from lib import S, C, EX, OL, DLG, REVEAL, IMG, INS2
from ocrtext import lines, fixed, _fix
from . import shared as X

IMG_DIR = "../assets/img/unit02/"
CI = ("Correct", "Incorrect")


def ci_rows(items):
    """Предложение, выбор «верно / неверно» и исправление из ключа."""
    out = []
    for s, fix in items:
        k = "Correct" if fix is None else "Incorrect"
        out.append(f"{s}<br>{C(k, *CI)}" + ("" if fix is None else " " + REVEAL(fix, "Исправление (ключ)")))
    return OL(out)


def bls1():
    items = [("It’s quite frustrating in the class. It sometimes seems as if I’m the only person who wants to study and learn.", None),
             ("He was in shock. Honestly, he looked as he’d seen a ghost!", "He looked as if he’d seen a ghost!"),
             ("She sounded like quite upset the last time I spoke to her.", "She sounded quite upset …"),
             ("I had to tell him the bad news. I felt as if terrible afterwards.", "I felt terrible afterwards."),
             ("I’ve only met him once, but he really annoyed me with the way he spoke about women. He seemed like an idiot to me.", None),
             ("Don’t eat that. It tastes like disgusting.", "It tastes disgusting."),
             ("She said the flight would cost €50 and the hotel €30 a night, which sounds like a really good deal.", None),
             ("Do you think this dress makes me look like fat?", "Do you think this dress makes me look fat?")]
    return EX("t2-bl1", "1", "Correct the sentences which are incorrect.", ci_rows(items))


EDING = [("Can you explain it again? I’m still a bit ", "confused", "."), ("The instructions for this camera are really ", "confusing", "."),
         ("He’s got a really ", "annoying", " habit of tapping the table with his finger all the time."),
         ("I’m a bit ", "annoyed", " that he hasn’t phoned me! He promised he’d ring me tonight."),
         ("This weather is really ", "depressing", "! It’s so wet."),
         ("He’s been ", "depressed", " for a while, but he refuses to go and see someone about it."),
         ("That film was so ", "scary", ". I jumped out of my seat about five times!"),
         ("I can’t look down. I’m ", "scared", " of heights!"),
         ("I’m ", "worried", " we’ll miss our flight."), ("The news of all these terrorist attacks is a bit ", "worrying", "."),
         ("I was really ", "surprised", " when I arrived here. I didn’t expect to see people living on the streets."),
         ("I thought the ending was really ", "surprising", ". I mean, I didn’t expect him to really be a ghost!"),
         ("I get really ", "frustrated", " when I can’t say what I want to say. It drives me mad!"),
         ("It’s quite ", "frustrating", " working there, because sometimes you know you could a better job, but you just don’t have time!"),
         ("It was so ", "boring", " that I fell asleep halfway through the film, so I didn’t see the end."),
         ("I’m ", "bored", "! Can’t we do something else?")]
PAIRS = ["annoyed / annoying", "frustrated / frustrating", "bored / boring", "surprised / surprising", "confused / confusing",
         "scared / scary", "depressed / depressing", "worried / worrying"]


def eding1():
    rows = []
    for i, (a, k, b) in enumerate(EDING):
        pair = next(p.split(" / ") for p in PAIRS if k in p.split(" / "))
        rows.append(f"<b>{i // 2 + 1}{'ab'[i % 2]}</b> {a}{S(k, pair)}{b}")
    box = '<div class="wordbox">' + "".join(f"<span>{p}</span>" for p in PAIRS) + "</div>"
    return EX("t2-ed1", "1", "Complete the pairs of sentences with the adjectives in the box.",
              box + '<ol class="items" style="list-style:none;padding-left:4px">' + "".join(f"<li>{r}</li>" for r in rows) + "</ol>")


def pc1():
    rows = [DLG(("A", "What are the hours like where you work?"),
                ("B", "OK. " + C("I usually just work", "I’m usually just working", "I usually just work") + " nine to five, but this month " +
                 C("I’m doing", "I’m doing", "I do") + " a lot of overtime because we’ve got a really tight deadline to meet, so " +
                 C("I’m working", "I’m working", "I work") + " from nine in the morning till nine at night or even ten most days.")),
            DLG(("A", "Where do you work?"),
                ("B", "Well, " + C("I normally work", "I’m normally working", "I normally work") + " in the centre of town, but this week " +
                 C("I’m working", "I’m working", "I work") + " from home, because " + C("they are doing up", "they do up", "they are doing up") +
                 " our office.")),
            DLG(("A", "What does your job involve exactly?"),
                ("B", "Just general office work, " + C("I answer", "I’m answering", "I answer") + " the phone and " +
                 C("make", "making", "make") + " appointments for my boss, that kind of thing, but " +
                 C("we’re holding", "we’re holding", "we hold") + " a conference in a couple of months, so at the moment " +
                 C("I’m sorting out", "I’m sorting out", "I sort out") + " lots of things for that as well."))]
    return EX("t2-pc1", "1", "Choose the correct form.", OL(rows))


def pc2():
    items = [("Can you phone back? I have dinner.", "I’m having dinner."), ("Ignore him. He’s just being silly.", None),
             ("Is she seeing anyone at the moment?", None), ("I’m annoyed with him. He’s still owing me money.", "He still owes me money."),
             ("I don’t need any help thanks. I just look.", "I’m just looking."), ("I go to the shops. Do you want anything?", "I’m going to the shops."),
             ("I’m preferring coffee, if you don’t mind.", "I prefer coffee, if you don’t mind."),
             ("I love cycling. I belong to a local cycling club.", None)]
    return EX("t2-pc2", "2", "Find the five mistakes and correct them.", ci_rows(items))


def pc3():
    rows = [
        INS2("I generally have lots of free time, but I’m studying really hard this month because I have exams.", "generally",
             ["Generally I have lots of free time, but I’m studying really hard this month because I have exams."]),
        INS2("I generally have lots of free time, but I’m studying really hard this month because I have exams.", "this month"),
        INS2("What are you doing these days? Are you still studying?", "these days"),
        INS2("What are you doing these days? Are you still studying?", "still"),
        INS2("I’m finding it quite difficult at home at the moment, because my husband normally does the cooking, but he’s away "
             "for three weeks on business.", "at the moment"),
        INS2("I’m finding it quite difficult at home at the moment, because my husband normally does the cooking, but he’s away "
             "for three weeks on business.", "normally"),
        INS2("I’m sorry, we’re currently experiencing problems with the system. Can you call back in a half an hour?", "currently"),
        INS2("They’re doing building work outside our office at the moment. Honestly, it’s driving me mad.", "at the moment"),
        INS2("I usually go to my dance class on Tuesdays, but I’m working so I’m going to miss it this week.", "usually"),
        INS2("I usually go to my dance class on Tuesdays, but I’m working so I’m going to miss it this week.", "this week"),
    ]
    labels = ["1", "1", "2", "2", "3", "3", "4", "5", "6", "6"]
    body = "".join(f'<div class="ins-wrap"><b>{n}</b> {r}</div>' for n, r in zip(labels, rows))
    return EX("t2-pc3", "3", "Complete these sentences by putting the words in brackets into the correct place. "
              '<span style="font-weight:400">Нажмите на место между словами, куда нужно вставить слово.</span>', body)


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip()
        if t.startswith("Glossary"):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part1 = ('<article class="page" id="t138"><span class="page-no">Учебник, с. 138</span>'
             '<h2>Grammar reference: be, look, seem · -ed / -ing adjectives</h2>'
             '<p><a href="theory.html#gr138">Правило — в разделе «Теория»</a></p>' + bls1() + eding1() +
             gloss(138, (50, 870, 345, 1000)) + "</article>")
    part2 = ('<article class="page" id="t139"><span class="page-no">Учебник, с. 139</span>'
             '<h2>Grammar reference: Present continuous / present simple</h2>'
             '<p><a href="theory.html#gr139">Правило — в разделе «Теория»</a></p>' + pc1() + pc2() + pc3() +
             gloss(139, (428, 920, 745, 1030)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 14–19, 122–123</span><h2>Итоговый тест по модулю 2</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.bls_match("t2-f1", "1") + X.collocations("t2-f2", "2") + X.ing_ed("t2-f3", "3") +
             X.pictures("t2-f4", "4", "Match 1–6 in exercise 3 to the people in the picture.", IMG(IMG_DIR + "p17-class.jpg", "")) +
             X.reading_adj("t2-f5", "5", "Which adjectives went with these nouns in the article <i>It only takes Juan Mann to change the world!</i>?") +
             X.listen_adj("t2-f6", "6", "Do the adjectives describe Sarah or Louise (Listening 2.3)?") +
             X.pc_gaps("t2-f7", "7") + X.double_q("t2-f8", "8") + X.double_match("t2-f9", "9") +
             X.starters("t2-f10", "10") + X.endings("t2-f11", "11", "Which endings could you use: in business emails, "
                                                    "in emails to acquaintances, in emails to close friends / family members?") +
             "</article>")
    toc = ('<nav class="toc"><a href="#t138">be, look, seem · -ed / -ing</a><a href="#t139">Present continuous</a>'
           '<a href="#final">Итоговый тест</a></nav>')
    return toc + part1 + part2 + final
