"""Страница «Тесты»: упражнения Grammar reference p. 146 (ключи — Grammar Reference, 07) и итоговый тест."""
from lib import G, C, EX, OL
from . import shared as X


def gr1():
    """After, once and when, Exercise 1. Ключ: 1 if 2 when 3 once 4 as soon as 5 as long as 6 finish 7 start 8 has finished."""
    rows = [f"I’ll phone you {C('if', 'when', 'if')} I can’t come to the meeting.",
            f"I’ll phone you {C('when', 'when', 'if')} I get home.",
            f"I’m going to have a holiday {C('once', 'once', 'if')} my final exams have finished. I deserve it!",
            f"I’m going to bed {C('as soon as', 'as soon as', 'if')} I get to the hotel.",
            f"If you’re strict with them, you’ll gain their respect – {C('as long as', 'as soon as', 'as long as')} you’re fair "
            "as well.",
            f"After I {C('finish', 'will finish', 'finish')} my master, I’m going to do a PhD.",
            f"I’m probably going to go to Canada to study English, before I {C('start', 'will start', 'start')} university.",
            f"I’m going to take a nice, long holiday once the course {C('has finished', 'finished', 'has finished')}."]
    return EX("t7-g1", "1", "Choose the correct word.", OL(rows))


FC = [("If you want to get a good grade, you’ll have to work a lot harder!",
       "If you want to get a good grade, you’ll have to work a lot harder!"),
      ("If he’ll find a job, he might move out.", "If he finds a job, he might move out."),
      ("If you won’t have your passport or some other kind of ID, they’ll refuse to register you on the course.",
       "If you don’t have your passport or some other kind of ID, they’ll refuse to register you on the course."),
      ("They told us if he skips any more classes, they’re going to throw him off the course.",
       "They told us if he skips any more classes, they’re going to throw him off the course."),
      ("Your students don’t behave better if you don’t set some clear rules.",
       "Your students won’t behave better if you don’t set some clear rules."),
      ("What you will do if you don’t get offered a place on a masters?",
       "What will you do if you don’t get offered a place on a masters?"),
      ("I won’t can finish this essay by tomorrow unless you give me some peace and quiet!",
       "I won’t finish this essay by tomorrow unless you give me some peace and quiet!"),
      ("You’ll fail the exam if you revise properly.", "You’ll fail the exam if you don’t revise properly.")]


def gr2():
    """First conditionals, Exercise 1. Ключ: 1 correct 2 If he finds a job 3 you don’t have 4 correct 5 won’t behave better
    6 What will you do if 7 I won’t finish this essay 8 if you don’t revise."""
    return EX("t7-g2", "2", "Decide which six sentences are incorrect. Write all the sentences correctly (copy the correct ones).",
              OL([f"{q}<br>{G(a, 'wide')}" for q, a in FC]))


def gr3():
    """Other conditional sentences, Exercise 1. Ключ: 1 borrow + need 2 feeling + miss 3 fail + re-take 4 be + cheat
    5 should stop + finding 6 be + working 7 become + leave 8 make sure + share."""
    rows = [f"You can always {G('borrow')} my notes from the lecture if you {G('need')} to.",
            f"If I’m not {G('feeling')} very well, I can always {G('miss')} the occasional lecture.",
            f"If you {G('fail')} the end-of-year exams, you have to {G('re-take|retake')} the whole year all over again!",
            f"In my opinion, you deserve to {G('be')} thrown out of university if you {G('cheat')} in an exam.",
            f"You {G('should stop')} drinking coffee if you’re {G('finding')} it difficult to get to sleep.",
            f"My personal tutor can {G('be')} quite strict if he thinks you’re not {G('working')} hard enough.",
            f"Revision can {G('become')} stressful if you {G('leave')} it till the last minute.",
            f"{G('Make sure')} you keep your valuables safe if you {G('share')} a flat or house."]
    box = X.wordbox(["be + working", "become + leave", "borrow + need", "be + cheat", "fail + re-take", "feeling + miss",
                     "make sure + share", "should stop + finding"])
    return EX("t7-g3", "3", "Complete the sentences with the pairs of verbs.", box + OL(rows))


def build():
    part1 = ('<article class="page" id="t146"><span class="page-no">Учебник, с. 146</span>'
             '<h2>Grammar reference: After, once, when · Conditionals</h2>'
             '<p><a href="theory.html#gr146">Правило — в разделе «Теория»</a></p>' + gr1() + gr2() + gr3() + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 48–53, 132–133</span>'
             '<h2>Итоговый тест по модулю 7</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.courses("t7-f1", "1") + X.dc_fix("t7-f2", "2") +
             X.listen71("t7-f3", "3", "Complete the questions from <i>Listening</i> 7.1 (Daniel and Paulina).") +
             X.bold_words("t7-f4", "4", "Match the words from the article <i>Learning to be happy</i> with their meanings.") +
             X.families("t7-f5", "5") + X.sts("t7-f6", "6") +
             X.conv72("t7-f7", "7", "Who is the main speaker in each conversation in <i>Listening</i> 7.2? There is one person "
                      "you do not need to use.") +
             X.verbs72("t7-f8", "8") + X.cond73("t7-f9", "9", "Complete the second half of each sentence from "
                                                 "<i>Listening</i> 7.3.") +
             X.first_cond("t7-f10", "10") + X.trends("t7-f11", "11") + X.as_such("t7-f12", "12") + "</article>")
    toc = '<nav class="toc"><a href="#t146">Grammar reference</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part1 + final
