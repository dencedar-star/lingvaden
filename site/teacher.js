/* lingvaden.ru — кабинет преподавателя: ученики, пространства (перетаскивание), курсы и прогресс,
   задания (база тестов → домашняя работа), домашние работы (сданные — с колокольчиком), профиль */
(function () {
  "use strict";
  var app = document.getElementById("t-app");
  if (!app || !window.EN) return;
  var EN = window.EN, esc = EN.esc, post = EN.post, API = EN.api, ROOT = document.body.dataset.root || "/";
  var D = null, CAT = null, EXMAP = {}, UNITS = {}, HW = null, busy = false;
  var KIND = { "class": "Класс", group: "Группа", marathon: "Марафон", other: "Другое" };
  var PAGE_T = { tests: "Тесты", book: "Учебник", writing: "Письмо", theory: "Теория", workbook: "Тетрадь" };

  function $(s, r) { return (r || app).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || app).querySelectorAll(s)); }
  function get(a, q) {
    return fetch(API + a + (q || ""), { credentials: "same-origin", cache: "no-store" }).then(function (r) {
      if (r.status === 401) { location.href = ROOT; throw 0; }
      return r.json();
    });
  }
  function dur(sec) {
    sec = +sec || 0;
    if (sec < 60) return sec ? "< 1 мин" : "0 мин";
    var m = Math.round(sec / 60), h = Math.floor(m / 60);
    return h ? h + " ч " + (m % 60 < 10 ? "0" : "") + (m % 60) + " мин" : m + " мин";
  }
  function when(s) {
    if (!s) return "—";
    var d = new Date(s.replace(" ", "T") + "+03:00"), now = new Date();
    var t = d.toLocaleTimeString("ru-RU", { hour: "2-digit", minute: "2-digit" });
    var days = Math.floor((new Date(now.toDateString()) - new Date(d.toDateString())) / 864e5);
    if (days === 0) return "сегодня " + t;
    if (days === 1) return "вчера " + t;
    return d.toLocaleDateString("ru-RU", { day: "numeric", month: "short", year: days > 300 ? "numeric" : undefined }) + " " + t;
  }
  function day(s) { return s ? new Date(s.replace(" ", "T") + "+03:00").toLocaleDateString("ru-RU", { day: "numeric", month: "long" }) : ""; }
  function pctCls(p) { return p >= 80 ? "hi" : p >= 50 ? "mid" : p > 0 ? "lo" : "none"; }
  var toast = EN.toast;
  var ERR = { name: "Укажите имя.", email: "E-mail указан с ошибкой.", noemail: "У ученика нет e-mail — укажите его.",
    mail: "Письмо не отправилось. Попробуйте позже или отправьте в Telegram.", maillimit: "Слишком много писем за сутки.",
    limit: "Достигнут предел учеников.", notfound: "Не найдено — обновите страницу.", title: "Назовите домашнюю работу.",
    items: "Выберите хотя бы одно задание.", nobody: "Выберите учеников или класс (в классе должны быть ученики)." };
  function act(a, data, okMsg) {
    if (busy) return Promise.resolve({ ok: false });
    busy = true;
    return post(a, data).then(function (r) {
      busy = false;
      if (!r.ok) { toast(ERR[r.error] || "Не получилось. Проверьте связь.", true); return r; }
      if (okMsg) toast(okMsg);
      return r;
    }, function () { busy = false; toast("Нет связи с сервером.", true); return { ok: false }; });
  }

  /* ---------------- данные ---------------- */
  function load() {
    return Promise.all([get("t_data"), CAT ? Promise.resolve(CAT) : fetch(ROOT + "assets/catalog.json?v=" + (window.EN && EN.ver || ""), { cache: "no-cache" }).then(function (r) { return r.json(); })])
      .then(function (x) {
        D = x[0]; CAT = x[1];
        if (!D.ok) throw 0;
        CAT.courses.forEach(function (c) {
          c.units.forEach(function (u) {
            var n = 0, t = 0;
            u.pages.forEach(function (p) {
              p.ex.forEach(function (e) {
                n++; t += e[1];
                EXMAP[e[0]] = { course: c.id, unit: u, page: p, let: e[2], ins: e[3], n: e[1] };
              });
            });
            UNITS[c.id + "/" + u.id] = { n: n, t: t, u: u };
          });
        });
        D.byId = {};
        D.students.forEach(function (s) { D.byId[s.id] = s; s.prog = {}; s.best = 0; s.done = 0; });
        D.progress.forEach(function (p) {
          var s = D.byId[p.sid]; if (!s) return;
          s.prog[p.course + "/" + p.unit] = p; s.best += p.best; s.done += p.done;
        });
        D.courseTotal = {};
        CAT.courses.forEach(function (c) { var t = 0; c.units.forEach(function (u) { t += UNITS[c.id + "/" + u.id].t; }); D.courseTotal[c.id] = t; });
      });
  }
  function loadHw() { return get("t_hw_list").then(function (r) { HW = r.ok ? r.hw : []; return HW; }); }
  function coursePct(s, cid) {
    var b = 0; Object.keys(s.prog).forEach(function (k) { if (k.indexOf(cid + "/") === 0) b += s.prog[k].best; });
    return D.courseTotal[cid] ? Math.round(100 * b / D.courseTotal[cid]) : 0;
  }
  function online(s) { return s.online ? '<span class="tag live" title="Сейчас на сайте">● онлайн</span> ' : ""; }
  function status(s) {
    if (!s.first_login_at) return '<span class="tag off">' + (s.invited_at ? "код отправлен · не входил(а)" : "ещё не входил(а)") + "</span>";
    return '<span class="tag on">был(а) ' + esc(when(s.last_seen_at || s.first_login_at)) + "</span>";
  }
  function spaceById(id) { return D.spaces.filter(function (x) { return x.id === +id; })[0]; }

  /* ---------------- каркас: вид выбирается меню слева ---------------- */
  var TITLES = { students: "Ученики", spaces: "Классы", courses: "Курсы", tasks: "Задания", homework: "Домашние работы", profile: "Профиль" };
  function route() {
    var h = location.hash.replace("#", "") || "students";
    var m = /^s=(\d+)/.exec(h), hw = /^hw=(\d+)&s=(\d+)/.exec(h);
    var key = m ? "students" : hw ? "homework" : h.split("&")[0];
    if (!TITLES[key]) key = "students";
    EN.markSide(key === "profile" ? "" : key);
    app.innerHTML = '<div id="t-view"></div>';
    var v = $("#t-view");
    if (m) return studentView(v, +m[1]);
    if (hw) return hwResult(v, +hw[1], +hw[2]);
    ({ students: studentsView, spaces: spacesView, courses: coursesView, tasks: tasksView, homework: homeworkView, profile: profileView })[key](v, h);
    scrollTo(0, 0);
  }
  function refresh() { return load().then(route); }
  addEventListener("hashchange", function () { if (D) route(); });
  function head(title, sub) { return '<div class="t-head"><div><h1 class="page-title">' + title + "</h1>" + (sub ? '<p class="lead">' + sub + "</p>" : "") + "</div></div>"; }

  /* ---------------- ученики ---------------- */
  function invite(s) {
    return "Здравствуйте, " + s.name + "! Это " + D.teacher.name + ". Приглашаю заниматься английским на Lingvaden English.\n" +
      "Ваш код для входа: " + s.code + " — введите его на " + D.site.replace(/^https?:\/\//, "") + "\nИли откройте личную ссылку: " + s.link;
  }
  function tgUrl(s) {
    return "https://t.me/share/url?url=" + encodeURIComponent(s.link) + "&text=" + encodeURIComponent(invite(s).replace("\nИли откройте личную ссылку: " + s.link, ""));
  }
  function copy(t, quiet) {
    return (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { if (!quiet) toast("Скопировано"); return true; }, function () {
      var ta = document.createElement("textarea"); ta.value = t; document.body.appendChild(ta); ta.select();
      var ok = false; try { ok = document.execCommand("copy"); } catch (e) {}
      ta.remove(); if (ok && !quiet) toast("Скопировано");
      return ok;
    });
  }
  // три способа передать ученику код и ссылку: Telegram, e-mail, скопировать
  function sendVia(s, via, win) {
    if (via === "telegram") {
      if (win) win.location = tgUrl(s); else window.open(tgUrl(s), "_blank", "noopener");
      post("t_invited", { id: s.id, via: "telegram" });
      return Promise.resolve();
    }
    if (via === "copy") {
      return copy(invite(s), true).then(function (ok) {
        post("t_invited", { id: s.id, via: "copy" });
        if (ok) toast("Приглашение с кодом и ссылкой скопировано"); else showInvite(s);
      });
    }
    if (!s.email) { askEmail(s); return Promise.resolve(); }
    return act("t_student_mail", { id: s.id }, "Письмо отправлено на " + s.email);
  }
  function showInvite(s) {
    var m = modal("<h2>Приглашение для: " + esc(s.name) + '</h2><textarea class="invite-t" readonly rows="5">' + esc(invite(s)) + "</textarea>" +
      '<div class="modal-btns"><button class="btn" type="button" data-c>Копировать</button></div>');
    m.box.querySelector("[data-c]").addEventListener("click", function () { copy(invite(s)); });
    m.box.querySelector("textarea").select();
  }
  function askEmail(s) {
    var m = modal("<h2>E-mail для: " + esc(s.name) + '</h2><form class="stack" data-f><label>E-mail ученика (или родителя)<input name="email" type="email" required maxlength="190"></label>' +
      '<div class="modal-btns"><button class="btn" type="submit">Сохранить и отправить</button></div></form>');
    var f = m.box.querySelector("[data-f]");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      act("t_student_update", { id: s.id, name: s.name, email: f.email.value }).then(function (r) {
        if (!r.ok) return;
        s.email = f.email.value.trim(); m.close();
        sendVia(s, "email").then(refresh);
      });
    });
  }
  function shareBtns(s) {
    return '<span class="send-btns"><button class="btn tg sm" type="button" data-via="telegram" data-sid="' + s.id + '" title="Отправить код и ссылку в Telegram">Telegram</button>' +
      '<button class="btn ghost sm" type="button" data-via="email" data-sid="' + s.id + '" title="' + (s.email ? "Письмо на " + esc(s.email) : "Указать e-mail и отправить") + '">E-mail</button>' +
      '<button class="btn plain sm" type="button" data-via="copy" data-sid="' + s.id + '" title="Скопировать приглашение с кодом и ссылкой">Копировать ссылку</button></span>';
  }
  function bindSend(v) {
    v.addEventListener("click", function (e) {
      var b = e.target.closest("[data-via][data-sid]"); if (!b) return;
      var s = D.byId[+b.getAttribute("data-sid")]; if (s) sendVia(s, b.getAttribute("data-via"));
    });
  }
  function studentCard(s) {
    var cid = CAT.courses[0].id, p = coursePct(s, cid);
    return '<div class="st-card" data-sid="' + s.id + '">' + EN.avatar(s.name, s.avatar) +
      '<div class="st-main">' + online(s) + '<a class="st-name" href="#s=' + s.id + '">' + esc(s.name) + "</a>" +
      '<span class="st-mail">код <b class="code">' + esc(s.code || "—") + "</b>" + (s.email ? " · " + esc(s.email) : "") + (s.telegram ? " · " + esc(s.telegram) : "") + "</span>" +
      '<div class="st-meta">' + status(s) + (s.total_seconds ? ' <span class="tag">⏱ ' + dur(s.total_seconds) + "</span>" : "") +
      s.spaces.map(function (id) { var sp = spaceById(id); return sp ? ' <span class="tag sp">' + esc(sp.name) + "</span>" : ""; }).join("") + "</div>" +
      '<div class="mini-bar" title="Прогресс по курсу"><i class="' + pctCls(p) + '" style="width:' + p + '%"></i></div></div>' +
      '<div class="st-acts">' + shareBtns(s) + '<span class="ic-btns"><button class="ic-btn" type="button" data-ed="' + s.id + '" title="Изменить" aria-label="Изменить">' + EN.icon("edit") +
      '</button><button class="ic-btn danger" type="button" data-del="' + s.id + '" title="Удалить" aria-label="Удалить">' + EN.icon("trash") + "</button></span></div></div>";
  }
  function studentsView(v) {
    var list = D.students.slice();
    v.innerHTML = head("Ученики", esc(D.teacher.name) + " · учеников: " + list.length) +
      '<section class="page"><h2>Добавить ученика</h2><form class="add-form add-st" id="add-st" autocomplete="off">' +
      '<input name="name" placeholder="ФИО или просто имя" maxlength="200" required>' +
      '<input name="email" type="email" placeholder="E-mail (для отправки письмом)" maxlength="190">' +
      '<button class="sr-only" type="submit" tabindex="-1">Добавить</button>' +   // Enter — первая (невидимая) кнопка: просто добавить
      '<div class="send-btns"><button class="btn tg" type="submit" data-v="telegram">Отправить в Telegram</button>' +
      '<button class="btn ghost" type="submit" data-v="email">Отправить по e-mail</button>' +
      '<button class="btn plain" type="submit" data-v="copy">Скопировать ссылку</button></div></form>' +
      '<p class="disclaimer">ⓘ <b>Можно указать просто имя</b> — фамилия и e-mail не обязательны. Ученик получит свой 6-значный код и личную ссылку: ' +
      'по коду он входит на главной странице. Вносите данные ученика с его согласия (до 14 лет — с согласия родителя). ' +
      '<a href="' + ROOT + 'legal/teachers.html" target="_blank">Условия для преподавателей</a></p></section>' +
      '<section class="page"><h2>Все ученики <small>' + list.length + "</small></h2>" +
      (list.length > 6 ? '<input class="filter" id="st-filter" placeholder="Найти ученика…">' : "") +
      '<div class="st-list" id="st-list">' + (list.length ? list.map(studentCard).join("") :
        '<p class="empty">Пока нет учеников. Добавьте первого — он получит код и личную ссылку.</p>') + "</div></section>";
    var f = $("#add-st");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      // Enter — просто добавить в список; кнопки — добавить и сразу отправить
      var via = e.submitter && e.submitter.getAttribute("data-v") || "";
      if (via === "email" && !f.email.value.trim()) { toast("Укажите e-mail, чтобы отправить письмо", true); f.email.focus(); return; }
      var win = via === "telegram" ? window.open("about:blank", "_blank") : null;   // окно — сразу по нажатию, иначе браузер его заблокирует
      act("t_student_add", { name: f.name.value, email: f.email.value }).then(function (r) {
        if (!r.ok) { if (win) win.close(); return; }
        var s = { id: r.id, name: f.name.value.trim(), email: f.email.value.trim(), code: r.code, link: r.link };
        var done = function () { f.reset(); refresh().then(function () { var x = $("#add-st input[name=name]"); if (x) x.focus(); var c = app.querySelector('.st-card[data-sid="' + r.id + '"]'); if (c) c.classList.add("fresh"); }); };
        if (!via) { toast("Ученик добавлен · код " + r.code); done(); return; }
        sendVia(s, via, win).then(function () { toast("Ученик добавлен: код " + r.code); done(); });
      });
    });
    var flt = $("#st-filter");
    if (flt) flt.addEventListener("input", function () {
      var q = flt.value.toLowerCase();
      $$(".st-card", v).forEach(function (c) { c.hidden = q && D.byId[c.getAttribute("data-sid")].name.toLowerCase().indexOf(q) < 0; });
    });
    bindSend(v);
    v.addEventListener("click", function (e) {
      var b = e.target.closest("[data-ed],[data-del]"); if (!b) return;
      var s = D.byId[+(b.getAttribute("data-ed") || b.getAttribute("data-del"))]; if (!s) return;
      if (b.hasAttribute("data-ed")) editStudent(s); else confirmDelete(s);
    });
  }
  function confirmDelete(s) {
    var m = modal("<h2>Удалить ученика?</h2><p><b>" + esc(s.name) + "</b> и все его данные — ответы, попытки, домашние работы, тексты, журнал — будут удалены. Отменить нельзя.</p>" +
      '<div class="modal-btns"><button class="btn danger" type="button" data-yes>Удалить</button><button class="btn plain" type="button" data-no>Отмена</button></div>');
    m.box.querySelector("[data-no]").addEventListener("click", m.close);
    m.box.querySelector("[data-yes]").addEventListener("click", function () {
      act("t_student_delete", { id: s.id }, "Ученик удалён").then(function (x) { if (x.ok) { m.close(); refresh(); } });
    });
  }

  /* ---------------- пространства ---------------- */
  function courseOptions(sel) {
    return '<option value="">любой курс</option>' + CAT.courses.map(function (c) {
      return '<option value="' + esc(c.id) + '"' + (sel === c.id ? " selected" : "") + ">" + esc(c.title) + "</option>";
    }).join("");
  }
  function spaceCard(p) {
    var mem = p.members.map(function (id) { return D.byId[id]; }).filter(Boolean);
    var avg = mem.length ? Math.round(mem.reduce(function (a, s) { return a + coursePct(s, p.course || CAT.courses[0].id); }, 0) / mem.length) : 0;
    return '<div class="space" data-space="' + p.id + '"><div class="space-head"><span class="kind k-' + p.kind + '">' + KIND[p.kind] + "</span>" +
      '<b class="space-name">' + esc(p.name) + '</b><span class="space-n">' + mem.length + "</span></div>" +
      (p.course ? '<div class="space-course">' + esc((CAT.courses.filter(function (c) { return c.id === p.course; })[0] || {}).title || p.course) + "</div>" : "") +
      '<div class="chips">' + (mem.length ? mem.map(function (s) {
        return '<span class="chip" data-sid="' + s.id + '"><a href="#s=' + s.id + '">' + esc(s.name) + '</a><button type="button" data-rm="' + s.id + '" aria-label="Убрать из класса">×</button></span>';
      }).join("") : '<span class="drop-hint">Перетащите сюда учеников</span>') + "</div>" +
      '<div class="space-foot"><a href="#courses&space=' + p.id + '">Прогресс' + (mem.length ? " · в среднем " + avg + "%" : "") + "</a>" +
      '<a href="#tasks&new&space=' + p.id + '">Задать работу</a>' +
      '<button class="btn plain sm" type="button" data-edit-space="' + p.id + '">Изменить</button></div></div>';
  }
  function spacesView(v) {
    v.innerHTML = head("Классы", "Классы, группы, марафоны. Перетащите ученика за значок ⠿ на класс; один ученик может быть в нескольких.") +
      '<div class="t-grid sp-grid"><section class="page t-col"><h2>Ученики <small>' + D.students.length + "</small></h2>" +
      (D.students.length > 8 ? '<input class="filter" id="st-filter" placeholder="Найти ученика…">' : "") +
      '<div class="drag-list">' + (D.students.length ? D.students.map(function (s) {
        return '<div class="st-card mini" data-sid="' + s.id + '"><span class="grip" title="Перетащите в класс" aria-hidden="true">⠿</span>' + EN.avatar(s.name, s.avatar) +
          '<a class="st-name" href="#s=' + s.id + '">' + esc(s.name) + "</a>" +
          '<select class="sm" data-addto="' + s.id + '" aria-label="Добавить в класс"><option value="">＋</option>' +
          D.spaces.map(function (p) { return '<option value="' + p.id + '">' + esc(p.name) + "</option>"; }).join("") + "</select></div>";
      }).join("") : '<p class="empty">Сначала добавьте учеников в разделе «Ученики».</p>') + "</div></section>" +
      '<section class="page t-col"><h2>Классы <small>' + D.spaces.length + "</small></h2>" +
      '<form class="add-form" id="add-sp" autocomplete="off"><input name="name" placeholder="Название: 7Б, Группа B1, Марафон…" maxlength="120" required>' +
      '<select name="kind"><option value="class">Класс</option><option value="group" selected>Группа</option><option value="marathon">Марафон</option><option value="other">Другое</option></select>' +
      '<select name="course">' + courseOptions("") + '</select><button class="btn" type="submit">Создать</button></form>' +
      '<div class="spaces">' + (D.spaces.length ? D.spaces.map(spaceCard).join("") : '<p class="empty">Создайте класс, группу или марафон.</p>') + "</div></section></div>";
    $("#add-sp").addEventListener("submit", function (e) {
      e.preventDefault(); var f = e.target;
      act("t_space_add", { name: f.name.value, kind: f.kind.value, course: f.course.value }, "Класс создан").then(function (r) { if (r.ok) refresh(); });
    });
    var flt = $("#st-filter");
    if (flt) flt.addEventListener("input", function () {
      var q = flt.value.toLowerCase();
      $$(".drag-list .st-card", v).forEach(function (c) { c.hidden = q && D.byId[c.getAttribute("data-sid")].name.toLowerCase().indexOf(q) < 0; });
    });
    v.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      if (b.hasAttribute("data-rm")) {
        var sp = +b.closest(".space").getAttribute("data-space");
        act("t_member", { space: sp, student: +b.getAttribute("data-rm"), on: 0 }).then(function (r) { if (r.ok) refresh(); });
      }
      if (b.hasAttribute("data-edit-space")) editSpace(+b.getAttribute("data-edit-space"));
    });
    v.addEventListener("change", function (e) {
      var s = e.target; if (!s.hasAttribute("data-addto") || !s.value) return;
      member(+s.value, +s.getAttribute("data-addto"));
    });
    dnd(v);
  }
  function member(space, sid) {
    var sp = spaceById(space);
    if (sp && sp.members.indexOf(sid) >= 0) { toast("Уже в «" + sp.name + "»"); return; }
    act("t_member", { space: space, student: sid, on: 1 }, sp ? "Добавлен(а) в «" + sp.name + "»" : "").then(function (r) { if (r.ok) refresh(); });
  }
  // перетаскивание указателем: мышь, палец, перо (HTML5 DnD на телефонах не работает)
  var dndOn = false, drag = null, dndView = null;
  function dnd(v) {
    dndView = v;
    v.addEventListener("pointerdown", function (e) {
      var card = e.target.closest(".st-card, .chip");
      if (!card || e.target.closest("button, select, input") || (e.target.closest("a") && !e.target.closest(".grip"))) return;
      if (e.pointerType !== "mouse" && !e.target.closest(".grip")) return;   // на телефоне — только за значок, чтобы не мешать прокрутке
      drag = { sid: +card.getAttribute("data-sid"), x: e.clientX, y: e.clientY, ghost: null, id: e.pointerId };
    });
    if (dndOn) return;
    dndOn = true;
    addEventListener("pointermove", function (e) {
      if (!drag || e.pointerId !== drag.id) return;
      if (!drag.ghost) {
        if (Math.abs(e.clientX - drag.x) + Math.abs(e.clientY - drag.y) < 6) return;
        drag.ghost = EN.el("div", "drag-ghost", esc(D.byId[drag.sid] ? D.byId[drag.sid].name : ""));
        document.body.appendChild(drag.ghost); document.body.classList.add("dragging");
      }
      e.preventDefault();
      drag.ghost.style.transform = "translate(" + (e.clientX + 12) + "px," + (e.clientY + 12) + "px)";
      var over = document.elementFromPoint(e.clientX, e.clientY);
      $$(".space", dndView).forEach(function (s) { s.classList.toggle("drop-over", !!over && s.contains(over)); });
    }, { passive: false });
    function end(e) {
      if (!drag || e.pointerId !== drag.id) return;
      var d = drag; drag = null;
      if (!d.ghost) return;
      d.ghost.remove(); document.body.classList.remove("dragging");
      var over = document.elementFromPoint(e.clientX, e.clientY), sp = over && over.closest && over.closest(".space");
      $$(".space", dndView).forEach(function (s) { s.classList.remove("drop-over"); });
      if (sp && dndView.contains(sp)) member(+sp.getAttribute("data-space"), d.sid);
    }
    addEventListener("pointerup", end);
    addEventListener("pointercancel", end);
  }
  function editSpace(id) {
    var p = spaceById(id); if (!p) return;
    var m = modal("<h2>Класс</h2><form id=\"sp-ed\" class=\"stack\"><label>Название<input name=\"name\" maxlength=\"120\" required value=\"" + esc(p.name) + "\"></label>" +
      '<label>Тип<select name="kind">' + Object.keys(KIND).map(function (k) { return '<option value="' + k + '"' + (k === p.kind ? " selected" : "") + ">" + KIND[k] + "</option>"; }).join("") + "</select></label>" +
      '<label>Курс<select name="course">' + courseOptions(p.course || "") + "</select></label>" +
      '<div class="modal-btns"><button class="btn" type="submit">Сохранить</button><button class="btn danger-o" type="button" data-del>Удалить класс</button></div>' +
      '<p class="note-s">Удаление класса не удаляет учеников и их результаты.</p></form>');
    var f = m.box.querySelector("#sp-ed");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      act("t_space_update", { id: id, name: f.name.value, kind: f.kind.value, course: f.course.value }, "Сохранено").then(function (r) { if (r.ok) { m.close(); refresh(); } });
    });
    f.querySelector("[data-del]").addEventListener("click", function (e) {
      var b = e.target;
      if (!b.classList.contains("armed")) { b.classList.add("armed"); b.textContent = "Точно удалить?"; return; }
      act("t_space_delete", { id: id }, "Класс удалён").then(function (r) { if (r.ok) { m.close(); refresh(); } });
    });
  }

  /* ---------------- модальные окна ---------------- */
  function modal(html, wide) {
    var m = EN.el("div", "modal"), b = EN.el("div", "modal-box" + (wide ? " wide" : ""), '<button class="modal-x" type="button" aria-label="Закрыть">×</button>' + html);
    m.appendChild(b); document.body.appendChild(m); document.body.classList.add("modal-open");
    function close() { m.remove(); document.body.classList.remove("modal-open"); }
    m.addEventListener("click", function (e) { if (e.target === m || e.target.classList.contains("modal-x")) close(); });
    addEventListener("keydown", function k(e) { if (e.key === "Escape") { close(); removeEventListener("keydown", k); } });
    return { box: b, close: close };
  }

  /* ---------------- курсы: свёрнутые карточки курсов, внутри — компактные модули ---------------- */
  function courseStat(c) {
    var n = 0; c.units.forEach(function (u) { n += UNITS[c.id + "/" + u.id].n; });
    return n;
  }
  function unitTiles(c, href) {
    return '<div class="u-tiles">' + c.units.map(function (u) {
      var U = UNITS[c.id + "/" + u.id];
      return '<a class="u-tile" href="' + esc(href ? href(u) : u.url) + '"><span class="u-n">' + esc(u.n) + '</span><span class="u-txt"><b>' + esc(u.title) +
        "</b><small>заданий с проверкой: " + U.n + "</small></span></a>";
    }).join("") + "</div>";
  }
  function coursesView(v, h) {
    var spaceId = (/space=(\d+)/.exec(h) || [])[1];
    var sp = spaceId ? spaceById(spaceId) : null;
    var one = CAT.courses.length === 1;
    var cards = CAT.courses.map(function (c) {
      return '<details class="course-card"' + (one ? " open" : "") + '><summary>' + (c.cover ? '<img class="cc-cover" src="' + esc(c.cover) + '" alt="" loading="lazy">' : '<span class="cc-ic">' + EN.icon("book") + "</span>") + '<span class="cc-t"><b>' + esc(c.title) +
        "</b><small>" + c.units.length + " модулей · " + courseStat(c) + ' упражнений с проверкой</small></span><span class="cc-chev" aria-hidden="true"></span></summary>' +
        unitTiles(c) + "</details>";
    }).join("");
    var c = CAT.courses.filter(function (x) { return x.id === ((sp && sp.course) || CAT.courses[0].id); })[0] || CAT.courses[0];
    var list = sp ? sp.members.map(function (id) { return D.byId[id]; }).filter(Boolean) : D.students;
    var opts = '<option value="">Все ученики</option>' + D.spaces.map(function (p) { return '<option value="' + p.id + '"' + (sp && sp.id === p.id ? " selected" : "") + ">" + esc(p.name) + "</option>"; }).join("");
    var th = "<tr><th>Ученик</th>" + c.units.map(function (u) { return '<th class="num" title="' + esc(u.title) + '">' + esc(u.n) + "</th>"; }).join("") +
      '<th class="num">Курс</th><th>Был(а)</th><th class="num">Время</th></tr>';
    var rows = list.map(function (s) {
      return '<tr><td><a href="#s=' + s.id + '">' + esc(s.name) + "</a></td>" + c.units.map(function (u) {
        var U = UNITS[c.id + "/" + u.id], p = s.prog[c.id + "/" + u.id], pct = p && U.t ? Math.round(100 * p.best / U.t) : 0;
        return '<td class="num cell ' + pctCls(pct) + '" title="' + esc(u.title) + (p ? ": заданий " + p.done + " из " + U.n + ", попыток " + p.attempts : ": не начат") + '">' + (p ? pct + "%" : "·") + "</td>";
      }).join("") + '<td class="num"><b>' + coursePct(s, c.id) + "%</b></td><td>" + esc(when(s.last_seen_at)) + '</td><td class="num">' + dur(s.total_seconds) + "</td></tr>";
    }).join("");
    v.innerHTML = head("Курсы", "Откройте курс, чтобы увидеть модули; материалы открываются так же, как у учеников.") +
      '<div class="course-list">' + cards + "</div>" +
      '<section class="page"><div class="row-btns"><h2 style="margin:0">Прогресс учеников · ' + esc(c.title) + '</h2><select id="pr-space">' + opts + "</select></div>" +
      '<p class="note-s">Процент — доля верных ответов по всем заданиям модуля (лучшая попытка). Наведите на ячейку — число заданий и попыток; нажмите на имя — все ответы.</p>' +
      (list.length ? '<div class="scroll"><table class="tbl prog">' + th + rows + "</table></div>" : '<p class="empty">Здесь пока нет учеников.</p>') + "</section>";
    $("#pr-space", v).addEventListener("change", function (e) { location.hash = e.target.value ? "courses&space=" + e.target.value : "courses"; });
  }

  /* ---------------- задания: список работ и конструктор в три шага ---------------- */
  function targets(hw) {
    return hw.targets.map(function (t) {
      if (t[0] === "space") { var sp = spaceById(t[1]); return sp ? esc(sp.name) : ""; }
      var s = D.byId[t[1]]; return s ? esc(s.name) : "";
    }).filter(Boolean).join(", ");
  }
  function exTitle(id) {
    var x = EXMAP[id];
    return x ? "Модуль " + esc(x.unit.n) + " · " + esc(PAGE_T[x.page.id] || x.page.title) + (x.let ? " · " + esc(x.let) : "") : esc(id);
  }
  function tasksView(v, h) {
    if (/(^|&)new/.test(h)) return composer(v, h);
    var arch = /(^|&)archive/.test(h);
    v.innerHTML = '<div class="t-head"><div><h1 class="page-title">Задания</h1><p class="lead">Домашние работы из базы тестов курса: ученики выполняют их в своём кабинете, результаты приходят в «Домашние работы».</p></div>' +
      '<a class="btn big" href="#tasks&new">+ Новое задание</a></div>' +
      '<div class="seg"><a href="#tasks"' + (arch ? "" : ' class="on"') + '>Активные</a><a href="#tasks&archive"' + (arch ? ' class="on"' : "") + ">Архив</a></div>" +
      '<div id="hw-made"><p class="lead">Загрузка…</p></div>';
    loadHw().then(function () {
      var box = $("#hw-made", v), list = HW.filter(function (x) { return !!x.archived_at === arch; });
      if (!list.length) {
        box.innerHTML = arch ? '<div class="page empty-state"><p>В архиве пусто.</p></div>' :
          '<div class="page empty-state"><div class="es-ic">' + EN.icon("list") + "</div><h2>Пока нет заданий</h2><p>Соберите домашнюю работу из упражнений курса и назначьте её ученику, нескольким ученикам или целому классу.</p>" +
          '<a class="btn big" href="#tasks&new">+ Новое задание</a></div>';
        return;
      }
      box.innerHTML = '<div class="hw-rows">' + list.map(function (hw) {
        var sub = hw.students.filter(function (x) { return x.submitted_at; }), all = hw.students.length;
        var avg = sub.length ? Math.round(sub.reduce(function (a, x) { return a + (x.total ? 100 * x.score / x.total : 0); }, 0) / sub.length) : null;
        var fresh = sub.filter(function (x) { return !x.seen_at; }).length;
        var late = hw.due_at && new Date(hw.due_at.replace(" ", "T") + "+03:00") < new Date();
        return '<div class="hw-row page"><div class="hw-main"><a class="hw-title" href="#homework&hw=' + hw.id + '">' + esc(hw.title) + "</a>" +
          '<div class="hw-meta"><span>' + EN.icon("users") + targets(hw) + "</span><span>" + EN.icon("list") + hw.items.length + " упр.</span>" +
          (hw.due_at ? '<span class="' + (late ? "late" : "") + '">до ' + esc(day(hw.due_at)) + "</span>" : "<span>без срока</span>") + "<span>создано " + esc(when(hw.created_at)) + "</span></div></div>" +
          '<div class="hw-prog"><div class="hw-pl"><b>' + sub.length + "</b> из " + all + " сдали" + (fresh ? ' <span class="badge">' + fresh + "</span>" : "") +
          (avg != null ? ' · средний <span class="sc ' + pctCls(avg) + '">' + avg + "%</span>" : "") + '</div><div class="mini-bar"><i class="hi" style="width:' + (all ? Math.round(100 * sub.length / all) : 0) + '%"></i></div></div>' +
          '<div class="hw-acts"><a class="btn sm" href="#homework&hw=' + hw.id + '">Результаты</a><a class="btn sm ghost" href="#tasks&new&from=' + hw.id + '" title="Новая работа с теми же упражнениями">Повторить</a>' +
          '<button class="btn sm plain" type="button" data-arch="' + hw.id + '" data-on="' + (arch ? 0 : 1) + '">' + (arch ? "Вернуть" : "В архив") + "</button></div></div>";
      }).join("") + "</div>";
      $$("[data-arch]", box).forEach(function (b) {
        b.addEventListener("click", function () {
          var on = +b.getAttribute("data-on");
          act("t_hw_archive", { id: +b.getAttribute("data-arch"), on: on }, on ? "Работа в архиве — ученики её больше не видят" : "Работа снова активна").then(function (r) { if (r.ok) route(); });
        });
      });
    });
  }

  // конструктор: 1 — упражнения, 2 — ученики, 3 — срок и отправка; справа — закреплённая сводка
  var CMP = null;
  function composer(v, h) {
    var from = +((/from=(\d+)/.exec(h) || [])[1] || 0), spq = (/space=(\d+)/.exec(h) || [])[1], stq = (/student=(\d+)/.exec(h) || [])[1];
    var key = h;
    if (!CMP || CMP.key !== key) {
      CMP = { key: key, step: 1, course: CAT.courses[0].id, unit: null, q: "", items: [], spaces: {}, students: {}, title: "", due: "", dueKind: "none", note: "", titleTouched: false };
      if (spq) CMP.spaces[spq] = true;
      if (stq) CMP.students[stq] = true;
      var src = from && HW ? HW.filter(function (x) { return x.id === from; })[0] : null;
      if (src) { CMP.items = src.items.map(function (it) { return it.ex; }).filter(function (id) { return EXMAP[id]; }); CMP.title = src.title; CMP.titleTouched = true; CMP.note = src.note || ""; CMP.course = src.course; }
    }
    if (from && !HW) { loadHw().then(function () { CMP = null; composer(v, h); }); return; }
    var C = CAT.courses.filter(function (x) { return x.id === CMP.course; })[0] || CAT.courses[0];
    if (!CMP.unit) CMP.unit = (CMP.items.length && EXMAP[CMP.items[0]] ? EXMAP[CMP.items[0]].unit.id : C.units[0].id);
    v.innerHTML = '<div class="crumbs"><a href="#tasks">Задания</a> › Новое задание</div><h1 class="page-title">Новое задание</h1>' +
      '<div class="cmp"><div class="cmp-main"><ol class="stepper">' + ["Упражнения", "Ученики", "Срок и отправка"].map(function (t, i) {
        return '<li class="' + (CMP.step === i + 1 ? "on" : CMP.step > i + 1 ? "done" : "") + '"><button type="button" data-step="' + (i + 1) + '"><span>' + (CMP.step > i + 1 ? "✓" : i + 1) + "</span>" + t + "</button></li>";
      }).join("") + '</ol><div id="cmp-step"></div><div class="cmp-nav"></div></div><aside class="cmp-sum page" id="cmp-sum"></aside></div>';
    var stepBox = $("#cmp-step", v), sum = $("#cmp-sum", v), nav = $(".cmp-nav", v);

    function recipients() {
      var ids = {};
      Object.keys(CMP.spaces).forEach(function (sid) { var sp = spaceById(sid); if (sp) sp.members.forEach(function (m) { ids[m] = 1; }); });
      Object.keys(CMP.students).forEach(function (s) { ids[s] = 1; });
      return Object.keys(ids).filter(function (s) { return D.byId[s]; });
    }
    function answers() { return CMP.items.reduce(function (a, id) { return a + (EXMAP[id] ? EXMAP[id].n : 0); }, 0); }
    function autoTitle() {
      if (CMP.titleTouched) return;
      var units = {}, pages = {};
      CMP.items.forEach(function (id) { var x = EXMAP[id]; if (x) { units[x.unit.n] = 1; pages[PAGE_T[x.page.id] || x.page.title] = 1; } });
      var u = Object.keys(units).sort(), p = Object.keys(pages);
      CMP.title = !u.length ? "" : (u.length === 1 ? "Модуль " + u[0] : "Модули " + u[0] + "–" + u[u.length - 1]) + (p.length === 1 ? " · " + p[0] : "");
    }
    function toggle(id) {
      var i = CMP.items.indexOf(id);
      if (i >= 0) CMP.items.splice(i, 1); else CMP.items.push(id);
      autoTitle();
    }

    /* сводка справа */
    function paintSum() {
      var rc = recipients(), n = CMP.items.length;
      sum.innerHTML = '<label class="sum-title">Название работы<input id="cmp-title" maxlength="200" value="' + esc(CMP.title) + '" placeholder="Например: Модуль 2 · Тесты"></label>' +
        '<div class="sum-h"><b>Упражнения</b><span>' + n + (n ? " · ответов " + answers() : "") + "</span></div>" +
        (n ? '<ol class="sum-items">' + CMP.items.map(function (id, i) {
          var x = EXMAP[id];
          return '<li><span class="si-t"><b>' + exTitle(id) + '</b><small>' + esc(x ? x.ins : "") + '</small></span><span class="si-a">' +
            '<button type="button" data-up="' + i + '" title="Выше"' + (i ? "" : " disabled") + ">↑</button>" +
            '<button type="button" data-down="' + i + '" title="Ниже"' + (i < n - 1 ? "" : " disabled") + ">↓</button>" +
            '<button type="button" data-rm="' + esc(id) + '" title="Убрать">×</button></span></li>';
        }).join("") + "</ol>" : '<p class="sum-empty">Добавьте упражнения из списка слева.</p>') +
        '<div class="sum-h"><b>Ученики</b><span>' + (rc.length ? rc.length : "не выбраны") + "</span></div>" +
        (rc.length ? '<div class="sum-who">' + Object.keys(CMP.spaces).map(function (sid) { var sp = spaceById(sid); return sp ? '<span class="chip-s">' + esc(sp.name) + "</span>" : ""; }).join("") +
          Object.keys(CMP.students).map(function (s) { var x = D.byId[s]; return x ? '<span class="chip-s">' + esc(x.name) + "</span>" : ""; }).join("") + "</div>" : "") +
        '<div class="sum-h"><b>Срок</b><span>' + (CMP.due ? esc(day(CMP.due + " 12:00:00")) : "без срока") + "</span></div>" +
        '<button class="btn big wide" type="button" id="cmp-go"' + (n && rc.length ? "" : " disabled") + ">Назначить" + (rc.length ? " · " + rc.length + " " + plural(rc.length, "ученику", "ученикам", "ученикам") : "") + "</button>" +
        (n && !rc.length ? '<p class="note-s">Осталось выбрать учеников — шаг 2.</p>' : "");
      var ti = $("#cmp-title", sum);
      ti.addEventListener("input", function () { CMP.title = ti.value; CMP.titleTouched = true; });
      sum.querySelectorAll("[data-rm]").forEach(function (b) { b.addEventListener("click", function () { toggle(b.getAttribute("data-rm")); paint(); }); });
      sum.querySelectorAll("[data-up],[data-down]").forEach(function (b) {
        b.addEventListener("click", function () {
          var i = +(b.getAttribute("data-up") || b.getAttribute("data-down")), j = b.hasAttribute("data-up") ? i - 1 : i + 1;
          var t = CMP.items[i]; CMP.items[i] = CMP.items[j]; CMP.items[j] = t; paintSum();
        });
      });
      $("#cmp-go", sum).addEventListener("click", submit);
    }

    /* шаг 1: упражнения — модули сверху, упражнения модуля списком, поиск по всему курсу */
    function exRow(id, n, lt, ins, page) {
      var on = CMP.items.indexOf(id) >= 0;
      return '<div class="ex-row' + (on ? " on" : "") + '" data-id="' + esc(id) + '"><button class="ex-add" type="button" data-tg="' + esc(id) + '" aria-pressed="' + on + '" title="' + (on ? "Убрать из работы" : "Добавить в работу") + '">' + (on ? "✓" : "+") + "</button>" +
        '<div class="ex-txt" data-tg="' + esc(id) + '">' + (lt ? '<b class="ex-let">' + esc(lt) + "</b> " : "") + esc(ins) + '<small>' + (page ? page + " · " : "") + n + " " + plural(n, "ответ", "ответа", "ответов") + "</small></div>" +
        '<button class="btn sm plain" type="button" data-pv="' + esc(id) + '">Просмотр</button></div>';
    }
    function step1() {
      var U = C.units.filter(function (u) { return u.id === CMP.unit; })[0] || C.units[0];
      var cnt = function (u) { var k = 0; u.pages.forEach(function (p) { p.ex.forEach(function (e) { if (CMP.items.indexOf(e[0]) >= 0) k++; }); }); return k; };
      var body = "";
      if (CMP.q) {
        var q = CMP.q.toLowerCase(), hits = 0;
        C.units.forEach(function (u) {
          var rows = "";
          u.pages.forEach(function (p) { p.ex.forEach(function (e) {
            if ((e[3] + " " + e[2] + " " + u.title + " " + (PAGE_T[p.id] || "")).toLowerCase().indexOf(q) >= 0) { rows += exRow(e[0], e[1], e[2], e[3], PAGE_T[p.id] || p.title); hits++; }
          }); });
          if (rows) body += '<div class="ex-group"><div class="ex-gh"><b>Модуль ' + esc(u.n) + " · " + esc(u.title) + "</b></div>" + rows + "</div>";
        });
        body = '<p class="note-s">Найдено: ' + hits + "</p>" + (body || '<p class="empty">Ничего не нашлось — попробуйте другое слово.</p>');
      } else {
        body = U.pages.filter(function (p) { return p.ex.length; }).sort(function (a, b) { return (a.id === "tests" ? -1 : 0) - (b.id === "tests" ? -1 : 0); }).map(function (p) {
          var all = p.ex.every(function (e) { return CMP.items.indexOf(e[0]) >= 0; });
          return '<div class="ex-group"><div class="ex-gh"><b>' + esc(PAGE_T[p.id] || p.title) + '</b><small>' + p.ex.length + " упр.</small>" +
            '<button class="btn sm ' + (all ? "plain" : "ghost") + '" type="button" data-all="' + esc(p.id) + '">' + (all ? "Убрать все" : "Добавить все") + "</button></div>" +
            p.ex.map(function (e) { return exRow(e[0], e[1], e[2], e[3]); }).join("") + "</div>";
        }).join("");
      }
      stepBox.innerHTML = '<div class="cmp-tools">' + (CAT.courses.length > 1 ? '<select id="cmp-course">' + CAT.courses.map(function (c) { return '<option value="' + esc(c.id) + '"' + (c.id === C.id ? " selected" : "") + ">" + esc(c.title) + "</option>"; }).join("") + "</select>" : "") +
        '<input class="filter" id="cmp-q" type="search" placeholder="Поиск по всем упражнениям курса: present perfect, vocabulary, weather…" value="' + esc(CMP.q) + '"></div>' +
        (CMP.q ? "" : '<div class="unit-strip">' + C.units.map(function (u) {
          var k = cnt(u);
          return '<button type="button" class="u-pill' + (u.id === U.id ? " on" : "") + '" data-unit="' + esc(u.id) + '" title="' + esc(u.title) + '"><b>' + esc(u.n) + "</b><span>" + esc(u.title) + "</span>" + (k ? "<i>" + k + "</i>" : "") + "</button>";
        }).join("") + "</div>") + '<div class="ex-list">' + body + "</div>";
      var qi = $("#cmp-q", stepBox), t0 = null;
      qi.addEventListener("input", function () { clearTimeout(t0); t0 = setTimeout(function () { CMP.q = qi.value.trim(); step1(); var x = $("#cmp-q", stepBox); x.focus(); x.setSelectionRange(x.value.length, x.value.length); }, 200); });
      var cs = $("#cmp-course", stepBox); if (cs) cs.addEventListener("change", function () { CMP.course = cs.value; CMP.unit = null; CMP.items = []; composer(v, h); });
      stepBox.querySelectorAll("[data-unit]").forEach(function (b) { b.addEventListener("click", function () { CMP.unit = b.getAttribute("data-unit"); step1(); }); });
      stepBox.querySelectorAll("[data-all]").forEach(function (b) {
        b.addEventListener("click", function () {
          var p = U.pages.filter(function (x) { return x.id === b.getAttribute("data-all"); })[0];
          var all = p.ex.every(function (e) { return CMP.items.indexOf(e[0]) >= 0; });
          p.ex.forEach(function (e) { var i = CMP.items.indexOf(e[0]); if (all && i >= 0) CMP.items.splice(i, 1); if (!all && i < 0) CMP.items.push(e[0]); });
          autoTitle(); paint();
        });
      });
      stepBox.querySelectorAll("[data-tg]").forEach(function (b) { b.addEventListener("click", function () { toggle(b.getAttribute("data-tg")); paint(); }); });
      stepBox.querySelectorAll("[data-pv]").forEach(function (b) { b.addEventListener("click", function () { preview(b.getAttribute("data-pv")); }); });
    }

    /* шаг 2: ученики — пространства целиком и отдельные ученики */
    function step2() {
      var spc = D.spaces.map(function (p) {
        var on = !!CMP.spaces[p.id];
        return '<button type="button" class="pick-card' + (on ? " on" : "") + '" data-sp="' + p.id + '"><span class="pc-chk">' + (on ? "✓" : "") + '</span><span><b>' + esc(p.name) + "</b><small>" + KIND[p.kind] + " · " +
          p.members.length + " " + plural(p.members.length, "ученик", "ученика", "учеников") + "</small></span></button>";
      }).join("");
      var inSpace = {};
      Object.keys(CMP.spaces).forEach(function (sid) { var sp = spaceById(sid); if (sp) sp.members.forEach(function (m) { inSpace[m] = sp.name; }); });
      var stl = D.students.map(function (s) {
        var on = !!CMP.students[s.id], via = inSpace[s.id];
        return '<button type="button" class="pick-st' + (on || via ? " on" : "") + '" data-st="' + s.id + '"' + (via && !on ? ' title="Уже получит через «' + esc(via) + '»"' : "") + '><span class="pc-chk">' + (on || via ? "✓" : "") + "</span>" +
          EN.avatar(s.name, s.avatar, "sm") + "<span>" + esc(s.name) + (via && !on ? "<small>через «" + esc(via) + "»</small>" : "") + "</span></button>";
      }).join("");
      stepBox.innerHTML = (D.spaces.length ? '<div class="pick-sec"><div class="ex-gh"><b>Классы</b><small>работу получат все ученики класса</small></div><div class="pick-grid">' + spc + "</div></div>" : "") +
        '<div class="pick-sec"><div class="ex-gh"><b>Ученики</b><small>' + D.students.length + '</small><button class="btn sm ghost" type="button" data-allst>Выбрать всех</button></div>' +
        (D.students.length > 8 ? '<input class="filter" id="pick-q" type="search" placeholder="Найти ученика…">' : "") +
        (D.students.length ? '<div class="pick-list">' + stl + "</div>" : '<p class="empty">Нет учеников — добавьте их в разделе «Ученики».</p>') + "</div>";
      stepBox.querySelectorAll("[data-sp]").forEach(function (b) { b.addEventListener("click", function () { var k = b.getAttribute("data-sp"); if (CMP.spaces[k]) delete CMP.spaces[k]; else CMP.spaces[k] = true; paint(); }); });
      stepBox.querySelectorAll("[data-st]").forEach(function (b) { b.addEventListener("click", function () { var k = b.getAttribute("data-st"); if (CMP.students[k]) delete CMP.students[k]; else CMP.students[k] = true; paint(); }); });
      var all = $("[data-allst]", stepBox);
      if (all) all.addEventListener("click", function () { var every = D.students.every(function (s) { return CMP.students[s.id]; }); D.students.forEach(function (s) { if (every) delete CMP.students[s.id]; else CMP.students[s.id] = true; }); paint(); });
      var pq = $("#pick-q", stepBox);
      if (pq) pq.addEventListener("input", function () { var q = pq.value.toLowerCase(); stepBox.querySelectorAll(".pick-st").forEach(function (b) { b.hidden = q && b.textContent.toLowerCase().indexOf(q) < 0; }); });
    }

    /* шаг 3: срок, комментарий, проверка перед отправкой */
    function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
    function step3() {
      var quick = [["none", "Без срока", 0], ["1", "Завтра", 1], ["3", "Через 3 дня", 3], ["7", "Через неделю", 7], ["custom", "Своя дата", -1]];
      stepBox.innerHTML = '<div class="pick-sec"><div class="ex-gh"><b>Срок сдачи</b></div><div class="seg due-seg">' + quick.map(function (q) {
        return '<button type="button" data-due="' + q[0] + '" data-d="' + q[2] + '"' + (CMP.dueKind === q[0] ? ' class="on"' : "") + ">" + q[1] + "</button>";
      }).join("") + '</div><input type="date" id="due-date" value="' + esc(CMP.due) + '"' + (CMP.dueKind === "custom" ? "" : " hidden") + "></div>" +
        '<div class="pick-sec"><div class="ex-gh"><b>Комментарий для учеников</b><small>необязательно</small></div><textarea id="cmp-note" rows="4" maxlength="4000" placeholder="Например: сначала повторите правило в разделе «Теория» модуля 2.">' + esc(CMP.note) + "</textarea></div>" +
        '<div class="pick-sec"><div class="ex-gh"><b>Как это будет у ученика</b></div><ul class="dots"><li>Работа появится в его кабинете в «Домашних работах».</li>' +
        "<li>После трёх неверных попыток правильный ответ подставится сам, а задание закроется.</li><li>Ученик нажимает «Отправить учителю» — у вас загорается колокольчик.</li></ul></div>";
      stepBox.querySelectorAll("[data-due]").forEach(function (b) {
        b.addEventListener("click", function () {
          CMP.dueKind = b.getAttribute("data-due"); var d = +b.getAttribute("data-d");
          if (d > 0) { var x = new Date(); x.setDate(x.getDate() + d); CMP.due = iso(x); } else if (d === 0) CMP.due = "";
          paint(); if (CMP.dueKind === "custom") $("#due-date", stepBox).focus();
        });
      });
      $("#due-date", stepBox).addEventListener("change", function (e) { CMP.due = e.target.value; paintSum(); paintSteps(); });
      $("#cmp-note", stepBox).addEventListener("input", function (e) { CMP.note = e.target.value; });
    }

    function paintNav() {
      var rc = recipients().length;
      nav.innerHTML = (CMP.step > 1 ? '<button class="btn plain" type="button" data-go="' + (CMP.step - 1) + '">← Назад</button>' : '<a class="btn plain" href="#tasks">Отмена</a>') +
        (CMP.step < 3 ? '<button class="btn" type="button" data-go="' + (CMP.step + 1) + '"' + ((CMP.step === 1 && !CMP.items.length) || (CMP.step === 2 && !rc) ? " disabled" : "") + ">Далее" + (CMP.step === 1 && CMP.items.length ? " · выбрано " + CMP.items.length : "") + " →</button>" :
          '<button class="btn" type="button" data-submit' + (CMP.items.length && rc ? "" : " disabled") + ">Назначить</button>");
      nav.querySelectorAll("[data-go]").forEach(function (b) { b.addEventListener("click", function () { go(+b.getAttribute("data-go")); }); });
      var sb = $("[data-submit]", nav); if (sb) sb.addEventListener("click", submit);
    }
    function go(n) {
      if (n > 1 && !CMP.items.length) { toast("Сначала добавьте упражнения", true); n = 1; }
      else if (n > 2 && !recipients().length) { toast("Выберите учеников или класс", true); n = 2; }
      CMP.step = n; paint(); scrollTo(0, 0);
    }
    function stepDone(i) { return i === 0 ? CMP.items.length > 0 : i === 1 ? recipients().length > 0 : !!CMP.due; }
    function paintSteps() {
      v.querySelectorAll(".stepper li").forEach(function (li, i) {
        var ok = stepDone(i);
        li.className = (CMP.step === i + 1 ? "on" : "") + (ok ? " done" : "");
        li.querySelector("span").textContent = ok ? "✓" : i + 1;
      });
    }
    function paint() {
      paintSteps();
      [step1, step2, step3][CMP.step - 1]();
      paintSum(); paintNav();
    }
    v.querySelectorAll("[data-step]").forEach(function (b) { b.addEventListener("click", function () { go(+b.getAttribute("data-step")); }); });
    function submit() {
      var title = (CMP.title || "").trim();
      if (!title) { autoTitle(); title = CMP.title || "Домашняя работа"; }
      var items = CMP.items.filter(function (id) { return EXMAP[id]; }).map(function (id) { var x = EXMAP[id]; return { ex: id, n: x.n, unit: x.unit.id, page: x.page.id }; });
      act("t_hw_add", { title: title, note: CMP.note, due: CMP.due, course: C.id, items: items, spaces: Object.keys(CMP.spaces).map(Number), students: Object.keys(CMP.students).map(Number) })
        .then(function (r) {
          if (!r.ok) return;
          CMP = null; HW = null;
          toast("Работа назначена: " + r.students + " " + plural(r.students, "ученик", "ученика", "учеников"));
          location.hash = "tasks";
        });
    }
    paint();
  }
  function plural(n, a, b, c) { n = Math.abs(n) % 100; var k = n % 10; return n > 10 && n < 20 ? c : k > 1 && k < 5 ? b : k === 1 ? a : c; }

  // просмотр упражнения так, как его увидит ученик (с кнопкой «Показать ответы»)
  var PV = {};
  function preview(id) {
    var x = EXMAP[id]; if (!x) return;
    var on = CMP && CMP.items.indexOf(id) >= 0;
    var m = modal('<div class="pv-head"><small>' + exTitle(id) + '</small></div><div class="pv-body"><p class="lead">Загрузка…</p></div>' +
      '<div class="modal-btns pv-btns"><button class="btn" type="button" data-pv-tg>' + (on ? "Убрать из работы" : "Добавить в работу") + '</button><a class="btn plain" href="' + esc(x.page.url) + "#" + esc(id) + '" target="_blank">Открыть на странице курса ↗</a></div>', true);
    var url = x.page.url;
    (PV[url] = PV[url] || fetch(url, { credentials: "same-origin" }).then(function (r) { return r.text(); }).then(function (t) { return new DOMParser().parseFromString(t, "text/html"); }))
      .then(function (doc) {
        var src = doc.getElementById(id), body = m.box.querySelector(".pv-body");
        if (!src) { body.innerHTML = '<p class="empty">Не удалось загрузить упражнение.</p>'; return; }
        var node = document.importNode(src, true); node.removeAttribute("id");
        body.innerHTML = ""; body.appendChild(node);
        EN.setupEx(node, { ns: "pv:", hw: "pv" });
        var rs = node.querySelector("[data-act=reset]"); if (rs) rs.hidden = true;
      });
    m.box.querySelector("[data-pv-tg]").addEventListener("click", function () {
      if (!CMP) return;
      var i = CMP.items.indexOf(id); if (i >= 0) CMP.items.splice(i, 1); else CMP.items.push(id);
      m.close(); route();
    });
  }

  /* ---------------- домашние работы: кто сдал и когда ---------------- */
  function hwStatus(x) {
    if (x.submitted_at) return '<span class="tag on">сдано ' + esc(when(x.submitted_at)) + "</span>";
    if (x.opened_at) return '<span class="tag">в работе' + (x.checks ? " · проверок " + x.checks : "") + "</span>";
    return '<span class="tag off">ещё не открыл(а)</span>';
  }
  function scoreTag(x) {
    if (!x.submitted_at || !x.total) return "";
    var p = Math.round(100 * x.score / x.total);
    return '<span class="sc ' + pctCls(p) + '">' + x.score + " из " + x.total + " · " + p + "%</span>";
  }
  function homeworkView(v, h) {
    var only = +((/hw=(\d+)/.exec(h) || [])[1] || 0);
    v.innerHTML = head("Домашние работы", "Сданные работы появляются здесь; новые отмечены колокольчиком и подсвечены.") + '<div id="hw-box"><p class="lead">Загрузка…</p></div>';
    loadHw().then(function () {
      var box = $("#hw-box", v), sub = [];
      HW.forEach(function (hw) { hw.students.forEach(function (x) { if (x.submitted_at) sub.push({ hw: hw, x: x }); }); });
      sub.sort(function (a, b) { return a.x.submitted_at < b.x.submitted_at ? 1 : -1; });
      var fresh = sub.filter(function (r) { return !r.x.seen_at; }).length;
      EN.setBadge(fresh, "teacher");
      var html = "";
      if (!only) {
        html += '<section class="page"><h2>Сданные работы' + (fresh ? ' <span class="badge">' + fresh + " новых</span>" : "") + "</h2>" + (sub.length ? '<div class="scroll"><table class="tbl hw-in"><tr><th></th><th>Ученик</th><th>Работа</th><th>Сдано</th><th class="num">Результат</th><th class="num">Проверок</th><th></th></tr>' +
          sub.map(function (r) {
            var s = D.byId[r.x.sid]; if (!s) return "";
            return '<tr class="' + (r.x.seen_at ? "" : "new") + '"><td>' + (r.x.seen_at ? "" : '<span class="bell-ic">' + EN.icon("bell") + "</span>") + "</td><td>" + EN.avatar(s.name, s.avatar, "sm") + " " + esc(s.name) + "</td><td>" + esc(r.hw.title) + "</td><td>" + esc(when(r.x.submitted_at)) +
              '</td><td class="num">' + scoreTag(r.x) + '</td><td class="num">' + r.x.checks + '</td><td><a class="btn sm" href="#hw=' + r.hw.id + "&s=" + s.id + '">Открыть</a></td></tr>';
          }).join("") + "</table></div>" : '<p class="empty">Пока никто не сдал работу. Назначить работу — в разделе <a href="#tasks&new">Задания</a>.</p>') + "</section>";
      }
      var list = HW.filter(function (x) { return !x.archived_at && (!only || x.id === only); });
      html += list.map(function (hw) {
        var done = hw.students.filter(function (x) { return x.submitted_at; }).length;
        return '<section class="page"><div class="row-btns"><h2 style="margin:0">' + esc(hw.title) + "</h2><small>" + targets(hw) + " · заданий " + hw.items.length +
          (hw.due_at ? " · срок " + esc(day(hw.due_at)) : "") + " · сдали " + done + " из " + hw.students.length + "</small></div>" +
          (hw.note ? '<p class="note-s">' + esc(hw.note) + "</p>" : "") + '<div class="scroll"><table class="tbl"><tr><th>Ученик</th><th>Статус</th><th class="num">Результат</th><th></th></tr>' +
          hw.students.map(function (x) {
            var s = D.byId[x.sid]; if (!s) return "";
            return "<tr" + (x.submitted_at && !x.seen_at ? ' class="new"' : "") + "><td>" + esc(s.name) + "</td><td>" + hwStatus(x) + '</td><td class="num">' + scoreTag(x) + "</td><td>" +
              (x.submitted_at || x.checks ? '<a class="btn sm ghost" href="#hw=' + hw.id + "&s=" + s.id + '">Ответы</a>' : "") + "</td></tr>";
          }).join("") + "</table></div></section>";
      }).join("") || (only ? '<p class="empty">Работа не найдена.</p>' : "");
      box.innerHTML = html;
    });
  }
  window.EN_BELL = function (n) { if (location.hash.indexOf("homework") >= 0 && n) route(); };

  // одна работа одного ученика: каждое задание — итог, число попыток и все попытки по порядку
  function exLabel(id) {
    var x = EXMAP[id];
    if (!x) return esc(id);
    return "Модуль " + esc(x.unit.n) + " · " + esc(PAGE_T[x.page.id] || x.page.title) + (x.let ? " · " + esc(x.let) : "") + ' <span class="ex-ins">' + esc(x.ins) + "</span>";
  }
  function attemptsHtml(list) {
    var k = 0;
    return list.map(function (a) {
      var items = a.items || a.answers || [];
      if (a.kind === "check") k++;
      var head = a.kind === "show" ? (a.auto ? "Правильные ответы подставлены после 3 неверных попыток" : "Показал(а) ответы") : "Попытка " + k;
      return '<div class="att' + (a.auto ? " auto" : "") + '"><div class="att-head"><b>' + head + "</b> · " + esc(when(a.created_at)) +
        (a.kind === "check" ? ' · <span class="sc ' + pctCls(Math.round(100 * a.score / a.total)) + '">' + a.score + " из " + a.total + "</span>" : "") + "</div>" +
        (a.kind === "check" ? '<ol class="att-items">' + items.map(function (it) {
          return '<li class="' + (it.ok ? "ok" : "bad") + '"><span class="v">' + (it.v !== "" ? esc(it.v) : "<i>пусто</i>") + "</span> " + (it.ok ? "✓" : "✗" + (it.e ? ' <span class="e">верно: ' + esc(it.e) + "</span>" : "")) + "</li>";
        }).join("") + "</ol>" : "") + "</div>";
    }).join("");
  }
  // проверка работы: каждое задание целиком, ответы ученика прямо в тексте, все попытки по вкладкам
  var PGC = {};
  function pageDoc(url) {
    return (PGC[url] = PGC[url] || fetch(url, { credentials: "same-origin" }).then(function (r) { return r.text(); })
      .then(function (t) { return new DOMParser().parseFromString(t, "text/html"); }));
  }
  function itemState(it, att) {
    var checks = att.filter(function (a) { return a.kind === "check"; }), last = checks[checks.length - 1];
    var auto = att.some(function (a) { return a.auto; });
    var st = !last ? "none" : +last.score === +last.total ? "good" : +last.score === 0 ? "bad" : "part";
    if (auto && st !== "good") st = "bad";
    return { checks: checks, last: last, auto: auto, st: st };
  }
  function hwResult(v, hid, sid) {
    v.innerHTML = '<p class="lead">Загрузка…</p>';
    Promise.all([get("t_hw_result", "&hw=" + hid + "&sid=" + sid), HW ? Promise.resolve(HW) : loadHw()]).then(function (x) {
      var r = x[0];
      if (!r.ok) { v.innerHTML = '<p class="empty">Не найдено. <a href="#homework">К домашним работам</a></p>'; return; }
      var st = r.status, s = D.byId[sid] || r.student, hw = (HW || []).filter(function (y) { return y.id === hid; })[0];
      if (hw) hw.students.forEach(function (y) { if (y.sid === sid && st.submitted_at) y.seen_at = y.seen_at || "now"; });
      // ученики этой работы: сдавшие — первыми
      var others = hw ? hw.students.slice().sort(function (a, b) { return (b.submitted_at || "") > (a.submitted_at || "") ? 1 : -1; }) : [];
      var idx = others.map(function (y) { return y.sid; }).indexOf(sid);
      var prev = idx > 0 ? others[idx - 1] : null, next = idx >= 0 && idx < others.length - 1 ? others[idx + 1] : null;
      var states = r.hw.items.map(function (it) { return itemState(it, r.attempts[it.ex] || []); });
      var cnt = { good: 0, part: 0, bad: 0, none: 0 }, checks = 0, autos = 0;
      states.forEach(function (q) { cnt[q.st]++; checks += q.checks.length; if (q.auto) autos++; });
      var pct = st.total ? Math.round(100 * st.score / st.total) : null;
      var side = others.length ? '<aside class="gr-side page"><div class="gr-sh">Ученики · ' + others.length + "</div>" + others.map(function (y) {
        var p = D.byId[y.sid]; if (!p) return "";
        var sc = y.submitted_at && y.total ? Math.round(100 * y.score / y.total) : null;
        return '<a class="gr-st' + (y.sid === sid ? " on" : "") + (y.submitted_at && !y.seen_at ? " new" : "") + '" href="#hw=' + hid + "&s=" + y.sid + '">' + EN.avatar(p.name, p.avatar, "sm") +
          '<span class="gr-sn">' + esc(p.name) + "<small>" + (y.submitted_at ? "сдано " + esc(when(y.submitted_at)) : y.opened_at ? "в работе" : "не открыл(а)") + "</small></span>" +
          (sc != null ? '<span class="sc ' + pctCls(sc) + '">' + sc + "%</span>" : "") + "</a>";
      }).join("") + "</aside>" : "";
      var nav = r.hw.items.map(function (it, i) { return '<a class="qn q-' + states[i].st + '" href="#gq' + i + '" data-q="' + i + '" title="' + exTitle(it.ex).replace(/"/g, "") + '">' + (i + 1) + "</a>"; }).join("");
      v.innerHTML = '<div class="crumbs"><a href="#homework">Домашние работы</a> › <a href="#homework&hw=' + hid + '">' + esc(r.hw.title) + "</a></div>" +
        '<div class="gr' + (side ? "" : " solo") + '">' + side + '<div class="gr-main">' +
        '<div class="gr-head page"><div class="gr-who">' + EN.avatar(s.name, s.avatar) + '<div><h1>' + esc(s.name) + "</h1><p>" + esc(r.hw.title) + " · " +
        (st.submitted_at ? "сдано " + esc(when(st.submitted_at)) : st.opened_at ? "ещё не сдано — в работе" : "ещё не открыто") + "</p></div></div>" +
        (pct != null ? '<div class="gr-score ' + pctCls(pct) + '"><b>' + pct + "%</b><small>" + st.score + " из " + st.total + " ответов</small></div>" : "") +
        '<div class="gr-pn">' + (prev ? '<a class="btn sm plain" href="#hw=' + hid + "&s=" + prev.sid + '" title="Предыдущий ученик">‹</a>' : "") +
        (next ? '<a class="btn sm plain" href="#hw=' + hid + "&s=" + next.sid + '" title="Следующий ученик">›</a>' : "") + "</div></div>" +
        '<div class="gr-stats"><span class="g-good"><b>' + cnt.good + "</b> верно</span><span class=\"g-part\"><b>" + cnt.part + "</b> с ошибками</span>" +
        '<span class="g-bad"><b>' + cnt.bad + "</b> не справился" + (autos ? " · ответ подставлен: " + autos : "") + '</span><span class="g-none"><b>' + cnt.none + "</b> не выполнено</span>" +
        "<span><b>" + checks + "</b> " + plural(checks, "проверка", "проверки", "проверок") + "</span></div>" +
        '<div class="gr-bar"><div class="gr-nav">' + nav + '</div><div class="seg gr-flt"><button type="button" data-f="all" class="on">Все</button><button type="button" data-f="err">С ошибками</button><button type="button" data-f="none">Не выполнено</button></div></div>' +
        '<div id="gr-items"></div><p class="note-s">Ученик видит результат сразу после каждой проверки; после трёх неверных попыток ответ подставлялся сам. ' +
        '<a href="#s=' + sid + '">Все результаты ученика →</a></p></div></div>';
      var box = $("#gr-items", v);
      r.hw.items.forEach(function (it, i) {
        var q = states[i], att = r.attempts[it.ex] || [], X = EXMAP[it.ex];
        var res = q.last ? '<span class="sc ' + pctCls(Math.round(100 * q.last.score / q.last.total)) + '">' + q.last.score + " из " + q.last.total + "</span>" : '<span class="tag off">не выполнено</span>';
        var card = EN.el("section", "page gr-item q-" + q.st, '<div class="gr-ih"><span class="qn q-' + q.st + '">' + (i + 1) + '</span><div class="gr-it"><small>' + exTitle(it.ex) + "</small></div>" +
          '<div class="gr-res">' + res + "<small>" + (q.checks.length ? plural(q.checks.length, "попытка", "попытки", "попыток").replace(/^/, q.checks.length + " ") : "") + (q.auto ? " · ответ подставлен" : "") + "</small></div></div>" +
          '<div class="gr-tabs"></div><div class="gr-body"><p class="lead">Загрузка задания…</p></div>' +
          (att.length ? '<details class="gr-list"><summary>Ответы списком</summary>' + attemptsHtml(att) + "</details>" : "") +
          (X ? '<a class="linkbtn" href="' + esc(X.page.url + "?review=" + sid + "#" + it.ex) + '">Открыть на странице курса →</a>' : ""));
        card.id = "gq" + i; card.setAttribute("data-st", q.st);
        box.appendChild(card);
        if (!X) { card.querySelector(".gr-body").innerHTML = '<p class="empty">Задание не найдено в курсе.</p>'; return; }
        pageDoc(X.page.url).then(function (doc) {
          var src = doc.getElementById(it.ex), body = card.querySelector(".gr-body");
          if (!src) { body.innerHTML = '<p class="empty">Не удалось загрузить задание.</p>'; return; }
          var node = document.importNode(src, true); node.removeAttribute("id");
          $$("details.reveal", node).forEach(function (d) { d.remove(); });
          body.innerHTML = ""; body.appendChild(node);
          var reg = EN.setupEx(node, { ns: "gr:", hw: "gr", locked: true });
          if (!reg) return;
          // вкладки: каждая проверка, подстановка ответа, правильные ответы
          var tabs = [], k = 0;
          att.forEach(function (a) {
            if (a.kind === "check") { k++; tabs.push({ label: "Попытка " + k, sc: a.score + "/" + a.total, cls: +a.score === +a.total ? "a-good" : "a-bad", st: a.st, t: a.created_at }); }
            else if (a.auto) tabs.push({ label: "Подставлен ответ", cls: "a-shown", st: a.st, t: a.created_at });
          });
          tabs.push({ label: "Правильные ответы", cls: "a-key", key: true });
          var cur = q.checks.length ? tabs.map(function (t) { return t.label; }).lastIndexOf("Попытка " + q.checks.length) : tabs.length - 1;
          var tb = card.querySelector(".gr-tabs");
          function show(n) {
            cur = n;
            tb.innerHTML = '<span class="gr-tl">' + (q.checks.length ? "Ответы ученика:" : "Ученик не проверял это задание.") + "</span>" + tabs.map(function (t, j) {
              return '<button type="button" class="rv-att ' + t.cls + (j === cur ? " on" : "") + '" data-t="' + j + '">' + esc(t.label) + (t.sc ? " · <b>" + t.sc + "</b>" : "") +
                (t.t ? " <small>" + esc(when(t.t)) + "</small>" : "") + "</button>";
            }).join("");
            var t = tabs[n];
            if (t.key) reg.showAll(); else reg.apply(t.st);
            // рядом с неверным ответом — правильный вариант, чтобы сразу было видно, в чём ошибка
            $$(".gr-hint", node).forEach(function (x) { x.remove(); });
            if (!t.key) {
              var hint = function (el, after) {
                var ans = (el.getAttribute("data-a") || "").split("|")[0]; if (!ans) return;
                var hs = EN.el("span", "gr-hint", "→ " + esc(ans)); (after || el).insertAdjacentElement("afterend", hs);
              };
              $$("input.gap.bad, select.sel.bad", node).forEach(function (el) { hint(el); });
              $$(".choice", node).forEach(function (el) { if (el.querySelector("button.bad")) hint(el); });
              $$(".order.bad", node).forEach(function (el) { hint(el); });
            }
            node.classList.toggle("gr-key", !!t.key);
            $$("[data-t]", tb).forEach(function (b) { b.addEventListener("click", function () { show(+b.getAttribute("data-t")); }); });
          }
          show(cur);
        });
      });
      // фильтр и навигатор
      $$(".gr-flt [data-f]", v).forEach(function (b) {
        b.addEventListener("click", function () {
          var f = b.getAttribute("data-f");
          $$(".gr-flt button", v).forEach(function (x) { x.classList.toggle("on", x === b); });
          $$(".gr-item", v).forEach(function (c) {
            var q = c.getAttribute("data-st");
            c.hidden = f === "err" ? !(q === "part" || q === "bad") : f === "none" ? q !== "none" : false;
          });
        });
      });
      $$(".gr-nav [data-q]", v).forEach(function (a) {
        a.addEventListener("click", function (e) {
          e.preventDefault();
          var c = $("#gq" + a.getAttribute("data-q"), v); if (!c) return;
          c.hidden = false; c.scrollIntoView({ behavior: "smooth", block: "start" });
          c.classList.add("rv-flash"); setTimeout(function () { c.classList.remove("rv-flash"); }, 1200);
        });
      });
      fetch(API + "me", { credentials: "same-origin", cache: "no-store" }).then(function (y) { return y.json(); }).then(function (y) { if (y.teacher) EN.setBadge(y.teacher.hw_new, "teacher"); });
    });
  }

  /* ---------------- ученик: всё подробно ---------------- */
  var EVT = {
    login: "Вход", logout: "Выход", view: "Открыл(а) страницу", check: "Проверил(а) задание", show: "Показал(а) ответы",
    reset: "Сбросил(а) задание", write: "Писал(а) текст", audio: "Слушал(а) аудио", reveal: "Открыл(а) ответ/ключ", consent: "Дал(а) согласие",
    hw_open: "Открыл(а) домашнюю работу", hw_submit: "Отправил(а) домашнюю работу", profile: "Изменил(а) профиль"
  };
  function exLink(id) {
    var x = EXMAP[id];
    if (!x) return esc(id);
    return '<a href="' + esc(x.page.url) + "#" + esc(id) + '" target="_blank">Модуль ' + esc(x.unit.n) + " · " + esc(x.page.title) + (x.let ? " · " + esc(x.let) : "") + "</a> " +
      '<span class="ex-ins">' + esc(x.ins) + "</span>";
  }
  function studentView(v, id) {
    var s = D.byId[id];
    if (!s) { v.innerHTML = '<p class="empty">Ученик не найден. <a href="#students">К списку</a></p>'; return; }
    v.innerHTML = '<p class="lead">Загрузка…</p>';
    Promise.all([get("t_student", "&id=" + id), HW ? Promise.resolve(HW) : loadHw()]).then(function (rr) {
      var r = rr[0];
      if (!r.ok) { v.innerHTML = '<p class="empty">Не удалось загрузить.</p>'; return; }
      var att = r.attempts, byEx = {};
      att.forEach(function (a) { (byEx[a.ex] = byEx[a.ex] || []).push(a); });
      var checks = att.filter(function (a) { return a.kind === "check"; });
      var wrong = checks.filter(function (a) { return +a.score < +a.total; }).length;
      var tiles = [["Время занятий", dur(s.total_seconds)], ["Входов", r.events.filter(function (e) { return e.type === "login"; }).length],
        ["Сеансов", r.visits.length], ["Заданий начато", r.progress.length], ["Проверок", checks.length], ["Из них с ошибками", wrong]];
      var h = '<div class="crumbs"><a href="#students">Ученики</a></div><div class="st-head"><div><h1 class="page-title">' + EN.avatar(s.name, s.avatar) + " " + esc(s.name) + "</h1>" +
        '<p class="lead">код <b class="code">' + esc(s.code || "—") + "</b>" + (s.email ? " · " + esc(s.email) : "") + (s.telegram ? " · " + esc(s.telegram) : "") + " · " + status(s) +
        (s.consent_at ? ' <span class="tag on">согласие ' + esc(when(s.consent_at)) + "</span>" : ' <span class="tag off">согласия ещё нет</span>') + "</p></div>" +
        '<div class="row-btns">' + shareBtns(s) + '<button class="btn plain sm" type="button" data-edit>Изменить</button></div></div>' +
        '<div class="kpis">' + tiles.map(function (t) { return '<div class="kpi"><div class="lbl">' + t[0] + '</div><div class="big">' + t[1] + "</div></div>"; }).join("") + "</div>";
      // домашние работы ученика
      var mine = HW.filter(function (hw) { return !hw.archived_at && hw.students.some(function (x) { return x.sid === id; }); });
      h += '<section class="page"><div class="row-btns"><h2 style="margin:0">Домашние работы</h2><a class="btn sm ghost" href="#tasks&new&student=' + id + '">Задать работу</a></div>' +
        (mine.length ? '<table class="tbl"><tr><th>Работа</th><th>Статус</th><th class="num">Результат</th><th></th></tr>' + mine.map(function (hw) {
          var x = hw.students.filter(function (y) { return y.sid === id; })[0];
          return "<tr><td>" + esc(hw.title) + "</td><td>" + hwStatus(x) + '</td><td class="num">' + scoreTag(x) + '</td><td><a class="btn sm ghost" href="#hw=' + hw.id + "&s=" + id + '">Ответы</a></td></tr>';
        }).join("") + "</table>" : '<p class="empty">Работ пока нет.</p>') + "</section>";
      // рабочее место разбора: задания глазами ученика, с его ответами
      var lastP = r.progress[0], rvUrl = function (ex) { var x = EXMAP[ex]; return x ? x.page.url + "?review=" + id + "#" + ex : null; };
      var liveUrl = s.live_path ? s.live_path + "?review=" + id + "&follow=1" + (s.live_ex ? "#" + s.live_ex : "") : null;
      var openUrl = (s.online && liveUrl) || (lastP && rvUrl(lastP.ex)) || (CAT.courses[0].units[0].pages[0].url + "?review=" + id);
      var followUrl = liveUrl || (lastP && rvUrl(lastP.ex) ? rvUrl(lastP.ex).replace("#", "&follow=1#") : openUrl + "&follow=1");
      h += '<section class="page rv-start"><div><h2>Рабочее место разбора</h2><p>Задания открываются так, как их видит ученик, — с его ответами прямо в тексте ' +
        "задания, отметками верно/неверно и всеми попытками по очереди. На онлайн-занятии включите «Следовать за учеником»: " +
        "страница сама переходит туда, где ученик, и каждые 4 секунды показывает, что он вводит.</p>" +
        '<p class="rv-state">' + (s.online ? '<span class="tag live">● ученик онлайн</span> ' : '<span class="tag">не в сети</span> ') +
        (s.live_path ? "последнее место: " + esc(s.live_path.replace(/^\//, "")) : "") + "</p></div>" +
        '<div class="row-btns"><a class="btn" href="' + esc(openUrl) + '">Открыть разбор</a><a class="btn ghost" href="' + esc(followUrl) + '">Следовать за учеником онлайн</a></div></section>';
      // пространства ученика: можно отметить несколько
      h += '<section class="page"><h2>Классы</h2>' + (D.spaces.length ? '<div class="sp-toggles">' + D.spaces.map(function (p) {
        return '<label class="sp-tg"><input type="checkbox" data-sp="' + p.id + '"' + (s.spaces.indexOf(p.id) >= 0 ? " checked" : "") + "> " +
          '<span class="kind k-' + p.kind + '">' + KIND[p.kind] + "</span> " + esc(p.name) + "</label>";
      }).join("") + "</div>" : '<p class="empty">Классов пока нет — создайте их в разделе «Классы».</p>') + "</section>";
      // прогресс по модулям → заданиям → попыткам
      var prog = {};
      r.progress.forEach(function (p) { prog[p.ex] = p; });
      CAT.courses.forEach(function (c) {
        h += '<section class="page"><h2>' + esc(c.title) + "</h2>";
        c.units.forEach(function (u) {
          var U = UNITS[c.id + "/" + u.id], b = 0, done = 0, att_n = 0;
          u.pages.forEach(function (p) { p.ex.forEach(function (e) { var x = prog[e[0]]; if (x) { b += +x.best; done++; att_n += +x.attempts; } }); });
          var pct = U.t ? Math.round(100 * b / U.t) : 0;
          h += '<details class="unit-d"' + (done ? " open" : "") + "><summary><span class=\"n\">" + esc(u.n) + "</span><b>" + esc(u.title) + '</b><span class="mini-bar"><i class="' + pctCls(pct) + '" style="width:' + pct + '%"></i></span>' +
            '<span class="u-stat">' + (done ? pct + "% · заданий " + done + " из " + U.n + " · проверок " + att_n : "не начат") + "</span></summary>";
          u.pages.forEach(function (p) {
            if (!p.ex.length) return;
            h += "<h4>" + esc(p.title) + ' <a class="rv-link" href="' + esc(p.url) + "?review=" + id + '">Разобрать страницу →</a></h4><table class="tbl ex-t"><tr><th>Задание</th><th class="num">Лучший</th><th class="num">Последний</th><th class="num">Попыток</th><th></th></tr>';
            p.ex.forEach(function (e) {
              var x = prog[e[0]], list = byEx[e[0]] || [];
              h += "<tr" + (x ? "" : ' class="dim"') + "><td>" + (e[2] ? "<b>" + esc(e[2]) + "</b> " : "") + '<span class="ex-ins">' + esc(e[3]) + "</span></td>" +
                '<td class="num">' + (x ? '<span class="sc ' + pctCls(Math.round(100 * x.best / e[1])) + '">' + x.best + "/" + e[1] + "</span>" : "—") + "</td>" +
                '<td class="num">' + (x ? x.last + "/" + e[1] : "—") + '</td><td class="num">' + (x ? x.attempts + (+x.shown ? " · ответы показаны" : "") : "—") + "</td>" +
                '<td class="acts">' + (x ? '<a class="btn sm" href="' + esc(p.url) + "?review=" + id + "#" + esc(e[0]) + '">Разобрать</a>' : "") +
                (list.length ? ' <button class="linkbtn" type="button" data-hist="' + esc(e[0]) + '">история (' + list.length + ")</button>" : "") + "</td></tr>";
            });
            h += "</table>";
          });
          h += "</details>";
        });
        h += "</section>";
      });
      if (r.writings.length) {
        h += '<section class="page"><h2>Письменные работы</h2>' + r.writings.map(function (w) {
          return '<div class="writing-v"><div class="w-meta"><b>' + esc(w.wid) + "</b> · " + w.words + " слов · " + esc(when(w.updated_at)) +
            ' · <a href="' + esc(w.page || "#") + '" target="_blank">страница</a></div><div class="w-text">' + esc(w.text).replace(/\n/g, "<br>") + "</div></div>";
        }).join("") + "</section>";
      }
      h += '<section class="page"><h2>Входы и время</h2>' + (r.visits.length ? '<div class="scroll"><table class="tbl"><tr><th>Начало</th><th>Конец</th><th class="num">Время</th><th class="num">Страниц</th><th>Устройство</th></tr>' +
        r.visits.map(function (x) {
          return "<tr><td>" + esc(when(x.started_at)) + "</td><td>" + esc(when(x.last_at)) + '</td><td class="num">' + dur(x.seconds) + '</td><td class="num">' + x.pages + "</td><td>" +
            ({ phone: "телефон", tablet: "планшет", desktop: "компьютер" }[x.device] || "—") + "</td></tr>";
        }).join("") + "</table></div>" : '<p class="empty">Ученик ещё не занимался.</p>') + "</section>";
      h += '<section class="page"><h2>Журнал действий <small>последние ' + r.events.length + "</small></h2>" + (r.events.length ? '<ul class="timeline">' + r.events.map(function (e) {
        var d = e.data || {}, t = EVT[e.type] || e.type, x = "";
        if (e.type === "check") x = (e.ex ? exLink(e.ex) : "") + ' — <b class="sc ' + pctCls(d.n ? Math.round(100 * d.s / d.n) : 0) + '">' + d.s + " из " + d.n + "</b>" + (d.hw ? " · домашняя работа" : "");
        else if (e.type === "show") { t = d.auto ? "Подставлены верные ответы (3 ошибки)" : t; x = e.ex ? exLink(e.ex) : ""; }
        else if (e.type === "reset" || e.type === "reveal") x = e.ex ? exLink(e.ex) : esc(d.what || "");
        else if (e.type === "view") x = '<a href="' + esc(e.page || "#") + '" target="_blank">' + esc((d.title || e.page || "").split(" · ")[0]) + "</a>";
        else if (e.type === "write") x = esc(e.ex) + " · " + (d.words || 0) + " слов";
        else if (e.type === "audio") x = esc(d.what || "");
        else if (e.type === "hw_submit") x = (d.s != null ? d.s + " из " + d.n : "");
        else if (e.type === "login") x = (d.via === "code" ? "по коду" : "по ссылке") + (d.device ? " · " + ({ phone: "телефон", tablet: "планшет", desktop: "компьютер" }[d.device] || "") : "");
        return '<li class="ev-' + esc(e.type) + '"><time>' + esc(when(e.created_at)) + "</time><span>" + t + (x ? ": " + x : "") + "</span></li>";
      }).join("") + "</ul>" : '<p class="empty">Пока пусто.</p>') + "</section>" +
        '<section class="page danger-zone"><h2>Код и удаление</h2><p>Если код или ссылка попали к посторонним — выдайте новые (старые перестанут работать).</p>' +
        '<div class="row-btns"><button class="btn ghost" type="button" data-relink>Новый код и ссылка</button></div>' +
        '<p>Удаление стирает ученика и все его данные: ответы, попытки, домашние работы, тексты, журнал. Отменить нельзя.</p>' +
        '<button class="btn danger-o" type="button" data-del>Удалить ученика</button></section>';
      v.innerHTML = h;
      bindSend(v);
      $$("[data-sp]", v).forEach(function (c) {
        c.addEventListener("change", function () {
          act("t_member", { space: +c.getAttribute("data-sp"), student: id, on: c.checked ? 1 : 0 }, c.checked ? "Добавлен(а) в класс" : "Убран(а) из класса")
            .then(function (x) { if (!x.ok) c.checked = !c.checked; else load(); });
        });
      });
      v.querySelector("[data-edit]").addEventListener("click", function () { editStudent(s); });
      v.querySelector("[data-relink]").addEventListener("click", function (e) {
        var b = e.target;
        if (!b.classList.contains("armed")) { b.classList.add("armed"); b.textContent = "Нажмите ещё раз — старые код и ссылка перестанут работать"; return; }
        act("t_student_relink", { id: id }, "Новые код и ссылка готовы").then(function (x) { if (x.ok) refresh(); });
      });
      v.querySelector("[data-del]").addEventListener("click", function (e) {
        var b = e.target;
        if (!b.classList.contains("armed")) { b.classList.add("armed"); b.textContent = "Нажмите ещё раз — удалить безвозвратно"; return; }
        act("t_student_delete", { id: id }, "Ученик удалён").then(function (x) { if (x.ok) { location.hash = "students"; refresh(); } });
      });
      $$("[data-hist]", v).forEach(function (b) {
        b.addEventListener("click", function () {
          var ex = b.getAttribute("data-hist");
          modal("<h2>" + esc(s.name) + " · история ответов</h2><p>" + exLink(ex) + "</p>" + attemptsHtml((byEx[ex] || []).slice().reverse()), true);
        });
      });
    });
  }
  function editStudent(s) {
    var m = modal('<h2>Ученик</h2><form id="st-ed" class="stack"><label>ФИО или имя<input name="name" maxlength="200" required value="' + esc(s.name) + '"></label>' +
      '<label>E-mail (необязательно)<input name="email" type="email" maxlength="190" value="' + esc(s.email || "") + '"></label>' +
      '<p class="disclaimer">ⓘ Можно указать просто имя. E-mail нужен только для отправки кода и ссылки письмом.</p>' +
      '<div class="modal-btns"><button class="btn" type="submit">Сохранить</button></div></form>');
    var f = m.box.querySelector("#st-ed");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      act("t_student_update", { id: s.id, name: f.name.value, email: f.email.value }, "Сохранено").then(function (r) { if (r.ok) { m.close(); refresh(); } });
    });
  }

  /* ---------------- профиль ---------------- */
  function profileView(v) {
    var u = EN.me.user;
    v.innerHTML = '<div id="pf"></div>';
    EN.profile($("#pf", v), "teacher", u, function () { location.reload(); });
  }

  /* ---------------- запуск: app.js сообщает, кто вошёл ---------------- */
  window.EN_TEACHER = function (d) {
    if (!d) { app.innerHTML = '<div class="page"><p>Нет связи с сервером. Проверьте интернет и обновите страницу.</p></div>'; return; }
    EN.ctx = { course: "", unit: "", page: "", path: location.pathname };
    EN.log({ t: "view", title: "Кабинет преподавателя" });
    refresh().catch(function () { app.innerHTML = '<div class="page"><p>Не удалось загрузить кабинет. Обновите страницу.</p></div>'; });
  };
})();
