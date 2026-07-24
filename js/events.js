/* Zoneblox — Encart "Prochains évènements & admin abuses" (accueil)
   Statique-compatible : lit data/events.json, calcule les comptes à rebours
   côté client et se met à jour chaque seconde. N'invente aucune heure :
   n'affiche un décompte que si une occurrence est réellement calculable.
   Récurrences supportées :
     - recurrence.everyMinutes (+ alignToClock) : restocks alignés sur l'horloge UTC.
     - recurrence.weekly {dayUTC, hourUTC, minuteUTC, durationMinutes} : events hebdo.
     - datetime : évènement ponctuel (ISO UTC).
   status:"no-fixed-time" => affiché en chip "où surveiller", sans décompte. */
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
  var DOW = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];

  // Retourne {start, endsAt, inProgress, recurring} ou null si non calculable.
  function occurrence(ev, now) {
    var r = ev.recurrence;
    if (r && r.everyMinutes) {
      var step = r.everyMinutes * 60000;
      var start = Math.ceil((now + 1) / step) * step;
      return { start: start, endsAt: 0, inProgress: false, recurring: true };
    }
    if (r && r.weekly) {
      var w = r.weekly;
      var d = new Date(now);
      var target = Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate(),
                            w.hourUTC || 0, w.minuteUTC || 0, 0);
      var delta = ((w.dayUTC - d.getUTCDay()) + 7) % 7;
      target += delta * 86400000;
      if (target <= now) target += 7 * 86400000;
      var dur = (w.durationMinutes || 0) * 60000;
      var prev = target - 7 * 86400000;
      if (dur && now >= prev && now < prev + dur) {
        return { start: prev, endsAt: prev + dur, inProgress: true, recurring: true };
      }
      return { start: target, endsAt: target + dur, inProgress: false, recurring: true };
    }
    if (ev.datetime) {
      var t = Date.parse(ev.datetime);
      if (isNaN(t)) return null;
      var d2 = (ev.durationMinutes || 0) * 60000;
      if (d2 && now >= t && now < t + d2) {
        return { start: t, endsAt: t + d2, inProgress: true, recurring: false };
      }
      if (t > now) return { start: t, endsAt: t + d2, inProgress: false, recurring: false };
      return null; // ponctuel passé => masqué
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

  function fmtWhen(ev) {
    var w = ev.recurrence && ev.recurrence.weekly;
    if (w) {
      var hh = (w.hourUTC < 10 ? "0" : "") + w.hourUTC;
      var mm = (w.minuteUTC || 0) < 10 ? "0" + (w.minuteUTC || 0) : (w.minuteUTC || 0);
      return "chaque " + DOW[w.dayUTC] + " · " + hh + ":" + mm + " UTC";
    }
    if (ev.recurrence && ev.recurrence.everyMinutes) {
      var em = ev.recurrence.everyMinutes;
      return em >= 60 ? "toutes les " + (em / 60) + " h" : "toutes les " + em + " min";
    }
    return "";
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

    var timed = [], untimed = [];
    events.forEach(function (ev) {
      var occ = occurrence(ev, now);
      if (occ) { ev._occ = occ; timed.push(ev); }
      else { untimed.push(ev); }
    });
    // En cours d'abord, puis par imminence.
    timed.sort(function (a, b) {
      if (a._occ.inProgress !== b._occ.inProgress) return a._occ.inProgress ? -1 : 1;
      return (a._occ.inProgress ? a._occ.endsAt : a._occ.start) -
             (b._occ.inProgress ? b._occ.endsAt : b._occ.start);
    });

    var html = "";

    if (timed.length) {
      html += '<div class="zb-ev-sub">⏱️ Comptes à rebours en direct</div>';
      html += '<div class="zb-ev-grid">';
      timed.forEach(function (ev) {
        var k = KIND[ev.kind] || { emoji: "📌", label: ev.kind || "" };
        var occ = ev._occ;
        var when = fmtWhen(ev);
        var w = ev.recurrence && ev.recurrence.weekly;
        html +=
          '<a class="zb-ev-card' + (occ.inProgress ? " zb-ev-live" : "") + '" href="' + esc(linkFor(ev)) + '">' +
            '<div class="zb-ev-top"><span class="zb-ev-kind">' + k.emoji + " " + esc(k.label) + "</span>" +
              (occ.inProgress ? '<span class="zb-ev-badge-live">● en cours</span>'
                              : (occ.recurring ? '<span class="zb-ev-rec">récurrent</span>' : "")) + "</div>" +
            '<div class="zb-ev-game">' + esc(ev.game) + "</div>" +
            '<div class="zb-ev-title">' + esc(ev.title) + "</div>" +
            '<div class="zb-ev-cd" data-slug="' + esc(ev.slug) + '">--:--</div>' +
            '<div class="zb-ev-meta">' +
              (occ.inProgress ? "se termine dans" : (when || "prochain")) +
            "</div>" +
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
    BOX._events = timed; // référence pour tick()
    tick();
  }

  function tick() {
    var now = Date.now();
    var list = BOX._events || [];
    for (var i = 0; i < list.length; i++) {
      var ev = list[i];
      var el = BOX.querySelector('.zb-ev-cd[data-slug="' + cssEsc(ev.slug) + '"]');
      if (!el) continue;
      var occ = occurrence(ev, now); // recalcul (gère le passage d'occurrence)
      if (!occ) { el.textContent = "—"; continue; }
      ev._occ = occ;
      var remain = occ.inProgress ? (occ.endsAt - now) : (occ.start - now);
      el.textContent = fmtCountdown(remain);
      if (remain <= 60000) el.classList.add("zb-ev-soon"); else el.classList.remove("zb-ev-soon");
    }
  }

  function cssEsc(s) { return String(s).replace(/["\\]/g, "\\$&"); }

  var url = "/data/events.json?cb=" + Math.floor(Date.now() / 60000);
  fetch(url, { headers: { Accept: "application/json" } })
    .then(function (r) { if (!r.ok) throw 0; return r.json(); })
    .then(function (data) { render(data); setInterval(tick, 1000); })
    .catch(function () {
      var sec = document.getElementById("evenements");
      if (sec) sec.style.display = "none";
    });
})();
