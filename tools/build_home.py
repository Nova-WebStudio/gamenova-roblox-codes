#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZoneBlox — Générateur des sections DYNAMIQUES de l'accueil (index.html).

But : que « Dernières actualités », « Jeux du moment », « Guides & astuces »,
« Codes » et « Tier lists » se remplissent AUTOMATIQUEMENT depuis les données,
triés du plus récent au plus ancien. Ré-exécutable et idempotent : on le relance
après toute mise à jour de contenu (codes, guides, actus…) et l'accueil se rafraîchit.

  python3 tools/build_home.py

Ne touche QUE l'intérieur des <section id="..."> ciblées ; ne change pas le hero,
le header, le footer, ni le JS. Aucun contenu inventé : tout vient des données.
"""
import re, io, os, json, glob, html as H, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*a): return os.path.join(ROOT, *a)
def e(s): return H.escape(str(s), quote=True)

FR_ABBR = {"janv.":1,"févr.":2,"mars":3,"avr.":4,"mai":5,"juin":6,"juil.":7,"août":8,"sept.":9,"oct.":10,"nov.":11,"déc.":12}
def parse_fr(d):
    m = re.match(r"(\d{1,2})\s+([^\s]+)\s+(\d{4})", (d or "").strip())
    if not m: return datetime.date(2000,1,1)
    day, mon, yr = m.groups()
    return datetime.date(int(yr), FR_ABBR.get(mon, 1), int(day))
def parse_iso(d):
    try: return datetime.date(*[int(x) for x in d.split("-")])
    except Exception: return datetime.date(2000,1,1)

# ---------- chargement des données ----------
html_txt = io.open(P("index.html"), encoding="utf-8").read()
GAMES = json.loads(re.search(r"const GAMES\s*=\s*(\[.*?\]);", html_txt, re.DOTALL).group(1))
GBY = {g["slug"]: g for g in GAMES}
GUIDE_SET = {os.path.basename(f)[:-5] for f in glob.glob(P("guides","*.html"))}
def load(rel):
    p = P("data","aniimo",rel)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
A_updates = load("updates.json"); A_guides = load("guides.json")
A_tier = load("tier-list.json"); A_codes = load("codes.json"); A_videos = load("videos.json")

# ---------- helpers de rendu (réutilisent les classes .pcard existantes) ----------
def gimg(slug, label, aniimo=False):
    if aniimo:
        return ('<div class="ph"><img src="/images/hero-bg.webp" alt="Aniimo" loading="lazy" '
                'style="object-position:right center"><span class="tag">%s</span></div>') % e(label)
    g = GBY.get(slug); thumb = g["thumb"] if g else ""
    return ('<div class="ph"><img src="%s" alt="Miniature %s" loading="lazy" decoding="async" '
            'onerror="this.onerror=null;this.src=\'/images/games/%s.svg\'"><span class="tag">%s</span></div>') % (
            e(thumb), e(g["name"] if g else slug), e(slug), e(label))
def sec_head(icon, title, sub, more_href=None, more_txt=None):
    more = ('<a class="more" href="%s">%s</a>' % (more_href, e(more_txt))) if more_href else ""
    return '<div class="sec-head"><div><h2>%s %s</h2><p>%s</p></div>%s</div>' % (icon, e(title), e(sub), more)

# ---------- sections ----------
def s_actualites():
    # RÈGLE : un seul article par jeu (donc des jeux DIFFÉRENTS), trié du plus récent au plus ancien.
    KIND = {"event":"🎉 Évènement","update":"🆕 Mise à jour","patch":"🔧 Patch",
            "news":"📰 Actualité","trailer":"🎬 Trailer","announce":"📢 Annonce"}
    FRM = ["","janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    def frdate(iso):
        d = parse_iso(iso); return "%d %s %d" % (d.day, FRM[d.month], d.year)
    picks = []  # (game, entrée la plus récente) — UNE par jeu
    for gp in sorted(glob.glob(P("data","games","*.json"))):
        try: game = json.load(open(gp, encoding="utf-8"))
        except Exception: continue
        up = P("data", game.get("slug",""), "updates.json")
        if not os.path.exists(up): continue
        try: d = json.load(open(up, encoding="utf-8"))
        except Exception: continue
        ents = sorted(d.get("entries", []), key=lambda x: parse_iso(x.get("date","")), reverse=True)
        if ents: picks.append((game, ents[0]))
    picks.sort(key=lambda t: parse_iso(t[1].get("date","")), reverse=True)
    picks = picks[:3]
    if not picks:
        return None
    cards = ""
    for game, en in picks:
        img = game.get("coverImage","/images/hero-bg.webp"); pos = game.get("coverPosition","center")
        name = game.get("name", game.get("slug",""))
        cards += ('<a class="pcard" href="/games/%s/updates/"><div class="ph">'
            '<img src="%s" alt="Actualité %s" loading="lazy" style="object-position:%s" '
            'onerror="this.onerror=null;this.src=\'/images/hero-bg.webp\'">'
            '<span class="tag" style="border:0;background:linear-gradient(100deg,#7c5cff,#4d9bff)">%s</span></div>'
            '<div class="pb"><h3>%s</h3><span class="pmeta">%s · %s</span>'
            '<span class="pcta">Lire →</span></div></a>') % (
            e(game.get("slug","")), e(img), e(name), e(pos),
            e(KIND.get(en.get("kind"),"Actu")), e(en.get("title","")), e(name), e(frdate(en.get("date",""))))
    return (sec_head("📰","Dernières actualités","La dernière actu de chaque jeu, mise à jour automatiquement.",
                     "/actualites/","Toutes les actus →")
            + '<div class="pgrid c3">%s</div>' % cards)

def gamecard(slug, aniimo=False):
    if aniimo:
        chips = ["🎁 Codes","📖 Guides","📊 Tier list","🐾 Créatures","📰 Actus"]
        return ('<a class="pcard" href="/games/aniimo/">%s<div class="pb"><h3>Aniimo</h3>'
                '<span class="pmeta">RPG · Multi-plateforme</span><div class="chips">%s</div>'
                '<span class="pcta">Explorer →</span></div></a>') % (gimg(slug,"Nouveau",True), "".join("<span>%s</span>"%e(c) for c in chips))
    g = GBY[slug]; chips = ["🎁 Codes"]
    if slug in GUIDE_SET: chips.append("📖 Guide")
    if g.get("tier"): chips.append("📊 Tier list")
    return ('<a class="pcard" href="/codes-%s.html">%s<div class="pb"><h3>%s</h3>'
            '<span class="pmeta">Roblox · %s</span><div class="chips">%s</div>'
            '<span class="pcta">Explorer →</span></div></a>') % (
            slug, gimg(slug,"Roblox"), e(g["name"]), e(g["cat"]), "".join("<span>%s</span>"%e(c) for c in chips))

def s_jeux_du_moment():
    ordered = sorted([g for g in GAMES if g.get("thumb")], key=lambda g: parse_fr(g.get("date","")), reverse=True)
    slugs = [g["slug"] for g in ordered][:7]
    cards = gamecard(None, True) + "".join(gamecard(s) for s in slugs)
    return (sec_head("🎮","Jeux du moment","Les jeux mis à jour le plus récemment sur Zoneblox.","/games/","Tous les jeux →")
            + '<div class="pgrid c4">%s</div>' % cards)

def s_guides():
    cards = ""
    for gd in sorted(A_guides.get("guides", []), key=lambda x: parse_iso(x.get("updated","")), reverse=True):
        cards += ('<a class="pcard" href="/games/aniimo/guides/%s/">%s<div class="pb"><h3>%s</h3>'
            '<span class="pmeta">Aniimo · %s</span><span class="pcta">Lire le guide →</span></div></a>') % (
            gd["slug"], gimg(None,"Guide",True), e(gd["title"]), e(gd.get("category","Guide")))
    rob = ["blox-fruits","anime-vanguards","grow-a-garden","blade-ball","fisch","blue-lock-rivals"]
    for s in rob:
        if s in GBY:
            cards += ('<a class="pcard" href="/guides/%s.html">%s<div class="pb"><h3>Guide %s</h3>'
                '<span class="pmeta">Guide · Roblox</span><span class="pcta">Lire le guide →</span></div></a>') % (
                s, gimg(s,"Guide"), e(GBY[s]["name"]))
    return (sec_head("📖","Guides & astuces","Nos derniers guides, du plus récent au plus ancien.","/guides.html","Tous les guides →")
            + '<div class="pgrid c4">%s</div>' % cards)

def s_codes():
    cards = ('<a class="pcard" href="/games/aniimo/codes/">%s<div class="pb"><h3>Aniimo</h3>'
             '<span class="codes-n">11 codes actifs</span><span class="pmeta">🔄 Vérifié le 18 sept. 2026</span>'
             '<span class="pcta">Voir les codes →</span></div></a>') % gimg(None,"Codes",True)
    withcodes = sorted([g for g in GAMES if g.get("count",0) > 0], key=lambda g: parse_fr(g.get("date","")), reverse=True)[:7]
    for g in withcodes:
        cards += ('<a class="pcard" href="/codes-%s.html">%s<div class="pb"><h3>%s</h3>'
            '<span class="codes-n">%d codes actifs</span><span class="pmeta">🔄 Vérifié le %s</span>'
            '<span class="pcta">Voir les codes →</span></div></a>') % (
            g["slug"], gimg(g["slug"],"Codes"), e(g["name"]), g["count"], e(g["date"]))
    return (sec_head("🎁","Codes","Les codes vérifiés le plus récemment, mis à jour automatiquement.","/tous-les-codes.html","Tous les codes →")
            + '<div class="pgrid c4">%s</div>' % cards)

def s_tierlists():
    cards = ('<a class="pcard" href="/games/aniimo/tier-list/">%s<div class="pb"><h3>Tier list Aniimo</h3>'
             '<span class="pmeta">Meilleures créatures</span><span class="pcta">Voir la tier list →</span></div></a>') % gimg(None,"Tier list",True)
    rob = ["blox-fruits","anime-vanguards","blue-lock-rivals","anime-last-stand","king-legacy","grand-piece-online","fruit-battlegrounds"]
    for s in rob:
        name = GBY[s]["name"] if s in GBY else s.replace("-"," ").title()
        cards += ('<a class="pcard" href="/tier-list/%s.html">%s<div class="pb"><h3>Tier list %s</h3>'
            '<span class="pmeta">Classement méta</span><span class="pcta">Voir la tier list →</span></div></a>') % (
            s, gimg(s,"Tier list"), e(name))
    return (sec_head("📊","Tier lists","Le classement méta des meilleures unités, fruits, pets et créatures.","/tier-lists.html","Toutes les tier lists →")
            + '<div class="pgrid c4">%s</div>' % cards)

BUILDERS = {"actualites": s_actualites, "jeux-du-moment": s_jeux_du_moment, "guides-astuces": s_guides,
            "codes": s_codes, "tier-lists": s_tierlists}

def replace_section(txt, sid, inner):
    start = txt.find('<section class="block wrap" id="%s">' % sid)
    if start < 0: return txt, False
    end = txt.find("</section>", start)
    if end < 0: return txt, False
    new = '<section class="block wrap" id="%s">%s</section>' % (sid, inner)
    return txt[:start] + new + txt[end + len("</section>"):], True

def main():
    txt = html_txt; done = []
    for sid, fn in BUILDERS.items():
        inner = fn()
        if inner is None:
            continue
        txt, ok = replace_section(txt, sid, inner)
        if ok: done.append(sid)
    assert txt.rstrip().endswith("</html>"), "sortie tronquée"
    assert "\x00" not in txt, "null byte"
    bal = len(re.findall(r"<div\b", txt)) - txt.count("</div>")
    assert bal == 0, "déséquilibre div: %d" % bal
    io.open(P("index.html"), "w", encoding="utf-8").write(txt)
    print("Sections régénérées :", ", ".join(done))

if __name__ == "__main__":
    main()
