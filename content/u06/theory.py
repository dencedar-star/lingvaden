"""Страница «Теория»: Grammar reference p. 145 (из OCR) и правила из уроков юнита 06."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX[145] = [("I’s an amazing", "It’s an amazing"), (" - ", " – "), (" -ing", " –ing")]


def build():
    g145 = grammar_ref(145, (80, 105, 378, 930), heads=("must",))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 42–47</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3><i>must</i> <small>(p. 46)</small></h3><div class="box">' +
        "".join(f"<p>{i}) {r}</p>" for i, r in enumerate(X.MUST_RULES, 1)) +
        '<hr><p class="ex-line">' + "<br>".join(X.MUST_EX) + '</p></div>'
        '<div class="box"><p><b>If you use <i>must</i> and <i>mustn’t</i> to tell other people what to do, it often sounds rude '
        'and aggressive. It is better to use other structures in these situations.</b></p><p class="ex-line"><i>Don’t buy</i> it '
        'here. It’s too expensive. <i>Wait</i> till you get back home.<br>(<i>If I were you,) I’d take it back</i> to the shop '
        'and ask for a refund.<br>I’m sorry, but smoking’s <i>not allowed</i> in the store.</p></div>'
        '<h3>Avoiding repetition: <i>one / ones</i> <small>(p. 43)</small></h3>'
        '<div class="box"><p><b>We often use <i>one / ones</i> to avoid repeating words when we compare the difference between '
        'two things.</b></p><p class="ex-line">This phone has an MP3 player, whereas this one doesn’t.<br>These ones all use a '
        'lithium battery, whereas those use a nickel cadmium one, which isn’t as good.</p></div>'
        '<h3>Intonation <small>(p. 43)</small></h3><div class="box"><p><b>When negotiating prices, we express surprise about a '
        'price using high intonation. To make an alternative offer or to agree, we use lower intonation.</b></p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 47)</small></h4><p><b><i>You don’t want to'
        '</i></b> — When we want to tell friends what we think they should or should not do, we often use sentences beginning '
        'with <i>You want to</i> or <i>You don’t want to</i>.</p><p><i>You want to be careful if you go to the market.<br>You '
        'don’t want to get ripped off.<br>You don’t want to buy that! It doesn’t suit you.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 44)</small></h4><p><i>It’s not worth getting upset about.<br>It’s '
        'not worth arguing about. He won’t change his mind.<br>It’s not worth doing. Nobody is interested.<br>It’s not worth the '
        'trouble. It’s a long way to travel.<br>It’s not worth a hundred pounds. It’s really bad quality.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 42, 44</span><h2>Vocabulary</h2>'
             '<h3>Describing souvenirs and presents <small>(p. 42)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{g}</b></td><td>{', '.join(w for w, k in X.SOUV if k == i)}</td></tr>"
                     for i, g in enumerate(X.GROUPS)) +
             '</table><h3>Clothes and accessories <small>(p. 44)</small></h3><p class="ex-line">' +
             "<br>".join(g for g, _ in X.ODD) + '</p><p class="ex-line">doesn’t fit him / her properly · don’t suit him / her · '
             'don’t match / don’t go with</p></article>')
    writing = ('<article class="page" id="reports"><span class="page-no">Учебник, с. 130–131</span><h2>Writing: reports</h2>'
               '<div class="box"><p><b>We often refer to particular things in a report using <i>as far as X is / are concerned'
               '</i> or <i>in terms of X</i>.</b></p><p class="ex-line">As far as classes are concerned, the council could '
               'provide a wider range for all age groups.<br>In terms of the sports facilities, the council could provide more '
               'organised teams.</p></div><p>The passive is used in reports because it is more formal and impersonal: <i>this is '
               'rarely used, more could be done, so it could be used</i>.</p><p>Recommendations: <i>the council could provide … · '
               'more could be done … · why not show …? · the council should consider …</i></p></article>')
    toc = ('<nav class="toc"><a href="#gr145">must</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#reports">Reports</a></nav>')
    return toc + gr_page(145, "gr145", g145, "06 Going shopping") + unit_boxes + vocab + writing
