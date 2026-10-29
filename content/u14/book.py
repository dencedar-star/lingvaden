"""Страница «Учебник»: Unit 14 Technology, pp. 98–103. Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, script, fixed, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit14/"

FIX[101] = [("date - as well a plenty", "date – as well as plenty"), (" - ", " – "), ("CANALS ", ""), ("THE SINCLAIR C5 ", ""),
            ("reveals a long", "<b>reveals</b> a long"), ("of non-starters", "of <b>non-starters</b>"),
            ("had fallen out of use", "had <b>fallen out of use</b>"), ("This bitter fight for market share",
                                                                       "This <b>bitter</b> fight for <b>market share</b>"),
            ("electric vehicle was", "electric <b>vehicle</b> was"), ("cost its creator", "cost its <b>creator</b>"),
            ("ground, thus dangerous", "ground, <b>thus</b> dangerous"), ("goes to show. That", "goes to show. That")]
FIX[172] = FIX.get(172, []) + [("1: Ah! OK", "J: Ah! OK"), ("): Turning", "J: Turning"), ("as soon as 1 have", "as soon as I have"),
                               ("From Marketing", "From Marketing."), ("comes up", "comes up.")]
FIX[173] = FIX.get(173, []) + [("Wowl", "Wow!"), ("or sott -", "or soft …"), ("F No, it’s", "F: No, it’s"), (" - ", " – ")]


def br(lines):
    return "<br>".join(lines)


def article():
    intro = [fixed(101, p) for p in paras(101, (45, 110, 780, 345), indent=12)]
    canals = fixed(101, " ".join(paras(101, (270, 390, 775, 535), indent=12)))
    video = [fixed(101, p) for p in paras(101, (62, 575, 260, 900), indent=12) if p != "VIDEO CASSETTES"]
    c5 = [fixed(101, p) for p in paras(101, (286, 575, 775, 735), indent=12)]
    c5b = [fixed(101, p) for p in paras(101, (620, 730, 775, 990), indent=12)]
    c5[-1] += " " + c5b[0]
    c5 += c5b[1:]
    return ('<div class="article"><h3 class="art-title">Here today, gone tomorrow!</h3>' +
            "".join(f"<p>{p}</p>" for p in intro) +
            '<div class="cols"><div>' + IMG(IMG_DIR + "p101-canal.jpg", "") + "</div>"
            f"<div><h4>Canals</h4><p>{canals}</p></div></div>"
            '<div class="cols"><div><h4>Video cassettes</h4>' + "".join(f"<p>{p}</p>" for p in video) +
            IMG(IMG_DIR + "p101-video.jpg", "") + "</div>"
            '<div><h4>The Sinclair C5</h4>' + "".join(f"<p>{p}</p>" for p in c5) +
            IMG(IMG_DIR + "p101-sinclair.jpg", "") + "</div></div></div>")


def S142():
    return SCRIPT("14.2", "J = Jirka, E = Ella", script(172, (392, 185, 794, 805)), "172")


def S143():
    return SCRIPT("14.3", "", script(172, (392, 825, 794, 1060)) + script(173, (40, 75, 400, 775)), "172–173")


def p98():
    spk = SEC("Speaking", "", EX("b98-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "What kind of computer do you have?", "Why did you choose that make? Are you happy with it?",
        "Are you good with computers? What kind of things do you know how to do?",
        "Is there anything you would still like to learn how to do?"])))
    voc = SEC("Vocabulary", "Computers",
              EX("b98-va", "A", "Label the picture with the words in the box.",
                 X.wordbox([f"{i + 1} {w}" for i, w in enumerate(X.PC)]) +
                 IMG(IMG_DIR + "p98-computer.jpg", "Computer", cls="md")) +
              X.pc_nouns("b98-vb") +
              EX("b98-vc", "C", "Underline the words that collocate with the twelve gapped nouns in exercise B. Translate these "
                 "collocations into your language.", REVEAL(br(rows(21, 1, 44, 56, split=57)), "Ответ (ключ)")) +
              EX("b98-vd", "D", "Work in pairs. Discuss these questions:", UL([
                  "Have you ever had any of the problems described in 7–12 in exercise B? When? What happened?",
                  "What do you usually do when you have computer problems?"])))
    return PAGE_BOX(98, IMG(IMG_DIR + "p98-banner.jpg", "14 Technology") +
                    '<div class="cols"><div>' + spk + '</div><div>' + IMG(IMG_DIR + "p99-circuit.jpg", "") + "</div></div>" +
                    voc)


def p99():
    pbox = ('<div class="box"><p><b>Abbreviations are formed using the first letters of each word in the name of something. For '
            'example, <i>USA</i> is an abbreviation for the <i>United States of America</i>. When we say abbreviations, we '
            'usually stress each individual letter. However, occasionally we say them as one word.</b></p></div>')
    pr = SEC("Pronunciation", "Abbreviations", pbox +
             EX("b99-pa", "A", "Work in pairs. Do you know what these abbreviations are?",
                X.wordbox(["IT", "USB", "PC", "URL", "RTF", "PDF", "DVD", "FAQs", "ASAP", "GPS", "JPEG", "WiFi", "RAM",
                           "CD-ROM", "AIDS"]) + REVEAL(br(rows(22, 0, 2, 17, split=59)), "Ответ (ключ)")) +
             EX("b99-pb", "B", '<span class="audio-ic">♪</span> 14.1 Now listen and practise saying them.', ""))
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a telephone call between Ella, a marketing manager for a large design '
              'firm, and Jirka, who works in the IT department.</p>' +
              EX("b99-la", "A", '<span class="audio-ic">♪</span> 14.2 Listen and answer the questions.', OL([
                  "What is the main problem with Ella’s computer?", "What other problem had she been having with it?",
                  "What two suggestions does Jirka make?", "How does Ella respond to each of them?",
                  "What does Jirka suggest Ella should do in the end?"]) +
                 REVEAL(br(numbered(rows(22, 0, 20, 29, split=59))), "Ответ (ключ)")) + S142())
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">Have you tried re-booting it at all?'
                '<br>Have you talked to anyone in IT about it at all?<br>I didn’t learn anything at all on that course!<br>'
                'I don’t have any plans at all for the holidays.<br>He hardly ate anything at all.<br>I hardly know her at all, '
                'to be honest.</p></div>')
    spk = SEC("Speaking", "", EX("b99-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "What do you think of the advice Jirka gives Ella?",
        "Do you know anyone who works in IT? Do they enjoy it? Would you like to do that kind of work?",
        "Do you think men tend to be better with technology than women? Why? / Why not?"])))
    t1 = ('<table class="voc"><tr><td>A: Have you</td><td>tried rebooting?<br>checked the connection?</td></tr>'
          '<tr><td>B: Yeah,</td><td>but it didn’t work.<br>but it made no difference.<br>but it didn’t do any good.<br>'
          'but I didn’t have any success.</td></tr></table>'
          '<table class="voc"><tr><td>A: Have you</td><td>tried rebooting?<br>checked the connection?</td></tr>'
          '<tr><td>B: No,</td><td>I haven’t.<br>not yet.</td></tr>'
          '<tr><td>A: Well, try that.</td><td>Otherwise, I can’t really help.<br>Otherwise, you’re best taking it to a shop.<br>'
          'Otherwise, you’ll have to get a new one.<br>Otherwise, I don’t know what else you can do.</td></tr></table>')
    dc = SEC("Developing conversations", "Responding to advice",
             EX("b99-da", "A", "Translate the phrases in the boxes into your language.", t1) +
             EX("b99-db", "B", "Look at the situations in 1–5. Take turns to give advice and respond to it.", OL([
                 "The attachment won’t open.", "The printer’s not working.",
                 "The computer crashed and I can’t find the file I was working on.", "I can’t log on to the network.",
                 "I left the power cable for my laptop on the train."])))
    cp = SEC("Conversation practice", "",
             EX("b99-ca", "A", "Work in pairs. Make a list of as many problems you could have with a computer as you can. "
                "Compare your list with another pair. Did they have any ideas you had not thought of?", "") +
             EX("b99-cb", "B", "Now role-play four telephone calls between someone who works on a help desk and someone with "
                "computer problems. Change roles after each conversation. Use as much language from these pages as possible.",
                ""))
    return PAGE_BOX(99, '<div class="cols"><div>' + pr + lis + patterns + '</div><div>' + spk + dc + cp + "</div></div>")


def p100():
    read = SEC("Reading", "",
               EX("b100-ra", "A", "The things in these photographs are all connected to the theme of an article you are going "
                  "to read. Work in pairs. Discuss what you think the article might be about, and how the things could be "
                  "connected.", IMG(IMG_DIR + "p100-photos.jpg", "a canal, a floppy disc, videotapes, the Sinclair C5",
                                    cls="md")) +
               EX("b100-rb", "B", "Read the article quickly and see if your ideas were correct. Work in pairs. Compare what you "
                  "remember about the things in the photos.", REVEAL(" ".join(rows(22, 0, 34, 43, split=59)), "Ответ (ключ)")) +
               article() +
               X.article_tf("b100-rc", "C", "Decide if these sentences about the article are true or false, according to the "
                            "author. Then look back and underline the parts of the text that showed you the answer.") +
               EX("b100-rd", "D", "Work in pairs. Discuss these questions:", UL([
                   "Can you think of any other examples of technology that soon became out of date and were replaced by "
                   "something else?", "Can you think of anything that has enjoyed a revival recently?",
                   "What are the hot new pieces of technology at the moment? Have you bought any of them?",
                   "The writer mentioned the videotape format war and the Mac / PC debate. Can you think of any other similar "
                   "examples?"])) +
               EX("b100-re", "E", "Work in pairs. Discuss what you think the words in <b>bold</b> in the article mean.",
                  REVEAL(br(rows(22, 1, 5, 16, split=59)), "Ответ (ключ)")))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>hot</i></b></p><p>When we describe something as '
              '<i>hot</i>, it means we think it is very exciting and interesting – because it is so new.</p><p><i>That hot new '
              'piece of technology you queued all day to buy.<br>Their new web phone is the hot new thing this winter.<br>'
              'She’s one of the hottest young directors in Hollywood.<br>It’s a great site. They have all the hot news and '
              'gossip!</i></p></div>')
    voc = SEC("Vocabulary", "Talking about markets",
              '<p class="intro">In <i>Reading</i>, you read about the bitter fight between Sony and JVC for <i>market share</i>.</p>' +
              EX("b100-va", "A", "Decide which of the two possible endings for each sentence below best describes the situation "
                 "in your country. Then work in pairs to compare your ideas. Explain your choices.", OL([
                     "The beauty salon market is <i>almost saturated / growing steadily</i>.",
                     "The English language market is <i>huge / tiny</i>.",
                     "The hat market is <i>bigger / smaller</i> than it used to be.",
                     "The mobile phone market is <i>completely saturated / booming</i>.",
                     "The computer game market is <i>in decline / still growing</i>.",
                     "The bottled water market is <i>big business / dead</i>.",
                     "The DVD market is <i>in decline / fairly steady</i>.",
                     "The package holiday market is <i>bigger / smaller</i> than it was twenty years ago."])) +
              EX("b100-vb", "B", "Which endings in <i>italics</i> in exercise A best describe these markets in your country?",
                 X.wordbox(["the housing market", "the cigarette market", "the DIY market", "the tourist market",
                            "the fast food market", "the organic food market", "the coffee shop market", "the online market",
                            "the black market", "the digital camera market"])))
    return PAGE_BOX(100, read + '<div class="cols"><div>' + native + '</div><div>' + voc + "</div></div>")


def p102():
    voc = SEC("Vocabulary", "Technology, programs and gadgets", X.gadgets("b102-va") +
              EX("b102-vb", "B", "Work in pairs. What kind of things do you think are being described in 1–12 in exercise A?",
                 REVEAL(br(rows(22, 1, 27, 40, split=59)), "Возможные ответы (ключ)")) +
              IMG(IMG_DIR + "p102-upgrade.jpg", "He still refuses to upgrade", cls="md"))
    spk = SEC("Speaking", "", EX("b102-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Do you know anyone who always buys the latest gadgets, technology or computer programs?",
        "Do you know anyone who is a bit of a technophobe? In what way?",
        "Have you bought any new electronic items, gadgets or software recently? What? Why did you get them?"])))
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear three conversations about gadgets or technology.</p>' +
              EX("b102-la", "A", '<span class="audio-ic">♪</span> 14.3 Listen and answer the questions.', OL([
                  "What items are they talking about?", "Do all of the speakers think the items are good?"]) +
                 REVEAL(br(numbered(rows(22, 1, 42, 48, split=59))), "Ответ (ключ)")) +
              EX("b102-lb", "B", "Now answer these questions. Listen again if you need to.", UL([
                  "1a Why is using solar energy so common in Germany?", "1b Is it accessible even to poor people?",
                  "2a Why do they start talking about the GPS?", "2b What reasons does she give for not getting one?",
                  "3a What are the advantages of the egg cooker?", "3b What does the woman see as a better invention? Why?"]) +
                 REVEAL(br(rows(22, 1, 49, 57, split=59) + rows(23, 0, 0, 2, split=56)), "Ответ (ключ)")) +
              EX("b102-lc", "C", "Work in pairs. Discuss these questions:", UL([
                  "Does your government subsidise anything? Do you think it is good?",
                  "Is there any gadget or piece of technology that you could happily do without?",
                  "Can you think of any other gadgets which are environmentally friendly?",
                  "Is there anything that you would like to be invented – but that has not been invented yet?"])) + S143())
    return PAGE_BOX(102, '<div class="cols"><div>' + voc + '</div><div>' + spk + lis +
                    IMG(IMG_DIR + "p102-googled.jpg", "“I’m sorry, Jason. I don’t date anyone new until I’ve googled them.”",
                        cls="md") + "</div></div>")


def p103():
    gr = SEC("Grammar", "<i>-ing</i> forms and <i>to</i>-infinitives", X.ing_rules("b103-ga") +
             EX("b103-gb", "B", "Work in pairs. Discuss these questions:", UL([
                 "Does your language have an equivalent of the <i>-ing</i> form and <i>to</i>-infinitive?",
                 "Are they used in the same way as the examples in exercise A?"])) +
             X.ing_correct("b103-gc") + HELP(153) +
             EX("b103-gd", "D", "Complete the sentences so they are true for you. Use a verb phrase with an <i>-ing</i> form or "
                "a <i>to</i>-infinitive. Then work in pairs to compare your ideas.", OL([
                    "I keep …", "I wish they’d invented a machine … .", "I think … is OK for women, but not for men.",
                    "I’m hoping … sometime in the future.", "I could never get used to … .", "I think … is better for you than … .",
                    "I spend most of my weekends … .", "I’ve arranged … at the weekend."]) +
                '<div class="writer" data-target="" data-id="u14-ing"><textarea rows="6"></textarea></div>'))
    spk = SEC("Speaking", "",
              EX("b103-sa", "A", "Work in groups. Explain why each of the following things may be good or bad for the "
                 "environment. Which is the most important thing to do? Use these sentence starters:",
                 '<p class="ex-line"><i>I think X is bad for the environment because … .<br>…-ing is more important than …-ing '
                 'because … .<br>I think it has something to do with …-ing.</i></p>' + UL([
                     "Leaving your TV on standby overnight.", "Eating regularly at a fast food / hamburger place.",
                     "Planting a tall tree near your house.", "Closing curtains at night.",
                     "Using a ceiling fan in the summer and winter.", "Taking a plastic bag from every shop you buy from.",
                     "Eating a lot of rice.", "Going on holiday abroad.", "Wearing a hat in the house if it is cold.",
                     "Cycling and walking everywhere.", "Using energy-efficient light bulbs.",
                     "Using biofuels: fuels made from biological materials such as sugar cane or palm oil."])) +
              EX("b103-sb", "B", "Write your own ideas about things you have heard are good / bad for the environment. Has "
                 "anyone in your group heard the same?",
                 '<p class="ex-line"><i>… is supposed to be bad.<br>… is supposed to cause / create / be a good way of …-ing.'
                 '</i></p>') +
              EX("b103-sc", "C", "Work in pairs. Discuss these questions:", UL([
                  "Which of the things in exercises A and B do you do? Why?", "Which do you avoid doing?",
                  "Which would you consider doing or stopping?", "Which could you never get used to doing?"])))
    return PAGE_BOX(103, '<div class="cols"><div>' + gr + '</div><div>' + spk +
                    IMG(IMG_DIR + "p103-recycle.jpg", "", cls="md") + "</div></div>")


def build():
    return p98() + p99() + p100() + PAGE_BOX(101, '<p class="note-s">Текст статьи <i>Here today, gone tomorrow!</i> — на с. '
                                                  '100, в задании Reading.</p>') + p102() + p103()
