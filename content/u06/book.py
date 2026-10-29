"""Страница «Учебник»: Unit 06 Going shopping, pp. 42–47 (+ Information files 2, 4, 8). Длинные тексты — из OCR и ключей."""
import re
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import lines, paras, script, fixed, _fix, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit06/"

FIX[45] = [("a look a bit", "a I look a bit"), ("b look smart", "b I look smart"), ("c 1 look", "c I look"),
           ("| like to shop", "I like to shop"), ("Why should 1?", "Why should I?"), ("much l’d", "much I’d"),
           ("once | lose", "once I lose"), ("centres / mails", "centres / malls"), ("without it.I", "without it. I"),
           ("6-19", "6–19"), ("Sometimes -especially", "Sometimes – especially")]
FIX.setdefault(157, []).extend([("*shirts", "shirts"), ("than shopping", "than shopping."), (" - ", " – ")])
FIX.setdefault(164, []).extend([("B: Two - I’ve", "B: Two – I’ve"), ("Blue. but", "Blue, but")])
FIX.setdefault(165, []).extend([("No chancel", "No chance!"), (" - ", " – ")])


def questionnaire():
    qs = []
    for box in [(25, 265, 268, 1075), (272, 265, 505, 1075), (522, 70, 765, 1060)]:
        ls = lines(45, box)
        base = min(l["x"] for l in ls)
        for l in ls:
            t = fixed(45, _fix(l["t"])).strip()
            m = re.match(r"^(\d{1,2})\s+(.*)$", t)
            o = re.match(r"^([abc])\s+(.*)$", t)
            if m and int(m.group(1)) == len(qs) + 1:
                qs.append([m.group(2), []])
            elif o and qs and (l["x"] - base) * 794 / 2481 < 30:
                qs[-1][1].append(o.group(2))
            elif qs:
                if qs[-1][1]:
                    qs[-1][1][-1] += " " + t
                else:
                    qs[-1][0] += " " + t
    items = "".join(f"<li><b>{q}</b>" + OL(opts, "items alpha") + "</li>" for q, opts in qs)
    return ('<div class="article">' + IMG(IMG_DIR + "p45-banner.jpg", "Shop till you drop!", cls="md") +
            f'<ol class="items">{items}</ol></div>')


def file4():
    ps = paras(157, (60, 250, 397, 1000), indent=10**6, gap=1.2)
    out = ""
    for p in ps:
        m = re.match(r"^(\d+)-(\d+)\s+(.*)$", fixed(157, p))
        if m:
            out += f"<h4>{m.group(1)}–{m.group(2)}</h4><p>{m.group(3)}</p>"
    return ("<p>Answers to the <i>Shop till you drop!</i> questionnaire. Add up your score.<br>Answers a = 1 · Answers b = 3 · "
            "Answers c = 5</p>" + out)


def S61():
    return SCRIPT("6.1", "", script(164, (397, 445, 794, 885)), "164")


def S62():
    return SCRIPT("6.2", "", script(164, (397, 910, 794, 1060)) + script(165, (0, 70, 397, 660)), "164–165")


def S63():
    return SCRIPT("6.3", "L = Leo, N = Noel", script(165, (0, 700, 397, 1060)) + script(165, (397, 70, 794, 280)), "165")


def p42():
    voc = SEC("Vocabulary", "Describing souvenirs and presents",
              X.wordbox([w for w, _ in X.SOUV]) + X.souvenir_groups("b42-va") +
              EX("b42-vb", "B", "Use the words to describe the things in the pictures.", "") + X.souvenirs("b42-vc") +
              EX("b42-vd", "D", "Work in pairs. Tell your partner about souvenirs that you have bought or that people have bought "
                 "for you.", ""))
    bkey = REVEAL(UL([r for r in " ".join(rows(9, 0, 9, 14)).split("• ") if r]), "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a tourist buying a small rug. The tourist is negotiating with the '
              'seller.</p>' +
              EX("b42-la", "A", "Before you listen, work in pairs. Discuss these questions:", UL([
                  "What reasons might the tourist give for paying less?", "What reasons might the seller give for paying more?"])) +
              EX("b42-lb", "B", '<span class="audio-ic">♪</span> 6.1 Listen to the conversation and find out what reasons they '
                 "give.", bkey) + S61() +
              IMG(IMG_DIR + "p42-market.jpg", "", cls="md") + IMG(IMG_DIR + "p42-souvenirs.jpg", "", cls="md"))
    return PAGE_BOX(42, IMG(IMG_DIR + "p42-banner.jpg", "06 Going shopping") +
                    '<div class="cols"><div>' + voc + '</div><div>' + lis + "</div></div>")


def p43():
    pr = SEC("Pronunciation", "Intonation",
             '<div class="box"><p><b>When negotiating prices, we express surprise about a price using high intonation. To make '
             'an alternative offer or to agree, we use lower intonation.</b></p></div>' +
             EX("b43-pa", "A", '<span class="audio-ic">♪</span> 6.1 Listen to the conversation again and read the audioscript on '
                "p. 164. Notice the numbers where the intonation rises and those where it drops.", "") +
             EX("b43-pb", "B", "Work in pairs. Practice reading the conversation, using high and low intonation.", "") +
             EX("b43-pc", "C", "Work in pairs. Student A is the owner of one of the shops in the picture. Student B is a tourist "
                "who wants to buy a souvenir. Negotiate the price.", ""))
    dc = SEC("Developing conversations", "Avoiding repetition",
             '<p class="intro">We often use <i>one / ones</i> to avoid repeating words when we compare the difference between two '
             'things.</p>' + X.ones("b43-da") +
             EX("b43-db", "B", "Work in groups. Compare the features of any mobile phones you have.", ""))
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a man in a mobile phone shop. His phone company, Blue, has offered him the '
              'S620 and he is thinking of getting a better upgrade by changing company. The assistant offers him an N5703.</p>' +
              X.phones("b43-la", "A", '<span class="audio-ic">♪</span> 6.2 Listen and complete the table. Then work in pairs to '
                       "compare your answers.") +
              EX("b43-lb", "B", "The assistant starts by offering one number of free calls and messages, and ends by offering "
                 "another. Would you accept her final offer?", "") +
              X.phone_fix("b43-lc") +
              EX("b43-ld", "D", "Listen and read through the audioscript on pp. 164–165 to check your answers.", "") + S62())
    f2 = ("<p><b>Student A</b> — You are the customer. Decide:</p>" + UL([
        "how much you currently pay for your phone.", "how many text messages you get per month: 100? 200? 300?",
        "how many minutes you get per month: 100? 200? 300?",
        "Then decide what questions you want to ask about the new phone: camera? kind of battery? MP3 player?"]))
    f8 = ("<p><b>Student B</b> — You are the salesperson. Decide what functions the phone you are selling has: camera? MP3? "
          "email?</p><p>What makes it better than other phones: battery? price?</p><p>How many text messages per month you can "
          "offer: 100? 200? 300?</p><p>How many minutes per month you can offer: 100? 200? 300?</p><p>What price can you offer "
          "everything for?</p>")
    cp = SEC("Conversation practice", "",
             '<p class="intro">Work in pairs. You are going to role-play a conversation in a phone shop between a customer and a '
             'salesperson, similar to the one in <i>Listening</i>.</p>' +
             EX("b43-ca", "A", "Look through the audioscript on pp. 164–165 and underline any expressions you could use.", "") +
             EX("b43-cb", "B", "Student A, read File 2 on p. 156. Student B, read File 8 on p. 158. Role-play the conversation.",
                REVEAL(f2, "File 2, p. 156 — Student A") + REVEAL(f8, "File 8, p. 158 — Student B")) +
             IMG(IMG_DIR + "p43-cartoon.jpg", "Take care…", cls="md"))
    return PAGE_BOX(43, '<div class="cols"><div>' + IMG(IMG_DIR + "p43-shop.jpg", "", cls="md") + pr + dc +
                    '</div><div>' + lis + cp + "</div></div>")


def p44():
    akey = REVEAL(OL([r[2:] for r in numbered(rows(9, 0, 48, 58))]), "Объяснение (ключ)")
    voc = SEC("Vocabulary", "Clothes and accessories", X.odd_one("b44-va") + akey +
              EX("b44-vb", "B", "Work in pairs. Say what you think of the way the people in the picture below are dressed. Use "
                 "some of the language from exercise A. You might also want to use some of these expressions:", UL([
                     "That top / shirt <i>doesn’t fit</i> him / her <i>properly</i>.",
                     "Those trainers / earrings <i>don’t suit</i> him / her.",
                     "Those trainers <i>don’t match / don’t go with</i> that / those …"]) +
                 IMG(IMG_DIR + "p44-people.jpg", "")))
    group_a = ["avoid something", "last a long time", "can’t really afford it", "do without something", "come back empty-handed",
               "shop around", "go window-shopping", "get ripped off", "an outfit", "price tag"]
    group_b = ["out-of-town shopping mall", "force a company out of business", "a label", "in the sales", "designer brands",
               "an overdraft", "owe money", "retail therapy", "an exception", "second-hand"]
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">It’s not worth getting upset about.<br>'
                'It’s not worth arguing about. He won’t change his mind.<br>It’s not worth doing. Nobody is interested.<br>'
                'It’s not worth the trouble. It’s a long way to travel.<br>It’s not worth a hundred pounds. It’s really bad '
                'quality.</p></div>')
    read = SEC("Reading", "",
               '<p class="intro">You are going to read a questionnaire from a magazine to find out your attitudes to shopping, '
               'fashion and money.</p>' +
               EX("b44-ra", "A", "Work in two groups: Group A and Group B. See how many of the words in the box you know. Look "
                  "up any words you do not know in the <i>Vocabulary Builder</i>.",
                  '<div class="cols"><div><h4>Group A</h4>' + X.wordbox(group_a) + '</div><div><h4>Group B</h4>' +
                  X.wordbox(group_b) + "</div></div>") +
               EX("b44-rb", "B", "Now work in pairs: one person from Group A, the other from Group B. Go through the "
                  "questionnaire together and discuss your answers. Explain the new words from exercise A to each other if you "
                  "need to.", "") +
               EX("b44-rc", "C", "When you have finished, look at File 4 on p. 157. Calculate your marks and read the appropriate "
                  "description. Tell your partner if the description of you is accurate. Why? / Why not?",
                  REVEAL(file4(), "File 4, p. 157 — результаты")) + patterns)
    return PAGE_BOX(44, '<div class="cols"><div>' + voc + '</div><div>' + read + "</div></div>")


def p45():
    return PAGE_BOX(45, questionnaire())


def p46():
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(9, 1, 3, 13, split=58))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two friends, Leo and Noel, talking about buying tickets for a gig. <i>A '
              'gig</i> is a rock concert, usually in a small venue.</p>' +
              EX("b46-la", "A", "Work in pairs. Discuss these questions:", UL([
                  "Do you ever go to gigs? What was the last band you saw?",
                  "What is the most you have ever paid for a ticket for something?",
                  "Where is the best place to buy tickets for concerts / sports events?"])) +
              EX("b46-lb", "B", '<span class="audio-ic">♪</span> 6.3 Listen and answer these questions.', OL([
                  "Who does Leo want to see?", "Is Noel going to the gig?", "Why is Leo surprised that tickets have sold out?",
                  "Why does Leo want to go to the gig?", "What two things does Noel suggest he should do?",
                  "How does Leo respond to each of Noel’s suggestions?"]) + bkey) + S63() +
              EX("b46-lc", "C", "Work in pairs. Discuss these questions:", UL([
                  "Do you think Noel’s suggestions to Leo were good?", "Do you ever use online auction sites like eBay? What for?",
                  "What is the best birthday present you have ever received?"])))
    gr = SEC("Grammar", "<i>must</i>",
             '<p class="intro">In <i>Listening</i>, you heard the speakers say:</p>' + X.must_rules("b46-ga") +
             X.must_uses("b46-gb") + EX("b46-gc", "C", "Work in pairs. Compare your answers.", "") + HELP(145))
    return PAGE_BOX(46, '<div class="cols"><div>' + lis + '</div><div>' + gr + "</div></div>" + IMG(IMG_DIR + "p46-band.jpg", ""))


def p47():
    gr = (X.must_gaps("b47-gd") +
          EX("b47-ge", "E", "Make a list of the following. Then work in pairs to discuss your ideas.", UL([
              "two things you must remember to do this week", "two things you mustn’t forget to do this week",
              "five things visitors to your town simply must do / see / try"])) +
          EX("b47-gf", "F", "Work in pairs. Look at the photos below. Have conversations like this …",
             DLG(("A", "How old do you think …… is?"), ("B", "I’m not sure. He / She must be something like …")) +
             "<p><b>Explain your guesses.</b></p>" +
             '<div class="box"><p><b>If you use <i>must</i> and <i>mustn’t</i> to tell other people what to do, it often sounds '
             'rude and aggressive. It is better to use other structures in these situations. For example:</b></p><hr>'
             '<p class="ex-line"><i>Don’t buy</i> it here. It’s too expensive. <i>Wait</i> till you get back home.<br>(<i>If I were '
             'you,) I’d take it back</i> to the shop and ask for a refund.<br>I’m sorry, but smoking’s <i>not allowed</i> in the '
             'store.</p></div>' + IMG(IMG_DIR + "p47-faces.jpg", "", cls="md")))
    dc = SEC("Developing conversations", "Responding to recommendations",
             '<p class="intro">When you ask two or more people to recommend things, you often get different opinions. Look at '
             'this example:</p>' +
             DLG(("A", "I’m thinking of going shopping for clothes while I’m here. Can you recommend anywhere?"),
                 ("B", "Well, you could try Oxford Street. There are lots of big department stores there."),
                 ("C", "No, you don’t want to go there! It’s a rip-off! I’d go to a street market instead. There’s more choice – "
                       "and they’re cheaper.")) + X.rec_order("b47-da"))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>You don’t want to</i></b></p><p>When we want to tell '
              'friends what we think they should or should not do, we often use sentences beginning with <i>You want to</i> or '
              '<i>You don’t want to</i>.</p><p><i>You want to be careful if you go to the market.<br>You don’t want to get ripped '
              'off.<br>You don’t want to buy that! It doesn’t suit you.</i></p></div>')
    spk = SEC("Speaking", "",
              EX("b47-sa", "A", "Work in groups of three. You are going to role-play a conversation between a tourist and two "
                 "local people where you live.",
                 "<p><b>Student A:</b> you are the tourist. You want to go shopping for some different things. Ask for "
                 "recommendations.</p><p><b>Students B and C:</b> you are locals. Suggest some different places. Explain why your "
                 "ideas are good – and why the other ideas are bad!</p>"))
    return PAGE_BOX(47, '<div class="cols"><div>' + gr + '</div><div>' + dc + native + spk + "</div></div>")


def build():
    return p42() + p43() + p44() + p45() + p46() + p47()
