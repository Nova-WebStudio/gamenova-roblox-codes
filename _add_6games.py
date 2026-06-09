# -*- coding: utf-8 -*-
"""Ajoute 6 nouveaux jeux à Zoneblox (run 2026-06-09)"""
import io, os, re, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
def R(p):
    with io.open(os.path.join(BASE,p), encoding="utf-8") as f: return f.read()
def W(p, s):
    fp = os.path.join(BASE, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with io.open(fp, "w", encoding="utf-8") as f: f.write(s)

DATE_FR  = "9 juin 2026"
DATE_ISO = "2026-06-09"
MONTH    = "juin 2026"

GAMES = [
  dict(
    slug="peroxide", name="Peroxide", emoji="💀", cat="anime", catLabel="Anime",
    placeId="9096881148", universeId=3419284255,
    desc="RPG d'action inspiré de Bleach : devenez Soul Reaper, Hollow ou Quincy, débloquez des techniques maudites et montez en puissance dans des combats dynamiques. Les codes offrent des Product Essence et des Premium Dyes.",
    redeem="cliquez sur l'icône Statistiques (graphique en barres) en haut à gauche, allez dans l'onglet « Settings », saisissez le code dans la case « Code Here » puis appuyez sur Entrée.",
    codes=[
      ("TasteTheRainbow", "🎨 +10 Premium Dye + 20 Product Essence"),
    ],
    similar=[("blox-fruits","🍎","Blox Fruits"),("king-legacy","⚡","King Legacy"),("type-soul","💀","Type Soul")],
    about1="Peroxide est un RPG d'action massivement multijoueur inspiré de l'univers de Bleach : choisissez votre camp (Soul Reaper, Hollow, Arrancar ou Quincy), maîtrisez votre moveset unique et progressez en affrontant d'autres joueurs ou des monstres. Avec plus de 390 millions de visites au compteur, c'est l'un des jeux d'anime les plus joués de Roblox.",
    about2="La progression repose sur le système de Progression de Grade et l'obtention de différentes races/transformations. Les codes vous offrent de la Product Essence (pour améliorer vos équipements) et des Premium Dyes (pour personnaliser votre apparence). Suivez le Discord officiel pour ne rater aucun code.",
    svg1="#2c3e50", svg2="#8e44ad",
  ),
  dict(
    slug="grimoires-era", name="Grimoires Era", emoji="📖", cat="anime", catLabel="Anime",
    placeId="14115013144", universeId=4886369361,
    desc="RPG inspiré de Black Clover : obtenez votre grimoire, maîtrisez votre magie et devenez le Roi Mage. Les codes offrent des Grimoire Spins, Aura Spins, Race Spins et boosts d'XP.",
    redeem="ouvrez le menu (touche M ou bouton Menu), allez dans l'onglet « Info », saisissez le code dans la case de codes puis cliquez sur « Go ».",
    codes=[
      ("SorryShutdown",  "🔮 Grimoire Spins + boosts"),
      ("GGgames",        "🔮 Grimoire Spins + Race Spins"),
      ("SorryBugs3",     "✨ Aura Spins + boosts XP"),
      ("SorryBugs4",     "✨ Aura Spins + Race Spins"),
      ("Guizera",        "🔮 Grimoire Spins gratuits"),
      ("WEAPOLOGIZE",    "⚡ Boosts multiples"),
      ("SorryBugs2",     "🔮 Grimoire Spins + boosts"),
      ("Release",        "🎁 Récompenses de lancement"),
      ("FunzyLabs",      "✨ Boosts XP + Grimoire Spins"),
      ("GrimoiresEra2",  "🔮 Grimoire Spins (mise à jour 2)"),
      ("GameOpen",       "🎉 Récompenses d'ouverture"),
    ],
    similar=[("shindo-life","🌀","Shindo Life"),("anime-vanguards","⚔️","Anime Vanguards"),("attack-on-titan-revolution","⚔️","Attack on Titan Revolution")],
    about1="Grimoires Era est un RPG inspiré de Black Clover : dans ce monde où la magie définit tout, obtenez votre grimoire, développez votre type de magie et gravissez les rangs des chevaliers magiques. Le jeu propose un système de spin pour déterminer votre grimoire, votre race et votre aura, à l'image des meilleurs jeux RNG de Roblox.",
    about2="La progression passe par les quêtes de boss, l'entraînement de votre magie et les donjons coopératifs. Les codes sont particulièrement généreux : ils offrent des Grimoire Spins pour changer votre magie, des Aura Spins pour votre apparence et des boosts XP pour progresser plus vite. Rejoignez le Discord officiel FunzyLabs pour rester informé des nouvelles sorties.",
    svg1="#27ae60", svg2="#f39c12",
  ),
  dict(
    slug="pressure", name="Pressure", emoji="🌊", cat="battle", catLabel="Combat",
    placeId="12411473842", universeId=4367208330,
    desc="Jeu d'horreur coopératif inspiré de DOORS : explorez des couloirs sous-marins angoissants, fuyez les entités et survivez avec vos amis. Les codes offrent des Kroner (monnaie) et des Revive Tokens.",
    redeem="lancez le jeu, cliquez sur l'icône clé/paramètres dans le lobby, trouvez la barre « Codes » sous le volume musical, saisissez le code puis cliquez sur « Submit ».",
    codes=[
      ("YOURTAKINGTOOLONG",       "⏱️ 1 Revive Token"),
      ("MiserableLaunchOnceAgain","🎁 1 Revive Token"),
      ("WasteOfTime",             "💀 2 Revive Tokens"),
      ("SMILEYBOMB!!!",           "💰 500 Kroner"),
    ],
    similar=[("dandys-world","🧸","Dandy's World"),("survive-the-killer","🔪","Survive the Killer"),("99-nights-in-the-forest","🔦","99 Nights in the Forest")],
    about1="Pressure est l'un des jeux d'horreur les plus populaires de Roblox en 2025-2026 : un survival coopératif situé dans une station de recherche sous-marine envahie par des créatures terrifiantes. Inspiré par DOORS et d'autres jeux d'horreur de Roblox, il propose des mécaniques de furtivité, de résolution d'énigmes et de coopération pour survivre.",
    about2="Chaque run dans Pressure est différent : la disposition des couloirs change, les entités réagissent différemment et les ressources à collecter varient. Les Kroner permettent d'acheter des consommables avant chaque partie, et les Revive Tokens sauvent la mise quand votre équipe est en difficulté. Suivez le développeur @YourFriendZeal sur X pour les derniers codes.",
    svg1="#1a2a4a", svg2="#00bfff",
  ),
  dict(
    slug="muscle-legends", name="Muscle Legends", emoji="💪", cat="simulator", catLabel="Simulateur",
    placeId="3623096087", universeId=1268927906,
    desc="Simulateur de musculation Roblox : entraînez-vous, devenez plus fort, débloquez des gymnases et affrontez d'autres joueurs en PvP. Les codes offrent des Gemmes, de la Force et de l'Agilité.",
    redeem="lancez le jeu, cliquez sur le bouton « Codes » à droite de l'écran, tapez le code dans la case « Type Code Here » puis cliquez sur le bouton vert « ENTER ».",
    codes=[
      ("FrostGems10",       "💎 10 000 Gemmes"),
      ("GalaxyCrystal50",   "💎 5 000 Gemmes"),
      ("SpaceGems50",       "💎 5 000 Gemmes"),
      ("EpicReward500",     "💎 500 Gemmes"),
      ("SkyAgility50",      "🏃 500 Agilité"),
      ("Speedy50",          "🏃 250 Agilité"),
      ("MillionWarriors",   "💪 1 500 Force"),
      ("MuscleStorm50",     "💪 1 500 Force"),
      ("SuperMuscle100",    "💪 200 Force"),
      ("MegaLift50",        "💪 250 Force"),
      ("SuperPunch100",     "👊 100 Force"),
    ],
    similar=[("bee-swarm-simulator","🐝","Bee Swarm Simulator"),("pet-simulator-99","🐹","Pet Simulator 99"),("noob-incremental","🧱","Noob Incremental")],
    about1="Muscle Legends est le simulateur de musculation culte de Roblox : cliquez pour vous entraîner, augmentez vos statistiques de Force et d'Agilité, débloquez de nouveaux gymnases de plus en plus puissants et affrontez d'autres joueurs dans des duels PvP. Le jeu propose aussi des modes coopératifs et des défis quotidiens.",
    about2="La progression dans Muscle Legends repose sur l'entraînement régulier, le choix des bons équipements et la collection de Pets qui multiplient vos gains. Les Gemmes permettent d'acheter des boosts et des passes d'entraînement premium. Les codes du jeu sont particulièrement généreux : certains offrent des dizaines de milliers de Gemmes en un seul code !",
    svg1="#e74c3c", svg2="#f39c12",
  ),
  dict(
    slug="anime-dimensions-simulator", name="Anime Dimensions Simulator", emoji="🌌", cat="anime", catLabel="Anime",
    placeId="6938803436", universeId=2655311011,
    desc="Simulateur d'anime où vous collectionnez des personnages légendaires de vos animes préférés et les faites combattre en équipe. Les codes offrent des Gemmes, des Raid Tokens et des boosts d'XP.",
    redeem="cliquez sur l'icône oiseau (Twitter/X) en haut à gauche de l'écran, saisissez le code dans la case puis appuyez sur « Go » ou Entrée.",
    codes=[
      ("MINIUPDATE",   "💎 200 Gemmes + 75 Raid Tokens + Boosts 20 min"),
      ("S2AG2E9",      "💎 Gemmes + Raid Tokens"),
      ("LUC2K2Y8",     "💎 Gemmes + boosts"),
      ("2ESP2E5R",     "💎 Gemmes gratuits"),
      ("DIME2NSI2ON4", "💎 Gemmes + Tokens"),
      ("M2OC2HI0",     "🎁 Récompenses diverses"),
      ("2C2U2T",       "💎 Gemmes gratuits"),
      ("AN2IM2E3",     "💎 Gemmes + Raid Tokens"),
      ("ULTRA",        "💎 100 Gemmes + 100 Raid Tokens + Boosts"),
      ("HALLOWEEN",    "💎 100 Gemmes + 100 Raid Tokens + Boosts"),
    ],
    similar=[("anime-vanguards","⚔️","Anime Vanguards"),("anime-champions-simulator","🌌","Anime Champions Simulator"),("anime-defenders","🗡️","Anime Defenders")],
    about1="Anime Dimensions Simulator est un simulateur d'anime ambitieux où vous constituez une équipe de personnages légendaires issus des plus grands animes (Dragon Ball, Naruto, One Piece, Bleach et bien d'autres). Placez vos combattants sur le terrain, améliorez-les et affrontez des vagues d'ennemis toujours plus puissants dans des raids épiques.",
    about2="La mécanique principale repose sur la collection et l'évolution de vos personnages (jusqu'au rang Ultra Légendaire), la synergie d'équipe et la participation aux raids de boss pour obtenir des matériaux rares. Les codes offrent des Gemmes pour invoquer de nouveaux personnages et des Raid Tokens pour accéder aux donjons premium. Avec plus de 47 codes actifs, c'est l'un des jeux les plus généreux en codes de Roblox.",
    svg1="#6a0dad", svg2="#00cfff",
  ),
  dict(
    slug="ro-ghoul", name="Ro-Ghoul", emoji="👁️", cat="anime", catLabel="Anime",
    placeId="914010731", universeId=914010731,
    desc="RPG d'action inspiré de Tokyo Ghoul : choisissez d'être Ghoul ou Enquêteur CCG, maîtrisez vos kagunes/quinques et progressez dans l'histoire. Les codes offrent des RC, du Yen et des Color Credits.",
    redeem="cliquez sur le bouton « </> » à gauche de l'écran, saisissez le code dans la case de texte puis appuyez sur « Submit Code ».",
    codes=[
      ("MATCHMAKING!",    "🔴 1M RC + 10M Yen + 30 Color Credits + 20 cœurs"),
      ("ANNIVERSARY-8",   "🎂 2M RC + 20M Yen + 120 Color Credits + 80 cœurs"),
      ("No-Ghoul",        "🔴 1M RC + 10M Yen + 30 Color Credits + 20 cœurs"),
      ("03/04/26 upd",    "⚡ 1M RC + 10M Yen + 30 Color Credits + 20 cœurs"),
      ("ReReKura1",       "🎁 1M RC + 10M Yen + 30 Color Credits + 20 cœurs"),
    ],
    similar=[("type-soul","💀","Type Soul"),("attack-on-titan-revolution","⚔️","Attack on Titan Revolution"),("shindo-life","🌀","Shindo Life")],
    about1="Ro-Ghoul est un RPG d'action classique de Roblox inspiré de l'anime Tokyo Ghoul : au cœur de la ville de Tokyo, choisissez de jouer du côté des Ghouls (créatures qui se nourrissent d'humains) ou de la Commission de Contre-Ghouls (CCG) qui cherche à les éliminer. Avec plus de 8 années d'existence, c'est l'un des jeux d'anime les plus emblématiques de la plateforme.",
    about2="La progression dans Ro-Ghoul repose sur l'accumulation de RC (cellules Rc pour les Ghouls) et de Yen (pour les enquêteurs CCG), permettant d'améliorer vos kagunes et quinques. Les codes anniversaire sont particulièrement généreux et marquent chaque année de nouveaux records pour le jeu. La 8e mise à jour anniversaire est disponible, célébrant l'incroyable longévité du jeu.",
    svg1="#1a0a0a", svg2="#cc0000",
  ),
]

def make_svg(g):
    slug = g["slug"]
    c1, c2 = g["svg1"], g["svg2"]
    em = g["emoji"]
    name = g["name"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 225">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="400" height="225" fill="url(#bg)" rx="8"/>
  <text x="200" y="110" font-family="Arial,sans-serif" font-size="60" text-anchor="middle" dominant-baseline="middle">{em}</text>
  <text x="200" y="175" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="white" text-anchor="middle" opacity="0.9">{name}</text>
</svg>"""

def make_page(g):
    slug = g["slug"]
    name = g["name"]
    emoji = g["emoji"]
    cat = g["cat"]
    catLabel = g["catLabel"]
    desc = g["desc"]
    codes = g["codes"]
    redeem = g["redeem"]
    similar = g["similar"]
    about1 = g["about1"]
    about2 = g["about2"]
    n = len(codes)
    thumb_url = f"https://tr.rbxcdn.com/placeholder-{slug}/768/432/Image/Png/noFilter"
    name_title = name.replace("'", "&#39;")
    
    # Build codes table rows
    if codes:
        rows = "\n".join(
            f'<tr><td><div class="code-cell"><span class="code-value">{c}</span></div></td>'
            f'<td><span class="reward-tag">{r}</span></td>'
            f'<td><button class="copy-btn" onclick="copyCode(this,\'{c}\')">Copier</button></td></tr>'
            for c, r in codes
        )
        codes_tab = f"""<div class="codes-live-banner"><div class="pulse-dot"></div><div><strong>{n} codes actifs trouvés</strong><br><span>Dernière vérification : {DATE_FR} — vérifié chaque jour.</span></div></div>
<div class="notice notice-info"><span class="notice-icon">ℹ️</span><p><strong>Comment utiliser :</strong> {redeem}</p></div>
<h3 style="margin:24px 0 14px">Comment utiliser les codes {name}</h3>
<div class="redeem-steps"><div class="redeem-step"><div class="step-num">1</div><div class="step-icon">🚀</div><h4>Lancer le jeu</h4><p>Ouvrez Roblox et lancez le jeu</p></div><div class="redeem-step"><div class="step-num">2</div><div class="step-icon">📋</div><h4>Ouvrir les codes</h4><p>Repérez la zone de saisie des codes</p></div><div class="redeem-step"><div class="step-num">3</div><div class="step-icon">⌨️</div><h4>Saisir le code</h4><p>Collez le code exactement (sensible à la casse)</p></div><div class="redeem-step"><div class="step-num">4</div><div class="step-icon">🎁</div><h4>Valider</h4><p>Validez — la récompense arrive aussitôt</p></div></div>
<div class="codes-section" style="margin-top:24px"><div class="codes-status-bar"><div class="status-dot green" style="width:8px;height:8px;border-radius:50%;background:#00c853;box-shadow:0 0 8px #00c853;animation:pulse 2s infinite"></div><span style="font-size:.85rem;font-weight:600;color:#00c853">Codes actifs — fonctionnent en {MONTH}</span><span style="font-size:.78rem;color:var(--text-muted);margin-left:auto">Vérifié le {DATE_FR}</span></div>
<div style="overflow-x:auto"><table class="codes-table"><thead><tr><th>Code</th><th>Récompense</th><th>Action</th></tr></thead><tbody>{rows}</tbody></table></div></div>"""
    else:
        codes_tab = f"""<div class="notice notice-info" style="border-left:3px solid #0096ff"><span class="notice-icon">ℹ️</span><p><strong>Aucun code actif confirmé actuellement.</strong> Dès qu'un code officiel sortira, il sera ajouté ici. Revenez chaque jour !</p></div>
<h3 style="margin:24px 0 14px">Comment utiliser les codes {name}</h3>
<div class="redeem-steps"><div class="redeem-step"><div class="step-num">1</div><div class="step-icon">🚀</div><h4>Lancer le jeu</h4><p>Ouvrez Roblox et lancez le jeu</p></div><div class="redeem-step"><div class="step-num">2</div><div class="step-icon">📋</div><h4>Ouvrir les codes</h4><p>{redeem}</p></div><div class="redeem-step"><div class="step-num">3</div><div class="step-icon">⌨️</div><h4>Saisir le code</h4><p>Collez le code exactement (sensible à la casse)</p></div><div class="redeem-step"><div class="step-num">4</div><div class="step-icon">🎁</div><h4>Valider</h4><p>Validez — la récompense arrive aussitôt</p></div></div>"""

    # Build similar links for sidebar
    sim_links = "\n".join(
        f'<a href="/codes/{s}.html" style="display:flex;align-items:center;gap:10px;font-size:.85rem;color:var(--text-muted)">{e} {n2}</a>'
        for s, e, n2 in similar
    )
    sim_about = "\n".join(
        f'<a href="/codes/{s}.html" style="display:flex;align-items:center;gap:10px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-sm);padding:12px 14px;text-decoration:none;color:var(--text-primary);font-weight:600;font-size:.9rem">🎮 Codes {n2} →</a>'
        for s, e, n2 in similar
    )

    # CTA banner - no guide or tier list yet, use hub links
    cta_banner = f"""<div class="container" data-cta="guidelink" style="margin-top:18px"><div style="display:flex;flex-wrap:wrap;align-items:center;gap:14px;justify-content:space-between;background:linear-gradient(135deg,rgba(162,89,255,.20),rgba(0,207,255,.12));border:1.5px solid rgba(162,89,255,.55);box-shadow:0 8px 28px rgba(162,89,255,.22);border-radius:var(--radius);padding:16px 20px"><div style="display:flex;align-items:center;gap:12px;min-width:200px;flex:1"><span style="font-size:1.9rem">📖</span><div><div style="font-weight:800;font-size:1.05rem;color:var(--text-primary)">Besoin d&#39;aide pour progresser ?</div><div style="font-size:.85rem;color:var(--text-muted)">Découvrez nos guides et tier lists Roblox</div></div></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/guides/" style="display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:700;padding:11px 18px;border-radius:var(--radius-sm);text-decoration:none;white-space:nowrap">📖 Guides</a><a href="/tier-list/" style="display:inline-flex;align-items:center;gap:7px;background:transparent;color:var(--text-primary);font-weight:700;padding:11px 18px;border-radius:var(--radius-sm);text-decoration:none;white-space:nowrap;border:1.5px solid rgba(162,89,255,.55)">📊 Tier lists</a></div></div></div>"""

    # meta count string
    meta_codes = f"{n} codes actifs" if n > 0 else "codes"

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FEL71QVHNL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-FEL71QVHNL');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Codes {name} ({MONTH}) – Tous les codes actifs | Zoneblox</title>
  <meta name="description" content="Codes {name} pour {MONTH} : {meta_codes}, guide d'utilisation, astuces et vidéos. Récompenses gratuites !">
  <meta name="keywords" content="codes {name.lower()}, codes {name.lower()} 2026, {name.lower()} roblox, codes roblox {name.lower()}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0e0b1a">
  <link rel="canonical" href="https://zoneblox.com/codes/{slug}.html">
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Zoneblox">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:url" content="https://zoneblox.com/codes/{slug}.html">
  <meta property="og:title" content="Codes {name} ({MONTH}) – Tous les codes actifs | Zoneblox">
  <meta property="og:description" content="Codes {name} pour {MONTH} : {meta_codes}, guide d'utilisation et astuces. Récompenses gratuites !">
  <meta property="og:image" content="https://zoneblox.com/images/og-cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","inLanguage":"fr-FR","headline":"Codes {name} ({MONTH}) – Tous les codes actifs | Zoneblox","datePublished":"{DATE_ISO}","dateModified":"{DATE_ISO}","author":{{"@type":"Organization","name":"Zoneblox"}},"publisher":{{"@type":"Organization","name":"Zoneblox","logo":{{"@type":"ImageObject","url":"https://zoneblox.com/images/logo.png"}}}}}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Accueil","item":"https://zoneblox.com/"}},{{"@type":"ListItem","position":2,"name":"Tous les codes","item":"https://zoneblox.com/codes/"}},{{"@type":"ListItem","position":3,"name":"{name}","item":"https://zoneblox.com/codes/{slug}.html"}}]}}
  </script>
  <link rel="stylesheet" href="/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    .codes-live-banner{{background:linear-gradient(135deg,rgba(0,200,83,.08),rgba(0,207,255,.06));border:1px solid rgba(0,200,83,.3);border-radius:var(--radius);padding:14px 18px;display:flex;align-items:center;gap:12px;margin-bottom:20px}}
    .pulse-dot{{width:10px;height:10px;border-radius:50%;background:#00c853;box-shadow:0 0 10px #00c853;animation:pulse 2s infinite;flex-shrink:0}}
    .page-tabs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px;margin-bottom:28px}}.page-tab{{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:15px 10px;font-size:.95rem;font-weight:700;color:var(--text-muted);cursor:pointer;transition:.15s;text-align:center}}.page-tab:hover{{color:var(--text-primary);border-color:rgba(162,89,255,.45);transform:translateY(-2px)}}.page-tab.active{{background:linear-gradient(135deg,var(--accent),var(--accent2));border-color:transparent;color:#fff;box-shadow:0 6px 18px rgba(162,89,255,.35)}}.tab-content{{display:none}}.tab-content.active{{display:block}}
    .tips-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
    .videos-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}}
    .video-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}}
    .video-embed{{position:relative;padding-top:56.25%;background:#000}}
    .video-embed iframe{{position:absolute;top:0;left:0;width:100%;height:100%;border:none}}
    .video-embed a{{position:absolute;top:0;left:0;width:100%;height:100%;display:flex;align-items:center;justify-content:center}}
    .video-label{{padding:12px 16px;font-size:.85rem;font-weight:600;color:var(--text-primary)}}
  </style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <nav class="nav-inner">
      <a href="/" class="nav-logo"><div class="logo-icon">🎮</div><span>Zone<span class="gradient-text">blox</span></span></a>
      <ul class="nav-links"><li><a href="/">Accueil</a></li><li><a href="/codes/" class="active">Tous les codes</a></li><li><a href="/tier-list/">Tier lists</a></li><li><a href="/guides/">Guides</a></li><li><a href="/ugc-gratuit/">UGC gratuits</a></li><li><a href="/about.html">À propos</a></li></ul>
      <div class="nav-right"><button class="nav-toggle"><span></span><span></span><span></span></button></div>
    </nav>
  </div>
</header>

<div class="game-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Accueil</a><span class="sep">›</span><a href="/codes/">Tous les codes</a><span class="sep">›</span><span>{name}</span></div>
    <div class="game-hero-inner">
      <img data-game="{slug}" src="/images/games/{slug}.svg" onerror="this.onerror=null;this.src='/images/games/{slug}.svg'" alt="{name}" class="game-hero-thumb" style="object-fit:cover;width:200px;height:112px;border-radius:var(--radius)">
      <div class="game-hero-info">
        <h1>Codes {name} <span class="gradient-text">{MONTH}</span></h1>
        <div class="game-meta">
          <div class="game-meta-item">✅ <strong>{n} codes actifs</strong></div>
          <div class="game-meta-item">🕐 Mis à jour le <strong>{DATE_FR}</strong></div>
          <div class="game-meta-item">🏷️ <strong>{catLabel}</strong></div>
        </div>
        <p class="desc">{desc}</p>
      </div>
    </div>
  </div>
</div>

<div class="container" style="margin-top:20px">
  <div class="ad-banner ad-leaderboard"><span>728 × 90 — Google AdSense</span></div>
{cta_banner}
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
          {codes_tab}
        </div>

        <div class="tab-content" id="tab-tips">
          <div class="tips-grid">
<div class="tip-card"><div class="tip-num">1</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Utilisez les codes dès leur sortie</h4><p style="font-size:.85rem">Beaucoup de codes Roblox expirent en quelques jours. Dès qu'un nouveau code apparaît, utilisez-le sans attendre pour ne pas le rater.</p></div>
<div class="tip-card"><div class="tip-num">2</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Copiez-collez sans erreur</h4><p style="font-size:.85rem">Les codes sont sensibles à la casse. Copiez-les directement depuis Zoneblox plutôt que de les retaper, pour éviter les fautes de frappe.</p></div>
<div class="tip-card"><div class="tip-num">3</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Suivez le Discord officiel</h4><p style="font-size:.85rem">Les développeurs annoncent les nouveaux codes en premier sur Discord. Rejoignez le serveur officiel de {name} pour être le premier informé.</p></div>
<div class="tip-card"><div class="tip-num">4</div><h4 style="margin-bottom:6px;color:var(--text-primary)">Revenez chaque jour</h4><p style="font-size:.85rem">Zoneblox vérifie et met à jour les codes quotidiennement. Ajoutez cette page à vos favoris pour ne jamais manquer une récompense gratuite.</p></div>
          </div>
        </div>

        <div class="tab-content" id="tab-videos">
          <p style="margin-bottom:20px;font-size:.9rem">Les vidéos les plus populaires du moment sur {name}.</p>
          <div class="videos-grid">
            <div class="video-card"><div class="video-embed" style="position:relative;padding-top:56.25%">
              <a href="https://www.youtube.com/results?search_query={name.replace(' ', '+')}+Roblox+codes" target="_blank" rel="noopener" style="gap:10px;background:linear-gradient(135deg,#1a1a30,#0a0a1a);color:#fff;text-decoration:none;font-weight:700;font-size:.95rem"><span style="font-size:2.4rem">▶</span> Voir les vidéos sur YouTube</a>
            </div><div class="video-label">🎬 {name} — vidéos populaires</div></div>
          </div>
        </div>

        <div class="tab-content" id="tab-faq">
          <div style="display:flex;flex-direction:column;gap:14px">
<details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Quels sont les codes {name} actifs ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Tous les codes actifs sont listés dans le tableau ci-dessus, avec leur récompense. Ils sont vérifiés chaque jour.</p></details>
<details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Pourquoi mon code {name} ne fonctionne pas ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Les codes sont sensibles à la casse : copiez-collez-les exactement. S'il ne marche toujours pas, le code a peut-être expiré ou a déjà été utilisé sur votre compte.</p></details>
<details class="tip-card" style="cursor:pointer"><summary style="font-weight:700;font-size:.95rem;color:var(--text-primary);user-select:none;list-style:none;display:flex;justify-content:space-between">Où trouver les nouveaux codes ? <span>▼</span></summary><p style="margin-top:10px;font-size:.88rem">Sur Zoneblox, mis à jour chaque jour, ainsi que sur le Discord et le compte X (Twitter) officiels de {name}.</p></details>
          </div>
        </div>
      </div>

      <aside>
        <div class="sidebar-sticky">
          <div class="ad-banner ad-rectangle" style="height:250px;width:100%;background:var(--bg-secondary);border:1px dashed rgba(255,255,255,0.1);border-radius:var(--radius);display:flex;align-items:center;justify-content:center;font-size:.75rem;color:var(--text-muted)">300 × 250<br>Google AdSense</div>
          <div class="sidebar-widget">
            <h3 style="font-size:.95rem;margin-bottom:14px;border-bottom:1px solid var(--border);padding-bottom:10px">📧 Recevez les nouveaux codes en premier</h3>
            <p style="font-size:.82rem;margin-bottom:12px">Abonnez-vous et soyez averti dès qu'un nouveau code {name} sort.</p>
            <form class="newsletter-form" onsubmit="return false">
              <input type="email" placeholder="votre@email.com" required>
              <button type="submit">🔔 Me prévenir</button>
            </form>
          </div>
          <div class="sidebar-widget">
            <h3 style="font-size:.95rem;margin-bottom:14px;border-bottom:1px solid var(--border);padding-bottom:10px">🎮 Jeux similaires</h3>
            <div style="display:flex;flex-direction:column;gap:8px">
              {sim_links}
            </div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

<!-- ABOUT-START -->
<section class="section" style="padding-top:0">
  <div class="container" style="max-width:900px">
    <h2 class="section-title" style="margin-bottom:14px"><span>À propos de {name}</span></h2>
    <div style="color:var(--text-muted);font-size:.95rem;line-height:1.75;display:flex;flex-direction:column;gap:14px">
      <p>{about1}</p>
      <p>{about2}</p>
    </div>
    <h3 style="margin:26px 0 12px">🎮 Jeux similaires</h3>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px">
      {sim_about}
    </div>
  </div>
</section>
<!-- ABOUT-END -->

<footer class="site-footer">
  <div class="container">
    <div class="footer-bottom" style="padding:24px 0">
      <span>© 2026 Zoneblox — Non affilié à Roblox Corporation.</span>
      <span><a href="/about.html">À propos</a> · <a href="/privacy.html">Confidentialité</a> · <a href="/terms.html">Conditions</a> · <a href="/contact.html">Contact</a></span>
    </div>
  </div>
</footer>
<script src="/js/main.js?v=15"></script>
<script>
function switchTab(tabId){{document.querySelectorAll('.page-tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));var b=document.querySelector('[data-tab="'+tabId+'"]');var p=document.getElementById('tab-'+tabId);if(b)b.classList.add('active');if(p)p.classList.add('active');}}
document.querySelectorAll('.page-tab').forEach(function(tab){{tab.addEventListener('click',function(){{switchTab(tab.dataset.tab);}});}});
</script>
</body>
</html>"""
    return html

# ============ BUILD PAGES ============
print("Building 6 new game pages...")
for g in GAMES:
    slug = g["slug"]
    W(f"codes/{slug}.html", make_page(g))
    W(f"images/games/{slug}.svg", make_svg(g))
    print(f"  ✅ codes/{slug}.html + images/games/{slug}.svg")

# ============ UPDATE main.js ============
print("\nUpdating js/main.js...")
main_js = R("js/main.js")

# 1. Insert into GAMES_INDEX (before the closing ];)
new_gi_entries = ""
for g in GAMES:
    slug = g["slug"]
    name = g["name"]
    emoji = g["emoji"]
    cat = g["cat"]
    n = len(g["codes"])
    new_gi_entries += f"  {{ name: '{name}', slug: '{slug}', emoji: '{emoji}', codes: {n} }},\n"

main_js = main_js.replace(
    "  { name: 'Combat Warriors', slug: 'combat-warriors', emoji: '🗡️', codes: 0 },\n  { name: 'Survive the Killer', slug: 'survive-the-killer', emoji: '🔪', codes: 0 },\n];",
    "  { name: 'Combat Warriors', slug: 'combat-warriors', emoji: '🗡️', codes: 0 },\n  { name: 'Survive the Killer', slug: 'survive-the-killer', emoji: '🔪', codes: 0 },\n" +
    new_gi_entries + "];"
)

# 2. Insert into ROBLOX_THUMBS (before the }; closing)
new_thumb_entries = ""
for g in GAMES:
    slug = g["slug"]
    # Use SVG path as static placeholder - will be loaded by applyRobloxThumbs() if API available
    new_thumb_entries += f"  '{slug}': '/images/games/{slug}.svg',\n"

main_js = main_js.replace(
    "  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/768/432/Image/Png/noFilter',\n};",
    "  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/768/432/Image/Png/noFilter',\n" +
    new_thumb_entries + "};"
)

# 3. Insert into ROBLOX_UNIVERSE_IDS (before the closing };)
new_uid_entries = ""
for g in GAMES:
    slug = g["slug"]
    uid = g["universeId"]
    new_uid_entries += f"  '{slug}': {uid},\n"

main_js = main_js.replace(
    "  'survive-the-killer': 1489026993,\n};",
    "  'survive-the-killer': 1489026993,\n" + new_uid_entries + "};"
)

W("js/main.js", main_js)
print("  ✅ js/main.js updated (GAMES_INDEX + ROBLOX_THUMBS + ROBLOX_UNIVERSE_IDS)")

# ============ UPDATE codes/index.html ============
print("\nUpdating codes/index.html...")
idx = R("codes/index.html")

# Add to ALL_GAMES before closing ];
new_all_games = ""
for g in GAMES:
    slug = g["slug"]
    name = g["name"].replace("'", "\\'")
    emoji = g["emoji"]
    cat = g["cat"]
    n = len(g["codes"])
    new_all_games += f"  {{ name:'{name}', slug:'{slug}', emoji:'{emoji}', cat:'{cat}', codes:{n}, iso:'{DATE_ISO}', updated:'{DATE_FR}', hot:true }},\n"

idx = idx.replace(
    "  { name:'Survive the Killer', slug:'survive-the-killer', emoji:'🔪', cat:'battle', codes:0, iso:'2026-06-07', updated:'7 juin 2026', hot:true },\n];",
    "  { name:'Survive the Killer', slug:'survive-the-killer', emoji:'🔪', cat:'battle', codes:0, iso:'2026-06-07', updated:'7 juin 2026', hot:true },\n" +
    new_all_games + "];"
)

# Add to THUMBS
new_thumbs = ""
for g in GAMES:
    slug = g["slug"]
    new_thumbs += f"  '{slug}': '/images/games/{slug}.svg',\n"

idx = idx.replace(
    "  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/768/432/Image/Png/noFilter',\n};",
    "  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/768/432/Image/Png/noFilter',\n" +
    new_thumbs + "};"
)

W("codes/index.html", idx)
print("  ✅ codes/index.html updated (ALL_GAMES + THUMBS)")

# ============ UPDATE sitemap.xml ============
print("\nUpdating sitemap.xml...")
sitemap = R("sitemap.xml")
new_urls = ""
for g in GAMES:
    slug = g["slug"]
    new_urls += f"""  <url>
    <loc>https://zoneblox.com/codes/{slug}.html</loc>
    <lastmod>{DATE_ISO}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
W("sitemap.xml", sitemap)
print("  ✅ sitemap.xml updated")

print("\n✅ All done! 6 games added:")
for g in GAMES:
    print(f"  - {g['name']} ({len(g['codes'])} codes, slug: {g['slug']})")
