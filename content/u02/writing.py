"""Страница «Письмо»: Writing 02 Short emails, pp. 122–123."""
import re
from lib import S, EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from ocrtext import paras, fixed, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit02/"
FIX[122] = [("Hi Thorsten -", "Hi Thorsten –"), ("Many thanks, Oliver", "Many thanks,<br>Oliver"),
            ("All the best. Melanie", "All the best,<br>Melanie"), ("Cheers for now, Davorka", "Cheers for now,<br>Davorka"),
            ("27” and", "27<sup>th</sup> and"), ("27” ", "27<sup>th</sup> "), (" - ", " – ")]

# варианты для пропусков в письмах: начало «Just a quick note» + концовки из упражнения A
OPTS = [f"Just a quick note {k} {e}" for k, a, b in X.PAIRS for e in (a, b)]
EMAIL_KEY = [OPTS[8], OPTS[2], OPTS[12]]  # e1, b1, g1 — ключ C: 1 to ask … 2 to say I’m sorry … 3 to say congratulations


def email(n, box):
    ps = [fixed(122, p) for p in paras(122, box, indent=10**6, gap=1.2)]
    head, body, rest = ps[0], ps[1], ps[2:]
    body = re.sub(r"^[.…\s]+", "", body)
    return (f'<div class="story"><p><b>{n}</b> &nbsp;{head}</p><p>{S(EMAIL_KEY[n - 1], OPTS)} {body}</p>'
            + "".join(f"<p>{p}</p>" for p in rest) + "</div>")


def build():
    spk = SEC("Speaking", "", EX("w2-s", "", "Work in pairs. Discuss these questions:", UL([
        "How often do you check your email?", "How many emails a day do you think you send?",
        "Who do you write to most often?", "Do you ever send emails in English? Who to? Why?"])))
    table = ('<table class="voc"><tr><td>Just a</td><td>quick<br>short</td><td>one<br>note<br>email</td>'
             '<td>' + "<br>".join(X.STARTERS) + "</td></tr></table>")
    box = ('<div class="box"><p><b>We generally begin emails with a line explaining why we are writing. To people we already '
           'know, we often begin with sentence starters like this:</b></p></div>' + table)
    ckey = REVEAL(OL([r[2:] for r in numbered(rows(27, 1, 16, 23, split=56))]), "Ответы (ключ)")
    wr = SEC("Writing", "Explaining why you are writing", box +
             X.starters("w2-wa") +
             EX("w2-wb", "B", "Work in pairs. Write one more possible ending for each of the seven sentence starters in the box.", "") +
             EX("w2-wc", "C", "Complete the three emails by adding the correct whole sentences from exercise A.",
                email(1, (405, 205, 758, 425)) + email(2, (405, 450, 758, 690)) + email(3, (400, 720, 758, 945)) + ckey))
    spk2 = SEC("Speaking", "", EX("w2-s2", "", "Work in pairs. Discuss these questions:", UL([
        "Have you ever lost anyone’s contact details? How? Did you manage to get them back again?",
        "Have you ever been to a wedding? When? Whose?"])))
    gbox = ('<div class="box"><p><b>When we add information to a sentence using <i>and / or</i>, we often leave words out if '
            'they have already been used. We assume the missing words are understood by the reader.</b></p><hr>'
            '<p class="ex-line">I hope this is OK with you and (I hope this) won’t cause too many problems.</p></div>')
    akey = REVEAL(OL([r[2:] for r in rows(27, 1, 26, 30, split=56)]), "Ответы (ключ)")
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(27, 1, 32, 46, split=56))]) +
                  '<p class="note-s">В ключе в п. 5 другие названия городов (Prague, Bratislava), чем в учебнике.</p>',
                  "Ответы (ключ)")
    groups = [["We left Sydney on Friday night.", "We arrived in Hong Kong on Saturday morning."],
              ["I really want to send one of the photos to my mum.", "I want to burn some of the other photos onto a CD."],
              ["Don’t worry about missing class tomorrow.", "Don’t worry about taking time off if you need to."],
              ["Don’t feel you have to wear a suit to the party tonight.", "Don’t feel you have to bring a present."],
              ["I am going to Rome tomorrow.", "I am going to Pisa on Friday, so I won’t be at the meeting on Thursday.",
               "I won’t be at work for the rest of this week."],
              ["I thought the story was great.", "I thought the acting was really good, but I didn’t really like the ending.",
               "I didn’t really like some of the songs."]]
    gr = SEC("Grammar", "Leaving out words", gbox +
             EX("w2-ga", "A", "Decide which words have been left out of sentences 1–4.", OL([
                 "I’m planning to come to Germany next month on business and really need to contact Matthias Einhoff before I arrive.",
                 "I’ll talk to Rose on Thursday and ask her what I missed, but please let me know if there’s anything urgent I need "
                 "to do or know about before then.",
                 "I’ve got my exams coming up next month and am already really worried about them.",
                 "Have you changed your mobile or lost it or something?"]) + akey) +
             EX("w2-gb", "B", "Rewrite each of the groups of sentences below as one sentence. Link your ideas using <i>and / or</i>. "
                "Leave out any words you think are unnecessary.",
                OL([" ".join(g) + '<div class="writer" data-target="" data-id="u02-lo' + str(i) + '"><textarea rows="2"></textarea></div>'
                    for i, g in enumerate(groups, 1)]) + bkey))
    vbox = ('<div class="box"><p><b>The way we end emails depends on who we are writing to. Some endings are more common for '
            'formal emails; some are more common for informal ones.</b></p></div>')
    voc = SEC("Vocabulary", "Ending emails", vbox + X.endings("w2-va") +
              EX("w2-vb", "B", "Work in pairs. Think of the letters and emails that you send. Which endings in exercise A could "
                 "you use if you wrote them in English? Say as much as you can about who the emails are to, and which endings "
                 "you would use.", ""))
    pr = SEC("Practice", "", EX("w2-p", "", "Write four short emails. Begin each one with a sentence from <i>Writing: explaining "
                                "why you are writing</i>. Try to write two informal emails, and two more formal ones. Use as much "
                                "of the language from these pages as you can.",
                                "".join(f'<div class="writer" data-target="" data-id="u02-email{i}"><textarea placeholder="Hi … / Dear …">'
                                        '</textarea><div class="cnt"></div></div>' for i in range(1, 5))) +
             IMG(IMG_DIR + "p123-prague.jpg", ""))
    p122 = PAGE_BOX(122, IMG(IMG_DIR + "p122-banner.jpg", "02 Writing — Short emails") +
                    spk + wr)
    p123 = PAGE_BOX(123, '<div class="cols"><div>' + spk2 + gr + '</div><div>' + voc + pr + "</div></div>")
    return p122 + p123
