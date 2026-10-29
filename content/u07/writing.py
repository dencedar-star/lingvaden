"""Страница «Письмо» модуля 07: своего урока письма у юнита нет, поэтому здесь Review 02, часть 1 — Revise together,
pp. 60–61 (повторение юнитов 5–8). Ключи — 02 Review (keys, с. 13)."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from keys import rows, numbered
from writing_map import note
from review import practice
from .shared import wordbox

IMG_DIR = "../assets/img/unit07/"

# Pronunciation A: звук и два слова в каждой клетке (в учебнике подчёркнут нужный звук)
SOUNDS = [("/p/", "apply", "permanent"), ("/t/", "training", "tutor"), ("/tʃ/", "cheat", "overcharge"),
          ("/k/", "accounts", "contract"), ("/b/", "bland", "diabetic"), ("/d/", "discipline", "avoid"),
          ("/dʒ/", "gorgeous", "rigid"), ("/g/", "rug", "gig"), ("/f/", "afford", "fake"), ("/s/", "civil service", "juicy"),
          ("/l/", "label", "lecture"), ("/ʃ/", "sugary", "portion"), ("/v/", "venue", "woven"), ("/z/", "overseas", "raise"),
          ("/r/", "rep", "research"), ("/w/", "warehouse", "swear")]
CLUSTERS = ["trainers", "skip", "stripy", "squid", "grade", "bright", "swap", "pretty", "spread", "greasy", "brand",
            "playground"]


def build():
    return note(7) + _build()


def _build():
    lt = SEC("Learner training", "",
             EX("r60-lt", "", "Work in groups of three. Look at the different ways of revising vocabulary and then discuss the "
                "questions.", UL(["Do you do any of these things? Why / Why not?",
                                  "What do you think is good or bad about these ways?",
                                  "Have you got any other ways of learning vocabulary?"]) +
                wordbox(["I try to put new words into a story.", "I write an alphabetical list of single words and "
                         "translations.", "I put an expression on a card with the translation on the back.",
                         "I write new vocabulary on a paper and stick it on my fridge."])))
    game = SEC("Game", "",
               EX("r60-g", "", "Work in pairs. Student A use <i>only</i> the green squares; student B use <i>only</i> the "
                  "yellow squares. Spend 5 minutes looking at your questions and revising the answers. Then take turns tossing a "
                  "coin: Heads = move one of your squares; Tails = move two of your squares. When you land on a square, your "
                  "partner looks at the relevant page in the book to check your answers, but <i>you don’t</i>! If you are "
                  "right, move forward one space (but don’t answer the question until your next turn). If you aren’t right, "
                  "your partner tells you the right answer, and you miss a go. When you’ve finished the game, change colours "
                  "and play again.", IMG(IMG_DIR + "p60-game.jpg", "Game board")))
    cp = SEC("Conversation practice", "",
             practice("r61-cp", [("Working life", 37), ("Going shopping", 43), ("School and studying", 49), ("Eating", 55)]))
    act = SEC("Act or draw", "",
              EX("r61-ad", "", "One person should act or draw as many of these words as you can in three minutes. Your partners "
                 "should try to guess the words. Do not speak while you are acting or drawing!",
                 wordbox(["dirt", "stare", "pot", "carved", "price tag", "queue", "dust", "roast", "bracelet", "scruffy",
                          "hang", "a ferry", "bend over", "a warehouse", "starving", "stripy", "an outfit", "whisper", "slam",
                          "rotting", "trainers", "stew", "a gig", "an essay"])))
    quiz = SEC("Quiz", "",
               EX("r61-q", "", "Answer as many of the questions as possible.", OL([
                   "Why might you not be <b>accepted</b> on a course?", "If something is <b>tacky</b>, is it nice?",
                   "What might you <b>upgrade</b>, and why?", "Why might a school be described as <b>rough</b>?",
                   "What is the opposite of someone who is <b>very bright</b>?", "What are <b>postgraduate</b> courses?",
                   "If you work in <b>HR</b>, what do you do?", "What should you do if you <b>owe someone money</b>?",
                   "What is the difference between <b>it doesn’t suit you</b> and <b>it doesn’t fit</b>?",
                   "Say two things which might make food <b>off-putting</b>.",
                   "Why might a company or shop <b>go out of business</b>?",
                   "What is the problem if you work in <b>cramped conditions</b>?",
                   "Why might a drug be <b>taken off the market</b>?", "What do <b>pushy parents</b> do?",
                   "Name three things that are <b>fattening</b>."]) +
                  '<div class="writer" data-target="" data-id="u07-quiz"><textarea rows="6"></textarea></div>' +
                  REVEAL("<br>".join(numbered(rows(13, 0, 4, 34, split=60))), "Возможные ответы (ключ)")))
    col = SEC("Collocations", "",
              EX("r61-c", "", "Take turns to read out collocation lists from Unit 5 of the Vocabulary Builder. Where there is "
                 "a ‘~’, say ‘<i>blah</i>’ instead. Your partner should guess as many words as they can. Each time you change "
                 "roles, move to the next unit.", ""))
    tbl = '<table class="tbl sounds">' + "".join(
        "<tr>" + "".join(f'<td><span class="phon">{s}</span><br>{a}<br>{b}</td>' for s, a, b in SOUNDS[i:i + 4]) + "</tr>"
        for i in range(0, len(SOUNDS), 4)) + "</table>"
    pr = SEC("Pronunciation", "Consonant sounds",
             EX("r61-pa", "A", '<span class="audio-ic">♪</span> R 2.1 Listen and repeat the sounds and the words.', tbl) +
             EX("r61-pb", "B", "Which sounds do you find hardest to pronounce?",
                '<p>Notice that when you say <span class="phon">/p/, /t/, /f/, /tʃ/, /k/</span> and <span class="phon">/s/</span> '
                "it is important to push more air out of your mouth as you make the sound.</p>") +
             EX("r61-pc", "C", "A group of consonants at the start of a word is called a <i>consonant cluster</i>, such as "
                "<i>str</i> in <i>straight</i>. Always try to say these sounds very clearly when they are at the beginning of "
                "a word. If you make a pronunciation mistake here, it can be especially difficult for people to understand "
                "you. Try saying these words.", wordbox(CLUSTERS)) +
             '<p class="help">▶ Find this difficult? Try adding a short <span class="phon">/ə/</span> sound between the '
             "consonants and then speed up. People will still understand you.</p>")
    p60 = PAGE_BOX(60, IMG(IMG_DIR + "p60-banner.jpg", "02 Review") + lt + game)
    p61 = PAGE_BOX(61, '<h2>Revise together</h2><p class="intro">For each of the activities below, work in groups of three. '
                       'Use the Vocabulary Builder if you want to.</p><div class="cols"><div>' + cp + act + quiz +
                   '</div><div>' + col + pr + "</div></div>")
    return p60 + p61
