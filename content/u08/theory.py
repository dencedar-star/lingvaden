"""Страница «Теория»: Grammar reference p. 147 (из OCR) и правила из уроков юнита 08."""
from grammar import grammar_ref, gr_page
from . import shared as X

HEADS = ("tend to", "Second conditionals")


def build():
    g147 = (grammar_ref(147, (90, 128, 400, 372), heads=HEADS, breaks=("There are several other ways of doing this as well.",)) +
            grammar_ref(147, (90, 655, 400, 1040), heads=HEADS,
                        breaks=("Either part of the sentence can come first. When the",
                                "Using If I / he / she / it was like this is very common.")))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 54–59</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>tend to <small>(p. 57)</small></h3>'
        '<div class="box"><p class="ex-line">The portions here <i>tend to be</i> enormous.<br>People <i>tend to buy</i> fresh food '
        'every day and cook.<br>They <i>tend not to eat</i> while they’re drinking.</p><hr><p><b>We use <i>tend to</i> before a '
        'verb to mean <i>usually, but not always</i>. The negative form is <i>tend not to</i> or <i>don’t tend to</i>.</b></p></div>'
        '<h3>Second conditionals <small>(p. 59)</small></h3>'
        '<div class="box"><p class="ex-line">They might attract a few more people if they redecorated.<br>It would be better if it '
        'didn’t have so much sauce on it!<br>What would happen if they called the police?</p><hr><p><b>These sentences are all '
        'examples of the second conditional. The <i>if</i> part of the sentence is in the past simple (or continuous). This shows '
        'the speaker thinks a situation in the present or in the future is impossible to change or is not actually going to take '
        'place. The other part of the sentence uses either <i>would</i> + base form – to show a definite result or <i>might</i> '
        '+ base form – to show a possible result.</b></p></div>'
        '<h3>Describing dishes <small>(p. 55)</small></h3>'
        '<div class="box"><p class="ex-line"><i>It’s a kind of</i> vegetable / side dish / spice.<br><i>It’s a bit like</i> an '
        'oyster, <i>but</i> smaller.<br><i>It’s a bit like</i> vodka, <i>but not as</i> strong.<br><i>It’s made from</i> pig’s '
        'blood / a special kind of bean.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 58)</small></h4><p><b><i>No wonder</i></b> — '
        'If you say <i>(It’s) no wonder</i> something happened, it means you are not surprised about it.</p><p><i>No wonder he '
        'overslept this morning! He didn’t get to bed till three last night.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 57)</small></h4><p><i>Just because you’re foreign, it doesn’t mean '
        '(that) you can’t learn how to use chopsticks!<br>Just because I’m a man, it doesn’t mean (that) I can’t cook.<br>'
        'Just because you can it doesn’t mean (that) you should.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 54, 58</span><h2>Vocabulary</h2>'
             '<h3>Ways of cooking <small>(p. 54)</small></h3>' + X.wordbox(X.COOK) +
             '<p class="ex-line">spicy · fattening · tasty · greasy · bland · filling</p>'
             '<h3>Restaurants <small>(p. 58)</small></h3><p class="ex-line">It’s always packed. · It’s always deserted. · It looks '
             'out over the sea. · The portions are huge. · The food’s very rich. · It’s home-style cooking. · It only does seafood. '
             '· It’s got trendy décor. · The food’s quite greasy. · It’s all organic.</p>'
             '<h3>over- <small>(p. 58)</small></h3><p><b>We add <i>over-</i> to some verbs to mean <i>too much</i>.</b></p>' +
             X.wordbox(X.OVER) + "</article>")
    writing = ('<article class="page" id="review"><span class="page-no">Учебник, с. 134–135</span><h2>Writing: a review</h2>'
               '<h3>Describing films</h3>' + X.wordbox(X.ADJ + ["well-chosen", "superbly acted", "well-written",
                                                                "beautifully filmed", "brilliantly directed"]) +
               '<h3>While and during</h3><div class="box"><p><b><i>during</i> + noun</b> — during the Second World War<br>'
               '<b><i>while</i> + clause</b> — While they are there, the father distracts the boy …</p></div>'
               '<h3>Adding information after the noun</h3><div class="box"><p><b>We often make a text shorter by adding '
               'information after a noun using an <i>-ed / -ing</i> participle, a prepositional phrase, or relative clause.</b></p>'
               '<p class="ex-line">This is a strangely uplifting film directed by and starring Roberto Benigni.</p></div></article>')
    toc = ('<nav class="toc"><a href="#gr147">tend to · Second conditionals</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#review">A review</a></nav>')
    return toc + gr_page(147, "gr147", g147) + unit_boxes + vocab + writing
