"""Страница «Тесты»: упражнения Grammar reference p. 151 (ключи — Grammar Reference, 12) и итоговый тест."""
from lib import G, C, EX, OL, DLG
from ocrtext import lines, fixed, _fix
from . import shared as X


def used1():
    """Ключ: 1 have 2 would 3 is / was 4 never / didn’t 5 go 6 went 7 used 8 did 9 to 10 would."""
    n = lambda i, a: f"<sup>{i}</sup>{G(a)}"
    d = DLG(("A", "Arnedo’s a lovely place, isn’t it? How do you know it?"),
            ("B", f"Well, my parents used to {n(1, 'have')} a little house near there. We {n(2, 'would')} go there every summer for a month."),
            ("A", "Really? Whereabouts?"), ("B", f"The house {n(3, 'is|was')} actually just outside the town."),
            ("A", "Lovely. Did you ever go walking round there?"),
            ("B", f"Not really. In fact, we {n(4, 'never|didn’t')} use to do that much. We’d {n(5, 'go')} swimming in the river or "
                  f"sit around and read. Sometimes we {n(6, 'went')} for a bike ride, but to be honest, none of us {n(7, 'used')} to "
                  "like walking."),
            ("A", f"What a shame. So {n(8, 'did')} your parents sell the house?"),
            ("B", f"Yeah. As we got older, we used {n(9, 'to')} complain about going. We {n(10, 'would')} keep asking not to go. In "
                  "the end, they got fed up and sold it, yes."))
    return EX("t12-u1", "1", "Complete the conversation with one word in each space.", d)


def wish1():
    """Ключ: 1 had 2 hadn’t 3 hadn’t 4 had 5 hadn’t 6 had 7 hadn’t 8 had."""
    c = lambda k: C(k, "had", "hadn’t")
    rows = [f"I often wish I {c('had')} travelled more when I had the chance, but it’s impossible with the children.",
            f"I wish I {c('hadn’t')} gone. It was such a waste of time.",
            f"All the flights are really expensive. I wish I {c('hadn’t')} left it till the last minute to book them.",
            f"I wish I {c('had')} brought up my children in the country. It’s healthier and they would’ve had more freedom.",
            f"I wish I {c('hadn’t')} ignored him. He was right.",
            f"Thanks. You’ve really put my mind at rest. I wish I {c('had')} spoken to you earlier.",
            f"I really shouted at her and I wish I {c('hadn’t')} now.",
            f"I never really pushed my children, but I sometimes wish I {c('had')}. They would’ve thanked me for it."]
    return EX("t12-w1", "2", "Choose the correct form.", OL(rows))


def wish2():
    """Ключ: 1 I hadn’t started smoking 2 I had asked her 3 you had told me 4 I hadn’t been so hard on my children
    5 I hadn’t lost touch with them 6 I’d moved when I had the chance."""
    W = lambda a: G(a, "wide")
    rows = [("I really regret starting smoking.", f"I really wish {W('I hadn’t started smoking|I had not started smoking')}."),
            ("I really regret not asking her.", f"I wish {W('I had asked her|I’d asked her')}."),
            ("It’s a shame you didn’t tell me.", f"I wish {W('you had told me|you’d told me')}."),
            ("I regret being so hard on my children.", f"I wish {W('I hadn’t been so hard on my children|I had not been so hard on my children')}."),
            ("It’s a shame I lost touch with them.", f"I really wish {W('I hadn’t lost touch with them|I had not lost touch with them')}."),
            ("It’s a shame I didn’t move when I had the chance.", f"I wish {W('I’d moved when I had the chance|I had moved when I had the chance')}.")]
    return EX("t12-w2", "3", "Rewrite the sentences so they have a similar meaning.", OL([f"{a}<br>{b}" for a, b in rows]))


def gloss(p, box):
    out = []
    for l in lines(p, box):
        t = fixed(p, _fix(l["t"])).strip().replace(" - ", " – ")
        if t.startswith("Glossary") or set(t) <= set(". "):
            continue
        head = t.split(":", 1)[0]
        if ":" in t and len(head) < 30 and head[:1].islower():
            out.append([head, t.split(":", 1)[1].strip()])
        elif out:
            out[-1][1] += " " + t
    return '<div class="glossary"><h4>Glossary</h4>' + "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in out) + "</div>"


def build():
    part = ('<article class="page" id="t151"><span class="page-no">Учебник, с. 151</span>'
            '<h2>Grammar reference: <i>used to, would</i>; regrets and wishes</h2>'
            '<p><a href="theory.html#gr151">Правило — в разделе «Теория»</a></p>' + used1() + wish1() + wish2() +
            gloss(151, (450, 935, 745, 1035)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 82–87</span><h2>Итоговый тест по модулю 12</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.character("t12-f1", "1") + X.thats_like("t12-f2", "2") +
             X.heard("t12-f3", "3", "Choose the words that Lewis and Jessica use in <i>Listening</i> 12.1.") +
             X.used_to_a("t12-f4", "4", "Complete the sentences from <i>Listening</i> 12.1.") + X.used_to_b("t12-f5", "5") +
             X.nicolas("t12-f6", "6", "Match the statements with the speakers 1–5 from <i>Listening</i> 12.3. There is one statement "
                       "you do not need to use.") +
             X.synonyms("t12-f7", "7") + X.regrets("t12-f8", "8") + X.text_defs("t12-f9", "9") +
             X.friendship("t12-f10", "10") + "</article>")
    toc = '<nav class="toc"><a href="#t151">Used to, would; wish</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part + final
