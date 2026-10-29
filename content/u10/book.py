"""Страница «Учебник»: Unit 10 Going out, pp. 70–75. Длинные тексты — из OCR и ключей."""
import re
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, text, script, fixed, FIX
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit10/"

FIX.setdefault(73, []).extend([("Independiete", "Independiente"), (" - ", " – ")])
FIX.setdefault(168, []).extend([("1: Oh", "J: Oh"), ("8.307", "8.30?"), ("shall | just", "shall I just"),
                                ("Exactly, Maybe", "Exactly. Maybe"), ("but 1 really", "but I really"), (" - ", " – ")])
FIX.setdefault(169, []).extend([("A: 1 know", "A: I know"), ("C Oh dear", "C: Oh dear"), ("l’ve", "I’ve"),
                                ("bit.I mean", "bit. I mean"), (" - ", " – ")])

BOLD = ["authentic", "birthplace", "fusion", "catch", "squad", "exclusive", "crowd", "keen", "stroll", "cast"]

# пункты путеводителя: (заголовок, подзаголовок-область или None, область текста)
GUIDE = [("1 / Teatro Colón", (30, 414, 264, 452), (30, 462, 264, 625)),
         ("2 / Señor Tango", (30, 832, 264, 868), (30, 880, 264, 1045)),
         ("3 / La Boca", None, (268, 414, 502, 610)),
         ("4 / Boca Juniors vs. Independiente", (268, 702, 502, 722), (268, 735, 502, 850)),
         ("5 / Opera Bay", (268, 911, 502, 931), (268, 944, 502, 1045)),
         ("6 / Mundo Bizarro", None, (510, 110, 752, 196)),
         ("7 / La Chacra steakhouse", None, (510, 285, 752, 480)),
         ("8 / Avenida Florida", None, (510, 542, 752, 740))]


def _bold(s):
    for w in BOLD:
        s = re.sub(rf"\b{w}\b", f"<b>{w}</b>", s, count=1)
    return s


def guide():
    out = []
    for title, sub, body in GUIDE:
        h = f"<h4>{title}</h4>"
        if sub:
            h += f'<p><b>{fixed(73, " ".join(paras(73, sub, indent=10**6, gap=10**6)))}</b></p>'
        ps = [fixed(73, p) for p in paras(73, body, indent=10)]
        out.append(h + "".join(f"<p>{_bold(p)}</p>" for p in ps))
    return ('<div class="article"><h3 class="art-title">What’s on in Buenos Aires?</h3>' +
            IMG(IMG_DIR + "p73-header.jpg", "", cls="md") + '<div class="colum">' + "".join(out) + "</div>" +
            '<div class="cols">' + IMG(IMG_DIR + "p73-teatro.jpg", "Teatro Colón") + IMG(IMG_DIR + "p73-tango.jpg", "") +
            "</div></div>")


def S101():
    return SCRIPT("10.1", "D = Dan, J = Jason", script(168, (400, 145, 794, 405)), "168")


def S102():
    return SCRIPT("10.2", "D = Dan, J = Jason", script(168, (400, 448, 794, 900)), "168")


def S105():
    a = script(168, (400, 928, 794, 1050))
    sp, t = a[-1]
    a[-1] = (sp, t + " " + fixed(169, text(169, (0, 80, 397, 117))))   # реплика переходит на с. 169
    return SCRIPT("10.5", "", a + script(169, (0, 116, 397, 840)), "168–169")


def p70():
    voc = SEC("Vocabulary", "Films, exhibitions and plays", X.odd_one("b70-va") +
              EX("b70-vb", "B", "Work in pairs. Discuss these questions:", UL([
                  "How often do you go to the cinema / art exhibitions / the theatre?",
                  "What kind of films / art / theatre do you like?",
                  "Are there any films / exhibitions / plays on at the moment that you would like to see?"])) +
              X.whats_on("b70-vc") +
              EX("b70-vd", "D", "Work in pairs. Ask each other the questions in exercise C, but give your own answers about "
                 "things that are on in your town.", ""))
    return PAGE_BOX(70, IMG(IMG_DIR + "p70-banner.jpg", "10 Going out") + voc + IMG(IMG_DIR + "p70-sculpture.jpg", ""))


def p71():
    akey = REVEAL(OL(["a Brazilian horror film", "zombies taking over Brasilia", "9.10 p.m. and 12 midnight", "the Capitol"]),
                  "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two friends, Dan and Jason, making plans for the evening.</p>' +
              EX("b71-la", "A", '<span class="audio-ic">♪</span> 10.1 Listen to the first part of the conversation and answer '
                 "the questions.", OL(["What’s on?", "What’s it about?", "When’s it on?", "Where’s it on?"]) + akey) + S101() +
              EX("b71-lb", "B", '<span class="audio-ic">♪</span> 10.2 Listen to the rest of the conversation and answer the '
                 "questions.", OL(["Where is the cinema? Mark it on the map below.", "What time do they arrange to meet? Why?"]) +
                 IMG(IMG_DIR + "p71-map.jpg", "Map", cls="md") +
                 '<p class="note-s">Ответов к этому заданию в ключах нет — проверьте себя по аудиоскрипту 10.2.</p>') + S102())
    native = ('<div class="note"><h4>Native speaker English</h4><p>We use <b><i>right</i></b> before prepositional phrases to '
              'mean <i>exactly</i>.</p><p><i>It’s right in front of the main entrance.<br>It’s right behind you.<br>'
              'George Clooney was sitting right next to me!<br>We got to the theatre right on time.</i></p></div>')
    dc = SEC("Developing conversations", "Explaining where things are", X.directions("b71-da") +
             EX("b71-db", "B", "Work in pairs. Take turns to draw maps to illustrate each of the descriptions in exercise A. "
                "Explain what you are drawing. Do you agree the map is accurate?", ""))
    cp = SEC("Conversation practice", "",
             EX("b71-ca", "A", "Work in pairs. You are going to have a conversation similar to the one in <i>Listening</i>.",
                "<p><b>Student A:</b> invite your friend out tonight. Start by asking: <i>Do you fancy going to the cinema / "
                "an exhibition / the theatre?</i> Think about what you want to do and some details about it. Suggest where "
                "and when to meet.</p><p><b>Student B:</b> find out more about what your friend wants to do by asking "
                "<i>What’s on?</i> and other questions. Agree to go. Ask where it is exactly. Do not accept the first meeting "
                "time your partner suggests.</p>"))
    return PAGE_BOX(71, '<div class="cols"><div>' + IMG(IMG_DIR + "p71-friends.jpg", "") + lis + '</div><div>' + dc +
                    native + cp + "</div></div>")


def p72():
    box = ('<div class="box"><p><b>I haven’t seen</b> the new David Lynch movie, <b>but it’s supposed to be</b> quite weird.<br>'
           '<b>I haven’t heard</b> the new Snow Patrol CD, <b>but it’s supposed to be</b> quite dull.<br>'
           '<b>I haven’t been to</b> the Julie Freeman installation yet, <b>but it’s supposed to be</b> amazing.</p></div>')
    voc = SEC("Vocabulary", "Describing what’s on", X.adjectives("b72-va") +
              EX("b72-vb", "B", "Think of some films, plays, musicals, exhibitions, books, CDs or places that you do not "
                 "personally know, but that you could describe using some of the words in exercise A. Write sentences about "
                 "them using the patterns in the box.", box +
                 '<div class="writer" data-target="" data-id="u10-supposed"><textarea rows="4" placeholder="I haven’t seen …, '
                 'but it’s supposed to be …"></textarea></div>') +
              EX("b72-vc", "C", "Work in small groups. Tell the other students your ideas from exercise B. See if they have "
                 "heard similar things – or if they know the things / places and have different opinions about them.", ""))
    bkey = REVEAL(UL(["Spectacular – scenery and lighting in opera", "Incredible – dance (the tango)", "Trendy – bar",
                      "Terrific – cocktails", "Weird – décor", "Touristy – street", "Amazing – street life"]), "Ответ (ключ)")
    ckey = REVEAL(UL(["1908 was when the Teatro Colón was built.", "Luana DeVol is the American soprano in the opera "
                      "<i>Elektra</i>.", "The 19th century was when the tango was first created.",
                      "Broadway – no musical on Broadway (New York) is better than the show at Señor Tango.",
                      "Diego Maradona played for Boca Juniors and is one of the best-known footballers of all time.",
                      "You can’t wear trainers and jeans at Opera Bay, the city’s most exclusive disco.",
                      "The décor in the bar Mundo Bizarro is weird and wonderful.",
                      "The steak at La Chacra steakhouse is the best on earth.",
                      "They often don’t finish dinner until around midnight.",
                      "There are many different kinds of street performers in Avenida Florida."]), "Ответ (ключ)")
    read = SEC("Reading", "",
               '<p class="intro">You are going to read a page from a website about what is on in Buenos Aires, the capital of '
               'Argentina.</p>' +
               EX("b72-ra", "A", "Before you read, work in pairs. Discuss what you know about the city and the country. You "
                  "might need to use <i>It’s supposed to … / There’s supposed to be …</i>", "") +
               EX("b72-rb", "B", "Now read the text quickly. Find seven adjectives from <i>Vocabulary</i> exercise A. What do "
                  "they describe?", bkey) +
               EX("b72-rc", "C", "Read the page again more slowly. Then, work in pairs. Discuss what you remember about the "
                  "dates, times, people and things in the box below.",
                  X.wordbox(["1908", "Luana DeVol", "the 19th century", "Broadway", "artists", "Diego Maradona",
                             "trainers and jeans", "décor", "steak", "midnight", "street performers"]) + ckey) +
               X.bold_words("b72-rd") + X.bold_gaps("b72-re"))
    spk = SEC("Speaking", "", EX("b72-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "From what you have read, how do you think the nightlife in your city / town compares to Buenos Aires?",
        "Can you think of any places in your city / town that are similar to the places you read about? Do you ever go to any "
        "of them?"])))
    dc = SEC("Developing conversations", "Why you do not want to do things",
             '<div class="box"><p><b>When we are trying to arrange what to do and we are given different options, we usually '
             'explain why we don’t like certain ideas. We use several common expressions to do this.</b></p></div>' +
             X.expressions("b72-da") +
             EX("b72-db", "B", '<span class="audio-ic">♪</span> 10.3 Listen to check your answers. Then practise saying the '
                "expressions.", "") +
             EX("b72-dc", "C", "Work in pairs. Imagine you are staying in Buenos Aires for a couple of days. Look at the "
                "<i>What’s on in Buenos Aires</i> guide again. Decide which of the options sound good to you, and which do "
                "not. Then role-play a conversation deciding what you want to do. Reject options using some of the "
                "expressions from exercise A. Then discuss where and when to meet.", ""))
    return (PAGE_BOX(72, '<div class="cols"><div>' + voc + read + '</div><div>' + spk + dc + "</div></div>") +
            PAGE_BOX(73, guide()))


def p74():
    spk = SEC("Speaking", "", EX("b74-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Have you been out anywhere recently?", "Where did you go?", "How was it?"])))
    voc = SEC("Vocabulary", "Describing an event", X.event("b74-va") +
              EX("b74-vb", "B", "Decide if the answers could refer to a film, club, play, exhibition or gig. More than one "
                 "answer may be possible.", "") +
              EX("b74-vc", "C", "Work in pairs. Try to remember as much of the language in exercise A as you can.",
                 "<p><b>Student A:</b> ask <i>How was the …?</i><br><b>Student B:</b> close your book and give an appropriate "
                 "answer from exercise A.</p>") +
              EX("b74-vd", "D", "Tell each other about some films / clubs / plays / exhibitions you think are: <i>great / "
                 "overrated / moving / trendy / rubbish / weird</i>.", ""))
    pron = SEC("Pronunciation", "Intonation and lists",
               '<div class="box"><p><b>When we give our opinion about things we have seen, we often list what we liked or '
               'disliked. As we say a list of words, the intonation goes up on each word until the last one, when it goes '
               'down. We often finish these lists by adding <i>everything</i>.</b></p></div>' +
               EX("b74-pa", "A", '<span class="audio-ic">♪</span> 10.4 Listen to these lists and repeat them.',
                  '<p class="ex-line">It was great. The special effects, the soundtrack, everything!<br>It was awful. The music, '
                  'the venue, everything!<br>It was terrific. The acting, the scenery, everything!</p>') +
               EX("b74-pb", "B", "Work in pairs. Take turns saying these sentences.",
                  "<p><b>Student A:</b> ask <i>What was so good / bad about it?</i><br><b>Student B:</b> give the answer.</p>" +
                  OL(["The food, the service, everything. It was fantastic.",
                      "The people, the music, everything. It was just brilliant.",
                      "The story, the acting, everything. It was one of the worst things I’ve seen in a long time.",
                      "The music, the dancing, everything. It was dreadful.", "The hotel, the countryside, everything. It was great.",
                      "The weather, the place, everything. We had a great time.",
                      "The special effects, the soundtrack, everything. It was one of the best things I’ve seen in ages.",
                      "The scenery, the direction, everything. It was really bad."])) +
               EX("b74-pc", "C", "Work in pairs. What do you think the sentences in exercise B are describing?", "") +
               EX("b74-pd", "D", "Tell your partner about a great / terrible time you had on holiday / at a cinema / theatre / "
                  "restaurant / hotel / party, etc. Use the patterns in exercise B. Add some more details with other language "
                  "you have learned in this unit.", ""))
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">It was one of the worst things I’ve '
                'seen in a long time.<br>It was one of the best things I’ve seen in ages.<br>It’s one of the worst clubs I’ve '
                'ever been to.<br>He’s one of nicest people I’ve ever met.<br>It’s the nicest thing anyone’s ever done for me.'
                '<br>It’s the best book I’ve read in ages.</p></div>')
    return PAGE_BOX(74, '<div class="cols"><div>' + spk + voc + IMG(IMG_DIR + "p74-club.jpg", "", cls="md") +
                    '</div><div>' + pron + patterns + "</div></div>")


def p75():
    bkey = REVEAL(OL(["no; yes – because her boyfriend Hans was late and there was a long queue for the gig, so they went to a "
                      "club instead; yes – because her friend had a spare ticket for the theatre",
                      "yes – good film; no – awful club; yes – brilliant and moving play", "no; no; yes"]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear three conversations about what people did the previous night.</p>' +
              X.kinds("b75-la") +
              EX("b75-lb", "B", "Work in pairs. Discuss these questions about each of the conversations.", OL([
                  "Did they change their plans? Why?", "Did they enjoy the night? Why? / Why not?",
                  "Did their experience match what other people had said about the event?"]) + bkey) +
              EX("b75-lc", "C", "Listen and check.", "") + S105())
    box = ('<div class="box"><p><b>There are several ways of referring to future plans, promises or predictions that we made in '
           'the past. Usually, <i>am going to</i> becomes <i>was going to</i> and <i>will</i> becomes <i>would</i>.</b></p><hr>'
           '<p class="ex-line"><i>I was going to stay in, but a friend called me and so I ended up going out to see a play.<br>'
           'The film was much better than I thought it would be.</i></p></div>')
    akey = REVEAL(OL(["The original prediction was probably ‘I don’t think it will be very good.’", "I’ll pick you up at 7.",
                      "We aren’t going to get in.", "I’m going to stay in.", "I’ll go with you."]), "Ответы (ключ)")
    gr = SEC("Grammar", "The future in the past", box +
             EX("b75-ga", "A", "Look at these sentences from the three conversations in <i>Listening</i>. Work in pairs. "
                "Discuss what you think the original plan, promise, or prediction was.", OL([
                    "Brilliant – it was much better than I thought it would be.", "Hans had promised me he’d pick me up at 7.",
                    "We decided we weren’t going to get in.", "I thought you said you were going to stay in.",
                    "I said I’d go with her."]) + akey) +
             X.fip_gaps("b75-gb") + X.fip_rewrite("b75-gc") + HELP(149))
    spk = SEC("Speaking", "",
              EX("b75-sa", "A", "Check you understand the words in <b>bold</b>.", OL([
                  "Have you ever been <b>pleasantly surprised by</b> something? Why?",
                  "Have you ever been very <b>disappointed by</b> something? Why?",
                  "Can you think of a time you had a <b>last-minute change</b> of plan? What happened? Did it <b>turn out well "
                  "/ badly</b>?", "Can you think of any predictions that have <b>failed to come true</b>?",
                  "Have you ever <b>failed to keep a promise</b>? What happened?",
                  "Have your parents ever <b>promised to</b> do something and then not done it? How did you feel about it?",
                  "Has the government / local council in your country <b>broken</b> any of its <b>promises</b>? What did they "
                  "say they would do?"])) +
              EX("b75-sb", "B", "Work in groups. Discuss the questions and explain your answers using future forms in the past.",
                 IMG(IMG_DIR + "p75-cartoon.jpg", "", cls="md")))
    return PAGE_BOX(75, '<div class="cols"><div>' + lis + gr + '</div><div>' + spk + "</div></div>")


def build():
    return p70() + p71() + p72() + p74() + p75()
