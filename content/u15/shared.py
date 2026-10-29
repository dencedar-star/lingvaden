"""Упражнения модуля 15, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, EX, OL

AH = list("abcdefgh")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


PATIENT = ["My ankle’s quite swollen. I can hardly walk on it.", "I’ve done something to my back. It really hurts.",
           "I hit my head and got this nasty bump.", "I’ve had this nasty cough for weeks.",
           "I’ve got this nasty rash. It’s really itchy.", "It’s quite a nasty cut.", "You’ve broken your leg, I’m afraid.",
           "You’ve got very high blood pressure."]
DOCTOR = ["It’s a chest infection. It should clear up with antibiotics.",
          "Don’t scratch it. I’ll give you some cream for the itchiness.",
          "It’s probably just sprained, but we should have it X-rayed.", "Well, I have been under a lot of stress recently.",
          "Oh no! How long will I have to have it in plaster?", "Did you feel dizzy or lose consciousness at all?",
          "Will it need some stitches?", "I’ll get the nurse to give you some painkillers, but you’ll need to rest it. Don’t "
                                         "do any lifting."]


def comments(id, letter="D", instr="Match the patients’ and doctors’ comments."):
    """p. 105, Vocabulary D. Ключ: 1c 2h 3f 4a 5b 6g 7e 8d."""
    key = "c h f a b g e d".split()
    return EX(id, letter, instr, OL([f"{q} … {S(k, AH)}" for q, k in zip(PATIENT, key)]) + OL(DOCTOR, "items alpha"))


def any_q(id, letter="A", instr="Re-write the questions with <i>any</i>."):
    """p. 105, Developing conversations A. Ключ: 1 Any other symptoms? 2 (On) any medication? 3 Any itchiness?
    4 Any dizziness? 5 Any stiffness? 6 Any vomiting? 7 Any questions? 8 Any pain?"""
    rows = [("Do you have any other symptoms?", "Any other symptoms?"),
            ("Are you on any medication?", "Any medication?|On any medication?"), ("Does it feel itchy?", "Any itchiness?"),
            ("Have you felt dizzy at all?", "Any dizziness?"), ("Does it feel stiff?", "Any stiffness?"),
            ("Did you vomit at all?", "Any vomiting?"), ("Do you want to ask me anything?", "Any questions?"),
            ("Does it hurt at all?", "Any pain?")]
    return EX(id, letter, instr, OL([f"{q} → {G(a)}" for q, a in rows]))


MYTHS = ["You can catch a cold if you go out with wet hair.", "Antibiotics can cure a cold.", "Eating chocolate can cause acne.",
         "Cracking the joints in your fingers can cause arthritis.", "The less cholesterol you have, the better.",
         "Swallowing chewing gum is bad for you.", "Coffee is a drug."]


def myths(id, letter="B", instr="Now read the website. Decide if the statements are true or if they are myths, according to "
          "the writer."):
    """p. 106, Reading B. Ключ: 1–6 Myth, 7 True."""
    keys = ["Myth"] * 6 + ["True"]
    return EX(id, letter, instr, OL([f"{s} {C(k, 'True', 'Myth')}" for s, k in zip(MYTHS, keys)]))


FORMS = [("Apparently, the virus is quite <i>infected</i>, so I don’t want to visit him in case I catch it.", "infectious"),
         ("She’s got some kind of <i>medicine</i> condition which means she can only work part-time.", "medical"),
         ("Unfortunately, the condition is not <i>cure</i>, so he’ll have to live with it for the rest of his life.", "curable"),
         ("The drugs can be quite <i>addicted</i>, so you have to be careful how long you take them for.", "addictive"),
         ("You shouldn’t eat too many <i>fat</i> foods.", "fatty"),
         ("He’s been very <i>irritability</i> recently. I don’t know why.", "irritable"),
         ("The body produces vitamin D <i>natural</i> when exposed to sun.", "naturally"),
         ("He picked up this really nasty <i>viral</i> when he was on holiday.", "virus")]


def forms(id, letter="B", instr="Correct the words in the wrong form in sentences 1–8."):
    """p. 107, Forming words B. Ключ: 1 infectious 2 medical 3 curable 4 addictive 5 fatty 6 irritable 7 naturally 8 virus."""
    return EX(id, letter, instr, OL([f"{s} → {G(a)}" for s, a in FORMS]))


def causes(id, letter="B", instr="Complete the sentences with one word in each gap."):
    """p. 107, Explaining causes and results B. Ключ: 1 means 2 lead 3 linked 4 made 5 makes 6 caused."""
    rows = [f"He’s got a genetic condition which {G('means')} he has to see the doctor regularly.",
            f"A poor diet in childhood can {G('lead')} to health problems in later life.",
            f"Depression has been {G('linked')} to a lack of vitamin C in the diet.",
            f"The changes the government have introduced to the health service have {G('made')} things worse.",
            f"The main side effect of the medication is that it {G('makes')} you feel tired and sleepy.",
            f"The disease is {G('caused')} by a virus that attacks the brain."]
    return EX(id, letter, instr, OL(rows))


ACC = [("I was grilling some meat and I caught my hand on the grill and {} it quite badly.", "burned", "bruised"),
       ("I was jogging and I {} a rock and hurt my knee really badly.", "tripped over", "slipped"),
       ("I was out riding and the horse got scared by a bang and I {} the horse and broke my collar bone.", "fell off",
        "fell down"),
       ("I was walking down the street and this dog suddenly attacked me and {} me on the leg.", "bit", "stung"),
       ("I was cycling and a bus drove across me. I {} the side and sprained my wrist.", "crashed into", "fell into"),
       ("I had some food at a street market and I think I got food {} from there. It was awful.", "poisoning", "infection"),
       ("I spent the whole day on the beach and ended up with terrible {}.", "sunburn", "suntan"),
       ("It was really hot on the underground and I felt dizzy and then just {}.", "fainted", "disappeared"),
       ("I broke my arm when I {} on some ice.", "slipped", "tripped"),
       ("This bee {} me on the arm and my whole arm swelled up.", "stung", "bit")]
# порядок вариантов — как в учебнике
ACC_ORDER = [("burned", "bruised"), ("tripped over", "slipped"), ("fell off", "fell down"), ("bit", "stung"),
             ("crashed into", "fell into"), ("infection", "poisoning"), ("suntan", "sunburn"), ("fainted", "disappeared"),
             ("tripped", "slipped"), ("stung", "bit")]


def accidents(id, letter="A", instr="Choose the correct words."):
    """p. 108, Vocabulary A. Ключ: 1 burned 2 tripped over 3 fell off 4 bit 5 crashed into 6 poisoning 7 sunburn 8 fainted
    9 slipped 10 stung."""
    return EX(id, letter, instr, OL([t.format(C(a, *o)) for (t, a, _), o in zip(ACC, ACC_ORDER)]))


EVENTS = [("He had quite a few cuts and bruises.", "3"), ("It spoilt his holiday, really.", "7"),
          ("James went off the road into some bushes and fell off.", "2"), ("He had to have a few stitches in the cuts.", "6"),
          ("She took him to hospital, which was really kind of her.", "5"),
          ("We were going back to the hotel down a steep road.", "1"), ("He’s now found out his bike frame’s broken.", "8"),
          ("A woman came past in her car a minute or two later.", "4")]


def events(id, letter="B", instr="Put the events from the conversation in order."):
    """p. 109, Listening B. Ключ: f, c, a, h, e, d, b, g."""
    nums = [str(i) for i in range(1, 9)]
    return EX(id, letter, instr, OL([f"{t} → {S(k, nums)}" for t, k in EVENTS], "items alpha"))


def past_forms(id, letter="B", instr="Complete the sentences with the correct past forms."):
    """p. 109, Grammar B. Ключ: 1 had, gave 2 ate, needed 3 would have, was 4 would not hurt, was
    5 had done (would do / was doing), could 6 had done, had caused."""
    rows = [f"The doctor told me I {G('had')} a chest infection and {G('gave')} me some antibiotics. It cleared up after a "
            "week. (have, give)",
            f"The doctor said he {G('ate')} too much and he {G('needed')} to go on a diet, but he refused. (eat, need)",
            f"The doctors said she {G('would have')} some problems in the future, but she {G('was')} incredibly lucky to "
            "survive the crash. (have, be)",
            f"The doctor told me the injection {G('wouldn’t hurt|would not hurt')}, but it {G('was')} really painful! "
            "(not hurt, be)",
            f"They said the surgeon {G('had done|would do|was doing')} everything she {G('could')} to keep him alive. (do, can)",
            f"She told me they {G('had done')} several tests already, but they still didn’t know what {G('had caused')} the "
            "problem, so they had to do more. (do, cause)"]
    return EX(id, letter, instr, OL(rows))
