"""Страница «Теория»: Grammar reference p. 148 (из OCR) и правила из уроков юнита 09."""
from grammar import grammar_ref, gr_page
from . import shared as X

HEADS = ("COMPARING THE PAST WITH NOW", "Making comparisons using adjectives", "Making comparisons using nouns",
         "Uncountable nouns", "Countable nouns")


def build():
    g148 = (grammar_ref(148, (45, 110, 395, 1045), heads=HEADS, breaks=("Use (just) as + adjective to explain that two things",)) +
            '<h3>Time phrases</h3><p class="rule">Here are some expressions used to compare times:</p>'
            '<p class="egs"><i>than / as it used to be · than / as there was before · than / as it is nowadays · than / as it is '
            'now · that / as there are now · than / as when I was a kid</i></p>'
            '<h3>‘Double’ comparatives</h3><p class="rule">We often use ‘double’ comparatives to show a change is continuing. Note '
            'the tenses and time phrases we use.</p><h3>With nouns:</h3><p class="egs"><i>More and more people are moving out to '
            'the suburbs.</i></p><p class="egs"><i>Fewer and fewer people are voting in elections.</i></p><h3>With adjectives:</h3>'
            '<p class="egs"><i>Over recent years, the city has just got bigger and bigger.</i></p><p class="egs"><i>Buying a house '
            'is getting more and more expensive.</i></p>')
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 64–69</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Adding emphasis with auxiliaries <small>(p. 65)</small></h3>'
        '<div class="box"><p class="ex-line">Their flat <i>does</i> need a bit of work done on it, but they’ve actually bought it.'
        '</p><hr><p><b>We can add emphasis to sentences by either adding the auxiliaries <i>do, does</i> or <i>did</i> – or by '
        'stressing the auxiliary verb already there.</b></p></div>'
        '<h3>Making comparisons <small>(p. 65)</small></h3>'
        '<div class="box"><p><b>We often describe how large places are by making comparisons with places that the listener '
        'knows.</b></p><p class="ex-line">The lounge is <i>huge – it’s twice the size of</i> this room.<br>It’s got a <i>great</i> '
        'kitchen – <i>it’s a similar size to</i> yours, maybe a bit bigger.<br>Her garden’s <i>nice – it’s about the same size '
        'as</i> mine.</p></div>'
        '<h3>Describing changes <small>(p. 66)</small></h3>'
        '<div class="box"><p><b>We often talk about changes using verbs in the present perfect. We add adverbs to describe the '
        'degree of change.</b></p><p class="ex-line">House prices have risen dramatically over the past ten years.<br>'
        'Unemployment has fallen slightly since last year.</p></div>'
        '<h3>Asking about rules <small>(p. 69)</small></h3>'
        '<div class="box"><p class="ex-line">Would it be OK if I have friends to visit? — No, not at all – <b>as long as</b> '
        'you’re quiet if you’re back late.<br>Would it be possible to get web access in my room? — <b>I’m afraid not</b>, but '
        'there is an Internet café nearby.<br>Is it OK if I play music in my room? — Of course, <b>within reason</b>.</p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 65)</small></h4><p><i>The flat needs a lot of work (to be) done on '
        'it.<br>It needs a lot of money (to be) spent on it.<br>The oven needs a good clean. It’s really dirty.<br>The roof needs '
        'fixing. It leaks in heavy rain!</i></p></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 64, 68</span><h2>Vocabulary</h2>'
             '<h3>Describing where you live <small>(p. 64)</small></h3>' + X.wordbox(X.FEAT) + '<table class="voc">' +
             "".join(f"<tr><td><b>{w}</b></td><td>{d}</td></tr>" for w, d in X.MEAN) + "</table>"
             '<h3>Describing areas <small>(p. 68)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{k}</b></td><td>{q}</td></tr>" for q, k in X.AREA_S) + "</table></article>")
    toc = ('<nav class="toc"><a href="#gr148">Comparing the past with now</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(148, "gr148", g148) + unit_boxes + vocab
