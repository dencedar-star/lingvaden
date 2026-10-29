"""Страница «Теория»: Grammar reference pp. 140–141 (из OCR) и правила из уроков юнита 03."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX[140] = [("last week, It was", "last week. It was"), ("last month. X", "last month. ✗"), ("I went...", "I went … ✓"),
            ("but / was told", "but I was told"), ("Yes, / have now", "Yes, I have now")]
FIX[141] = [("B: I’II go I’m going to Bulgaria. I’ll spend I’m going to spend",
             "B: <s>I’ll go</s> I’m going to Bulgaria. <s>I’ll spend</s> I’m going to spend"),
            ("appointment /class.", "appointment / class.")]

HEADS141 = ("THE FUTURE", "Questions", "Definite plans", "The present continuous and be going to", "Uncertain plans",
            "Will", "Might")


def build():
    g140 = grammar_ref(140, (40, 110, 350, 985), heads=("Present perfect questions",),
                       breaks=("Use the past simple to talk and ask about the details", "Do not use the present perfect with past time"))
    g141 = (grammar_ref(141, (75, 110, 410, 985), heads=HEADS141) +
            grammar_ref(141, (435, 110, 750, 375), heads=HEADS141))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 20–25</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Present perfect questions <small>(p. 23)</small></h3>'
        '<div class="box"><p class="ex-line">A: <i>Have you been</i> away on holiday recently?<br>'
        'B: Yes, I went camping in Tuscany. <i>Have you ever been</i> there?<br>A: No, never. What’s it like?</p><hr>'
        '<p><b>To ask about general experiences before now, we often use the present perfect simple. Don’t just give a '
        '<i>Yes</i> or <i>No</i> answer – add a comment.</b></p></div>'
        '<h3>The future <small>(p. 25)</small></h3>'
        '<div class="box"><p><b>We use lots of different forms to talk about the future.</b></p><hr><table class="voc">' +
        "".join(f"<tr><td>{s}</td></tr>" for s in X.FUT) + "</table><hr>" +
        "".join(f"<p>{l}) {d}</p>" for l, d in zip("abcd", X.FUT_DEF)) +
        '<p class="note-s">Ключ: 1 a 2 a 3 b 4 d 5 a, c 6 a 7 b, d</p></div>'
        '<h3>Recommendations <small>(p. 21)</small></h3>'
        '<div class="box"><p class="ex-line">I’m thinking of doing some shopping today. Can you recommend anywhere?<br>'
        'Well, you could try Oxford Street.<br>To be honest, I’m not really a big fan of department stores.<br>'
        'Oh, OK. Well, in that case, how about Portobello Road?</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 25)</small></h4><p><b><i>at some point</i></b> — '
        'If you do something <i>at some point</i>, you do it at one moment, but you do not know when exactly.</p>'
        '<p><i>I need to go to the bank at some point today.<br>I’ll definitely see him at some point this week.<br>'
        'We went the wrong way at some point and got completely lost.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 24)</small></h4><p><i>It depends on the weather.<br>'
        'It depends (on) whether it’s raining (or not).<br>It depends (on) how much it costs.<br>'
        'It depends (on) how far it is to walk.<br>It depends (on) how long it’ll take.<br>'
        'It depends (on) what time I get up.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 20, 22, 24</span><h2>Vocabulary</h2>'
             '<h3>Places of interest <small>(p. 20)</small></h3>' + X.wordbox(X.BOX1 + X.BOX2) +
             '<p class="ex-line">about ten miles <b>outside of town</b> · <b>out in the</b> west of the city · '
             '<b>down by the</b> river · <b>all along the</b> coast</p>'
             '<h3>Holiday problems <small>(p. 22)</small></h3>' + X.wordbox(X.PROBLEMS_BOX) +
             '<h3>Weather <small>(p. 24)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in zip(X.WEATHER, [X.WEATHER_END[i] for i in (2, 3, 5, 0, 1, 4, 7, 6)])) +
             "</table></article>")
    writing = ('<article class="page" id="stories"><span class="page-no">Учебник, с. 124–125</span><h2>Writing: stories</h2>'
               '<h3>Just about to, just as</h3>'
               '<div class="box"><p><b><i>Was / Were (just) about to</i> + verb is used to talk about something you were '
               'planning to do before something else happened. <i>When suddenly</i> often follows <i>just about to</i>.</b></p>'
               '<p class="ex-line">I was just about to jump when it suddenly hit me!</p><hr>'
               '<p><b><i>Just as</i> is used to emphasise that two verbs happened at exactly the same time. It is more common '
               'to use the past continuous after <i>just as</i>, but the past simple is also possible.</b></p>'
               '<p class="ex-line">Just as I was thinking about maybe changing my mind, the voice behind me screamed, '
               '‘Go! Go! Go!’<br>Just as I turned on the computer, the lights went out.</p></div>'
               '<h3>Ways of doing things</h3><div class="box"><p><b>Using descriptive verbs makes stories more exciting.</b></p>'
               '<p class="ex-line">The voice behind me screamed, ‘Go! Go! Go!’</p></div><table class="voc">' +
               "".join(f"<tr><td><b>{v}</b></td><td>{d}</td></tr>" for d, v in X.DEFS) + "</table></article>")
    toc = ('<nav class="toc"><a href="#gr140">Present perfect questions</a><a href="#gr141">The future</a>'
           '<a href="#boxes">Правила из уроков</a><a href="#vocab">Vocabulary</a><a href="#stories">Stories</a></nav>')
    return toc + gr_page(140, "gr140", g140) + gr_page(141, "gr141", g141) + unit_boxes + vocab + writing
