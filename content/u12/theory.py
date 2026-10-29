"""Страница «Теория»: Grammar reference p. 151 (из OCR) и правила из уроков юнита 12."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX.setdefault(151, []).extend([
    ("My sister would be /", "My sister <s>would be</s> /"), ("I would have / had", "I <s>would have</s> / had"),
    ("I-would meet met", "I <s>would meet</s> met"), ("but I only used", "but I only <s>used"), ("to go went twice", "to go</s> went twice"),
    ("I wish i’d been", "I wish I’d been"), ("(- I", "(= I"), ("and now i", "and now I"), ("pp. 136-137", "pp. 136–137")])


def build():
    g151 = (grammar_ref(151, (80, 110, 395, 665), heads=("Used to, would and the past simple",),
                        breaks=("Look at the different ways the negative of used to is", "It is very common to introduce memories with used",
                                "Do not use would to describe character or possessions", "Do not use would or used to for single events.")) +
            grammar_ref(151, (440, 110, 750, 380), heads=("Regrets and wishes",),
                        breaks=("Look at these other ways of expressing regret.",)))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 82–87</span><h2>Правила из уроков юнита</h2>'
        '<h3><i>Used to</i> and <i>would</i> <small>(p. 84)</small></h3>'
        '<div class="box"><p><b><i>Used to</i> or the past simple can be used to describe someone’s character in the past, '
        'especially when there has been a change since then. <i>Used to</i> and <i>would</i> and the past simple can all describe '
        'regular activities / habits in the past. We tend to start with <i>used to</i> and then use <i>would</i> or the past simple '
        'to give details.</b></p><p class="ex-line">We used to be quite close. We were both quite sporty – we would go to the beach '
        'a lot, we’d play tennis together and that kind of thing – but he’s not interested now.</p></div>'
        '<h3>Expressing regrets (<i>wish</i>) <small>(p. 85)</small></h3>'
        '<div class="box"><p class="ex-line">I sometimes wish <i>we’d stayed</i> together.<br>I wish we <i>hadn’t split up</i>.<br>'
        'We’d talk about the things we wished <i>we’d said</i> to him.</p><hr><p class="ex-line">' +
        "<br>".join(k.split("|")[0] for _, _, k in X.REGRET) + "</p></div>"
        '<h3><i>That’s like …</i> <small>(p. 83)</small></h3>'
        '<div class="box"><p><b>When we talk about the character of someone we know, we often compare the person to someone with a '
        'similar character. To introduce these comments, we often use <i>That’s like …</i></b></p><p class="ex-line">That’s like my '
        'sister. She’s really lazy too.</p></div>'
        '<h3>Synonyms <small>(p. 85)</small></h3>'
        '<div class="box"><p><b>Although synonyms share meanings and can share collocations, they are often not interchangeable. '
        'They will have different collocations or use a different grammar.</b></p><table class="voc">' +
        "".join(f"<tr><td><b>{k}</b></td><td>{t.replace('~', '…')}</td></tr>" for t, k in X.SYN) + "</table></div>"
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 87)</small></h4><p><b><i>if you ask me</i></b> = '
        '<i>in my opinion</i>.</p><p><i>If you ask me, it does more harm than good.<br>If you ask me, it’s stupid.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 83)</small></h4><p><i>He’s very sweet and affectionate, but he can be '
        'quite naughty sometimes.<br>You can be so stubborn sometimes!<br>He can be very nice when he wants to be.</i></p></div>'
        "</div></article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 82–87</span><h2>Vocabulary</h2>'
             '<h3>Describing character <small>(p. 82)</small></h3>' + X.wordbox(X.CHAR1 + X.CHAR2) +
             '<h3>Words from the text <small>(p. 86)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{k}</b></td><td>{t.format('…')}</td></tr>" for t, k in X.DEFS) + "</table></article>")
    toc = ('<nav class="toc"><a href="#gr151">Used to, would; wish</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(151, "gr151", g151) + unit_boxes + vocab
