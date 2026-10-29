"""Страница «Теория»: Grammar reference p. 155 (из OCR) и правила из уроков юнита 16."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX[155] = FIX.get(155, []) + [("that / was born in", "that I was born in"), ("(that) | have", "(that) I have")]


def build():
    g155 = grammar_ref(155, (80, 110, 400, 990), heads=("Defining relative clauses",),
                       breaks=("To add information about a person",))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 110–115</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Defining relative clauses <small>(p. 113)</small></h3>'
        '<div class="box"><p><b>We often use relative clauses to add information after a noun:</b></p>'
        '<p class="ex-line">He was a Czech writer <i>who wrote about education</i>.</p><hr>'
        '<p>You can also use <i>that</i> instead of <i>who</i>.<br>Things — <i>that</i> or <i>which</i>; times — <i>that</i> or '
        '<i>when</i>; possessions — <i>whose</i>; places — <i>where</i>.</p></div>'
        '<h3>Apparently <small>(p. 111)</small></h3>'
        '<div class="box"><p><b>We often introduce sentences about things in the news with <i>apparently</i>. This shows we are '
        'not 100% certain these facts are true – we are just reporting what we have heard.</b></p>'
        '<p class="ex-line">Apparently, she found out her husband was having an affair with another Hollywood actress.</p></div>'
        '<h3>Responding to news <small>(p. 111)</small></h3>'
        '<div class="box"><p><b>When we comment on things people tell us, we often add the question tags <i>wasn’t it? / isn’t '
        'it?</i> As we expect people to agree with us in these situations, our voice goes down on the tag.</b></p>'
        '<p class="ex-line">Yeah. It was shocking, wasn’t it?<br>I know. It’s crazy, isn’t it?</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 114)</small></h4><p><b><i>easier said than '
        'done</i></b> — when we think someone’s advice or suggestion sounds good, but is actually very difficult to do.</p>'
        '<p><i>I know I should stop smoking, but it’s easier said than done.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 111)</small></h4><p><i>Did you see that thing on TV about the '
        'mobile phone factory closing down?<br>Did you read about Paris Simpson getting arrested?<br>Did you hear about Laura '
        'losing her job?</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 110, 112, 114</span><h2>Vocabulary</h2>'
             '<h3>Newspapers <small>(p. 110)</small></h3>' +
             X.wordbox(["national news", "international news", "the business pages", "the sports pages", "the letters page",
                        "the gossip pages", "the reviews", "the horoscopes"]) +
             '<p class="ex-line">marks out of ten · exchange rate · premiere · the score · ceasefire · star sign</p>'
             '<h3>Explaining who people are <small>(p. 112)</small></h3>' + X.wordbox(X.WHO) +
             '<p class="ex-line">studied radiation · discovered · campaigned for the rights of · was responsible for the deaths '
             'of · led the liberation struggle · set the world record · is considered the father of · developed a vaccine '
             'against · whose most famous work is</p>'
             '<h3>Collocations from <i>Seeking fame and fortune</i> <small>(p. 114)</small></h3>'
             '<p class="ex-line">that option isn’t available · follow in his footsteps · no barrier to · got out of control · '
             'left me a house in her will · saved my life · forward the email · caught my eye · repay your kindness · came into '
             'a lot of money</p></article>')
    toc = ('<nav class="toc"><a href="#gr155">Defining relative clauses</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a></nav>')
    return toc + gr_page(155, "gr155", g155) + unit_boxes + vocab
