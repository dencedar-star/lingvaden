"""Страница «Учебник»: Unit 03 Time off, pp. 20–25 (+ Information files pp. 156–158). Длинные тексты — из OCR и ключей."""
from lib import G, EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, text, lines, script, fixed, _fix, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit03/"

FIX[21] = [(" - ", " – "), ("nightlife", "nightlife.")]
FIX[22] = [("with 16", "with 16."), ("next on 39", "next on 39.")]
FIX[23] = [("cating", "eating"), ("cight", "eight"), (" - ", " – "), ("karoshi:", "<i>karoshi</i>:")]
FIX[156] = [(" - ", " – ")]
FIX[157] = [(" - ", " – ")]
FIX[158] = [("Pisa, or Sienna", "Pisa, Sienna")]
FIX[161] = FIX.get(161, [])
FIX[162] = [("€40.1 can", "€40. I can"), ("visit If", "visit if"), ("l might", "I might"), (" - ", " – "),
            ("Schindler’s List", "<i>Schindler’s List</i>")]

KRAKOW = ["Rynek Glowny", "Full-day tour to Auschwitz-Birkenau Museum", "Half-day tour to Wieliczka Salt Mine",
          "Full-day tour to the Tatras mountains", "Tour of Nowa Huta", "Alchemia", "Kazimierz", "St. Mary’s Church"]


def krakow():
    items = []
    for l in lines(21, (40, 880, 394, 1060)) + lines(21, (394, 825, 794, 1060)):
        t = fixed(21, _fix(l["t"])).strip()
        if t in KRAKOW:
            items.append([t, ""])
        elif items:
            items[-1][1] = (items[-1][1] + " " + t).strip()
    return ('<div class="article">' + IMG(IMG_DIR + "p21-krakow.jpg", "Kraków", cls="md") +
            '<div class="cols">' + "".join(f"<p><b>{n}</b><br>{d}</p>" for n, d in items) + "</div></div>")


def holiday_facts():
    out = []
    for l in lines(22, (430, 495, 700, 705)):
        t = fixed(22, _fix(l["t"])).strip()
        if t == "HOLIDAY FACTS":
            continue
        if t.startswith("•"):
            out.append(t.lstrip("• "))
        elif out:
            out[-1] += " " + t
    return '<div class="note"><h4>Holiday facts</h4>' + UL(out) + "</div>"


def article():
    first = fixed(23, text(23, (50, 135, 410, 372)))
    ps = [first] + [fixed(23, p) for p in paras(23, (50, 375, 410, 870), indent=30)]
    return ('<div class="article"><h3 class="art-title">Workers Can’t Bank on Holidays</h3><div class="colum">' +
            "".join(f"<p>{p}</p>" for p in ps) + "</div>" + IMG(IMG_DIR + "p23-traffic.jpg", "") + "</div>")


def roles():
    data = [("A", "Maggie", "a personal assistant (PA) from the UK", 156, (50, 205, 360, 410)),
            ("B", "Luca", "a civil servant from Italy", 157, (400, 205, 745, 380)),
            ("C", "Ethan", "a marketing manager from the United States", 158, (48, 220, 345, 390))]
    out = []
    for st, name, job, pg, box in data:
        t = fixed(pg, text(pg, box))
        out.append(REVEAL(f'<p class="note-s">Information files, p. {pg}</p><p>You are {name}, {job}. Read about your holidays '
                          f'and then discuss them with the other students. Answer the questions on p. 23.</p>'
                          f'<div class="story"><p>{t}</p></div>', f"Student {st}: {name} (p. {pg})"))
    return "".join(out)


def S31():
    return SCRIPT("3.1", "C = Claire, R = receptionist",
                  script(161, (397, 800, 794, 1060)) + script(162, (0, 80, 397, 400)), "161–162")


def S32():
    return SCRIPT("3.2", "C = Cristina, A = Andrew", script(162, (0, 400, 397, 1050)), "162")


def p20():
    spk = SEC("Speaking", "", EX("b20-sa", "A", "Work in pairs. Discuss the question.",
                                 "<p>What are the main tourist attractions locally / regionally / nationally?</p>"))
    voc = SEC("Vocabulary", "Places of interest", X.places("b20-va") + X.preps("b20-vb") +
              EX("b20-vc", "C", "Think of five towns / cities / areas in your country that contain places of interest. Choose "
                 "language from exercises A and B to describe the places of interest. Then work in pairs. Have conversations "
                 "like this:",
                 DLG(("A", "Have you ever been to …?"), ("B", "No, never. What’s it like?"),
                     ("A", "Oh, it’s great. There are some / lots of amazing … there. There’s a / an incredible / great … there."),
                     ("B", "Oh really? It sounds great."))))
    return PAGE_BOX(20, IMG(IMG_DIR + "p20-banner.jpg", "03 Time off") +
                    '<div class="cols">' + IMG(IMG_DIR + "p20-places1.jpg", "") + IMG(IMG_DIR + "p20-places2.jpg", "") + "</div>" +
                    spk + voc)


def p21():
    bkey = REVEAL("<p>" + " ".join(rows(3, 1, 17, 20, split=57)) + "</p><p>" + " ".join(rows(3, 1, 20, 24, split=57)) + "</p>", "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a conversation between a tourist and a hotel receptionist in Kraków, '
              'Poland.</p>' +
              EX("b21-la", "A", "Look at the places to visit in and around the city. Work in pairs. Decide which you would go "
                 "and see and why.", krakow()) +
              EX("b21-lb", "B", '<span class="audio-ic">♪</span> 3.1 Listen. Which of the things in Kraków are discussed? '
                 "What does the tourist, Claire, decide to do? Work in pairs and compare your ideas.", bkey) +
              X.recommend("b21-lc") + S31())
    dc = SEC("Developing conversations", "Recommendations", X.conv_order("b21-da") +
             EX("b21-db", "B", "Work in pairs. Practise reading the conversations.", ""))
    cp = SEC("Conversation practice", "",
             EX("b21-ca", "A", "Work in pairs. Role-play a conversation between a tourist and a hotel receptionist in the place "
                "where you live. When you have finished, change roles and start again.",
                "<p><b>Student A:</b> you are the tourist. You are thinking of going sightseeing. Ask for recommendations. "
                "Reject some before deciding on one.</p><p><b>Student B:</b> you are the hotel receptionist. Suggest some "
                "different places to the tourist. Explain why they are good.</p>"))
    return PAGE_BOX(21, '<div class="cols"><div>' + IMG(IMG_DIR + "p21-friends.jpg", "") + lis +
                    '</div><div>' + dc + cp + "</div></div>")


def p22():
    voc = SEC("Vocabulary", "Holiday problems", IMG(IMG_DIR + "p22-problems.jpg", "") +
              EX("b22-va", "A", "What problems are the people having in each of the pictures?", "") +
              X.problems("b22-vb") + EX("b22-vc", "C", "Have any of these things happened to you? When?", ""))
    ckey = REVEAL(OL([r[2:] for r in numbered(rows(4, 0, 11, 28))]), "Ответы (ключ)")
    read = SEC("Reading", "",
               '<p class="intro">You are going to read an article about public holidays and workers’ holiday entitlement in '
               'different countries. Note that public holidays are known as <i>bank holidays</i> in the UK.</p>' +
               EX("b22-ra", "A", "Work in pairs. Discuss these questions.", UL([
                   "How many public holidays are there where you live? Do you take all of them?",
                   "What is your favourite public holiday? Are there any you do not like? Why?",
                   "What did you do on the last public holiday?"])) +
               EX("b22-rb", "B", "Read these Holiday facts. Is there anything you find surprising? Why?", holiday_facts()) +
               article() +
               EX("b22-rc", "C", "Now read the article. Answer these questions.", OL([
                   "Why does the writer refer to the August bank holiday as an ‘annual horror show’?",
                   "What are the unions complaining about?", "What changes do the unions want?",
                   "What is <i>karoshi</i> and why is it mentioned?",
                   "What problems are caused by the high number of public holidays in Puerto Rico?"]) + ckey) +
               X.numbers("b22-rd", "D", "Work in pairs. What do these numbers in the article refer to?") +
               EX("b22-re", "E", "Work in small groups. Discuss these questions.", UL([
                   "Do you think the union is right? Why? / Why not?",
                   "Do you think your country needs more public holidays? Why? / Why not?"])))
    return PAGE_BOX(22, voc + read)


def p23():
    spk = SEC("Speaking", "",
              '<p class="intro">You are going to read different people’s experiences of the issues in the article.</p>' +
              EX("b23-sa", "A", "Work in groups of three. Student A, read about <b>Maggie</b> on p. 156. Student B, read about "
                 "<b>Luca</b> on p. 157. Student C, read about <b>Ethan</b> on p. 158.",
                 roles() + "<p><b>Don’t look back at the texts. Role-play a conversation asking and answering these "
                 "questions.</b></p>" + UL([
                     "What do you do?", "How much holiday do you get per year?",
                     "Is that the same for everyone in the UK / Italy / the US? Are you happy with what you get now?",
                     "Have you been away on holiday recently? Where did you go?"])) +
              EX("b23-sb", "B", "When you finish, discuss these questions.", UL([
                  "Is it OK to miss school to go on holiday?", "Whose last holiday was the best: Maggie’s, Luca’s or Ethan’s? Why?",
                  "Which of the three people is most like you?"])))
    box = ('<div class="box"><p><b>Look at this possible exchange from the role-play in <i>Speaking</i>.</b></p><hr>' +
           DLG(("A", "<i>Have you been</i> away on holiday recently?"),
               ("B", "Yes, I went camping in Tuscany. <i>Have you ever been</i> there?"), ("A", "No, never. What’s it like?")) +
           "<hr><p><b>To ask about general experiences before now, we often use the present perfect simple. Don’t just give a "
           "<i>Yes</i> or <i>No</i> answer – add a comment.</b></p></div>")
    answers = ["What’s it like?", "It’s supposed to be amazing.", "Several times.", "I’ve never really fancied it.",
               "I’d love to, though.", "It’s great. You should go.", "I wouldn’t go there, if I were you. It’s not worth it.",
               "… but I’m actually going to go there this summer.", "Have you? I’ve heard it’s quite nice."]
    gr = SEC("Grammar", "Present perfect questions", box +
             EX("b23-ga", "A", "Add <i>Yes</i> or <i>No, never</i> to the front of the following answers to the question "
                "<i>Have you (ever) been to X?</i>",
                OL([f"…… {a}" for a in answers]) + '<p class="note-s">Ответов к этому заданию в ключах нет.</p>') +
             HELP(140) +
             EX("b23-gb", "B", "Think of six places you have been to for which you would give the answers in exercise A. Write "
                "only the names of the places on a clean piece of paper.", "") +
             EX("b23-gc", "C", "Work in pairs. Swap your piece of paper with a partner. Ask <i>‘Have you been to …’</i> "
                "questions about the places on your partner’s list.", ""))
    return PAGE_BOX(23, '<div class="cols"><div>' + spk + '</div><div>' + gr + "</div></div>")


def p24():
    voc = SEC("Vocabulary", "Weather", X.weather("b24-va") +
              EX("b24-vb", "B", "Spend two minutes memorising the sentence endings in exercise A. Then work in pairs.",
                 "<p><b>Student A:</b> say 1–8<br><b>Student B:</b> close your book and say the endings.</p>") +
              EX("b24-vc", "C", "Work in pairs. Discuss these questions:", UL([
                  "Do you know what the forecast is for tomorrow / the weekend / next week?",
                  "Are there any bad times to visit where you live because of the weather? Why? And when is the best time to visit?",
                  "How many of the different kinds of weather in exercise A have you had in the last year?"])) +
              IMG(IMG_DIR + "p24-landscape.jpg", "", cls="md"))
    akey = REVEAL("<p>" + " ".join(rows(4, 0, 46, 50)) + "</p><p>" + " ".join(rows(4, 0, 50, 54)) + "</p>", "Ответ (ключ)")
    table = ('<table class="voc"><tr><th></th><th>Cristina</th><th>Andrew</th></tr>'
             '<tr><td><b>Plans</b></td><td>Italy, Sicily, holiday, beach, suntan, village on coast, Palermo</td>'
             '<td>Work, lunch with parents, picnic, beach</td></tr>'
             '<tr><td><b>Weather</b></td><td>Pour down, wet.</td><td>Hot, sunny, 27 degrees</td></tr></table>')
    tbl = ('<table class="voc"><tr><th></th><th>Cristina</th><th>Andrew</th></tr>'
           '<tr><td><b>Plans</b></td><td><div class="writer" data-target="" data-id="u03-cp"><textarea rows="2"></textarea></div></td>'
           '<td><div class="writer" data-target="" data-id="u03-ap"><textarea rows="2"></textarea></div></td></tr>'
           '<tr><td><b>Weather</b></td><td><div class="writer" data-target="" data-id="u03-cw"><textarea rows="2"></textarea></div></td>'
           '<td><div class="writer" data-target="" data-id="u03-aw"><textarea rows="2"></textarea></div></td></tr></table>')
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two English people discussing their plans for the coming Easter holiday. '
              'They also talk about the weather in Italy and the UK.</p>' +
              EX("b24-la", "A", "Before you listen, work in pairs. Discuss why the people might describe the weather as annoying "
                 "or worrying.", akey) +
              EX("b24-lb", "B", '<span class="audio-ic">♪</span> 3.2 Now listen and complete the table.',
                 tbl + REVEAL(table, "Ответ (ключ)")) + S32())
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">It depends on the weather.<br>'
                'It depends (on) whether it’s raining (or not).<br>It depends (on) how much it costs.<br>'
                'It depends (on) how far it is to walk.<br>It depends (on) how long it’ll take.<br>'
                'It depends (on) what time I get up.</p></div>')
    spk = SEC("Speaking", "", EX("b24-sa", "A", "Work in pairs. Discuss the question.",
                                 "<p>What is the most important thing for you when choosing a holiday? Why?</p>" + UL([
                                     "the countryside", "being near a beach or a pool", "the nightlife",
                                     "guaranteed good weather", "the local sights", "peace and quiet", "the history",
                                     "the food"])))
    return PAGE_BOX(24, '<div class="cols"><div>' + voc + '</div><div>' + lis + patterns + spk + "</div></div>" +
                    IMG(IMG_DIR + "p24-island.jpg", ""))


def p25():
    gr = SEC("Grammar", "The future",
             EX("b25-ga", "A", "We use lots of different forms to talk about the future. How many do you know?", "") +
             X.future_match("b25-gb") + HELP(141) + X.future_gaps("b25-gc"))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>at some point</i></b></p>'
              '<p>If you do something <i>at some point</i>, you do it at one moment, but you do not know when exactly.</p>'
              '<p><i>I need to go to the bank at some point today.<br>I’ll definitely see him at some point this week.<br>'
              'We went the wrong way at some point and got completely lost.</i></p></div>')
    disc = EX("b25-gd", "D", "Work in pairs. Discuss these questions.", UL([
        "Are you going away in the summer?", "Have you got any plans for the weekend?", "What are you doing after the class?",
        "Are you going to do anything for your birthday?", "Are you going to continue studying English after this course?",
        "What are you going to do after you leave school / graduate?", "Have you got any plans to change jobs?"]))
    spk = SEC("Speaking", "",
              EX("b25-sa", "A", "Look at the calendar at the bottom of the page.",
                 "<p><b>There is a public holiday on the Tuesday. You also have three days annual holiday till the end of the "
                 "year, so you could take more time off if you want. It might rain on Saturday or Sunday and be a bit chilly, "
                 "but it is going to clear up and get hotter during the week. Write in the calendar:</b></p>" + UL([
                     "two nice things you are going to do", "one other appointment.", "one thing you have got to do."]) +
                 "<p><b>Think about other things you might possibly do and when.</b></p>") +
              EX("b25-sb", "B", "Work in pairs. Role-play a conversation. Try to arrange to do something together during the "
                 "week. In the conversation, try to use some of the language you have learnt in this unit. Start by asking: "
                 "<i>So what are you doing …?</i>", IMG(IMG_DIR + "p25-calendar.jpg", "October calendar", cls="md")))
    return PAGE_BOX(25, '<div class="cols"><div>' + IMG(IMG_DIR + "p25-couple.jpg", "", cls="md") + gr +
                    '</div><div>' + native + disc + spk + "</div></div>")


def build():
    return p20() + p21() + p22() + p23() + p24() + p25()
