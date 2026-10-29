"""Страница «Письмо» модуля 11. Отдельного урока письма у юнита нет (к юнитам 9–12 относятся Writing 05–06, с. 128–131),
поэтому здесь — письменные задания из уроков юнита 11, а после них Review 03, часть 1 — Revise together, pp. 88–89
(повторение юнитов 9–12). Ключи — 03 Review (keys, с. 19)."""
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL
from keys import rows, numbered
from review import practice, sounds
from .shared import wordbox

IMG_DIR = "../assets/img/unit11/"


def writer(id, target, ph, rows=8):
    return (f'<div class="writer" data-target="{target}" data-id="{id}"><textarea rows="{rows}" placeholder="{ph}"></textarea>'
            '<div class="cnt"></div></div>')


from writing_map import note as _wnote


def build():
    return _wnote(int("11")) + _build() + review()


def _build():
    intro = ('<p class="note-s">В учебнике у юнита 11 нет отдельного урока письма: к блоку юнитов 9–12 относятся уроки '
             '<i>Writing 05 Suggesting changes</i> и <i>Writing 06 Reports</i> (с. 128–131). Здесь собраны письменные задания '
             'из уроков юнита 11.</p>')
    a = SEC("An animal story", "p. 77",
            EX("w11-a", "1", "Think of any strange or unusual animals you have seen – or any animals you have seen doing something "
               "strange. Write the story: where you were, what the animals were doing (use <i>-ing</i> clauses: <i>I suddenly "
               "saw a huge lizard lying on a rock</i>), how you felt and what happened in the end. Write 100–150 words.",
               writer("u11-w-story", "100–150", "It reminds me of something I once saw …")))
    b = SEC("Animals and the environment", "pp. 78–79",
            EX("w11-b", "2", "Write a short news article (80–120 words) about an endangered species or an environmental problem "
               "in your country. Use passives: <i>is threatened, are being hunted, was reintroduced, has been arrested</i>.",
               writer("u11-w-news", "80–120", "…")))
    c = SEC("A pet", "p. 81",
            EX("w11-c", "3", "Describe a pet that you or someone you know has. Answer the questions from <i>Speaking</i> A "
               "(Is it poisonous? What breed is it? Where do you keep it? What do you feed it? …). Write 80–120 words.",
               writer("u11-w-pet", "80–120", "My friend has got a …")))
    d = SEC("Language patterns", "p. 78",
            EX("w11-d", "4", "Write the sentences in your language. Then translate them back into English and compare your "
               "English to the original.",
               '<p class="ex-line">Mongolia is known as ‘the land of the horse’.<br>Shanghai is known as ‘the Paris of the '
               'East’.<br>The area is known for its oysters.<br>This rare species of shark is known to inhabit fresh water.</p>' +
               writer("u11-w-patterns", "", "…", 6)))
    return intro + PAGE_BOX("76–81", IMG(IMG_DIR + "p77-flamingos.jpg", "", cls="md") + a + b + c + d)


# ---------------- Review 03, часть 1 (pp. 88–89) ----------------
CELLS = [("/ɪə/", "weird"), ("/eə/", "spare"), ("/ʊə/", "rural"), ("/eɪ/", "safe"), ("/aɪ/", "tiger"), ("/ɔɪ/", "destroy"),
         ("/əʊ/", "crow"), ("/aʊ/", "power")]
WORDS = ["l<u>o</u>cated", "wh<u>a</u>le", "n<u>ow</u>adays", "sp<u>oi</u>lt", "sh<u>ar</u>ed", "t<u>ou</u>rist", "disapp<u>ear</u>",
         "h<u>i</u>de"]
# в ключах ответа нет; по подчёркнутым звукам: located – crow, whale – safe, nowadays – power, spoilt – destroy,
# shared – spare, tourist – rural, disappear – weird, hide – tiger
KEY = dict(zip(WORDS, ["crow", "safe", "power", "destroy", "spare", "rural", "weird", "tiger"]))


def review():
    lt = SEC("Learner training", "",
             EX("r88-lt", "", "Work in groups of three. Read the statements. Then discuss these questions:", UL([
                 "Which statements do you agree with? Why?", "Are you happy with your accent in English? Why? / Why not?",
                 "Which aspects of your pronunciation do you want to work on?"]) +
                '<div class="cols">' + "".join(f'<div class="note"><p>{t}</p></div>' for t in [
                    "When you look up words in the dictionary, write the pronunciation in phonetic script.",
                    "I want to keep my accent so people can hear where I am from.",
                    "It is important to practise saying individual sounds.",
                    "I prefer American accents to British accents.", "It is best to practise saying words together."]) +
                "</div>"))
    game = SEC("Game", "",
               EX("r88-g", "", "Work in pairs. Student A use <i>only</i> the green squares; student B use <i>only</i> the "
                  "yellow squares. Spend 5 minutes looking at your questions and revising the answers. Then take turns tossing a "
                  "coin: Heads = move one of your squares; Tails = move two of your squares. When you land on a square, your "
                  "partner looks at the relevant page in the book to check your answers, but <i>you don’t</i>! If you are "
                  "right, move forward one space (but don’t answer the question until your next turn). If you aren’t right, "
                  "your partner tells you the right answer, and you miss a go. When you’ve finished the game, change colours "
                  "and play again.", IMG(IMG_DIR + "p88-game.jpg", "Game board")))
    cp = SEC("Conversation practice", "",
             practice("r89-cp", [("Houses", 65), ("Going out", 71), ("The natural world", 77), ("People I know", 83)]))
    act = SEC("Act or draw", "",
              EX("r89-ad", "", "One person should act or draw as many of these words as you can in three minutes. Your partners "
                 "should try to guess the words. Do not speak while you are acting or drawing!",
                 wordbox(["halfway down", "an open fire", "an installation", "crawl around", "sweat like crazy", "smelly",
                          "a demonstration", "graffiti", "dull", "a gig", "a squirrel", "a cockroach", "stroke", "stay calm",
                          "a cage", "shy", "a patio", "in tears", "hiss", "a nest", "aggressive"])))
    quiz = SEC("Quiz", "",
               EX("r89-q", "", "Answer as many of the questions as possible.", OL([
                   "What is the opposite of a <b>cramped</b> flat?", "Say three things that can <b>drop dramatically</b>.",
                   "What kind of things happen in a <b>rough</b> area?", "Say three different kinds of <b>play</b>.",
                   "If a film is <b>terrific</b>, is it good?", "Why might you feel <b>out of place</b>?",
                   "What is the opposite of <b>breaking</b> a promise?", "What might you see <b>circling in the sky</b>?",
                   "Say three <b>endangered species</b>.", "Why might the police <b>search</b> a building?",
                   "Say two things people <b>exaggerate</b> about.", "What might kids do if they are <b>naughty</b>?",
                   "Say three things people <b>grow out of</b>.", "Why might two friends <b>fall out</b>?",
                   "How could you <b>track</b> someone <b>down</b>?"]) +
                  '<div class="writer" data-target="" data-id="u11-quiz"><textarea rows="6"></textarea></div>' +
                  REVEAL("<br>".join(numbered(rows(19, 0, 16, 46, split=57))), "Возможные ответы (ключ)")))
    col = SEC("Collocations", "",
              EX("r89-c", "", "Take turns to read out collocation lists from Unit 9 of the Vocabulary Builder. Where there is "
                 "a ‘~’, say ‘<i>blah</i>’ instead. Your partner should guess as many words as they can. Each time you change "
                 "roles, move on to the next unit.", ""))
    tbl, pb = sounds("r89-pb", "B", "Add the words below to the appropriate box, according to the way the underlined sounds are "
                     "pronounced.", CELLS, WORDS, KEY)
    pr = SEC("Pronunciation", "Diphthongs",
             EX("r89-pa", "A", '<span class="audio-ic">♪</span> R 3.1 Listen and repeat the sounds and words.', tbl) + pb +
             EX("r89-pc", "C", "Which sounds do you find hardest to pronounce?", ""))
    spk = SEC("Speaking", "",
              EX("r89-sa", "A", "Work in pairs. Look at the pictures below. Discuss what you think the two people in each picture "
                 "are talking about.", IMG(IMG_DIR + "p89-speaking.jpg", "Two pictures", cls="md")) +
              EX("r89-sb", "B", "Role-play the two conversations. Decide which roles you are each going to take. Spend five "
                 "minutes planning what you are going to say. Look back at "
                 '<a href="../unit09/book.html#p69">Unit 9 p. 69</a> and <a href="../unit12/book.html#p84">Unit 12 p. 84</a> '
                 "for ideas if you need to. Then have the conversations.", "") +
              EX("r89-sc", "C", "When was the last time you had conversations like these? Who with? What did you talk about?", ""))
    p88 = PAGE_BOX(88, IMG(IMG_DIR + "p88-banner.jpg", "03 Review") + lt + game)
    p89 = PAGE_BOX(89, '<h2>Revise together</h2><p class="intro">For each of the activities below, work in groups of three. '
                       'Use the Vocabulary Builder if you want to.</p><div class="cols"><div>' + cp + act + quiz + col +
                   '</div><div>' + pr + spk + "</div></div>")
    return p88 + p89
