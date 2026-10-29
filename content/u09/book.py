"""Страница «Учебник»: Unit 09 Houses, pp. 64–69. Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import text, fixed, FIX
from keys import rows, numbered
from u07.ocrx import script2, col_paras
from . import shared as X

IMG_DIR = "../assets/img/unit09/"

FIX.setdefault(67, []).extend([("supply. which", "supply, which"), ("housing. particularly", "housing, particularly"),
                               (" - ", " – "), ("homes —", "homes –")])
FIX.setdefault(69, []).extend([(" - ", " – ")])
FIX.setdefault(167, []).extend([(" - ", " – ")])
FIX.setdefault(168, []).extend([("forward tol", "forward to!"), ("them! it has", "them! It has"), ("A: 1 know", "A: I know"),
                                ("C: 1 live", "C: I live"), ("after a while.", "after a while,"), (" - ", " – ")])
HEADS = ("No place like home", "The shape of things to come?", "The roots of the problem", "Top-down solutions",
         "And bottom-up ones")
BOLD = ["noisy", "taking advantage of", "mortgages at low interest rates", "dramatic price rises", "as investments",
        "tackling the problem", "protect the environment", "huge increase in", "buying second homes"]


def article():
    html = ""
    for p in col_paras(67, [(30, 638, 212, 1050), (210, 638, 380, 835), (380, 160, 568, 835), (566, 460, 745, 840)], heads=HEADS):
        if p.startswith("#"):
            html += f"<h4>{p[1:]}</h4>"
        else:
            html += "<p>" + p.replace(" At present, the housing", "</p><p>At present, the housing") + "</p>"
    for w in BOLD:
        html = html.replace(w, f"<b>{w}</b>", 1)
    return ('<div class="article"><h3 class="art-title">Priced out of the market</h3>' +
            '<div class="cols">' + IMG(IMG_DIR + "p67-flats.jpg", "") + IMG(IMG_DIR + "p67-signs.jpg", "", cls="sm") + "</div>" +
            f'<div class="colum">{html}</div>' + IMG(IMG_DIR + "p67-photos.jpg", "") + "</div>")


def S91():
    return SCRIPT("9.1", "G = Gavin, L = Lynn", script2([(167, (397, 830, 794, 1060)), (168, (0, 70, 397, 395))], "GL"), "167–168")


def S93():
    return SCRIPT("9.3", "", script2([(168, (0, 425, 397, 1050))], "ABCD"), "168")


def p64():
    voc = SEC("Vocabulary", "Describing where you live", X.features("b64-va", "A", "Which of the words in the box can you see in "
                                                                     "the pictures?") +
              EX("b64-vb", "B", "Work in pairs. Which of the things in exercise A have you got where you live? Are there any "
                 "things you are happy not having?", "") +
              X.meanings("b64-vc", "C", "Use the extra information in sentences 1–10 to guess the meanings of the words in "
                         "<b>bold</b>. Translate the sentences into your language.") +
              EX("b64-vd", "D", "Work in pairs. Discuss which of the words above describe your home.", ""))
    return PAGE_BOX(64, IMG(IMG_DIR + "p64-banner.jpg", "09 Houses") + voc + IMG(IMG_DIR + "p64-house.jpg", "A house"))


def p65():
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">The flat needs a lot of work (to be) '
                'done on it.<br>It needs a lot of money (to be) spent on it.<br>The oven needs a good clean. It’s really dirty.<br>'
                'It needs a new coat of paint.<br>The roof needs fixing. It leaks in heavy rain!<br>It does work. The batteries '
                'just need replacing.</p></div>')
    akey = REVEAL(OL([r[2:] for r in numbered(rows(14, 0, 27, 35))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two people, Gavin and Lynn, talking about their friends’ new flat.</p>' +
              EX("b65-la", "A", '<span class="audio-ic">♪</span> 9.1 Listen and answer the questions.', OL([
                  "Why did Nick and Carol move?", "What is nice about their new place?", "What are the problems with the new place?",
                  "In what way was their old place better?"]) + akey) +
              X.endings("b65-lb", "B", "Look at the sentence beginnings from the conversation you listened to. Discuss in pairs "
                        "how each sentence ended. Then listen to the conversation again and check.") +
              EX("b65-lc", "C", "In groups, discuss these questions.", UL([
                  "Do you like the sound of Nick and Carol’s new place?", "How many times have you moved in your life? Why?",
                  "Have you ever done any work on your place? What?", "Have you ever shared a room? How was it?"])) + S91())
    pbox = ('<div class="box"><p><b>In the conversation, Gavin said that Nick and Carol’s flat ‘<i>does</i> need a bit of work done '
            'on it, but they’ve actually bought it’.</b></p><hr><p><b>We can add emphasis to sentences by either adding the '
            'auxiliaries <i>do, does</i> or <i>did</i> – or by stressing the auxiliary verb already there.</b></p></div>')
    pkey = REVEAL(" ".join(rows(14, 0, 49, 54)), "Ключ к рамке")
    pron = SEC("Pronunciation", "Adding emphasis with auxiliaries", pbox + pkey +
               EX("b65-pa", "A", "Work with a partner. Which auxiliaries in the sentences below do you expect to be stressed?", OL([
                   "‘I do like Paris. I just don’t want to live there.’", "‘The kitchen’s lovely, but it does need a good clean!’",
                   "‘I did visit their flat once, but it was a long time ago.’",
                   "‘They did send me their new address, but I’ve lost it.’", "‘It isn’t very central, but it is very affordable.’",
                   "‘I have been there. I’ve just forgotten the way.’", "‘They’ve got a huge flat, but it is a bit dark inside.’",
                   "‘It’s quite run-down, but it has got potential.’"])) +
               EX("b65-pb", "B", '<span class="audio-ic">♪</span> 9.2 Listen and practise saying the sentences.', ""))
    dbox = ('<div class="box"><p><b>We often describe how large places are by making comparisons with places that the listener '
            'knows.</b></p><hr><p class="ex-line">The lounge is <i>huge – it’s twice the size of</i> this room.<br>It’s got a '
            '<i>great</i> kitchen – <i>it’s a similar size to</i> yours, maybe a bit bigger.<br>Her garden’s <i>nice – it’s about '
            'the same size as</i> mine.</p></div>')
    dc = SEC("Developing conversations", "Making comparisons", dbox + X.sizes("b65-da") +
             EX("b65-db", "B", "Tell a partner how big the rooms are where you live.", ""))
    cp = SEC("Conversation practice", "",
             EX("b65-ca", "", "Think of the flat or house of someone you know and have similar conversations to the one you heard "
                "in <i>Listening</i>. Start the conversation like this:",
                DLG(("A", "Did I tell you I went round to see X the other day?"),
                    ("B", "No, you didn’t. How is she / he? I haven’t seen her / him for ages."))))
    return PAGE_BOX(65, '<div class="cols"><div>' + IMG(IMG_DIR + "p65-building.jpg", "") + patterns + lis +
                    '</div><div>' + pron + dc + cp + "</div></div>")


def p66():
    table = ('<table class="voc"><tr><td rowspan="2">Unemployment has<br>House prices have</td><td>risen<br>increased<br>gone up</td>'
             '<td>dramatically<br>a lot<br>steadily<br>slightly</td><td rowspan="2">over the past few months.<br>over the last '
             'few years.<br>over the past ten years.<br>since last year.</td></tr><tr><td>gone down<br>dropped<br>fallen</td>'
             '<td>a bit<br>by 15%</td></tr></table>')
    voc = SEC("Vocabulary", "Describing changes",
              '<div class="box"><p><b>We often talk about changes using verbs in the present perfect. We add adverbs to describe '
              'the degree of change. Look at these examples.</b></p>' + table + "</div>" + IMG(IMG_DIR + "p66-room.jpg", "", cls="sm") +
              EX("b66-va", "A", "Decide how the things in the box have changed in your country from the past to now. Choose "
                 "adverbs and time expressions to add more details.",
                 X.wordbox(["Unemployment", "House prices", "The average wage", "Petrol prices", "The divorce rate", "Food prices",
                            "The crime rate", "Interest rates", "The birth rate", "Taxes"])) +
              EX("b66-vb", "B", "Look at the comments below. Which changes in exercise A could the speakers be discussing?", UL([
                  "It’s because there’s an election next year.", "I think it’s happened because of problems in the economy.",
                  "I guess it might be because there aren’t enough homes.",
                  "It’s probably a result of having more police on the street.", "It has something to do with rising oil prices.",
                  "I think it has something to do with the fact that people have to work long hours."])) +
              EX("b66-vc", "C", "Work in pairs. Ask and answer questions about changes in your country using the language in "
                 "exercises A and B. For example:",
                 DLG(("A", "Why do you think the crime rate has fallen over the last few years?"),
                     ("B", "I’m not sure. I guess it might be because people are richer."))))
    pics = " ".join(rows(14, 1, 17, 23, split=58)).replace(" Picture", "\nPicture").split("\n")
    akey = REVEAL(UL(pics), "Ответ (ключ)")
    read = SEC("Reading", "",
               '<p class="intro">You are going to read an article entitled <i>Priced out of the market</i>. It is about different '
               'solutions to the current shortage of housing in many countries.</p>' +
               EX("b66-ra", "A", "Look at the pictures in the article. How do you think each one is connected to the title?", akey) +
               EX("b66-rb", "B", "Read the article and see if you were right. When do you think it was written? Why?", article()) +
               X.true_false("b66-rc", "C", "Decide if these sentences about the article are true or false. Read again and check.") +
               EX("b66-rd", "D", "Work in groups of three. Discuss these questions:", OL([
                   "Do you have any of the same problems in your country?",
                   "What do you think of the different ideas for dealing with the housing problem? What’s the best solution? Can "
                   "you think of any others?",
                   "How much do house prices vary in your town / city / country? Where is the best place to buy?",
                   "If you could live anywhere you wanted, where would you choose? Why?"])) +
               X.article_e("b66-re"))
    return PAGE_BOX(66, voc + read)


def p68():
    voc = SEC("Vocabulary", "Describing areas", X.areas("b68-va") +
              EX("b68-vb", "B", "Write a list of areas you know. Work in pairs. Swap your paper and ask <i>What’s … like?</i> Your "
                 "partner should answer the questions using language from exercise A.", ""))
    conv = [numbered(rows(15, 0, a, b)) for a, b in ((2, 10), (10, 17))]
    akey = REVEAL("".join(f"<p><b>Conversation {i}</b></p>" + OL([r.split(" ", 1)[1] for r in [c[0][2:]] + c[1:]])
                          for i, c in enumerate(conv, 1)), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two people talking about the area they live in.</p>' +
              EX("b68-la", "A", '<span class="audio-ic">♪</span> 9.3 Listen and answer the questions about each conversation.',
                 OL(["Do they like it?", "What’s nice about the area?", "What’s bad about the area?", "How has the area changed?",
                     "What caused the change?"]) + akey) + S93())
    gr = SEC("Grammar", "Comparing the past with now",
             X.compare("b68-ga", "A", "Try and complete the sentences from <i>Listening</i>. They compare things between the past "
                       "and now. Check your answers in the audioscript.") +
             EX("b68-gb", "B", "Translate the sentences in exercise A into your language.", "") + HELP(148) +
             EX("b68-gc", "C", "Complete these sentences so they are true about your town, country or society. Work in pairs. "
                "Explain your ideas. Some of the pictures may help.", OL([
                    "… is / are much worse than … was / were before.", "… isn’t / aren’t as bad as it / they used to be.",
                    "There is much less … than there was a few years ago.", "There is / are more … than there was / were in the past.",
                    "It’s far easier to … than it used to be.", "… is more touristy than it used to be.",
                    "… is / are getting better and better.", "Over the past few years, they’ve built more and more … in … ."]) +
                '<div class="writer" data-target="" data-id="u09-gc"><textarea rows="5"></textarea></div>') +
             EX("b68-gd", "D", "Work in groups of three. Discuss how the world is better than before, and how it is worse.", ""))
    return PAGE_BOX(68, '<div class="cols"><div>' + voc + lis + '</div><div>' + gr + "</div></div>" +
                    IMG(IMG_DIR + "p68-photos.jpg", ""))


ADS = [("RENTAL", (55, 225, 235, 402)), ("", (245, 200, 462, 345)), ("", (470, 180, 760, 252)), ("", (470, 275, 760, 348)),
       ("", (55, 420, 235, 560)), ("", (250, 395, 525, 550))]


def p69():
    ads = "".join(f'<div class="note">{"<h4>" + h + "</h4>" if h else ""}<p>{fixed(69, text(69, b))}</p></div>' for h, b in ADS)
    spk = SEC("Speaking", "",
              EX("b69-sa", "A", "Read adverts for six host families for foreign students studying in the centre of Berlin. Prices "
                 "are per week. Give each a mark 1–5 (1=bad, 5=great).",
                 f'<div class="cols">{ads}</div>' + IMG(IMG_DIR + "p69-room.jpg", "", cls="sm")) +
              EX("b69-sb", "B", "Work in pairs. Discuss whether you would like to stay in each one and why / why not.", ""))
    dc = SEC("Developing conversations", "Asking about rules",
             '<p class="intro">A student is asking some questions to a new host family.</p>' +
             X.rules("b69-da", "A", "Match the student’s questions 1–6 with the host family’s replies a–f. Notice the expressions "
                     "in <b>bold</b>, which set limits to the answers.") +
             EX("b69-db", "B", "Underline the different ways of making a request in the questions in exercise A.", "") +
             EX("b69-dc", "C", "Work in pairs. Imagine you are going to stay with one of the host families in <i>Speaking</i>. "
                "Write down six more questions you would ask and the replies you might get. Use the language from exercise A.",
                '<div class="writer" data-target="" data-id="u09-rules"><textarea rows="6"></textarea></div>'))
    spk2 = SEC("Speaking", "",
               EX("b69-s2", "A", "Role-play a phone call between a student and a host family. Use as much new language from this "
                  "unit as you can. Ask questions about:", UL(["the house", "the area", "rules", "any special requests"]) +
                  IMG(IMG_DIR + "p69-cartoon.jpg", "That’s your room there.", cls="md")))
    return PAGE_BOX(69, spk + '<div class="cols"><div>' + dc + '</div><div>' + spk2 + "</div></div>")


def build():
    return p64() + p65() + p66() + p68() + p69()
