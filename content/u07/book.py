"""Страница «Учебник»: Unit 07 School and studying, pp. 48–53. Длинные тексты — из OCR и ключей."""
from lib import EX, OL, UL, DLG, SEC, PAGE_BOX, IMG, REVEAL, SCRIPT, HELP
from ocrtext import text, fixed, FIX
from keys import rows, numbered
from .ocrx import script2, numbered_script, col_paras, bullets
from . import shared as X

IMG_DIR = "../assets/img/unit07/"

FIX.setdefault(50, []).extend([("Tongjon", "<i>Tongjon</i>"), ("The Goat and the Goatherd", "<i>The Goat and the Goatherd</i>"),
                               (" - ", " – ")])
FIX.setdefault(51, []).extend([("“T’ve", "“I’ve"), ("tomorrow:", "tomorrow."), ("I say;", "I say,"), ("Tongion", "Tongjon"),
                               ("Tongiou", "Tongjon"), ("cconom", "econom"), ("scems", "seems"), (" - ", " – ")])
FIX.setdefault(53, []).extend([("paper I must", "paper ‘I must"), ("get expelled", "get expelled.")])
FIX.setdefault(165, []).extend([("1am, yeah", "I am, yeah"), ("Wowl", "Wow!"), ("l’ve", "I’ve"), ("Psychology.", "Psychology,"),
                                ("‘ll just", "I’ll just"), ("If | try", "If I try"), ("explain something.", "explain something,"),
                                (" - ", " – ")])
FIX.setdefault(166, []).extend([("have to bel", "have to be!"), ("Oh nol", "Oh no!"), ("bit fed up", "bit fed up."),
                                ("test or !", "test or I"), ("affecting you’re", "affecting your"), (" - ", " – ")])

BOLD = ["go through", "thick", "pushy", "bright", "points to", "relevant", "recite", "parenthood", "core", "rigid"]


def article():
    ps = col_paras(51, [(15, 505, 262, 1050), (262, 505, 500, 1050), (495, 735, 794, 1050)])
    html = "".join(f"<p>{p}</p>" for p in ps)
    for w in BOLD:
        html = html.replace(f" {w} ", f" <b>{w}</b> ", 1) if w != "bright" else html.replace("very bright.", "very <b>bright</b>.", 1)
    html = html.replace("Affluenza", "<i>Affluenza</i>").replace("Tongjon", "<i>Tongjon</i>")
    return ('<div class="article">' + IMG(IMG_DIR + "p51-title.jpg", "Learning to be happy") +
            '<h3 class="art-title">Learning to be happy</h3><div class="colum">' + html + "</div>" +
            '<div class="cols">' + IMG(IMG_DIR + "p51-books.jpg", "") + IMG(IMG_DIR + "p51-boy.jpg", "") + "</div></div>")


def S71():
    return SCRIPT("7.1", "D = Daniel, P = Paulina", script2([(165, (397, 330, 794, 960))], "DP"), "165")


def S72():
    return SCRIPT("7.2", "", script2([(165, (397, 975, 794, 1060)), (166, (0, 70, 397, 880))], "ABCDEFGH"), "165–166")


def S73():
    return SCRIPT("7.3", "", numbered_script([(166, (0, 905, 397, 1050)), (166, (397, 75, 794, 120))]), "166")


def p48():
    spk = SEC("Speaking", "",
              EX("b48-sa", "A", "Work in pairs. Discuss these questions:", UL([
                  "What kind of courses do you think the people in the pictures are doing?",
                  "Have you ever done any courses like this?", "Would you like to?"])) +
              EX("b48-sb", "B", "Have you ever done any of the courses in the box or any similar courses? Work in pairs. Tell "
                 "your partner about:", UL(["where you did the course.", "why you did it.", "how long it lasted.",
                                            "what the tutors / other students were like.", "whether or not it was worth doing."]) +
                 X.wordbox(["a postgraduate course", "an evening course", "a training course", "a first-aid course",
                            "an online course", "an IT course"])))
    voc = SEC("Vocabulary", "Describing courses", X.courses("b48-va") +
              EX("b48-vb", "B", "Work in pairs. Use five of the collocations in exercise A to talk about the course you discussed "
                 "in <i>Speaking</i> exercise B, or another course you have done.", ""))
    return PAGE_BOX(48, IMG(IMG_DIR + "p48-banner.jpg", "07 School and studying") +
                    '<div class="cols"><div>' + spk + '</div><div>' + voc + "</div></div>" + IMG(IMG_DIR + "p48-photos.jpg", ""))


def p49():
    dc = SEC("Developing conversations", "How’s the course going?",
             '<p class="note-s">For example: <i>Really well. I’m really <u>progress</u> it. I can’t believe how much '
             '<u>enjoying</u> I’ve already made!</i> → Really well. I’m really enjoying it. I can’t believe how much progress '
             'I’ve already made!</p>' + X.dc_fix("b49-da") +
             EX("b49-db", "B", "Work in pairs. Take turns asking <i>How’s the course going?</i> Give different answers each "
                "time.", ""))
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(10, 0, 29, 38))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear two friends, Daniel and Paulina, talking about a course Paulina is '
              'doing.</p>' + X.listen71("b49-la") +
              EX("b49-lb", "B", "Listen again. Take notes on the answers to the questions.", bkey) + S71())
    patterns = ('<div class="box"><h4>Language patterns</h4><p><b>Write the sentences in your language. Translate them back into '
                'English. Compare your English to the original.</b></p><p class="ex-line">I’m glad (that) it’s going well.<br>'
                'I’m glad (that) you’re feeling better.<br>I’m glad (that) you like the present.<br>'
                'I’m glad (that) everything is OK.<br>I’m glad to hear the accident wasn’t that serious.<br>'
                'I’m glad to see they’ve finally fixed the lift!</p></div>')
    box = ('<div class="box"><p><b>When a clause starts with <i>after</i>, <i>once</i> or <i>when</i>, we can then use the present '
           'simple or present perfect although we’re referring to the future. Using the present perfect emphasises a finished '
           'action.</b></p><hr><p class="ex-line">What are you going to do once <i>the course has finished</i>?<br>'
           '<i>When I’m there</i>, I might look for a job.<br><i>After I get back</i> from Australia, I’ll just start looking '
           'for a proper job.</p></div>')
    rw = [("I’m going to leave school next month. Then I might go away for a few weeks.", "After …, I …"),
          ("The course finishes soon. Then I’ll have to start paying back all my debts.", "Once …, I’ll …"),
          ("You are going to move to Germany soon. Are you going to look for a job there?", "Are … when …?"),
          ("I’ll call you this weekend. I need to finish my essay first.", "I’ll … when …"),
          ("My workload should lighten in the future. Then I’m going to start going swimming regularly again.", "Once …, I’m …"),
          ("I’m in a lecture at the moment. It finishes at three. Then I’ll call you back.", "I’ll … after …")]
    gr = SEC("Grammar", "After, once and when", box +
             EX("b49-ga", "A", "Rewrite each of the pairs of sentences as one sentence.",
                OL([f'{q}<br><i>{f}</i><div class="writer" data-target="" data-id="u07-ga{i}"><textarea rows="1"></textarea></div>'
                    for i, (q, f) in enumerate(rw, 1)]) +
                '<p class="note-s">Ответов к этому заданию в ключах нет — сверьтесь с правилом и справочником на с. 146.</p>') +
             EX("b49-gb", "B", "Work in pairs. Think of possible endings for these questions about your English course / other "
                "studies / your holiday / work plans, etc. Take turns asking and answering your questions.",
                OL(["What are you going to do once …?", "Where are you going to stay when …?", "Where are you going to go after …?"])) +
             HELP(146))
    cp = SEC("Conversation practice", "",
             EX("b49-ca", "A", "Work in pairs. Role-play a similar conversation to the one in <i>Listening</i>, but choose a "
                "different course. Think about how to answer the six pairs of questions from exercise A in <i>Listening</i>. "
                "Start the conversation like this: <i>How’s the course going? Are you still enjoying it?</i>", ""))
    return PAGE_BOX(49, '<div class="cols"><div>' + IMG(IMG_DIR + "p49-graduates.jpg", "") + dc + lis +
                    '</div><div>' + patterns + gr + cp + "</div></div>")


def p50():
    korea = f'<div class="story">{IMG(IMG_DIR + "p50-girl.jpg", "", cls="sm")}<p>{fixed(50, text(50, (15, 760, 270, 1025)))}</p></div>'
    spk = SEC("Speaking", "",
              EX("b50-sa", "A", "Read the short text about a Korean school student. Then work in pairs. Discuss these "
                 "questions:", UL(["Do you have any subjects like <i>Tongjon</i> at your school?",
                                   "Would you like to do a course where you choose what you study?",
                                   "What do you think are the advantages and disadvantages of this kind of study?"]) + korea))
    akey = REVEAL(OL([r[2:] for r in numbered(rows(10, 0, 43, 56) + rows(10, 1, 0, 2, split=57))]), "Ответы (ключ)")
    read = SEC("Reading", "",
               EX("b50-ra", "A", "Read the article about alternative ideas about education. Answer the questions.", OL([
                   "What caused the writer to write the article?", "Why does the writer talk about her daughter?",
                   "Why does she mention the main industry in Patagonia?", "Why does she mention PSHE?",
                   "Why does she talk about <i>Tongjon</i>?", "Why does she quote the Russian poet Pushkin?"]) + akey) +
               article() +
               X.bold_words("b50-rb", "B", "Work in pairs. Discuss what you think the words in bold in the article mean. Then "
                            "match them with their meanings.") +
               EX("b50-rc", "C", "Work in pairs. Look at the article again and try to find:", UL([
                   "something which is the same for you.", "something which is similar in your country.",
                   "something which you found surprising.", "something which does not happen in your country.",
                   "something that made you smile.", "an opinion you agree with and one you disagree with."]) +
                  "<p><b>Compare your ideas and explain your choices.</b></p>"))
    native = ('<div class="note"><h4>Native speaker English</h4><p><b><i>in mind</i></b></p>'
              '<p>If you have something <i>in mind</i>, you are thinking of this thing.</p>'
              '<p><i>Such ideas are not really what Oliver James has in mind.<br>Have you got anywhere in mind for your holiday?<br>'
              'I’ve got three people in mind for the new job.<br>What have you got in mind?<br>'
              'I’ll keep you in mind if I hear of any opportunities for work.</i></p></div>')
    vbox = ('<div class="box"><p><b>One way to build your vocabulary is to learn word families: words which all have the same '
            'root, like <i>innovate</i>, <i>innovative</i> and <i>innovation</i>. These words are often next to each other in a '
            'dictionary, so they are easy to look up. Make sure you try to learn the collocations that go with these words as '
            'well.</b></p></div>')
    voc = SEC("Vocabulary", "Forming words", vbox + X.families("b50-va") +
              EX("b50-vb", "B", "Work in groups. Discuss these questions:", UL([
                  "Do you think state education is better than private education?",
                  "Have you ever done something that you saw as a failure?", "What has been your biggest achievement so far?",
                  "Has anyone been an inspiration to you? How?"])))
    return PAGE_BOX(50, '<div class="cols"><div>' + spk + '</div><div>' + read + native + voc + "</div></div>")


def p52():
    spk = SEC("Speaking", "", EX("b52-sa", "A", "Work in pairs. Discuss what might be good / bad about going to each of the "
                                  "schools in the pictures. Explain your decisions.", ""))
    vkey = REVEAL(OL([r.split(" ", 1)[1] if r[:1].isdigit() else r
                      for r in numbered([r.replace("1teacher", "1 teacher") for r in rows(10, 1, 27, 56, split=57)])]),
                  "Ключ с пояснениями")
    voc = SEC("Vocabulary", "Schools, teachers and students", X.sts("b52-va", "A", "Work in pairs. Read sentences 1–16 and "
                                                                    "decide whether each describes a school, a teacher or a "
                                                                    "student, and if it is a positive (+) or negative (−) "
                                                                    "description.") + vkey +
              EX("b52-vb", "B", "Work in pairs. Use some of the language from exercise A to talk about:", UL([
                  "what kind of student you are.", "the good and bad teachers you have had.", "the school you go / went to."])))
    bkey = REVEAL(OL([r[2:] for r in numbered(rows(11, 0, 6, 19))]), "Ответы (ключ)")
    lis = SEC("Listening", "",
              '<p class="intro">You are going to hear four conversations about different aspects of education.</p>' +
              X.conv72("b52-la") +
              EX("b52-lb", "B", "Work in pairs. Answer these questions. Then listen again to check your answers.", OL([
                  "Why is the teacher annoyed? What advice is she given?",
                  "Why is the overseas student unhappy? What is she going to do?",
                  "What rule does the lecturer explain? Are there any exceptions to the rule?", "Why is the parent happy?"]) + bkey) +
              X.verbs72("b52-lc", "C", "Try to remember which verbs went with these nouns in the four conversations. Then "
                        "compare your ideas with the audioscript.") +
              EX("b52-ld", "D", "Work in pairs. Discuss these questions:", UL([
                  "Do you agree that teachers should be strict?", "Have you ever made a stupid mistake in an exam / test? How?",
                  "Do you know anyone who has changed schools? Why?"])) + S72())
    return PAGE_BOX(52, IMG(IMG_DIR + "p52-schools.jpg", "") + '<div class="cols"><div>' + spk + voc +
                    '</div><div>' + lis + "</div></div>")


def p53():
    box = ('<div class="box"><p><b>We use present tenses in the <i>if</i> clause to talk either a) about real present situations or '
           'b) possible future situations. The other half of the sentence uses different verb forms, according to their normal '
           'meanings.</b></p><hr><p><b>In zero conditionals, we use the present simple to talk about real repeated actions in '
           'the present.</b></p><hr><p><b>In first conditionals, we use <i>will</i> to talk about definite decisions and '
           'consequences in the future. <i>Might</i> is used to talk about possible ones.</b></p><hr><p><b>In some conditional '
           'sentences, we use imperatives and <i>should</i> to give advice.</b></p></div>')
    fkey = REVEAL(OL([r[2:] for r in numbered(rows(11, 0, 32, 54))]), "Ответы и формы глаголов (ключ)")
    gr = SEC("Grammar", "Zero conditionals and first conditionals",
             EX("b53-ga", "A", "Work in pairs. Look at these sentences from <i>Listening</i>. Try to remember how each sentence "
                "finished.", OL([q for q, _ in X.COND])) +
             X.cond73("b53-gb", "B", '<span class="audio-ic">♪</span> 7.3 Listen and write down the second half of each sentence '
                      "in exercise A. Which verb forms are used in each part of the sentences?") + fkey + box + HELP(146) +
             X.first_cond("b53-gc") +
             EX("b53-gd", "D", "Write your own ideas to answer these questions.", OL([
                 DLG(("A", "What are you going to study at university?"), ("B", "It depends … . If …, …")),
                 DLG(("A", "How long are you going to stay in your job?"), ("B", "It depends … . If …, …")),
                 DLG(("A", "Do you want to go out later?"), ("B", "It depends … . If …, …"))]) +
                '<div class="writer" data-target="" data-id="u07-gd"><textarea rows="4"></textarea></div>') +
             EX("b53-ge", "E", "Work in pairs. Role-play the three conversations in exercise D using your ideas. Your partner "
                "should continue the conversations by saying <i>And what if …</i>", "") + S73())
    rules = '<div class="note"><h4>School rules</h4>' + UL(bullets(53, (50, 720, 745, 1045))) + "</div>"
    spk = SEC("Speaking", "",
              EX("b53-sa", "A", "Look at the school rules and their consequences. Work in pairs. Discuss these questions:",
                 UL(["Which rules do you think are fair?", "Are any the same as you have / had at school?"]) + rules) +
              EX("b53-sb", "B", "Invent five new rules for your own class.", ""))
    return PAGE_BOX(53, '<div class="cols"><div>' + gr + '</div><div>' + spk + "</div></div>")


def build():
    return p48() + p49() + p50() + p52() + p53()
