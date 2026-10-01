# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-01 (run 05h — full maintenance jeudi ; run planifié 03h00 UTC exécuté avec retard)**

## ✅ FAIT CE MATIN (run 05h 2026-10-01)

- **🗓️ DÉBUT DE MOIS — `sync_month.py`** : les **184 pages codes** sont passées aux libellés **« octobre 2026 »** (title, og:title, meta description, élision « d'octobre »). Gros signal de fraîcheur SEO mensuel.
- **🔧 FIX `universal-tower-defense-x`** : 18 chips périmés (thème Bleach/DBS) → **7 codes frais** (Football11!, UniversalFootball!, NewBlitzPass! confirmés par **mmoculture 01/10 + theclick 28/09 + PGG** ; +WeLoveYoruichi2!, UTDZApologyForBugs!, WeLoveUTDZ!, SrryForWhoopsie! via **mmoculture 01/10 + PGG**). Compteur 18→7.
- **➕ AJOUT `combat-warriors`** : page à 0 code → **CHAOS_AND_RAGE + OK_LATE_AGAIN** (confirmés **robloxden 01/10 + PGG 26/09** ; C6NNON expiré selon PGG, C4PID/LongSchnoze109 = source unique non ajoutés). Compteur 0→2.
- **Hot games revérifiés — aucun changement de chips** (verifDate → 1 oct) : blue-lock-rivals (4, Beebom 30/09 + PGG 26/09), volleyball-legends (3, Update 89, Fossbytes 01/10 + Beebom 26/09), grow-a-garden (2, Beebom 01/10 + PocketGamer 05/09), anime-vanguards (22, Pocket Tactics 27/09 = match exact), blade-ball (15, Beebom 01/09 confirme 14/15), fruit-battlegrounds (4, base PT 22/09).
- **Rotation reconfirmée sans changement** (verifDate → 1 oct) : brainrot-evolution (24, tous actifs chez Beebom 19/09), anime-dimensions-simulator (8/10 confirmés PGG 26/09), bedwars (0 — pas de système de codes), project-slayers (0, Beebom 01/10 + PT 29/09), weapon-rng (4, robloxden 14/09).
- **GTA 6** : entrée **Game Informer** (dossier 14 pages, ~12 screenshots, météo avancée, Leonida/Miami) ajoutée à `data/gta-6/updates.json` (HIGH, pushsquare + techwiser). **UPDATE evergreen, pas de nouvelle URL.**
- **Aniimo** : `lastChecked` → 01/10, 11 codes gardés (voir divergence ci-dessous).
- **Régénération** OK : build_site → build_home → build_codes_json (**184 jeux, 1260 codes**) → build_sitemap (**383 URLs**). **QC clean** : JSON/XML valides, main.js OK, 0 déséquilibre div, 0 null byte, GA4 présent, cache `main.js?v=47`, sitemap finit `</urlset>`.

---

## 🔥 URGENT

- **GTA 6** — reveal Game Informer **traité** (entrée evergreen ajoutée). Rester attentif à toute **annonce officielle Rockstar** (trailer 3, date, précommande) d'ici le **19 nov 2026** → UPDATE evergreen, jamais de nouvelle URL. Séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.

---

## 🟢 À PUBLIER

_(rien)_ — kill switch éditorial maintenu. Grow a Garden / Steal a Brainrot dominent (couverts). Pas de titre neuf réunissant traction réelle + codes réels + absence de page. « 2 excellents > 20 faibles ».

---

## 🛠️ À METTRE À JOUR

- **anime-champions-simulator** : 11 chips **NON revérifiés** (seule source trouvée = Pocket Tactics daté mars 2025, inexploitable). verifDate **non rafraîchie**. **Priorité du prochain run** : trouver une source datée du mois courant.
- **anime-eternal** : sous-listé (13 chips, Update 55) alors que le jeu est à **Update 60P4** (PGG 01/09). Nos 13 restent actifs. **Ajouter Update 56→60 avec une 2e source fraîche.**
- **Grosses listes** reportées (sous-listage stable, pas de faux-actif prouvé) : anime-astral-simulator (100), dragon-blox (82), anime-battle-rng (35), clover-retribution.

---

## 🟡 À PRÉPARER / SURVEILLER (tendances)

- **GTA 6** · suivi officiel Rockstar (voir URGENT).
- **FC 27** · monitor : post-lancement, promos Saison 1 connues, rien de concret (SBC/promo) justifiant une page.
- **Aniimo** · divergence sources (voir ci-dessous) ; patch game8 daté 22 sept à surveiller.
- **blue-lock-rivals** · rotation quasi quotidienne (codes SNUFFY) → revérifier chaque run.
- **volleyball-legends** · rotation ~hebdo (Update NN) → revérifier souvent.
- **universal-tower-defense-x** · TD à rotation rapide (codes football/UTDZ) → revérifier souvent.

---

## 👀 À REVÉRIFIER (codes — conflits / à trancher)

- **steal-a-brainrot** : CONFLIT. GamesRadar (03/09) donne BESTBRAINROTEVER **actif** ; Pocket Tactics (22/09) dit **aucun code actif**. Chip **gardé** (pas de preuve explicite d'expiration), à retrancher avec une source fraîche.
- **spongebob-tower-defense** : DIVERGENCE. Fossbytes (01/10) confirme nos 2 (GetGudKid, CHALLENGEWON) + NEWBEGINNINGS2/RAINBOWMOUNTS ; PGG (05/09) liste 3 **autres** (SeasonReworkbby, ROADTO200K, IMMANICPRISMATIC). Aucun accord 2-sources → rien ajouté, 2 gardés.
- **aniimo** : DIVERGENCE. PGG (01/10) + Destructoid (28/09) ne listent que **2** codes (ANIIMOGIFT, Aniimo2026) ; nos **11** (confirmés GamesRadar+PT le 29/09). Gardés (codes de lancement evergreen, pas de preuve d'expiration).
- **anime-dimensions-simulator** : ULTRA + HALLOWEEN gardés (PGG 26/09 ne les liste pas mais pas de preuve d'expiration ; HALLOWEEN possiblement réactivé pour octobre).
- **blade-ball** : SERPENT gardé (Beebom 01/09 ne l'a pas, source ancienne, pas de preuve) ; GOODVSEVIL (Beebom seul) non ajouté.
- **Reports antérieurs en attente** : grow-a-garden FREESEED/STORY/STARBUD (torigate désormais **confirmé expiré** par Beebom 01/10), a-one-piece-game/Re:AOPG, locked, grimoires-era, spin-a-brainrot, world-cup-album, fifa-super-soccer, arene-de-sniper (mapping placeId), doors 777.

---

## 📅 PRIORITÉS DEMAIN (run 05h — 2026-10-02, vendredi)

1. **Codes** (priorité absolue) : hotGames — blue-lock-rivals (SNUFFY), volleyball-legends (Update NN), grow-a-garden, steal-a-brainrot (trancher conflit), anime-vanguards, blade-ball, fruit-battlegrounds, universal-tower-defense-x (rotation rapide).
2. **anime-champions-simulator** : trouver une source datée du mois courant (non revérifié aujourd'hui).
3. **anime-eternal** : ajouter Update 56→60 avec 2e source.
4. **Rotation** : poursuivre les plus anciens restants — anime-astral-simulator, clover-retribution, anime-battle-rng, dragon-blox (grosses listes, vérif sous-listage), anime-champions/origins, fire-force-online, jujutsu-infinite, evade.
5. **GTA 6** : veille annonce officielle Rockstar.
6. **Régénération** : build_site → build_home → build_codes_json (si codes changés) → build_sitemap.

---

_Note : le bloc « jeu de la semaine » (spec §30) n'existe pas (homepage refondue, sections auto via build_home.py) → étape lundi = N/A. Pour publier : git add/commit/push manuel (voir rapport)._
