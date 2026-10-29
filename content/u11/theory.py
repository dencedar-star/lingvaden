"""Страница «Теория»: Grammar reference p. 150 (из OCR) и правила из уроков юнита 11."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX.setdefault(150, []).extend([("- it is not", "– it is not"), ("- we do not", "– we do not"), ("- we want", "– we want")])


def build():
    g150 = (grammar_ref(150, (40, 110, 395, 312)) +
            grammar_ref(150, (400, 110, 760, 640), heads=("Passives",),
                        breaks=("We make passive sentences with be + past participle.", "Intransitive verbs (verbs that do not have an object)",
                                "A passive is used instead of an active because:", "Although you can say who or what did the action with",
                                "Look at how we make passive sentences in different",
                                "– we do not know who or what did the action", "– we want to emphasise who the action was done to.")))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 76–81</span><h2>Правила из уроков юнита</h2>'
        '<h3><i>-ing</i> clauses <small>(p. 77)</small></h3>'
        '<div class="box"><p><b>We can add clauses that begin with a verb in the <i>-ing</i> form to a sentence. It explains what '
        'someone / something is, or was, doing at a particular time.</b></p><p class="ex-line"><i>I suddenly noticed a group of '
        'crows looking quite excited.</i> (= I suddenly noticed a group of crows. They were looking quite excited.)<br>'
        '<i>I suddenly saw this huge snake lying across the road.</i> (= I suddenly saw this huge snake. It was lying across the '
        'road.)</p></div>'
        '<h3>Passives <small>(p. 79)</small></h3>'
        '<div class="box"><p><b>We use passives when it is not clear who does an action (or it is unimportant). Passives are '
        'formed using the correct form of the verb <i>to be</i> + the past participle.</b></p><p class="ex-line">Scientists '
        'have warned that up to 50% of all animal species <i>could be destroyed</i> by global warming if action <i>is not '
        'taken</i> soon.</p></div>'
        '<h3>Helping to tell stories <small>(p. 77)</small></h3>'
        '<div class="box"><p><b>Good listeners ask questions when people tell stories.</b></p><p class="ex-line">' +
        " · ".join(X.QBOX) + '</p><p class="ex-line"><i>It reminds me of something I once saw …<br>It actually reminds me of '
        'something that happened to me …</i></p></div>'
        '<h3>Stress and intonation for emphasis <small>(p. 81)</small></h3>'
        '<div class="box"><p><b>We often put an extra stress on adverbs like <i>so</i> to emphasise how we feel. The vowel sound '
        'is also lengthened.</b></p><p class="ex-line">Oh, they’re <u>so</u> cute! · It <u>really</u> stinks! · It’s just '
        '<u>incredibly</u> noisy!</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 80)</small></h4><p>We often describe '
        'ourselves in terms of things we like – or do not like – by saying we are <i>a dog / morning / film person</i>.</p>'
        '<p><i>I’m actually more of a cat person.<br>I’m a night person. I often don’t go to bed till three or later.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 78)</small></h4><p><i>Mongolia is known as ‘the land of the horse’.'
        '<br>Aubergines are also known as eggplants.<br>The area is known for its oysters.<br>Very few details are known about '
        'this rare species.</i></p></div></div></article>')
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 76–81, 159</span><h2>Vocabulary</h2>'
             '<h3>Animals <small>(File 10, p. 159)</small></h3>' +
             X.wordbox(["squirrel", "lizard", "bear", "eagle", "dolphin", "cockroach", "deer", "whale", "wolf", "crow",
                        "crocodile", "parrot", "snake", "scorpion", "rat"]) +
             '<h3>Animals and the environment <small>(p. 78)</small></h3>' + X.wordbox(X.WORDS) +
             '<h3>Keeping pets <small>(p. 80)</small></h3>' + X.wordbox(X.PETS_BOX) +
             '<h3>Forming words <small>(p. 81)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{w}</td><td><b>{n}</b></td></tr>" for w, n in [
                 ("free", "freedom"), ("destroy", "destruction"), ("extinct", "extinction"), ("warn", "warning"),
                 ("threaten", "threat"), ("investigate", "investigation"), ("independent", "independence")]) +
             "</table></article>")
    toc = ('<nav class="toc"><a href="#gr150"><i>-ing</i> clauses, passives</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(150, "gr150", g150) + unit_boxes + vocab
