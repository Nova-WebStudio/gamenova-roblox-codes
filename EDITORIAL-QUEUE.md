# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-20 (run 05h — mardi)**

## ✅ FAIT — RUN 05h 2026-10-20

- **Codes — 3 éditions propres (multi-sources, non destructives) :**
  - **Grand Piece Online** → ajout **FREE_Drops8** (Boost drop ×2 1 j). **3 sources concordantes** : Dexerto 18/10 + ProGameGuides 01/10 + Destructoid 19/10. Set final 4 (FREE_Drops8, ILOVEGPO_3, FREE_Drops7, FREE_EXP6). **Kill switch** sur `5FREETAILORVOUCHERS_2` + `ANOTHER3FREETAILORVOUCHERS!` : Destructoid 19/10 + PGG 01/10 = **expirés** vs Dexerto 18/10 = actifs → NON ajoutés (infirme le candidat de la queue 19/10).
  - **Da Hood** → ajout **MACRO!** (1M DHC) + **ETERNAL** (500K DHC). 3 sources (TechWiser 12/10 direct + robloxden 18/10 + PGG 12/10). Set final 4. DOG/SHARK **conservés** (robloxden 18/10 = expirés, mais PocketGamer 10/10 + TechWiser 12/10 = actifs → 1 seule preuve d'expiration, insuffisant).
  - **Anime Vanguards** → **refresh 2ᵉ anniversaire** : page passée de 8 à **13 codes**. +5 **double-confirmés** (Twinfinite 19/10 + ProGameGuides 12/10, récompenses concordantes) : Finally, 2ndAnniversary, TrueShadowMonarch, HappyAnniversary, 100thTournament. `Prepare` confirmé expiré (2 sources).
- **Hot games — re-vérifiés, défendables, 0 autre édition** : blue-lock-rivals (page = set actif ; EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT **kill switch maintenu** ; conflit récompense 5 vs 7 spins → page conservée), steal-a-brainrot (BESTBRAINROTEVER, Dexerto 12/10), grow-a-garden, fisch, volleyball-legends.
- **GTA 6 — UPDATE evergreen** : **Launch Trailer (Trailer 3) publié le 15/10** ajouté à `data/gta-6/updates.json` (RockstarINTEL 15/10 + gHacks 16/10). Release **19/11/2026 réaffirmée**. Pas de vidéo ajoutée (ID YouTube officiel non vérifié → anti-invention).
- **Aniimo** : 14/15 codes concordants (mein-mmo 09/10). Seul écart : `aniimazingfroyo` (page = actif vs mein-mmo = expiré, 1 source) → conservé.
- **Rotation — 11 jeux re-vérifiés** (catalogVerify → 20/10). Découvertes : voir « À METTRE À JOUR ».
- **Régénération** : build_codes_json + build_site + build_home + build_sitemap. **QC OK** (node --check main.js, JSON, sitemap 395 URLs, pages éditées : `</html>`, divs équilibrés, CTA unique, GA4, Avatars).

---

## 🔥 URGENT

- **GTA 6** — ~1 mois avant lancement (19/11/2026). Launch Trailer déjà sorti (15/10). Surveiller à chaque run les **confirmations pré-lancement Rockstar Newswire** (préchargement 12/11, éventuels patchs day-one). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.

## 🟢 À PUBLIER

_(rien)_ — kill switch maintenu sur tous les conflits ; aucun nouveau jeu Roblox avec preuve d'intérêt multi-source **+ codes réels** cette nuit.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **Grimoires Era — page très probablement PÉRIMÉE (conflit 3 voies).** PocketGamer 03/10 (REVAMPSOON!/25SPINS!/2025BOOSTS!/CLOVER) vs games.gg (NEXTCHAPTER!/MINING!/UPDATE0.6!/SYSTEMREWORK!) vs page ZoneBlox (11 codes, **aucun commun**). → **Rebuild via source officielle** (Trello/Discord). Ne rien éditer tant que 2 sources fiables ne concordent pas.
- **Haze Piece** — roonby 13/10 confirme 18/20. Candidats ajout : **PHANTOMSHIP + OKUCHI** (5 Race Spins) → besoin 2ᵉ source. Sub2XenoTy / Sub2CaptainMaui absents chez roonby mais pas de preuve d'expiration → conservés.
- **Rivals** — page plus récente que la source dispo (Insider Gaming 04/10). **SORRY** flagué expiré (1 source) → candidat retrait, besoin 2ᵉ source + confirmer FREE182 / COMMUNITY20-23.
- **noob-incremental — MUST_UPDATE (report).** Set actif double-confirmé (Dexerto 10/10 + RobloxDen 15/10). Rewrite à exécuter une fois récompenses re-sourcées + resync `const ACTIVE`/compteur.
- **fish-an-anime-rng** — conflit 3 voies non tranché. 2 sources fraîches concordantes requises.
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses (anti-invention).
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : republier un set fiable là où il existe.

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Naming FC 27 vs FC 26** : titre EA live = **FC 26** (promos Festival of Football « Answer the Call » + Halloween Puzzle Crafting en cours, ea.com officiel). **Bloque la couverture Ultimate Team / Halloween.** À trancher.
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents du code** → étape du lundi **non exécutable**. À Peter : ajouter les marqueurs ou confirmer le mécanisme.
- **⚠️ Grosses listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35) : rebuild autour du set vérifié-actif, ou maintien ? **Rotation en retard ~40 j** (depuis 10/09).
- **Dette technique copyAll** : `const ACTIVE` peut diverger de la liste visible sur d'anciennes pages. Resynchronisé à chaque édition (OK sur les 3 pages éditées ce jour).

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : grimoires-era (conflit 3 voies), rivals (SORRY), haze-piece (PHANTOMSHIP/OKUCHI), da-hood (DOG/SHARK), grand-piece-online (5FREETAILORVOUCHERS_2/ANOTHER), aniimo (aniimazingfroyo), fish-an-anime-rng, bloxstrike, catch-and-tame, iron-soul-dungeon, anime-expeditions, anime-defenders ; blue-lock-rivals (EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT).
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées, ~40 j) ; 33 jeux **jamais entrés dans catalogVerify**.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 21/10)

1. **Grimoires Era** : source officielle (Trello/Discord) → rebuild propre (page périmée confirmée).
2. **Haze Piece** : 2ᵉ source → ajouter PHANTOMSHIP + OKUCHI.
3. **Rivals** : source fraîche → trancher SORRY + confirmer les codes récents.
4. **Hot games** : re-vérifier GPO, Da Hood (DOG/SHARK + PVP/BUFF), BLR, Anime Vanguards (expirations anniversaire), steal-a-brainrot, grow-a-garden, fisch.
5. **noob-incremental** : exécuter le rewrite une fois récompenses sourcées.
6. **GTA 6** Newswire · **FC 26** (si naming tranché) · **Aniimo** (aniimazingfroyo 2ᵉ source).
7. **Rotation suite** : jeux jamais vérifiés + inflated lists (décision Peter).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
