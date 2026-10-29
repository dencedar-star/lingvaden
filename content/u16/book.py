"""Страница «Учебник»: Unit 16 News and events, pp. 110–115. Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, script, lines, fixed, _fix, FIX
from keys import rows
from . import shared as X

IMG_DIR = "../assets/img/unit16/"

FIX[114] = [(" - ", " – ")]
FIX[115] = [("É1o million", "£10 million"), ("Pop idol", "<i>Pop Idol</i>"), ("World Idol", "<i>World Idol</i>"),
            ("him, It", "him. It"), ("photos. some", "photos, some"), ("1 kiss", "I kiss"), ("90-", "90 –"), (" - ", " – "),
            ("The Guinness Book of Records", "<i>The Guinness Book of Records</i>"), ("My Generation", "<i>My Generation</i>")]
FIX[174] = FIX.get(174, []) + [("1 know", "I know"), ("Italy:", "Italy."), ("Brazilian, I’m", "Brazilian. I’m"), ("l’ve", "I’ve"),
                               ("D. To be honest", "D: To be honest"), ("club record", "club record."),
                               ("Oranges in August", "<i>Oranges in August</i>"),
                               ("Anna and Maja and Jens", "<i>Anna and Maja and Jens</i>")]
FIX[175] = FIX.get(175, []) + [(" - ", " – ")]

HEADS = ["Date someone who’s already famous", "Go on a reality TV show", "Inherit a fortune", "Start a blog or set up a website",
         "Become a hero", "Don’t give up!"]
BOXES = [(25, 395, 268, 550), (25, 605, 268, 864), (272, 395, 518, 563), (272, 797, 518, 1056), (522, 395, 750, 547),
         (522, 605, 750, 803)]
IMGS = {2: "p115-idol.jpg", 3: "p115-paris.jpg", 6: "p115-singer.jpg"}


def br(lines_):
    return "<br>".join(lines_)


def article():
    intro = [fixed(114, p) for b in [(50, 285, 420, 355), (440, 285, 762, 490)] for p in paras(114, b, indent=12)]
    out = ""
    for i, (h, b) in enumerate(zip(HEADS, BOXES), 1):
        body = "".join(f"<p>{fixed(115, p)}</p>" for p in paras(115, b, indent=12))
        img = IMG(IMG_DIR + IMGS[i], "", cls="md") if i in IMGS else ""
        out += f'<div class="note"><h4>{i} {h}</h4>{body}{img}</div>'
    return ('<div class="article"><h3 class="art-title">Seeking fame and fortune</h3>' +
            "".join(f"<p><b>{p}</b></p>" for p in intro) + IMG(IMG_DIR + "p115-zimmers.jpg", "") +
            '<div class="cols">' + out + "</div></div>")


def S161():
    return SCRIPT("16.1", "", script(174, (30, 535, 394, 1060)) + script(174, (394, 75, 794, 237)), "174")


def S162():
    ls = []
    for l in lines(174, (394, 255, 794, 420)):
        t = fixed(174, _fix(l["t"])).strip()
        n, _, rest = t.partition(" ")
        ls.append((n, rest))
    return SCRIPT("16.2", "", ls, "174")


def S163():
    return SCRIPT("16.3", "", script(174, (394, 440, 794, 1060)) + script(175, (30, 75, 394, 362)), "174–175")


def p110():
    voc = SEC("Vocabulary", "Newspapers",
              EX("b110-va", "A", "Look at these different parts of a newspaper. Tick ✓ the parts you usually look at and put a "
                 "cross ✗ by any you never look at.",
                 X.wordbox(["national news", "the business pages", "the letters page", "the reviews", "international news",
                            "the sports pages", "the gossip pages", "the horoscopes"])) +
              EX("b110-vb", "B", "Work in pairs. Compare your ideas and explain your decisions. Which part do you usually read "
                 "first?", "") +
              EX("b110-vc", "C", "Check you understand the words and expressions in <b>bold</b>. Then discuss which part of the "
                 "newspaper each question refers to.", OL([
                     "How many <b>marks out of ten</b> did they give it?", "What’s the <b>exchange rate</b> at the moment?",
                     "Did you see what she was wearing at the <b>premiere</b>?", "What was <b>the score</b> in the game last night?",
                     "So have they agreed a <b>ceasefire</b> yet?", "What <b>star sign</b> are you?"]) +
                 REVEAL(br(rows(24, 1, 35, 46, split=65)), "Ответ (ключ)")))
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear five conversations about different news stories.</p>' +
              X.news_pairs("b110-la", "A", "The words below come from the conversations: two from each. Work in pairs. Discuss "
                                           "which pairs of words go together, and what kind of story they might come from.") +
              EX("b110-lb", "B", '<span class="audio-ic">♪</span> 16.1 Now listen and check your ideas. Take notes on:', UL([
                  "which of the words in exercise A appear in which conversation.",
                  "what story is being discussed in each case."]) + REVEAL(br(rows(24, 1, 48, 56, split=65)), "Ответ (ключ)")) +
              EX("b110-lc", "C", "Work in pairs. Can you remember the whole sentences that each of the words in exercise A "
                 "appeared in? Compare your ideas. Then listen again and read the audioscript to check your answers.", "") +
              EX("b110-ld", "D", "Work in pairs. Practise reading the conversations. Continue each conversation for as long as "
                 "you can by adding your own ideas and comments.", "") + S161())
    return PAGE_BOX(110, IMG(IMG_DIR + "p110-banner.jpg", "16 News and events") +
                    '<div class="cols"><div>' + voc + '</div><div>' + lis + "</div></div>" +
                    IMG(IMG_DIR + "p110-premiere.jpg", ""))


def p111():
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">Did you see that thing on TV about the '
                'mobile phone factory closing down?<br>Did you see that thing in the papers about Moscow being the most '
                'expensive city in the world now?<br>Did you read about Paris Simpson getting arrested?<br>Did you read about '
                'Inter Milan signing that young Irish kid?<br>Did you hear about Laura losing her job?<br>Did you hear about Lee '
                'getting promoted?</p></div>')
    dbox = ('<div class="box"><p><b>We often introduce sentences about things in the news with <i>apparently</i>. This shows we '
            'are not 100% certain these facts are true – we are just reporting what we have heard.</b></p><hr>'
            '<p class="ex-line"><i>Apparently</i>, she found out her husband was having an affair with another Hollywood actress.'
            '<br><i>Apparently</i>, they think his attackers might have been even younger than him.</p></div>')
    dc = SEC("Developing conversations", "<i>Apparently</i>", dbox +
             EX("b111-da", "A", "Complete the dialogues below with your own ideas.", OL([
                 DLG(("A", "Did you see that thing in the paper about the murder in town last night?"),
                     ("B", "Yeah, it was awful, wasn’t it? Apparently, …")),
                 DLG(("A", "Did you see that thing on TV about the new shopping mall they’re going to build?"),
                     ("B", "Yeah, it’s great, isn’t it? Apparently, …")),
                 DLG(("A", "Did you see that politician on TV last night trying to dance to hip-hop?"),
                     ("B", "Yeah, it was really funny, wasn’t it? Apparently, …")),
                 DLG(("A", "Did you see that thing in the paper about that tennis player, James Jenkins?"),
                     ("B", "No. What was that?"), ("A", "Well, apparently, …")),
                 DLG(("A", "Did you see that thing on the news about Shaynee Wilson and her boyfriend getting arrested?"),
                     ("B", "No. What was that?"), ("A", "Well, apparently, …"))]) +
                '<div class="writer" data-target="" data-id="u16-apparently"><textarea rows="5"></textarea></div>') +
             EX("b111-db", "B", "Have you heard any gossip or stories you aren’t sure are true? Tell a partner using "
                "<i>apparently</i>.", ""))
    pbox = ('<div class="box"><p><b>When we comment on things people tell us, we often add the question tags <i>wasn’t it? / '
            'isn’t it?</i> As we expect people to agree with us in these situations, our voice goes down on the tag.</b></p><hr>'
            '<p class="ex-line">E: Did you see that thing on TV about the murder last night?<br>F: Yeah. It was shocking, '
            '<i>wasn’t it?</i></p></div>')
    pr = SEC("Pronunciation", "Responding to news", pbox +
             EX("b111-pa", "A", '<span class="audio-ic">♪</span> 16.2 Listen to ten sentences. Repeat them.', S162()) +
             EX("b111-pb", "B", "Work in pairs. Take turns saying the sentences below. Respond with a comment + question tag.",
                OL(["Did you hear about Jay and Selma splitting up?",
                    "Did you hear about John getting food poisoning from his own cooking?",
                    "Did you read about Angelina booking a special hotel room for her dog?",
                    "Did you read that the ceasefire has ended already?", "Did you read that she paid $5,000 for that dress?",
                    "Did you hear that Jay and Selma are back together?"])))
    cp = SEC("Conversation practice", "",
             EX("b111-ca", "A", "Think of two news stories you have read or heard about recently. Write one question for each "
                "story, using the ones in <i>Language patterns</i> as a model.", "") +
             EX("b111-cb", "B", "Work in groups. Discuss the stories. Start your conversations with your questions from "
                "exercise A.", ""))
    return PAGE_BOX(111, '<div class="cols"><div>' + IMG(IMG_DIR + "p111-newspaper.jpg", "") + patterns + dc +
                    IMG(IMG_DIR + "p111-camera.jpg", "") + '</div><div>' + pr + cp + "</div></div>")


def p112():
    spk = SEC("Speaking", "",
              EX("b112-sa", "A", "Work in groups. Do you know who any of the people in the photos below are? Discuss them. Use "
                 "some of these expressions:", '<p class="ex-line">I haven’t got a clue!<br>Isn’t that that American '
                 'politician? What’s his name?<br>He looks really familiar, but I can’t remember who he is.<br>I’m fairly sure '
                 'that’s …</p>' + IMG(IMG_DIR + "p112-people.jpg", "Famous people") +
                 REVEAL(br(rows(25, 0, 3, 6, split=56)), "Кто на фото (ключ)")))
    voc = SEC("Vocabulary", "Explaining who people are", X.who_people("b112-va") +
              EX("b112-vb", "B", "Translate the parts of the sentences in exercise A in <i>italics</i>.", "") +
              EX("b112-vc", "C", "Can you use the words in <i>italics</i> to describe any other famous people from now or in the "
                 "past?", ""))
    return PAGE_BOX(112, spk + voc)


def p113():
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear three short conversations about four more famous or important people.</p>' +
              EX("b113-la", "A", '<span class="audio-ic">♪</span> 16.3 Listen and answer the questions for each conversation.',
                 OL(["Why do they start talking about Garibaldi / Comenius / Eddy Merckx / Magritte?",
                     "What is each person famous for?", "Where is each person from?",
                     "What else do you learn about each one?"]) +
                 REVEAL(br(rows(25, 0, 15, 41, split=56)), "Ответ (ключ)")) +
              EX("b113-lb", "B", "Work in pairs.", OL([
                  "Can you think of a place:" + UL(["which is <i>named after</i> a famous person?",
                                                    "which is decorated with <i>memorabilia</i>?"]),
                  "Can you think of someone:" + UL(["who is a national hero?", "who was ahead of his / her time?"])])) + S163())
    gbox = ('<div class="box"><p><b>We often use relative clauses to add information after a noun:</b></p>'
            '<p class="ex-line">He was a Czech writer <i>who wrote about education</i>.</p><hr>'
            '<p><b>You can also use <i>that</i> instead of <i>who</i> in the sentence above.<br>To add information about things, '
            'use <i>that</i> or <i>which</i>.<br>To add information about times, use <i>that</i> or <i>when</i>.<br>To add '
            'information about possessions, use <i>whose</i>.<br>To add information about places, use <i>where</i>.</b></p></div>')
    gr = SEC("Grammar", "Defining relative clauses", gbox + X.rel_cross("b113-ga") + HELP(155))
    spk = SEC("Speaking", "",
              EX("b113-sa", "A", "Work in pairs. Role-play a conversation.",
                 "<p><b>Student A:</b> You are visiting the town / country where <b>Student B</b> lives. Ask about statues, "
                 "monuments and streets named after people, dates or places, to find out their significance. For example:"
                 "<br><i>Who’s that statue of in the main square?<br>Why’s it called The Darwin Institute?</i><br>"
                 "<b>Student B:</b> Explain.</p>") +
              EX("b113-sb", "B", "Make the following lists:", UL([
                  "the four greatest living people in your country.",
                  "the four most important people who have ever lived in your country."]) +
                 "<p><b>Write the list individually. Then work in pairs. Compare your list with a partner and try to agree on "
                 "the same lists.</b></p><p><b>If your partner does not know any of the people you have chosen, explain who "
                 "they are / were. Use these sentence frames:</b><br><i>He’s the man who …<br>She’s the woman who …</i></p>"))
    return PAGE_BOX(113, '<div class="cols"><div>' + IMG(IMG_DIR + "p113-cyclist.jpg", "") +
                    IMG(IMG_DIR + "p113-pipe.jpg", "Ceci n’est pas une pipe.") + lis + '</div><div>' + gr + spk +
                    "</div></div>")


def p114():
    read = SEC("Reading", "",
               EX("b114-ra", "A", "Read the short article about a survey. Then work in pairs. Discuss these questions:", UL([
                   "Why do you think so many people want to be famous?",
                   "What kind of problems do you think these ambitions might cause?",
                   "Can you think of any celebrities who have found fame hard to cope with?",
                   "Which six different ways of becoming rich and famous do you expect the article to mention?"]) +
                  REVEAL(br(rows(25, 0, 51, 56, split=56)), "Ответ на последний вопрос (ключ)")) +
               article() + X.sections("b114-rb") +
               EX("b114-rc", "C", "Read the rest of the article. Then work in pairs. Discuss why the people and things below "
                  "were mentioned. Check your ideas by looking at the article again if you need to.",
                  X.wordbox(["the gossip magazines", "an advertising company", "<i>The Guinness Book of Records</i>",
                             "Kurt Nilsen", "Paris Hilton", "Kim Sing and Bee Lian Man", "Golda Bechal", "Mahir Cagri",
                             "karaoke", "Kuldeep Singh", "The Zimmers", "The Who"]) +
                  REVEAL(br(rows(25, 1, 10, 36, split=56)), "Ответ (ключ)")) +
               X.fame_words("b114-rd", "D", "Complete the sentences with the correct form of the words from the article. "
                                            "Underline the words that collocate with them in each sentence.") +
               EX("b114-re", "E", "Work in pairs. Use three of the collocations from exercise D to say something about your "
                  "life. For example:", "<p><i>I’d like to follow in my father’s footsteps and become a surgeon.</i></p>"))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>easier said than done</i></b></p><p>When we think '
              'someone’s advice or suggestion sounds good, but is actually very difficult to do, we often say it is <i>easier '
              'said than done</i>.</p><p><i>Obviously, finding a famous partner is easier said than done.<br>I know I should stop '
              'smoking, but it’s easier said than done.<br>People keep telling me to forget her, but that’s easier said than '
              'done.</i></p></div>')
    spk = SEC("Speaking", "", EX("b114-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Can you think of any other people who have become famous in the six ways mentioned in the article?",
        "Would you like to be famous? Why? / Why not?", "What do you think is the best way to become famous?",
        "Can you think of any bad ways of becoming famous?"])))
    return PAGE_BOX(114, read + '<div class="cols"><div>' + native + '</div><div>' + spk + "</div></div>")


def build():
    return (p110() + p111() + p112() + p113() + p114() +
            PAGE_BOX(115, '<p class="note-s">Текст статьи <i>Seeking fame and fortune</i> — на с. 114, в задании Reading.</p>'))
