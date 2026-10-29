/* lingvaden.ru — рабочее место ученика: курсы, домашние работы («Отправить учителю»), результаты, профиль */
(function () {
  "use strict";
  var app = document.getElementById("s-app");
  if (!app || !window.EN) return;
  var EN = window.EN, esc = EN.esc, post = EN.post, API = EN.api, ROOT = document.body.dataset.root || "/";
  var ST = null, CAT = null, EXMAP = {};
  var PAGE_T = { tests: "Тесты", book: "Учебник", writing: "Письмо", theory: "Теория", workbook: "Тетрадь" };

  function $(s, r) { return (r || app).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || app).querySelectorAll(s)); }
  function get(a, q) {
    return fetch(API + a + (q || ""), { credentials: "same-origin", cache: "no-store" }).then(function (r) {
      if (r.status === 401) { location.href = ROOT; throw 0; }
      return r.json();
    });
  }
  function when(s) {
    if (!s) return "—";
    var d = new Date(s.replace(" ", "T") + "+03:00"), now = new Date();
    var t = d.toLocaleTimeString("ru-RU", { hour: "2-digit", minute: "2-digit" });
    var days = Math.floor((new Date(now.toDateString()) - new Date(d.toDateString())) / 864e5);
    if (days === 0) return "сегодня " + t;
    if (days === 1) return "вчера " + t;
    return d.toLocaleDateString("ru-RU", { day: "numeric", month: "short" }) + " " + t;
  }
  function day(s) { return s ? new Date(s.replace(" ", "T") + "+03:00").toLocaleDateString("ru-RU", { day: "numeric", month: "long" }) : ""; }
  function pctCls(p) { return p >= 80 ? "hi" : p >= 50 ? "mid" : p > 0 ? "lo" : "none"; }
  function catalog() {
    if (CAT) return Promise.resolve(CAT);
    return fetch(ROOT + "assets/catalog.json?v=" + (window.EN && EN.ver || ""), { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (c) {
      CAT = c;
      c.courses.forEach(function (co) { co.units.forEach(function (u) { u.pages.forEach(function (p) { p.ex.forEach(function (e) { EXMAP[e[0]] = { unit: u, page: p, let: e[2], ins: e[3], n: e[1] }; }); }); }); });
      return c;
    });
  }

  var TITLES = { courses: 1, homework: 1, results: 1, profile: 1 };
  function route() {
    var h = location.hash.replace("#", "") || "courses";
    var hw = /^hw=(\d+)/.exec(h), key = hw ? "homework" : h.split("&")[0];
    if (!TITLES[key]) key = "courses";
    EN.markSide(key === "profile" ? "" : key);
    app.innerHTML = '<div id="s-view"><p class="lead">Загрузка…</p></div>';
    var v = $("#s-view");
    scrollTo(0, 0);
    if (hw) return runner(v, +hw[1]);
    ({ courses: coursesView, homework: homeworkView, results: resultsView, profile: profileView })[key](v);
  }
  addEventListener("hashchange", function () { if (ST) route(); });

  /* ---------------- курсы ---------------- */
  function unitStat(u) {
    var s = 0, t = 0, done = 0, n = 0;
    u.pages.forEach(function (p) { p.ex.forEach(function (x) { n++; t += x[1]; var sc = EN.lsGet("score:" + x[0]); if (sc) { done++; s += sc.best || sc.s; } }); });
    return { s: s, t: t, done: done, n: n, pct: t ? Math.round(100 * s / t) : 0 };
  }
  function coursesView(v) {
    catalog().then(function (cat) {
      var last = EN.lsGet("last");
      var h = '<h1 class="page-title">Здравствуйте, ' + esc(String(ST.name).split(" ")[0]) + "!</h1><p class=\"lead\">Ваш преподаватель — <b>" + esc(ST.teacher || "") + "</b>." +
        (ST.offline ? " Нет связи с сервером — показан прогресс с этого устройства." : "") + "</p>";
      if (ST.hw_open) h += '<a class="hw-call" href="#homework">Домашних работ к выполнению: <b>' + ST.hw_open + "</b> — открыть →</a>";
      if (last) h += '<p><a class="btn" href="' + esc(last.path) + '">Продолжить: ' + esc(last.title) + "</a></p>";
      var one = cat.courses.length === 1;
      cat.courses.forEach(function (c) {
        var tot = 0, got = 0;
        var tiles = c.units.map(function (u) {
          var r = unitStat(u); tot += r.t; got += r.s;
          return '<a class="u-tile" href="' + esc(u.url) + '"><span class="u-n">' + esc(u.n) + '</span><span class="u-txt"><b>' + esc(u.title) + "</b><small>" +
            (r.done ? "сделано " + r.done + " из " + r.n + " · " + r.pct + "%" : "заданий: " + r.n) + '</small><span class="mini-bar"><i class="' + pctCls(r.pct) + '" style="width:' + r.pct + '%"></i></span></span></a>';
        }).join("");
        var pct = tot ? Math.round(100 * got / tot) : 0;
        h += '<details class="course-card"' + (one ? " open" : "") + '><summary>' + (c.cover ? '<img class="cc-cover" src="' + esc(c.cover) + '" alt="" loading="lazy">' : '<span class="cc-ic">' + EN.icon("book") + "</span>") + '<span class="cc-t"><b>' + esc(c.title) +
          "</b><small>" + c.units.length + " модулей · пройдено " + pct + '%</small></span><span class="cc-chev" aria-hidden="true"></span></summary><div class="u-tiles">' + tiles + "</div></details>";
      });
      v.innerHTML = h;
    });
  }

  /* ---------------- домашние работы ---------------- */
  function hwState(x) {
    if (x.submitted_at) return '<span class="tag on">отправлено ' + esc(when(x.submitted_at)) + "</span>" + (x.total ? ' <span class="sc ' + pctCls(Math.round(100 * x.score / x.total)) + '">' + x.score + " из " + x.total + "</span>" : "");
    if (x.opened_at) return '<span class="tag">в работе</span>';
    return '<span class="tag new">новая</span>';
  }
  function homeworkView(v) {
    get("s_hw_list").then(function (r) {
      var list = r.ok ? r.hw : [];
      var open = list.filter(function (x) { return !x.submitted_at; });
      EN.setBadge(open.length, "student"); ST.hw_open = open.length;
      v.innerHTML = '<h1 class="page-title">Домашние работы</h1><p class="lead">Работы от вашего преподавателя. Выполните задания и нажмите «Отправить учителю». ' +
        "После трёх неверных попыток правильный ответ подставится сам.</p>" +
        (list.length ? '<div class="hw-cards">' + list.map(function (x) {
          var late = x.due_at && !x.submitted_at && new Date(x.due_at.replace(" ", "T") + "+03:00") < new Date();
          return '<a class="hw-card' + (x.submitted_at ? " done" : "") + '" href="#hw=' + x.id + '"><div class="hw-t"><b>' + esc(x.title) + "</b>" + hwState(x) + "</div>" +
            "<small>заданий: " + x.n + (x.due_at ? ' · <span class="' + (late ? "late" : "") + '">сдать до ' + esc(day(x.due_at)) + "</span>" : "") + " · задано " + esc(when(x.created_at)) + "</small>" +
            (x.note ? '<p class="note-s">' + esc(x.note) + "</p>" : "") + '<span class="btn sm' + (x.submitted_at ? " ghost" : "") + '">' + (x.submitted_at ? "Посмотреть" : x.opened_at ? "Продолжить" : "Выполнить") + "</span></a>";
        }).join("") + "</div>" : '<div class="page"><p class="empty">Домашних работ пока нет.</p></div>');
    });
  }

  // выполнение работы: задания собираются со страниц курса и проверяются так же, как там
  var pageCache = {};
  function fetchPage(url) {
    if (!pageCache[url]) pageCache[url] = fetch(url, { credentials: "same-origin" }).then(function (r) { return r.text(); })
      .then(function (t) { return new DOMParser().parseFromString(t, "text/html"); });
    return pageCache[url];
  }
  function runner(v, id) {
    Promise.all([get("s_hw", "&id=" + id), catalog()]).then(function (x) {
      var r = x[0];
      if (!r.ok) { v.innerHTML = '<div class="page"><p class="empty">Работа не найдена. <a href="#homework">К домашним работам</a></p></div>'; return; }
      var hw = r.hw, ns = "hw" + hw.id + ":", done = !!hw.submitted_at;
      // ответы с другого устройства
      Object.keys(r.last || {}).forEach(function (ex) {
        var L = r.last[ex];
        if (L.st && !EN.lsGet(ns + "ans:" + ex)) EN.lsSet(ns + "ans:" + ex, L.st);
        if (L.t != null && !EN.lsGet(ns + "score:" + ex)) EN.lsSet(ns + "score:" + ex, { s: L.s, t: L.t, best: L.s });
        if ((EN.lsGet(ns + "fails:" + ex) || 0) < L.fails) EN.lsSet(ns + "fails:" + ex, L.fails);
        if (L.fails >= 3) EN.lsSet(ns + "auto:" + ex, 1);
      });
      v.innerHTML = '<div class="crumbs"><a href="#homework">Домашние работы</a></div><h1 class="page-title">' + esc(hw.title) + "</h1>" +
        '<p class="lead">Заданий: ' + hw.items.length + (hw.due_at ? " · сдать до " + esc(day(hw.due_at)) : "") + "</p>" +
        (hw.note ? '<div class="page hw-note"><b>Комментарий преподавателя:</b> ' + esc(hw.note) + "</div>" : "") +
        (done ? '<div class="hw-sent">✓ Работа отправлена учителю ' + esc(when(hw.submitted_at)) + (hw.total ? " · результат " + hw.score + " из " + hw.total : "") + "</div>" : "") +
        '<div id="hw-list"></div><div id="hw-foot"></div>';
      var list = $("#hw-list", v), regs = [];
      var urls = {};
      hw.items.forEach(function (it) { urls[ROOT + it.unit + "/" + it.page + ".html"] = 1; });
      Promise.all(Object.keys(urls).map(fetchPage)).then(function () {
        var chain = Promise.resolve();
        hw.items.forEach(function (it, i) {
          chain = chain.then(function () {
            return fetchPage(ROOT + it.unit + "/" + it.page + ".html").then(function (doc) {
              var src = doc.getElementById(it.ex), X = EXMAP[it.ex];
              var box = EN.el("section", "page hw-item", '<div class="hw-ih"><span class="hw-no">' + (i + 1) + "</span><div><small>Модуль " +
                esc(X ? X.unit.n : it.unit.replace("unit", "")) + " · " + esc(PAGE_T[it.page] || it.page) + '</small></div><a class="linkbtn" href="' + ROOT + it.unit + "/" + it.page + ".html#" + esc(it.ex) +
                '" target="_blank" title="Открыть задание на странице курса — с текстом и картинками">в учебнике ↗</a></div>');
              if (!src) { box.insertAdjacentHTML("beforeend", '<p class="empty">Задание не найдено — сообщите преподавателю.</p>'); list.appendChild(box); return; }
              var node = document.importNode(src, true);
              node.removeAttribute("id");
              $$("details.reveal", node).forEach(function (d) { d.remove(); });
              box.appendChild(node); list.appendChild(box);
              var reg = EN.setupEx(node, { ns: ns, c: hw.course, u: it.unit, p: it.page, hw: done ? 0 : hw.id, locked: done, onCheck: paintFoot });
              if (reg) { regs.push(reg); var sb = node.querySelector("[data-act=show]"); if (sb) sb.remove(); }
            });
          });
        });
        return chain;
      }).then(function () { paintFoot(); });
      function paintFoot() {
        var foot = $("#hw-foot", v); if (!foot) return;
        var checked = regs.filter(function (r2) { return r2.score(); }).length;
        var good = regs.filter(function (r2) { var s = r2.score(); return s && s.s === s.t; }).length;
        foot.innerHTML = '<div class="hw-submit page"><div><b>Проверено заданий: ' + checked + " из " + regs.length + "</b><br><small>полностью верно: " + good + "</small></div>" +
          (done ? '<span class="tag on">Отправлено</span>' : '<button class="btn big" type="button" data-send>Отправить учителю</button>') + '<div class="err" hidden></div></div>';
        var b = foot.querySelector("[data-send]");
        if (b) b.addEventListener("click", function () { submit(b); });
      }
      function submit(b) {
        regs.forEach(function (r2) { if (r2.dirty()) r2.check(); });   // введённое, но не проверенное — проверяем сейчас
        var left = regs.filter(function (r2) { return !r2.score(); }).length;
        if (left && !b.classList.contains("armed")) {
          b.classList.add("armed"); b.textContent = "Не выполнено заданий: " + left + ". Всё равно отправить?"; return;
        }
        b.disabled = true; b.textContent = "Отправляю…";
        Promise.resolve(EN.flush()).then(function () { return post("s_hw_submit", { id: hw.id }); }).then(function (res) {
          if (!res.ok && res.error !== "submitted") { b.disabled = false; b.textContent = "Отправить учителю"; var er = $("#hw-foot .err", v); er.hidden = false; er.textContent = "Не получилось отправить — проверьте связь и попробуйте ещё раз."; return; }
          EN.toast("Работа отправлена учителю");
          if (ST.hw_open) { ST.hw_open--; EN.setBadge(ST.hw_open, "student"); }
          route();
        });
      }
    });
  }

  /* ---------------- результаты ---------------- */
  function resultsView(v) {
    Promise.all([catalog(), get("s_hw_list")]).then(function (x) {
      var cat = x[0], hl = x[1].ok ? x[1].hw : [];
      var h = '<h1 class="page-title">Мои результаты</h1>';
      cat.courses.forEach(function (c) {
        h += '<section class="page"><h2>' + esc(c.title) + '</h2><table class="tbl"><tr><th>Модуль</th><th class="num">Заданий</th><th class="num">Верно</th><th>Прогресс</th></tr>';
        c.units.forEach(function (u) {
          var r = unitStat(u);
          h += '<tr><td><a href="' + esc(u.url) + '">' + esc(u.n) + " " + esc(u.title) + '</a></td><td class="num">' + r.done + " из " + r.n + '</td><td class="num">' + r.s + " из " + r.t +
            '</td><td><span class="mini-bar"><i class="' + pctCls(r.pct) + '" style="width:' + r.pct + '%"></i></span> ' + r.pct + "%</td></tr>";
        });
        h += "</table></section>";
      });
      var sent = hl.filter(function (y) { return y.submitted_at; });
      h += '<section class="page"><h2>Сданные домашние работы</h2>' + (sent.length ? '<table class="tbl"><tr><th>Работа</th><th>Отправлена</th><th class="num">Результат</th></tr>' +
        sent.map(function (y) { return '<tr><td><a href="#hw=' + y.id + '">' + esc(y.title) + "</a></td><td>" + esc(when(y.submitted_at)) + '</td><td class="num">' + (y.total ? y.score + " из " + y.total : "—") + "</td></tr>"; }).join("") +
        "</table>" : '<p class="empty">Пока нет.</p>') + "</section>";
      v.innerHTML = h;
    });
  }

  /* ---------------- профиль и данные ---------------- */
  function profileView(v) {
    v.innerHTML = '<div id="pf"></div><section class="page"><h2>Мои данные</h2><p>Ваши ответы, попытки, домашние работы, время занятий и тексты видит ваш преподаватель. ' +
      '<a href="' + ROOT + 'legal/privacy.html">Как мы храним данные</a>.</p>' +
      '<button class="btn danger-o" type="button" data-forget>Удалить мои данные</button>' +
      '<div class="confirm" hidden><p><b>Удалить всё?</b> Ответы, попытки, домашние работы, тексты и время занятий будут стёрты с сервера, код и ссылка ' +
      'перестанут работать, преподаватель больше не увидит ваш прогресс. Отменить нельзя.</p>' +
      '<button class="btn danger" type="button" data-forget-yes>Да, удалить</button> <button class="btn plain" type="button" data-forget-no>Отмена</button></div></section>';
    EN.profile($("#pf", v), "student", ST, function () { location.reload(); });
    var cf = $(".confirm", v);
    $("[data-forget]", v).addEventListener("click", function () { cf.hidden = false; });
    $("[data-forget-no]", v).addEventListener("click", function () { cf.hidden = true; });
    $("[data-forget-yes]", v).addEventListener("click", function () {
      post("forget", {}).then(function (r) {
        if (!r.ok) return;
        try { Object.keys(localStorage).forEach(function (k) { if (k.indexOf("en:s" + ST.id + ":") === 0) localStorage.removeItem(k); }); localStorage.removeItem("en_who"); } catch (e) {}
        location.href = ROOT;
      });
    });
  }

  /* ---------------- запуск: app.js сообщает, кто вошёл ---------------- */
  window.EN_ME = function (st) {
    if (!st) { location.href = ROOT; return; }
    ST = st;
    route();
  };
})();
