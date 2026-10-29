"""Страница «Учебник»: Unit 05 Working life, pp. 36–41. Длинные тексты — из OCR и ключей."""
import re
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import lines, script, fixed, _fix, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit05/"

FIX[40] = [("I Hundreds", "Hundreds"), ("/ on my", "on my"), ("iy They", "They"), ("| They also", "They also"),
           ("I Many banks", "Many banks"), ("• | do about", "do about"), ("hours work’", "hours ‘work’"),
           ("funerals", "funerals."), ("chemicals. ”", "chemicals. “I"), ("l’ve", "I’ve"), ("*rubbish", "rubbish"),
           ("McCreary, “", "McCreary. “"), ("The Worst Jobs", "<i>The Worst Jobs"), ("in History returns", "in History</i> returns"),
           (" - ", " – ")]
FIX.setdefault(163, []).extend([("1: Oh yeah", "I: Oh yeah"), ("1 Thanks", "I: Thanks"), ("terriblel", "terrible!")])
FIX.setdefault(164, []).extend([("5 l: l often", "5 I: I often"), ("1: No, I know", "J: No, I know"), ("A: 1 know", "A: I know"),
                                ("Adam, It", "Adam. It")])
BOLD = ["drug trials", "side effects", "quick and easy way", "national average", "very grateful", "cramped conditions",
        "slam down the phone", "minimum wage", "got on with"]
JUNK = re.compile(r"^([LГ•|I1-9\s\-—_.]{0,8}|L[\s\-—_]+)$")


def block(p, box, title=None, split=()):
    ls = [fixed(p, _fix(l["t"])).strip() for l in lines(p, box)]
    ls = [t for t in ls if not JUNK.match(t) and t != title]
    s = ""
    for t in ls:
        s = s[:-1] + t if s.endswith("-") and not s.endswith(" -") else (s + " " + t).strip()
    for b in BOLD:
        s = s.replace(b, f"<b>{b}</b>", 1)
    for k in split:
        s = s.replace(" " + k, "</p><p>" + k)
    h = f"<h4>{title.capitalize() if title.isupper() else title}</h4>" if title else ""
    return f"{h}<p>{s}</p>"


def article():
    intro = block(40, (40, 390, 325, 625))
    jobs = (block(40, (350, 75, 765, 272), "HUMAN GUINEA PIGS") + block(40, (350, 295, 765, 492), "EMBALMERS") +
            block(40, (350, 515, 765, 725), "CALL CENTRE WORKER", split=("One worker",)) +
            IMG(IMG_DIR + "p40-recycling.jpg", "", cls="md") + block(40, (345, 780, 765, 1068), "RECYCLING PLANT WORKER"))
    return ('<div class="article"><h3 class="art-title">Terrible jobs not a thing of the past.</h3>'
            f'<div class="story">{intro}</div><div class="colum">{jobs}</div></div>')


def bullets(rs):
    out = []
    for r in rs:
        if r.startswith("•") or not out:
            out.append(r.lstrip("• "))
        else:
            out[-1] += " " + r
    return out


def S51():
    return SCRIPT("5.1", "I = Ivan, A = Amanda", script(163, (397, 340, 794, 1060)), "163")


def S52():
    return SCRIPT("5.2", "", script(164, (0, 80, 397, 445)), "164")


def S53():
    return SCRIPT("5.3", "", script(164, (0, 460, 397, 1060)) + script(164, (397, 80, 794, 395)), "164")


def p36():
    bkey = REVEAL(UL(bullets(rows(7, 1, 12, 28, split=59))), "Значения (ключ)")
    voc = SEC("Vocabulary", "Jobs", X.jobs("b36-va") +
              EX("b36-vb", "B", "Use the extra information in sentences 1–10 to guess the meanings of the words in <b>bold</b>. "
                 "Translate the sentences into your language.", OL([
                     "It’s very <b>competitive</b>. It’s difficult to find a good job.",
                     "It’s very <b>well-paid</b>. He gets £60,000 a year as well as a bonus at the end of the year.",
                     "It’s quite <b>rewarding</b>. You really help people and that makes you feel good.",
                     "It’s quite <b>insecure</b>. You are often self-employed or have a temporary contract and it’s quite badly-paid.",
                     "You don’t have any <b>responsibility</b>. Once your day’s finished, you don’t have to worry about anything.",
                     "You need to be quite <b>creative</b>. You have to think of a lot of new ideas and new ways of doing things.",
                     "It’s very <b>stressful</b>. You’re under a lot of time pressure.",
                     "It’s <b>physically demanding</b>. You have to be strong and fit.",
                     "It’s very <b>varied</b>. You get to do lots of different things.",
                     "There’s a lot of <b>paperwork</b> – writing reports, filling in forms, things like that."]) + bkey) +
              EX("b36-vc", "C", "Work in groups. Discuss these questions.", UL([
                  "Are the jobs in Exercise A good jobs to have in your country at the moment? Would you do any of them?",
                  "Do you know anyone who does any of these jobs? Who do they work for? Do they enjoy it?"])))
    akey = REVEAL(OL([r[2:] for r in numbered(rows(7, 1, 30, 36, split=59))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two people, Ivan and Amanda, talking about work.</p>' +
              EX("b36-la", "A", '<span class="audio-ic">♪</span> 5.1 Listen and answer the questions.', OL([
                  "What do they do now?", "What jobs have they done in the past?", "What are Ivan’s plans for the future? Why?",
                  "How old are they both now?"]) + akey) +
              X.ivan("b36-lb") + S51())
    return PAGE_BOX(36, IMG(IMG_DIR + "p36-banner.jpg", "05 Working life") +
                    '<div class="cols"><div>' + voc + '</div><div>' + lis + "</div></div>")


def p37():
    spk = (EX("b37-lc", "C", "Work in pairs. Discuss the questions:", UL([
        "Would you ever work for no money? Why? / Why not?",
        "Are there any jobs for life in your country? Do you think it is good? Why? / Why not?"])) +
        '<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
        'English. Compare your English to the original.</b></p><p class="ex-line">It’s quite a creative job, which is nice.<br>'
        'It’s quite well-paid, which is good.<br>I have to work 14 hours a day, which is really tiring.<br>I didn’t get the '
        'promotion, which was a bit disappointing.<br>My old office overlooked a park, which was nice.</p></div>')
    voc = SEC("Vocabulary", "Workplaces and activities", X.workplaces("b37-va") +
              EX("b37-vb", "B", "Work in pairs. Use the words and phrases in exercise A to have conversations like this:",
                 DLG(("A", "What do you do?"), ("B", "I work for a …… company."), ("A", "Oh yeah? Doing what?"),
                     ("B", "I’m in sales. I’m the rep for the whole of the south."))))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>Rep</i></b></p>'
              '<p><i>Rep</i> is short for <i>representative</i>. You can be <i>a sales rep, a holiday rep, a class rep</i>, etc. '
              'We also use <i>admin</i> instead of <i>administration</i> and <i>HR</i> instead of <i>human resources</i>.</p></div>')
    dbox = ('<div class="box"><p><b>In conversations we often give our opinion of what we think of the other speaker’s job or '
            'situation using <i>That must be</i> + adjective.</b></p><hr>' +
            DLG(("A", "Sometimes I do something like fifty or sixty hours a week."), ("B", "Really? <i>That must be</i> stressful.")) +
            "</div>")
    dkey = REVEAL("<p>" + "<br>".join(rows(7, 1, 48, 52, split=59)) + "</p>", "Ответ (ключ)")
    dc = SEC("Developing conversations", "<i>That must be …</i>", dbox +
             EX("b37-da", "A", "Respond to these sentences with <i>That must be …</i>", OL([
                 "I’m the sales manager for Europe. I’m in charge of thirty reps.", "I travel a lot round Europe and the Middle East.",
                 "I care for people who are dying.", "Basically, I just sit in front of a TV screen all day.",
                 "I often can’t explain myself clearly in English.", "I really see the kids develop and improve."])) +
             EX("b37-db", "B", '<span class="audio-ic">♪</span> 5.2 Listen to six conversations. Which three short answers do '
                "the speakers use to respond to <i>That must be …?</i>", dkey) + S52() +
             EX("b37-dc", "C", "Practise reading the conversations in exercise B.", ""))
    cp = SEC("Conversation practice", "",
             EX("b37-ca", "A", "Choose a job from these pages or a different job. Work in pairs. Describe the job in as much "
                "detail as you can, using language from these pages. Your partner must guess the job.",
                IMG(IMG_DIR + "p37-warehouse.jpg", "", cls="md")))
    return PAGE_BOX(37, '<div class="cols"><div>' + IMG(IMG_DIR + "p37-business.jpg", "", cls="md") + spk + voc +
                    '</div><div>' + native + dc + cp + "</div></div>")


def p38():
    gbox = ('<div class="box"><p><b>We use <i>have to</i> to talk about rules. We also use <i>have to</i> for things that we feel '
            'are essential to do.</b></p><hr><p><b>We use <i>don’t have to</i> for something which is not necessary. We also use '
            '<i>don’t have to</i> when there is no rule (the person can choose to do something or not).</b></p><hr>'
            '<p><b>We use <i>can</i> to show something is possible.</b></p><hr><p class="ex-line"><i>I have to work</i> really '
            'long hours sometimes.<br>I’m glad <i>I don’t have to work</i> tonight!<br><i>I can walk</i> to work. The office is '
            'really close to my flat.</p></div>')
    gr = SEC("Grammar", "<i>Have to, don’t have to, can</i>", gbox + X.have_to("b38-ga") +
             EX("b38-gb", "B", "Tick the sentences in exercise A that are true for the place you study / work in. Then make three "
                "more true sentences. Work in pairs to discuss your ideas.", "") +
             X.pic_jobs("b38-gc", "C", "Work in pairs. Discuss which jobs you can see in the pictures. Do you think they are good "
                        "jobs or bad jobs? Why? Make sentences about the jobs using <i>have to, don’t have to</i> and <i>can</i>.") +
             HELP(144))
    return PAGE_BOX(38, gr)


def p39():
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear three conversations about rules at work.</p>' +
              EX("b39-la", "A", "Before you listen, work in pairs. Discuss these questions:", UL([
                  "Why do you think companies have the rules below?", "Do you think they are sensible and fair?"])) +
              X.rules_conv("b39-lb") + X.collocations("b39-lc") + S53() +
              EX("b39-ld", "D", "Do you think the rules are fair in exercise B? Why? / Why not?", ""))
    gbox = ('<div class="box"><p><b>We sometimes use <i>be allowed to</i> instead of <i>can</i> to talk about permission. We use '
            '<i>be supposed to</i> and <i>should really</i> instead of <i>have to</i>, especially when the rules are often '
            'broken.</b></p><hr><p class="ex-line">They have a strict dress code – woman <i>aren’t</i> even <i>allowed to wear</i> '
            'smart trousers.<br><i>You’re not supposed to</i> use the company computers.<br><i>You should really arrange</i> time '
            'off with me a month in advance.</p></div>')
    bkey = REVEAL(UL(bullets(rows(8, 0, 40, 49))), "Возможные ответы (ключ)")
    gr = SEC("Grammar", "Talking about rules", gbox + X.rules_choose("b39-ga") +
             EX("b39-gb", "B", "What rules are being broken in the pictures?", IMG(IMG_DIR + "p39-cartoons.jpg", "") + bkey) +
             EX("b39-gc", "C", "Work in pairs. Discuss these questions. Use <i>should / shouldn’t really</i> and <i>(not) supposed "
                "to</i> where appropriate.", UL([
                    "Are there any rules where you work / study which you do not like? Do you follow them?",
                    "Are there any laws in your country that people often break? How do you feel about that?",
                    "Are there any other rules or laws you would like to see introduced at work / school / in your country?"])) +
             HELP(144))
    return PAGE_BOX(39, '<div class="cols"><div>' + lis + '</div><div>' + gr + "</div></div>")


def p40():
    akey = REVEAL(OL([r[2:] for r in numbered(rows(8, 0, 55, 61))]), "Ответ (ключ)")
    dkey = REVEAL(UL(bullets(rows(8, 1, 8, 16))), "Возможные ответы (ключ)")
    read = SEC("Reading", "",
               EX("b40-ra", "A", "Read the opening of a magazine article and decide:", OL([
                   "why the author wrote the article.", "what the rest of the article will be about."]) + akey) +
               EX("b40-rb", "B", "Think of different jobs where the workers:", OL([q for q, _ in X.PROBLEMS])) +
               article() + X.art_jobs("b40-rc") +
               EX("b40-rd", "D", "Work in pairs. Discuss these questions about the jobs in the article:", UL([
                   "Did anybody like any aspects of their job? Why?", "What other reasons did the people give for doing the jobs?",
                   "Do you think they are good reasons?"]) + dkey))
    return PAGE_BOX(40, read)


def p41():
    read = (X.art_words("b41-re") +
            EX("b41-rf", "F", "Put the jobs in the article in order from the best to the worst (best = 1, worst = 4). Work in "
               "pairs. Compare your answers and explain your decisions. Are there any other jobs you would hate to do?", ""))
    vbox = ('<div class="box"><p><b>We use <i>be used to</i> when a habit or situation is normal for us because of our '
            'experience. This habit might be difficult for other people.</b></p><p class="ex-line">Some people find working with '
            'kids difficult, but <i>I’m used to it</i>. I have five brothers and sisters who are younger than me.</p><hr>'
            '<p><b>We use <i>get used to</i> when a habit or situation is changing from being difficult to being normal / easy. '
            'We use it with lots of tenses.</b></p><p class="ex-line">I never had to wear a suit and tie before I had this job. '
            'I’d still prefer something less formal, but <i>I’m slowly getting used to it</i>.</p></div>')
    akey = REVEAL("<p>" + " ".join(rows(8, 1, 24, 28)).replace(") ", ")<br>") + "</p>", "Ответ (ключ)")
    voc = SEC("Vocabulary", "<i>Be used to, get used to</i>", vbox +
              EX("b41-va", "A", "Look back at the article, <i>Terrible jobs not a thing of the past</i> on p. 40, and find one "
                 "example of <i>be used to</i> and one example of <i>get used to</i>.", akey) +
              X.used_to("b41-vb") +
              EX("b41-vc", "C", "Underline the six expressions using <i>be used to / get used to</i> in exercise B. Translate them "
                 "into your language. Does your language use a similar structure to <i>be used to / get used to</i>?", "") +
              EX("b41-vd", "D", "Now practise reading the conversations.", ""))
    spk = SEC("Speaking", "",
              '<p class="intro">Work in pairs. You both have new jobs in Britain or America and are discussing how you are finding '
              'your work and life.</p>' +
              EX("b41-sa", "A", "Decide what your jobs are and where you live. Decide the questions you will ask. For example:", UL([
                  "How are you finding your job?", "Do you get on with the other people at work?", "How are you finding living here?",
                  "What’s your flat / the area you live in like?", "What do you think of the weather / food?"])) +
              EX("b41-sb", "B", "Role-play a conversation. Use at least two <i>be / get used to</i> comments.", ""))
    return PAGE_BOX(41, '<div class="cols"><div>' + read + IMG(IMG_DIR + "p41-guard.jpg", "", cls="md") + voc +
                    '</div><div>' + spk + "</div></div>")


def build():
    return p36() + p37() + p38() + p39() + p40() + p41()
