"""Страница «Тесты»: упражнения Grammar reference p. 150 (ключи — Grammar Reference, 11) и итоговый тест."""
from lib import G, EX, OL
from ocrtext import lines, fixed, _fix
from ocrtext import FIX
from . import shared as X

FIX.setdefault(150, []).append(("kills your appetite.", "kills your appetite,"))

ING_BOX = ["chase", "circle", "crawl", "eat", "jump", "look for", "make", "stare"]
PASS_BOX = ["arrest", "give", "release", "see", "smuggle", "keep", "search", "create"]


def ing1():
    """Ключ: 1 chasing 2 staring 3 eating 4 jump 5 making 6 looking for 7 circling 8 crawl / crawling."""
    rows = [f"I was woken up by the cats {G('chasing')} a terrified mouse around.",
            f"This deer was just standing there in the middle of the road {G('staring')} at us.",
            f"It was horrible. This huge rat was sitting in the middle of the kitchen {G('eating')} a piece of cheese.",
            f"It was amazing. As we were sailing along, we saw a group of dolphins {G('jump|jumping')} out of the water.",
            f"I think there’s something wrong with the dog. It was up most of the night {G('making')} a terrible noise.",
            f"About an hour after we finally gave up looking for it, the dog just walked into the house {G('looking for')} for its dinner!",
            f"When I was walking up in the mountains, I saw this huge bird {G('circling')} overhead. It stayed for about ten minutes.",
            f"I saw a cockroach {G('crawl|crawling')} across the restaurant floor! It really killed my appetite."]
    return EX("t11-g1", "1", "Complete the sentences below with the correct form of the verbs in the box.",
              X.wordbox(ING_BOX) + OL(rows))


def pass1():
    """Ключ: 1 was searched 2 be smuggled 3 was arrested 4 was released 5 are being created 6 were being kept 7 be seen 8 was given."""
    rows = [f"When the house {G('was searched')}, police found over two hundred cats living in terrible conditions.",
            f"The eggs were taken from the eagle’s nest. Police believe they will now {G('be smuggled')} out of the country and sold abroad.",
            f"I just heard on the news that someone {G('was arrested|has been arrested')} and charged with the murder.",
            f"He {G('was released')} last Friday after a year in prison.",
            f"With the recent investment in the area, plenty of new jobs {G('are being created')} at the moment.",
            f"When the police raided the farm, they found that crocodiles {G('were being kept')} in a small lake.",
            f"He’s an amazing performer. His show really has to {G('be seen')} to be believed.",
            f"I don’t know why he was surprised they sacked him. He {G('was given|had been given')} several warnings about lateness."]
    return EX("t11-p1", "2", "Complete the sentences with the correct form of the verbs in the box.", X.wordbox(PASS_BOX) + OL(rows))


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
    part = ('<article class="page" id="t150"><span class="page-no">Учебник, с. 150</span>'
            '<h2>Grammar reference: <i>-ing</i> clauses and passives</h2>'
            '<p><a href="theory.html#gr150">Правило — в разделе «Теория»</a></p>' + ing1() + pass1() +
            gloss(150, (45, 760, 345, 1015)) + "</article>")
    final = ('<article class="page" id="final"><span class="page-no">Учебник, с. 76–81</span><h2>Итоговый тест по модулю 11</h2>'
             '<p class="lead">Задания юнита с автоматической проверкой. Можно проверять по одному или все сразу кнопкой внизу.</p>' +
             X.which_conv("t11-f1", "1", "In which conversation in <i>Listening</i> 11.1 did someone:") +
             X.story_qs("t11-f2", "2") + X.ing_clauses("t11-f3", "3") +
             X.articles("t11-f4", "4", "Match the articles with the headlines. Then complete the gaps with the words in the box.") +
             X.passive_gaps("t11-f5", "5", "Complete these sentences from the articles by putting the verbs into a passive form.") +
             X.participles("t11-f6", "6") + X.pets("t11-f7", "7") +
             X.pets_tf("t11-f8", "8", "Are these sentences about Suzie and Al’s conversation (<i>Listening</i> 11.3) true or false?") +
             X.nouns("t11-f9", "9") + X.pet_questions("t11-f10", "10") + "</article>")
    toc = '<nav class="toc"><a href="#t150"><i>-ing</i> clauses, passives</a><a href="#final">Итоговый тест</a></nav>'
    return toc + part + final
