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
CSSV = "2"
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
    links = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' class="active"' if key == active else "", label)
        for label, href, key in NAV_ITEMS)
    mobile = "".join('<a href="%s">%s</a>' % (href, label) for label, href, key in NAV_ITEMS)
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
        '%s\n<link rel="stylesheet" href="/css/platform.css?v=%s" />\n<link rel="stylesheet" href="/css/nav-fix.css?v=2" />\n%s</head>\n'
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
    icons = {"codes": "🎁", "guides": "📖", "tier-list": "📊", "videos": "🎬", "creatures": "🐾"}
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
    return ('<section class="panel"><h2>🔎 Sources</h2><p class="sub">Informations croisées entre plusieurs sources ; vérifie toujours en jeu.</p>'
            '<div class="prose"><p>' + " · ".join('<a href="%s" rel="nofollow noopener" target="_blank" style="color:var(--primary-2)">%s</a>'
            % (e_att(s["url"]), e_att(s.get("name", s["url"]))) for s in sources) + '</p></div></section>')

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
        body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", "/games/%s/guides/" % slug), (gd["title"], None)]) +
            '<div class="layout"><div>'
            '<section class="ghero"><div class="info"><h1>%s</h1><div class="meta">'
            '<span class="pill">📖 %s</span><span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
            '<span class="pill">✍️ Par <a href="/a-propos.html#editorial" style="color:var(--text)">L\'équipe Zoneblox</a></span></div></div></section>'
            '<p class="prose" style="margin-top:18px">%s</p>'
            '%s'
            '%s'
            '%s'
            '</div><aside class="side">%s'
            '<div class="box"><h3>Sur cette page</h3><nav class="toc">%s</nav></div></aside></div>') % (
            e_att(gd["title"]), e_att(gd.get("category", "Guide")), fr_date(gd.get("updated", "")),
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
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Guides", None)]) +
        '<section class="ghero"><div class="info"><h1>Guides %s</h1><p class="prose" style="margin-top:8px">'
        'Nos guides pour débuter et progresser dans %s. De nouveaux guides arrivent au fil des découvertes.</p></div></section>'
        '<div class="grid-cards" style="margin-top:22px">%s</div>') % (e_att(g["name"]), e_att(g["name"]), cards)
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
    roles_html = "".join('<div class="step"><div class="n" style="width:auto;padding:0 10px;font-size:.8rem">%s</div>'
        '<h3 style="margin-top:8px">%s</h3><p>%s</p></div>' % (e_att(r["role"]), e_att(" · ".join(r["picks"])), e_att(r.get("why", "")))
        for r in data.get("rolePicks", []))
    entries = [x for t in data.get("tiers", []) for x in t.get("entries", [])]
    itemlist = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "Tier list %s" % g["name"],
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x} for i, x in enumerate(entries)]}, ensure_ascii=False)
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Tier list", None)]) +
        '<div class="layout"><div>'
        '<section class="ghero"><div class="info"><h1>Tier list %s : les meilleures créatures</h1><div class="meta">'
        '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
        '<span class="pill">✍️ L\'équipe Zoneblox</span></div></div></section>'
        '<p class="prose" style="margin-top:18px">%s</p>'
        '<section class="panel"><div class="panel-head"><h2>🏆 Classement</h2></div>%s</section>'
        '<section class="panel"><div class="panel-head"><h2>🎯 Meilleurs choix par rôle</h2></div>'
        '<p class="sub">Une bonne équipe mélange au moins 3 rôles (DPS, Heal, Support, Break, Regen).</p>'
        '<div class="steps">%s</div></section>'
        '%s'
        '</div><aside class="side">%s</aside></div>') % (
        e_att(g["name"]), fr_date(data.get("updated", "")), e_att(data.get("methodology", "")),
        tiers_html, roles_html, sources_html(data.get("sources", [])), related_box(g, "tier-list"))
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
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Vidéos", None)]) +
        '<section class="ghero"><div class="info"><h1>Vidéos %s (français)</h1><p class="prose" style="margin-top:8px">'
        'Une sélection de vidéos francophones utiles pour %s. %s</p></div></section>'
        '<div class="grid-cards" style="margin-top:22px">%s</div>') % (
        e_att(g["name"]), e_att(g["name"]), e_att(data.get("note", "")), cards)
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Vidéos", "/games/%s/videos/" % slug)])]
    htmlp = page("Vidéos %s en français — guides & astuces | Zoneblox" % g["name"],
        "Les meilleures vidéos francophones pour %s : guides débutant, astuces et progression." % g["name"],
        SITE + "/games/%s/videos/" % slug, body, active="games", extra_ld=ld)
    write("games/%s/videos/index.html" % slug, htmlp)
    return SITE + "/games/%s/videos/" % slug

# ---------- rendu : carte & lieux ----------
def build_locations(g, data):
    slug = g["slug"]
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
    body = (crumb_html([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Carte & lieux", None)]) +
        '<div class="layout"><div>'
        '<section class="ghero"><div class="info"><h1>Carte & lieux d\'Aniimo : régions d\'Idyll</h1><div class="meta">'
        '<span class="pill">🔄 Vérifié le <strong style="color:var(--text);margin-left:4px">%s</strong></span>'
        '<span class="pill">✍️ L\'équipe Zoneblox</span></div></div></section>'
        '<p class="prose" style="margin-top:18px">%s</p>'
        '<section class="panel"><div class="panel-head"><h2>🌦️ Comment trouver une créature (spawns par conditions)</h2></div>'
        '<p class="prose">%s</p></section>'
        '<section class="panel"><div class="panel-head"><h2>📌 Ce que la carte recense</h2></div>'
        '<div style="display:flex;flex-wrap:wrap;gap:6px">%s</div></section>'
        '<section class="panel"><div class="panel-head"><h2>🗺️ Régions connues</h2></div>%s'
        '<p class="sub" style="margin-top:6px">%s</p></section>'
        '<section class="panel"><div class="panel-head"><h2>🧭 Cartes interactives (spawns de créatures)</h2></div>'
        '<p class="sub">Pour l\'emplacement exact des créatures, coffres et boss, ces cartes interactives communautaires sont les plus complètes. '
        'Zoneblox ne les copie pas : on te renvoie directement vers ces outils.</p>'
        '<div class="grid-cards">%s</div></section>'
        '%s'
        '</div><aside class="side">%s</aside></div>') % (
        fr_date(data.get("updated", "")), e_att(data.get("overview", "")), e_att(data.get("spawnMechanic", "")),
        poi, regions, e_att(data.get("regionsNote", "")), maps, sources_html(data.get("sources", [])), related_box(g, "locations"))
    ld = [crumb_ld([("Accueil", "/"), ("Jeux", "/games/"), (g["name"], "/games/%s/" % slug), ("Carte & lieux", "/games/%s/locations/" % slug)])]
    htmlp = page("Carte & lieux Aniimo — régions d'Idyll & spawns | Zoneblox",
        "La carte d'Aniimo : régions d'Idyll, tranches de niveaux et mécanique de spawn (météo, jour/nuit), plus les meilleures cartes interactives pour trouver les créatures.",
        SITE + "/games/%s/locations/" % slug, body, active="games", extra_ld=ld)
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

RENDERERS = {"codes": build_codes, "guides": build_guides, "tier-list": build_tierlist, "videos": build_videos, "locations": build_locations}

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
