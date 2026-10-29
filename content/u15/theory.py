"""Страница «Теория»: Grammar reference p. 154 и правила из уроков юнита 15.
Справочник с. 154 почти целиком из таблиц и списков, поэтому собран вручную, а не из OCR."""
from grammar import gr_page
from . import shared as X

SHIFT = [("Present simple", "Past simple"), ("Present continuous", "Past continuous"), ("Present perfect", "Past perfect"),
         ("Past simple", "Past perfect"), ("be going to", "was going to"), ("will", "would"), ("can", "could"),
         ("must / have to", "had to")]


def build():
    g154 = (
        '<h3>Reported speech</h3>'
        '<p class="rule">We report what people said using a verb + (<i>that</i>) clause. Some verbs with this pattern are:</p>' +
        X.wordbox(["admitted", "agreed", "said", "claimed", "told s.o.", "explained", "warned", "promised"]) +
        '<p class="rule">When reporting things that have finished or which we believe to be untrue now, use past tenses. Move '
        'one tense back.</p><table class="voc">' +
        "".join(f"<tr><td>{a}</td><td>→ {b}</td></tr>" for a, b in SHIFT) + "</table>"
        '<p class="egs"><i>“I’m going to Poland tomorrow.” → I saw him last week and he said he was going to Poland.<br>'
        '“We travelled twelve hours to be there.” → They told me they’d travelled twelve hours to be there!<br>'
        '“I can’t come now. I’m studying.” → He said he couldn’t come because he was studying.<br>'
        'A: I hate football. B: I thought you said you liked it.</i></p>'
        '<p class="rule">The following stay the same in reported speech.</p>'
        '<p class="egs"><i>The doctor told me I should rest.<br>He claimed he used to be very rich.<br>'
        'He agreed that he might be wrong.</i></p>'
        '<p class="rule">When what is being reported is still true, you can use present and future forms in the normal way '
        'because we are talking from the point of view of now.</p>'
        '<p class="egs"><i>She said she lives in Madrid now.<br>They said they can’t come tomorrow because they’re working.<br>'
        'He said he’s already seen the film and he doesn’t want to see it again.</i></p>'
        '<h3>Reporting verbs</h3>'
        '<p class="rule">Some reporting verbs can be followed by a <i>to</i>-infinitive or <i>-ing</i> form.</p>'
        '<p><b>+ <i>to</i>-infinitive</b></p>' +
        X.wordbox(["agree", "claim", "offer", "promise", "refuse", "threaten", "advise s.o.", "persuade s.o.", "told s.o.",
                   "warn s.o."]) +
        '<p><b>+ <i>-ing</i></b></p>' + X.wordbox(["admit", "apologise for", "deny", "insist on", "recommend", "suggest"]) +
        '<p class="rule">Verbs often have more than one pattern.</p>'
        '<p class="egs"><i>Our doctor recommended trying a different medication.<br>The doctor recommended that I use cream from '
        'now on.<br>My doctor recommended a specialist based in Kraków.</i></p>')
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 104–109</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Short questions with <i>any</i> <small>(p. 105)</small></h3>'
        '<div class="box"><p><b>We often shorten questions to <i>any</i> + plural / uncountable noun, especially when they follow '
        'other related questions.</b></p><p class="ex-line">Are you allergic to anything? = Any allergies?<br>Have you had any '
        'diarrhoea? = Any diarrhoea?</p></div>'
        '<h3>Reported speech <small>(p. 109)</small></h3>'
        '<div class="box"><p><b>When we tell people about things that happened to us, we often report things using <i>said / '
        'told me (that)</i> + clause.</b></p><p class="ex-line">He kept saying he’d be OK.<br>They told me they’d given James an '
        'X-ray and there was nothing broken.</p></div>'
        '<h3>Reporting verbs <small>(p. 109)</small></h3>'
        '<div class="box"><p><b>We also use other reporting verbs to summarise the content of what was said.</b></p>'
        '<p class="ex-line">The woman driving offered to take James. · She insisted on taking him. · We persuaded him to go. · '
        'She promised to call me. · The doctors told him not to cycle.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 106)</small></h4><p><b><i>a bug</i></b> — '
        'is often used to talk about a disease such as a virus.</p><p><i>I picked up a bug while I was away.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 105)</small></h4><p><i>I’ll get the nurse to give you some '
        'painkillers.<br>If it rains, I’ll get my dad to drive us there.<br>I got a friend to help me carry stuff because of my '
        'bad back.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 104, 107, 108</span><h2>Vocabulary</h2>'
             '<h3>Injuries and illness <small>(p. 104)</small></h3>' +
             X.wordbox(["coughing", "sneezing", "stomach ache", "sprained", "stiff", "swollen", "dizzy", "high blood pressure",
                        "rash", "itchy", "migraines", "bump", "flu", "cold", "allergy", "upset stomach", "broken", "arthritis",
                        "headache", "cut"]) +
             '<h3>Forming words <small>(p. 107)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in [
                 ("virus", "viral"), ("infectious", "infection"), ("cure", "incurable, curable"), ("medicine", "medical"),
                 ("fat", "fatty"), ("natural", "naturally"), ("addicted", "addictive"), ("irritable", "irritability")]) +
             "</table><h3>Explaining causes and results <small>(p. 107)</small></h3>"
             '<p class="ex-line">X causes Y · X makes Y worse · X leads to Y · Y is caused by X · X means (that) … · '
             'X is linked to Y · X makes you feel …</p>'
             '<h3>Accidents and problems <small>(p. 108)</small></h3>' +
             X.wordbox(["burn", "trip over", "fall off", "bite", "crash into", "food poisoning", "sunburn", "faint", "slip",
                        "sting"]) + "</article>")
    toc = ('<nav class="toc"><a href="#gr154">Reported speech · reporting verbs</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(154, "gr154", g154) + unit_boxes + vocab
