/* Zoneblox — Encart "Prochains évènements & admin abuses" (accueil)
   Statique-compatible : lit data/events.json, calcule les comptes à rebours
   côté client et se met à jour chaque seconde. N'invente aucune heure :
   n'affiche un décompte que si une occurrence est réellement calculable. */
(function () {
  "use strict";
  var BOX = document.getElementById("eventsBox");
  if (!BOX) return;

  var KIND = {
    "restock":     { emoji: "🛒", label: "Restock" },
    "event":       { emoji: "🎉", label: "Event" },
    "update":      { emoji: "🔄", label: "Mise à jour" },
    "admin-abuse": { emoji: "🎬", label: "Admin abuse" }
  };

  // Prochaine occurrence (ms epoch) ou null si non calculable.
  function nextOccurrence(ev, now) {
    if (ev.recurrence && ev.recurrence.everyMinutes) {
      var step = ev.recurrence.everyMinutes * 60000;
      // alignToClock : occurrences alignées sur l'horloge UTC (:00, :05, :30…)
      return Math.ceil((now + 1) / step) * step;
    }
    if (ev.datetime) {
      var t = Date.parse(ev.datetime);
      if (!isNaN(t) && t > now) return t;
    }
    return null;
  }

  function fmtCountdown(ms) {
    if (ms < 0) ms = 0;
    var s = Math.floor(ms / 1000);
    var d = Math.floor(s / 86400); s -= d * 86400;
    var h = Math.floor(s / 3600);  s -= h * 3600;
    var m = Math.floor(s / 60);    s -= m * 60;
    function p(n) { return (n < 10 ? "0" : "") + n; }
    if (d > 0) return d + "j " + p(h) + "h " + p(m) + "m";
    if (h > 0) return p(h) + ":" + p(m) + ":" + p(s);
    return p(m) + ":" + p(s);
  }

  function esc(x) {
    return String(x == null ? "" : x).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function linkFor(ev) {
    var s = ev.source || "";
    if (/^codes\//.test(s)) return "/" + s;
    return s || "#";
  }

  function render(data) {
    var events = (data && data.events) || [];
    var now = Date.now();

    var timed = [];   // avec décompte
    var untimed = []; // sans horaire fixe
    events.forEach(function (ev) {
      var next = nextOccurrence(ev, now);
      if (next) { ev._next = next; timed.push(ev); }
      else { untimed.push(ev); }
    });
    timed.sort(function (a, b) { return a._next - b._next; });

    var html = "";

    if (timed.length) {
      html += '<div class="zb-ev-sub">⏱️ Comptes à rebours en direct</div>';
      html += '<div class="zb-ev-grid">';
      timed.forEach(function (ev) {
        var k = KIND[ev.kind] || { emoji: "📌", label: ev.kind || "" };
        html +=
          '<a class="zb-ev-card" href="' + esc(linkFor(ev)) + '">' +
            '<div class="zb-ev-top"><span class="zb-ev-kind">' + k.emoji + " " + esc(k.label) + "</span>" +
              (ev.recurrence ? '<span class="zb-ev-rec">récurrent</span>' : "") + "</div>" +
            '<div class="zb-ev-game">' + esc(ev.game) + "</div>" +
            '<div class="zb-ev-title">' + esc(ev.title) + "</div>" +
            '<div class="zb-ev-cd" data-next="' + ev._next + '" data-rec="' +
              (ev.recurrence ? ev.recurrence.everyMinutes : "") + '">--:--</div>' +
            (ev.reward ? '<div class="zb-ev-reward">' + esc(ev.reward) + "</div>" : "") +
          "</a>";
      });
      html += "</div>";
    }

    if (untimed.length) {
      html += '<div class="zb-ev-sub zb-ev-sub2">🎬 Admin abuses &amp; MAJ — sans horaire officiel</div>';
      html += '<div class="zb-ev-chips">';
      untimed.forEach(function (ev) {
        var k = KIND[ev.kind] || { emoji: "📌", label: ev.kind || "" };
        html +=
          '<a class="zb-ev-chip" href="' + esc(linkFor(ev)) + '" title="' +
            esc(ev.game + " — " + (ev.watch || "surveiller les canaux officiels")) + '">' +
            "<b>" + esc(ev.game) + "</b> " +
            '<span class="zb-ev-chip-k">' + k.emoji + " " + esc(k.label) + "</span>" +
          "</a>";
      });
      html += "</div>";
    }

    if (!timed.length && !untimed.length) {
      html = '<p class="zb-ev-empty">Aucun évènement suivi pour le moment.</p>';
    }

    if (data && data.meta && data.meta.note) {
      html += '<p class="zb-ev-note">ℹ️ ' + esc(data.meta.note) + "</p>";
    }

    BOX.innerHTML = html;
    tick(); // premier affichage immédiat
  }

  // Met à jour tous les décomptes ; recalcule l'occurrence des récurrents.
  function tick() {
    var now = Date.now();
    var nodes = BOX.querySelectorAll(".zb-ev-cd");
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      var next = parseInt(el.getAttribute("data-next"), 10);
      var recMin = parseInt(el.getAttribute("data-rec"), 10);
      if (recMin && now >= next) {
        var step = recMin * 60000;
        next = Math.ceil((now + 1) / step) * step;
        el.setAttribute("data-next", next);
      }
      el.textContent = fmtCountdown(next - now);
      if (next - now <= 60000) el.classList.add("zb-ev-soon");
      else el.classList.remove("zb-ev-soon");
    }
  }

  function boot(data) {
    render(data);
    setInterval(tick, 1000);
  }

  var url = "/data/events.json?cb=" + Math.floor(Date.now() / 60000);
  fetch(url, { headers: { Accept: "application/json" } })
    .then(function (r) { if (!r.ok) throw 0; return r.json(); })
    .then(boot)
    .catch(function () {
      // Dégradation propre : masque l'encart si les données sont indisponibles.
      var sec = document.getElementById("evenements");
      if (sec) sec.style.display = "none";
    });
})();
