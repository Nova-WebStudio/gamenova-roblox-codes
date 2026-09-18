#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZoneBlox — Générateur multigaming statique (game-first).

Principe : ajouter un jeu = une opération DATA, pas DEV.
  - data/games/<slug>.json  : entité jeu + contentTypes déclarés
  - data/<slug>/<type>.json : données par type de contenu (codes, ...)
Le générateur rend des pages statiques réutilisables sous /games/ :
  - /games/                    (annuaire des jeux)
  - /games/<slug>/             (hub du jeu)
  - /games/<slug>/<type>/      (une page par type de contenu disponible)

Ne touche JAMAIS aux pages Roblox historiques (URLs plates préservées).
Pur stdlib (aucune dépendance). Idempotent.

Usage :  python3 tools/build_site.py
"""
import json, os, glob, html, datetime, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://zoneblox.com"
GA = "G-FEL71QVHNL"
CSSV = "5"
FR_MONTHS = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet",
             "août", "septembre", "octobre", "novembre", "décembre"]

def e(s):
    return html.escape(str(s), quote=True) if s is not None else ""

def fr_date(iso):
    """2026-09-17 -> 17 septembre 2026 ; renvoie tel quel si non ISO."""
    try:
        y, m, d = [int(x) for x in iso.split("-")]
        return f"{d} {FR_MONTHS[m]} {y}"
    except Exception:
        return iso

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ---------- gabarits partagés ----------
GA_SNIPPET = ("<script>\nwindow.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}\n"
    "(function(){var l=false;function g(){if(l)return;l=true;var s=document.createElement('script');"
    "s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=%s';document.head.appendChild(s);"
    "gtag('js',new Date());gtag('config','%s');}\n"
    "['scroll','mousemove','touchstart','click','keydown'].forEach(function(ev){window.addEventListener(ev,g,{once:true,passive:true});});\n"
    "setTimeout(g,5000);})();\n</script>") % (GA, GA)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet" />')

NAV_ITEMS = [
    ("Accueil", "/", "home"),
    ("Jeux", "/games/", "games"),
    ("Tous les codes", "/tous-les-codes.html", "codes"),
    ("Tier lists", "/tier-lists.html", "tiers"),
    ("Guides", "/guides.html", "guides"),
    ("Avatars", "/avatar/", "avatars"),
    ("UGC gratuits", "/ugc-gratuits.html", "ugc"),
]

def header(active=""):
    def ac(key):
        return ' class="active"' if key == active else ""
    links = (
        '<a href="/"%s>Accueil</a>' % ac("home")
        + ('<div class="nav-item"><a href="/tous-les-codes.html"%s>Roblox<span class="nav-caret">▾</span></a>'
           '<div class="nav-menu"><a href="/tous-les-codes.html">🎁 Tous les codes</a>'
           '<a href="/tier-lists.html">📊 Tier lists</a><a href="/guides.html">📖 Guides</a></div></div>' % ac("codes"))
        + '<div class="nav-item"><a href="/games/aniimo/">Aniimo<span class="nav-caret">▾</span></a>'
          '<div class="nav-menu"><a href="/games/aniimo/codes/">🎁 Codes</a><a href="/games/aniimo/guides/">📖 Guides</a>'
          '<a href="/games/aniimo/tier-list/">📊 Tier list</a><a href="/games/aniimo/locations/">🗺️ Carte & lieux</a></div></div>'
        + '<div class="nav-item"><a href="/games/gta-6/">GTA 6<span class="nav-caret">▾</span></a>'
          '<div class="nav-menu"><a href="/games/gta-6/updates/">📰 Actualités</a><a href="/games/gta-6/guides/">📖 Infos & preview</a>'
          '<a href="/games/gta-6/videos/">🎬 Trailers</a></div></div>'
        + '<div class="nav-item"><a href="/games/fc-27/">FC 27<span class="nav-caret">▾</span></a>'
          '<div class="nav-menu"><a href="/games/fc-27/updates/">📰 Actualités</a><a href="/games/fc-27/guides/">📖 Infos & preview</a>'
          '<a href="/games/fc-27/videos/">🎬 Trailers</a></div></div>'
        + '<a href="/games/"%s>Tous les jeux</a>' % ac("games")
        + '<a href="/avatar/"%s>Avatars</a>' % ac("avatars")
        + '<a href="/ugc-gratuits.html"%s>UGC gratuits</a>' % ac("ugc"))
    mobile = (
        '<a href="/">Accueil</a>'
        '<span class="mob-group">Roblox</span>'
        '<a href="/tous-les-codes.html">🎁 Tous les codes</a><a href="/tier-lists.html">📊 Tier lists</a><a href="/guides.html">📖 Guides</a>'
        '<span class="mob-group">Aniimo</span>'
        '<a href="/games/aniimo/codes/">🎁 Codes</a><a href="/games/aniimo/guides/">📖 Guides</a>'
        '<a href="/games/aniimo/tier-list/">📊 Tier list</a><a href="/games/aniimo/locations/">🗺️ Carte & lieux</a>'
        '<span class="mob-group">GTA 6</span>'
        '<a href="/games/gta-6/updates/">📰 Actualités</a><a href="/games/gta-6/guides/">📖 Infos & preview</a>'
        '<a href="/games/gta-6/videos/">🎬 Trailers</a>'
        '<span class="mob-group">FC 27</span>'
        '<a href="/games/fc-27/updates/">📰 Actualités</a><a href="/games/fc-27/guides/">📖 Infos & preview</a>'
        '<a href="/games/fc-27/videos/">🎬 Trailers</a>'
        '<span class="mob-group">Plus</span>'
        '<a href="/games/">Tous les jeux</a><a href="/avatar/">Avatars</a><a href="/ugc-gratuits.html">UGC gratuits</a>')
    return ('<header><div class="wrap"><nav class="nav" aria-label="Navigation principale">'
        '<a href="/" class="brand" aria-label="Zoneblox"><img src="/images/logo-zoneblox.png" alt="Zoneblox — codes Roblox &amp; more" style="height:40px;width:auto;display:block" onerror="this.onerror=null;this.outerHTML=&#39;<span class=&quot;logo&quot;>🎮</span>Zone<span>blox</span>&#39;"></a>'
        '<div class="nav-links">%s</div>'
        '<div class="nav-search"><label class="search-input"><span class="search-ico">🔍</span>'
        '<input type="search" placeholder="Rechercher un jeu…" aria-label="Rechercher"/></label></div>'
        '<button class="burger" id="burger" aria-label="Menu" aria-expanded="false">☰</button></nav>'
        '<div class="mobile-menu" id="mobileMenu">%s</div></div></header>') % (links, mobile)

def footer():
    return ('<footer><div class="wrap"><div class="foot-grid">'
        '<div class="foot-brand"><a href="/" class="brand" aria-label="Zoneblox"><img src="/images/logo-zoneblox.png" alt="Zoneblox — codes Roblox &amp; more" style="height:40px;width:auto;display:block" onerror="this.onerror=null;this.outerHTML=&#39;<span class=&quot;logo&quot;>🎮</span>Zone<span>blox</span>&#39;"></a>'
        '<p>La plateforme gaming : codes, guides, tier lists, wikis et actus, vérifiés à la main et mis à jour chaque jour.</p></div>'
        '<div><h4>Explorer</h4><a href="/games/">Tous les jeux</a><a href="/tous-les-codes.html">Tous les codes</a><a href="/tier-lists.html">Tier lists</a><a href="/guides.html">Guides</a></div>'
        '<div><h4>Jeux</h4><a href="/games/aniimo/">Aniimo</a><a href="/tous-les-codes.html">Roblox</a></div>'
        '<div><h4>Site</h4><a href="/a-propos.html">À propos</a><a href="/a-propos.html#editorial">Politique éditoriale</a><a href="/a-propos.html#contact">Contact</a></div>'
        '</div><div class="legal"><span>© %d Zoneblox. Non affilié aux éditeurs des jeux cités.</span>'
        '<span>Réalisé avec passion par COSMOVIA</span></div></div></footer>') % datetime.date.today().year

def crumb_html(items):
    parts = []
    for i, (label, url) in enumerate(items):
        if url and i < len(items) - 1:
            parts.append('<a href="%s">%s</a>' % (url, e(label)))
        else:
            parts.append('<span style="color:var(--text)">%s</span>' % e(label))
        if i < len(items) - 1:
            parts.append('<span class="sep">›</span>')
    return '<nav class="crumb" aria-label="Fil d\'ariane">' + "".join(parts) + "</nav>"

def crumb_ld(items):
    el = []
    for i, (label, url) in enumerate(items):
        item = {"@type": "ListItem", "position": i + 1, "name": label}
        if url:
            item["item"] = SITE + url
        el.append(item)
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                       "itemListElement": el}, ensure_ascii=False)

def page(title, desc, canonical, body, active="", extra_ld=None, extra_js=""):
    ld = ""
    for block in (extra_ld or []):
        ld += '<script type="application/ld+json">%s</script>\n' % block
    return ("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>%s\n"
        '<meta charset="UTF-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
        "<title>%s</title>\n"
        '<meta name="description" content="%s" />\n'
        '<link rel="canonical" href="%s" />\n'
        '<meta property="og:type" content="website" />\n'
        '<meta property="og:title" content="%s" />\n'
        '<meta property="og:description" content="%s" />\n'
        '<meta property="og:url" content="%s" />\n'
        '<meta name="twitter:card" content="summary_large_image" />\n'
        '<meta name="theme-color" content="#0a0b16" />\n'
        '%s\n<link rel="stylesheet" href="/css/platform.css?v=%s" />\n<link rel="stylesheet" href="/css/nav-fix.css?v=5" />\n%s</head>\n'
        '<body>\n<a href="#main" class="skip">Aller au contenu</a>\n%s\n<main id="main"><div class="wrap">\n%s\n</div></main>\n%s\n'
        '<div class="toast" id="toast">Copié ✓</div>\n%s\n</body>\n</html>\n') % (
        GA_SNIPPET, e(title), e(desc), canonical, e(title), e(desc), canonical,
        FONTS, CSSV, ld, header(active), body, footer(), COMMON_JS + extra_js)

COMMON_JS = ("<script>\nconst $=(s,c=document)=>c.querySelector(s);const $$=(s,c=document)=>[...c.querySelectorAll(s)];\n"
    "function toast(m){const t=$('#toast');if(!t)return;t.textContent=m;t.classList.add('show');clearTimeout(t._t);t._t=setTimeout(()=>t.classList.remove('show'),1600);}\n"
    "function copyText(t,cb){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(cb).catch(()=>fb(t,cb));}else fb(t,cb);}\n"
    "function fb(t,cb){const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(a);cb();}\n"
    "document.addEventListener('click',e=>{const b=e.target.closest('.copy');if(b&&b.dataset.code){copyText(b.dataset.code,()=>{const o=b.innerHTML;b.innerHTML='✓ Copié';b.classList.add('done');toast('« '+b.dataset.code+' » copié ✓');setTimeout(()=>{b.innerHTML=o;b.classList.remove('done')},1400);});}});\n"
    "const _burger=$('#burger');if(_burger)_burger.addEventListener('click',()=>{const m=$('#mobileMenu');const o=m.classList.toggle('open');_burger.setAttribute('aria-expanded',o);_burger.textContent=o?'✕':'☰';});\n"
    "const _te=$('#toggleExp');if(_te)_te.addEventListener('click',()=>{const l=$('#expiredList');const open=l.classList.toggle('open');_te.setAttribute('aria-expanded',open);_te.textContent=(open?'▾ Masquer':'▸ Afficher')+' les codes expirés ('+(l.dataset.count||0)+')';});\n"
    "$$('.q button').forEach(b=>b.addEventListener('click',()=>{const q=b.parentElement,open=q.classList.contains('open');$$('.q').forEach(x=>{x.classList.remove('open');x.querySelector('button').setAttribute('aria-expanded','false')});if(!open){q.classList.add('open');b.setAttribute('aria-expanded','true');}}));\n"
    "const _ca=$('#copyAll');if(_ca)_ca.addEventListener('click',()=>{const all=$$('#activeList .copy').map(b=>b.dataset.code).join('\\n');if(all)copyText(all,()=>toast('Codes copiés ✓'));});\n"
    "</script>")

def cover_html(game, cls="cover"):
    """Vignette de marque (monogramme sur dégradé) — jamais de faux visuel."""
    a = game.get("accent", ["#7c5cff", "#4d9bff"])
    return ('<div class="%s" style="background:linear-gradient(135deg,%s,%s);display:grid;place-items:center">'
            '<span style="font-weight:900;font-size:2rem;color:#fff;letter-spacing:-1px">%s</span></div>') % (
            cls, e(a[0]), e(a[1]), e(game.get("monogram", game["name"][:2].upper())))

def e_att(s):
    return html.escape(str(s), quote=True) if s is not None else ""

def ghero(g, h1_html, meta_html="", sub_html=""):
    """Hero de page avec bannière image RÉELLE en fond (miniature du jeu) si disponible.
    Retombe sur un hero uni si le jeu n'a pas de coverImage. Jamais de SVG en fond."""
    ci = g.get("coverImage")
    stock = g.get("stockBanner")  # image libre de droit (hotlink) — fallback si pas de cover jeu
    src = ci or stock
    if src:
        pos = g.get("coverPosition", "center")
        cls = " ghero--img"
        style = ' style="--cover:url(%s);--covpos:%s"' % (e_att(src), e_att(pos))
        bg = '<div class="ghero-bg" aria-hidden="true"></div>'
    else:
        cls = style = bg = ""
    inner = "<h1>%s</h1>" % h1_html
    if meta_html:
        inner += '<div class="meta">%s</div>' % meta_html
    inner += sub_html
    return '<section class="ghero%s"%s>%s<div class="info">%s</div></section>' % (cls, style, bg, inner)

def elements_panel(data):
    """Légende visuelle des éléments (codée, sans photo). '' si absent."""
    els = data.get("elements", [])
    if not els:
        return ""
    def mm(x):
        s = x.get("strong"); w = x.get("weak")
        if not s and not w:
            return '<span class="el-mm el-tbc">contres à confirmer</span>'
        out = ""
        if s: out += '<span class="el-up">▲ fort : %s</span>' % e_att(" · ".join(s))
        if w: out += '<span class="el-dn">▼ faible : %s</span>' % e_att(" · ".join(w))
        return '<span class="el-mm">%s</span>' % out
    chips = "".join(
        '<div class="el-chip" style="--c:%s"><span class="el-top"><span class="el-ico">%s</span><strong>%s</strong></span>%s</div>'
        % (e_att(x.get("color", "#7c5cff")), e_att(x.get("icon", "•")), e_att(x["name"]), mm(x)) for x in els)
    note = ('<p class="sub" style="margin-top:12px">%s</p>' % e_att(data["elementsNote"])) if data.get("elementsNote") else ""
    pb = data.get("prismanaBest")
    prismana = ""
    if pb and pb.get("picks"):
        pills = "".join('<span class="pill" style="background:var(--surface-2)">%s</span>' % e_att(x) for x in pb["picks"])
        prismana = ('<section class="panel"><div class="panel-head"><h2>💎 Meilleurs Aniimo Prismana</h2></div>'
                    '<p class="sub">%s</p><div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:8px">%s</div></section>') % (
                    e_att(pb.get("note", "")), pills)
    return ('<section class="panel"><div class="panel-head"><h2>🌈 Les %d éléments &amp; leurs contres</h2></div>'
            '<div class="el-grid">%s</div>%s</section>%s') % (len(els), chips, note, prismana)

# ---------- helpers annuaire ----------
FR_ABBR = {"janv.":1,"jan.":1,"févr.":2,"fév.":2,"mars":3,"avr.":4,"mai":5,"juin":6,
           "juil.":7,"juill.":7,"août":8,"aout":8,"sept.":9,"sep.":9,"oct.":10,"nov.":11,"déc.":12,"dec.":12}
def fr_abbr_to_iso(s):
    m = re.match(r"(\d{1,2})\s+([A-Za-zéûôàè.]+)\s+(\d{4})", (s or "").strip())
    if not m: return "0000-00-00"
    d, mon, y = m.groups()
    mo = FR_ABBR.get(mon.lower(), 0)
    return "%04d-%02d-%02d" % (int(y), mo, int(d))

KNOWN_GENRES = ["Simulateur","Anime","Combat","RPG","Tycoon","Tower Defense","Sport","Obby","Horreur","Aventure","Stratégie"]
def derive_genres(genre_str):
    g = (genre_str or "").lower()
    found = [k for k in KNOWN_GENRES if k.lower() in g]
    return found or ([genre_str] if genre_str else [])

def platforms_of_standalone(game):
    labels = " ".join(game.get("platforms", [])).lower()
    out = []
    if any(k in labels for k in ["pc","steam","epic","playstation","ps5","xbox","console","switch"]): out.append("PC / Console")
    if any(k in labels for k in ["ios","android","mobile"]): out.append("Mobile")
    return out or ["PC / Console"]

def load_roblox_games():
    h = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    i = h.find("const GAMES = [")
    if i == -1: return []
    i += len("const GAMES = ")
    depth = 0
    for k in range(i, len(h)):
        if h[k] == "[": depth += 1
        elif h[k] == "]":
            depth -= 1
            if depth == 0:
                return json.loads(h[i:k+1])
    return []

# ---------- rendu : annuaire /games/ ----------
def build_directory(games):
    entries = []
    # jeux standalone (data/games/*.json) — mis en avant
    for g in games:
        if not g.get("isActive", True): continue
        plats = platforms_of_standalone(g)
        genres = derive_genres(g.get("genre", ""))
        cts = [ct["label"] for ct in g.get("contentTypes", []) if ct["status"] == "available"] or ["Hub"]
        entries.append({
            "name": g["name"], "slug": g["slug"], "url": "/games/%s/" % g["slug"],
            "source": "standalone", "platforms": plats, "genres": genres,
            "updated": g.get("releaseDate", "0000-00-00"), "new": bool(g.get("isNew") or g.get("isFeatured")),
            "thumb": g.get("coverImage"), "coverpos": g.get("coverPosition"), "accent": g.get("accent", ["#7c5cff","#4d9bff"]),
            "monogram": g.get("monogram", g["name"][:2].upper()), "cts": cts,
            "platformLabel": " · ".join(plats), "genreLabel": genres[0] if genres else "",
        })
    # types de contenu réellement présents (pour badges data-driven)
    guide_slugs = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "guides", "*.html"))}
    tier_slugs = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "tier-list", "*.html"))}
    # jeux Roblox (const GAMES d'index.html)
    for g in load_roblox_games():
        cts = ["Codes"]
        if g["slug"] in guide_slugs: cts.append("Guides")
        if g.get("tier") or g["slug"] in tier_slugs: cts.append("Tier list")
        entries.append({
            "name": g["name"], "slug": g["slug"], "url": "/codes-%s.html" % g["slug"],
            "source": "roblox", "platforms": ["Roblox"], "genres": [g.get("cat","")],
            "updated": fr_abbr_to_iso(g.get("date","")), "new": g.get("tag") == "new",
            "hot": g.get("tag") == "hot", "thumb": g.get("thumb"), "cts": cts,
            "platformLabel": "Roblox", "genreLabel": g.get("cat",""),
        })

    # options de filtres (uniquement ce qui existe réellement)
    plat_present = []
    for p in ["Roblox", "PC / Console", "Mobile"]:
        if any(p in e["platforms"] for e in entries): plat_present.append(p)
    genre_present = sorted({g for e in entries for g in e["genres"] if g})

    def card(e):
        low_name = e["name"].lower().replace('"', "")
        dp = "|".join(p.lower() for p in e["platforms"])
        dg = "|".join(g.lower() for g in e["genres"] if g)
        badge = ""
        if e.get("new"): badge = '<span class="badge" style="background:linear-gradient(100deg,#7c5cff,#4d9bff)">Nouveau</span>'
        elif e.get("hot"): badge = '<span class="badge">🔥 Populaire</span>'
        if e["thumb"]:
            posstyle = (' style="object-position:%s"' % e["coverpos"]) if e.get("coverpos") else ''
            thumb = ('<div class="thumb"><img src="%s" alt="Miniature %s" loading="lazy" decoding="async"%s '
                     'onerror="this.onerror=null;this.src=\'/images/games/%s.svg\'">%s</div>' % (
                     e["thumb"], e_att(e["name"]), posstyle, e["slug"], badge))
        else:
            a = e.get("accent", ["#7c5cff","#4d9bff"])
            thumb = ('<div class="thumb" style="background:linear-gradient(135deg,%s,%s);display:grid;place-items:center">'
                     '<span style="font-weight:900;font-size:1.9rem;color:#fff">%s</span>%s</div>' % (
                     a[0], a[1], e.get("monogram","?"), badge))
        cts = "".join("<span>%s</span>" % e_att(c) for c in e["cts"])
        return ('<a class="gcard" data-name="%s" data-platform="%s" data-genre="%s" data-updated="%s" data-new="%d" href="%s">'
                '%s<div class="body"><h3>%s</h3><span class="plat">%s · %s</span>'
                '<span class="cts">%s</span>'
                '<div class="cta"><span class="btn btn-primary btn-sm">Explorer →</span></div></div></a>') % (
                e_att(low_name), dp, dg, e["updated"], 1 if e.get("new") else 0, e["url"],
                thumb, e_att(e["name"]), e_att(e["platformLabel"]), e_att(e["genreLabel"]), cts)

    cards = "".join(card(e) for e in entries)

    def chips(group_id, values):
        out = ['<button class="chip active" data-val="all">Tous</button>']
        for v in values:
            out.append('<button class="chip" data-val="%s">%s</button>' % (e_att(v.lower()), e_att(v)))
        return '<div class="chips" id="%s">%s</div>' % (group_id, "".join(out))

    toolbar = (
        '<div class="dir-toolbar">'
        '<div class="dir-search"><span class="search-ico" aria-hidden="true">🔍</span>'
        '<label for="gameSearch" class="skip">Rechercher un jeu</label>'
        '<input id="gameSearch" type="search" placeholder="Blox Fruits, Aniimo, GTA 6…" autocomplete="off"></div>'
        '<div class="filter-row">'
        '<div class="filter-group"><span class="flabel">Plateforme</span>%s</div>'
        '<div class="filter-group"><span class="flabel">Genre</span>%s</div>'
        '<div class="dir-sort"><label for="sortSel">Trier :</label>'
        '<select id="sortSel"><option value="recent">Récemment mis à jour</option>'
        '<option value="az">A → Z</option></select></div>'
        '</div></div>') % (chips("platChips", plat_present), chips("genreChips", genre_present))

    # ---- Section "À découvrir" (featured : Roblox + jeux standalone) ----
    roblox_count = sum(1 for e in entries if e["source"] == "roblox")
    def feat_roblox():
        return ('<a class="fcard" href="/tous-les-codes.html">'
            '<div class="fimg"><img src="/images/hero-bg.webp" alt="Roblox — jeux et codes" loading="lazy" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:left center"></div>'
            '<div class="fbody"><h3>Roblox</h3>'
            '<span style="color:var(--muted);font-size:.85rem">Plateforme · %d jeux</span>'
            '<span class="ct-list"><span>Codes</span><span>Guides</span><span>Tier lists</span></span>'
            '<span class="btn btn-primary btn-sm" style="align-self:flex-start;margin-top:6px">Explorer Roblox →</span>'
            '</div></a>') % roblox_count
    def feat_standalone(g):
        plats = platforms_of_standalone(g); genres = derive_genres(g.get("genre", ""))
        avail = [ct["label"] for ct in g.get("contentTypes", []) if ct["status"] == "available"]
        soon = [ct["label"] for ct in g.get("contentTypes", []) if ct["status"] == "soon"][:2]
        ctshtml = ("".join("<span>%s</span>" % e_att(c) for c in avail) +
                   "".join('<span style="opacity:.5">%s · bientôt</span>' % e_att(c) for c in soon))
        a = g.get("accent", ["#7c5cff", "#4d9bff"])
        badge = ('<span class="badge" style="position:absolute;top:12px;left:12px;background:linear-gradient(100deg,#7c5cff,#4d9bff)">Nouveau</span>'
                 if (g.get("isNew") or g.get("isFeatured")) else "")
        cover = g.get("coverImage")
        pos = g.get("coverPosition", "center")
        if cover:
            fimg = '<div class="fimg">%s<img src="%s" alt="%s" loading="lazy" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:%s"></div>' % (badge, cover, e_att(g["name"]), pos)
        else:
            fimg = '<div class="fimg" style="background:linear-gradient(135deg,%s,%s)">%s<span style="font-weight:900;font-size:2.2rem;color:#fff;letter-spacing:-1px">%s</span></div>' % (a[0], a[1], badge, e_att(g["name"]))
        return ('<a class="fcard" href="/games/%s/">%s'
            '<div class="fbody"><h3>%s</h3>'
            '<span style="color:var(--muted);font-size:.85rem">%s · %s</span>'
            '<span class="ct-list">%s</span>'
            '<span class="btn btn-primary btn-sm" style="align-self:flex-start;margin-top:6px">Explorer %s →</span>'
            '</div></a>') % (g["slug"], fimg, e_att(g["name"]),
                             e_att(" · ".join(plats)), e_att(genres[0] if genres else ""), ctshtml, e_att(g["name"]))
    featured = feat_roblox() + "".join(feat_standalone(g) for g in games if g.get("isActive", True))

    body = (crumb_html([("Accueil", "/"), ("Jeux", None)]) +
        '<section class="ghero"><div class="info"><h1>Tous les jeux</h1>'
        '<p class="prose" style="margin-top:8px">Explore les jeux suivis par Zoneblox et découvre, pour chacun, '
        'ses codes, guides, tier lists, bases de données et actualités.</p></div></section>'
        '<div style="margin-top:26px;display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap">'
        '<h2 style="font-size:1.4rem">🔥 À découvrir</h2>'
        '<span style="color:var(--muted-2);font-size:.85rem">Sélection Zoneblox</span></div>'
        '<div class="featured-grid">' + featured + '</div>'
        '<h2 style="font-size:1.4rem;margin-top:36px;margin-bottom:4px">🎮 Le catalogue complet</h2>'
        + toolbar +
        '<p class="dir-count" id="dirCount" aria-live="polite"></p>'
        '<div class="grid-cards" id="gamesGrid">' + cards + '</div>'
        '<div class="empty-state" id="emptyState" hidden>Aucun jeu ne correspond à ta recherche. '
        '<button class="chip" onclick="location.reload()">Réinitialiser</button></div>')

    itemlist = json.dumps({"@context": "https://schema.org", "@type": "ItemList",
        "name": "Jeux couverts par Zoneblox", "numberOfItems": len(entries),
        "itemListElement": [{"@type": "ListItem", "position": i+1, "name": e["name"], "url": SITE + e["url"]}
                            for i, e in enumerate(entries)]}, ensure_ascii=False)
    ld = [itemlist, crumb_ld([("Accueil", "/"), ("Jeux", "/games/")])]

    dir_js = r"""<script>
(function(){
  var grid=document.getElementById('gamesGrid');if(!grid)return;
  var cards=[].slice.call(grid.children);
  var search=document.getElementById('gameSearch');
  var countEl=document.getElementById('dirCount');
  var empty=document.getElementById('emptyState');
  var sortSel=document.getElementById('sortSel');
  var state={q:'',plat:'all',genre:'all',sort:'recent'};
  function group(id,key){var g=document.getElementById(id);if(!g)return;
    g.addEventListener('click',function(ev){var c=ev.target.closest('.chip');if(!c)return;
      [].forEach.call(g.querySelectorAll('.chip'),function(x){x.classList.remove('active')});
      c.classList.add('active');state[key]=c.dataset.val;apply();});}
  group('platChips','plat');group('genreChips','genre');
  if(search)search.addEventListener('input',function(){state.q=search.value.trim().toLowerCase();apply();});
  if(sortSel)sortSel.addEventListener('change',function(e){state.sort=e.target.value;apply();});
  function apply(){
    var vis=0;
    cards.forEach(function(c){
      var okQ=!state.q||c.dataset.name.indexOf(state.q)>-1;
      var okP=state.plat==='all'||c.dataset.platform.split('|').indexOf(state.plat)>-1;
      var okG=state.genre==='all'||c.dataset.genre.split('|').indexOf(state.genre)>-1;
      var show=okQ&&okP&&okG;c.classList.toggle('hide',!show);if(show)vis++;
    });
    var sorted=cards.slice().sort(function(a,b){
      if(state.sort==='recent')return (b.dataset.updated||'').localeCompare(a.dataset.updated||'')||a.dataset.name.localeCompare(b.dataset.name);
      return a.dataset.name.localeCompare(b.dataset.name);
    });
    sorted.forEach(function(c){grid.appendChild(c);});
    if(countEl)countEl.textContent=vis+' jeu'+(vis>1?'x':'')+' trouvé'+(vis>1?'s':'');
    if(empty)empty.hidden=vis>0;
  }
  apply();
})();
</script>"""

    htmlp = page("Jeux vidéo : codes, guides, tier lists & actualités | Zoneblox",
        "L'annuaire des jeux couverts par Zoneblox : recherche et filtres pour trouver les codes, guides et tier lists de Roblox, Aniimo et d'autres jeux.",
        SITE + "/games/", body, active="games", extra_ld=ld, extra_js=dir_js)
    write("games/index.html", htmlp)

    # index JSON réutilisable (recherche globale future)
    write("data/games-index.json", json.dumps({"generated": datetime.date.today().isoformat(),
        "count": len(entries), "games": entries}, ensure_ascii=False, indent=1))
    return SITE + "/games/"

# ---------- rendu : hub d'un jeu ----------
def build_hub(g):
    slug = g["slug"]
    meta = []
    meta.append('<span class="pill">🎮 %s</span>' % e(g.get("genre", "")))
    if g.get("publisher"):
        meta.append('<span class="pill">🏷️ %s</span>' % e(g["publisher"]))
    if g.get("releaseDate"):
        meta.append('<span class="pill">📅 %s</span>' % e(fr_date(g["releaseDate"])))
    meta.append('<span class="pill">🕹️ %s</span>' % e(", ".join(g.get("platforms", []))))
    # chips content-type nav
    chips = []
    for ct in g["contentTypes"]:
        if ct["status"] == "available":
            chips.append('<a href="/games/%s/%s/"><span class="ci">%s</span>%s</a>' % (
                slug, ct["type"], ct["icon"], e(ct["label"])))
    ct_nav = ('<div class="ct-nav">' + "".join(chips) + "</div>") if chips else ""
    # content-type grid
    cards = []
    for ct in g["contentTypes"]:
        if ct["status"] == "available":
            cards.append('<a class="ct-card" href="/games/%s/%s/"><span class="ic">%s</span>'
                '<span><h3>%s</h3><p>%s</p></span></a>' % (
                slug, ct["type"], ct["icon"], e(ct["label"]), e(ct.get("blurb", ""))))
        else:
            cards.append('<span class="ct-card soon"><span class="ic">%s</span>'
                '<span><h3>%s <span style="font-size:.7rem;color:var(--muted-2)">· bientôt</span></h3>'
                '<p>%s</p></span></span>' % (ct["icon"], e(ct["label"]), e(ct.get("blurb", ""))))
    # official link
    off = ('<span class="pill">🔗 <a href="%s" rel="nofollow noopener" target="_blank" style="color:var(--text)">Site officiel</a></span>'
           % e(g["officialWebsite"])) if g.get("officialWebsite") else ""
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], None)]) +
        '<section class="ghero">%s<div class="info"><h1>%s</h1>'
        '<div class="meta">%s %s</div></div></section>'
        '<p class="prose" style="margin-top:18px">%s</p>%s'
        '<section class="panel"><div class="panel-head"><h2>📂 Contenu %s</h2></div>'
        '<p class="sub">Toutes les ressources Zoneblox pour %s. De nouvelles sections arrivent régulièrement.</p>'
        '<div class="ct-grid">%s</div></section>'
        '<section class="panel"><h2>À propos d\'%s</h2><p class="prose">%s</p>'
        '<p class="prose">%s</p></section>'
        '%s') % (
        cover_html(g), e(g["name"]), "".join(meta), off,
        e(g.get("description", "")), ct_nav,
        e(g["name"]), e(g["name"]), "".join(cards),
        e(g["name"]), e(g.get("description", "")), e(g.get("releaseNote", "")),
        hub_faq(g))
    # VideoGame + Breadcrumb JSON-LD
    vg = {"@context": "https://schema.org", "@type": "VideoGame", "name": g["name"],
          "description": g.get("shortDescription", ""), "genre": g.get("genre", ""),
          "gamePlatform": g.get("platforms", []), "applicationCategory": "Game"}
    if g.get("publisher"):
        vg["publisher"] = {"@type": "Organization", "name": g["publisher"]}
    if g.get("releaseDate"):
        vg["datePublished"] = g["releaseDate"]
    if g.get("officialWebsite"):
        vg["url"] = g["officialWebsite"]
    ld = [json.dumps(vg, ensure_ascii=False),
          crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug)])]
    htmlp = page("%s — Codes, guides & tier list | Zoneblox" % g["name"],
        "%s : codes actifs, guides, tier list et actualités. %s" % (g["name"], g.get("shortDescription", "")),
        SITE + "/games/%s/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/index.html" % slug, htmlp)
    return SITE + "/games/%s/" % slug

def hub_faq(g):
    faqs = [
        ("Qu'est-ce que %s ?" % g["name"], g.get("description", "")),
        ("Sur quelles plateformes jouer à %s ?" % g["name"], g.get("releaseNote", "")),
        ("%s est-il gratuit ?" % g["name"], "Oui, %s est un jeu free-to-play." % g["name"] if "free-to-play" in g.get("description","").lower() or "free-to-play" in g.get("genre","").lower() else "Consulte le site officiel pour le modèle économique à jour."),
    ]
    qhtml = "".join('<div class="q"><button aria-expanded="false"><span>%s</span><span class="plus">+</span></button>'
                    '<div class="a"><p>%s</p></div></div>' % (e(q), e(a)) for q, a in faqs if a)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in faqs if a]}, ensure_ascii=False)
    return ('<section class="panel" id="faq"><h2>❓ Questions fréquentes</h2><div class="faq">%s</div>'
            '<script type="application/ld+json">%s</script></section>') % (qhtml, ld)

# ---------- rendu : page codes ----------
def build_codes(g, data):
    slug = g["slug"]
    now = datetime.date.today()
    cur_month, cur_year = FR_MONTHS[now.month], now.year
    active = data.get("active", [])
    expired = data.get("expired", [])
    checked = fr_date(data.get("lastChecked", ""))
    n = len(active)
    active_html = "".join(
        '<div class="code"><div class="val"><code>%s</code>%s</div>'
        '<div class="desc"><div class="reward">🎁 %s</div>%s</div>'
        '<button class="copy" data-code="%s">📋 Copier</button></div>' % (
            e(c["code"]), '<span class="new">NOUVEAU</span>' if c.get("new") else "",
            e(c["reward"]),
            ('<div class="tag">Ajouté le %s · vérifié le %s</div>' % (fr_date(c.get("added","")), fr_date(c.get("verified","")))) if c.get("added") else "",
            e(c["code"])) for c in active) or '<p class="prose" style="color:var(--muted)">Aucun code actif pour le moment — cette page est vérifiée chaque jour, reviens bientôt.</p>'
    if expired:
        exp_html = "".join('<div class="code"><div class="val"><code>%s</code></div>'
            '<div class="desc"><div class="tag">Expiré</div></div></div>' % e(c["code"]) for c in expired)
        exp_block = ('<section class="panel" id="expires"><div class="panel-head"><h2>💀 Codes expirés</h2></div>'
            '<p class="sub">On les garde pour référence — inutile de les essayer.</p>'
            '<button class="toggle-exp" id="toggleExp" aria-expanded="false">▸ Afficher les codes expirés (%d)</button>'
            '<div class="expired" id="expiredList" data-count="%d">%s</div></section>' % (len(expired), len(expired), exp_html))
    else:
        exp_block = ('<section class="panel" id="expires"><div class="panel-head"><h2>💀 Codes expirés</h2></div>'
            '<p class="prose" style="color:var(--muted)">Aucun code expiré connu à ce jour — %s est récent. '
            'Les codes retirés seront listés ici et datés.</p></section>' % e(g["name"]))
    # redeem steps
    steps = "".join('<div class="step"><div class="n">%d</div><p>%s</p></div>' % (i + 1, e(s))
                    for i, s in enumerate(data.get("redeem", {}).get("steps", [])))
    # faq
    faqs = data.get("faqs", [])
    faq_html = "".join('<div class="q"><button aria-expanded="false"><span>%s</span><span class="plus">+</span></button>'
        '<div class="a"><p>%s</p></div></div>' % (e(f["q"]), e(f["a"])) for f in faqs)
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                       for f in faqs]}, ensure_ascii=False)
    itemlist_ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList",
        "name": "Codes %s actifs" % g["name"],
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["code"]}
                            for i, c in enumerate(active)]}, ensure_ascii=False)
    # sources
    src = data.get("sources", [])
    src_html = ""
    if src:
        src_html = ('<section class="panel"><h2>🔎 Sources</h2><p class="sub">Codes vérifiés en croisant plusieurs sources fiables.</p>'
            '<div class="prose"><p>' + " · ".join('<a href="%s" rel="nofollow noopener" target="_blank" style="color:var(--primary-2)">%s</a>'
            % (e(u), e(re.sub(r"https?://(www\.)?([^/]+).*", r"\2", u))) for u in src) + '</p></div></section>')
    # related content
    rel = ['<a href="/games/%s/">🏠 Hub %s</a>' % (slug, e(g["name"]))]
    for ct in g["contentTypes"]:
        if ct["type"] != "codes" and ct["status"] == "available":
            rel.append('<a href="/games/%s/%s/">%s %s</a>' % (slug, ct["type"], ct["icon"], e(ct["label"])))
    rel.append('<a href="/games/">🎮 Tous les jeux</a>')
    related = ('<div class="box"><h3>Aussi sur %s</h3><div class="related">%s</div></div>' % (
        e(g["name"]), "".join('<a href="%s"><span class="tn" style="background:var(--grad)">→</span>'
        '<span><div class="rn">%s</div></span></a>' % (
            re.search(r'href="([^"]+)"', r).group(1), re.sub(r"<[^>]+>", "", r)) for r in rel)))
    note = ('<p class="prose" style="color:var(--muted-2);font-size:.85rem;margin-top:10px">%s</p>' % e(data["note"])) if data.get("note") else ""

    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Codes", None)]) +
        '<div class="layout"><div>'
        '<section class="ghero">%s<div class="info"><h1>Codes %s — %s %d</h1>'
        '<div class="meta"><span class="pill ok"><span class="pulse"></span> %d code%s actif%s</span>'
        '<span class="pill">🔄 Vérifié le <strong id="verifDate" style="color:var(--text);margin-left:4px">%s</strong></span>'
        '<span class="pill">✍️ Par <a href="/a-propos.html#editorial" style="color:var(--text)">L\'équipe Zoneblox</a></span></div></div></section>'
        '<p class="prose" style="margin-top:18px">Voici <strong>tous les codes %s actifs</strong>, vérifiés à la main et mis à jour. '
        'Copie un code en un clic puis échange-le en jeu. Les codes sont <strong>sensibles à la casse</strong>.</p>'
        '<section class="panel" id="actifs"><div class="panel-head"><h2>🎁 Codes actifs</h2>'
        '<button class="btn btn-primary btn-sm" id="copyAll">📋 Tout copier</button></div>'
        '<p class="sub">Clique sur un code pour le copier. Il sera collé tel quel dans le jeu.</p>'
        '<div class="codes-list" id="activeList">%s</div></section>'
        '%s'
        '<section class="panel" id="guide"><div class="panel-head"><h2>📖 Comment échanger un code %s</h2></div>'
        '<p class="sub">%s</p><div class="steps">%s</div></section>'
        '<section class="panel"><h2>❌ Pourquoi mon code ne fonctionne pas ?</h2>'
        '<p class="prose">Trois causes reviennent presque toujours. <strong>Le code a expiré</strong> : s\'il n\'est plus dans la liste active ci-dessus, il est sans doute mort. '
        '<strong>Une faute de casse</strong> : les codes sont sensibles à la casse, utilise le bouton Copier. '
        '<strong>Déjà utilisé</strong> : chaque code n\'est valable qu\'une seule fois par compte.</p>%s</section>'
        '%s'
        '<section class="panel" id="faq"><h2>❓ Questions fréquentes</h2><div class="faq">%s</div></section>'
        '</div>'
        '<aside class="side">%s'
        '<div class="box"><h3>Sur cette page</h3><nav class="toc"><a href="#actifs">🎁 Codes actifs</a>'
        '<a href="#expires">💀 Codes expirés</a><a href="#guide">📖 Comment échanger</a><a href="#faq">❓ FAQ</a></nav></div>'
        '</aside></div>') % (
        cover_html(g), e(g["name"]), e(cur_month.capitalize()), cur_year,
        n, "s" if n > 1 else "", "s" if n > 1 else "", checked,
        e(g["name"]), active_html, exp_block, e(g["name"]),
        e(data.get("redeem", {}).get("intro", "")), steps, note, src_html, faq_html, related)
    ld = [itemlist_ld, faq_ld,
          crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Codes", "/games/%s/codes/" % slug)])]
    htmlp = page("Codes %s (%s %d) — Codes actifs & récompenses | Zoneblox" % (g["name"], cur_month, cur_year),
        "Tous les codes %s actifs de %s %d, vérifiés à la main : récompenses, date de vérification et comment les échanger en jeu." % (g["name"], cur_month, cur_year),
        SITE + "/games/%s/codes/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/codes/index.html" % slug, htmlp)
    return SITE + "/games/%s/codes/" % slug

# ---------- rendu : liens croisés (maillage interne) ----------
def related_box(g, current):
    links = ['<a href="/games/%s/">🏠 Hub %s</a>' % (g["slug"], e_att(g["name"]))]
    icons = {"codes": "🎁", "guides": "📖", "tier-list": "📊", "videos": "🎬", "creatures": "🐾", "locations": "🗺️", "updates": "📰"}
    for ct in g.get("contentTypes", []):
        if ct["type"] == current or ct["status"] != "available":
            continue
        links.append('<a href="/games/%s/%s/">%s %s</a>' % (g["slug"], ct["type"], icons.get(ct["type"], "•"), e_att(ct["label"])))
    if current != "videos" and any(ct["type"] == "videos" and ct["status"] == "available" for ct in g.get("contentTypes", [])):
        pass
    items = "".join('<a href="%s"><span class="tn" style="background:var(--grad)">→</span><span><div class="rn">%s</div></span></a>'
                    % (re.search(r'href="([^"]+)"', l).group(1), re.sub(r"<[^>]+>", "", l)) for l in links)
    return '<div class="box"><h3>Aussi sur %s</h3><div class="related">%s</div></div>' % (e_att(g["name"]), items)

def sources_html(sources):
    if not sources:
        return ""
    def one(s):
        if isinstance(s, str):
            url = s; name = s.split("//")[-1].split("/")[0]
        else:
            url = s["url"]; name = s.get("name", s["url"])
        return '<a href="%s" rel="nofollow noopener" target="_blank" style="color:var(--primary-2)">%s</a>' % (e_att(url), e_att(name))
    return ('<section class="panel"><h2>🔎 Sources</h2><p class="sub">Informations croisées entre plusieurs sources ; vérifie toujours en jeu.</p>'
            '<div class="prose"><p>' + " · ".join(one(s) for s in sources) + '</p></div></section>')

# ---------- rendu : guides ----------
def build_guides(g, data):
    slug = g["slug"]
    guides = data.get("guides", [])
    urls = []
    # pages articles
    for gd in guides:
        gs = gd["slug"]
        toc = "".join('<a href="#%s">%s</a>' % (i, e_att(s["h"])) for i, s in
                      [("s%d" % k, s) for k, s in enumerate(gd.get("sections", []))])
        secs = "".join('<section class="panel"><h2 id="s%d">%s</h2><p class="prose">%s</p></section>'
                       % (k, e_att(s["h"]), e_att(s["p"])) for k, s in enumerate(gd.get("sections", [])))
        faqs = gd.get("faqs", [])
        faq_html = "".join('<div class="q"><button aria-expanded="false"><span>%s</span><span class="plus">+</span></button>'
            '<div class="a"><p>%s</p></div></div>' % (e_att(f["q"]), e_att(f["a"])) for f in faqs)
        faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faqs]}, ensure_ascii=False)
        art_ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": gd["title"],
            "datePublished": gd.get("updated", data.get("updated", "")), "dateModified": gd.get("updated", data.get("updated", "")),
            "author": {"@type": "Organization", "name": "L'équipe Zoneblox"}}, ensure_ascii=False)
        hero = ghero(g, e_att(gd["title"]),
            '<span class="pill">📖 %s</span>'
            '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
            '<span class="pill">✍️ Par <a href="/a-propos.html#editorial" style="color:var(--text)">L\'équipe Zoneblox</a></span>'
            % (e_att(gd.get("category", "Guide")), fr_date(gd.get("updated", ""))))
        body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", "/games/%s/guides/" % slug), (gd["title"], None)]) +
            '<div class="layout"><div>'
            + hero +
            '<p class="prose" style="margin-top:18px">%s</p>'
            '%s'
            '%s'
            '%s'
            '</div><aside class="side">%s'
            '<div class="box"><h3>Sur cette page</h3><nav class="toc">%s</nav></div></aside></div>') % (
            e_att(gd.get("intro", "")), secs,
            ('<section class="panel" id="faq"><h2>❓ Questions fréquentes</h2><div class="faq">%s</div></section>' % faq_html) if faqs else "",
            sources_html(data.get("sources", [])),
            related_box(g, "guides"), toc)
        ld = [art_ld, crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", "/games/%s/guides/" % slug), (gd["title"], "/games/%s/guides/%s/" % (slug, gs))])]
        if faqs:
            ld.append(faq_ld)
        htmlp = page("%s | Zoneblox" % gd["title"],
            e(gd.get("intro", ""))[:158],
            SITE + "/games/%s/guides/%s/" % (slug, gs), body, active="games", extra_ld=ld)
        write("games/%s/guides/%s/index.html" % (slug, gs), htmlp)
        urls.append(SITE + "/games/%s/guides/%s/" % (slug, gs))
    # hub guides
    cards = "".join('<a class="gcard" href="/games/%s/guides/%s/"><div class="body"><h3>%s</h3>'
        '<span class="plat">%s</span><p>%s</p><div class="cta"><span class="btn btn-primary btn-sm">Lire →</span></div></div></a>'
        % (slug, gd["slug"], e_att(gd["title"]), e_att(gd.get("category", "Guide")), e_att(gd.get("intro", "")[:110] + "…")) for gd in guides)
    hub_hero = ghero(g, "Guides %s" % e_att(g["name"]), "",
        '<p class="prose" style="margin-top:8px">Nos guides pour débuter et progresser dans %s. '
        'De nouveaux guides arrivent au fil des découvertes.</p>' % e_att(g["name"]))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", None)]) +
        hub_hero + '<div class="grid-cards" style="margin-top:22px">%s</div>') % cards
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", "/games/%s/guides/" % slug)])]
    htmlp = page("Guides %s — débuter & progresser | Zoneblox" % g["name"],
        "Tous les guides Zoneblox pour %s : guide débutant, mécaniques, progression. Vérifiés et sourcés." % g["name"],
        SITE + "/games/%s/guides/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/guides/index.html" % slug, htmlp)
    urls.append(SITE + "/games/%s/guides/" % slug)
    return urls

# ---------- rendu : tier list ----------
def build_tierlist(g, data):
    slug = g["slug"]
    tiers_html = ""
    for t in data.get("tiers", []):
        chips = "".join('<span class="pill" style="background:var(--surface-2)">%s</span>' % e_att(x) for x in t.get("entries", []))
        tiers_html += ('<div style="display:flex;gap:14px;align-items:flex-start;background:var(--bg-2);border:1px solid var(--border);'
            'border-radius:14px;padding:14px;margin-bottom:12px">'
            '<span style="flex:none;width:52px;height:52px;border-radius:12px;background:%s;display:grid;place-items:center;'
            'font-weight:900;font-size:1.5rem;color:#0a0b16">%s</span>'
            '<div><div style="display:flex;flex-wrap:wrap;gap:6px">%s</div>'
            '<p style="color:var(--muted);font-size:.82rem;margin-top:6px">%s</p></div></div>') % (
            e_att(t.get("color", "#7c5cff")), e_att(t["label"]), chips, e_att(t.get("note", "")))
    rc = data.get("roleColors", {})
    roles_html = "".join('<div class="step role-step" style="--c:%s"><div class="role-badge" style="background:%s">%s</div>'
        '<h3 style="margin-top:10px">%s</h3><p>%s</p></div>' % (
        e_att(rc.get(r["role"], "#7c5cff")), e_att(rc.get(r["role"], "#7c5cff")), e_att(r["role"]),
        e_att(" · ".join(r["picks"])), e_att(r.get("why", "")))
        for r in data.get("rolePicks", []))
    entries = [x for t in data.get("tiers", []) for x in t.get("entries", [])]
    itemlist = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "Tier list %s" % g["name"],
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x} for i, x in enumerate(entries)]}, ensure_ascii=False)
    hero = ghero(g, "Tier list %s : les meilleures créatures" % e_att(g["name"]),
        '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
        '<span class="pill">✍️ L\'équipe Zoneblox</span>' % fr_date(data.get("updated", "")))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Tier list", None)]) +
        '<div class="layout"><div>' + hero +
        '<p class="prose" style="margin-top:18px">%s</p>'
        '<section class="panel"><div class="panel-head"><h2>🏆 Classement</h2></div>%s</section>'
        '%s'
        '<section class="panel"><div class="panel-head"><h2>🎯 Meilleurs choix par rôle</h2></div>'
        '<p class="sub">Une bonne équipe mélange au moins 3 rôles (DPS, Heal, Support, Break, Regen).</p>'
        '<div class="steps">%s</div></section>'
        '%s'
        '</div><aside class="side">%s</aside></div>') % (
        e_att(data.get("methodology", "")), tiers_html, elements_panel(data),
        roles_html, sources_html(data.get("sources", [])), related_box(g, "tier-list"))
    ld = [itemlist, crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Tier list", "/games/%s/tier-list/" % slug)])]
    htmlp = page("Tier list %s (%s %d) — meilleures créatures | Zoneblox" % (g["name"], FR_MONTHS[datetime.date.today().month], datetime.date.today().year),
        "Tier list %s : les meilleures créatures classées et les meilleurs choix par rôle, méta de lancement croisée entre plusieurs sources." % g["name"],
        SITE + "/games/%s/tier-list/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/tier-list/index.html" % slug, htmlp)
    return SITE + "/games/%s/tier-list/" % slug

# ---------- rendu : vidéos ----------
def build_videos(g, data):
    slug = g["slug"]
    cards = ""
    for v in data.get("videos", []):
        thumb = "https://i.ytimg.com/vi/%s/hqdefault.jpg" % v["youtubeId"] if v.get("youtubeId") else ""
        img = ('<div class="thumb"><img src="%s" alt="%s" loading="lazy"><span class="badge">▶ %s</span></div>' % (thumb, e_att(v["title"]), e_att(v.get("category", "Vidéo")))) if thumb else ""
        cards += ('<a class="gcard" href="%s" rel="nofollow noopener" target="_blank">%s<div class="body"><h3 style="font-size:1rem">%s</h3>'
            '<span class="plat">%s · YouTube</span><div class="cta"><span class="btn btn-primary btn-sm">Voir sur YouTube →</span></div></div></a>') % (
            e_att(v["url"]), img, e_att(v["title"]), e_att(v.get("language", "fr").upper()))
    vhero = ghero(g, "Vidéos %s (français)" % e_att(g["name"]), "",
        '<p class="prose" style="margin-top:8px">Une sélection de vidéos francophones utiles pour %s. %s</p>'
        % (e_att(g["name"]), e_att(data.get("note", ""))))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Vidéos", None)]) +
        vhero + '<div class="grid-cards" style="margin-top:22px">%s</div>') % cards
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Vidéos", "/games/%s/videos/" % slug)])]
    htmlp = page("Vidéos %s en français — guides & astuces | Zoneblox" % g["name"],
        "Les meilleures vidéos francophones pour %s : guides débutant, astuces et progression." % g["name"],
        SITE + "/games/%s/videos/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/videos/index.html" % slug, htmlp)
    return SITE + "/games/%s/videos/" % slug

# ---------- rendu : carte & lieux ----------
AMAP_JS = """
<script>
(function(){
  var svg=document.getElementById('amSvg'); if(!svg) return;
  var canvas=document.getElementById('amCanvas');
  var VBW=1000, VBH=680;
  var st={k:1,x:0,y:0};
  function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
  function apply(){
    st.k=clamp(st.k,1,6);
    st.x=clamp(st.x,(1-st.k)*VBW,0);
    st.y=clamp(st.y,(1-st.k)*VBH,0);
    canvas.setAttribute('transform','translate('+st.x+' '+st.y+') scale('+st.k+')');
  }
  function toVB(e){var r=svg.getBoundingClientRect();return {x:(e.clientX-r.left)/r.width*VBW,y:(e.clientY-r.top)/r.height*VBH};}
  svg.addEventListener('wheel',function(e){e.preventDefault();var p=toVB(e);var f=e.deltaY<0?1.18:1/1.18;var nk=clamp(st.k*f,1,6);var r=nk/st.k;st.x=p.x-r*(p.x-st.x);st.y=p.y-r*(p.y-st.y);st.k=nk;apply();},{passive:false});
  var drag=null,moved=false;
  svg.addEventListener('pointerdown',function(e){drag={x:e.clientX,y:e.clientY,ox:st.x,oy:st.y};moved=false;try{svg.setPointerCapture(e.pointerId);}catch(_){}svg.classList.add('am-grab');});
  svg.addEventListener('pointermove',function(e){if(!drag)return;if(Math.abs(e.clientX-drag.x)+Math.abs(e.clientY-drag.y)>4)moved=true;var r=svg.getBoundingClientRect();st.x=drag.ox+(e.clientX-drag.x)/r.width*VBW;st.y=drag.oy+(e.clientY-drag.y)/r.height*VBH;apply();});
  function endDrag(){drag=null;svg.classList.remove('am-grab');}
  svg.addEventListener('pointerup',endDrag);svg.addEventListener('pointercancel',endDrag);
  function byId(id){return document.getElementById(id);}
  function on(id,fn){var b=byId(id);if(b)b.addEventListener('click',fn);}
  on('amIn',function(){st.k=clamp(st.k*1.3,1,6);apply();});
  on('amOut',function(){st.k=clamp(st.k/1.3,1,6);apply();});
  on('amReset',function(){st={k:1,x:0,y:0};apply();sel(null);});
  on('amFull',function(){var w=svg.closest('.am-panel');var rq=w.requestFullscreen||w.webkitRequestFullscreen;if(!document.fullscreenElement&&rq){rq.call(w);}else if(document.exitFullscreen){document.exitFullscreen();}});
  var det=byId('amDetail');
  var ICO={};$$('.am-chip').forEach(function(c){ICO[c.dataset.type]=c.querySelector('.am-ico').textContent+' '+c.textContent.trim();});
  function regionCard(el){
    var poi=(el.dataset.poi||'').split(',').filter(Boolean);
    var chips=poi.map(function(t){return '<span class="am-dchip">'+(ICO[t]||t)+'</span>';}).join('');
    return '<div class="am-dhead"><h3>'+el.dataset.name+'</h3>'+
      (el.dataset.level?'<span class="pill">📍 '+el.dataset.level+'</span>':'')+
      (el.dataset.terrain?'<span class="pill">'+el.dataset.terrain+'</span>':'')+'</div>'+
      '<p>'+el.dataset.spawn+'</p>'+
      (chips?'<div class="am-dpoi"><span class="am-dpoi-t">Repères présents</span>'+chips+'</div>':'')+
      '<p class="am-dnote">Positions schématiques — pour l\\'emplacement exact, voir les cartes datamine plus bas.</p>';
  }
  function sel(el){
    $$('.am-region').forEach(function(r){r.classList.toggle('sel',r===el);});
    if(!el){det.innerHTML='<div class="am-detail-empty"><strong>Clique sur une région</strong><span>ou choisis-la ci-dessus pour voir ses créatures et repères.</span></div>';return;}
    det.innerHTML=regionCard(el);
  }
  $$('.am-region').forEach(function(r){r.addEventListener('click',function(){if(moved)return;sel(r);});});
  function center(id){
    var el=svg.querySelector('.am-region[data-id="'+id+'"]');if(!el)return;
    var b=el.getBBox();var cx=b.x+b.width/2,cy=b.y+b.height/2;
    st.k=2.2;st.x=VBW/2-st.k*cx;st.y=VBH/2-st.k*cy;apply();sel(el);
  }
  $$('.am-jump').forEach(function(j){j.addEventListener('click',function(){center(j.dataset.id);});});
  $$('.am-chip').forEach(function(c){c.addEventListener('click',function(){
    c.classList.toggle('off');var off=c.classList.contains('off');
    $$('.am-poi[data-type="'+c.dataset.type+'"]').forEach(function(p){p.style.display=off?'none':'';});
  });});
  var sb=byId('amSearch');
  if(sb){sb.addEventListener('input',function(){var q=sb.value.toLowerCase().trim();$$('.am-jump').forEach(function(j){j.style.display=j.textContent.toLowerCase().indexOf(q)>=0?'':'none';});});
  sb.addEventListener('keydown',function(e){if(e.key==='Enter'){var v=$$('.am-jump').find(function(j){return j.style.display!=='none';});if(v)center(v.dataset.id);}});}
  apply();
})();
</script>
"""

def _build_amap(mp):
    """Construit la section 'carte interactive' à partir de data['map']. Retourne '' si absent."""
    if not mp:
        return ""
    color_by = {l["type"]: l for l in mp.get("legend", [])}
    reg_svg = ""
    for r in mp.get("regions", []):
        lb = r.get("label", {"x": 0, "y": 0})
        reg_svg += (
            f'<path class="am-region" data-id="{e_att(r["id"])}" data-name="{e_att(r["name"])}" '
            f'data-level="{e_att(r.get("levelBand",""))}" data-terrain="{e_att(r.get("terrain",""))}" '
            f'data-spawn="{e_att(r.get("spawn",""))}" data-poi="{e_att(",".join(r.get("poi",[])))}" '
            f'd="{e_att(r["path"])}" fill="{e_att(r["color"])}"></path>'
            f'<text class="am-rlabel" x="{lb["x"]}" y="{lb["y"]}">{e_att(r["name"])}</text>'
            f'<text class="am-rsub" x="{lb["x"]}" y="{lb["y"]+20}">{e_att(r.get("levelBand",""))}</text>')
    un_svg = ""
    for u in mp.get("unmapped", []):
        lb = u.get("label", {"x": 0, "y": 0})
        un_svg += (f'<path class="am-unmapped" d="{e_att(u["path"])}"></path>'
                   f'<text class="am-ulabel" x="{lb["x"]}" y="{lb["y"]}">{e_att(u["text"])}</text>')
    mk_svg = ""
    for m in mp.get("markers", []):
        li = color_by.get(m["type"], {"icon": "•", "color": "#ffffff"})
        mk_svg += (f'<g class="am-poi" data-type="{e_att(m["type"])}" transform="translate({m["x"]},{m["y"]})">'
                   f'<title>{e_att(m.get("label",""))}</title>'
                   f'<circle class="am-poi-dot" r="14" fill="{e_att(li["color"])}"></circle>'
                   f'<text class="am-poi-ico" y="1">{e_att(li["icon"])}</text></g>')
    legend_chips = "".join(
        f'<button class="am-chip" data-type="{e_att(l["type"])}" style="--c:{e_att(l["color"])}">'
        f'<span class="am-ico">{e_att(l["icon"])}</span>{e_att(l["label"])}</button>'
        for l in mp.get("legend", []))
    jump_chips = "".join(
        f'<button class="am-jump" data-id="{e_att(r["id"])}">{e_att(r["name"])}</button>'
        for r in mp.get("regions", []))
    svg = (
        f'<svg id="amSvg" viewBox="{e_att(mp.get("viewBox","0 0 1000 680"))}" preserveAspectRatio="xMidYMid meet" '
        'role="img" aria-label="Carte schématique du continent d&#39;Idyll">'
        '<defs><radialGradient id="amSea" cx="50%" cy="38%" r="85%">'
        '<stop offset="0" stop-color="#12305e"></stop><stop offset="1" stop-color="#0a1730"></stop></radialGradient></defs>'
        '<g id="amCanvas">'
        '<rect x="-300" y="-300" width="1600" height="1280" fill="url(#amSea)"></rect>'
        f'<path class="am-land" d="{e_att(mp.get("land",""))}"></path>'
        f'{un_svg}{reg_svg}{mk_svg}'
        '</g></svg>')
    return (
        '<section class="panel am-panel"><div class="panel-head"><h2>🗺️ Carte interactive d\'Idyll</h2>'
        '<span class="pill">Schématique</span></div>'
        f'<p class="sub">{e_att(mp.get("note",""))}</p>'
        '<div class="am-tools">'
        '<label class="am-search"><span>🔎</span><input id="amSearch" type="search" placeholder="Chercher une région…" aria-label="Chercher une région"></label>'
        f'<div class="am-jumps">{jump_chips}</div></div>'
        '<div class="am-wrap"><div class="am-stage">'
        f'{svg}'
        '<div class="am-ctrl">'
        '<button class="am-btn" id="amIn" aria-label="Zoom avant" title="Zoom avant">+</button>'
        '<button class="am-btn" id="amOut" aria-label="Zoom arrière" title="Zoom arrière">−</button>'
        '<button class="am-btn" id="amReset" aria-label="Réinitialiser la vue" title="Réinitialiser">⟳</button>'
        '<button class="am-btn" id="amFull" aria-label="Plein écran" title="Plein écran">⛶</button></div>'
        '<div class="am-hint-badge">Glisse pour te déplacer · molette pour zoomer · clique une région</div>'
        '</div>'
        '<aside class="am-detail" id="amDetail"><div class="am-detail-empty">'
        '<strong>Clique sur une région</strong><span>ou choisis-la ci-dessus pour voir ses créatures et repères.</span>'
        '</div></aside></div>'
        f'<div class="am-legend"><span class="am-legend-t">Calques :</span>{legend_chips}</div>'
        '</section>')

ZONE_JS = """
<script>
(function(){
  if(!document.querySelector('.zgrid')) return;
  $$('.zchip').forEach(function(c){c.addEventListener('click',function(){
    c.classList.toggle('off');var off=c.classList.contains('off');
    $$('.zpin[data-type="'+c.dataset.type+'"]').forEach(function(p){p.style.display=off?'none':'';});
  });});
  $$('.zpin').forEach(function(p){p.addEventListener('click',function(e){
    e.preventDefault();e.stopPropagation();
    var open=p.classList.contains('open');
    $$('.zpin.open').forEach(function(x){x.classList.remove('open');});
    if(!open)p.classList.add('open');
  });});
  document.addEventListener('click',function(){$$('.zpin.open').forEach(function(x){x.classList.remove('open');});});
  var lb=document.getElementById('zlb');
  if(lb){var lbi=lb.querySelector('img');
    $$('.zshot-img').forEach(function(im){im.addEventListener('click',function(){lbi.src=im.src;lbi.alt=im.alt;lb.hidden=false;});});
    function close(){lb.hidden=true;lbi.src='';}
    lb.addEventListener('click',close);
    var cb=lb.querySelector('.zlb-close');if(cb)cb.addEventListener('click',function(e){e.stopPropagation();close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  }
})();
</script>
"""

def _build_zones(data):
    """Galerie de captures de zones annotées (image + pins), depuis data['zones']. '' si absent."""
    zones = data.get("zones", [])
    if not zones:
        return ""
    legend = data.get("legend", [])
    color_by = {l["type"]: l for l in legend}
    legend_chips = "".join(
        f'<button class="zchip" data-type="{e_att(l["type"])}" style="--c:{e_att(l["color"])}">'
        f'<span class="zico">{e_att(l["icon"])}</span>{e_att(l["label"])}</button>'
        for l in legend)
    zcards = ""
    for z in zones:
        pins = ""
        for p in z.get("pins", []):
            li = color_by.get(p["type"], {"icon": "•", "color": "#ffffff"})
            pins += (f'<button class="zpin" data-type="{e_att(p["type"])}" '
                     f'style="left:{p["x"]}%;top:{p["y"]}%;--c:{e_att(li["color"])}" '
                     f'aria-label="{e_att(p["label"])}" title="{e_att(p["label"])}">'
                     f'<span class="zpin-dot">{e_att(li["icon"])}</span>'
                     f'<span class="zpin-label">{e_att(p["label"])}</span></button>')
        meta = ""
        if z.get("levelBand"):
            meta += f'<span class="pill">📍 {e_att(z["levelBand"])}</span>'
        if z.get("terrain"):
            meta += f'<span class="pill">{e_att(z["terrain"])}</span>'
        img = e_att(z.get("image", ""))
        drop = e_att(z.get("image", "").replace("/images/", "images/"))
        img_tag = (f'<img class="zshot-img" src="{img}" alt="Zone {e_att(z["name"])} — Aniimo" loading="lazy" '
                   f'onerror="this.closest(&#39;.zshot&#39;).classList.add(&#39;noimg&#39;)">') if img else ""
        cap = f'<figcaption>{e_att(z["intro"])}</figcaption>' if z.get("intro") else ""
        zcards += (
            f'<figure class="zshot" data-id="{e_att(z["id"])}">'
            f'<div class="zshot-head"><h3>{e_att(z["name"])}</h3>{meta}</div>'
            f'<div class="zshot-frame">{img_tag}'
            f'<div class="zshot-ph"><span class="zshot-ph-ico">🖼️</span><strong>Capture à ajouter</strong>'
            f'<span class="zshot-ph-sub">Dépose <code>{drop}</code></span></div>'
            f'<div class="zpins">{pins}</div></div>{cap}</figure>')
    return (
        '<section class="panel"><div class="panel-head"><h2>🗺️ Zones d\'Idyll (captures annotées)</h2>'
        '<span class="pill">Repères</span></div>'
        f'<p class="sub">{e_att(data.get("zonesNote",""))}</p>'
        f'<div class="zlegend"><span class="zlegend-t">Calques :</span>{legend_chips}</div>'
        f'<div class="zgrid">{zcards}</div>'
        '<div class="zlightbox" id="zlb" hidden><button class="zlb-close" aria-label="Fermer">✕</button><img alt=""></div>'
        '</section>')

def build_locations(g, data):
    slug = g["slug"]
    # Cartes : on ne fabrique pas de carte maison ; on renvoie vers les cartes
    # interactives des concurrents (section « Cartes datamine communautaires » plus bas).
    map_section = ""
    poi = "".join('<span class="pill" style="background:var(--surface-2)">%s</span>' % e_att(x) for x in data.get("poiTypes", []))
    regions = "".join('<div style="background:var(--bg-2);border:1px solid var(--border);border-radius:14px;padding:16px;margin-bottom:12px">'
        '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:baseline"><h3 style="font-size:1.05rem">%s</h3>'
        '%s%s</div><p style="color:var(--muted);font-size:.9rem;margin-top:6px">%s</p></div>' % (
        e_att(r["name"]),
        ('<span class="pill">📍 %s</span>' % e_att(r["levelBand"])) if r.get("levelBand") else "",
        ('<span class="pill">%s</span>' % e_att(r["terrain"])) if r.get("terrain") else "",
        e_att(r.get("notes", ""))) for r in data.get("regions", []))
    maps = "".join('<a class="gcard" href="%s" rel="nofollow noopener" target="_blank"><div class="body"><h3 style="font-size:1rem">%s</h3>'
        '<span class="plat">Carte interactive · externe</span><div class="cta"><span class="btn btn-primary btn-sm">Ouvrir la carte →</span></div></div></a>'
        % (e_att(m["url"]), e_att(m["name"])) for m in data.get("interactiveMaps", []))
    loc_hero = ghero(g, "Carte & lieux d'%s : régions d'Idyll" % e_att(g["name"]),
        '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
        '<span class="pill">✍️ L\'équipe Zoneblox</span>' % fr_date(data.get("updated", "")))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Carte & lieux", None)]) +
        '<div class="layout"><div>'
        + loc_hero +
        '<p class="prose" style="margin-top:18px">%s</p>'
        '%s'
        '<section class="panel"><div class="panel-head"><h2>🌦️ Comment trouver une créature (spawns par conditions)</h2></div>'
        '<p class="prose">%s</p></section>'
        '<section class="panel"><div class="panel-head"><h2>📌 Ce que la carte recense</h2></div>'
        '<div style="display:flex;flex-wrap:wrap;gap:6px">%s</div></section>'
        '<section class="panel"><div class="panel-head"><h2>🗺️ Régions connues</h2></div>%s'
        '<p class="sub" style="margin-top:6px">%s</p></section>'
        '<section class="panel"><div class="panel-head"><h2>🧭 Cartes datamine communautaires (spawns exacts)</h2></div>'
        '<p class="sub">Pour l\'emplacement exact des créatures, coffres et boss, ces cartes interactives communautaires sont les plus complètes. '
        'Zoneblox ne les copie pas : on te renvoie directement vers ces outils.</p>'
        '<div class="grid-cards">%s</div></section>'
        '%s'
        '</div><aside class="side">%s</aside></div>') % (
        e_att(data.get("overview", "")), map_section, e_att(data.get("spawnMechanic", "")),
        poi, regions, e_att(data.get("regionsNote", "")), maps, sources_html(data.get("sources", [])), related_box(g, "locations"))
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Carte & lieux", "/games/%s/locations/" % slug)])]
    htmlp = page("Carte & lieux Aniimo — régions d'Idyll & spawns | Zoneblox",
        "La carte d'Aniimo : carte interactive des régions d'Idyll, tranches de niveaux et mécanique de spawn (météo, jour/nuit), plus les meilleures cartes interactives pour trouver les créatures.",
        SITE + "/games/%s/locations/" % slug, body, active="games", extra_ld=ld, extra_js=ZONE_JS)
    write("games/%s/locations/index.html" % slug, htmlp)
    return SITE + "/games/%s/locations/" % slug

# ---------- IO ----------
_written = []
def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    assert content.rstrip().endswith("</html>") or rel.endswith((".xml", ".json")), "sortie tronquée: " + rel
    assert content.count("\x00") == 0, "null byte: " + rel
    _written.append(rel)

CREA_ROLE_COL = {"DPS": "#ff5f80", "Heal": "#35e0a1", "Support": "#4d9bff", "Break": "#ffbd4a", "Regen": "#9ff0c0"}
ANIIMO_ELEM_BANNER = {"Feu": "feu", "Eau": "eau", "Herbe": "herbe", "Glace": "glace", "Foudre": "foudre"}
def _crea_banner(c):
    """Bannière d'ambiance ORIGINALE (par élément) ou l'image fournie (captures licenciées)."""
    if c.get("image"):
        return c["image"]
    first = (c.get("element") or "").split("/")[0].strip()
    return "/images/aniimo/banner-%s.svg" % ANIIMO_ELEM_BANNER.get(first, "idyll")
def _crea_chips(c):
    out = ""
    if c.get("element"):
        out += '<span class="pill">%s</span>' % e_att(c["element"])
    else:
        out += '<span class="pill" style="opacity:.75">Élément à confirmer</span>'
    if c.get("role"):
        out += '<span class="pill" style="background:%s;color:#0a0b16;border:0">%s</span>' % (e_att(CREA_ROLE_COL.get(c["role"], "#7c5cff")), e_att(c["role"]))
    if c.get("stage"):
        out += '<span class="pill">%s</span>' % e_att(c["stage"])
    if c.get("tier"):
        out += '<span class="pill">Tier %s</span>' % e_att(c["tier"])
    return out

def build_creatures(g, data):
    slug = g["slug"]; urls = []
    cres = data.get("creatures", [])
    for c in cres:
        cs = c["slug"]
        conf = ('<span class="pill">Confiance : %s</span>' % e_att(c["confidence"])) if c.get("confidence") else ""
        stats = ""
        if c.get("stats"):
            rows = "".join('<div class="cstat"><span>%s</span><strong>%s</strong></div>' % (e_att(k), e_att(v)) for k, v in c["stats"].items())
            stats = '<section class="panel"><div class="panel-head"><h2>📊 Stats de base</h2></div><div class="cstats">%s</div></section>' % rows
        blocks = ""
        for label, key in [("🎯 Obtention", "obtention"), ("🧬 Évolution", "evolution"), ("⭐ Utilité", "utilite")]:
            if c.get(key):
                blocks += '<section class="panel"><div class="panel-head"><h2>%s</h2></div><p class="prose">%s</p></section>' % (label, e_att(c[key]))
        if c.get("elementNote"):
            blocks += '<section class="panel"><p class="sub">ⓘ %s</p></section>' % e_att(c["elementNote"])
        gc = dict(g); gc["coverImage"] = _crea_banner(c); gc["coverPosition"] = "center"
        hero = ghero(gc, "%s — Aniimo" % e_att(c["name"]),
            _crea_chips(c) + conf + ('<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>' % fr_date(data.get("updated", ""))))
        body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Créatures", "/games/%s/creatures/" % slug), (c["name"], None)])
            + '<div class="layout"><div>' + hero + stats + blocks + sources_html(c.get("sources", []))
            + '</div><aside class="side">%s</aside></div>' % related_box(g, "creatures"))
        ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Créatures", "/games/%s/creatures/" % slug), (c["name"], "/games/%s/creatures/%s/" % (slug, cs))])]
        htmlp = page("%s Aniimo — élément, rôle, obtention & évolution | Zoneblox" % c["name"],
            ("%s dans Aniimo : élément, rôle, comment l'obtenir, évolution et utilité. Fiche vérifiée et sourcée." % c["name"])[:158],
            SITE + "/games/%s/creatures/%s/" % (slug, cs), body, active="games", extra_ld=ld)
        write("games/%s/creatures/%s/index.html" % (slug, cs), htmlp)
        urls.append(SITE + "/games/%s/creatures/%s/" % (slug, cs))
    cards = "".join('<a class="gcard" href="/games/%s/creatures/%s/"><div class="body"><h3 style="font-size:1.05rem">%s</h3>'
        '<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:6px">%s</div>'
        '<div class="cta"><span class="btn btn-primary btn-sm">Voir la fiche →</span></div></div></a>'
        % (slug, c["slug"], e_att(c["name"]), _crea_chips(c)) for c in cres)
    gi = dict(g); gi["coverImage"] = "/images/aniimo/banner-idyll.svg"; gi["coverPosition"] = "center"
    hero = ghero(gi, "Créatures d'Aniimo : base de données",
        '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span><span class="pill">%d fiches</span>' % (fr_date(data.get("updated", "")), len(cres)))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Créatures", None)])
        + hero + '<p class="prose" style="margin-top:18px">%s</p>' % e_att(data.get("intro", ""))
        + '<section class="panel"><div class="grid-cards">%s</div>%s</section>' % (cards, ('<p class="sub" style="margin-top:12px">%s</p>' % e_att(data["note"])) if data.get("note") else ""))
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Créatures", "/games/%s/creatures/" % slug)]),
          json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "Créatures Aniimo",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["name"]} for i, c in enumerate(cres)]}, ensure_ascii=False)]
    htmlp = page("Créatures Aniimo — base de données (élément, rôle, évolution) | Zoneblox",
        "La base de créatures Aniimo : élément, rôle, obtention et évolution des meilleurs Aniimo, vérifiés et sourcés.",
        SITE + "/games/%s/creatures/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/creatures/index.html" % slug, htmlp)
    urls.append(SITE + "/games/%s/creatures/" % slug)
    return urls

def _sources_inline(sources):
    if not sources:
        return ""
    return '<p class="upd-src">Sources : ' + " · ".join(
        '<a href="%s" rel="nofollow noopener" target="_blank">%s</a>' % (e_att(s), e_att(s.split("//")[-1].split("/")[0])) for s in sources) + '</p>'

def build_updates(g, data):
    slug = g["slug"]
    KIND = {"event": "🎉 Évènement", "update": "🆕 Mise à jour", "patch": "🔧 Patch", "admin-abuse": "🛠️ Admin"}
    items = ""
    for en in data.get("entries", []):
        items += ('<article class="upd"><div class="upd-head"><span class="pill">%s</span>'
            '<span class="pill">📅 %s</span>%s</div><h3>%s</h3><p class="prose">%s</p>%s</article>') % (
            e_att(KIND.get(en.get("kind"), "Actu")), fr_date(en.get("date", "")),
            ('<span class="pill">Confiance : %s</span>' % e_att(en["confidence"])) if en.get("confidence") else "",
            e_att(en["title"]), e_att(en["summary"]), _sources_inline(en.get("sources", [])))
    hero = ghero(g, "Actualités &amp; mises à jour — %s" % e_att(g["name"]),
        '<span class="pill">🔄 Mis à jour le <strong style="color:var(--text);margin-left:4px">%s</strong></span>' % fr_date(data.get("updated", "")))
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Actualités", None)])
        + '<div class="layout"><div>' + hero + '<p class="prose" style="margin-top:18px">%s</p>' % e_att(data.get("intro", ""))
        + '<div class="upd-list">%s</div>' % items
        + '</div><aside class="side">%s</aside></div>' % related_box(g, "updates"))
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Actualités", "/games/%s/updates/" % slug)])]
    htmlp = page("Actualités %s — mises à jour & trailers | Zoneblox" % g["name"],
        ("Le suivi des actualités, mises à jour et trailers de %s, vérifiés et sourcés — jamais d'annonce inventée." % g["name"])[:158],
        SITE + "/games/%s/updates/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/updates/index.html" % slug, htmlp)
    return SITE + "/games/%s/updates/" % slug

RENDERERS = {"codes": build_codes, "guides": build_guides, "tier-list": build_tierlist, "videos": build_videos, "locations": build_locations, "creatures": build_creatures, "updates": build_updates}

def main():
    games = [load_json(p) for p in sorted(glob.glob(os.path.join(ROOT, "data/games/*.json")))]
    urls = []
    urls.append(build_directory(games))
    for g in games:
        urls.append(build_hub(g))
        for ct in g["contentTypes"]:
            if ct["status"] != "available":
                continue
            renderer = RENDERERS.get(ct["type"])
            data_path = os.path.join(ROOT, "data", g["slug"], ct["type"] + ".json")
            if renderer and os.path.exists(data_path):
                res = renderer(g, load_json(data_path))
                urls += res if isinstance(res, list) else [res]
    # sitemap dédié /games/
    today = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        pr = "0.9" if u.rstrip("/").endswith("codes") or u.rstrip("/").endswith("/games") else "0.8"
        sm.append('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (u, today, pr))
    sm.append("</urlset>\n")
    write("sitemap-games.xml", "\n".join(sm))
    print("Pages générées : %d" % len(_written))
    for w in _written:
        print("  •", w)
    print("URLs sitemap-games.xml : %d" % len(urls))

if __name__ == "__main__":
    main()
