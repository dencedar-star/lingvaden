"""Страница «Учебник»: Unit 02 Feelings, pp. 14–19. Длинные тексты — из OCR и ключей."""
import re
from lib import C, EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, text, lines, script, fixed, _fix, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit02/"

FIX[16] = [("1 was just on my own", "I was just on my own"), (" - ", " – "), ("(’One man’)", "(‘One man’)")]
FIX[17] = [("leam from", "learn from"), ("learned, “ he said", "learned,” he said"), (" - ", " – "),
           ("inspiring on the site", "inspiring on the site."), ("get professional help", "get professional help."),
           ("get by. the mistakes", "get by, the mistakes")]
FIX[19] = [(" - ", " – ")]
FIX.setdefault(160, []).append(("i haven’t spoken", "I haven’t spoken"))
FIX[161] = [("Chris and i", "Chris and I"), ("C: 1 know", "C: I know"), ("I know, 1 know", "I know, I know"),
            ("1 was really", "I was really"), ("l’ve just", "I’ve just"), ("where l am", "where I am"),
            ("1 can imagine", "I can imagine"), ("Louisel", "Louise!"), ("L• Oh", "L: Oh"), ("5: ", "S: "),
            ("relationshipl", "relationship!"), ("50 ...", "So ..."), ("would be good", "would be good."), (" - ", " – ")]

ARTICLE_BOLD = ["meaningful connections", "desperate attempt", "international star", "miserable year", "true identity",
                "social skills", "professional help", "original plan"]


def article():
    first = text(16, (515, 425, 790, 545)) + " " + text(16, (420, 543, 790, 557))
    ps = [first] + paras(16, (420, 557, 790, 750), indent=8) + paras(17, (55, 430, 345, 1060), indent=8)
    ps = [fixed(16 if i < 3 else 17, p) for i, p in enumerate(ps)]
    html = ""
    for p in ps:
        for w in ARTICLE_BOLD:
            p = p.replace(w, f"<b>{w}</b>", 1)
        html += f"<p>{p}</p>"
    html = html.replace("<b>professional help</b>.", "<b>professional help</b>.", 1)
    return ('<div class="article"><span class="tag">Today’s story</span>'
            + IMG(IMG_DIR + "p16-title.jpg", "It Only Takes Juan Mann To Change The World!", cls="md") +
            f'<div class="colum">{IMG(IMG_DIR + "p16-sign.jpg", "Free hugs", cls="flt")}{html}</div>'
            '<div class="cols">' + IMG(IMG_DIR + "p16-hug.jpg", "") + IMG(IMG_DIR + "p17-hug.jpg", "") + "</div></div>")


def heaven_hell():
    def entries(box):
        out = []
        for l in lines(19, box):
            t = fixed(19, _fix(l["t"])).strip()
            if re.match(r"^[.…•]", t):
                out.append(re.sub(r"^[.…•\s]+", "", t))
            elif out:
                out[-1] += " " + t
        res = []
        for e in out:
            m = re.match(r"^(.*[.!?])\s+([A-Z][\w’ -]+, \d+, [\w ]+)$", e)
            q, who = (m.group(1), m.group(2)) if m else (e, "")
            res.append(f"<p>…<b>{q}</b> <small>{who}</small></p>")
        return "".join(res)
    return ('<div class="cols">'
            f'<div class="story">{IMG(IMG_DIR + "p19-heaven.jpg", "")}<h4>My idea of heaven is:</h4>{entries((40, 720, 405, 1080))}</div>'
            f'<div class="story">{IMG(IMG_DIR + "p19-hell.jpg", "")}<h4>My idea of hell is:</h4>{entries((435, 720, 792, 1062))}</div>'
            "</div>")


def S21():
    return SCRIPT("2.1", "R = Ryan, C = Clara · B = Belinda, A = Alisha",
                  script(160, (397, 900, 794, 1050)) + script(161, (0, 80, 397, 775)), "160–161")


def S23():
    return SCRIPT("2.3", "S = Sarah, L = Louise",
                  script(161, (0, 780, 397, 1050)) + script(161, (397, 80, 794, 760)), "161")


RESP = [("I can’t drink at the moment. I’m pregnant.", "Really? Congratulations!", "When is the baby due?"),
        ("I’m going to Canada to study English.", "Wow, that’s great!", "How long are you going for?"),
        ("I’m afraid I can’t meet you tonight.", "Oh, what a shame!", "Are you sure?"),
        ("My brother’s not very well.", "Oh no! I’m really sorry.", "I hope it’s not too serious."),
        ("I’ve lost my wallet.", "Oh no, what a pain!", "Did it have much in it?"),
        ("I’ve found my wallet!", "Phew, that’s a relief!", "Where was it?")]


def p14():
    words = ["exhausted", "worried", "fed up", "confused", "terrible", "relaxed", "stressed", "in a good / bad mood", "upset",
             "furious", "annoyed", "disappointed", "pleased", "down", "guilty"]
    vkey = REVEAL("<p>" + "</p><p>".join(" ".join(rows(2, 0, a, b)) for a, b in ((41, 46), (46, 50))) + "</p>", "Ответ (ключ)")
    voc = SEC("Vocabulary", "Feelings",
              EX("b14-va", "A", "How are the people in the pictures feeling? Why? Can you use any of the words in the box to describe them?",
                 '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in words) + "</div>" +
                 IMG(IMG_DIR + "p14-shop.jpg", "Picture 1") + IMG(IMG_DIR + "p14-retirement.jpg", "Picture 2") + vkey) +
              EX("b14-vb", "B", "Which of the words in A may show you are feeling: <i>tired, ill, sad, happy, unsure, angry,</i> "
                 "or <i>bad about something you did?</i>", "") +
              EX("b14-vc", "C", "Have you had any of these feelings recently? Why?", ""))
    box = ('<div class="box"><p><b><i>Be, feel, look, seem,</i> and <i>sound</i> are all linking verbs that can be followed '
           'directly by an adjective.</b></p></div>')
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p>'
                '<p class="ex-line">She expected to get a better mark.<br>I expected London to be more modern.<br>'
                'I didn’t expect to have so much homework.<br>We didn’t expect it to take so long.<br>'
                'We didn’t expect you to be so early.</p></div>')
    gr = SEC("Grammar", "be, look, seem etc", box + X.bls_match("b14-ga") +
             EX("b14-gb", "B", "Write your own responses to 1–8. Practise in pairs.", "") + HELP(138) + patterns)
    return PAGE_BOX(14, IMG(IMG_DIR + "p14-banner.jpg", "02 Feelings") +
                    '<div class="cols"><div>' + voc + '</div><div>' + gr + "</div></div>")


def p15():
    lkey_a = REVEAL(" ".join(rows(2, 1, 2, 4)), "Ответ (ключ)")
    lkey_b = REVEAL(" ".join(rows(2, 1, 6, 8)), "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two conversations. The first is between two people talking about their '
              'friend Karim. The second is between two women, Belinda and Alisha.</p>' +
              EX("b15-la", "A", '<span class="audio-ic">♪</span> 2.1 Listen. How do these people feel?',
                 '<p><b>Conversation 1:</b> Karim<br><b>Conversation 2:</b> Belinda, Alisha</p>' + lkey_a) +
              EX("b15-lb", "B", "Do you remember why they feel this way? Listen again and check.", lkey_b) + S21())
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>How come?</i></b></p>'
              '<p>People often use <i>How come?</i> instead of <i>Why?</i></p>' +
              DLG(("A", "<i>I can’t come to your wedding, I’m afraid.</i>"), ("B", "<i>Oh what a shame. How come?</i>"),
                  ("A", "<i>I’ve got an exam that day.</i>")) + "</div>")
    spk = SEC("Speaking", "", EX("b15-sa", "A", "Work in pairs. Discuss these questions.", UL([
        "Do you find it easy to talk about your feelings? Who do you talk to if you have a problem?",
        "What would you do or say if a friend was upset? Would it be different if it was a man or a woman?",
        "What kind of things do you do to cheer yourself up?", "Are you good at sorting out problems?"])) +
        IMG(IMG_DIR + "p15-worried.jpg", "", cls="sm"))
    dc = SEC("Developing conversations", "Response expressions",
             '<div class="box"><p><b>We use lots of short expressions to respond to news.</b></p></div>' +
             EX("b15-da", "A", "Look at the following conversations and try to translate the expressions in <b>bold</b>. "
                "Are there any you cannot translate?",
                OL([DLG(("A", a), ("B", f"<b>{b}</b> {c}")) for a, b, c in RESP])) + IMG(IMG_DIR + "p15-friends.jpg", ""))
    pron = SEC("Pronunciation", "Responding",
               '<div class="box"><p><b>With positive responses our voice goes higher.</b></p><hr>'
               '<p><b>With negative responses our voice goes lower.</b></p></div>' +
               EX("b15-pa", "A", '<span class="audio-ic">♪</span> 2.2 Listen to the six responses from <i>Developing '
                  'conversations</i> and copy the stress and intonation.',
                  SCRIPT("2.2", "responses", [("B", b) for _, b, _ in RESP], "15")) +
               EX("b15-pb", "B", "Work in pairs. Practise 1–6 from <i>Developing conversations</i>. Try to continue them.", ""))
    cp = SEC("Conversation practice", "",
             EX("b15-ca", "A", "Work in pairs. Think of a piece of good or bad news. Write a conversation like the ones you "
                "heard in <i>Listening</i>. Include response expressions.", "") +
             EX("b15-cb", "B", "Try to remember your conversation. Act it out in front of another pair of students.", ""))
    return PAGE_BOX(15, '<div class="cols"><div>' + IMG(IMG_DIR + "p15-boy.jpg", "") + lis + native + spk +
                    '</div><div>' + dc + pron + cp + "</div></div>")


def p16():
    spk = SEC("Speaking", "",
              EX("b16-sa", "A", "Check you understand the words and expressions in <b>bold</b>. Then discuss the questions in groups.",
                 OL(["How often do you do these things? In what situations?" + UL([
                     "<b>hug</b> people", "<b>kiss</b> people <b>on the cheek</b> or <b>lips</b>",
                     "walk <b>arm in arm</b> with people or <b>hold hands</b>", "<b>shake hands</b> or <b>bow</b>",
                     "touch people on the arm or <b>put</b> your arm <b>round</b> their shoulder"]),
                     "Do you do any of these things more often or less often than most people in your country? Why?<br>"
                     "<i>I think I’m fairly typical. / I’m maybe a little bit unusual.</i>",
                     "Have you been anywhere where they do these things differently to you? Where? What do they do?"])))
    ckey = REVEAL(OL([r[2:] for r in numbered(rows(2, 1, 13, 26))]), "Ответы (ключ)")
    read = SEC("Reading", "",
               EX("b16-ra", "A", "Work in pairs. Look at the text <i>It only takes Juan Mann to change the world!</i> "
                  "Discuss these questions.", UL([
                      "What is the man doing in the pictures? Why?", "What would you do if you saw someone like this?",
                      "Are any people like him famous in your local area / country? What for? How do people feel about them?"])) +
               EX("b16-rb", "B", "Read and see if you feel differently about the man afterwards.", "") +
               article() +
               EX("b16-rc", "C", "Work in pairs. Discuss these questions. Then read the article again to check your answers.",
                  OL(["What made Juan Mann start his campaign?", "How did he feel when he went out the first time?",
                      "Who first asked for a hug and why?", "How did Mann become so famous?",
                      "Why does he feel surprised and lucky about what he does now?",
                      "What is Mann’s theory about why people want hugs?"]) + ckey) +
               X.reading_adj("b16-rd"))
    return PAGE_BOX(16, '<div class="cols-31"><div>' + spk + '</div><div>' + IMG(IMG_DIR + "p16-couple.jpg", "") +
                    "</div></div>" + read)


def p17():
    voc = SEC("Vocabulary", "Adjective collocations",
              X.collocations("b17-va", "A", "In the text, you read that 2004 was a <i>depressing</i> time for Juan Mann. "
                             "Match these <i>-ing</i> adjectives with the nouns.") +
              EX("b17-vb", "B", "Write eight true sentences using the new collocations.", ""))
    box = ('<div class="box"><p><b>Some adjectives, including those ending in <i>-ing</i>, only describe things which cause a '
           'feeling:</b></p><p class="ex-line">The film was so <i>boring</i> that I fell asleep.</p><hr>'
           '<p><b>The <i>-ed</i> and other adjectives in Vocabulary exercise A on p. 14 describe people’s feelings:</b></p>'
           '<p class="ex-line">I’m <i>exhausted</i>. I need to go to bed.</p></div>')
    gr = SEC("Grammar", "-ing / -ed adjectives", box + X.ing_ed("b17-ga") +
             X.pictures("b17-gb", img=IMG(IMG_DIR + "p17-class.jpg", "")) + HELP(138))
    spk = SEC("Speaking", "", EX("b17-sa", "A", "Work in pairs. Discuss these questions.", UL([
        "Does your town or area have any similar problems to Sydney?",
        "At one point the city council tried to stop Juan Mann’s free hugs campaign. Why do you think they did that?",
        "Has your government tried to stop something popular? Why? Was it successful?",
        "Can you think of any other news stories which have been spread through the Internet?",
        "Have you ever posted anything on the Internet? What?"])))
    return PAGE_BOX(17, voc + gr + spk)


def p18():
    ckey = REVEAL("<p>" + " ".join(rows(3, 0, 8, 11)) + "</p><p>" + " ".join(rows(3, 0, 11, 16)) + "</p>", "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two friends talking. Sarah has just met Louise in front of a shop.</p>' +
              EX("b18-la", "A", "What things do you think they will say? Have the conversation.", "") +
              X.listen_adj("b18-lb") +
              EX("b18-lc", "C", "Why are they <i>annoyed, happy, being mysterious,</i> etc.? Listen again if you need to.", ckey) + S23())
    bkey = REVEAL("<br>".join(rows(3, 0, 33, 36)), "Ответ (ключ)")
    pc = SEC("Grammar", "Present continuous", X.pc_gaps("b18-ga") +
             EX("b18-gb", "B", "Work in pairs. Discuss the questions.",
                OL(["Which examples of the present continuous in 1–8 in exercise A:" + OL([
                    "show an action is temporary and / or unfinished?",
                    "show something in the future that involves an arrangement with other people?"], "items alpha"),
                    "Which sentence in exercise A uses the verb <i>be</i> in the present continuous form? Why?"]) + bkey) + HELP(139))
    box = ('<div class="box"><p><b>Double questions are very common in English. Notice these examples from <i>Listening</i>.</b></p><hr>'
           '<p class="ex-line">So what <i>are you doing</i> here? <i>Are you window shopping?</i><br>'
           'What <i>are you doing</i> on Friday? <i>Do you fancy</i> meeting?</p></div>')
    dq = SEC("Grammar", "Present continuous / present simple questions", box + X.double_q("b18-qa") + X.double_match("b18-qb") +
             EX("b18-qc", "C", "Work in pairs. Have conversations asking and answering 1–4 below. Add second questions to make "
                "double questions. Try to continue each conversation for as long as you can. For example:",
                DLG(("A", "<i>What are you doing these days? Are you still studying?</i>"),
                    ("B", "<i>No, I’m working in a bank now. And what are you doing these days? Are you still teaching?</i>"),
                    ("A", "<i>Yes, but I’m not enjoying it!</i>")) +
                OL(["What are you doing these days?", "What are you doing here?", "What are you doing after the class?",
                    "What’s the matter with him?"])))
    return PAGE_BOX(18, '<div class="cols"><div>' + IMG(IMG_DIR + "p18-friends.jpg", "") + lis + pc +
                    '</div><div>' + dq + "</div></div>")


def p19():
    reqs = [("Do you think you could help me with this?", "No, sorry, but I can’t. …"),
            ("We’re going out for dinner later. Would you like to join us?", "Oh, I’d love to, but I can’t. …"),
            ("Can I just check my email on your computer?", "No, sorry. …"),
            ("Do you really like this kind of music? Can I just turn it off?", "No, don’t! …"),
            ("This is rubbish! Is it OK if I change the channel?", "No, it’s not! …"),
            ("I was wondering if you wanted to go out somewhere with me on Friday?", "Oh, it’s nice of you to ask me, but I can’t. …")]
    dc = SEC("Developing conversations", "Making excuses",
             '<div class="box"><p><b>Look at the example from <i>Listening</i>. We often use the present simple or continuous to '
             'explain why we can’t or don’t want to do something.</b></p><hr>' +
             DLG(("A", "<i>What are you doing on Friday? Do you fancy meeting? It’d be nice to hear more of your news.</i>"),
                 ("B", "<i>I’m afraid I can’t. I play badminton on Fridays.</i> or <i>I’m going away for the weekend.</i>")) +
             "</div>" +
             EX("b19-da", "A", "Give reasons for refusing the following requests:", OL([DLG(("A", a), ("B", b)) for a, b in reqs])) +
             EX("b19-db", "B", "Work in pairs. Take turns reading out the questions. Read your response and continue the conversation.", ""))
    spk = SEC("Speaking", "",
              EX("b19-sa", "A", "Look at the pictures below. Are they your idea of holiday heaven or of holiday hell? Why?", "") +
              EX("b19-sb", "B", "Read the short text about other people’s ideas of heaven and hell. Work in pairs. Discuss which "
                 "of the ideas you agree with. What is your favourite comment? Why?", "") +
              EX("b19-sc", "C", "Write your own idea of heaven and hell. Explain why. Use language from this unit or the text such as:",
                 '<p class="starters"><b>verbs:</b> <i>love, annoy, hate, can’t stand, depress, bore,</i> etc.<br>'
                 '<b>adjectives:</b> <i>relaxing, annoying, boring, fantastic, amazing,</i> etc.</p>' +
                 '<div class="writer" data-target="" data-id="u02-heaven"><textarea placeholder="My idea of heaven is … My idea of hell is …">'
                 '</textarea><div class="cnt"></div></div>') +
              EX("b19-sd", "D", "Tell different students your ideas. Do they agree with you?", ""))
    return PAGE_BOX(19, '<div class="cols"><div>' + dc + '</div><div>' + spk + "</div></div>" + heaven_hell())


def build():
    return p14() + p15() + p16() + p17() + p18() + p19()
FIX[161].append(("just .. well", "just ... well"))
