"""Страница «Теория»: Grammar reference p. 152 (из OCR) и правила из уроков юнита 13."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX[152] = [("If wed been", "If we’d been"), ("If we would’ve left had left", "If we <s>would’ve left</s> had left"),
            ("Use: - would", "Use:<br>– would"), (" - could", "<br>– could")]


def build():
    g152 = (grammar_ref(152, (45, 110, 380, 560), heads=("Third conditionals",)) +
            grammar_ref(152, (400, 110, 740, 570), heads=("Should have",),
                        breaks=("Should’ve explains good things", "Shouldn’t have explains things")))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 92–97</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>Third conditionals <small>(p. 95)</small></h3>'
        '<div class="box"><p class="ex-line">If she hadn’t been so determined, she would never have made it to Australia.<br>'
        'I would probably have ended up in trouble if I had stayed there.</p><hr>'
        '<p><b>These are examples of a third conditional. The <i>if</i> part of the sentence uses the past perfect to talk '
        'about imagined situations in the past. The second part of the sentence uses <i>would / might + have</i> + the past '
        'participle to talk about the results of the imagined situation.</b></p></div>'
        '<h3>Should have <small>(p. 97)</small></h3>'
        '<div class="box"><p><b>We use <i>should have / should not have</i> + past participle to talk about things that went '
        'wrong in the past. <i>Should have</i> explains good things you failed to do or that you were unable to do. '
        '<i>Should not have</i> explains things you did that were a bad idea.</b></p></div>'
        '<h3>Blaming people <small>(p. 97)</small></h3>'
        '<div class="box"><p><b>We use <i>it’s my / his fault</i> or <i>I blame myself / him</i> to say who caused a problem. '
        'We often use <i>should have</i> and the third conditional as well.</b></p>'
        '<p class="ex-line">Don’t blame me. You should’ve read the small print.<br>It’s not his fault – it’s yours!<br>'
        'I blame myself. I should’ve listened to my dad.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 96)</small></h4><p><b><i>I bet</i></b> — '
        'we often use <i>I bet</i> to respond to what people have told us. It means <i>I’m sure</i>.</p>'
        '<p><i>A: It was boiling.<br>B: Lucky you! I bet that was nice.</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 93)</small></h4><p><i>I got completely lost and ended up going round '
        'in circles for ages.<br>Whenever I drive, we end up arguing.<br>We got lost and ended up in the middle of nowhere.'
        '<br>A lot of ex-soldiers end up homeless.<br>If he keeps driving like that, he’ll end up dead!</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 92, 93, 96</span><h2>Vocabulary</h2>'
             '<h3>Ways of travelling and travel problems <small>(p. 92)</small></h3><table class="voc">'
             '<tr><td><b>By train</b></td><td>carriage, line, platform, (level) crossing · railway, station, compartment</td></tr>'
             '<tr><td><b>By ferry</b></td><td>crossing, deck, harbour · boat, port, foot passenger</td></tr>'
             '<tr><td><b>By car</b></td><td>bend, tyre, traffic lights · traffic jam, motorway, crossroads</td></tr>'
             '<tr><td><b>By plane</b></td><td>take-off, check-in desk, security · passport control, crew, customs</td></tr>'
             '</table>'
             '<h3>Phrasal verbs <small>(p. 93)</small></h3><div class="box"><p><b>A phrasal verb is a verb – <i>put, throw, '
             'take</i>, etc. – plus a particle like <i>up, off, out, down</i>, etc. Phrasal verbs are more colloquial and '
             'informal than single word verbs.</b></p></div><table class="voc">' +
             "".join(f"<tr><td><b>{a}</b></td><td>{b}</td></tr>" for a, b in [
                 ("hang around", "sit, wait and not do much"), ("go through", "experience something unpleasant"),
                 ("check in", "sign and get your room (at a hotel) / register for a flight"), ("set off", "start a journey"),
                 ("pour down", "rain very heavily"), ("work out", "find an answer to a problem"), ("get back", "return"),
                 ("calm down", "stop feeling so angry and upset")]) + "</table>"
             '<h3>Strong adjectives <small>(p. 96)</small></h3><div class="box"><p><b>A small group of adjectives contain the '
             'idea of <i>very</i>. For example, <i>terrified</i> means <i>very scared</i>. To make them stronger, we use '
             '<i>really</i> or <i>absolutely</i>, not <i>very</i>.</b></p></div><table class="voc">' +
             "".join(f"<tr><td><b>{a}</b></td><td>very {b}</td></tr>" for a, b in [
                 ("boiling", "hot"), ("freezing", "cold"), ("huge", "big"), ("delicious", "good (food)"),
                 ("fantastic", "good"), ("soaked", "wet"), ("filthy", "dirty"), ("exhausted", "tired"),
                 ("packed", "crowded"), ("fascinating", "interesting"), ("furious", "angry"), ("starving", "hungry")]) +
             "</table></article>")
    writing = ('<article class="page" id="essay"><span class="page-no">Учебник, с. 132–133</span><h2>Writing: for and against</h2>'
               '<h3>Describing trends</h3><div class="box"><p><b>To describe a change that happened before now, but which has '
               'present results, use the present perfect simple.</b></p><p class="ex-line">The number of cars on our roads has '
               'increased a lot over the last twenty years.</p><hr><p><b>To describe a trend that is not finished, we usually '
               'use the present continuous.</b></p><p class="ex-line">Traffic is getting worse every year and we are slowly '
               'running out of oil.</p></div>'
               '<h3>As such</h3><div class="box"><p><b>To introduce results or conclusions, we often use <i>as such</i>. It means '
               '‘Because what has just been said is true.’ It usually begins a sentence and is followed by a comma.</b></p></div>'
               '<h3>Linking words in an essay</h3>' + X.wordbox(X.ESSAY_BOX) + "</article>")
    toc = ('<nav class="toc"><a href="#gr152">Third conditionals · should have</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#essay">For and against</a></nav>')
    return toc + gr_page(152, "gr152", g152) + unit_boxes + vocab + writing
