"""Страница «Письмо» модуля 08: своего урока письма у юнита нет, поэтому здесь Review 02, часть 2 — Check what you know,
pp. 62–63 (проверочная по юнитам 5–8). Ключи — 02 Review (keys, с. 13); аудиоскрипт R 2.2 — с. 167."""
from lib import G, S, C, EX, OL, SEC, PAGE_BOX, SCRIPT
from ocrtext import lines, fixed, _fix, FIX
from writing_map import note
from review import gr, total
from .shared import wordbox

FIX[167] = FIX.get(167, []) + [(" - ", " – "), ("chicken -", "chicken –"), ("1 love it", "I love it"),
                               ("as | have", "as I have"), ("but 1 quite", "but I quite"), ("and | sometimes", "and I sometimes"),
                               ("chocolate.I", "chocolate. I"), ("| hardly", "I hardly")]
JOBS = ["businessman", "chef", "teacher", "model", "factory worker", "student", "waiter"]


def SR22():
    """Аудиоскрипт R 2.2 (с. 167, правая колонка): заголовки «Speaker N» на отдельных строках."""
    items = []
    for l in lines(167, (400, 100, 794, 765)):
        t = fixed(167, _fix(l["t"])).strip()
        if "R2.2" in t or "R 2.2" in t or t.startswith("REVIEW") or t == "AUDIOSCRIPT":
            continue
        if t.startswith("Speaker "):
            items.append([t, ""])
        elif items:
            items[-1][1] = (items[-1][1] + " " + t).strip()
    return SCRIPT("R 2.2", "", [tuple(i) for i in items], "167")


def listening():
    keys = ["chef", "model", "teacher", "businessman", "factory worker"]
    a = EX("r62-la", "A", '<span class="audio-ic">♪</span> R 2.2 Listen. Which of the things in the box does each person do?',
           wordbox(JOBS) + OL([f"Speaker {i}: {S(k, sorted(JOBS))}" for i, k in enumerate(keys, 1)], "items plain"))
    b = EX("r62-lb", "B", "Listen again and decide which speaker:", OL([
        f"has changed jobs and is worried about getting fat. {S('4', list('12345'))}",
        f"has an injury from work and stopped eating something. {S('5', list('12345'))}",
        f"never goes on a diet and wants to change jobs. {S('2', list('12345'))}",
        f"compares his job to the past and keeps strong discipline. {S('3', list('12345'))}",
        f"enjoys the job, but complains about co-workers. {S('1', list('12345'))}"], "items alpha"))
    return SEC("Listening", "", '<p class="intro">You are going to hear five people talk about things connected with food and '
                                'restaurants.</p>' + a + b + SR22() + total(10))


def rules():
    rows = [("You must hand in your essay on Tuesday.",
             f"You {G('can’t hand in|cannot hand in|can not hand in')} your essay later than Tuesday.", "can"),
            ("You must tell me in advance if you want a day off.",
             f"You {G('are supposed to tell me|’re supposed to tell me')} sooner if you want a day off.", "supposed"),
            ("It’s not a problem if you use the Internet at any time.",
             f"You {G('are allowed to use|’re allowed to use')} the Internet whenever you like.", "allowed"),
            ("You mustn’t go there. It’s a rip-off.",
             f"{G('I wouldn’t go|I would not go|I’d not go')} there, if I were you. It’s a waste of money.", "would"),
            ("You can skip the queue if you have a ticket.",
             f"You {G('have to queue|have to wait in the queue|have to wait in a queue|have to wait in line')} if you "
             "don’t have a ticket.", "have"),
            ("You should go if you’re busy.", f"You {G('don’t have to|do not have to')} stay behind if you’re busy.", "have"),
            ("I need to ask for a doctor’s certificate.",
             f"{G('I mustn’t|I must not|mustn’t|must not')} forget to get a doctor’s certificate.", "must"),
            ("Is taking photos inside the gallery prohibited?",
             G("Am I allowed to take|Are we allowed to take|Are you allowed to take|Am I allowed|Are we allowed|"
               "Are you allowed") + " photos inside the gallery?", "allowed")]
    return SEC("Grammar", "Talking about rules",
               EX("r62-gr", "", "Complete the second sentence using the word in brackets, so it has a similar meaning to the "
                  "first one.", OL([f"{a}<br>{b} <small>({w})</small>" for a, b, w in rows])) + total(8) + gr(144))


def conditionals():
    rows = [("{} I get another job soon, I’m going to get into debt.", ["When", "Since", "Unless", "If"], 2),
            ("Honestly, I think I’d explode {} I ate another thing.", ["unless", "when", "after", "if"], 3),
            ("He {} his homework unless you stand over him and force him to do it.",
             ["didn’t do", "doesn’t do", "hasn’t done", "wouldn’t do"], 1),
            ("If he {} hard, he’d probably pass, but he’s just very lazy.", ["will work", "would work", "worked", "works"], 2),
            # в ключах 4d (works) — опечатка: при «he’d probably pass» нужен второй тип, c (worked)
            ("If she {} it, she can take it back to the shop.", ["will like", "won’t like", "wouldn’t like", "doesn’t like"], 3),
            ("We can get a sandwich before the film, if you {}.", ["ate", "won’t eat", "don’t eat", "haven’t eaten"], 3),
            ("If you have any problems, {} me a ring.", ["just give", "you’ll just give", "just you give", "you gave"], 0),
            ("If I could work anywhere, I {} a job with Google.", ["would get", "got", "can get", "will get"], 0)]
    return SEC("Conditionals", "",
               EX("r62-co", "", "Choose the correct words a–d to complete the sentences.",
                  OL([t.format(C(o[k], *o)) for t, o, k in rows]) +
                  '<p class="note-s">В ключах к п. 4 указан вариант d (works), но с <i>he’d probably pass</i> нужно условное '
                  'второго типа — <i>worked</i> (c).</p>') + total(8) +
               '<p class="help">▶ Find this difficult? Look back at grammar reference <a href="../unit07/theory.html#gr146">'
               'p. 146</a> and <a href="../unit08/theory.html#gr147">p. 147</a>.</p>')


def adverbs():
    rows = [("I work {} a rep for a small company.", ("as", "like"), "as"),
            ("I’m {} charge of the whole department.", ("in", "of"), "in"),
            ("He’s {} sick. Hopefully, he’ll back at work soon.", ("away", "off"), "off"),
            ("I’m sorry to ask you {} such short notice, but I need you to work this weekend.", ("to", "at"), "at"),
            ("People near the factory are exposed {} dangerous chemicals.", ("with", "to"), "to"),
            ("He’s stressed. He’s {} a lot of pressure at work.", ("under", "below"), "under"),
            ("There’s so much competition now, I don’t know if we can stay {} business for much longer.", ("in", "on"), "in"),
            ("He insisted {} paying for everything. He wouldn’t let me pay a penny!", ("of", "on"), "on"),
            ("We’re having some friends {} for dinner. Would you like to come as well?", ("at", "round"), "round"),
            ("They’ve got some books {} special offer – three for two.", ("of", "on"), "on")]
    return SEC("Adverbs and prepositions", "",
               EX("r62-ap", "", "Choose the correct preposition or adverb.", OL([t.format(C(a, *o)) for t, o, a in rows])) +
               total(10))


def collocation():
    rows = [("a", ["well-paid", "temporary", "scruffy", "stressful", "demanding"], "job", "scruffy"),
            ("", ["filling", "deserted", "sugary", "vegan", "chewy", "disgusting"], "food", "deserted"),
            ("a", ["hard", "post-graduate", "evening", "struggling", "online"], "course", "struggling"),
            ("", ["thick", "rewarding", "trendy", "smart", "plain", "colourful"], "clothes", "rewarding"),
            ("a", ["hand-painted", "mass-produced", "china", "plastic", "silk"], "plate", "silk"),
            ("", ["grated", "mashed", "boiled", "steamed", "sliced", "limited"], "carrot", "limited")]
    return SEC("Collocation", "",
               EX("r63-cl", "", "Decide which word does not collocate with the word in bold.",
                  OL([f"{art} {C(k, *o)} <b>{n}</b>".strip() for art, o, n, k in rows])) + total(6))


def conversations():
    d = [["A: What’s the difference between these phones?",
          f"B: Well, firstly, this one is pay-as-you-go, {G('but|whereas|while')} that {G('one|phone|type|model')} requires "
          "a contract."],
         ["A: What are <i>kakis</i>?",
          f"B: Oh they’re a {G('kind|type|sort')} of fruit. They’re a bit {G('like')} big tomatoes, but they are creamier and "
          "they’re sweeter."],
         ["A: I spend a lot of time travelling round Asia.", f"B: Really. That {G('must')} be really interesting.",
          f"A: Yeah, it {G('should|would|can')} be, but unfortunately I often only see the hotel!"],
         [f"A: How’s the course {G('going')}?", f"B: Great – but I’m very busy. I have to {G('hand')} in an essay at the end of "
                                               "the week."]]
    return SEC("Developing conversations", "",
               EX("r63-dc", "", "Complete the dialogues with one word in each gap.", OL(["<br>".join(x) for x in d])) +
               total(8))


def verb_noun():
    verbs = ["ask for / split", "cheat in / fail", "owe / save", "ask for / fill in", "drop / pick up", "skip / have",
             "leave / deserve", "get into / pay back", "set / break", "extend / miss"]
    nouns = ["breakfast", "a tip", "litter", "the rules", "the deadline", "the bill", "an exam", "an application form", "debt",
             "money"]
    key = ["the bill", "an exam", "money", "an application form", "litter", "breakfast", "a tip", "debt", "the rules",
           "the deadline"]
    return SEC("Verb – noun collocations", "",
               EX("r63-vn", "", "Match the pairs of verbs with a noun.", wordbox(nouns) +
                  OL([f"{v} … {S(k, nouns)}" for v, k in zip(verbs, key)])) + total(10) +
               '<p class="help">▶ Find this difficult? Remember the Vocabulary Builder has information on new collocations.</p>')


def forming():
    rows = [("The mobile phone business is incredibly {}.", "compete", "competitive"),
            ("It’s a very {} environment at work.", "support", "supportive"),
            ("When it comes to food, she’s not very {}.", "adventure", "adventurous"),
            ("The course was really useful – just very {}.", "practice", "practical"),
            ("She’s very {}. She always does her homework.", "study", "studious"),
            ("He’s very {} about history.", "know", "knowledgeable"),
            ("Some parents are {} and pay for private tutors.", "push", "pushy"),
            ("My tutor’s {} and tells us we’re doing well.", "encourage", "encouraging"),
            ("The menu for the school dinners isn’t very {}.", "variety", "varied"),
            ("It’s a {} investment: you can lose a lot of money.", "risk", "risky")]
    return SEC("Forming words", "",
               EX("r63-fw", "", "Complete 1–10 with the adjectives of the words in bold.",
                  OL([t.format(G(a)) + f" <b>{w}</b>" for t, w, a in rows])) + total(10))


def vocabulary():
    g = lambda n, hint, a: f"<sup>{n}</sup><i>{hint}…</i> {G(a)}"
    t1 = (f"An organisation which deals with people who are in debt has said the situation is getting worse. It says people "
          f"often {g(1, 'o', 'owe')} £20,000 on credit cards and regularly go into overdraft on their bank "
          f"{g(2, 'ac', 'account|accounts')}. It blames a mixture of consumerism and low salaries. It wants the government to "
          f"raise the minimum {g(3, 'w', 'wage')}, and suggests banks should {g(4, 'av', 'avoid')} giving loans to people who "
          f"can’t afford to pay them back. It says that those in debt should be sensible. They should do "
          f"{g(5, 'w', 'without')} the latest trendy clothes and should wait to buy things in the {g(6, 's', 'sales')} when "
          "things are cheaper.")
    t2 = (f"A school headmaster has called for schools to reduce the amount of {g(7, 'ho', 'homework')} children are given. "
          f"He says it does not affect students’ level of achievement and, as evidence of this, he {g(8, 'po', 'points')} to "
          f"the success of Finland where students {g(9, 't', 'tend')} to have a lighter {g(10, 'wo', 'workload')} outside "
          "school.")
    return SEC("Vocabulary", "",
               EX("r63-vo", "", "Complete the words in the two short articles. The first letters are given.",
                  "".join(f'<div class="story hand"><p>{t}</p></div>' for t in (t1, t2))) + total(10))


def build():
    return note(8) + _build()


def _build():
    p62 = PAGE_BOX(62, '<h2>Check what you know</h2><p class="lead">Проверочная работа по юнитам 5–8: в учебнике за неё '
                       'можно получить до 80 баллов.</p><div class="cols"><div>' + listening() + rules() +
                   '</div><div>' + conditionals() + adverbs() + "</div></div>")
    p63 = PAGE_BOX(63, '<div class="cols"><div>' + collocation() + conversations() + verb_noun() + '</div><div>' + forming() +
                   vocabulary() + "</div></div>")
    return p62 + p63
