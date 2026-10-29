/* Lingvaden English — service worker: приложение (PWA) и работа без сети.
   Страницы: сначала сеть, без сети — из кеша. Файлы оформления и картинки: из кеша, обновляются в фоне.
   API (/api/) и аудио/видео (/media/) не кешируются. Версия кеша — версия сборки. */
var V = "en-{V}";
var CORE = ["/", "/assets/app.css?v={V}", "/assets/app.js?v={V}", "/assets/fonts/fonts.css", "/assets/favicon.svg?v={V}",
            "/how/", "/me/", "/teacher/"];
self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(V).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k !== V; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener("fetch", function (e) {
  var r = e.request, u = new URL(r.url);
  if (r.method !== "GET" || u.origin !== location.origin || u.pathname.indexOf("/api/") === 0 || u.pathname.indexOf("/s/") === 0 ||
      u.pathname.indexOf("/media/") === 0) return;   // аудио/видео: запросы по частям (Range), в кеш не кладём
  if (r.mode === "navigate" || (r.headers.get("accept") || "").indexOf("text/html") >= 0) {
    e.respondWith(fetch(r).then(function (res) {
      // страница курса без входа переадресует на главную: отдаём браузеру переадресацию, в кеш не кладём
      if (res.redirected) return Response.redirect(res.url, 302);
      if (res.ok) { var copy = res.clone(); caches.open(V).then(function (c) { c.put(r, copy); }); }
      return res;
    }).catch(function () { return caches.match(r).then(function (m) { return m || caches.match("/"); }); }));
    return;
  }
  // каталог курсов меняется с каждой сборкой: сначала сеть, без сети — из кеша
  if (u.pathname.indexOf("/assets/catalog.json") === 0) {
    e.respondWith(fetch(r).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(V).then(function (c) { c.put(r, copy); }); }
      return res;
    }).catch(function () { return caches.match(r); }));
    return;
  }
  e.respondWith(caches.match(r).then(function (m) {
    var net = fetch(r).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(V).then(function (c) { c.put(r, copy); }); }
      return res;
    }).catch(function () { return m; });
    return m || net;
  }));
});
