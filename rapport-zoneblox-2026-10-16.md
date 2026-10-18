# Rapport ZoneBlox — 2026-10-16 (run 05h, vendredi)

**Mode :** 05h FULL MAINTENANCE + EDITORIAL. Fenêtre de recherche : 12-24 h (nuit). Vendredi → **pas** de « Jeu de la semaine » (§30).
**Verdict global :** nuit calme. **Aucune édition de code** (tout stable confirmé ou conflit non tranché → kill switch). 13 `verifDate` rafraîchies. Mémoire éditoriale + builds + QC OK. **EXACTITUDE > FRAÎCHEUR** respecté.

---

## CODES

### hotGames vérifiés (stables — codes inchangés, verifDate → 16/10)

| Jeu | État | Sources fraîches |
|-----|------|------------------|
| volleyball-legends | ✅ UPDATE_91 / REPLAYS / MVP | samlover 13/10 + roonby 10/10 (UPDATE_90/SKELETON_BUNDLE/JINX/SLOT_REWORK expirés 10/10) |
| steal-a-brainrot | ✅ BESTBRAINROTEVER (seul) | Dexerto 12/10 « no new codes » |
| grow-a-garden | ✅ RDCAward / BEANORLEAVE10 | Dexerto (maj 08/04, source faible) — aucune preuve d'expiration → conservés |
| anime-last-stand | ✅ MagicKnights! / ElfReincarnation! / IsItReallyWeekly?! | pockettactics 03/10 + nerdschalk (les 4 autres = expirés) — page correcte |

### Candidats en attente / kill switch maintenu

- **blue-lock-rivals** — CONFLIT non tranché. Dexerto 11/10 = nouveau set (EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT) actif + ancien set expiré, **mais mono-source** ; PocketTactics 04/10 montre encore l'ancien set actif ; softwaretestinghelp (23/07) + insider-gaming (codes hiver) = junk. **Page inchangée (ancien set).**
- **anime-vanguards** — membership ambiguë : pcgamer 09/10 = 2ndAnniDay1→Day7 ; page = Day2→Day6 + Assault/SummerLeaving/AnniNextHopefully ; roonby 13/10 « NEW » non confirmé. Pas de concordance 2-sources → inchangé.
- **fisch** — source roonby 10/10 messy (« no codes available » contradictoire). Inchangé.

### Rotation — 6 jeux hot jamais deep-vérifiés (catalogVerify → 16/10)

| Jeu | Résultat |
|-----|----------|
| run-a-restaurant | ✅ FISHIES / RAR4EVER confirmés exacts (Dexerto 10/10) |
| animal-hospital | ✅ 0 code (progameguides + destructoid) — page honnête conservée |
| noob-incremental | ⚠️ **STALE** → flag MUST_UPDATE (set actif double-confirmé, rewrite reporté faute de récompenses fiables) |
| vv-ultimatum | CONFLIT (roonby 13/10 vs nerdschalk 19/09, intersection déjà sur la page) — inchangé |
| fifa-super-soccer | WorldCupSecret probablement expiré (nerdschalk 07/09 + absent Dexerto) ; remplacement non tranché — inchangé |
| spin-a-soccer-card | sources périmées contradictoires (dexerto 25/08 vs tryhardguides 27/02) — « aucun code » conservé |

**Codes ajoutés : 0 · Codes expirés retirés : 0 · Candidats en attente : blue-lock-rivals, noob-incremental, fifa-super-soccer, anime-vanguards, vv-ultimatum.**

---

## SEO

- Aucune nouvelle page créée (règle UPDATE BEFORE CREATE + kill switch éditorial). Aucune intention de recherche nouvelle non couverte détectée cette nuit.
- 13 pages rajeunies via `verifDate` (fraîcheur SEO sans mentir sur l'ancienneté des codes).
- Opportunité SEO identifiée : réécriture propre de **noob-incremental** (page périmée vs demande réelle) — reportée (données récompenses).

## NOUVEAUX JEUX

Aucun. Aucun nouveau jeu Roblox avec preuve d'intérêt multi-source cette nuit (« steal an egg » cité viral mais déjà hot chez nous, 0 code confirmé).

## CONTENU

Guides : 0 · Tier lists : 0 · Articles : 0 · Mises à jour : 13 `verifDate` + mémoire éditoriale. (Qualité > quantité : rien à publier.)

## ANIIMO

Codes octobre disponibles (mein-mmo). Data-driven → `data/aniimo/` + `build_site.py`, ≥2 sources requises. **Différé** (pas de modification directe sous `/games/`).

## GTA 6

Trailer 3 **toujours non sorti** au 16/10 : uniquement rumeurs d'insiders ; le « jalon du 15/10 » = spéculation presse ; **0 confirmation Rockstar Newswire**. Sortie **nov. 2026 RAPPORTÉE**, non reconfirmée. CONFIRMÉ / RAPPORTÉ / RUMEUR maintenus séparés. UPDATE evergreen uniquement, aucune page créée.

## FC 27

Titre EA live = **FC 26** (promo « Festival of Football — Answer the Call » en cours). Reconfirme la question de naming FC 27 vs FC 26 → **décision Peter**. Rien renommé (décision à risque).

---

## EDITORIAL INTELLIGENCE

- **Top opportunités :** noob-incremental (rewrite bien sourcé, reporté) · blue-lock-rivals (trancher le drop).
- **Tendances :** rien de neuf confirmé (nuit calme).
- **Articles créés :** 0 · **Pages mises à jour :** 13 verifDate.
- **Sujets ignorés :** nouveaux jeux « viraux » sans preuve multi-source (kill switch).
- **À surveiller :** GTA 6 Trailer 3 (Newswire), FC 26 promos, Aniimo codes oct, blue-lock drop.
- `editorial-intelligence.json` : meta + 4 topics rafraîchis (GTA6, FC, Aniimo, blue-lock) + 1 topic ajouté (noob-incremental-stale, UPDATE_REQUIRED). 43 topics.

## EDITORIAL QUEUE

- **Urgents :** blue-lock-rivals (2ᵉ source du drop), GTA 6 Trailer 3.
- **À publier :** rien.
- **À mettre à jour :** noob-incremental (MUST_UPDATE), fifa-super-soccer, iron-soul-dungeon, anime-expeditions/defenders, dig-and-clean, 8 pages vides, Aniimo oct.
- **À préparer / Peter :** naming FC26, jeu de la semaine (§30), listes gonflées.
- **Demain :** codes hot + exécuter rewrite noob-incremental + rotation suite (bloxstrike, catch-and-tame, fish-an-anime-rng).

---

## QC

- `code-watch.json`, `editorial-intelligence.json`, `data/codes.json`, `data/games-index.json` : **JSON valides** ✅
- 13 pages codes éditées : `</html>` présent, **0 null byte** ✅
- `node --check js/main.js` : OK ✅
- `sitemap.xml` + `sitemap-games.xml` : XML bien formés ✅
- Builds (ordre §29) : `build_site.py` (40 URLs games) · `build_home.py` (5 sections) · `build_codes_json.py` (185 jeux / **1279 codes**) · `build_sitemap.py` (**385 URLs**, lastmod verifDate=185) ✅
- `/avatar/` non touché ✅ · aucun fichier corrompu.
- Édition codes pages = **verifDate uniquement** (changements `const ACTIVE` visibles dans le diff = run 68-pages de la veille non encore commité, cohérents avec la vérif du jour).

---

Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
