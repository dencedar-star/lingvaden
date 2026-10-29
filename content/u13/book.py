"""Страница «Учебник»: Unit 13 Travel, pp. 92–97. Длинные тексты — из OCR и ключей."""
import re
from lib import G, EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, text, script, fixed, FIX
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit13/"

FIX[94] = [("forty years ago", "Forty years ago"), (" — ", " – "), ("--", "–")]
FIX[95] = [("scasick", "seasick"), ("‘The ship’s", "The ship’s"), ("rich family:", "rich family."),
           ("Unfortunately;", "Unfortunately,"), ("Personally speaking.", "Personally speaking,"), (" - ", " – "),
           (" — ", " – ")]
FIX[97] = [("SITUATION 1 ", ""), ("SITUATION 2 ", ""), ("SITUATION 3 ", ""), ("SITUATION 4 ", "")]
FIX[171] = FIX.get(171, []) + [("Oh nol", "Oh no!"), ("you arel", "you are!"), ("wrong turning I", "wrong turning. I"), ("take- off", "take-off"),
            (" - ", " – ")]
FIX[172] = FIX.get(172, []) + [("I €200!", "I: €200!"), ("1 wish", "I wish"), ("Sir, You’re", "Sir. You’re"), ("poor thing", "poor thing!"),
            (" - ", " – ")]


def br(lines):
    return "<br>".join(lines)


def _join(ps):
    """Склеивает абзацы, разорванные переходом в другую колонку."""
    out = []
    for p in ps:
        if out and not re.search(r"[.!?”]$", out[-1]):
            out[-1] += " " + p
        else:
            out.append(p)
    return out


def article():
    p1 = _join([fixed(94, p) for b in [(70, 700, 252, 1060), (252, 700, 455, 1060), (455, 700, 700, 1060)]
                for p in paras(94, b, indent=12)])
    p2 = _join([fixed(95, p) for b in [(70, 440, 275, 1045), (278, 700, 475, 1045), (482, 700, 705, 1045)]
                for p in paras(95, b, indent=12)])
    return ('<div class="article"><h3 class="art-title">Journey to a New Nation</h3>'
            '<p class="note-s"><b>Martin O’Neill</b> celebrates international migrants day and his own special anniversary.</p>'
            '<h4>Part 1</h4><div class="colum">' + "".join(f"<p>{p}</p>" for p in p1) + "</div>" +
            IMG(IMG_DIR + "p94-protest.jpg", "") +
            '<h4>Part 2</h4><div class="colum">' + "".join(f"<p>{p}</p>" for p in p2) + "</div>" +
            '<div class="cols">' + IMG(IMG_DIR + "p95-refugees.jpg", "") + IMG(IMG_DIR + "p95-boat.jpg", "") + "</div></div>")


def S131():
    return SCRIPT("13.1", "M = Maria, B = Belinda, A = Andre; L = Lara, K = Karen", script(171, (405, 340, 794, 1045)), "171")


def S133():
    return SCRIPT("13.3", "", script(172, (25, 65, 392, 1060)) + script(172, (392, 65, 794, 145)), "172")


def p92():
    spk = SEC("Speaking", "",
              EX("b92-sa", "A", "Work in pairs. Discuss what you think the words in bold mean.", OL([
                  "When was the last time you went on <b>a day trip</b>? Where did you go?",
                  "Does anyone you know ever go on <b>business trips</b>?",
                  "Have you ever been on <b>a shopping trip</b>, <b>a school trip</b> or <b>a hunting trip</b>? Where to? "
                  "What was it like?", "Do you usually <b>travel light</b>?",
                  "Do you know anyone who has <b>been travelling</b> for a few months? Where did they go?",
                  "What’s the longest <b>journey</b> you’ve ever taken?"]) +
                 REVEAL(br(rows(20, 0, 5, 13, split=56)), "Ответ (ключ)")) +
              EX("b92-sb", "B", "Now answer the questions in groups.", ""))
    voc = SEC("Vocabulary", "Ways of travelling and travel problems",
              X.travel_sort("b92-va") +
              EX("b92-vb", "B", "Work in pairs. Add two more words under each heading in the table.",
                 REVEAL("By train – railway, station, compartment<br>By ferry – boat, port, foot passenger<br>"
                        "By car – traffic jam, motorway, crossroads<br>By plane – passport control, crew, customs",
                        "Возможные ответы (ключ)")) +
              X.travel_nouns("b92-vc") +
              EX("b92-vd", "D", "Work in pairs. Look at the pictures. Discuss what is good and what is bad about each way of "
                 "travelling. Which way do you prefer? Why?", "<p>(See the pictures at the top of the page.)</p>"))
    return PAGE_BOX(92, IMG(IMG_DIR + "p92-banner.jpg", "13 Travel") +
                    '<div class="cols"><div>' + spk + '</div><div>' + IMG(IMG_DIR + "p92-transport.jpg", "") + "</div></div>" + voc)


def p93():
    akey = REVEAL(br(rows(20, 0, 37, 46, split=56)), "Ответ (ключ)")
    bkey = REVEAL("huge – queue; bumpy – flight; terrifying – experience / flight; slippery – roads; wrong – turning; "
                  "stupid – male driver; hurt – the speaker (wasn’t hurt)", "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two conversations about journeys.</p>' +
              EX("b93-la", "A", '<span class="audio-ic">♪</span> 13.1 Listen and answer the questions.', OL([
                  "How did the people in each conversation travel?", "What three problems did each have?"]) + akey) +
              EX("b93-lb", "B", "Can you remember what nouns in the listening texts these adjectives were used to describe? "
                 "Work in pairs to compare your ideas. Then listen again to check.",
                 X.wordbox(["huge", "bumpy", "terrifying", "slippery", "wrong", "stupid", "hurt"]) + bkey) +
              EX("b93-lc", "C", "Work in pairs. Discuss these questions:", UL([
                  "How long before your flight do you usually get to the airport? Why?", "Have you ever missed a flight? Why?",
                  "Has anything strange or scary ever happened to you while flying / driving?",
                  "Can you drive? What are your strong points and weak points as a driver?",
                  "Do you agree with Lara’s comments about male drivers?"])) + S131())
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">I got completely lost and ended up '
                'going round in circles for ages.<br>Whenever I drive, we end up arguing.<br>We got lost and ended up in the '
                'middle of nowhere.<br>A lot of ex-soldiers end up homeless. It’s awful!<br>If he keeps driving like that, '
                'he’ll end up dead!</p></div>')
    box = ('<div class="box"><p><b>A phrasal verb is a verb – <i>put, throw, take</i>, etc. – plus a particle like <i>up, off, '
           'out, down</i>, etc. Sometimes they are used instead of single word verbs. Phrasal verbs are more colloquial and '
           'informal than single word verbs.</b></p></div>')
    voc = SEC("Vocabulary", "Phrasal verbs", box + X.phrasal("b93-va") + X.particles("b93-vb") +
              EX("b93-vc", "C", "Write your own sentences using the phrasal verbs.",
                 '<div class="writer" data-target="" data-id="u13-phrasal"><textarea rows="5"></textarea></div>'))
    cp = SEC("Conversation practice", "",
             EX("b93-ca", "A", "Work in pairs. You are going to have a conversation about a terrible journey Student A has had. "
                "Student B: begin by asking, <i>‘So how was your journey?’</i> Then change roles.", ""))
    return PAGE_BOX(93, '<div class="cols"><div>' + IMG(IMG_DIR + "p93-trains.jpg", "") + lis +
                    IMG(IMG_DIR + "p93-airport.jpg", "") + '</div><div>' + patterns + voc + cp + "</div></div>")


def p94():
    spk = SEC("Speaking", "",
              EX("b94-sa", "A", "Check you understand the words in <b>bold</b>. Then work in pairs. Discuss these questions:",
                 UL(["Who would <b>stamp</b> your passport and why?",
                     "Have you ever had to get a <b>visa</b> to visit another country?",
                     "What <b>restrictions on immigration</b> might a country have?",
                     "Is there much <b>bureaucracy</b> in your country?", "Why do people <b>emigrate</b>?",
                     "Why might someone become a <b>refugee</b>?"]) +
                 REVEAL(br(rows(20, 1, 17, 29, split=57)), "Значения слов (ключ)")))
    read = SEC("Reading", "",
               EX("b94-ra", "A", "Read part 1 of the article about immigration and then answer the questions in pairs.", OL([
                   "What does the author say has changed about immigration? Do you agree?",
                   "Why does he think building fences can be hypocritical and useless? Do you agree?",
                   "What reasons does he give for emigration? Can you think of any examples of these reasons?"]) +
                  REVEAL(br(rows(20, 1, 31, 41, split=57)), "Ответ (ключ)")) +
               EX("b94-rb", "B", "Before you read part 2 of the article, look at the pictures and discuss in pairs:", OL([
                   "where you think the people were from.", "why you think they were escaping.",
                   "what dangers you think they faced.", "what happened to them in the end."])) +
               EX("b94-rc", "C", "Now read part 2 and find out the answers to 1–4 in exercise B for Mai Ho.",
                  REVEAL(br(rows(20, 1, 42, 49, split=57)), "Ответ (ключ)")) +
               article() +
               EX("b94-rd", "D", "All the words in <i>italics</i> in 1–7 were used in the article. Can you remember how they "
                  "were used?", OL([
                      "I <i>invested</i> all my savings to set up the business.", "The teacher <i>confiscated</i> my mobile phone.",
                      "The teacher <i>bribed</i> the kids with sweets to calm them down.",
                      "A lot of women still face sexual <i>discrimination</i>.", "I’ve <i>set up</i> my own website.",
                      "She was <i>elected</i> president last year.", "He got the job <i>thanks</i> to the school he went to."]) +
                  REVEAL(br(rows(21, 0, 1, 17, split=56)), "Ответ (ключ)")) +
               EX("b94-re", "E", "Who are the most famous immigrants into / emigrants from your country? What difference "
                  "have they made?", IMG(IMG_DIR + "p94-cuba.jpg", "", cls="md")))
    return PAGE_BOX(94, spk + read)


def p95():
    gr = SEC("Grammar", "Third conditionals", X.third_box("b95-ga") + X.third_match("b95-gb") +
             EX("b95-gc", "C", "Write an alternative ending to the second half of each sentence in exercise B.",
                '<div class="writer" data-target="" data-id="u13-third"><textarea rows="6"></textarea></div>') + HELP(152))
    return PAGE_BOX(95, gr + '<p class="note-s">Текст статьи (часть 2) — на с. 94, в задании Reading.</p>')


def p96():
    box = ('<div class="box"><p><b>A small group of adjectives contain the idea of <i>very</i>. For example, <i>terrified</i> '
           'means <i>very scared</i>. To make them stronger, we use <i>really</i> or <i>absolutely</i>, not <i>very</i>.</b></p>'
           '</div>')
    voc = SEC("Vocabulary", "Strong adjectives", box + X.strong_match("b96-va") +
              EX("b96-vb", "B", '<span class="audio-ic">♪</span> 13.2 Listen and check your answers.', "") +
              EX("b96-vc", "C", "Listen again. Mark the main stress in each of the adjectives in a–l.", "") +
              EX("b96-vd", "D", "Try to remember responses a–l. Test each other in pairs.",
                 "<p><b>Student A:</b> read out 1–6.<br><b>Student B:</b> close your book and say the responses. Then change "
                 "roles.<br><b>Student B:</b> read out 7–12.<br><b>Student A:</b> close your book and say the responses.</p>") +
              EX("b96-ve", "E", "Tell your partner as much as you can about any places you have been to that were: "
                 "<i>boiling / freezing / filthy / huge / fascinating / packed</i>.", ""))
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear four conversations about travel experiences.</p>' +
              EX("b96-la", "A", '<span class="audio-ic">♪</span> 13.3 Listen and answer the questions.', OL([
                  "Which strong adjectives do the speakers use?", "What are they describing?"]) +
                 REVEAL(br(rows(21, 0, 33, 40, split=56)), "Ответ (ключ)")) +
              X.mistakes("b96-lb", "B", "Listen again. Complete the phrases about the mistakes each person made. Why did they "
                         "do / not do these things?") +
              REVEAL(br(rows(21, 0, 42, 49, split=56)), "Почему (ключ)") + S133())
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>I bet</i></b></p><p>We often use <i>I bet</i> to '
              'respond to what people have told us. It means <i>I’m sure</i>.</p>' +
              DLG(("A", "<i>It was boiling.</i>"), ("B", "<i>Lucky you! I bet that was nice.</i>")) +
              DLG(("A", "<i>The town was absolutely dead at night.</i>"), ("B", "<i>I bet you’re glad you were only there for "
                                                                               "a day.</i>")) + "</div>")
    return PAGE_BOX(96, '<div class="cols"><div>' + voc + '</div><div>' + lis + native + "</div></div>" +
                    IMG(IMG_DIR + "p96-helsinki.jpg", ""))


def p97():
    box = ('<div class="box"><p><b>We use <i>should have / should not have</i> + past participle to talk about things that went '
           'wrong in the past. <i>Should have</i> explains good things you failed to do or that you were unable to do. '
           '<i>Should not have</i> explains things you did that were a bad idea.</b></p></div>')
    gkey = REVEAL(br(rows(21, 0, 52, 56, split=56) + rows(21, 1, 0, 20, split=57)), "Возможные ответы (ключ)")
    gr = SEC("Grammar", "Should have", box +
             EX("b97-ga", "A", "Work in pairs. Decide what actually happened in 1–8. Then use a third conditional to explain "
                "what would have been a better idea and why.", OL([
                    "I knew we should’ve taken the plane instead of the ferry.", "I should’ve worn something lighter.",
                    "He shouldn’t have been driving so fast in the rain.", "You should’ve read the instructions more carefully.",
                    "I knew we should’ve booked the tickets in advance.", "They should’ve told you about the party sooner.",
                    "His parents shouldn’t have left him on his own at home.",
                    "I shouldn’t have left my bag hanging from the back of my seat."]) +
                '<div class="writer" data-target="" data-id="u13-should"><textarea rows="6" placeholder="1 We took the ferry – '
                'if we’d gone by plane, …"></textarea></div>' + gkey) + HELP(152))
    dbox = ('<div class="box"><p><b>We use <i>it’s my / his fault</i> or <i>I blame myself / him</i> to say who caused a problem. '
            'We often use <i>should have</i> and the third conditional as well.</b></p></div>')
    dc = SEC("Developing conversations", "Blaming people", dbox + X.blame("b97-da"))
    sit = "".join(f'<div class="note"><h4>Situation {i + 1}</h4><p>{fixed(97, text(97, b))}</p></div>'
                  for i, b in enumerate([(26, 570, 195, 810), (207, 570, 375, 830), (384, 570, 552, 875),
                                         (562, 570, 736, 905)]))
    spk = SEC("Speaking", "",
              EX("b97-sa", "A", "Work in pairs. Discuss the situations below and decide who is to blame. Use <i>should have</i> "
                 "or third conditionals to explain why.", '<div class="cols">' + sit + "</div>") +
              EX("b97-sb", "B", "Work in pairs. Choose one of the situations. You are going to role-play the conversation. "
                 "Before you start, decide who will take which role and think about how you will try and blame the other "
                 "person.", IMG(IMG_DIR + "p97-cartoon.jpg", "Reasons it’s not your fault — 4 for $1.00", cls="md")))
    return PAGE_BOX(97, '<div class="cols"><div>' + gr + '</div><div>' + dc + "</div></div>" + spk)


def build():
    return p92() + p93() + p94() + p95() + p96() + p97()
