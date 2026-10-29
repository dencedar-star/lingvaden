"""Упражнения модуля 9, которые выводятся и в «Учебнике», и в «Тестах» (с разными id). Ответы — ключи."""
from lib import G, S, C, TF, EX, OL

AH = list("abcdefgh")


def wordbox(ws):
    return '<div class="wordbox">' + "".join(f"<span>{w}</span>" for w in ws) + "</div>"


FEAT = ["a courtyard", "a swimming pool", "gas central heating", "a back garden", "a loft", "a roof terrace", "a garage",
        "a patio", "an open fire", "a balcony", "a tiled floor", "a basement"]
NOT_SEEN = {"a courtyard"}


def features(id, letter="A", instr="Which of the words in the box can you see in the picture?"):
    """p. 64, Vocabulary A. Ключ: в картинке всё, кроме courtyard (про loft ключ молчит — не проверяем)."""
    items = [f"{w} {C('No' if w in NOT_SEEN else 'Yes', 'Yes', 'No')}" for w in FEAT if w != "a loft"]
    return EX(id, letter, instr, wordbox(FEAT) + OL(items) + '<p class="note-s">Про <i>a loft</i> в ключе ничего не сказано.</p>')


MEAN = [("cramped", "doesn’t have much space"), ("bright", "has a lot of light"),
        ("conveniently located", "within easy reach of shops, transport, etc."),
        ("a shared flat", "a flat where a number of friends (or housemates) live together"),
        ("run-down", "old and in a bad condition"), ("spacious", "having a lot of space (opposite of cramped)"),
        ("affordable", "easy to pay the rent / mortgage"), ("newly built", "of recent construction, modern"),
        ("central", "near or in the town centre"), ("compact", "small but well-designed, neat")]
MEAN_S = ["It’s only a one-bedroom flat, so now we have the baby and all the extra baby stuff, it’s quite <b>cramped</b>.",
          "We’ve got huge windows, so we get a lot of sunlight, which means it’s nice and <b>bright</b> in the summer.",
          "It’s very <b>conveniently located</b>. There’s a shop just round the corner and it’s five minutes from the nearest station.",
          "I’m renting a room in <b>a shared flat</b> with four other students. It’s nice, but it’s cold. The central heating needs fixing.",
          "I live on the fifth floor of an old block of flats. The whole place is quite <b>run-down</b>. It needs a lot of work done on it.",
          "It’s very <b>spacious</b>. It’s the biggest place I’ve ever lived in.",
          "It’s very <b>affordable</b>. My rent is quite low. I only pay fifty pounds a week.",
          "I live in a <b>newly built</b> block of flats. It’s great. It’s all very modern.",
          "It’s very <b>central</b>. I can walk into town in ten minutes.",
          "It’s not very big, but it’s big enough. It’s nice and <b>compact</b>."]


def meanings(id, letter="C", instr="Use the extra information in sentences 1–10 to guess the meanings of the words in <b>bold</b>."):
    """p. 64, Vocabulary C. Значения — ключ."""
    opts = sorted(d for _, d in MEAN)
    return EX(id, letter, instr, OL([f"{s}<br><b>{w}</b> = {S(d, opts)}" for s, (w, d) in zip(MEAN_S, MEAN)]))


ENDS = [("Did I tell you I went …", "round to see Nick and Carol the other day?"),
        ("I haven’t seen them …", "for ages."), ("They said to say …", "‘Hello’ to you.|Hello to you."),
        ("It’s quite a lot …", "bigger than their old place."), ("That must be …", "nice for them."),
        ("That’s the main reason …", "they moved out."), ("I must go …", "round and see them."),
        ("The only problem is, though, it’s not …", "as central as their old place.|as central as their old place was.")]


def endings(id, letter="B", instr="Look at the sentence beginnings from the conversation. Complete each sentence."):
    """p. 65, Listening B. Ключ: полные предложения из ключа."""
    return EX(id, letter, instr, OL([f"{q} {G(a, 'wide')}" for q, a in ENDS]))


def _v(*ss):
    out = []
    for s in ss:
        out += [s, s.replace(" –", ""), s.replace(" – ", ", ")]
    return "|".join(dict.fromkeys(out))


SIZE = [("His bedroom’s tiny. It’s about half-size of mine.", _v("His bedroom’s tiny. It’s about half the size of mine.")),
        ("The kitchen is enormous. It’s three times the size of my.",
         _v("The kitchen’s enormous. It’s three times the size of mine.", "The kitchen is enormous. It’s three times the size of mine.")),
        ("The bathroom’s OK. It’s about same size as yours – maybe a little bit bigger.",
         _v("The bathroom’s OK. It’s about the same size as yours – maybe a little bigger.",
            "The bathroom’s OK. It’s about the same size as yours – maybe a little bit bigger.")),
        ("They’ve got a huge garden. It’s twice the size of your.", _v("They’ve got a huge garden. It’s twice the size of yours.")),
        ("They’ve got a small basement. It’s a similar size of this room – maybe a little bit smaller.",
         _v("They’ve got a small basement. It’s a similar size to this room – maybe a little smaller.",
            "They’ve got a small basement. It’s a similar size to this room – maybe a little bit smaller.")),
        ("They’ve got a lovely front room. It’s twice as wide as this room and maybe a little bit more long.",
         _v("They’ve got a lovely front room. It’s twice as wide as this room and maybe a little longer.",
            "They’ve got a lovely front room. It’s twice as wide as this room and maybe a little bit longer."))]


def sizes(id, letter="A", instr="Correct the mistakes in these sentences. You may need to add extra words."):
    """p. 65, Developing conversations A. Ответы — ключ."""
    return EX(id, letter, instr, OL([f"{q}<br>{G(a, 'wide')}" for q, a in SIZE]))


TFS = [("Jim Wynand pays a lot of rent for his flat.", "F"), ("The development he’s living in is temporary.", "T"),
       ("House prices in London have more than doubled over the last decade.", "T"),
       ("In recent years, it has become cheaper for house buyers to borrow money from banks.", "T"),
       ("More people want to sell houses than buy them.", "F"),
       ("Some houses are built specifically for people in jobs which are important for society.", "T"),
       ("The number of people adding extra rooms to their houses has increased slightly over recent years.", "F"),
       ("It is becoming more normal for people to leave home later than they had perhaps planned to.", "T")]


def true_false(id, letter="C", instr="Decide if these sentences about the article are true or false."):
    """p. 66, Reading C. Ключ: 1 F 2 T 3 T 4 T 5 F 6 T 7 F 8 T."""
    return EX(id, letter, instr, OL([f"{q} {TF(k)}" for q, k in TFS]))


def article_e(id, letter="E", instr="Without looking at the article, complete the sentences."):
    """p. 66, Reading E. Ключ: 1 taking 2 rises 3 protect 4 investments 5 gets 6 increase 7 at 8 tackling."""
    rows = [f"More and more young people are now {G('taking')} advantage of the new housing developments.",
            f"Prices used to be so low it was inevitable that there would be dramatic price {G('rises')}.",
            f"By limiting new developments to inner city areas, the government aims to {G('protect')} the environment.",
            f"Lots of people buy second homes as {G('investments')}. They keep them for a few years then sell them at a profit.",
            f"It’s the main going out area, so it {G('gets')} very noisy in the evenings.",
            f"There has been a huge {G('increase')} in the number of people adding extra rooms to their properties.",
            f"More and more banks now offer mortgages {G('at')} very low interest rates.",
            f"They need to find some new ways of {G('tackling')} the problem."]
    return EX(id, letter, instr, OL(rows))


AREAS = ["convenient", "noisy", "rough", "lively", "dirty", "residential", "dead", "green", "isolated", "posh"]
AREA_S = [("There’s absolutely nothing to do round there in the evenings and it’s fairly quiet during the day too!", "dead"),
          ("We live on a main road and lots of lorries go past.", "noisy"),
          ("The nightlife’s good. There’s always something happening.", "lively"),
          ("It’s quite run-down and there’s quite a lot of crime and social problems.", "rough"),
          ("There are lots of parks and trees, which is nice.", "green"),
          ("It’s incredibly expensive round there. All you see are beautiful houses with perfect gardens. I could never afford to "
           "live there.", "posh"),
          ("It’s in the middle of nowhere. You need a car to get anywhere.", "isolated"),
          ("There’s a lot of litter – the streets are filthy and there’s graffiti everywhere.", "dirty"),
          ("There are plenty of shops and it’s well connected for transport.", "convenient"),
          ("There are lots of families living there, so it’s nice for the kids, but we could do with more shops nearby.",
           "residential")]


def areas(id, letter="A", instr="Match the words in the box with sentences 1–10."):
    """p. 68, Vocabulary A. Ключ: 1 dead 2 noisy 3 lively 4 rough 5 green 6 posh 7 isolated 8 dirty 9 convenient 10 residential."""
    return EX(id, letter, instr, wordbox(AREAS) + OL([f"{q} → {S(k, sorted(AREAS))}" for q, k in AREA_S]))


def compare(id, letter="A", instr="Complete the sentences from <i>Listening</i>. They compare things between the past and now."):
    """p. 68, Grammar A. Ключ: 1 better, it was 2 nowhere near as, there was 3 not as quiet, it used to be 4 fewer, there are
    5 became, bigger."""
    rows = [f"There are still bad things about it, but it’s {G('better')} than {G('it was')} before.",
            f"There’s {G('nowhere near as')} much crime as {G('there was')} five years ago.",
            f"It’s {G('not as')} quiet as {G('it used to be')}.",
            f"There were {G('fewer|far fewer')} flights than {G('there are')} now.",
            f"One of the budget airlines started using the airport and over the past few years it {G('became|’s become|has become')} "
            f"bigger and {G('bigger')}."]
    return EX(id, letter, instr, OL(rows))


RULES_Q = ["Would it be OK if I have friends to visit?", "Would you mind if I cooked for myself sometimes?",
           "Do I have to be home before a certain time?", "Can I use the washing machine whenever I like?",
           "Would it be possible to get web access in my room?", "Is it OK if I play music in my room?"]
RULES_A = ["No, not at all – <b>as long as</b> you’re quiet if you’re back late.",
           "<b>I’m afraid not</b>, but there is an Internet café nearby.", "Not at all – <b>as long as</b> you clean up after yourself.",
           "<b>It depends how</b> long for. It’s fine if it’s just a few days.",
           "Of course, <b>within reason</b>. Obviously, you shouldn’t play it too loud.",
           "<b>Within reason</b>. Obviously, I don’t want you washing clothes in the middle of the night."]


def rules(id, letter="A", instr="Match the student’s questions 1–6 with the host family’s replies a–f."):
    """p. 69, Developing conversations A. Ключ: 1 d 2 c 3 a 4 f 5 b 6 e."""
    return EX(id, letter, instr, OL([f"{q} → {S(k, AH[:6])}" for q, k in zip(RULES_Q, "dcafbe")]) + OL(RULES_A, "items alpha"))
