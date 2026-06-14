/**
 * build-items.mjs — Génère avatar/data/items.json à partir de l'API catalogue Roblox.
 *
 * Outil 100 % informatif : on ne fait que LIRE le catalogue public Roblox et mettre
 * en cache (nom, prix, slot, vignette) dans un fichier JSON statique. Aucun achat,
 * aucun équipement, aucune authentification.
 *
 * Usage :   node build-items.mjs
 * Requiert : Node 18+ (fetch global). Aucune dépendance npm.
 *
 * À lancer depuis le dossier /avatar/. Écrit dans ./data/items.json.
 * À relancer périodiquement (ex. 1×/semaine) pour rafraîchir prix & vignettes.
 */

import { writeFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = join(__dirname, 'data', 'items.json');

// ─── Styles → mots-clés de recherche catalogue ────────────────────────────────
const STYLES = {
  anime:     ['anime hair', 'anime', 'anime mask', 'anime shirt', 'anime pants', 'anime wings'],
  ninja:     ['ninja hair', 'ninja', 'ninja mask', 'ninja shirt', 'ninja pants', 'ninja headband'],
  cyberpunk: ['cyberpunk hair', 'cyberpunk', 'cyber mask', 'cyberpunk jacket', 'cyberpunk pants', 'cyber wings'],
  demon:     ['demon hair', 'demon horns', 'demon', 'demon shirt', 'demon pants', 'demon wings'],
};

// ─── assetType Roblox → slot d'avatar ─────────────────────────────────────────
const SLOT_BY_ASSETTYPE = {
  8: 'hat', 41: 'hair', 42: 'face', 43: 'neck', 44: 'shoulder', 45: 'front',
  46: 'back', 47: 'waist', 2: 'top', 11: 'top', 12: 'bottom',
  64: 'top', 65: 'top', 67: 'top', 68: 'top', 66: 'bottom', 69: 'bottom',
};

// Une coiffe/masque dont le nom contient « mask/masque » est rangée en "face".
const MASK_RE = /\b(mask|masque|balaclava|face\s*cover)\b/i;

const COLORS = {
  noir: /\b(black|noir|dark|onyx|obsidian)\b/i,
  blanc: /\b(white|blanc|ivory)\b/i,
  rouge: /\b(red|rouge|crimson|scarlet|blood)\b/i,
  bleu: /\b(blue|bleu|cyan|azure|navy)\b/i,
  vert: /\b(green|vert|emerald|lime)\b/i,
  rose: /\b(pink|rose|magenta)\b/i,
  violet: /\b(purple|violet|lilac|amethyst)\b/i,
  jaune: /\b(yellow|jaune|gold|golden|blonde|blond)\b/i,
  orange: /\b(orange)\b/i,
  marron: /\b(brown|marron|tan|chestnut)\b/i,
  argent: /\b(silver|grey|gray|gris|chrome)\b/i,
};

const FEMALE_RE = /\b(girl|female|woman|twintails|pigtails|bun|buns|ponytail|princess|dress|skirt)\b/i;
const MALE_RE   = /\b(boy|male|man|men|beard)\b/i;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function fetchJSON(url, tries = 5) {
  for (let i = 0; i < tries; i++) {
    try {
      const res = await fetch(url, { headers: { 'User-Agent': 'ZonebloxAvatar/1.0 (+https://zoneblox.com)' } });
      if (res.status === 429) { await sleep(4000 * (i + 1)); continue; }
      if (!res.ok) { await sleep(1500 * (i + 1)); continue; }
      return await res.json();
    } catch {
      await sleep(1500 * (i + 1));
    }
  }
  return null;
}

async function searchCatalog(keyword, limit = 28) {
  const url = `https://catalog.roblox.com/v1/search/items/details?Keyword=${encodeURIComponent(keyword)}&Limit=${limit}&SortType=1`;
  const j = await fetchJSON(url);
  return (j && Array.isArray(j.data)) ? j.data : [];
}

async function getThumbs(ids) {
  const out = {};
  for (let i = 0; i < ids.length; i += 50) {
    const batch = ids.slice(i, i + 50);
    const url = `https://thumbnails.roblox.com/v1/assets?assetIds=${batch.join(',')}&size=150x150&format=Png&isCircular=false`;
    const j = await fetchJSON(url);
    for (const t of (j?.data || [])) if (t.imageUrl) out[t.targetId] = t.imageUrl;
    await sleep(500);
  }
  return out;
}

function tagColors(name) {
  const out = [];
  for (const [c, re] of Object.entries(COLORS)) if (re.test(name)) out.push(c);
  return out;
}
function tagGender(name) {
  if (FEMALE_RE.test(name)) return 'fille';
  if (MALE_RE.test(name)) return 'garcon';
  return 'unisexe';
}

async function main() {
  const byId = new Map();

  for (const [style, keywords] of Object.entries(STYLES)) {
    for (const kw of keywords) {
      const rows = await searchCatalog(kw);
      for (const r of rows) {
        if (r.itemType !== 'Asset') continue;
        let slot = SLOT_BY_ASSETTYPE[r.assetType];
        if (!slot) continue;
        if (slot === 'hat' && MASK_RE.test(r.name)) slot = 'face';
        const price = (typeof r.price === 'number') ? r.price : (r.lowestPrice ?? null);
        if (price == null) continue; // ignore les objets sans prix affiché (limited/hors-vente)

        const existing = byId.get(r.id);
        if (existing) {
          if (!existing.styles.includes(style)) existing.styles.push(style);
          continue;
        }
        byId.set(r.id, {
          id: r.id,
          name: r.name.trim(),
          price,
          slot,
          assetType: r.assetType,
          styles: [style],
          colors: tagColors(r.name),
          gender: tagGender(r.name),
          creator: r.creatorName || '',
          favorites: r.favoriteCount || 0,
          limited: Array.isArray(r.itemRestrictions) && r.itemRestrictions.length > 0,
        });
      }
      await sleep(1200); // pacing anti rate-limit
      process.stdout.write(`· ${style}/${kw}: ${byId.size} items cumulés\n`);
    }
  }

  // Vignettes (rbxcdn) pour chaque item
  const ids = [...byId.keys()];
  process.stdout.write(`→ Vignettes pour ${ids.length} items…\n`);
  const thumbs = await getThumbs(ids);
  for (const it of byId.values()) it.thumbUrl = thumbs[it.id] || null;

  const items = [...byId.values()].sort((a, b) => b.favorites - a.favorites);
  const payload = {
    generatedAt: new Date().toISOString(),
    source: 'Roblox catalog API (catalog.roblox.com)',
    note: 'Données et vignettes : Roblox. Outil informatif Zoneblox — aucun achat ni équipement.',
    styles: Object.keys(STYLES),
    count: items.length,
    items,
  };

  await mkdir(dirname(OUT), { recursive: true });
  await writeFile(OUT, JSON.stringify(payload, null, 2), 'utf8');
  process.stdout.write(`✅ ${items.length} items écrits → ${OUT}\n`);
}

main().catch((e) => { console.error(e); process.exit(1); });
