"""Страница «Теория»: Grammar reference p. 144 (из OCR) и правила из уроков юнита 05."""
from grammar import grammar_ref, gr_page
from . import shared as X


def build():
    g144 = (grammar_ref(144, (33, 105, 340, 712)) +
            grammar_ref(144, (398, 105, 716, 548), breaks=("When the rule says it is OK to do something, people",)))
    unit_boxes = (
        '<article class="page" id="boxes"><span class="page-no">Учебник, с. 36–41</span>'
        '<h2>Правила из уроков юнита</h2>'
        '<h3><i>Have to, don’t have to, can</i> <small>(p. 38)</small></h3>'
        '<div class="box"><p><b>We use <i>have to</i> to talk about rules. We also use <i>have to</i> for things that we feel are '
        'essential to do.</b></p><hr><p><b>We use <i>don’t have to</i> for something which is not necessary. We also use '
        '<i>don’t have to</i> when there is no rule (the person can choose to do something or not).</b></p><hr><p><b>We use '
        '<i>can</i> to show something is possible.</b></p><hr><p class="ex-line"><i>I have to work</i> really long hours '
        'sometimes.<br>I’m glad <i>I don’t have to work</i> tonight!<br><i>I can walk</i> to work. The office is really close to '
        'my flat.</p></div>'
        '<h3>Talking about rules <small>(p. 39)</small></h3>'
        '<div class="box"><p><b>We sometimes use <i>be allowed to</i> instead of <i>can</i> to talk about permission. We use '
        '<i>be supposed to</i> and <i>should really</i> instead of <i>have to</i>, especially when the rules are often broken.'
        '</b></p><hr><p class="ex-line">They have a strict dress code – woman <i>aren’t</i> even <i>allowed to wear</i> smart '
        'trousers.<br><i>You’re not supposed to</i> use the company computers.<br><i>You should really arrange</i> time off with '
        'me a month in advance.</p></div>'
        '<h3><i>Be used to, get used to</i> <small>(p. 41)</small></h3>'
        '<div class="box"><p><b>We use <i>be used to</i> when a habit or situation is normal for us because of our experience. '
        'This habit might be difficult for other people.</b></p><p class="ex-line">Some people find working with kids difficult, '
        'but <i>I’m used to it</i>. I have five brothers and sisters who are younger than me.</p><hr><p><b>We use <i>get used '
        'to</i> when a habit or situation is changing from being difficult to being normal / easy. We use it with lots of '
        'tenses.</b></p><p class="ex-line">I never had to wear a suit and tie before I had this job. I’d still prefer something '
        'less formal, but <i>I’m slowly getting used to it</i>.</p></div>'
        '<h3><i>That must be …</i> <small>(p. 37)</small></h3>'
        '<div class="box"><p><b>In conversations we often give our opinion of what we think of the other speaker’s job or '
        'situation using <i>That must be</i> + adjective.</b></p><p class="ex-line">A: Sometimes I do something like fifty or '
        'sixty hours a week.<br>B: Really? <i>That must be</i> stressful.</p></div>'
        '<div class="cols"><div class="note"><h4>Native speaker English <small>(p. 37)</small></h4><p><b><i>Rep</i></b> is short '
        'for <i>representative</i>. You can be <i>a sales rep, a holiday rep, a class rep</i>, etc. We also use <i>admin</i> '
        'instead of <i>administration</i> and <i>HR</i> instead of <i>human resources</i>.</p></div>'
        '<div class="note"><h4>Language patterns <small>(p. 37)</small></h4><p><i>It’s quite a creative job, which is nice.<br>'
        'It’s quite well-paid, which is good.<br>I have to work 14 hours a day, which is really tiring.<br>I didn’t get the '
        'promotion, which was a bit disappointing.<br>My old office overlooked a park, which was nice.</i></p></div></div>'
        "</article>")
    vocab = ('<article class="page" id="vocab"><span class="page-no">Учебник, с. 36–41</span><h2>Vocabulary</h2>'
             '<h3>Jobs <small>(p. 36)</small></h3>' + X.wordbox(X.JOBS_BOX + X.PIC_JOBS) +
             '<p class="ex-line">competitive · well-paid · rewarding · insecure · responsibility · creative · stressful · '
             'physically demanding · varied · paperwork</p>'
             '<h3>Workplaces and activities <small>(p. 37)</small></h3><table class="voc">' +
             "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in zip(X.WP, [X.WP_END[i] for i in (2, 4, 3, 1, 0)])) +
             '</table><h3>Collocations <small>(p. 39)</small></h3><p class="ex-line">' +
             " · ".join(" ".join(c) for c in X.COLL) + "</p></article>")
    writing = ('<article class="page" id="changes"><span class="page-no">Учебник, с. 128–129</span><h2>Writing: suggesting '
               'changes</h2><p class="ex-line">I am writing on behalf of … · On the whole, … · However, we were wondering if we '
               'could possibly suggest one change. · At the moment, we are scheduled to … · Alternatively, … · We are sorry if '
               'this causes any inconvenience, but …</p><h3>Programme</h3><p class="ex-line">put together / include / swap '
               'things round in the programme · a last-minute change · a full / an exciting programme</p>'
               '<h3><i>However, although</i> and <i>but</i></h3><div class="box"><p><b><i>Although</i> and <i>but</i> connect '
               'two parts of the same sentence. <i>Although</i> usually starts the sentence, but can come in the middle.</b></p>'
               '<p><b><i>However</i> always connects to an idea in a previous sentence. It usually starts the second sentence, but '
               'it can come in the middle or at the end of the second sentence.</b></p></div></article>')
    toc = ('<nav class="toc"><a href="#gr144">Have to · Rules</a><a href="#boxes">Правила из уроков</a>'
           '<a href="#vocab">Vocabulary</a><a href="#changes">Suggesting changes</a></nav>')
    return toc + gr_page(144, "gr144", g144, "05 Working life") + unit_boxes + vocab + writing
