"""Страница «Теория»: Grammar reference p. 149 (из OCR) и правила из уроков юнита 10."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX.setdefault(149, []).extend([("I said i’d do it", "I said I’d do it"), ("is used to tall", "is used to talk"),
                                ("hed be there", "he’d be there"), ("tired", "tired."), ("but | actually", "but I actually"),
                                (" - ", " – ")])
HEADS149 = ("Plans / arrangements", "Reporting promises", "Reporting predictions",
            "Other verbs and structures to report the future in the past")


def build():
    intro = ('<p class="rule">There are several ways of referring to future plans, promises or predictions that we made in the '
             'past.</p><table class="voc"><tr><th>future</th><th>future in the past</th></tr>'
             '<tr><td><i>I’m going to go out later.</i></td><td><i>I was going to go out.</i></td></tr>'
             '<tr><td><i>I’ll do it later, OK.</i></td><td><i>He said he’d do it.</i></td></tr>'
             '<tr><td><i>I’ll probably see you there.</i></td><td><i>He said he’d probably see us there.</i></td></tr>'
             '<tr><td><i>I might come later.</i></td><td><i>She said she might come.</i></td></tr></table>')
    verbs = ('<p class="rule">The following verbs are often used with <i>to</i>- infinitive to talk about the future in the past:</p>'
             '<p class="ex-line">want · plan · intend · promise · expect · hope · mean</p>')
    g149 = (intro + grammar_ref(149, (85, 255, 398, 770), heads=HEADS149 + ("Other verbs and structures to report the future in the past",),
                                breaks=("Use was supposed to / was meant to to talk about",)) +
            verbs + grammar_ref(149, (85, 848, 398, 1020)))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 70–75</span><h2>Правила из уроков юнита</h2>'
        '<h3>The future in the past <small>(p. 75)</small></h3>'
        '<div class="box"><p><b>There are several ways of referring to future plans, promises or predictions that we made in the '
        'past. Usually, <i>am going to</i> becomes <i>was going to</i> and <i>will</i> becomes <i>would</i>.</b></p><hr>'
        '<p class="ex-line"><i>I was going to stay in, but a friend called me and so I ended up going out to see a play.<br>'
        'The film was much better than I thought it would be.</i></p></div>'
        '<h3>Why you do not want to do things <small>(p. 72)</small></h3>'
        '<div class="box"><p><b>When we are trying to arrange what to do and we are given different options, we usually explain '
        'why we don’t like certain ideas.</b></p><p class="ex-line">' + "<br>".join(a for _, a in X.EXPR) + "</p></div>"
        '<h3>Describing what’s on <small>(p. 72)</small></h3>'
        '<div class="box"><p class="ex-line"><b>I haven’t seen</b> the new David Lynch movie, <b>but it’s supposed to be</b> '
        'quite weird.<br><b>I haven’t heard</b> the new Snow Patrol CD, <b>but it’s supposed to be</b> quite dull.</p></div>'
        '<h3>Intonation and lists <small>(p. 74)</small></h3>'
        '<div class="box"><p><b>As we say a list of words, the intonation goes up on each word until the last one, when it goes '
        'down. We often finish these lists by adding <i>everything</i>.</b></p><p class="ex-line">It was great. The special '
        'effects, the soundtrack, everything!</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 71)</small></h4><p>We use <b><i>right</i></b> '
        'before prepositional phrases to mean <i>exactly</i>.</p><p><i>It’s right in front of the main entrance.<br>It’s right '
        'behind you.<br>We got to the theatre right on time.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 74)</small></h4><p><i>It was one of the worst things I’ve seen in a '
        'long time.<br>It was one of the best things I’ve seen in ages.<br>It’s one of the worst clubs I’ve ever been to.<br>'
        'It’s the best book I’ve read in ages.</i></p></div></div></article>')
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 70–74</span><h2>Vocabulary</h2>'
             '<h3>Films, exhibitions and plays <small>(p. 70)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{' / '.join(g)}</td><td>odd one out: <b>{k}</b></td></tr>" for g, k in X.ODD) + "</table>"
             '<h3>Explaining where things are <small>(p. 71)</small></h3>' + X.wordbox(X.DIR_BOX1 + X.DIR_BOX2) +
             '<h3>Describing what’s on <small>(p. 72)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{w}</b></td><td>{k}</td></tr>" for w, k in X.ADJ) + "</table>"
             '<h3>Words from the text <small>(p. 73)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{w}</b></td><td>{d}</td></tr>" for w, d in X.BOLD) + "</table>"
             '<h3>Describing an event <small>(p. 74)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{a}</td><td>{X.EVENT_END[ord(k) - 97]}</td></tr>" for a, k in zip(X.EVENT, "b a e c d g h f".split())) +
             "</table></article>")
    toc = ('<nav class="toc"><a href="#gr149">The future in the past</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(149, "gr149", g149) + unit_boxes + vocab
