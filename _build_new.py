# -*- coding: utf-8 -*-
"""Génère les 6 nouvelles pages codes + SVG + tier list ASTD pour Zoneblox.
Run depuis le dossier GameNova."""
import io, os
BASE = os.path.dirname(os.path.abspath(__file__))
def W(p, s):
    fp = os.path.join(BASE, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with io.open(fp, "w", encoding="utf-8") as f:
        f.write(s)

DATE_FR = "6 juin 2026"
DATE_ISO = "2026-06-06"
VER = "8"

# slug -> data
GAMES = {
 "all-star-tower-defense": dict(
    name="All Star Tower Defense", emoji="🌟", cat="anime", catlabel="Anime",
    thumb="https://tr.rbxcdn.com/180DAY-9fbd50db5a51699b733c9529ee542d19/768/432/Image/Webp/noFilter",
    universe=4996049426,
    desc="Tower defense d'anime culte : invoquez des personnages inspirés des plus grands animes, placez vos unités et repoussez les vagues d'ennemis. Les codes offrent des Gemmes et de la Poussière d'étoile.",
    card="Tower defense d'anime culte : invoquez vos personnages, placez vos unités et repoussez les vagues. Codes : Gemmes et Poussière d'étoile.",
    redeem="Cliquez sur l'icône Paramètres (⚙️) puis le champ « Enter Code Here »",
    similar=[("anime-vanguards","⚔️","Anime Vanguards"),("anime-defenders","🗡️","Anime Defenders"),("toilet-tower-defense","🚽","Toilet Tower Defense")],
    tierlist=True,
    codes=[
      ("cosmicrebel","🎁 2 700 Gemmes + 170 Poussière d'étoile"),
      ("omgupdate2026","🎁 2 700 Gemmes + 170 Poussière d'étoile (niveau 50+)"),
      ("UpdateThisWeek","🎁 500 Gemmes + 150 Poussière d'étoile (niveau 40+)"),
      ("fordanielxd","🎁 67 Gemmes + 67 Poussière d'étoile (niveau 100+)"),
    ]),
 "anime-champions-simulator": dict(
    name="Anime Champions Simulator", emoji="🌌", cat="anime", catlabel="Anime",
    thumb="https://tr.rbxcdn.com/180DAY-9d4be137161ea266ba1c2c6f28832e21/768/432/Image/Webp/noFilter",
    universe=None,
    desc="Simulateur d'anime du créateur d'Anime Fighters Simulator : collectionnez et entraînez de puissants champions, explorez la galaxie et affrontez des boss. Les codes offrent Diamants, Médailles Premium et Boosts.",
    card="Collectionnez et entraînez de puissants champions d'anime à travers la galaxie. Codes : Diamants, Médailles Premium et Boosts.",
    redeem="Cliquez sur l'icône Boutique 🛒 puis l'icône oiseau (Twitter)",
    similar=[("anime-vanguards","⚔️","Anime Vanguards"),("blox-fruits","🍎","Blox Fruits"),("pet-simulator-99","🐹","Pet Simulator 99")],
    tierlist=False,
    codes=[
      ("GearGoals","💎 50 Médailles Premium, Invocations Beach, Boosts 250 %"),
      ("HappyMonday","💎 1 000 Diamants, Boosts, Poussière de Rune"),
      ("ShowUp","💎 Boosts, Diamants et Poussière de Rune"),
      ("HappyThanksgiving","💎 Boosts, Poussière de Rune, Médailles Premium"),
      ("TheGames","💎 1 000 Diamants, Poussière de Rune, Boosts"),
      ("GamesShutdown","💎 Invocations Beach, Boosts 250 %, Médailles Premium"),
      ("SummerSunday","💎 Invocations et ressources diverses"),
    ]),
 "sonic-speed-simulator": dict(
    name="Sonic Speed Simulator", emoji="💨", cat="simulator", catlabel="Simulateur",
    thumb="https://tr.rbxcdn.com/180DAY-82939a396600a61e4abadd92664f8d83/768/432/Image/Webp/noFilter",
    universe=None,
    desc="Le simulateur de vitesse officiel Sonic : courez, montez de niveau, débloquez de nouveaux mondes et collectionnez des skins de personnages Sonic. Les codes offrent Chao, boosts et tickets de course.",
    card="Courez à toute vitesse, débloquez des mondes et collectionnez les skins Sonic. Codes : Chao, boosts et tickets de course.",
    redeem="Ouvrez la Boutique à droite puis l'onglet « Redeem Codes »",
    similar=[("pet-simulator-99","🐹","Pet Simulator 99"),("grow-a-garden","🌱","Grow a Garden"),("bee-swarm-simulator","🐝","Bee Swarm Simulator")],
    tierlist=False,
    codes=[
      ("race2win","🎫 100 Tickets de course"),
      ("1billion","🐾 Pet « You »"),
      ("thumbsup","🐾 Chao Bloxian"),
      ("thankyouchao","🐾 Chao Gratitude"),
      ("Hooray50k","⚡ Boost Triple XP (30 min)"),
      ("40kThankYou","💍 Boost Anneaux (30 min)"),
      ("Amazing35","🧲 Boost Aimant (30 min)"),
      ("25k","🧲 Boost Aimant (30 min)"),
    ]),
 "tower-defense-simulator": dict(
    name="Tower Defense Simulator", emoji="🧟", cat="battle", catlabel="Combat",
    thumb="https://tr.rbxcdn.com/180DAY-f4a7603e22db5d7a43e966fe145a96e1/768/432/Image/Webp/noFilter",
    universe=None,
    desc="Le tower defense de référence sur Roblox : placez vos tours, coopérez avec vos amis et repoussez des vagues de zombies pour débloquer de nouvelles unités. Aucun code actif confirmé actuellement.",
    card="Placez vos tours, coopérez et repoussez les vagues de zombies pour débloquer de nouvelles unités. Aucun code actif confirmé pour l'instant.",
    redeem="Cliquez sur l'icône Twitter/X en bas de l'écran",
    similar=[("toilet-tower-defense","🚽","Toilet Tower Defense"),("anime-defenders","🗡️","Anime Defenders"),("blade-ball","⚔️","Blade Ball")],
    tierlist=False,
    codes=[]),
 "project-slayers": dict(
    name="Project Slayers", emoji="🌸", cat="anime", catlabel="Anime",
    thumb="https://tr.rbxcdn.com/180DAY-612b92100da817e8dc2bb8fd35ce117e/768/432/Image/Webp/noFilter",
    universe=5956785391,
    desc="RPG d'action inspiré de Demon Slayer : devenez pourfendeur de démons ou démon, maîtrisez les souffles et les arts démoniaques, et explorez un vaste monde ouvert. Aucun code actif confirmé actuellement.",
    card="RPG d'action inspiré de Demon Slayer : souffles, arts démoniaques et monde ouvert. Aucun code actif confirmé pour l'instant.",
    redeem="Cliquez sur l'icône Cadeau 🎁 à gauche de l'écran",
    similar=[("blox-fruits","🍎","Blox Fruits"),("king-legacy","⚡","King Legacy"),("type-soul","💀","Type Soul")],
    tierlist=False,
    codes=[]),
 "the-strongest-battlegrounds": dict(
    name="The Strongest Battlegrounds", emoji="👊", cat="battle", catlabel="Combat",
    thumb="https://tr.rbxcdn.com/180DAY-c947df5b221c30672c3591247a8c6495/768/432/Image/Webp/noFilter",
    universe=10449761463,
    desc="Le jeu de combat phénomène inspiré de One-Punch Man : entraînez-vous, débloquez des styles surpuissants et affrontez les autres joueurs dans des combats PVP nerveux. Le jeu n'utilise pas de codes de récompense classiques.",
    card="Jeu de combat inspiré de One-Punch Man : styles surpuissants et PVP nerveux. Pas de codes de récompense dans ce jeu.",
    redeem="Ce jeu n'utilise pas de codes de récompense",
    similar=[("blade-ball","⚔️","Blade Ball"),("untitled-boxing-game","🥊","Untitled Boxing Game"),("rivals","🎯","Rivals")],
    tierlist=False,
    codes=[]),
}

# Ordre d'affichage (le plus chaud d'abord)
ORDER = ["all-star-tower-defense","anime-champions-simulator","sonic-speed-simulator",
         "tower-defense-simulator","project-slayers","the-strongest-battlegrounds"]

def esc(s):
    return s.replace("&","&amp;")

def codes_table(codes):
    rows = []
    for code, reward in codes:
        rows.append(
          '<tr><td><div class="code-cell"><span class="code-value">%s</span></div></td>'
          '<td><span class="reward-tag">%s</span></td>'
          '<td><button class="copy-btn" onclick="copyCode(this,\'%s\')">Copier</button></td></tr>'
          % (code, reward, code))
    return "\n".join(rows)

def codes_block(g):
    name = g["name"]; codes = g["codes"]; redeem = g["redeem"]
    steps = (
      '<h3 style="margin:24px 0 14px">Comment utiliser les codes %s</h3>'
      '<div class="redeem-steps">'
      '<div class="redeem-step"><div class="step-num">1</div><div class="step-icon">🚀</div><h4>Lancer le jeu</h4><p>Ouvrez Roblox et lancez le jeu</p></div>'
      '<div class="redeem-step"><div class="step-num">2</div><div class="step-icon">📋</div><h4>Ouvrir les codes</h4><p>%s</p></div>'
      '<div class="redeem-step"><div class="step-num">3</div><div class="step-icon">⌨️</div><h4>Saisir le code</h4><p>Collez le code exactement (sensible à la casse)</p></div>'
      '<div class="redeem-step"><div class="step-num">4</div><div class="step-icon">🎁</div><h4>Valider</h4><p>Validez — la récompense arrive aussitôt</p></div>'
      '</div>' % (name, redeem)
    )
    if codes:
        n = len(codes)
        banner = (
          '<div class="codes-live-banner"><div class="pulse-dot"></div><div>'
          '<strong>%d codes actifs trouvés</strong><br>'
          '<span>Dernière vérification : %s — vérifié chaque jour.</span></div></div>'
          '<div class="notice notice-info"><span class="notice-icon">ℹ️</span>'
          '<p><strong>Comment utiliser :</strong> ouvrez le jeu, ouvrez la zone des codes, '
          'saisissez le code exactement (sensible à la casse) puis validez.</p></div>' % (n, DATE_FR)
        )
        table = (
          '<div class="codes-section" style="margin-top:24px">'
          '<div class="codes-status-bar">'
          '<div class="status-dot green" style="width:8px;height:8px;border-radius:50%%;background:#00c853;box-shadow:0 0 8px #00c853;animation:pulse 2s infinite"></div>'
          '<span style="font-size:.85rem;font-weight:600;color:#00c853">Codes actifs — fonctionnent en juin 2026</span>'
          '<span style="font-size:.78rem;color:var(--text-muted);margin-left:auto">Vérifié le %s</span></div>'
          '<div style="overflow-x:auto"><table class="codes-table"><thead><tr><th>Code</th><th>Récompense</th><th>Action</th></tr></thead><tbody>%s</tbody></table></div></div>'
          % (DATE_FR, codes_table(codes))
        )
        return banner + steps + table
    else:
        notice = (
          '<div class="notice notice-warn" style="border-radius:var(--radius);padding:14px 18px;'
          'background:rgba(255,159,28,.08);border-left:3px solid #ff9f1c;display:flex;gap:10px;align-items:flex-start;margin-bottom:8px">'
          '<span class="notice-icon">⚠️</span>'
          '<p><strong>Aucun code actif confirmé actuellement</strong> pour %s. '
          'Cette page est vérifiée chaque jour : dès qu\'un nouveau code officiel sort, il apparaîtra ici. '
          'Pensez à ajouter cette page à vos favoris.</p></div>' % name
        )
        return notice + steps

def tl_button(g):
    if not g.get("tierlist"):
        return ""
    slug_tl = "all-star-tower-defense"
    return ('<div style="margin-top:14px"><a href="/tier-list/%s.html" '
            'style="display:inline-flex;align-items:center;gap:8px;background:var(--bg-card);border:1px solid var(--border);'
            'color:var(--text-primary);font-weight:700;padding:10px 18px;border-radius:var(--radius-sm);text-decoration:none">'
            '📊 Voir la tier list %s (meilleures unités) →</a></div>' % (slug_tl, g["name"]))

def sidebar_similar(similar):
    out = []
    for s, e, nm in similar:
        out.append('<a href="/codes/%s.html" style="display:flex;align-items:center;gap:10px;font-size:.85rem;color:var(--text-muted)">%s %s</a>' % (s, e, nm))
    return "\n".join(out)

PAGE = r'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Codes @@NAME@@ (juin 2026) – Tous les codes actifs | Zoneblox</title>
  <meta name="description" content="Codes @@NAME@@ pour juin 2026 : liste vérifiée chaque jour, guide d'utilisation, astuces et vidéos. Récompenses gratuites !">
  <meta name="keywords" content="codes @@NAMELC@@, codes @@NAMELC@@ 2026, @@NAMELC@@ roblox, codes roblox">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0e0b1a">
  <link rel="canonical" href="https://zoneblox.com/codes/@@SLUG@@.html">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎮</text></svg>">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Zoneblox">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:url" content="https://zoneblox.com/codes/@@SLUG@@.html">
  <meta property="og:title" content="Codes @@NAME@@ (juin 2026) – Tous les codes actifs | Zoneblox">
  <meta property="og:description" content="Codes @@NAME@@ pour juin 2026 : liste vérifiée chaque jour, guide d'utilisation, astuces et vidéos. Récompenses gratuites !">
  <meta property="og:image" content="https://zoneblox.com/images/og-cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Article","inLanguage":"fr-FR","headline":"Codes @@NAME@@ (juin 2026) – Tous les codes actifs | Zoneblox","datePublished":"@@ISO@@","dateModified":"@@ISO@@","author":{"@type":"Organization","name":"Zoneblox"},"publisher":{"@type":"Organization","name":"Zoneblox","logo":{"@type":"ImageObject","url":"https://zoneblox.com/images/logo.png"}}}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://zoneblox.com/"},{"@type":"ListItem","position":2,"name":"Tous les codes","item":"https://zoneblox.com/codes/"},{"@type":"ListItem","position":3,"name":"@@NAME@@","item":"https://zoneblox.com/codes/@@SLUG@@.html"}]}
  </script>
  <link rel="stylesheet" href="/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    .codes-live-banner{background:linear-gradient(135deg,rgba(0,200,83,.08),rgba(0,207,255,.06));border:1px solid rgba(0,200,83,.3);border-radius:var(--radius);padding:14px 18px;display:flex;align-items:center;gap:12px;margin-bottom:20px}
    .pulse-dot{width:10px;height:10px;border-radius:50%;background:#00c853;box-shadow:0 0 10px #00c853;animation:pulse 2s infinite;flex-shrink:0}
    .page-tabs{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px;margin-bottom:28px}.page-tab{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:15px 10px;font-size:.95rem;font-weight:700;color:var(--text-muted);cursor:pointer;transition:.15s;text-align:center}.page-tab:hover{color:var(--text-primary);border-color:rgba(162,89,255,.45);transform:translateY(-2px)}.page-tab.active{background:linear-gradient(135deg,var(--accent),var(--accent2));border-color:transparent;color:#fff;box-shadow:0 6px 18px rgba(162,89,255,.35)}.tab-content{display:none}.tab-content.active{display:block}
    .tips-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
    .videos-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
    .video-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}
    .video-embed{position:relative;padding-top:56.25%;background:#000}
    .video-embed iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:none}
    .video-label{padding:12px 16px;font-size:.85rem;font-weight:600;color:var(--text-primary)}
  </style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <nav class="nav-inner">
      <a href="/" class="nav-logo"><div class="logo-icon">🎮</div><span>Zone<span class="gradient-text">blox</span></span></a>
      <ul class="nav-links">
        <li><a href="/">Accueil</a></li>
        <li><a href="/codes/" class="active">Tous les codes</a></li>
        <li><a href="/about.html">À propos</a></li>
      </ul>
      <div class="nav-right"><button class="nav-toggle"><span></span><span></span><span></span></button></div>
    </nav>
  </div>
</header>

<div class="game-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Accueil</a><span class="sep">›</span><a href="/codes/">Tous les codes</a><span class="sep">›</span><span>@@NAME@@</span></div>
    <div class="game-hero-inner">
      <img data-game="@@SLUG@@" src="@@THUMB@@" onerror="this.onerror=null;this.src='/images/games/@@SLUG@@.svg'" alt="@@NAME@@" class="game-hero-thumb" style="object-fit:cover;width:200px;height:112px;border-radius:var(--radius)">
      <div class="game-hero-info">
        <h1>Codes @@NAME@@ <span class="gradient-text">juin 2026</span></h1>
        <div class="game-meta">
          <div class="game-meta-item">@@METACODES@@</div>
          <div class="game-meta-item">🕐 Mis à jour le <strong>@@DATE@@</strong></div>
          <div class="game-meta-item">🏷️ <strong>@@CATLABEL@@</strong></div>
        </div>
        <p class="desc">@@DESC@@</p>
        @@TLBUTTON@@
      </div>
    </div>
  </div>
</div>

<div class="container" style="margin-top:20px">
  <div class="ad-banner ad-leaderboard"><span>728 × 90 — Google AdSense</span></div>
</div>

<section class="section">
  <div class="container">
    <div class="page-with-sidebar">
      <div class="main-col">
        <div class="page-tabs">
          <div class="page-tab active" data-tab="codes">🎁 Codes</div>
          <div class="page-tab" data-tab="tips">💡 Astuces</div>
          <div class="page-tab" data-tab="videos">🎬 Vidéos</div>
          <div class="page-tab" data-tab="faq">❓ FAQ</div>
        </div>

        <div class="tab-content active" id="tab-codes">
          @@CODESBLOCK@@
        </div>

        <div class="tab-content" id="tab-tips">
          <div class="tips-grid"><div class="tip-card"><div class="tip-num">1</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Utilisez les codes dès leur sortie</h4><p style="font-size:.85rem">Beaucoup de codes Roblox expirent en quelques jours. Dès qu'un nouveau code apparaît, utilisez-le sans attendre pour ne pas le rater.</p></div>
<div class="tip-card"><div class="tip-num">2</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Copiez-collez sans erreur</h4><p style="font-size:.85rem">Les codes sont sensibles à la casse. Copiez-les directement depuis Zoneblox plutôt que de les retaper, pour éviter les fautes.</p></div>
<div class="tip-card"><div class="tip-num">3</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Revenez chaque jour</h4><p style="font-size:.85rem">Nous vérifions et mettons à jour les codes quotidiennement. Ajoutez cette page à vos favoris pour ne jamais manquer une récompense gratuite.</p></div></div>
        </div>

        <div class="tab-content" id="tab-videos">
          <p style="margin-bottom:20px;font-size:.9rem">Les vidéos les plus populaires du moment sur @@NAME@@.</p>
          <div class="videos-grid">
            <div class="video-card"><div class="video-embed">
              <a href="https://www.youtube.com/results?search_query=@@NAMEQ@@+Roblox" target="_blank" rel="noopener" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:10px;background:linear-gradient(135deg,#1a1a30,#0a0a1a);color:#fff;text-decoration:none;font-weight:700;font-size:.95rem"><span style="font-size:2.4rem">▶</span> Voir les vidéos sur YouTube</a>
            </div><div class="video-label">🎬 @@NAME@@ — vidéos populaires</div></div>
          </div>
        </div>

        <div class="tab-content" id="tab-faq">
          <div style="display:flex;flex-direction:column;gap:14px"><details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Quels sont les codes @@NAME@@ actifs ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Tous les codes actifs sont listés dans l'onglet Codes ci-dessus, avec leur récompense. Ils sont vérifiés chaque jour.</p></details>
<details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Pourquoi mon code @@NAME@@ ne fonctionne pas ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Les codes sont sensibles à la casse : copiez-collez-les exactement. S'il ne marche toujours pas, le code a peut-être expiré ou a déjà été utilisé sur votre compte.</p></details>
<details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Où trouver les nouveaux codes @@NAME@@ ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Sur Zoneblox, mis à jour chaque jour, ainsi que sur le Discord et le compte X (Twitter) officiels de @@NAME@@.</p></details></div>
        </div>
      </div>

      <aside>
        <div class="sidebar-sticky">
          <div class="ad-banner ad-rectangle" style="height:250px;width:100%;background:var(--bg-secondary);border:1px dashed rgba(255,255,255,0.1);border-radius:var(--radius);display:flex;align-items:center;justify-content:center;font-size:.75rem;color:var(--text-muted)">300 × 250<br>Google AdSense</div>
          <div class="sidebar-widget">
            <h3 style="font-size:.95rem;margin-bottom:14px;border-bottom:1px solid var(--border);padding-bottom:10px">📧 Recevez les nouveaux codes en premier</h3>
            <p style="font-size:.82rem;margin-bottom:12px">Abonnez-vous et soyez averti dès qu'un nouveau code @@NAME@@ sort.</p>
            <form class="newsletter-form" onsubmit="return false">
              <input type="email" placeholder="votre@email.com" required>
              <button type="submit">🔔 Me prévenir</button>
            </form>
          </div>
          <div class="sidebar-widget">
            <h3 style="font-size:.95rem;margin-bottom:14px;border-bottom:1px solid var(--border);padding-bottom:10px">🎮 Jeux similaires</h3>
            <div style="display:flex;flex-direction:column;gap:8px">
              @@SIMILAR@@
            </div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-bottom" style="padding:24px 0">
      <span>© 2026 Zoneblox — Non affilié à Roblox Corporation.</span>
      <span><a href="/about.html">À propos</a> · <a href="/privacy.html">Confidentialité</a> · <a href="/terms.html">Conditions</a> · <a href="/contact.html">Contact</a></span>
    </div>
  </div>
</footer>
<script src="/js/main.js?v=@@VER@@"></script>
<script>
function switchTab(tabId){document.querySelectorAll('.page-tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));var b=document.querySelector('[data-tab="'+tabId+'"]');var p=document.getElementById('tab-'+tabId);if(b)b.classList.add('active');if(p)p.classList.add('active');}
document.querySelectorAll('.page-tab').forEach(function(tab){tab.addEventListener('click',function(){switchTab(tab.dataset.tab);});});
</script>
</body>
</html>
'''

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#221a44"/><stop offset="1" stop-color="#0a0a1a"/>
    </linearGradient>
  </defs>
  <rect width="480" height="270" fill="url(#g)"/>
  <circle cx="240" cy="118" r="74" fill="rgba(162,89,255,0.18)"/>
  <text x="240" y="118" font-size="84" text-anchor="middle" dominant-baseline="central">@@EMOJI@@</text>
  <text x="240" y="225" font-size="@@FS@@" fill="#f0f0ff" font-family="Arial, Helvetica, sans-serif" font-weight="700" text-anchor="middle">@@NAME@@</text>
</svg>
'''

def build_page(slug, g):
    metacodes = ('✅ <strong>%d codes actifs</strong>' % len(g["codes"])) if g["codes"] else 'ⓘ <strong>Aucun code actif</strong>'
    html = PAGE
    repl = {
      "@@NAME@@": g["name"],
      "@@NAMELC@@": g["name"].lower(),
      "@@NAMEQ@@": g["name"].replace(" ", "+"),
      "@@SLUG@@": slug,
      "@@ISO@@": DATE_ISO,
      "@@DATE@@": DATE_FR,
      "@@THUMB@@": g["thumb"],
      "@@METACODES@@": metacodes,
      "@@CATLABEL@@": g["catlabel"],
      "@@DESC@@": g["desc"],
      "@@TLBUTTON@@": tl_button(g),
      "@@CODESBLOCK@@": codes_block(g),
      "@@SIMILAR@@": sidebar_similar(g["similar"]),
      "@@VER@@": VER,
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    return html

def build_svg(slug, g):
    nm = g["name"]
    fs = "26" if len(nm) <= 18 else ("21" if len(nm) <= 24 else "17")
    return SVG.replace("@@EMOJI@@", g["emoji"]).replace("@@FS@@", fs).replace("@@NAME@@", esc(nm))

for slug in ORDER:
    g = GAMES[slug]
    W("codes/%s.html" % slug, build_page(slug, g))
    W("images/games/%s.svg" % slug, build_svg(slug, g))
    print("page+svg:", slug)

# ---------- TIER LIST ASTD ----------
ASTD_TL = r'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Star Tower Defense Tier List (juin 2026) — Meilleures unités | Zoneblox</title>
  <meta name="description" content="All Star Tower Defense Tier List (juin 2026) : les meilleures unités classées selon leurs DPS et leur polyvalence (Infini, Histoire, Raids). Tier list communautaire indicative mise à jour régulièrement sur Zoneblox.">
  <meta name="keywords" content="all star tower defense tier list, astd best units, meilleures unités astd, tier list astd 2026">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0e0b1a">
  <link rel="canonical" href="https://zoneblox.com/tier-list/all-star-tower-defense.html">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎮</text></svg>">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Zoneblox">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:url" content="https://zoneblox.com/tier-list/all-star-tower-defense.html">
  <meta property="og:title" content="All Star Tower Defense Tier List (juin 2026) — Meilleures unités | Zoneblox">
  <meta property="og:description" content="Les meilleures unités d'All Star Tower Defense classées, méta juin 2026.">
  <meta property="og:image" content="https://zoneblox.com/images/og-cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"ItemList","name":"All Star Tower Defense Tier List — Unités","itemListElement":[{"@type":"ListItem","position":1,"name":"Super God Koku"},{"@type":"ListItem","position":2,"name":"Renitsu (District)"},{"@type":"ListItem","position":3,"name":"Zazashi (PERFECTION)"},{"@type":"ListItem","position":4,"name":"King Vegu"},{"@type":"ListItem","position":5,"name":"Earing"}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://zoneblox.com/"},{"@type":"ListItem","position":2,"name":"Tier lists","item":"https://zoneblox.com/tier-list/"},{"@type":"ListItem","position":3,"name":"All Star Tower Defense Tier List","item":"https://zoneblox.com/tier-list/all-star-tower-defense.html"}]}
  </script>
  <link rel="stylesheet" href="/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    .tier-row{display:flex;gap:14px;margin-bottom:12px;align-items:stretch}
    .tier-badge{flex-shrink:0;width:74px;display:flex;align-items:center;justify-content:center;border-radius:12px;font-size:1.3rem;font-weight:900;text-align:center;padding:10px 6px}
    .tier-items{flex:1;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:8px 10px;display:flex;flex-wrap:wrap;align-items:center}
    .chip{display:inline-block;background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:7px 13px;margin:4px;font-size:.9rem;font-weight:600;color:var(--text-primary)}
    .tier-s{background:#ff4d4d;color:#fff}.tier-a{background:#ff9f1c;color:#3a2300}.tier-b{background:#ffd93d;color:#3a2f00}
  </style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <nav class="nav-inner">
      <a href="/" class="nav-logo"><div class="logo-icon">🎮</div><span>Zone<span class="gradient-text">blox</span></span></a>
      <ul class="nav-links"><li><a href="/">Accueil</a></li><li><a href="/codes/">Tous les codes</a></li><li><a href="/tier-list/" class="active">Tier lists</a></li><li><a href="/about.html">À propos</a></li></ul>
      <div class="nav-right"><button class="nav-toggle"><span></span><span></span><span></span></button></div>
    </nav>
  </div>
</header>

<div class="game-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Accueil</a><span class="sep">›</span><a href="/tier-list/">Tier lists</a><span class="sep">›</span><span>All Star Tower Defense</span></div>
    <h1>All Star Tower Defense Tier List <span class="gradient-text">juin 2026</span></h1>
    <p class="desc" style="max-width:760px;margin-top:8px">Le classement des meilleures unités d'All Star Tower Defense pour juin 2026, selon leurs DPS, leur polyvalence et leur efficacité en mode Infini, Histoire, Raids et Gauntlet. Tier list communautaire indicative, mise à jour régulièrement.</p>
    <div style="margin-top:16px"><a href="/codes/all-star-tower-defense.html" style="display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:700;padding:11px 20px;border-radius:var(--radius-sm);text-decoration:none">🎁 Voir les codes All Star Tower Defense →</a></div>
  </div>
</div>

<div class="container" style="margin-top:20px"><div class="ad-banner ad-leaderboard"><span>728 × 90 — Google AdSense</span></div></div>

<section class="section">
  <div class="container" style="max-width:900px">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;flex-wrap:wrap">
      <span style="font-size:.8rem;color:var(--text-muted)">🕐 Mis à jour le <strong style="color:var(--text-primary)">@@DATE@@</strong></span>
      <span style="font-size:.8rem;color:var(--text-muted)">·</span>
      <span style="font-size:.8rem;color:var(--text-muted)">Classement des unités (DPS &amp; polyvalence)</span>
    </div>

    <div class="tier-row"><div class="tier-badge tier-s">S</div><div class="tier-items"><span class="chip">Super God Koku</span><span class="chip">Renitsu (District)</span><span class="chip">Zazashi (PERFECTION)</span><span class="chip">King Vegu</span></div></div>
    <div class="tier-row"><div class="tier-badge tier-a">A</div><div class="tier-items"><span class="chip">Earing</span><span class="chip">Ikki Potent (Hollow)</span><span class="chip">Buddha Navy</span><span class="chip">Slayer Mage</span></div></div>
    <div class="tier-row"><div class="tier-badge tier-b">B</div><div class="tier-items"><span class="chip">Igros (Elite Knight)</span><span class="chip">Akazo (Destructive)</span><span class="chip">Borul (Sage)</span></div></div>

    <div class="notice notice-info" style="margin-top:18px;border-radius:var(--radius);padding:14px 18px;background:rgba(0,150,255,0.08);border-left:3px solid #0096ff;display:flex;gap:10px;align-items:flex-start">
      <span style="font-size:1.1rem">ℹ️</span>
      <p style="font-size:.85rem;color:var(--text-muted)">Les meilleures unités sont celles qui délivrent le plus de DPS sur tous les modes : Super God Koku (placement colline) et Renitsu (placement sol) dominent le méta juin 2026. Pensez à associer un farmer, des carries maximisés et un bon support. Tier list communautaire indicative, qui évolue à chaque mise à jour et rééquilibrage.</p>
    </div>

    <div style="margin-top:22px;text-align:center"><a href="/tier-list/" style="display:inline-flex;align-items:center;gap:8px;background:var(--bg-card);border:1px solid var(--border);color:var(--text-primary);font-weight:700;padding:11px 20px;border-radius:var(--radius-sm);text-decoration:none">📊 Toutes les tier lists Roblox →</a></div>
  </div>
</section>

<footer class="site-footer"><div class="container"><div class="footer-bottom" style="padding:24px 0"><span>© 2026 Zoneblox — Non affilié à Roblox Corporation.</span><span><a href="/about.html">À propos</a> · <a href="/privacy.html">Confidentialité</a> · <a href="/terms.html">Conditions</a> · <a href="/contact.html">Contact</a></span></div></div></footer>
<script src="/js/main.js?v=@@VER@@"></script>
</body>
</html>
'''
W("tier-list/all-star-tower-defense.html", ASTD_TL.replace("@@DATE@@", DATE_FR).replace("@@VER@@", VER))
print("tier-list: all-star-tower-defense")
print("DONE build pages")

