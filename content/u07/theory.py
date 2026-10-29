"""Страница «Теория»: Grammar reference p. 146 (из OCR) и правила из уроков юнита 07."""
from ocrtext import FIX
from grammar import grammar_ref, gr_page
from . import shared as X

FIX.setdefault(146, []).extend([("if when you see", "if <s>when</s> you see"), ("If When I pass", "If <s>When</s> I pass"),
                                ("exam, ‘ll just", "exam, I’ll just")])
HEADS = ("After, once and when", "First conditionals", "Zero conditionals", "Other conditional sentences with present tenses")


def build():
    g146 = (grammar_ref(146, (45, 110, 400, 398), heads=HEADS) +
            grammar_ref(146, (45, 650, 400, 1000), heads=HEADS, breaks=("The other part of the sentence talks about the future",)) +
            grammar_ref(146, (405, 380, 794, 662), heads=HEADS))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 48–53</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3>After, once and when <small>(p. 49)</small></h3>'
        '<div class="box"><p><b>When a clause starts with <i>after</i>, <i>once</i> or <i>when</i>, we can then use the present '
        'simple or present perfect although we’re referring to the future. Using the present perfect emphasises a finished '
        'action.</b></p><hr><p class="ex-line">What are you going to do once <i>the course has finished</i>?<br>'
        '<i>When I’m there</i>, I might look for a job.<br><i>After I get back</i> from Australia, I’ll just start looking for a '
        'proper job.</p></div>'
        '<h3>Zero and first conditionals <small>(p. 53)</small></h3>'
        '<div class="box"><p><b>We use present tenses in the <i>if</i> clause to talk either a) about real present situations or '
        'b) possible future situations. The other half of the sentence uses different verb forms, according to their normal '
        'meanings.</b></p><hr><p><b>In zero conditionals, we use the present simple to talk about real repeated actions in the '
        'present.</b></p><hr><p><b>In first conditionals, we use <i>will</i> to talk about definite decisions and consequences '
        'in the future. <i>Might</i> is used to talk about possible ones.</b></p><hr><p><b>In some conditional sentences, we use '
        'imperatives and <i>should</i> to give advice.</b></p></div>'
        '<h3>How’s the course going? <small>(p. 49)</small></h3>'
        '<div class="box"><p class="ex-line">I’ve had a few ups and downs of course, but the tutors have been very helpful and '
        'supportive.<br>OK, but I’ve got my final exams next week, so I’m having to do lots of revision at the moment.<br>'
        'Actually I’m struggling at the moment. I just can’t cope with the workload. It’s really demanding.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 50)</small></h4><p><b><i>in mind</i></b> — '
        'If you have something <i>in mind</i>, you are thinking of this thing.</p><p><i>Such ideas are not really what Oliver '
        'James has in mind.<br>Have you got anywhere in mind for your holiday?<br>What have you got in mind?</i></p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 49)</small></h4><p><i>I’m glad (that) it’s going well.<br>'
        'I’m glad (that) you’re feeling better.<br>I’m glad (that) everything is OK.<br>'
        'I’m glad to hear the accident wasn’t that serious.<br>I’m glad to see they’ve finally fixed the lift!</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 48, 50, 52</span><h2>Vocabulary</h2>'
             '<h3>Describing courses <small>(p. 48)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{k}</b></td><td>{t}</td></tr>" for t, k in X.COLL) + "</table>"
             '<h3>Forming words <small>(p. 50)</small></h3><table class="voc"><tr><th>noun</th><th>verb</th></tr>'
             '<tr><td>education</td><td>educate</td></tr><tr><td>failure</td><td>fail</td></tr>'
             '<tr><td>achievement</td><td>achieve</td></tr><tr><td>calculation</td><td>calculate</td></tr>'
             '<tr><td>appreciation</td><td>appreciate</td></tr><tr><td>encouragement</td><td>encourage</td></tr>'
             '<tr><td>inspiration</td><td>inspire</td></tr></table>'
             '<h3>Words from the article <small>(p. 51)</small></h3><table class="voc">' +
             "".join(f"<tr><td><b>{w}</b></td><td>{d}</td></tr>" for w, d in X.BOLD) + "</table>"
             '<h3>Schools, teachers and students <small>(p. 52)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{t}</td><td>{w.replace('|', ' / ')}</td><td>{pn}</td></tr>" for t, w, pn in X.STS) +
             "</table></article>")
    writing = ('<article class="page" id="essay"><span class="page-no">Учебник, с. 132–133</span><h2>Writing: for and against</h2>'
               '<h3>Describing trends</h3><div class="box"><p><b>We usually begin introductions to essays by describing current '
               'trends (or problems) connected to the title. To describe a change that happened before now, but which has present '
               'results, use the present perfect simple.</b></p><p class="ex-line">The number of cars on our roads has increased '
               'a lot over the last twenty years.</p><hr><p><b>To describe a trend that is not finished, we usually use the '
               'present continuous.</b></p><p class="ex-line">Traffic is getting worse every year and we are slowly running out '
               'of oil.</p></div><h3>As such</h3><div class="box"><p><b>To introduce results or conclusions, we often use '
               '<i>as such</i>. It means ‘Because what has just been said is true.’ It usually begins a sentence and is followed '
               'by a comma.</b></p></div></article>')
    toc = ('<nav class="toc"><a href="#gr146">After, once, when · conditionals</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#essay">For and against</a></nav>')
    return toc + gr_page(146, "gr146", g146) + unit_boxes + vocab + writing
