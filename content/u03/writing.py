"""Страница «Письмо» модуля 03: своего урока письма у юнита нет, поэтому здесь Review 01, часть 1 — Revise together,
pp. 32–33 (повторение юнитов 1–4). Ключи — 01 Review (keys, с. 6)."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from keys import rows, numbered
from writing_map import note
from review import practice, sounds
from .shared import wordbox

IMG_DIR = "../assets/img/unit03/"

CELLS = [("/iː/", "cheek"), ("/ɪ/", "rip"), ("/ʊ/", "pull"), ("/uː/", "boots"), ("/e/", "upset"), ("/ə/", "gallery"),
         ("/ɜː/", "hurt"), ("/ɔː/", "sort"), ("/æ/", "bang"), ("/ʌ/", "hum"), ("/ɑː/", "spa"), ("/ɒ/", "loss")]
WORDS = ["exhausted", "confirm", "relief", "therapist", "marks", "due", "accent", "wonder", "attempt", "mosque", "skills",
         "bully"]
# ключ: cheek – relief, rip – skills, pull – bully, boots – due, upset – therapist, gallery – attempt, hurt – confirm,
# sort – exhausted, bang – accent, hum – wonder, spa – marks, loss – mosque
KEY = {"relief": "cheek", "skills": "rip", "bully": "pull", "due": "boots", "therapist": "upset", "attempt": "gallery",
       "confirm": "hurt", "exhausted": "sort", "accent": "bang", "wonder": "hum", "marks": "spa", "mosque": "loss"}

STRESS = ["At <u>lea</u>st you’re here <u>now</u>.", "<u>Fair</u> enough.", "I’m <u>sure</u> it’ll <u>sort</u> itself <u>out</u>.",
          "I <u>think</u> I’ll <u>join</u> you.", "It’s <u>not</u> <u>worth</u> it.", "A<u>part</u> from <u>that</u>",
          "<u>Not</u> as <u>much</u> as I <u>should</u>.", "When<u>ev</u>er I <u>get</u> the <u>chance</u>",
          "<u>Ten</u> years <u>on</u> and <u>off</u>.", "<u>On</u> in the <u>back</u>ground",
          "I <u>can’t</u> get it <u>out</u> of my <u>head</u>.", "It <u>does</u>n’t do <u>an</u>ything for <u>me</u>."]


def build():
    return note(3) + _build()


def _build():
    lt = SEC("Learner training", "",
             EX("r32-lt", "", "Work in groups of three. Discuss these questions:", UL([
                 "Do you write notes in your coursebook or do you use a separate exercise book? Why?",
                 "Compare the notes you have taken in the last few lessons. Are all of your notes similar? Discuss the reasons "
                 "for any differences.",
                 "What do you do with your notes after class? Tell each other any ideas you have about how to write and use "
                 "your notes better. Use these sentence starters:"]) +
                wordbox(["It’s important to…", "It’s best to…", "Don’t worry too much about…", "Make sure you…",
                         "It’s better to… than it is to…"])))
    game = SEC("Game", "",
               EX("r32-g", "", "Work in pairs. Student A use <i>only</i> the green squares; student B use <i>only</i> the "
                  "yellow squares. Spend 5 minutes looking at your questions and revising the answers. Then take turns tossing a "
                  "coin: Heads = move one of your squares; Tails = move two of your squares. When you land on a square, your "
                  "partner looks at the relevant page in the book to check your answers, but <i>you don’t</i>! If you are "
                  "right, move forward one space (but don’t answer the question until your next turn). If you aren’t right, "
                  "your partner tells you the right answer, and you miss a go. When you’ve finished the game, change colours "
                  "and play again.", IMG(IMG_DIR + "p32-game.jpg", "Game board")))
    cp = SEC("Conversation practice", "",
             practice("r33-cp", [("My first class", 9), ("Feelings", 15), ("Time off", 21), ("Interests", 27)]))
    act = SEC("Act or draw", "",
              EX("r33-ad", "", "One person should act or draw as many of these words as you can in three minutes. Your partners "
                 "should try to guess the words. Do not speak while you are acting or drawing!",
                 wordbox(["seat", "grab", "a ride", "restore", "hum", "court", "unfit", "prayer", "bang your head",
                          "can’t stand", "be stuck in a lift", "approach someone", "bully someone", "swim breaststroke",
                          "pull a muscle", "sign something", "split up", "score", "suntan", "a mine", "luggage", "warm up",
                          "whistle", "decorate", "hug", "kick", "ruins", "net", "bow", "shoot", "hurt", "lake"])))
    quiz = SEC("Quiz", "",
               EX("r33-q", "", "Answer as many of the questions as possible.", OL([
                   "What does <b>a head teacher</b> do?", "What’s the difference between <b>holding hands</b> and <b>shaking "
                   "hands</b>?", "Say two things you can <b>sort out</b>.", "How do you feel if you <b>get ripped off</b>? Why?",
                   "Why would you be <b>in a rush</b>? Why would you <b>rush</b> somebody to hospital?",
                   "Is it good to get <b>sunburnt</b>?", "Why would you <b>ignore</b> somebody?",
                   "Say three things people <b>boast</b> about.", "Say three things that can <b>break down</b>.",
                   "When do you need to <b>warm up</b>?", "What do you usually <b>get promoted</b> to?",
                   "Can you <b>hurt</b> a car?", "What’s the difference between <b>practise</b> and <b>play</b>?",
                   "Why might you <b>need cheering up</b>?", "Say two things that are often <b>due</b>."]) +
                  '<div class="writer" data-target="" data-id="u03-quiz"><textarea rows="6"></textarea></div>' +
                  REVEAL("<br>".join(numbered(rows(6, 0, 34, 55)) + numbered(rows(6, 1, 0, 9, split=63))),
                         "Возможные ответы (ключ)")))
    col = SEC("Collocations", "",
              EX("r33-c", "", "Take turns to read out collocation lists from unit 1 of the Vocabulary Builder. Where there is "
                 "a ‘~’, say ‘<i>blah</i>’ instead. Your partner should guess as many words as they can. Each time you change "
                 "roles, move to the next unit.", ""))
    tbl, pb = sounds("r33-pb", "B", "Add the words below to the appropriate box, according to how the underlined sounds are "
                     "pronounced.", CELLS, WORDS, KEY)
    pr = SEC("Pronunciation", "Vowel sounds",
             EX("r33-pa", "A", '<span class="audio-ic">♪</span> R 1.1 Listen and repeat the sounds and the words.', tbl) + pb +
             EX("r33-pc", "C", "Which sounds do you find hardest to pronounce?", ""))
    cs = SEC("Connected speech", "",
             EX("r33-ca", "A", '<span class="audio-ic">♪</span> R 1.2 Listen and say the sentences. The stressed sounds are '
                "marked for you.", OL(STRESS)) +
             EX("r33-cb", "B", "Work in pairs. Mark the expressions in exercise A in the following ways:",
                UL(["Mark where sounds disappear.",
                    "Mark where the consonant at the end of a word joins with the following vowel sound."])) +
             EX("r33-cc", "C", "Listen again and check your ideas with the audioscript on p. 163.",
                REVEAL("e = elision (the sound disappears), c = catenation (the consonant joins the following vowel sound).<br>" +
                       "<br>".join(rows(6, 1, 25, 37, split=63)[:12]), "Ключ")))
    p32 = PAGE_BOX(32, IMG(IMG_DIR + "p32-banner.jpg", "01 Review") + lt + game)
    p33 = PAGE_BOX(33, '<h2>Revise together</h2><p class="intro">For each of the activities below, work in groups of three. '
                       'Use the Vocabulary Builder if you want to.</p><div class="cols"><div>' + cp + act + quiz +
                   '</div><div>' + col + pr + cs + "</div></div>")
    return p32 + p33
