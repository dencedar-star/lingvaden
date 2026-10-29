"""Страница «Учебник»: Unit 15 Injuries and illness, pp. 104–109. Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import paras, script, fixed, FIX
from keys import rows, numbered
from . import shared as X

IMG_DIR = "../assets/img/unit15/"

FIX[106] = [(" - ", " – "), ("which causes the", "which <b>causes</b> the"), ("can make the", "can <b>make</b> the"),
            ("about what leads to", "about what <b>leads</b> to"), ("are caused by cracking", "are <b>caused</b> by cracking")]
FIX[107] = [("which means it", "which <b>means</b> it"), ("also lead to", "also <b>lead</b> to"),
            ("which makes your", "which <b>makes</b> your"), ("been linked to", "been <b>linked</b> to")]
FIX[173] = FIX.get(173, []) + [("1 was just coming", "I was just coming"), ("D. No, none", "D: No, none"), ("No. no.", "No, no."),
                               ("steep road, James", "steep road. James"), ("drugs -", "drugs –")]
FIX[174] = FIX.get(174, []) + [("hed be OK", "he’d be OK"), ("Yeah, 1 know", "Yeah, I know"), (" - ", " – ")]


def br(lines):
    return "<br>".join(lines)


def website():
    def part(p, box):
        return " ".join(fixed(p, x) for x in paras(p, box, indent=12))
    items = [("1", "p106-girl.jpg", part(106, (335, 450, 526, 685))), ("2", "", part(106, (335, 770, 526, 955))),
             ("3", "p106-boy.jpg", part(106, (552, 305, 756, 470))), ("4", "", part(106, (552, 818, 756, 940))),
             ("5", "", part(107, (60, 322, 318, 535))), ("6", "", part(107, (60, 625, 318, 684))),
             ("7", "", " ".join(f"<p>{fixed(107, x)}</p>" for x in paras(107, (60, 770, 318, 955), indent=12)))]
    out = ""
    for n, img, t in items:
        body = t if t.startswith("<p>") else f"<p>{t}</p>"
        out += f'<div class="note"><h4>{n}</h4>' + (IMG(IMG_DIR + img, "", cls="md") if img else "") + body + "</div>"
    return ('<div class="article"><h3 class="art-title">Fact or myth?</h3><div class="cols">' + out + "</div>"
            '<p class="note-s">Remember this is for information only. If you have any worries about your health, you should '
            "always consult your doctor.</p></div>")


def S151():
    return SCRIPT("15.1", "", script(173, (30, 800, 400, 1060)) + script(173, (400, 75, 794, 775)), "173")


def S152():
    return SCRIPT("15.2", "A = Anna, D = Dan", script(173, (400, 785, 794, 1060)) + script(174, (30, 75, 394, 480)), "173–174")


def p104():
    spk = SEC("Speaking", "", EX("b104-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "How often do you go to the doctor’s?", "When was the last time you felt unwell? What symptoms did you have?",
        "Do you have a healthy lifestyle? Why? / Why not?"])))
    voc = SEC("Vocabulary", "Injuries and illness",
              EX("b104-va", "A", "Use the extra information in sentences 1–10 to guess the meanings of the words in <b>bold</b>. "
                 "Translate the sentences.", OL([
                     "He says he’s got the <i>flu</i>, but it’s really just a <i>cold</i>. He’s <b>coughing</b> a lot at night.",
                     "He’s developed an <i>allergy</i> to cats. He starts <b>sneezing</b> as soon as he comes near one.",
                     "It’s not really a <b>stomach ache</b> – it doesn’t really hurt. It’s just an <i>upset stomach</i> – I’ve "
                     "got diarrhoea and I feel sick.", "I think I’ve <b>sprained</b> my ankle. I don’t think it’s <i>broken</i>.",
                     "She’s got a <b>stiff</b> neck. She can hardly turn it.",
                     "My gran’s got <i>arthritis</i>. The joints in her hands and her wrists are really <b>swollen</b>. She "
                     "can’t hold things.",
                     "I sometimes feel really <b>dizzy</b> and have to sit down. The doctor says it might be because of "
                     "<b>high blood pressure</b>.",
                     "I’ve developed this nasty <b>rash</b> on the back of my hand. It’s all red and it’s really <b>itchy</b>.",
                     "I’ve been getting <b>migraines</b> – just very painful <i>headaches</i> – and I sometimes feel quite sick.",
                     "I hit my head and got a nasty <i>cut</i> and a big <b>bump</b> appeared."]) +
                 REVEAL(br(rows(23, 0, 29, 55, split=57)), "Значения (ключ)")) +
              EX("b104-vb", "B", "How many of the problems in <b>bold</b> and <i>italics</i> have you had in the last five years? "
                 "Are there any you have never had?", "") +
              EX("b104-vc", "C", "Why might you need the things in the pictures?",
                 '<div class="cols">' + "".join(IMG(IMG_DIR + f"p104-{n}.jpg", n, cls="md") for n in (
                     "bandage", "support", "painkillers")) + "</div>" +
                 '<div class="cols">' + "".join(IMG(IMG_DIR + f"p104-{n}.jpg", n, cls="md") for n in (
                     "thermometer", "cream", "medicine")) + "</div>" +
                 REVEAL(br(rows(23, 1, 1, 12, split=57)), "Ответ (ключ)")))
    return PAGE_BOX(104, IMG(IMG_DIR + "p104-banner.jpg", "15 Injuries and illness") + spk + voc)


def p105():
    voc = (X.comments("b105-vd") +
           EX("b105-ve", "E", "Spend two minutes memorising a–h in exercise D. Work in pairs.",
              "<p><b>Student A:</b> say 1–8.<br><b>Student B:</b> close your book and say as much as you can from a–h.</p>"))
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">I’ll get the nurse to give you some '
                'painkillers.<br>If it rains, I’ll get my dad to drive us there.<br>As I was off sick for a week, I got the '
                'doctor to write a note.<br>I got a friend to help me carry stuff because of my bad back.</p></div>')
    qs = ('<div class="cols"><div class="note"><h4>Conversation 1</h4><p>Does this hurt?<br>Can you put any weight on it at all?'
          '<br>How did you do it?<br>How long will I have to wait for the X-ray?<br>Are you on any medication?<br>Any allergies?'
          '<br>You’ve never had any adverse reactions to any drugs?</p></div><div class="note"><h4>Conversation 2</h4>'
          '<p>What seems to be the problem?<br>How long have you been like this?<br>Any diarrhoea?<br>And has he been able to '
          'drink anything?<br>Does this hurt at all?<br>And here?</p></div></div>')
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two conversations between a doctor and a patient.</p>' +
              EX("b105-la", "A", '<span class="audio-ic">♪</span> 15.1 Look at the questions that are asked and discuss what '
                 "you think is wrong with the patients. Then listen and check if you were right.",
                 qs + REVEAL(br(rows(23, 1, 17, 20, split=57)), "Ответ (ключ)")) +
              EX("b105-lb", "B", "Listen again. Note down the answers to the questions.",
                 REVEAL(br(rows(23, 1, 21, 36, split=57)), "Ответ (ключ)")) +
              EX("b105-lc", "C", "Work in pairs. Role-play the two conversations.", "") + S151())
    dbox = ('<div class="box"><p><b>We often shorten questions to <i>any</i> + plural / uncountable noun, especially when they '
            'follow other related questions.</b></p><hr><p class="ex-line">Are you allergic to anything? = Any allergies?<br>'
            'Have you had any diarrhoea? = Any diarrhoea?</p></div>')
    dc = SEC("Developing conversations", "Short questions with <i>any</i>", dbox + X.any_q("b105-da"))
    cp = SEC("Conversation practice", "",
             EX("b105-ca", "A", "You are going to have a similar conversation to the ones you heard in <i>Listening</i>. Work in "
                "pairs. Decide on a medical problem.", "<p><b>Student A:</b> plan what questions to ask the doctor – and think "
                                                       "of details of your problem.<br><b>Student B:</b> decide what advice to "
                                                       "give.</p>") +
             EX("b105-cb", "B", "Role-play the conversation. Try to use as much new language from these pages as possible.", ""))
    return PAGE_BOX(105, '<div class="cols"><div>' + IMG(IMG_DIR + "p105-cabinet.jpg", "") + voc + patterns +
                    '</div><div>' + lis + dc + cp + "</div></div>")


def p106():
    read = SEC("Reading", "Fact or myth?",
               '<p class="intro">You are going to read a medical website which discusses whether certain beliefs about health '
               'are true or are myths.</p>' +
               EX("b106-ra", "A", "Work in pairs. Look at the following statements. Discuss if you think they are true. Explain "
                  "your ideas.", OL(X.MYTHS)) +
               website() +
               X.myths("b106-rb", "B", "Now read the website. Decide if the statements in exercise A are true or if they are "
                       "myths, according to the writer. Why?") +
               REVEAL(br(rows(23, 1, 47, 55, split=57)), "Почему (ключ)") +
               EX("b106-rc", "C", "From the website, can you remember:", OL([
                   "what mothers often tell their children?", "the best way to avoid catching a cold?",
                   "when you may need antibiotics?", "the best way to deal with a cold?", "what makes acne worse?",
                   "what other factors can cause heart attacks?", "what people think happens when they eat chewing gum?",
                   "what can happen when people give up coffee?"]) +
                  "<p><b>Look again at the website. Did you remember the exact words?</b></p>" +
                  REVEAL(br(numbered(rows(24, 0, 1, 13, split=65))), "Ответ (ключ)")))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>a bug</i></b></p><p><i>A bug</i> is often used to talk '
              'about a disease such as a virus.</p><p><i>The best way to avoid viruses like these is to wash your hands regularly '
              'when there’s a bug going around.<br>I picked up a bug while I was away. I was in bed for two days.</i></p>' +
              DLG(("A", "<i>Are you feeling better?</i>"), ("B", "<i>Much better. I think it was just one of those "
                                                                  "twenty-four-hour bugs.</i>")) + "</div>")
    return PAGE_BOX(106, read + native)


def p107():
    fw = SEC("Vocabulary", "Forming words",
             EX("b107-fa", "A", "Find words in the text in the same family as the words in the box.",
                X.wordbox(["virus", "infectious", "cure", "medicine", "fat", "natural", "addicted", "irritable"]) +
                REVEAL(br(rows(24, 0, 15, 20, split=65)), "Ответ (ключ)")) + X.forms("b107-fb"))
    spk = SEC("Speaking", "", EX("b107-sa", "A", "Work in pairs. Discuss these questions:", UL([
        "Was there anything in the text that surprised you?", "Why do you think these myths have come about?",
        "Have you heard any stories about health issues? What do you think about them?"])))
    cr = SEC("Vocabulary", "Explaining causes and results",
             EX("b107-ca", "A", "Look at the verbs in bold in the text. They all connect causes or reasons with results. Which "
                "prepositions or verb patterns go with the words?",
                "<p><b>causes</b> · <b>make</b> · <b>leads</b> · <b>caused</b> · <b>means</b> · <b>lead</b> · <b>makes</b> · "
                "<b>linked</b></p>") +
             X.causes("b107-cb") +
             EX("b107-cc", "C", "Work in pairs. Use the patterns in exercise B to talk about the causes / results of these "
                "medical problems:", X.wordbox(["asthma", "malaria", "HIV", "migraines", "sneezing", "upset stomach",
                                                 "diabetes", "insomnia", "rashes", "stress"])) +
             EX("b107-cd", "D", "Do you know anyone who suffers from the problems in exercise C? How does it affect their life?",
                ""))
    return PAGE_BOX(107, '<div class="cols"><div>' + fw + spk + '</div><div>' + cr + "</div></div>")


def p108():
    voc = SEC("Vocabulary", "Accidents and problems", X.accidents("b108-va") +
              EX("b108-vb", "B", "Look at the pictures. Choose one and imagine you are the person in it. Decide how to describe "
                 "what happened to you. Add as many extra details as you want to. Then work in pairs. Tell your stories.",
                 IMG(IMG_DIR + "p108-accidents.jpg", "Accidents")))
    return PAGE_BOX(108, voc)


def p109():
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear a Swedish woman, Anna, talking to her colleague, Dan, about his holiday. '
              'In the conversation, Dan describes an accident that his friend James had.</p>' +
              EX("b109-la", "A", '<span class="audio-ic">♪</span> 15.2 Listen and answer the questions.', OL([
                  "What kind of holiday was it?", "How did the accident happen?", "Was James badly injured?",
                  "How did they get him to a hospital?", "What did the doctors tell him?"]) +
                 REVEAL(br(numbered(rows(24, 0, 40, 50, split=65))), "Ответ (ключ)")) +
              X.events("b109-lb", "B", "Work in pairs. Put the events from the conversation in order. Listen again to check "
                                       "your answers.") +
              EX("b109-lc", "C", "Work in pairs. Discuss these questions:", UL([
                  "When was the last time someone was very kind to you?",
                  "Did Dan’s story about James remind you of any other stories you have heard?"])) + S152())
    gbox = ('<div class="box"><p><b>When we tell people about things that happened to us, we often report things using '
            '<i>said / told me (that)</i> + clause.</b></p></div>')
    gr = SEC("Grammar", "Reported speech", gbox +
             EX("b109-ga", "A", "Look at the examples 1–4 from <i>Listening</i> and answer the questions.", UL([
                 "What structures are the forms in <i>italics</i>?", "Why are they used? What did the people actually say?"]) +
                OL(["He kept saying he<i>’d be</i> OK.",
                    "After a couple of hours, they rang and told me they<i>’d given</i> James an X-ray and there <i>was</i> "
                    "nothing broken.",
                    "They said he <i>needed</i> to stay there a bit longer, though, as he <i>was waiting</i> to have a few "
                    "stitches in the cuts.", "He said he’s <i>going to</i> have to buy a new bike now."]) +
                REVEAL(br(rows(24, 0, 54, 56, split=65) + rows(24, 1, 0, 8, split=65)), "Ответ (ключ)")) +
             HELP(154) + X.past_forms("b109-gb") +
             EX("b109-gc", "C", "Work in pairs. Take turns to ask each other <i>What did the doctor say?</i> Report something "
                "different each time.", ""))
    rbox = '<div class="box"><p><b>We also use other reporting verbs to summarise the content of what was said.</b></p></div>'
    rv = SEC("Grammar", "Reporting verbs", rbox +
             EX("b109-ra", "A", "Can you remember how the following reporting verbs were used in <i>Listening</i>? Underline the "
                "verb patterns in the audioscript on pp. 173–174.",
                X.wordbox(["offered", "insisted", "persuaded", "promised", "told him not"]) +
                REVEAL(br(rows(24, 1, 18, 29, split=65)), "Ответ (ключ)")) +
             EX("b109-rb", "B", "Work in pairs. Discuss these questions. When was the last time someone you know:", UL([
                 "offered to do something for you?", "promised to do something?", "insisted on doing something?",
                 "persuaded you (not) to do something?", "told you (not) to do something?"])) + HELP(154))
    spk = SEC("Speaking", "", EX("b109-sa", "A", "Work in pairs. Talk about a time when you had an accident – or were ill. "
                                 "Describe what happened. Use reported speech and some reporting verbs.", ""))
    return PAGE_BOX(109, '<div class="cols"><div>' + IMG(IMG_DIR + "p109-bike.jpg", "") + lis + gr +
                    '</div><div>' + rv + spk + "</div></div>")


def build():
    return p104() + p105() + p106() + p107() + p108() + p109()
