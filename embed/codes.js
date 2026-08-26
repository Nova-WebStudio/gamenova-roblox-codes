/*! Zoneblox — widget "Codes du jour" embeddable.
 * Usage : <script async src="https://zoneblox.com/embed/codes.js?game=blox-fruits"></script>
 * Affiche les codes a jour d'un jeu Roblox + lien retour vers Zoneblox.
 * Auto-contenu, sans dependance, styles inline (aucun conflit avec le site hote). */
(function () {
  "use strict";
  var BASE = "https://zoneblox.com";
  var me = document.currentScript;
  if (!me) {
    var ss = document.getElementsByTagName("script");
    for (var i = ss.length - 1; i >= 0; i--) {
      if (ss[i].src && ss[i].src.indexOf("/embed/codes.js") !== -1) { me = ss[i]; break; }
    }
  }
  if (!me) return;
  var q = (me.src.split("?")[1] || "");
  var params = {};
  q.split("&").forEach(function (p) { var kv = p.split("="); if (kv[0]) params[kv[0]] = decodeURIComponent(kv[1] || ""); });
  var slug = (params.game || me.getAttribute("data-game") || "").trim();

  var box = document.createElement("div");
  box.setAttribute("data-zoneblox-widget", slug || "1");
  me.parentNode.insertBefore(box, me.nextSibling);

  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
    return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]; }); };

  function render(html) { box.innerHTML =
    '<div style="all:initial;display:block;font-family:Inter,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;'
    + 'max-width:460px;background:#141024;color:#f4f2fb;border:1px solid #2a2440;border-radius:16px;'
    + 'overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.25);line-height:1.4">' + html + '</div>'; }

  function shell(inner, name, verified, count) {
    var head =
      '<div style="display:flex;align-items:center;gap:10px;padding:12px 14px;background:linear-gradient(135deg,#7c3aed,#22d3ee)">'
      + '<span style="font-size:1.1rem">🎁</span>'
      + '<strong style="font-size:1rem;color:#fff;flex:1">Codes ' + esc(name) + '</strong>'
      + (count != null ? '<span style="background:rgba(0,0,0,.25);color:#fff;font-size:.72rem;font-weight:700;padding:3px 9px;border-radius:20px">' + count + ' actifs</span>' : '')
      + '</div>';
    var foot =
      '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;'
      + 'padding:10px 14px;border-top:1px solid #2a2440;background:#0f0b1a">'
      + '<span style="font-size:.72rem;color:#a79fc4">' + (verified ? "🔄 Vérifié le " + esc(verified) : "") + '</span>'
      + '<a href="' + BASE + '/codes-' + esc(slug) + '.html" target="_blank" rel="noopener" '
      + 'style="font-size:.8rem;font-weight:700;color:#22d3ee;text-decoration:none">Tous les codes sur Zoneblox →</a>'
      + '</div>';
    return head + '<div style="padding:10px 14px">' + inner + '</div>' + foot;
  }

  function copyBtn(code) {
    return '<button data-code="' + esc(code) + '" '
      + 'style="cursor:pointer;background:#211a38;border:1px solid #2a2440;color:#f4f2fb;font-size:.72rem;'
      + 'font-weight:700;padding:5px 9px;border-radius:8px">📋</button>';
  }

  function paint(game) {
    if (!game) {
      render(shell('<p style="margin:0;font-size:.85rem;color:#a79fc4">Codes indisponibles pour l\'instant. '
        + '<a href="' + BASE + '/tous-les-codes.html" target="_blank" rel="noopener" style="color:#22d3ee;text-decoration:none">Voir tous les codes →</a></p>', slug || "Roblox"));
      return;
    }
    var inner;
    if (!game.codes || !game.codes.length) {
      inner = '<p style="margin:0;font-size:.85rem;color:#a79fc4">Aucun code actif confirmé pour le moment. '
        + 'On vérifie chaque jour — reviens bientôt.</p>';
    } else {
      inner = game.codes.map(function (c) {
        return '<div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #221c3a">'
          + '<code style="font-family:ui-monospace,Menlo,Consolas,monospace;background:#211a38;color:#fff;'
          + 'font-size:.82rem;font-weight:700;padding:4px 8px;border-radius:6px;white-space:nowrap">' + esc(c.code) + '</code>'
          + '<span style="flex:1;font-size:.78rem;color:#c9c2e4">' + esc(c.reward) + '</span>'
          + copyBtn(c.code) + '</div>';
      }).join("");
    }
    render(shell(inner, game.name || slug, game.verified, game.count));
    box.addEventListener("click", function (e) {
      var b = e.target.closest ? e.target.closest("button[data-code]") : null;
      if (!b) return;
      var t = b.getAttribute("data-code");
      try { navigator.clipboard.writeText(t); b.textContent = "✓"; setTimeout(function () { b.textContent = "📋"; }, 1200); } catch (x) {}
    });
  }

  // rendu provisoire
  render(shell('<p style="margin:0;font-size:.82rem;color:#a79fc4">Chargement des codes…</p>', slug || "Roblox"));

  fetch(BASE + "/data/codes.json", { cache: "default" })
    .then(function (r) { return r.json(); })
    .then(function (d) { paint(d && d.games ? d.games[slug] : null); })
    .catch(function () { paint(null); });
})();
