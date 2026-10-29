#!/usr/bin/env python3
"""
build_pins.py — Génère des visuels d'épingles Pinterest (1000x1500, 2:3) de marque
ZoneBlox, 1 par jeu, à partir de data/codes.json + data/games-index.json.

- Format natif "liste de codes" (ou bullets "découverte" si pas de codes).
- Couleur d'accent reprise par jeu depuis games-index.json.
- Ne (re)génère QUE les jeux nouveaux (absents du manifeste) ou dont les codes
  ont changé (hash) — donc "une image par jeu ajouté" dans la tâche quotidienne.
- Écrit/actualise un manifeste pinterest/pins.json et une file pinterest/PIN-QUEUE.md
  avec le texte prêt (titre / description / lien / tableau) pour la publication assistée.
- NE PUBLIE RIEN : la publication Pinterest reste une étape humaine/assistée (navigateur).

Nécessite playwright + Pillow (conteneur cloud). Exemples :
  python3 tools/build_pins.py                 # nouveaux + codes modifiés (cap --max)
  python3 tools/build_pins.py --slug 1-anime-eyes --force
  python3 tools/build_pins.py --all           # backfill complet (long)
"""
import argparse, json, hashlib, re, sys, datetime, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

BRAND_CYAN = "#00e5ff"
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF←-⇿⌀-⏿️⃣]"
)

def strip_emoji(s: str) -> str:
    return re.sub(r"\s{2,}", " ", EMOJI_RE.sub("", s or "")).strip(" •·-").strip()

def hsh(obj) -> str:
    return hashlib.sha1(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]

# ---------- HTML template (design validé) ----------
TEMPLATE = """<!doctype html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1000px;height:1500px}}
body{{font-family:'Outfit',system-ui,Arial,sans-serif;width:1000px;height:1500px;overflow:hidden;
  position:relative;color:#eef0ff;
  background:
    radial-gradient(1200px 700px at 80% -8%, {accent}2e, transparent 60%),
    radial-gradient(900px 600px at -10% 108%, #7c5cff2e, transparent 60%),
    linear-gradient(160deg,#07071a 0%,#0c0c24 55%,#13133a 100%);}}
.wrap{{position:absolute;inset:0;padding:78px 70px 64px;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:16px;font-weight:800;font-size:34px}}
.logo{{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#7c5cff,#a259ff);
  box-shadow:0 0 30px #7c5cff80}}
.zb{{background:linear-gradient(90deg,#cdb8ff,#eef0ff);-webkit-background-clip:text;background-clip:text;color:transparent}}
.kicker{{margin-top:62px;align-self:flex-start;padding:14px 26px;border-radius:999px;font-weight:800;
  font-size:28px;letter-spacing:3px;color:{accent};background:{accent}1a;border:2px solid {accent}55;text-transform:uppercase}}
h1{{margin-top:26px;font-weight:900;font-size:{titlesize}px;line-height:.98;letter-spacing:-1px;
  background:linear-gradient(92deg,#ffffff,{accent});-webkit-background-clip:text;background-clip:text;color:transparent;
  text-shadow:0 10px 60px {accent}30;word-break:break-word}}
.sub{{margin-top:22px;font-size:33px;font-weight:600;color:#b9bde6}}
.sub .ok{{color:#35e0a1;font-weight:800}}
.body{{margin-top:48px;display:flex;flex-direction:column;gap:20px;flex:1}}
.chip{{background:linear-gradient(180deg,#191c3e,#12132f);border:2px solid #2a2c55;border-radius:22px;
  padding:24px 30px;box-shadow:0 10px 30px #00000040}}
.chip .code{{font-weight:900;font-size:48px;letter-spacing:2px;color:{accent};text-shadow:0 0 24px {accent}55}}
.chip .reward{{margin-top:8px;font-size:28px;font-weight:600;color:#c9cdf0}}
.line{{display:flex;align-items:flex-start;gap:20px;font-size:40px;font-weight:600;color:#e7e9ff;line-height:1.18}}
.line .dot{{color:{accent};font-weight:900}}
.more{{font-size:30px;font-weight:700;color:#9aa0c6;padding-left:6px}}
.footer{{margin-top:34px;display:flex;align-items:center;justify-content:space-between}}
.cta{{display:flex;align-items:center;gap:18px;font-weight:900;font-size:44px}}
.url{{color:#fff;background:linear-gradient(90deg,#7c5cff,#a259ff);padding:16px 32px;border-radius:16px;
  box-shadow:0 10px 40px #7c5cff55}}
.badge{{font-size:28px;font-weight:700;color:#8e93c4}}
</style></head><body><div class="wrap">
  <div class="brand"><span class="logo"></span><span class="zb">ZoneBlox</span></div>
  <div class="kicker">{kicker}</div>
  <h1>{title}</h1>
  <div class="sub">{sub} <span class="ok">✅</span></div>
  <div class="body">{body}</div>
  <div class="footer">
    <div class="cta"><span>👉</span><span class="url">zoneblox.com</span></div>
    <div class="badge">FR · à jour</div>
  </div>
</div></body></html>"""

def title_size(title: str) -> int:
    n = len(title)
    if n <= 10: return 120
    if n <= 16: return 104
    if n <= 22: return 86
    if n <= 30: return 70
    return 58

def build_html(name, kicker, sub, accent, mode, items):
    if mode == "chips":
        body = "\n".join(
            f'<div class="chip"><div class="code">{c}</div><div class="reward">{r}</div></div>'
            for c, r in items[:4]
        )
        if len(items) > 4:
            body += f'<div class="more">+ {len(items)-4} autre(s) code(s) sur zoneblox.com</div>'
    else:
        body = "\n".join(f'<div class="line"><span class="dot">▸</span>{t}</div>' for t in items[:4])
    return TEMPLATE.format(accent=accent, kicker=kicker, title=name, sub=sub,
                           body=body, titlesize=title_size(name))

def plan_pin(slug, cg, idx):
    """Retourne (spec_pour_render, meta_queue) pour un jeu."""
    name = cg.get("name", slug)
    accent = BRAND_CYAN
    platforms = []
    if idx:
        a = idx.get("accent") or []
        if a: accent = a[0]
        platforms = idx.get("platforms") or []
    is_roblox = any("roblox" in p.lower() for p in platforms) or True  # défaut Roblox
    rob = " (Roblox)" if is_roblox else ""
    link = f"https://zoneblox.com/codes-{slug}.html"
    codes = cg.get("codes") or []
    if codes:
        items = [(c["code"], strip_emoji(c.get("reward", ""))) for c in codes]
        code_names = ", ".join(c["code"] for c in codes[:4])
        spec = dict(name=name, kicker="CODES ROBLOX" if is_roblox else "CODES",
                    sub="Vérifiés à la main · à jour", accent=accent, mode="chips", items=items)
        title = f"Codes {name}{rob} — vérifiés à la main & à jour"
        desc = (f"Tous les codes actifs de {name}{rob}, vérifiés à la main : {code_names}. "
                f"Récompenses + guide et tier list sur ZoneBlox. "
                f"#Roblox #RobloxCodes #CodesRoblox #RobloxFR")
        board = "Codes Roblox"
    else:
        spec = dict(name=name, kicker="NOUVEAU SUR ZONEBLOX", sub="Codes · Tier list · Guide",
                    accent=accent, mode="lines",
                    items=["Tous les codes dès leur sortie", "La tier list de progression",
                           "Le guide complet pour débuter", "Mis à jour régulièrement"])
        title = f"{name}{rob} — codes, tier list & guide"
        desc = (f"Nouveau sur ZoneBlox : {name}{rob} ! Codes vérifiés à la main dès leur sortie, "
                f"tier list et guide complet. #Roblox #RobloxFR #NouveauxJeux")
        board = "Nouveaux jeux Roblox"
    meta = dict(slug=slug, title=title, description=desc, link=link, board=board)
    return spec, meta

def write_queue(queue_path, manifest):
    ready = [m for m in manifest.values() if m.get("status") == "ready"]
    ready.sort(key=lambda m: m.get("generated", ""), reverse=True)
    lines = [
        "# 📌 File d'attente des épingles Pinterest — ZoneBlox",
        "",
        f"_Généré automatiquement par `tools/build_pins.py` · {datetime.date.today().isoformat()}_",
        "",
        "> Publication **assistée/manuelle** (navigateur + session Pinterest). "
        "Visuels prêts dans `pinterest/pins/<slug>.jpg`. "
        "Après publication d'une épingle, passer son `status` à `published` dans `pinterest/pins.json`.",
        "",
        f"**{len(ready)} épingle(s) à publier.**",
        "",
    ]
    for m in ready:
        lines += [
            f"## {m['slug']}  → tableau **{m['board']}**",
            f"- **Visuel** : `pinterest/pins/{m['slug']}.jpg`",
            f"- **Titre** : {m['title']}",
            f"- **Description** : {m['description']}",
            f"- **Lien** : {m['link']}",
            "",
        ]
    pathlib.Path(queue_path).write_text("\n".join(lines), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--codes", default=None)
    ap.add_argument("--index", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--queue", default=None)
    ap.add_argument("--max", type=int, default=60, help="plafond de génération par run")
    ap.add_argument("--all", action="store_true", help="ignore le plafond (backfill complet)")
    ap.add_argument("--slug", default=None, help="ne traiter qu'un slug")
    ap.add_argument("--force", action="store_true", help="régénère même si à jour")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    codes_p = pathlib.Path(args.codes or root / "data/codes.json")
    index_p = pathlib.Path(args.index or root / "data/games-index.json")
    out_dir = pathlib.Path(args.out or root / "pinterest/pins")
    man_p = pathlib.Path(args.manifest or root / "pinterest/pins.json")
    queue_p = pathlib.Path(args.queue or root / "pinterest/PIN-QUEUE.md")
    out_dir.mkdir(parents=True, exist_ok=True)
    man_p.parent.mkdir(parents=True, exist_ok=True)

    codes_games = json.load(open(codes_p, encoding="utf-8")).get("games", {})
    idx_list = json.load(open(index_p, encoding="utf-8")).get("games", [])
    idx_by_slug = {g["slug"]: g for g in idx_list}
    manifest = json.load(open(man_p, encoding="utf-8")) if man_p.exists() else {}

    slugs = [args.slug] if args.slug else list(codes_games.keys())

    todo = []
    for slug in slugs:
        cg = codes_games.get(slug)
        if not cg:
            print("skip (absent de codes.json):", slug); continue
        h = hsh(cg.get("codes", []))
        png = out_dir / f"{slug}.jpg"
        prev = manifest.get(slug, {})
        stale = (prev.get("codes_hash") != h) or (not png.exists())
        if args.force or slug not in manifest or stale:
            todo.append((slug, cg, h))

    # priorité : plus récents d'abord (date 'updated' de games-index)
    todo.sort(key=lambda t: (idx_by_slug.get(t[0], {}).get("updated", "")), reverse=True)
    if not args.all and not args.slug:
        todo = todo[: args.max]

    if not todo:
        print("Rien à générer. Manifeste à jour."); write_queue(queue_p, manifest); return

    print(f"À générer : {len(todo)} épingle(s)…")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1000, "height": 1500}, device_scale_factor=2)
        for slug, cg, h in todo:
            spec, meta = plan_pin(slug, cg, idx_by_slug.get(slug))
            pg.set_content(build_html(**spec), wait_until="networkidle")
            pg.wait_for_timeout(500)
            tmp_png = out_dir / f".{slug}.tmp.png"
            pg.screenshot(path=str(tmp_png), clip={"x": 0, "y": 0, "width": 1000, "height": 1500})
            # downscale 2000x3000 -> 1000x1500 JPEG (taille maîtrisée)
            im = Image.open(tmp_png).convert("RGB").resize((1000, 1500), Image.LANCZOS)
            im.save(out_dir / f"{slug}.jpg", "JPEG", quality=90, optimize=True)
            tmp_png.unlink(missing_ok=True)
            prev = manifest.get(slug, {})
            manifest[slug] = dict(meta, codes_hash=h,
                                  generated=datetime.date.today().isoformat(),
                                  status="published" if prev.get("status") == "published"
                                         and prev.get("codes_hash") == h else "ready")
            print("  ✓", slug, "→", meta["board"])
        b.close()

    json.dump(manifest, open(man_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    write_queue(queue_p, manifest)
    ready = sum(1 for m in manifest.values() if m.get("status") == "ready")
    print(f"OK. Manifeste: {man_p} · File: {queue_p} · {ready} à publier.")

if __name__ == "__main__":
    main()
