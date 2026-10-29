"""Упражнения модуля 2, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи pp. 14–19."""
from lib import G, S, C, EX, OL

AH = list("abcdefgh")


def bls_match(id, letter="A", instr="Match 1–8 with the reasons a–h for the feelings."):
    """p. 14, Grammar A. Ключ: 1 d 2 b 3 h 4 g 5 c 6 e 7 f 8 a."""
    qs = ["Are you OK? You look a bit stressed.", "Are you all right? You look exhausted.",
          "Is Julie OK? She sounded a bit disappointed.", "Is Mike all right? He seems a bit down.",
          "Are you OK? You look a bit ill.", "Are you all right? You seem totally confused.",
          "Have you seen Ann? She sounded so relaxed!", "Hi. You look like you’re in a good mood."]
    rs = ["Yeah, I’ve just found out I’ve got a new job. I’m really pleased.",
          "I am! My car broke down and I had to walk home.",
          "Yeah, I feel terrible. I think I’m going to throw up.",
          "I am. I’m really behind with work and I’ve got exams next week.",
          "Yeah, I don’t get this. What am I supposed to do?",
          "Yeah. I think the week in the spa really helped her.",
          "He’s just split up with Jo and he’s quite upset.",
          "Yeah. I think she expected to get a better mark as she’d studied so much."]
    key = "d b h g c e f a".split()
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH)}" for q, k in zip(qs, key)]) + OL(rs, "items alpha"))


ADJ_NOUNS = ["connections", "attempt", "star", "year", "identity", "skills", "help", "plan"]
ADJ_KEY = ["meaningful", "desperate", "international", "miserable", "true", "social", "professional", "original"]


def reading_adj(id, letter="D", instr="Which adjectives went with these nouns?"):
    """p. 16, Reading D."""
    return EX(id, letter, instr, OL([f"{G(a)} {n}" for n, a in zip(ADJ_NOUNS, ADJ_KEY)]))


COLL_BOX = ["inspiring", "exciting", "disappointing", "annoying", "confusing", "relaxing"]


def collocations(id, letter="A", instr="Match these <i>-ing</i> adjectives with the nouns."):
    """p. 17, Vocabulary A. Ключ: 1 relaxing 2 annoying 3 exciting 4 inspiring 5 confusing 6 disappointing."""
    rows = [("relaxing", "holiday / bath / atmosphere / place / time"),
            ("annoying", "habit / person / noise / problem / spam"),
            ("exciting", "city / new development / discovery / opportunity"),
            ("inspiring", "teacher / speech / story / book / film / video clip"),
            ("confusing", "instructions / message / grammar / explanation"),
            ("disappointing", "response / news / loss / result / game / sales")]
    box = '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in COLL_BOX) + "</div>"
    return EX(id, letter, instr, box + OL([f"{S(k, COLL_BOX)} {n}" for k, n in rows]))


ING_ED = [("I’m ", "confusing", "confused", "confused", ". What did he say?"),
          ("This is really ", "interesting", "interested", "interesting", ". I love Maths."),
          ("I got a ", "disappointing", "disappointed", "disappointing", " mark in my test."),
          ("I’m so ", "boring", "bored", "bored", "! I can’t stand algebra!"),
          ("I hate being in my Dad’s class. He’s so ", "embarrassing", "embarrassed", "embarrassing", "!"),
          ("Why do I have to sit next to him? He’s so ", "scary", "scared", "scary", "!")]


def ing_ed(id, letter="A", instr="Choose the correct word (in <i>italics</i>) in sentences 1–6 below."):
    """p. 17, Grammar A."""
    return EX(id, letter, instr, OL([f"{a}{C(k, x, y)}{b}" for a, x, y, k, b in ING_ED]))


PIC = ["girl with yellow T-shirt", "girl with black hair", "boy with green T-shirt", "girl with brown hair",
       "boy with glasses", "blond boy at back"]


def pictures(id, letter="B", instr="Now match 1–6 to the pictures.", img=""):
    """p. 17, Grammar B. Ключ описывает людей на картинке."""
    opts = sorted(PIC)
    return EX(id, letter, instr, img + OL([f"{a}<i>{k}</i>{b} → {S(p, opts)}" for (a, _, _, k, b), p in zip(ING_ED, PIC)]))


LISTEN_ADJ = [("annoyed", "Sarah"), ("exhausted", "Louise"), ("happy", "Sarah"), ("mysterious", "Sarah"),
              ("shocked", "Louise"), ("stressed", "Louise")]


def listen_adj(id, letter="B", instr='<span class="audio-ic">♪</span> 2.3 Listen. Do the adjectives in the box describe Sarah or Louise?'):
    """p. 18, Listening A/B. Ключ: Louise — stressed, exhausted, shocked; Sarah — mysterious, happy, annoyed."""
    return EX(id, letter, instr, OL([f"{a} → {C(w, 'Sarah', 'Louise')}" for a, w in LISTEN_ADJ]))


def pc_gaps(id, letter="A", instr="Write the missing words from <i>Listening</i> in the present continuous."):
    """p. 18, Grammar A. Ключ: 1 am working / are finishing 2 are you doing? Are you window shopping? 3 I’m (just) meeting
    4 I’m seeing 5 are you being 6 I’m not getting; I’m (just) doing 7 are you doing 8 we’re going."""
    rows = [
        "I " + G("am working") + " quite hard at the moment. We " + G("are finishing") + " at nine most days!",
        "So what " + G("are you doing") + " here? " + G("Are you window shopping") + "?",
        "Not really. I " + G("am just meeting|am meeting") + " a friend here. I’m a bit early.",
        "I " + G("am seeing") + " someone from work.",
        "Why " + G("are you being") + " so mysterious about it? It’s unlike you. You normally tell me everything.",
        "I " + G("am not getting") + " any more money or anything. I " + G("am just doing|am doing") + " something different.",
        "What " + G("are you doing") + " on Friday? Do you fancy meeting?",
        "I’m afraid I can’t. I play badminton on Fridays and this Friday " + G("we are going") + " for a meal afterwards.",
    ]
    return EX(id, letter, instr, OL(rows))


DQ = [("How / your course / go? you / still / enjoy / it?",
       "How is your course going? Are you still enjoying it?|How’s your course going? Are you still enjoying it?"),
      ("What / you / do / now? you / fancy / going for a coffee?",
       "What are you doing now? Do you fancy going for a coffee?"),
      ("What / your sister / do / these days? she / still / study?",
       "What is your sister doing these days? Is she still studying?|What’s your sister doing these days? Is she still studying?"),
      ("you / work / this weekend? you / want / go for a picnic?",
       "Are you working this weekend? Do you want to go for a picnic?"),
      ("I / need / a coat? it / still / raining outside?", "Do I need a coat? Is it still raining outside?"),
      ("What / you / do here? you / work / near here?",
       "What are you doing here? Do you work near here?|What are you doing here? Are you working near here?"),
      ("What / you / do? you / wait / to be served?", "What are you doing? Are you waiting to be served?"),
      ("What / be / the matter with her? Why / she / shout / me?",
       "What is the matter with her? Why is she shouting at me?|What’s the matter with her? Why is she shouting at me?")]


def double_q(id, letter="A", instr="Make double questions in the present continuous or present simple with the ideas in 1–8."):
    """p. 18, Grammar (Present continuous / present simple questions) A."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in DQ]))


def double_match(id, letter="B", instr="Match the answers a–h with the questions 1–8 in exercise A."):
    """p. 18, B. Ключ: 1g 2e 3f 4a 5b 6h 7d 8c."""
    ans = ["I’m afraid so. I could meet you later today though, if you like.",
           "Yeah, it’s pouring down. I’ve got an umbrella, if you need one.",
           "I don’t know. She’s been in a bad mood all day. Just ignore her.",
           "Yeah, the assistant is just sorting out this lady’s problem.",
           "Sorry, I’m in a rush. My friend’s waiting for me.",
           "Yeah, she graduated last year, but now she’s doing a Masters.",
           "Yeah, although I’m finding it a lot harder than before.",
           "No, I’m just visiting a client. I’m just getting a sandwich before I go there."]
    key = "g e f a b h d c".split()
    qs = [a.split("|")[0] for _, a in DQ]
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH)}" for q, k in zip(qs, key)]) + OL(ans, "items alpha"))


ENDINGS = ["Kind regards", "Yours faithfully", "Many thanks", "Love", "All the best", "Yours sincerely", "Lots of love",
           "Cheers for now", "Yours"]
END_KEY = ["business", "business", "acquaintances", "close friends / family", "acquaintances", "business",
           "close friends / family", "close friends / family", "business"]


def endings(id, letter="A", instr="Look at these nine different ways of ending emails. Which endings could you use: "
            "in business emails, in emails to acquaintances, in emails to close friends / family members?"):
    """p. 123, Vocabulary A. Ключ (suggested answers): 1 Kind regards, Yours faithfully, Yours sincerely, Yours
    2 Many thanks, All the best 3 Love, Lots of love, Cheers for now."""
    opts = ["business", "acquaintances", "close friends / family"]
    return EX(id, letter, instr, OL([f"{e} → {S(k, opts)}" for e, k in zip(ENDINGS, END_KEY)]))


STARTERS = ["to let you know", "to remind", "to ask", "to tell", "to say I’m sorry", "to say thank you", "to say congratulations"]
PAIRS = [("to remind", "you that next Monday is a public holiday.", "you to bring that book you said you’d lend me."),
         ("to say I’m sorry", "I missed you while you were in Berlin.", "to hear you’ve been ill."),
         ("to say thank you", "for all your hard work organising the conference.", "for a lovely weekend."),
         ("to let you know", "I arrived safely in Hong Kong.", "I’ll be a bit late to the meeting tomorrow."),
         ("to ask", "if you could do me a big favour.", "if you could send me the photos you took at the party."),
         ("to tell", "you I can’t make the meeting tomorrow.", "you how much we enjoyed the barbecue last night."),
         ("to say congratulations", "on your exam results.", "to you both. The baby’s beautiful.")]


def starters(id, letter="A", instr="Complete each of the pairs of possible endings below with one sentence starter from the box."):
    """p. 122, Writing A. Ключ: a to remind b to say I’m sorry c to say thank you d to let you know e to ask f to tell
    g to say congratulations (начало — любое сочетание первых трёх колонок)."""
    rows = [f"… {S(k, STARTERS)} {a}<br>… {b}" for k, a, b in PAIRS]
    return EX(id, letter, instr, OL(rows, "items alpha"))
