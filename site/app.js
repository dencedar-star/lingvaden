/* lingvaden.ru — проверка заданий, прогресс, озвучка аудиоскриптов */
(function () {
  "use strict";
  // Ученик, вошедший по ссылке, хранит ответы под своим номером: на общем устройстве прогресс не смешивается
  var WHO = null;
  try { WHO = JSON.parse(localStorage.getItem("en_who")); } catch (e) {}
  var LS = WHO && WHO.sid ? "en:s" + WHO.sid + ":" : "en:";
  // Режим разбора: преподаватель открыл страницу курса с ?review=<id ученика> — показываем ответы ученика, ничего не сохраняем
  var RV = /[?&]review=(\d+)/.exec(location.search);
  var REVIEW = RV ? +RV[1] : 0;
  if (REVIEW) LS = "en:review:";
  var BD = document.body.dataset, ROOT = BD.root || "/";
  var API = ROOT + "api/api.php?a=";

  /* ---------- журнал действий (только для вошедших учеников и преподавателей) ---------- */
  var EN = window.EN = {
    // 1 модуль, 2 модуля, 5 модулей
    plural: function (n, f) { var a = n % 10, b = n % 100; return n + " " + (a === 1 && b !== 11 ? f[0] : a >= 2 && a <= 4 && (b < 12 || b > 14) ? f[1] : f[2]); },
    role: WHO && WHO.sid ? "student" : null,
    ctx: { course: BD.course || "", unit: BD.unit || "", page: BD.page || "", path: location.pathname },
    q: [],
    log: function (e) {
      if (!EN.role) return;
      if (e.t === "write") EN.q = EN.q.filter(function (x) { return !(x.t === "write" && x.wid === e.wid); });
      EN.q.push(e);
      if (e.t !== "tick" && e.t !== "view") EN.flush();
    },
    flush: function (beacon) {
      var pend = [];
      try { pend = JSON.parse(localStorage.getItem("en_log")) || []; } catch (e) {}
      if (EN.q.length && EN.role) pend.push({ role: EN.role, ctx: EN.ctx, ev: EN.q.splice(0) });
      try { localStorage.removeItem("en_log"); } catch (e) {}
      pend.forEach(function (b) {
        var body = JSON.stringify({ role: b.role, course: b.ctx.course, unit: b.ctx.unit, page: b.ctx.page, path: b.ctx.path, ev: b.ev });
        if (beacon && navigator.sendBeacon && navigator.sendBeacon(API + "log", new Blob([body], { type: "text/plain" }))) return;
        var pr = fetch(API + "log", { method: "POST", credentials: "same-origin", keepalive: body.length < 60000,
          headers: { "Content-Type": "application/json" }, body: body })
          .then(function (r) { if (!r.ok && r.status >= 500) throw 0; })
          .catch(function () { EN.keep(b); })
          .then(function () { EN._fl = EN._fl.filter(function (x) { return x !== pr; }); });
        EN._fl.push(pr);
      });
      // обещание «всё отправленное дошло» — домашнюю работу сдаём только после этого
      return Promise.all(EN._fl.slice());
    },
    _fl: [],
    draft: function (ex, n, st, extra) {   // черновик ответа — через 1,5 с после последнего изменения
      if (EN.role !== "student") return;
      clearTimeout(EN._dt[ex]);
      EN._dt[ex] = setTimeout(function () {
        EN.q = EN.q.filter(function (x) { return !(x.t === "draft" && x.ex === ex); });
        var e = { t: "draft", ex: ex, n: n, st: st };
        Object.keys(extra || {}).forEach(function (k) { e[k] = extra[k]; });
        EN.log(e);
      }, 1500);
    },
    _dt: {},
    keep: function (b) {   // нет сети — событие подождёт следующей отправки
      try { var a = JSON.parse(localStorage.getItem("en_log")) || []; a.push(b); localStorage.setItem("en_log", JSON.stringify(a.slice(-50))); } catch (e) {}
    }
  };
  EN.lsGet = function (k) { return lsGet(k); }; EN.lsSet = function (k, v) { lsSet(k, v); };
  function lsGet(k) { try { return JSON.parse(localStorage.getItem(LS + k)); } catch (e) { return null; } }
  function lsSet(k, v) { if (REVIEW) return; try { localStorage.setItem(LS + k, JSON.stringify(v)); } catch (e) {} }
  function lsDel(k) { try { localStorage.removeItem(LS + k); } catch (e) {} }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ---------- тема ---------- */
  var tbtn = document.querySelector(".theme");
  function curTheme() {
    var t = document.documentElement.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function paintThemeBtn() { if (tbtn) tbtn.textContent = curTheme() === "dark" ? "☀" : "☾"; }
  if (tbtn) {
    paintThemeBtn();
    tbtn.addEventListener("click", function () {
      var t = curTheme() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", t);
      try { localStorage.setItem("en_theme", t); } catch (e) {}
      paintThemeBtn();
    });
  }

  /* ---------- сравнение ответов ---------- */
  var CONTR = [
    [/\bcan['’]t\b/g, "cannot"], [/\bwon['’]t\b/g, "will not"], [/n['’]t\b/g, " not"],
    [/['’]m\b/g, " am"], [/['’]re\b/g, " are"], [/['’]ve\b/g, " have"], [/['’]ll\b/g, " will"], [/['’]d\b/g, " had"]
  ];
  function norm(s) {
    s = String(s || "").toLowerCase().replace(/[‘’`]/g, "'").replace(/[–—]/g, "-");
    CONTR.forEach(function (c) { s = s.replace(c[0], c[1]); });
    return s.replace(/[.,!?;:"]/g, " ").replace(/\s+/g, " ").trim();
  }
  function alts(el) { return (el.getAttribute("data-a") || "").split("|"); }
  function matches(val, el) {
    var v = norm(val);
    if (!v) return false;
    return alts(el).some(function (a) { return norm(a) === v; });
  }

  /* ---------- типы заданий ---------- */
  // каждый «элемент» умеет: check() → true/false, show(), reset(), save()/load()
  function Gap(el) {
    return {
      el: el,
      check: function () { var r = matches(el.value, el); mark(el, r ? "ok" : "bad"); return r; },
      show: function () { el.value = alts(el)[0]; mark(el, "shown"); },
      reset: function () { el.value = ""; mark(el, null); },
      get: function () { return el.value; },
      set: function (v) { el.value = v || ""; },
      txt: function () { return el.value; }, exp: function () { return alts(el).join(" / "); }
    };
  }
  function Sel(el) {
    if (!el.options.length) {
      var o = document.createElement("option"); o.value = ""; o.textContent = "—"; el.appendChild(o);
      (el.getAttribute("data-opts") || "").split("|").forEach(function (t) {
        var op = document.createElement("option"); op.value = t; op.textContent = t; el.appendChild(op);
      });
    }
    return {
      el: el,
      check: function () { var r = el.value !== "" && alts(el).indexOf(el.value) >= 0; mark(el, r ? "ok" : "bad"); return r; },
      show: function () { el.value = alts(el)[0]; mark(el, "shown"); },
      reset: function () { el.value = ""; mark(el, null); },
      get: function () { return el.value; },
      set: function (v) { el.value = v || ""; },
      txt: function () { return el.value; }, exp: function () { return alts(el).join(" / "); }
    };
  }
  function Choice(el) {
    var bs = $$("button", el);
    bs.forEach(function (b) {
      b.type = "button";
      b.setAttribute("aria-pressed", "false");
      b.addEventListener("click", function () {
        bs.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); x.classList.remove("ok", "bad", "shown"); });
        persist(el);
      });
    });
    function picked() { for (var i = 0; i < bs.length; i++) if (bs[i].getAttribute("aria-pressed") === "true") return bs[i]; return null; }
    return {
      el: el,
      check: function () {
        var p = picked(); bs.forEach(function (x) { x.classList.remove("ok", "bad", "shown"); });
        if (!p) return false;
        var r = alts(el).indexOf(p.textContent.trim()) >= 0; p.classList.add(r ? "ok" : "bad"); return r;
      },
      show: function () {
        bs.forEach(function (x) {
          var r = alts(el).indexOf(x.textContent.trim()) >= 0;
          x.setAttribute("aria-pressed", r ? "true" : "false"); x.classList.remove("ok", "bad", "shown");
          if (r) x.classList.add("shown");
        });
      },
      reset: function () { bs.forEach(function (x) { x.setAttribute("aria-pressed", "false"); x.classList.remove("ok", "bad", "shown"); }); },
      get: function () { var p = picked(); return p ? p.textContent.trim() : ""; },
      set: function (v) { bs.forEach(function (x) { x.setAttribute("aria-pressed", x.textContent.trim() === v ? "true" : "false"); }); },
      txt: function () { var p = picked(); return p ? p.textContent.trim() : ""; }, exp: function () { return alts(el).join(" / "); }
    };
  }
  function Insert(el) {
    // слово вставляется кликом в промежуток между словами; data-a — номер промежутка
    var word = el.getAttribute("data-word");
    var slots = $$(".slot", el);
    slots.forEach(function (s) {
      s.setAttribute("role", "button"); s.tabIndex = 0;
      function pick() {
        slots.forEach(function (x) { x.classList.remove("picked", "ok", "bad", "shown"); x.textContent = ""; });
        s.classList.add("picked"); s.textContent = word; persist(el);
      }
      s.addEventListener("click", pick);
      s.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(); } });
    });
    function cur() { for (var i = 0; i < slots.length; i++) if (slots[i].textContent) return i; return -1; }
    return {
      el: el,
      check: function () {
        var i = cur(); if (i < 0) return false;
        var r = alts(el).indexOf(String(i)) >= 0;
        slots[i].classList.remove("picked"); slots[i].classList.add(r ? "ok" : "bad"); return r;
      },
      show: function () {
        var i = +alts(el)[0];
        slots.forEach(function (x) { x.classList.remove("picked", "ok", "bad", "shown"); x.textContent = ""; });
        slots[i].textContent = word; slots[i].classList.add("shown");
      },
      reset: function () { slots.forEach(function (x) { x.classList.remove("picked", "ok", "bad", "shown"); x.textContent = ""; }); },
      get: function () { return cur(); },
      set: function (v) { if (v >= 0 && slots[v]) { slots[v].textContent = word; slots[v].classList.add("picked"); } },
      txt: function () { var i = cur(); return i < 0 ? "" : sentence(i); }, exp: function () { return sentence(+alts(el)[0]); }
    };
    // предложение со словом в промежутке i — для журнала преподавателя
    function sentence(i) {
      var out = "";
      Array.prototype.forEach.call(el.childNodes, function (n) {
        if (n.nodeType === 1 && n.classList.contains("word-tag")) return;
        if (n.nodeType === 1 && n.classList.contains("slot")) { if (slots.indexOf(n) === i) out += word + " "; return; }
        out += n.textContent;
      });
      return out.replace(/\s+/g, " ").replace(/ ([.,?!;])/g, "$1").trim();
    }
  }
  function Order(el) {
    var line = el.querySelector(".line"), bank = el.querySelector(".bank");
    var words = el.getAttribute("data-words").split("|");
    var ans = el.querySelector(".ans");
    function build(state) {
      line.innerHTML = ""; bank.innerHTML = "";
      words.forEach(function (w, i) {
        var t = document.createElement("button"); t.type = "button"; t.className = "tile"; t.textContent = w; t.dataset.i = i;
        t.addEventListener("click", function () {
          (t.parentNode === bank ? line : bank).appendChild(t);
          el.classList.remove("ok", "bad", "shown"); ans.hidden = true; persist(el);
        });
        bank.appendChild(t);
      });
      (state || []).forEach(function (i) { var t = bank.querySelector('[data-i="' + i + '"]'); if (t) line.appendChild(t); });
    }
    build();
    function text() { return $$(".tile", line).map(function (t) { return t.textContent; }).join(" "); }
    return {
      el: el,
      check: function () {
        el.classList.remove("ok", "bad", "shown"); ans.hidden = true;
        var r = matches(text(), el); el.classList.add(r ? "ok" : "bad"); return r;
      },
      show: function () {
        // расставляем плитки в порядке слов правильного ответа
        var target = alts(el)[0].replace(/[?.!]/g, "").split(/\s+/), used = {}, idx = [];
        target.forEach(function (w) {
          for (var i = 0; i < words.length; i++) {
            if (!used[i] && words[i].toLowerCase() === w.toLowerCase()) { used[i] = 1; idx.push(i); break; }
          }
        });
        build(idx);
        el.classList.remove("ok", "bad"); el.classList.add("shown"); ans.hidden = false;
      },
      reset: function () { el.classList.remove("ok", "bad", "shown"); ans.hidden = true; build(); },
      get: function () { return $$(".tile", line).map(function (t) { return +t.dataset.i; }); },
      set: function (v) { build(v); },
      txt: function () { return text(); }, exp: function () { return alts(el)[0]; }
    };
  }
  function mark(el, cls) { el.classList.remove("ok", "bad", "shown"); if (cls) el.classList.add(cls); }

  /* ---------- упражнения ---------- */
  var registry = [];
  function persist(node) {
    var ex = node.closest && node.closest(".ex");
    if (ex && ex._save) ex._save();
  }
  // opt (домашняя работа): ns — префикс хранилища, u/p — модуль и страница задания, hw — номер работы, locked — уже отправлена
  var MAXFAILS = 3;
  function setupEx(ex, opt) {
    opt = opt || {};
    var id = ex.getAttribute("data-ex"), ns = opt.ns || "";
    var tag = function (e) { if (opt.u) { e.u = opt.u; e.p = opt.p; e.c = opt.c; } if (opt.hw) e.hw = opt.hw; return e; };
    var items = [];
    $$("input.gap", ex).forEach(function (e) { items.push(Gap(e)); });
    $$("select.sel", ex).forEach(function (e) { items.push(Sel(e)); });
    $$(".choice", ex).forEach(function (e) { items.push(Choice(e)); });
    $$(".ins-row", ex).forEach(function (e) { items.push(Insert(e)); });
    $$(".order", ex).forEach(function (e) { items.push(Order(e)); });
    if (!items.length) return;
    // порядок элементов — как в документе
    items.sort(function (a, b) { return a.el.compareDocumentPosition(b.el) & 4 ? -1 : 1; });

    var bar = document.createElement("div"); bar.className = "toolbar";
    bar.innerHTML = '<button type="button" class="btn" data-act="check">Проверить</button>' +
      '<button type="button" class="btn ghost" data-act="show">Показать ответы</button>' +
      '<button type="button" class="btn plain" data-act="reset">Сбросить</button>' +
      '<span class="score" hidden></span>';
    ex.appendChild(bar);
    var scoreEl = bar.querySelector(".score");

    function showScore(s, t, shown) {
      scoreEl.hidden = false;
      scoreEl.textContent = shown ? "Ответы показаны" : (s + " из " + t) + (lsGet(ns + "auto:" + id) ? " · верные ответы подставлены после " + MAXFAILS + " попыток" : "");
      scoreEl.classList.toggle("full", !shown && s === t);
      // сколько неверных попыток уже было: точки (после третьей ответ подставится сам)
      var tr = bar.querySelector(".tries"), f = lsGet(ns + "fails:" + id) || 0;
      if (!tr) { tr = document.createElement("span"); tr.className = "tries"; bar.appendChild(tr); }
      var showTr = !shown && !REVIEW && s < t && f > 0 && !lsGet(ns + "auto:" + id) && !opt.locked;
      tr.hidden = !showTr;
      if (showTr) {
        var dots = ""; for (var k = 0; k < MAXFAILS; k++) dots += '<i class="' + (k < f ? "used" : "") + '"></i>';
        tr.innerHTML = dots + "<span>попытка " + f + " из " + MAXFAILS + (MAXFAILS - f === 1 ? " — дальше ответ подставится" : "") + "</span>";
        tr.title = "Неверных попыток: " + f + ". После " + MAXFAILS + "-й правильный ответ подставится сам.";
      }
    }
    // после трёх проверок с ошибками — правильный вариант вставляется сам, задание закрывается
    function lock(on) {
      ex.classList.toggle("ex-locked", !!on);
      $$("input.gap, select.sel, .choice button, .slot, .tile", ex).forEach(function (x) { x.disabled = !!on; if (x.classList.contains("slot") || x.classList.contains("tile")) x.style.pointerEvents = on ? "none" : ""; });
      $$("[data-act=check], [data-act=show]", bar).forEach(function (b) { b.hidden = !!on; });
      var rs = bar.querySelector("[data-act=reset]"); if (rs) rs.hidden = !!on && !!opt.hw;
    }
    function state() { return items.map(function (it) { return it.get(); }); }
    function check(quiet) {
      if (ex.classList.contains("ex-locked")) return lsGet(ns + "score:" + id) ? lsGet(ns + "score:" + id).s : 0;
      var s = 0, res = [], oks = [];
      items.forEach(function (it) {
        var ok = it.check(); if (ok) s++; oks.push(ok);
        res.push({ v: String(it.txt()), ok: ok, e: ok ? "" : String(it.exp()) });
      });
      // проверено — черновик этого задания больше не нужен
      clearTimeout(EN._dt[id]); EN.q = EN.q.filter(function (x) { return !(x.t === "draft" && x.ex === id); });
      var entered = res.some(function (r) { return r.v !== ""; });
      ex._lastSt = JSON.stringify(state());
      var prev = lsGet(ns + "score:" + id) || {};
      lsSet(ns + "score:" + id, { s: s, t: items.length, best: Math.max(s, prev.best || 0) });
      // в журнал — только если ученик что-то ввёл (пустую проверку «Проверить всё» не пишем)
      if (entered) EN.log(tag({ t: "check", ex: id, s: s, n: items.length, items: res, st: state() }));
      if (entered && s < items.length) {
        var fails = (lsGet(ns + "fails:" + id) || 0) + 1;
        lsSet(ns + "fails:" + id, fails);
        if (fails >= MAXFAILS) {
          items.forEach(function (it, i) { if (!oks[i]) it.show(); });
          lsSet(ns + "auto:" + id, 1); lsSet(ns + "ans:" + id, state());
          EN.log(tag({ t: "show", ex: id, n: items.length, st: state(), auto: 1 }));
          lock(true);
        }
      }
      showScore(s, items.length);
      refreshTotals();
      if (opt.onCheck) opt.onCheck();
      return s;
    }
    ex._save = function () { lsSet(ns + "ans:" + id, state()); EN.draft(id, items.length, state(), tag({})); };
    // разбор: показать заданное состояние (попытку ученика) и отметить верное/неверное, без записи и журнала
    ex._apply = function (st) {
      items.forEach(function (it) { it.reset(); });
      if (!st || st.length !== items.length) { scoreEl.hidden = true; return; }
      items.forEach(function (it, i) { it.set(st[i]); });
      var s = 0; items.forEach(function (it) { if (it.check()) s++; });
      showScore(s, items.length);
    };
    ex._load = function () {
      var saved = lsGet(ns + "ans:" + id);
      if (saved && saved.length === items.length) items.forEach(function (it, i) { it.set(saved[i]); });
      var sc = lsGet(ns + "score:" + id);
      if (sc) { showScore(sc.s, sc.t); ex._lastSt = JSON.stringify(state()); }
      if (lsGet(ns + "auto:" + id)) { items.forEach(function (it) { it.check(); }); lock(true); }
      if (opt.locked) lock(true);
    };
    ex._load();

    $$("input.gap", ex).forEach(function (e) {
      e.addEventListener("input", function () { mark(e, null); ex._save(); });
      e.addEventListener("keydown", function (k) { if (k.key === "Enter") { k.preventDefault(); check(); } });
    });
    $$("select.sel", ex).forEach(function (e) { e.addEventListener("change", function () { mark(e, null); ex._save(); }); });

    bar.addEventListener("click", function (e) {
      var a = e.target.getAttribute && e.target.getAttribute("data-act");
      if (a === "check") check();
      if (a === "show") { items.forEach(function (it) { it.show(); }); showScore(0, 0, true); ex._save(); EN.log(tag({ t: "show", ex: id, n: items.length, st: state() })); }
      if (a === "reset") {
        items.forEach(function (it) { it.reset(); }); scoreEl.hidden = true; lock(false);
        ["ans:", "score:", "fails:", "auto:"].forEach(function (k) { lsDel(ns + k + id); });
        refreshTotals(); EN.log(tag({ t: "reset", ex: id }));
      }
    });
    var reg = { id: id, total: items.length, check: check, ex: ex, load: ex._load, apply: ex._apply, state: state,
      showAll: function () { items.forEach(function (it) { it.reset(); it.show(); }); scoreEl.hidden = true; },
      // есть введённые, но ещё не проверенные ответы (перед отправкой учителю проверяются сами)
      dirty: function () { return !ex.classList.contains("ex-locked") && JSON.stringify(state()) !== ex._lastSt && items.some(function (it) { return String(it.txt()) !== ""; }); },
      score: function () { return lsGet(ns + "score:" + id); } };
    if (!opt.hw) registry.push(reg);
    return reg;
  }
  EN.setupEx = setupEx;
  $$(".ex[data-ex]").forEach(setupEx);

  /* ---------- прогресс ---------- */
  function sumScores(ids) {
    var s = 0, t = 0, done = 0;
    ids.forEach(function (x) {
      var id = x[0], n = x[1], sc = lsGet("score:" + id);
      t += n; if (sc) { s += sc.best || sc.s; done++; }
    });
    return { s: s, t: t, done: done, n: ids.length };
  }
  function refreshTotals() {
    $$("[data-progress]").forEach(function (box) {
      var ids = JSON.parse(box.getAttribute("data-progress"));
      var r = sumScores(ids);
      var pct = r.t ? Math.round(100 * r.s / r.t) : 0;
      var bar = box.querySelector(".bar i"); if (bar) bar.style.width = pct + "%";
      var lab = box.querySelector(".bar-l");
      if (lab) lab.textContent = r.done ? ("Выполнено заданий: " + r.done + " из " + r.n + " · верно " + r.s + " из " + r.t) : ("Заданий: " + r.n + " · ещё не начато");
    });
  }
  refreshTotals();
  var allBtn = document.querySelector("[data-check-all]");
  if (allBtn) allBtn.addEventListener("click", function () {
    registry.forEach(function (r) { r.check(); });
    var first = document.querySelector(".ex .bad");
    if (first) first.scrollIntoView({ behavior: "smooth", block: "center" });
  });

  /* ---------- писательское поле ---------- */
  var writers = [];
  $$(".writer").forEach(function (w) {
    var wid = w.getAttribute("data-id");
    var ta = w.querySelector("textarea"), c = w.querySelector(".cnt"), key = "write:" + wid;
    var t = w.getAttribute("data-target"), hint = t === null ? " (нужно около 150)" : (t ? " (нужно около " + t + ")" : "");
    function count() { if (!c) return; var n = (ta.value.match(/[A-Za-z0-9’']+/g) || []).length; c.textContent = "Слов: " + n + hint; }
    var timer = null, sent = ta.value;
    function push() { clearTimeout(timer); if (ta.value !== sent) { sent = ta.value; EN.log({ t: "write", wid: wid, text: ta.value }); } }
    w._load = function () { ta.value = lsGet(key) || ""; sent = ta.value; count(); };
    w._set = function (text) { ta.value = text || ""; count(); };
    w._load();
    ta.addEventListener("input", function () { lsSet(key, ta.value); count(); clearTimeout(timer); timer = setTimeout(push, 8000); });
    ta.addEventListener("blur", push);
    writers.push(w);
  });

  /* ---------- голосовой ответ (только в курсах, где сервер разрешает запись): ученик записывает, учитель слушает ---------- */
  var voices = [];
  function mmss(t) { t = Math.round(t); return Math.floor(t / 60) + ":" + ("0" + t % 60).slice(-2); }
  $$(".voice").forEach(function (v) {
    var wid = v.getAttribute("data-id"), max = +v.getAttribute("data-max") || 180;
    v.innerHTML = '<div class="vc-row"><button type="button" class="btn sm vc-rec" hidden>🎙 Записать ответ</button>' +
      '<button type="button" class="btn sm danger-o vc-stop" hidden>■ Стоп</button><span class="vc-time" hidden></span>' +
      '<span class="vc-msg"></span></div><div class="vc-play" hidden><audio controls preload="none"></audio></div>';
    var rec = v.querySelector(".vc-rec"), stop = v.querySelector(".vc-stop"), time = v.querySelector(".vc-time"),
      msg = v.querySelector(".vc-msg"), play = v.querySelector(".vc-play"), audio = play.querySelector("audio");
    function show(x) {   // x — {id, sec, at} с сервера или null
      play.hidden = !x;
      if (x) audio.src = API + "voice&id=" + x.id + "&v=" + encodeURIComponent(x.at || "");
      v.classList.toggle("rv-none", !x);
      return x;
    }
    v._show = function (x) { if (!x || audio.src.indexOf("id=" + x.id + "&") < 0 || audio.src.indexOf(encodeURIComponent(x.at || "")) < 0) show(x); };
    v._teacher = function (text) { rec.hidden = true; msg.textContent = text; };
    v._student = function (x) {
      rec.hidden = false; msg.textContent = "";
      if (show(x)) rec.textContent = "🎙 Перезаписать";
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder) {
        rec.disabled = true; msg.textContent = "Этот браузер не умеет записывать звук — откройте страницу в Chrome, Safari или Firefox.";
      }
    };
    var mr = null, chunks = [], t0 = 0, tick = null, stream = null;
    function finish() {
      clearInterval(tick); stop.hidden = true; time.hidden = true; rec.hidden = false; v.classList.remove("vc-on");
      if (stream) stream.getTracks().forEach(function (t) { t.stop(); });
    }
    rec.addEventListener("click", function () {
      if (play.hidden === false && !confirm("Записать заново? Прежняя запись заменится.")) return;
      msg.textContent = "";
      navigator.mediaDevices.getUserMedia({ audio: true }).then(function (st) {
        stream = st; chunks = [];
        var type = ["audio/webm;codecs=opus", "audio/mp4", "audio/ogg;codecs=opus", "audio/webm"].filter(function (t) { return MediaRecorder.isTypeSupported && MediaRecorder.isTypeSupported(t); })[0];
        mr = type ? new MediaRecorder(st, { mimeType: type, audioBitsPerSecond: 48000 }) : new MediaRecorder(st);
        mr.ondataavailable = function (e) { if (e.data && e.data.size) chunks.push(e.data); };
        mr.onstop = function () {
          var sec = Math.max(1, Math.round((Date.now() - t0) / 1000)), mime = (mr.mimeType || type || "audio/webm").split(";")[0];
          finish();
          var blob = new Blob(chunks, { type: mime });
          msg.textContent = "Отправляю…"; rec.disabled = true;
          fetch(API + "s_voice&course=" + encodeURIComponent(BD.course || "") + "&unit=" + encodeURIComponent(BD.unit || "") + "&wid=" + encodeURIComponent(wid) +
            "&sec=" + sec + "&path=" + encodeURIComponent(location.pathname), { method: "POST", credentials: "same-origin", headers: { "Content-Type": mime }, body: blob })
            .then(function (r) { return r.json(); })
            .then(function (d) {
              rec.disabled = false;
              if (!d.ok) { msg.textContent = d.error === "voice" ? "Запись в этом курсе недоступна." : "Не получилось сохранить запись. Попробуйте ещё раз."; return; }
              show(d); rec.textContent = "🎙 Перезаписать"; msg.textContent = "✓ Сохранено — преподаватель услышит ваш ответ";
            }, function () { rec.disabled = false; msg.textContent = "Нет связи с сервером — запись не сохранилась. Попробуйте ещё раз."; });
        };
        mr.start(1000); t0 = Date.now();
        rec.hidden = true; stop.hidden = false; time.hidden = false; v.classList.add("vc-on");
        time.textContent = "0:00 / " + mmss(max);
        tick = setInterval(function () {
          var s = (Date.now() - t0) / 1000; time.textContent = mmss(s) + " / " + mmss(max);
          if (s >= max && mr.state === "recording") mr.stop();
        }, 250);
      }, function () { msg.textContent = "Нет доступа к микрофону. Разрешите его в настройках браузера для lingvaden.ru и попробуйте снова."; });
    });
    stop.addEventListener("click", function () { if (mr && mr.state === "recording") mr.stop(); });
    voices.push(v);
  });

  var synth = window.speechSynthesis;
  // кнопка 🔊 у слова: произносит синтезатор речи браузера (американский английский)
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-say]");
    if (!b || !synth) return;
    var u = new SpeechSynthesisUtterance(b.getAttribute("data-say"));
    u.lang = "en-US"; u.rate = 0.9;
    synth.cancel(); synth.speak(u);
  });
  /* ---------- аудио и видео курса: одна запись за раз, переход к части, журнал прослушиваний ---------- */
  document.addEventListener("play", function (e) {
    var m = e.target;
    if (!m || !/^(AUDIO|VIDEO)$/.test(m.tagName)) return;
    $$("audio, video").forEach(function (x) { if (x !== m && !x.paused) x.pause(); });
    if (synth) synth.cancel();
    if (!m._logged) {
      m._logged = 1;
      var lab = m.parentNode.querySelector(".aud-l, figcaption b");
      EN.log({ t: "audio", what: lab ? lab.textContent.replace(/[♪▶]/g, "").trim() : m.getAttribute("src") });
    }
  }, true);
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".aud-parts [data-t]");
    if (!b) return;
    var a = b.closest(".aud").querySelector("audio"), t = +b.getAttribute("data-t");
    function go() { a.currentTime = t; a.play(); }
    if (a.readyState >= 1) go(); else { a.preload = "auto"; a.addEventListener("loadedmetadata", go, { once: true }); a.load(); }
  });

  /* ---------- озвучка аудиоскриптов синтезатором речи ---------- */
  $$(".script").forEach(function (sc) {
    var box = sc.querySelector(".tts");
    if (!box) return;
    if (!synth || !window.SpeechSynthesisUtterance) { box.hidden = true; return; }
    var play = box.querySelector("[data-play]"), stop = box.querySelector("[data-stop]");
    function voices() {
      var v = synth.getVoices().filter(function (x) { return /^en[-_]GB/i.test(x.lang); });
      if (!v.length) v = synth.getVoices().filter(function (x) { return /^en/i.test(x.lang); });
      return v;
    }
    function clear() { $$(".line", sc).forEach(function (l) { l.classList.remove("speaking"); }); }
    play.addEventListener("click", function () {
      synth.cancel(); clear();
      var sm = sc.querySelector("summary"); EN.log({ t: "audio", what: sm ? sm.textContent.replace(/\s+/g, " ").trim() : "" });
      var vs = voices(), map = {}, k = 0;
      var lines = $$(".line", sc);
      lines.forEach(function (l, i) {
        var sp = l.getAttribute("data-sp") || "";
        if (!(sp in map)) map[sp] = vs.length ? vs[(k++) % vs.length] : null;
        var u = new SpeechSynthesisUtterance(l.querySelector("span").textContent);
        u.lang = "en-GB"; if (map[sp]) u.voice = map[sp]; u.rate = 0.95;
        u.onstart = function () { clear(); l.classList.add("speaking"); };
        if (i === lines.length - 1) u.onend = clear;
        synth.speak(u);
      });
    });
    stop.addEventListener("click", function () { synth.cancel(); clear(); });
  });
  /* =================== платформа: вход по коду, меню слева, профиль, согласия =================== */
  function el(tag, cls, html) { var x = document.createElement(tag); if (cls) x.className = cls; if (html != null) x.innerHTML = html; return x; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function post(a, data) {
    return fetch(API + a, { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data || {}) }).then(function (r) { return r.json().catch(function () { return { ok: false, error: "net" }; }); });
  }
  EN.post = post; EN.esc = esc; EN.el = el; EN.api = API; EN.root = ROOT;
  // версия сборки (из адреса app.js) — для данных, которые меняются с каждой выкладкой
  EN.ver = ((document.querySelector('script[src*="app.js?v="]') || {}).src || "").split("v=")[1] || String(Date.now());

  // учёт времени: каждые 15 с, если вкладка открыта и с последнего действия прошло меньше минуты
  var lastAct = Date.now(), pendSec = 0;
  ["pointerdown", "keydown", "scroll", "touchstart", "mousemove"].forEach(function (t) {
    addEventListener(t, function () { lastAct = Date.now(); }, { passive: true });
  });
  setInterval(function () {
    if (!EN.role || document.visibilityState !== "visible" || Date.now() - lastAct > 60000) return;
    pendSec += 15;
    if (pendSec >= 60) { EN.log({ t: "tick", sec: pendSec }); pendSec = 0; EN.flush(); }
  }, 15000);
  // где ученик сейчас: задание, с которым он работает, и «я здесь» раз в 30 с — для разбора с преподавателем онлайн
  var lastFocus = "";
  ["focusin", "pointerdown"].forEach(function (t) {
    document.addEventListener(t, function (e) {
      var x = e.target.closest && e.target.closest(".ex[data-ex]");
      if (x && x.id !== lastFocus) { lastFocus = x.id; EN.log({ t: "focus", ex: x.id }); }
    }, true);
  });
  setInterval(function () { if (EN.role === "student" && document.visibilityState === "visible") EN.log({ t: "focus" }); }, 30000);
  function leave() { if (pendSec) { EN.log({ t: "tick", sec: pendSec }); pendSec = 0; } EN.flush(true); }
  addEventListener("pagehide", leave);
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") leave(); });
  // раскрытые ключи и ответы
  $$("details.reveal").forEach(function (d) {
    d.addEventListener("toggle", function () {
      if (!d.open) return;
      var ex = d.closest(".ex");
      EN.log({ t: "reveal", ex: ex ? ex.getAttribute("data-ex") : "", what: (d.querySelector("summary") || {}).textContent || "" });
    });
  });

  /* ---------- согласия при первом входе ---------- */
  var DOCS = {
    terms: ["Пользовательское соглашение", "legal/terms.html"], cookies: ["Cookies и хранилище", "legal/cookies.html"],
    privacy: ["Политика обработки персональных данных", "legal/privacy.html"],
    student_consent: ["Согласие ученика на обработку данных", "legal/student-consent.html"],
    teacher_terms: ["Условия для преподавателей", "legal/teachers.html"]
  };
  function link(d) { return '<a href="' + ROOT + DOCS[d][1] + '" target="_blank" rel="noopener">' + DOCS[d][0] + "</a>"; }
  function logout() {
    EN.flush();
    post("logout", {}).then(function () {
      try { localStorage.removeItem("en_who"); localStorage.removeItem("en_tw"); } catch (e) {}
      location.href = ROOT;
    });
  }
  EN.logout = logout;
  EN.consent = function (role, missing, name, done) {
    var m = el("div", "modal");
    var box = el("form", "modal-box consent");
    var h = role === "student"
      ? "<h2>Здравствуйте, " + esc(name) + "!</h2><p>Перед началом — один раз. Платформа сохраняет ваши ответы, попытки, домашние работы, входы и " +
        "время занятий, чтобы ваш преподаватель видел прогресс. Данные хранятся в России и никому больше не передаются.</p>" +
        '<label class="chk"><input type="checkbox" name="a" required> <span>Я принимаю ' + link("terms") + " и " + link("cookies") + "</span></label>" +
        '<label class="chk"><input type="checkbox" name="b" required> <span>Я даю ' + link("student_consent") + " на условиях — " + link("privacy") + "</span></label>" +
        '<fieldset><legend>Кто даёт согласие</legend><label class="chk"><input type="radio" name="age" value="14plus" required> <span>Мне 14 лет или больше — даю сам(а)</span></label>' +
        '<label class="chk"><input type="radio" name="age" value="parent"> <span>Мне меньше 14 — согласие даёт мой родитель (законный представитель), он рядом</span></label>' +
        '<label class="parent" hidden>Имя родителя (необязательно)<input name="parent" maxlength="120" autocomplete="off"></label></fieldset>'
      : "<h2>Добро пожаловать, " + esc(name) + "!</h2><p>Перед работой в кабинете примите условия. Это нужно один раз " +
        "(и снова — только если документы изменятся).</p>" +
        '<label class="chk"><input type="checkbox" name="a" required> <span>Я принимаю ' + link("terms") + " и " + link("cookies") + "</span></label>" +
        '<label class="chk"><input type="checkbox" name="b" required> <span>Я согласен(на) на обработку моих данных (ФИО, e-mail, Telegram, фото профиля, журнал работы) по ' + link("privacy") + "</span></label>" +
        '<label class="chk"><input type="checkbox" name="c" required> <span>Я принимаю ' + link("teacher_terms") + " и вношу данные учеников только с их " +
        "согласия (или согласия родителей); знаю, что <b>можно указать просто имя ученика</b></span></label>";
    box.innerHTML = h + '<div class="err" hidden></div><div class="modal-btns"><button class="btn" type="submit">Продолжить</button>' +
      '<button class="btn plain" type="button" data-out>Не согласен(на) — выйти</button></div>';
    m.appendChild(box); document.body.appendChild(m); document.body.classList.add("modal-open");
    $$('input[name="age"]', box).forEach(function (r) {
      r.addEventListener("change", function () { box.querySelector(".parent").hidden = box.age.value !== "parent"; });
    });
    box.querySelector("[data-out]").addEventListener("click", logout);
    box.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = { role: role, docs: missing };
      if (role === "student") { data.age = box.age.value; data.parent = box.parent ? box.parent.value : ""; }
      post("consent", data).then(function (r) {
        if (!r.ok) { var er = box.querySelector(".err"); er.hidden = false; er.textContent = "Не получилось сохранить — проверьте отметки и связь."; return; }
        m.remove(); document.body.classList.remove("modal-open"); if (done) done();
      });
    });
  };

  /* ---------- шапка (имя → профиль, выйти) и меню слева: у каждой роли своё ---------- */
  function initials(n) { return String(n || "?").trim().split(/\s+/).slice(0, 2).map(function (x) { return x.charAt(0); }).join("").toUpperCase(); }
  EN.initials = initials;
  EN.avatar = function (name, url, cls) {
    return '<span class="av' + (cls ? " " + cls : "") + '">' + (url ? '<img src="' + esc(url) + '" alt="">' : esc(initials(name))) + "</span>";
  };
  var ME = null;   // {role, user}
  var MENU = {
    teacher: [["students", "users", "Ученики"], ["spaces", "layers", "Классы"], ["courses", "book", "Курсы"], ["tasks", "list", "Задания"], ["homework", "bell", "Домашние работы"]],
    student: [["courses", "book", "Курсы"], ["homework", "list", "Домашние работы"], ["results", "chart", "Мои результаты"]]
  };
  // линейные значки (24×24, цвет — от текста)
  var ICON = {
    users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    layers: '<path d="m12 2 10 5-10 5L2 7l10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    book: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5v15z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
    list: '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 8h7M9 12h7M9 16h4"/><path d="M6.5 8h.01M6.5 12h.01M6.5 16h.01"/>',
    bell: '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    chart: '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
    edit: '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"/>',
    trash: '<path d="M3 6h18"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6M14 11v6"/>'
  };
  EN.icon = function (k) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (ICON[k] || "") + "</svg>"; };
  function home(role) { return ROOT + (role === "teacher" ? "teacher/" : "me/"); }
  EN.home = home;
  function paintWho(role, u) {
    var w = document.getElementById("who");
    if (!w) return;
    if (!u) { w.innerHTML = ""; w.hidden = true; return; }
    var sub = role === "teacher" ? "преподаватель" : "ученик" + (u.teacher ? " · " + u.teacher : "");
    w.innerHTML = '<details class="who-menu"><summary class="who-chip">' + EN.avatar(u.name, u.avatar) +
      '<span class="who-name">' + esc(String(u.name).split(" ")[0]) + '</span></summary><div class="who-drop"><b>' + esc(u.name) + "</b><small>" + esc(sub) + "</small>" +
      '<a href="' + home(role) + '#profile">Профиль</a><button type="button" data-out>Выйти</button></div></details>';
    w.hidden = false;
    w.querySelector("[data-out]").addEventListener("click", logout);
    // закрыть меню по клику вне его
    document.addEventListener("click", function (e) { var d = w.querySelector("details"); if (d && d.open && !d.contains(e.target)) d.open = false; });
  }
  function paintSide(role, u) {
    var side = document.getElementById("side");
    if (!side) return;
    if (!u || REVIEW && role !== "teacher") { side.hidden = true; document.body.classList.remove("with-side"); return; }
    var here = location.pathname === home(role).replace(/^\.\.\//, "/") || location.pathname.replace(/index\.html$/, "") === new URL(home(role), location.href).pathname;
    var cur = here ? (location.hash.replace("#", "").split(/[=&]/)[0] || MENU[role][0][0]) : (BD.unit ? "courses" : "");
    if (here && /^s$/.test(cur)) cur = "students";
    if (here && /^hw$/.test(cur)) cur = role === "teacher" ? "homework" : "homework";
    side.innerHTML = '<nav class="side-nav">' + MENU[role].map(function (m) {
      var badge = m[0] === "homework" ? '<span class="badge" data-badge hidden></span>' : "";
      return '<a href="' + home(role) + "#" + m[0] + '" data-m="' + m[0] + '"' + (m[0] === cur ? ' class="on"' : "") + '><span class="ic">' + EN.icon(m[1]) + "</span>" + m[2] + badge + "</a>";
    }).join("") + "</nav>";
    side.hidden = false; document.body.classList.add("with-side");
    setBadge(role === "teacher" ? u.hw_new : u.hw_open, role);
  }
  function setBadge(n, role) {
    var b = document.querySelector("#side [data-badge]");
    if (!b) return;
    b.hidden = !n; b.textContent = n || "";
    b.title = role === "teacher" ? "Новые сданные работы" : "Невыполненные домашние работы";
    var a = b.closest("a"); if (a) a.classList.toggle("ring", role === "teacher" && n > 0);
  }
  EN.setBadge = setBadge;
  EN.markSide = function (m) { $$("#side a").forEach(function (a) { a.classList.toggle("on", a.getAttribute("data-m") === m); }); };
  // сразу, до ответа сервера: из запомненного на этом устройстве (без мигания)
  (function () {
    var tw = null; try { tw = JSON.parse(localStorage.getItem("en_tw")); } catch (e) {}
    if (tw) { paintWho("teacher", tw); paintSide("teacher", tw); }
    else if (WHO && WHO.sid) { var u = { name: WHO.name, teacher: WHO.teacher, avatar: WHO.avatar }; paintWho("student", u); paintSide("student", u); }
  })();

  /* ---------- профиль: фото, ФИО, e-mail, Telegram ---------- */
  EN.profile = function (box, role, u, onSaved) {
    var code = role === "student" && u.code ? '<p class="note-s">Ваш код для входа: <b class="code">' + esc(u.code) + "</b> — вводится на главной странице. Не сообщайте его другим.</p>" : "";
    box.innerHTML = '<section class="page profile"><h2>Профиль</h2><div class="pf-grid"><div class="pf-photo">' + EN.avatar(u.name, u.avatar, "xl") +
      '<label class="btn ghost sm">Загрузить фото<input type="file" accept="image/*" hidden data-photo></label>' +
      (u.avatar ? '<button class="btn plain sm" type="button" data-nophoto>Убрать фото</button>' : "") + "</div>" +
      '<form class="stack" data-pf autocomplete="off"><label>Полное ФИО<input name="name" maxlength="200" required value="' + esc(u.name) + '"></label>' +
      '<label>E-mail<input name="email" type="email" maxlength="190" value="' + esc(u.email || "") + '" placeholder="name@example.ru"></label>' +
      '<label>Telegram<input name="telegram" maxlength="64" value="' + esc(u.telegram || "") + '" placeholder="@username или номер телефона"></label>' +
      '<div class="err" hidden></div><div class="row-btns"><button class="btn" type="submit">Сохранить</button>' +
      '<button class="btn plain" type="button" data-logout>Выйти</button></div></form></div>' + code +
      (role === "teacher" ? '<p class="note-s">Код входа выдаёт администрация; сменить его можно, написав на <a href="mailto:info@lingvaden.ru">info@lingvaden.ru</a>.</p>' :
        '<p class="note-s">Фото, e-mail и Telegram видит только ваш преподаватель.</p>') + "</section>";
    var f = box.querySelector("[data-pf]"), er = f.querySelector(".err");
    var ERR = { name: "Укажите ФИО.", email: "E-mail указан с ошибкой.", telegram: "Telegram: укажите @имя (4–32 латинских символа) или номер телефона.",
      image: "Не подошло фото — выберите JPG или PNG.", net: "Нет связи с сервером." };
    function fail(r) { er.hidden = false; er.textContent = ERR[r.error] || "Не получилось сохранить."; }
    f.addEventListener("submit", function (e) {
      e.preventDefault(); er.hidden = true;
      post("profile", { name: f.name.value, email: f.email.value, telegram: f.telegram.value }).then(function (r) {
        if (!r.ok) return fail(r);
        u.name = f.name.value.trim(); u.email = f.email.value.trim(); EN.toast("Сохранено"); if (onSaved) onSaved();
      });
    });
    f.querySelector("[data-logout]").addEventListener("click", logout);
    box.querySelector("[data-photo]").addEventListener("change", function (e) {
      var file = e.target.files[0]; if (!file) return;
      var img = new Image(), url = URL.createObjectURL(file);
      img.onload = function () {
        // квадрат 320×320 по центру, JPEG — фото получается лёгким (≈20–40 КБ)
        var c = document.createElement("canvas"), S = 320, k = Math.min(img.width, img.height);
        c.width = c.height = S;
        c.getContext("2d").drawImage(img, (img.width - k) / 2, (img.height - k) / 2, k, k, 0, 0, S, S);
        URL.revokeObjectURL(url);
        post("avatar_set", { data: c.toDataURL("image/jpeg", 0.85) }).then(function (r) {
          if (!r.ok) return fail(r);
          u.avatar = r.avatar; EN.toast("Фото обновлено"); if (onSaved) onSaved();
        });
      };
      img.onerror = function () { fail({ error: "image" }); };
      img.src = url;
    });
    var np = box.querySelector("[data-nophoto]");
    if (np) np.addEventListener("click", function () { post("avatar_del", {}).then(function (r) { if (r.ok) { u.avatar = null; if (onSaved) onSaved(); } }); });
  };
  EN.toast = function (msg, bad) {
    $$(".toast").forEach(function (x) { x.remove(); });   // одно сообщение за раз
    var t = el("div", "toast" + (bad ? " bad" : ""), esc(msg));
    document.body.appendChild(t); setTimeout(function () { t.classList.add("on"); }, 10);
    setTimeout(function () { t.classList.remove("on"); setTimeout(function () { t.remove(); }, 300); }, 2600);
  };

  function hello(st) {
    var box = document.getElementById("hello");
    if (!box) return;
    var last = lsGet("last");
    box.innerHTML = '<div class="hello-in"><div><h2>Здравствуйте, ' + esc(st.name) + "! 👋</h2><p>Вы вошли как ученик преподавателя <b>" +
      esc(st.teacher) + "</b>. Ответы и прогресс сохраняются автоматически — продолжить можно с любого устройства.</p></div>" +
      '<div class="hello-btns">' + (last ? '<a class="btn" href="' + esc(last.path) + '">Продолжить: ' + esc(last.title) + "</a>" : "") +
      '<button class="btn plain" type="button" data-x>Скрыть</button></div></div>';
    box.hidden = false;
    box.querySelector("[data-x]").addEventListener("click", function () { box.hidden = true; });
  }

  /* ---------- состояние ученика с сервера: прогресс на любом устройстве ---------- */
  function mergeState(state) {
    if (!state) return;
    var changed = false;
    Object.keys(state.p || {}).forEach(function (ex) {
      var p = state.p[ex], loc = lsGet("score:" + ex);
      if (p.t && (!loc || (p.best || 0) > (loc.best || 0))) {
        lsSet("score:" + ex, { s: loc ? loc.s : p.s, t: p.t, best: Math.max(p.best || 0, loc ? loc.best || 0 : 0) }); changed = true;
      }
      if (p.st && !lsGet("ans:" + ex)) { lsSet("ans:" + ex, p.st); changed = true; }
    });
    Object.keys(state.w || {}).forEach(function (wid) {
      if (!lsGet("write:" + wid) && state.w[wid]) { lsSet("write:" + wid, state.w[wid]); changed = true; }
    });
    if (changed) {
      registry.forEach(function (r) { r.load(); });
      writers.forEach(function (w) { w._load(); });
      refreshTotals();
    }
  }

  var PAGE = BD.app || (BD.unit ? "course" : "");   // home | teacher | student | course | info
  function onMe(d) {
    var st = d.student, tc = d.teacher;
    try { if (tc) localStorage.setItem("en_tw", JSON.stringify({ name: tc.name, avatar: tc.avatar })); else localStorage.removeItem("en_tw"); } catch (e) {}
    var role = tc ? "teacher" : st ? "student" : null, u = tc || st;
    ME = role ? { role: role, user: u } : null; EN.me = ME;
    var next = (/[?&]next=([^&#]+)/.exec(location.search) || [])[1];
    // без входа — только главная с вводом кода (и открытые страницы: как это работает, правовая информация)
    if (!role) {
      if (WHO && WHO.sid) { try { localStorage.removeItem("en_who"); } catch (e) {} }
      WHO = null; EN.role = null; paintWho(null, null); paintSide(null, null);
      if (PAGE === "teacher" || PAGE === "student" || PAGE === "course") { location.replace(ROOT + "?next=" + encodeURIComponent(location.pathname + location.search + location.hash)); return; }
      cookieBar();
      return;
    }
    // вошедший на главной — сразу в свой кабинет
    if (PAGE === "home") { location.replace(next && /^\/[a-z0-9\/._-]*$/i.test(decodeURIComponent(next)) ? decodeURIComponent(next) : home(role)); return; }
    if (PAGE === "teacher" && role !== "teacher") { location.replace(home(role) + location.hash); return; }
    if (PAGE === "student" && role !== "student") { location.replace(home(role) + location.hash); return; }
    paintWho(role, u);
    paintSide(role, u);
    if (REVIEW) {   // режим разбора: только для преподавателя этого ученика
      EN.role = null;
      if (tc) startReview(tc); else location.href = home(role);
      return;
    }
    if (role === "teacher") {
      EN.role = "teacher"; EN.ctx.path = location.pathname;
      voices.forEach(function (v) { v._teacher("Здесь ученик записывает ответ голосом. Послушать — в разборе ученика."); });
      var go = function () {
        if (!document.getElementById("t-app")) EN.log({ t: "view", title: document.title });
        if (window.EN_TEACHER) window.EN_TEACHER(d);
      };
      if (tc.consent && tc.consent.length) EN.consent("teacher", tc.consent, tc.name, go); else go();
      // колокольчик: новые сданные работы — раз в минуту
      setInterval(function () {
        if (document.visibilityState !== "visible") return;
        fetch(API + "me", { credentials: "same-origin", cache: "no-store" }).then(function (r) { return r.json(); })
          .then(function (x) { if (x.teacher) { setBadge(x.teacher.hw_new, "teacher"); if (window.EN_BELL) window.EN_BELL(x.teacher.hw_new); } }, function () {});
      }, 60000);
      return;
    }
    var nw = { sid: st.id, name: st.name, teacher: st.teacher, avatar: st.avatar };
    var was = WHO && WHO.sid;
    try { localStorage.setItem("en_who", JSON.stringify(nw)); } catch (e) {}
    if (was !== st.id && !sessionStorage.getItem("en_rl")) {   // другой ученик или первый вход — перечитать прогресс под его номером
      try { sessionStorage.setItem("en_rl", "1"); } catch (e) {}
      location.reload(); return;
    }
    try { sessionStorage.removeItem("en_rl"); } catch (e) {}
    WHO = nw; EN.role = "student";
    mergeState(d.state);
    voices.forEach(function (v) { v._student(((d.state || {}).v || {})[v.getAttribute("data-id")] || null); });
    var go2 = function () {
      EN.log({ t: "view", title: document.title });
      if (/[?&]hello=1/.test(location.search)) { hello(st); history.replaceState(null, "", location.pathname + location.hash); }
      if (window.EN_ME) window.EN_ME(st, d);
    };
    if (st.consent && st.consent.length) EN.consent("student", st.consent, st.name, go2); else go2();
    if (BD.unit && BD.page) lsSet("last", { path: location.pathname, title: (BD.label || "модуль " + BD.unit.replace("unit", "")) + " · " + document.title.split(" — ")[0] });
  }
  /* =================== рабочее место разбора (преподаватель) =================== */
  function startReview(tc) {
    var sid = REVIEW, follow = /[?&]follow=1/.test(location.search), pinned = {}, sig = {}, lastLive = "", busy = false;
    var keep = "review=" + sid;
    // ссылки внутри модуля — тоже в режиме разбора
    $$(".tabs a, .next a, .crumbs a").forEach(function (a) {
      var h = a.getAttribute("href"); if (!h || /^https?:|^#|^mailto/.test(h)) return;
      a.setAttribute("href", h + (h.indexOf("?") >= 0 ? "&" : "?") + keep);
    });
    $$(".toolbar [data-act=reset], .toolbar [data-act=check]").forEach(function (b) { b.hidden = true; });
    $$(".writer textarea").forEach(function (t) { t.readOnly = true; });
    var bar = el("div", "rv-bar", '<div class="rv-in"><span class="rv-eye">Разбор</span><b class="rv-name">…</b>' +
      '<span class="rv-live"></span><span class="rv-sp"></span>' +
      '<button class="btn sm ghost" type="button" data-nav="-1" title="Предыдущее задание с ответами">‹</button><span class="rv-pos"></span>' +
      '<button class="btn sm ghost" type="button" data-nav="1" title="Следующее задание с ответами">›</button>' +
      '<button class="btn sm ghost" type="button" data-bad>Следующее с ошибками</button>' +
      '<label class="rv-tg"><input type="checkbox" data-follow' + (follow ? " checked" : "") + '> Следовать за учеником</label>' +
      '<a class="btn sm plain" href="' + ROOT + "teacher/#s=" + sid + '">В кабинет</a></div>');
    var hdr = document.querySelector(".top"); hdr.parentNode.insertBefore(bar, hdr.nextSibling);
    document.body.classList.add("reviewing");
    var fb = bar.querySelector("[data-follow]");
    fb.addEventListener("change", function () { follow = fb.checked; if (follow) poll(); });
    function exList() { return registry.filter(function (r) { return r.ex.classList.contains("rv-has"); }); }
    function go(r) { r.ex.scrollIntoView({ behavior: "smooth", block: "start" }); r.ex.classList.add("rv-flash"); setTimeout(function () { r.ex.classList.remove("rv-flash"); }, 1200); }
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var list = exList(); if (!list.length) return;
      var y = 90, cur = 0;
      list.forEach(function (r, i) { if (r.ex.getBoundingClientRect().top < y + 5) cur = i; });
      if (b.hasAttribute("data-nav")) go(list[Math.max(0, Math.min(list.length - 1, cur + +b.getAttribute("data-nav")))]);
      if (b.hasAttribute("data-bad")) {
        var bad = list.filter(function (r, i) { return i > cur && r.ex.classList.contains("rv-bad"); });
        if (!bad.length) bad = list.filter(function (r) { return r.ex.classList.contains("rv-bad"); });
        if (bad.length) go(bad[0]);
      }
    });
    function when(t) { return t ? t.slice(11, 16) + (t.slice(0, 10) === new Date().toISOString().slice(0, 10) ? "" : " " + t.slice(8, 10) + "." + t.slice(5, 7)) : ""; }
    function panel(r, att, pr) {
      var p = r.ex.querySelector(".rv-panel");
      if (!p) { p = el("div", "rv-panel"); var ins = r.ex.querySelector(".ins"); ins.parentNode.insertBefore(p, ins.nextSibling); }
      var opts = [];
      (att || []).forEach(function (a, i) {
        opts.push({ key: "a" + a.id, st: a.st, label: a.kind === "show" ? "Показал(а) ответы" : "Попытка " + (opts.filter(function (o) { return o.check; }).length + 1),
          check: a.kind === "check", sc: a.kind === "check" ? a.score + "/" + a.total : "", ok: a.kind === "check" && +a.score === +a.total, t: a.created_at });
      });
      var lastAt = att && att.length ? att[att.length - 1].created_at : "";
      if (pr && pr.state && (!lastAt || pr.updated_at > lastAt)) opts.push({ key: "now", st: pr.state, label: "Сейчас вводит", sc: "", t: pr.updated_at, draft: true });
      r.ex.classList.toggle("rv-has", opts.length > 0);
      r.ex.classList.toggle("rv-none", opts.length === 0);
      var lastCheck = (att || []).filter(function (a) { return a.kind === "check"; }).pop();
      r.ex.classList.toggle("rv-bad", !!lastCheck && +lastCheck.score < +lastCheck.total);
      if (!opts.length) { p.innerHTML = '<span class="rv-empty">Ученик ещё не делал это задание</span>'; return; }
      var sel = pinned[r.id] && opts.some(function (o) { return o.key === pinned[r.id]; }) ? pinned[r.id] : opts[opts.length - 1].key;
      p.innerHTML = '<span class="rv-lbl">Ответы ученика:</span>' + opts.map(function (o) {
        return '<button type="button" class="rv-att' + (o.key === sel ? " on" : "") + (o.draft ? " a-draft" : o.check ? (o.ok ? " a-good" : " a-bad") : " a-shown") + '" data-k="' + o.key + '">' +
          esc(o.label) + (o.sc ? " · <b>" + o.sc + "</b>" : "") + ' <small>' + esc(when(o.t)) + "</small></button>";
      }).join("") + '<span class="rv-note">' + (pr ? "проверок: " + pr.attempts + (+pr.shown ? " · смотрел(а) ответы" : "") : "") + "</span>";
      var o = opts.filter(function (x) { return x.key === sel; })[0];
      r.apply(o.st);
      r.ex.classList.toggle("rv-draft", !!o.draft);
      $$(".rv-att", p).forEach(function (b) {
        b.addEventListener("click", function () {
          var k = b.getAttribute("data-k");
          pinned[r.id] = k === opts[opts.length - 1].key ? null : k;   // последняя — «живая», обновляется сама
          panel(r, att, pr);
        });
      });
    }
    function render(d) {
      bar.querySelector(".rv-name").textContent = d.student.name;
      registry.forEach(function (r) {
        var att = d.attempts[r.id], pr = d.progress[r.id];
        var sg = JSON.stringify([att ? att.length : 0, pr ? pr.updated_at : ""]);
        if (sig[r.id] === sg) return;
        var first = sig[r.id] === undefined; sig[r.id] = sg;
        panel(r, att, pr);
        if (!first) { r.ex.classList.add("rv-flash"); setTimeout(function () { r.ex.classList.remove("rv-flash"); }, 1200); }
      });
      voices.forEach(function (v) { var x = (d.voices || {})[v.getAttribute("data-id")] || null; v._teacher(x ? "🎙 Голосовой ответ ученика:" : "Голосового ответа пока нет"); v._show(x); });
      writers.forEach(function (w) {
        var x = d.writings[w.getAttribute("data-id")];
        w._set(x ? x.text : ""); w.classList.toggle("rv-none", !x);
      });
      var list = exList(); bar.querySelector(".rv-pos").textContent = list.length + " из " + registry.length;
      // где ученик сейчас
      var L = d.live || {}, live = bar.querySelector(".rv-live"), here = L.path === location.pathname;
      $$(".rv-here").forEach(function (x) { x.classList.remove("rv-here"); });
      if (L.online && here && L.ex) { var ex = document.getElementById(L.ex); if (ex) ex.classList.add("rv-here"); }
      live.innerHTML = L.online ? '<i class="dot on"></i> онлайн' + (here ? (L.ex ? ' · <a href="#' + esc(L.ex) + '">здесь, в задании</a>' : " · на этой странице") :
        ' · <a href="' + esc(L.path) + "?" + keep + (L.ex ? "#" + esc(L.ex) : "") + '">на другой странице →</a>') :
        '<i class="dot"></i> не в сети' + (L.at ? " · был(а) " + esc(when(L.at)) : "");
      var key = (L.path || "") + "#" + (L.ex || "");
      if (follow && L.online && key !== lastLive) {
        if (!here && L.path) { location.href = L.path + "?" + keep + "&follow=1" + (L.ex ? "#" + L.ex : ""); return; }
        if (L.ex && document.getElementById(L.ex) && lastLive !== "") go({ ex: document.getElementById(L.ex) });
      }
      lastLive = key;
    }
    function poll(first) {
      if (busy) return; busy = true;
      fetch(API + "t_review&id=" + sid + "&course=" + encodeURIComponent(BD.course || "") + "&unit=" + encodeURIComponent(BD.unit || "") +
        "&page=" + encodeURIComponent(BD.page || "") + (first ? "" : "&poll=1"), { credentials: "same-origin", cache: "no-store" })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          busy = false;
          if (!d.ok) { bar.querySelector(".rv-name").textContent = d.error === "notfound" ? "ученик не найден" : "нет доступа"; return; }
          render(d);
          if (first && location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) setTimeout(function () { t.scrollIntoView({ block: "start" }); }, 50); }
        }, function () { busy = false; });
    }
    poll(true);
    setInterval(function () { if (document.visibilityState === "visible") poll(); }, 4000);
  }

  function cookieBar() {
    try { if (localStorage.getItem("en_cookie_ok")) return; } catch (e) { return; }
    var b = el("div", "cookie-bar", "<span>Сайт использует только необходимые cookie и хранилище браузера — без рекламы и сторонней аналитики. " +
      '<a href="' + ROOT + 'legal/cookies.html">Подробнее</a></span><button class="btn" type="button">Понятно</button>');
    b.querySelector("button").addEventListener("click", function () { try { localStorage.setItem("en_cookie_ok", "1"); } catch (e) {} b.remove(); });
    document.body.appendChild(b);
  }
  fetch(API + "me&state=all", { credentials: "same-origin", cache: "no-store" })
    .then(function (r) { if (!r.ok) throw 0; return r.json(); })
    .then(onMe)
    .catch(function () {   // нет сети или сервера: показываем то, что знаем
      if (WHO && WHO.sid && window.EN_ME) window.EN_ME({ id: WHO.sid, name: WHO.name, teacher: WHO.teacher, offline: true }, null);
      if (window.EN_TEACHER) window.EN_TEACHER(null);
    });

  /* ---------- главная: вход по коду — по нему понятно, учитель это или ученик ---------- */
  var lf = document.getElementById("login-form");
  if (lf) {
    var lerr = document.getElementById("login-err");
    var LMSG = { bad: "Код не подошёл. Проверьте цифры или попросите код у преподавателя.",
      wait: "Слишком много попыток. Подождите 15 минут.", db: "Сервер временно недоступен. Попробуйте позже." };
    var lq = /[?&]err=(\w+)/.exec(location.search);
    if (lq && LMSG[lq[1]]) { lerr.hidden = false; lerr.textContent = LMSG[lq[1]]; }
    var cin = lf.code;
    cin.addEventListener("input", function () { cin.value = cin.value.replace(/\D/g, "").slice(0, 6); if (cin.value.length === 6) lf.requestSubmit ? lf.requestSubmit() : null; });
    lf.addEventListener("submit", function (e) {
      e.preventDefault();
      if (lf.dataset.busy) return; lf.dataset.busy = "1";
      post("login", { code: cin.value }).then(function (r) {
        delete lf.dataset.busy;
        if (r.ok) {
          var nx = (/[?&]next=([^&#]+)/.exec(location.search) || [])[1];
          nx = nx ? decodeURIComponent(nx) : "";
          location.href = nx && /^\/[a-z0-9\/._?=&#-]*$/i.test(nx) && (r.role === "teacher" || nx.indexOf("/teacher") !== 0) ? nx : home(r.role) + (r.role === "student" ? "?hello=1" : "");
          return;
        }
        lerr.hidden = false; lerr.textContent = LMSG[/^wait/.test(r.error) ? "wait" : (r.error === "db" ? "db" : "bad")];
        cin.select();
      }, function () { delete lf.dataset.busy; lerr.hidden = false; lerr.textContent = LMSG.db; });
    });
  }

  /* ---------- приложение (PWA) ---------- */
  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
    addEventListener("load", function () { navigator.serviceWorker.register(ROOT + "sw.js").catch(function () {}); });
  }
  var installEvt = null, ib = document.getElementById("pwa-install");
  addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); installEvt = e; if (ib) ib.hidden = false; });
  if (ib) ib.addEventListener("click", function () { if (installEvt) { installEvt.prompt(); installEvt = null; ib.hidden = true; } });
})();
