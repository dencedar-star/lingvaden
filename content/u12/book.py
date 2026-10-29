"""Страница «Учебник»: Unit 12 People I know, pp. 82–87. Длинные тексты — из OCR и ключей."""
import re
from lib import EX, OL, UL, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import text, lines, script, fixed, _fix, FIX
from . import shared as X

IMG_DIR = "../assets/img/unit12/"

FIX.setdefault(86, []).extend([("over 500 friends’", "over 500 ‘friends’"), (" - ", " – "), ("— scare me even —", "– scare me even –"),
                               ("paranoid —I worry", "paranoid – I worry")])
FIX.setdefault(87, []).extend([(" - ", " – "), (" — ", " – "), ("l’d rather", "I’d rather")])
FIX.setdefault(170, []).extend([("maybe 1 am", "maybe I am")])
FIX.setdefault(171, []).extend([("1 met him while", "I met him while"), ("until 1 went", "until I went"), ("so l’d talk", "so I’d talk"),
                                ("important -", "important –"), ("At some point. I had", "At some point, I had"), ("| regret that, really. Anyway.",
                                                                                   "I regret that, really. Anyway,"), (" - ", " – ")])

BOLD = ["endlessly", "distant friend", "struggles with", "ego trip", "came across", "paranoid", "track down", "drift apart"]


def _bold(s):
    for w in BOLD:
        s = s.replace(w, f"<b>{w}</b>", 1)
    return s


def article():
    secs = [("First things first", 86, (465, 498, 762, 690), ["However, there are"]),
            ("Social networking sites", 86, (465, 722, 762, 1045), ["Added to this"]),
            ("Turning back the clock", 87, (30, 500, 400, 645), []),
            ("Keeping it simple", 87, (30, 676, 400, 790), [])]
    out = []
    for h, p, box, breaks in secs:
        t = fixed(p, text(p, box))
        for b in breaks:
            t = t.replace(" " + b, "</p><p>" + b)
        out.append(f"<h4>{h}</h4><p>{_bold(t)}</p>")
    return ('<div class="article"><h3 class="art-title"><small>Opinion</small> Give me my space</h3>' +
            '<div class="cols">' + IMG(IMG_DIR + "p86-opinion.jpg", "") + IMG(IMG_DIR + "p87-myspace.jpg", "") + "</div>" +
            '<div class="colum">' + IMG(IMG_DIR + "p86-writer.jpg", "", cls="sm") + "".join(out) + "</div>" +
            IMG(IMG_DIR + "p87-sofa.jpg", "", cls="md") + "</div>")


def S121():
    return SCRIPT("12.1", "L = Lewis, J = Jessica", script(170, (390, 380, 794, 1050)), "170")


def S122():
    return SCRIPT("12.2", "", [("J", fixed(171, text(171, (40, 95, 397, 145))))], "171")


def S123():
    out = []
    for l in lines(171, (40, 175, 397, 850)):
        t = fixed(171, _fix(l["t"])).strip()
        m = re.match(r"^(\d) ([A-Z][a-z]+)$", t)
        if m:
            out += [("#", m.group(1)), (m.group(2), "")]
        elif out:
            sp, prev = out[-1]
            out[-1] = (sp, (prev + " " + t).strip())
    return SCRIPT("12.3", "", out, "171")


def p82():
    spk = SEC("Speaking", "", EX("b82-sa", "A", "Work in groups. Find out who has the biggest family. Ask about:", UL([
        "brothers and sisters", "nieces and nephews", "aunts and uncles", "great-grandparents", "grandparents", "cousins"]) +
        "<p><b>Does anyone have a half-brother / half-sister or a stepbrother / stepsister?</b></p>"))
    voc = SEC("Vocabulary", "Describing character", X.character("b82-va") +
              EX("b82-vb", "B", "Work in pairs. Discuss these questions:", UL([
                  "Which adjectives could you use to describe the people in the pictures on these pages? Use these verbs: "
                  "<i>He looks … / They look like they could be …</i>", "Which adjectives would you use to describe yourself?"])))
    return PAGE_BOX(82, IMG(IMG_DIR + "p82-banner.jpg", "12 People I know") + spk + voc + IMG(IMG_DIR + "p82-photos.jpg", ""))


def p83():
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">He’s very sweet and affectionate, but '
                'he can be quite naughty sometimes.<br>She’s nice, but she can be really rude sometimes.<br>You can be such an '
                'idiot sometimes!<br>You can be so stubborn sometimes!<br>He can be very nice when he wants to be.<br>She can be '
                'very generous when she wants to be.</p></div>')
    dc = SEC("Developing conversations", "<i>That’s like …</i>",
             '<div class="box"><p><b>When we talk about the character of someone we know, we often compare the person to someone '
             'with a similar character. To introduce these comments, we often use <i>That’s like …</i></b></p></div>' +
             X.thats_like("b83-da") +
             EX("b83-db", "B", "Work in pairs.", "<p><b>Student A:</b> read out 1–5.<br><b>Student B:</b> say a–e, but change "
                "the people so the sentences are true for you.</p>"))
    akey = REVEAL(OL(["Because she went out to phone her brother as it was his birthday.",
                      "They both talk a lot / are very chatty.", "He’s clever and bright but not intense. He’s friendly and outgoing.",
                      "He’s lazy and a bit of a dropout and into politics.",
                      "They used to be close but now they don’t really get on and she finds him a bit boring."]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a man called Lewis talking to a woman called Jessica about her family.</p>' +
              EX("b83-la", "A", '<span class="audio-ic">♪</span> 12.1 Listen and answer the questions.', OL([
                  "Why does Lewis start asking about Jessica’s brother, Noel?", "In what way is Lewis’s mum similar to Noel?",
                  "What is Noel like?", "What is Jessica’s younger brother like?", "How has her relationship with him changed?"]) +
                 akey) +
              X.heard("b83-lb", instr="Choose the words that you heard. Then listen again to check your answers.") + S121() +
              EX("b83-lc", "C", "Work in pairs. Discuss these questions:", UL([
                  "As a child, which is worst: being the oldest, the youngest or in the middle?",
                  "Do you know anyone who has won a scholarship?",
                  "Do you know anyone who went through a phase of being or doing something different?"])))
    cp = SEC("Conversation practice", "",
             EX("b83-ca", "A", "Have conversations about your family. Start by saying things like:",
                "<p class=\"ex-line\"><i>I’m going to my cousin’s on Saturday.<br>Sorry, that was my sister (on the phone).</i></p>"
                "<p><b>Continue the conversations by asking questions such as:</b></p><p class=\"ex-line\"><i>What’s she like? "
                "Do you get on well?<br>Are you close? Do you see her / him a lot?<br>What does he / she do?<br>Where do they "
                "live? Is it near here?<br>Have you got any other brothers and sisters, etc.?</i></p><p><b>Make comparisons "
                "with friends and family when you can.</b></p><p class=\"ex-line\"><i>That sounds like my dad. He’s always …</i></p>"))
    return PAGE_BOX(83, '<div class="cols"><div>' + IMG(IMG_DIR + "p83-family.jpg", "") + patterns + dc + '</div><div>' +
                    IMG(IMG_DIR + "p83-couple.jpg", "") + lis + cp + "</div></div>")


def p84():
    gbox = ('<div class="box"><p><b><i>Used to</i> or the past simple can be used to describe someone’s character in the past, '
            'especially when there has been a change since then. <i>Used to</i> and <i>would</i> and the past simple can all '
            'describe regular activities / habits in the past. We tend to start with <i>used to</i> and then use <i>would</i> or '
            'the past simple to give details.</b></p></div>')
    ckey = REVEAL(OL(["My gran used to be / was very religious. She used to / would go to church every Sunday and she always "
                      "made / would always make us say a prayer before dinner.",
                      "My grandfather was / used to be very indulgent. He would always buy / always used to buy us sweets and "
                      "he would / used to let us watch TV all day.",
                      "When I was a kid we would / used to go to the mountains every summer. We would / used to go walking and "
                      "we would / used to dive and swim in the river. It was fantastic.",
                      "I used to play basketball a lot. I would / used to train twice a week. We would / used to have a match "
                      "every Sunday. We won the league once.",
                      "We used to sit together at school. We would always / always used to talk to each other. We would / used "
                      "to pass each other notes and the teacher would / used to tell us off."]), "Ответы (ключ)")
    gr = SEC("Grammar", "<i>Used to</i> and <i>would</i>", X.used_to_a("b84-ga") + gbox + X.used_to_b("b84-gb") +
             EX("b84-gc", "C", "Make sentences like those in exercises A and B using <i>used to, would</i> and the past simple. "
                "For example:", '<p class="ex-line">be close – my brother – play together – go fishing a lot<br><i>I used to be '
                'close to my brother. We’d play / we played together and we’d go / we went fishing together a lot.</i></p>' + OL([
                    "my gran – very religious – go to church – Sunday – always make us say a prayer before dinner",
                    "my grandfather – be very indulgent – always buy us sweets – let us watch TV all day",
                    "when – I – a kid, we – go to mountains every summer – go walking – dive and swim in the river – be fantastic",
                    "I – play basketball a lot – train twice a week – have a match every Sunday – we – win the league once",
                    "we – sit together at school – always talk to each other – pass notes – teacher – tell us off"]) +
                '<div class="writer" data-target="" data-id="u12-usedto"><textarea rows="5"></textarea></div>' + ckey) +
             EX("b84-gd", "D", "Work in pairs. Tell your partner about two of the things below. Use <i>used to</i> and "
                "<i>would</i> to explain character and habits.", UL([
                    "someone you know whose character has changed", "your memories of a grandparent",
                    "your memories of summer holidays with family", "the lunch break when you were at primary school",
                    "a free-time activity you no longer do"])) + HELP(151) + S122())
    return PAGE_BOX(84, gr + IMG(IMG_DIR + "p84-lake.jpg", ""))


def p85():
    ckey = REVEAL("<p>He has worked in a café. He is Belgian. He has been to England and Rome, where he was on an Erasmus "
                  "programme. He used to have a girlfriend called Sandra and he now has a girlfriend called Brigitta, who he met "
                  "at university and who he’s been with for two years, though he’s known her for longer. He once shared a flat "
                  "with Jef. He’s outgoing, adventurous, bright, funny, likes travelling, and has a lot of friends. He’s loyal to "
                  "them.</p>", "Ответ (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear five people talking about how they became friends with a Belgian man '
              'called Nicolas.</p>' +
              EX("b85-la", "A", "Before you listen, work in groups. Talk about how you got to know your closest friend, "
                 "girlfriend / boyfriend or partner.", "") + X.nicolas("b85-lb") +
              EX("b85-lc", "C", "Work in pairs. Discuss these questions. Listen again if you need to.", UL([
                  "What do you learn about Nicolas’s life?", "What is Nicolas like?"]) + ckey) + S123())
    akey = REVEAL("<p><i>Stay</i> and <i>keep</i> share the most collocations. The odd one out is <i>maintain</i>.</p>",
                  "Ответ (ключ)")
    voc = SEC("Vocabulary", "Synonyms",
              EX("b85-va", "A", "Look at these sentences from <i>Listening</i>. What meaning do the words in <i>italics</i> share?",
                 OL(["It’s difficult <i>maintaining</i> a long-distance relationship.", "We’ve <i>remained</i> friends.",
                     "We <i>kept</i> in touch via e-mail.", "I sometimes wish we’d <i>stayed</i> together."], "items alpha")) +
              X.synonyms("b85-vb", instr="Decide which word in <i>italics</i> from exercise A completes each set of collocations "
                         "1–4 below. Then discuss these questions as a class: Which two words share the most collocations? Which "
                         "word does not share any collocations with the other words?") + akey +
              '<div class="box"><p><b>Although synonyms share meanings and can share collocations, they are often not '
              'interchangeable. They will have different collocations or use a different grammar. If you want to understand the '
              'differences, you need to notice these contexts.</b></p></div>' +
              EX("b85-vc", "C", "Work in pairs. Discuss these questions:", UL([
                  "Do you find it easy to stay calm under pressure?", "Do you know anyone who keeps getting into trouble?",
                  "Can you think of anything that remains a serious problem / big challenge in your country?",
                  "Do you find it difficult to maintain a conversation in English?"])))
    gr = SEC("Grammar", "Expressing regrets (<i>wish</i>)",
             EX("b85-ga", "A", "Look at the sentences from <i>Listening</i> and answer the questions.",
                '<p class="ex-line">I sometimes wish <i>we’d stayed</i> together.<br>I wish we <i>hadn’t split up</i>.<br>We’d talk '
                'about the things we wished <i>we’d said</i> to him.</p>' +
                OL(["What tense follows <i>wish</i> here?", "Is it referring to past or present situations?",
                    "Did the actions that follow <i>wish</i> happen or not?"])) +
             X.regrets("b85-ga4", "4") + HELP(151) +
             EX("b85-gb", "B", "Decide why someone might say each sentence 1–10 and what actually happened.", OL([
                 "I wish I’d known.", "I wish I’d met him.", "I wish I’d never asked.", "I wish they’d told me earlier.",
                 "I wish I’d tried harder at school.", "I really wish we hadn’t moved house.",
                 "Honestly, I wish I hadn’t said anything.", "I wish I hadn’t gone to the meeting.",
                 "I sometimes wish they’d given me a different name.", "I think he sometimes wishes he’d studied something else."])) +
             EX("b85-gc", "C", '<span class="audio-ic">♪</span> 12.4 Listen and repeat the sentences. Notice how we often do not '
                "pronounce the <i>’d</i> in <i>I’d</i> – or the <i>t</i> in <i>hadn’t</i>.", "") +
             EX("b85-gd", "D", "Write three sentences about things you wish you <i>had / had not done</i>. Work in pairs. Say as "
                "much as you can about your regrets.",
                '<div class="writer" data-target="" data-id="u12-wish"><textarea rows="4" placeholder="I wish I’d …"></textarea></div>'))
    return PAGE_BOX(85, '<div class="cols"><div>' + lis + voc + '</div><div>' + IMG(IMG_DIR + "p85-friends.jpg", "") + gr +
                    "</div></div>")


def p86():
    akey = REVEAL(OL(["b (… there are also lots of things about it that worry me … – paragraph two)",
                      "a (If one more person … I’ll scream! – paragraph three)",
                      "b (people only want you to join these sites to make them look even more popular – paragraph three)",
                      "a (I worry … in the future. – paragraph four)",
                      "b (People drift apart because … worth staying in touch! – paragraph five)",
                      "b (I don’t need to go … when to go out. – paragraph six)"]), "Ответы (ключ)")
    qs = [("Which sentence best describes how the writer feels about the Internet?", ["He can’t stand it.",
           "He’s got serious reservations about it.", "He’s got mixed feelings about it."], "b"),
          ("How does the writer feel when he gets invited to join social networking sites?", ["It drives him mad.",
           "He’s pleased to be asked to join.", "He feels quite guilty."], "a"),
          ("How does the writer explain the fact that some people have so many online friends?", ["They must be really popular.",
           "It helps them feel more important.", "Communicating online is better than talking face-to-face."], "b"),
          ("What worry about social networking sites does he have?", ["There could be unexpected consequences to publishing "
           "information online.", "Terrible pictures of parents could be posted online.",
           "People can already read private information about him online."], "a"),
          ("He doesn’t want to see old school friends again because …", ["it’s too much effort to find out where they are now.",
           "he feels they wouldn’t have much to talk about.", "they might be different now to when they last met."], "b"),
          ("The writer thinks he might shock some people because …", ["he doesn’t know how to use Instant Messenger.",
           "he doesn’t use the Web to organise his social life.", "he’s so talkative."], "b")]
    from lib import S
    rows = [f"{q}<br>" + "<br>".join(f"{l} {o}" for l, o in zip("abc", opts)) + f"<br>→ {S(k, ['a', 'b', 'c'])}" for q, opts, k in qs]
    read = SEC("Reading", "",
               EX("b86-ra", "A", "Read the article about the Internet and maintaining friendships. Choose the correct answer to "
                  "these questions. Underline the part of the article that tells you the answer.", OL(rows) + akey) +
               article() +
               EX("b86-rb", "B", "Mark the text with a ✓ where you agree with what is said, a ✗ where you disagree, and a ? where "
                  "you do not understand something. Discuss your ideas in pairs.", "") +
               X.text_defs("b86-rc"))
    return PAGE_BOX(86, read)


def p87():
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>if you ask me</i></b></p><p>We often introduce a personal '
              'opinion or criticism by using <i>if you ask me</i>. It means the same as <i>In my opinion</i>.</p><p><i>If you ask '
              'me, people only want you to join these sites to make them look even more popular!<br>If you ask me, it does more '
              'harm than good.<br>If you ask me, it’s stupid.</i></p></div>')
    spk = SEC("Speaking", "", X.friendship("b87-sa") +
              EX("b87-sb", "B", "Work in pairs. Discuss these questions:", UL([
                  "Do you have the same best friend as you did ten years ago? Why? / Why not?",
                  "Do you stay in touch with friends from primary or secondary school / university?",
                  "Have you ever been close to someone, but then drifted apart? Do you regret it?",
                  "Is there anyone you would like to get back in touch with?", "Have you ever tracked anyone down via the Internet?",
                  "Do you have any online friends? Have you met them face-to-face? How was it?"]) +
                 IMG(IMG_DIR + "p87-cartoon.jpg", "", "“I don’t want to be alone when I’m old, either, so when we’re old let’s get "
                     "back in touch.”", cls="md")))
    return PAGE_BOX(87, '<div class="cols"><div>' + native + '</div><div>' + spk + "</div></div>")


def build():
    return p82() + p83() + p84() + p85() + p86() + p87()
