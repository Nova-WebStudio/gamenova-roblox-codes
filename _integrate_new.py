# -*- coding: utf-8 -*-
import io, os
BASE = os.path.dirname(os.path.abspath(__file__))
def R(p):
    with io.open(os.path.join(BASE, p), encoding="utf-8") as f: return f.read()
def W(p, s):
    with io.open(os.path.join(BASE, p), "w", encoding="utf-8") as f: f.write(s)

DATE_ISO = "2026-06-06"; DATE_FR = "6 juin 2026"

# slug, name, emoji, cat, thumb, universe(or None), codes, hot, card_desc
NEW = [
 ("all-star-tower-defense","All Star Tower Defense","🌟","anime",
  "https://tr.rbxcdn.com/180DAY-9fbd50db5a51699b733c9529ee542d19/768/432/Image/Webp/noFilter",4996049426,4,True,
  "Tower defense d'anime culte : invoquez vos personnages, placez vos unités et repoussez les vagues. Codes : Gemmes et Poussière d'étoile."),
 ("anime-champions-simulator","Anime Champions Simulator","🌌","anime",
  "https://tr.rbxcdn.com/180DAY-9d4be137161ea266ba1c2c6f28832e21/768/432/Image/Webp/noFilter",None,7,True,
  "Collectionnez et entraînez de puissants champions d'anime à travers la galaxie. Codes : Diamants, Médailles Premium et Boosts."),
 ("sonic-speed-simulator","Sonic Speed Simulator","💨","simulator",
  "https://tr.rbxcdn.com/180DAY-82939a396600a61e4abadd92664f8d83/768/432/Image/Webp/noFilter",None,8,True,
  "Courez à toute vitesse, débloquez des mondes et collectionnez les skins Sonic. Codes : Chao, boosts et tickets de course."),
 ("tower-defense-simulator","Tower Defense Simulator","🧟","battle",
  "https://tr.rbxcdn.com/180DAY-f4a7603e22db5d7a43e966fe145a96e1/768/432/Image/Webp/noFilter",None,0,True,
  "Placez vos tours, coopérez et repoussez les vagues de zombies pour débloquer de nouvelles unités. Aucun code actif confirmé pour l'instant."),
 ("project-slayers","Project Slayers","🌸","anime",
  "https://tr.rbxcdn.com/180DAY-612b92100da817e8dc2bb8fd35ce117e/768/432/Image/Webp/noFilter",5956785391,0,True,
  "RPG d'action inspiré de Demon Slayer : souffles, arts démoniaques et monde ouvert. Aucun code actif confirmé pour l'instant."),
 ("the-strongest-battlegrounds","The Strongest Battlegrounds","👊","battle",
  "https://tr.rbxcdn.com/180DAY-c947df5b221c30672c3591247a8c6495/768/432/Image/Webp/noFilter",10449761463,0,True,
  "Jeu de combat inspiré de One-Punch Man : styles surpuissants et PVP nerveux. Pas de codes de récompense dans ce jeu."),
]

# ---------- js/main.js ----------
js = R("js/main.js")
# ROBLOX_THUMBS
tl = "".join("  '%s': '%s',\n" % (s, thumb) for s,_,_,_,thumb,_,_,_,_ in NEW)
anc = "  'haze-piece': 'https://tr.rbxcdn.com/180DAY-41212ff0c4a4a7105b2e1605f3666243/500/280/Image/Jpeg/noFilter',\n};"
assert js.count(anc) == 1, "thumbs anchor"
js = js.replace(anc, "  'haze-piece': 'https://tr.rbxcdn.com/180DAY-41212ff0c4a4a7105b2e1605f3666243/500/280/Image/Jpeg/noFilter',\n" + tl + "};", 1)
# GAMES_INDEX
gi = "".join("  { name: '%s', slug: '%s', emoji: '%s', codes: %d },\n" % (name,s,emoji,codes) for s,name,emoji,_,_,_,codes,_,_ in NEW)
gia = "  { name: 'Haze Piece', slug: 'haze-piece', emoji: '🌊', codes: 3 },\n];"
assert js.count(gia) == 1, "games_index anchor"
js = js.replace(gia, "  { name: 'Haze Piece', slug: 'haze-piece', emoji: '🌊', codes: 3 },\n" + gi + "];", 1)
# ROBLOX_UNIVERSE_IDS (only those with universe)
uid = "".join("  '%s': %d,\n" % (s,u) for s,_,_,_,_,u,_,_,_ in NEW if u)
uida = "  'haze-piece': 2644656496,\n};"
assert js.count(uida) == 1, "universe anchor"
js = js.replace(uida, "  'haze-piece': 2644656496,\n" + uid + "};", 1)
W("js/main.js", js)
print("main.js OK")

# ---------- codes/index.html ----------
ci = R("codes/index.html")
# THUMBS
ct = "".join("  '%s':'%s',\n" % (s,thumb) for s,_,_,_,thumb,_,_,_,_ in NEW)
ca = "  'haze-piece':'https://tr.rbxcdn.com/180DAY-41212ff0c4a4a7105b2e1605f3666243/500/280/Image/Jpeg/noFilter',\n};"
assert ci.count(ca) == 1, "ci thumbs anchor"
ci = ci.replace(ca, "  'haze-piece':'https://tr.rbxcdn.com/180DAY-41212ff0c4a4a7105b2e1605f3666243/500/280/Image/Jpeg/noFilter',\n" + ct + "};", 1)
# ALL_GAMES
ag = "".join("  { name:'%s', slug:'%s', emoji:'%s', cat:'%s', codes:%d, iso:'%s', updated:'%s', hot:%s },\n"
            % (name,s,emoji,cat,codes,DATE_ISO,DATE_FR,'true' if hot else 'false') for s,name,emoji,cat,_,_,codes,hot,_ in NEW)
i = ci.index("const ALL_GAMES = [")
j = ci.index("\n];", i)
ci = ci[:j+1] + ag + ci[j+1:]
# counter
ci = ci.replace("Affichage de <strong>52</strong> jeux", "Affichage de <strong>58</strong> jeux")
W("codes/index.html", ci)
print("codes/index.html OK")

# ---------- index.html ----------
ix = R("index.html")
ix = ix.replace("chacun des 52 jeux couverts", "chacun des 58 jeux couverts")
# cards before jujutsu-infinite card
def card(s,name,emoji,thumb,codes,desc):
    badge = '<span class="card-badge badge-hot">🆕 NOUVEAU</span>'
    meta = ('✅ %d codes actifs' % codes) if codes else 'ⓘ Aucun code actif'
    tl = ''
    if s == 'all-star-tower-defense':
        tl = ("\n          <span class=\"card-cta\" onclick=\"event.preventDefault();event.stopPropagation();"
              "window.location.href='/tier-list/all-star-tower-defense.html';return false;\" "
              "style=\"margin-top:8px;background:linear-gradient(135deg,#ff9f1c,#ff4d4d);box-shadow:0 4px 14px rgba(255,77,77,.35)\">📊 Voir la tier list</span>")
    return ('      <a href="/codes/%s.html" class="game-card">\n'
            '        <div class="game-card-thumb">\n'
            '          <img data-game="%s" src="%s" onerror="this.onerror=null;this.src=\'/images/games/%s.svg\'" alt="%s" class="thumb-svg">\n'
            '          %s\n'
            '        </div>\n'
            '        <div class="game-card-body">\n'
            '          <div class="game-card-title">%s</div>\n'
            '          <div class="game-card-meta">\n'
            '            <span class="meta-codes">%s</span>\n'
            '            <span class="meta-date">Mis à jour le %s</span>\n'
            '          </div>\n'
            '          <div class="game-card-desc">%s</div>\n'
            '          <span class="card-cta">🎁 Voir les codes</span>%s\n'
            '        </div>\n'
            '      </a>\n') % (s,s,thumb,s,name,badge,name,meta,DATE_FR,desc,tl)
cards = "".join(card(s,name,emoji,thumb,codes,desc) for s,name,emoji,_,thumb,_,codes,_,desc in NEW)
card_anchor = '      <a href="/codes/jujutsu-infinite.html" class="game-card">'
assert ix.count(card_anchor) == 1, "index card anchor"
ix = ix.replace(card_anchor, cards + card_anchor, 1)
# nav <li> "Tous les jeux"
nav = "".join('          <li><a href="/codes/%s.html">Codes %s</a></li>\n' % (s,name) for s,name,_,_,_,_,_,_,_ in NEW)
nav_anchor = '          <li><a href="/codes/haze-piece.html">Codes Haze Piece</a></li>\n'
assert ix.count(nav_anchor) == 1, "index nav anchor"
ix = ix.replace(nav_anchor, nav_anchor + nav, 1)
# tier list nav <li>
tlnav_anchor = '          <li><a href="/tier-list/basketball-zero.html">Tier list Basketball Zero</a></li>\n'
assert ix.count(tlnav_anchor) == 1, "index tier nav anchor"
ix = ix.replace(tlnav_anchor, tlnav_anchor + '          <li><a href="/tier-list/all-star-tower-defense.html">Tier list All Star Tower Defense</a></li>\n', 1)
W("index.html", ix)
print("index.html OK")

# ---------- sitemap.xml ----------
sm = R("sitemap.xml")
urls = "".join('  <url><loc>https://zoneblox.com/codes/%s.html</loc><changefreq>daily</changefreq><priority>0.8</priority><lastmod>%s</lastmod></url>\n' % (s,DATE_ISO) for s,_,_,_,_,_,_,_,_ in NEW)
urls += '  <url><loc>https://zoneblox.com/tier-list/all-star-tower-defense.html</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>%s</lastmod></url>\n' % DATE_ISO
assert "</urlset>" in sm
sm = sm.replace("</urlset>", urls + "</urlset>", 1)
W("sitemap.xml", sm)
print("sitemap.xml OK")

# ---------- tier-list/index.html ----------
tlh = R("tier-list/index.html")
sa = '    {"@type":"ListItem","position":19,"name":"Tier List Basketball Zero","url":"https://zoneblox.com/tier-list/basketball-zero.html"}'
assert tlh.count(sa) == 1, "tlhub schema anchor"
tlh = tlh.replace(sa, sa + ',\n    {"@type":"ListItem","position":20,"name":"Tier List All Star Tower Defense","url":"https://zoneblox.com/tier-list/all-star-tower-defense.html"}', 1)
cda = '      <a class="tl-card" href="/tier-list/basketball-zero.html"><span class="tl-emoji">🏀</span><span class="tl-info"><span class="tl-name">Basketball Zero</span><span class="tl-sub">Meilleurs styles classés</span></span><span class="tl-arrow">→</span></a>'
assert tlh.count(cda) == 1, "tlhub card anchor"
tlh = tlh.replace(cda, cda + '\n      <a class="tl-card" href="/tier-list/all-star-tower-defense.html"><span class="tl-emoji">🌟</span><span class="tl-info"><span class="tl-name">All Star Tower Defense</span><span class="tl-sub">Meilleures unités classées</span></span><span class="tl-arrow">→</span></a>', 1)
W("tier-list/index.html", tlh)
print("tier-list/index.html OK")
print("DONE integrate")
