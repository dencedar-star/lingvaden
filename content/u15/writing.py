"""Страница «Письмо» модуля 15: своего урока письма у юнита нет (Writing 01–08 в учебнике восемь),
поэтому здесь Review 04, часть 1 — Revise together, pp. 116–117 (повторение юнитов 13–16). Ключи — 04 Review."""
from lib import G, EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit15/"

PHON = [("/ˈhɑːbə/", "harbour"), ("/refjuˈdʒiː/", "refugee"), ("/ɪɡˈzɔːstɪd/", "exhausted"), ("/ˈkɜːsə/", "cursor"),
        ("/ɪnˈfɪərɪə/", "inferior"), ("/ɔːtəˈmætɪkli/", "automatically"), ("/daɪəˈriːə/", "diarrhoea|diarrhea"),
        ("/daɪəˈbiːtiːz/", "diabetes"), ("/ˈhɒrəskəʊps/", "horoscopes"), ("/ˈdredfʊl/", "dreadful")]


def phonetic(id, letter="A", instr="Write the correct spelling for the words in phonetic script below."):
    """p. 117, Pronunciation A. Ключ: 1 harbour 2 refugee 3 exhausted 4 cursor 5 inferior 6 automatically 7 diarrhoea
    8 diabetes 9 horoscopes 10 dreadful."""
    return EX(id, letter, instr, OL([f'<span class="phon">{p}</span> → {G(a)}' for p, a in PHON]))


from writing_map import note as _wnote


def build():
    return _wnote(int("15")) + _build()


def _build():
    lt = SEC("Learner training", "",
             EX("r116-lt", "", "Work in groups of three. Read these ideas about different ways of improving your English outside "
                "of class. Then discuss the questions.", UL([
                    "What do you think are the advantages and disadvantages of each idea?",
                    "How are you planning to improve your English once your course has finished?"]) +
                '<div class="cols">' + "".join(f'<div class="note"><p>{t}</p></div>' for t in [
                    "Go and live in an English-speaking country for a while. Try and stay with a local family.",
                    "Listen to audio books, and if you can, read the books at the same time as you listen.",
                    "Buy a good grammar book and work through it.",
                    "Do a language exchange with a student learning your language."]) + "</div>"))
    game = SEC("Game", "",
               EX("r116-g", "", "Work in pairs. Student A use <i>only</i> the green squares; student B use <i>only</i> the "
                  "yellow squares. Spend 5 minutes looking at your questions and revising the answers. Then take turns tossing a "
                  "coin: Heads = move one of your squares; Tails = move two of your squares. When you land on a square, your "
                  "partner looks at the relevant page in the book to check your answers, but <i>you don’t</i>! If you are "
                  "right, move forward one space (but don’t answer the question until your next turn). If you aren’t right, "
                  "your partner tells you the right answer, and you miss a go. When you’ve finished the game, change colours "
                  "and play again.", IMG(IMG_DIR + "p116-game.jpg", "Game board")))
    cp = SEC("Conversation practice", "",
             EX("r117-cp", "", "Choose one of these <i>Conversation Practice</i> activities:",
                '<p><a href="../unit13/book.html#p93">Travel p. 93</a><br><a href="../unit14/book.html#p99">Technology p. 99</a>'
                '<br><a href="../unit15/book.html#p105">Injuries and Illness p. 105</a><br>'
                '<a href="../unit16/book.html#p111">News and Events p. 111</a></p>'
                "<p><b>Two of you should do the task. The third person should listen and then give a mark of between 1 and 10 "
                "for the performance. Explain your decision. Then change roles.</b></p>"))
    act = SEC("Act or draw", "",
              EX("r117-ad", "", "One person should act or draw as many of these words as you can in three minutes. Your partners "
                 "should try to guess the words. Do not speak while you are acting or drawing!",
                 X.wordbox(["a flat tyre", "slippery", "bumpy", "freezing", "filthy", "pour down", "a scanner", "GPS", "a cable",
                            "solar power", "socket", "a temperature", "dizzy", "a bump", "itchy", "sneeze", "insomnia",
                            "a talent show", "stitches", "celebrity", "karaoke", "a blog", "robbery", "athlete", "dictator"])))
    quiz = SEC("Quiz", "",
               EX("r117-q", "", "Answer as many of the questions as possible.", OL([
                   "Say four different kinds of <b>trip</b> you can go on.",
                   "When might people have to deal with <b>bureaucracy</b>?",
                   "What kind of things happen when you <b>suffer discrimination</b>?",
                   "When might you <b>get distracted</b>? By what?", "If a market is <b>saturated</b>, is it good?",
                   "What kind of things can <b>enjoy a revival</b>?", "Say three things the government might <b>subsidise</b>.",
                   "Say three things you can <b>run out of</b>.",
                   "What is the difference between having <b>a cold</b> and having <b>the flu</b>?",
                   "How could you <b>sprain</b> your wrist?", "What should you do if you get <b>a rash</b>?",
                   "Say three things that can be <b>addictive</b>.", "Who might <b>agree a ceasefire</b>? Why?",
                   "How many <b>star signs</b> can you name?", "Why do people get <b>made redundant</b>?"]) +
                  '<div class="writer" data-target="" data-id="u15-quiz"><textarea rows="6"></textarea></div>' +
                  REVEAL("<br>".join(rows(26, 0, 4, 34)), "Возможные ответы (ключ)")))
    col = SEC("Collocations", "",
              EX("r117-c", "", "Take turns to read out collocation lists from Unit 13 of the Vocabulary Builder. Where there is "
                 "a ‘~’, say ‘<i>blah</i>’ instead. Your partner should guess as many words as they can. Each time you change "
                 "roles, move on to the next unit.", ""))
    pr = SEC("Pronunciation", "Phonetic symbols", phonetic("r117-pa") +
             EX("r117-pb", "B", '<span class="audio-ic">♪</span> R 4.1 Listen to the words from exercise A. Practise saying '
                "them.", ""))
    spk = SEC("Speaking", "",
              EX("r117-s", "", "Work in pairs. Look at the pictures below. Discuss the different roles that animals play in our "
                 "lives. How do you feel about each one?", IMG(IMG_DIR + "p117-animals.jpg", "Animals", cls="md")))
    p116 = PAGE_BOX(116, IMG(IMG_DIR + "p116-banner.jpg", "04 Review") + lt + game)
    p117 = PAGE_BOX(117, '<h2>Revise together</h2><p class="intro">For each of the activities below, work in groups of three. '
                         'Use the Vocabulary Builder if you want to.</p><div class="cols"><div>' + cp + act + quiz +
                    '</div><div>' + col + pr + spk + "</div></div>")
    return p116 + p117
