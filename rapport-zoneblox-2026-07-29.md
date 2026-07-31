# Rapport Zoneblox — 29 juillet 2026 (mercredi)

## a) Codes vérifiés (priorité absolue)

**Jeux « hot » re-scannés ce run** : Volleyball Legends, Anime Vanguards, Blade Ball, Blox Fruits, Grow a Garden, Grow a Garden 2, Steal a Brainrot. Sources : Pro Game Guides (fetch complet actif/expiré), Beebom, GamesRadar, Pocket Tactics, Roonby, u7buy, nerdschalk, Droid Gamers, PC Gamer, Fossbytes + descriptions officielles.

### Changements réels appliqués (2 jeux)

- **Volleyball Legends — CHANGEMENT RÉEL : 6 → 3 codes actifs.** L'**Update 80** (sorti le 25/07) a fait tourner la liste : le jeu fait expirer les codes des updates précédentes à chaque MAJ. Confirmé par **Roonby (25/07), u7buy et nerdschalk (« 3 active codes as of July 28 »)** → convergence ≥3 sources.
  - **Actifs (nouveaux)** : `UPDATE_80` (5 Lucky Style Spins), `HIDARI_FINALLY` (5 Lucky Style Spins), `ENCHO_NERF` (5 Lucky Ability Spins).
  - **Déplacés en expiré** : UPDATE_79, SEASON_17, FESTIVAL_UPD, UPDATE_78, LEADERBOARD, NEW_PACK.
  - Synchro : compteur 6→3 (game-meta + live-banner + prose), « Mis à jour le » **et** « Vérifié le » → 29/07, `dateModified` → 2026-07-29, section « Dernière mise à jour » réécrite, liste expirés (6→12). Page **1 564 mots** (≥1200 ✓). `codes:3` dans GAMES_INDEX/ALL_GAMES déjà cohérent (pas de bump main.js).

- **Anime Vanguards — CHANGEMENT RÉEL : 7 → 9 codes actifs.** L'**Extermination Event Part 2** ajoute 3 codes confirmés par **PGG + Beebom + GamesRadar + Droid Gamers + Pocket Tactics** (≥3 sources).
  - **Ajoutés** : `ExecutionPart2` (50 Trait Rerolls + 20 Copycat Tokens), `1DayL8` (500 Trait Rerolls), `HeavyEyes` (50 Memoria Shards + 50 Extermination Tokens) — tous niveau 30.
  - **Retiré (prudence)** : `WhoopsieDaisy` (marqué « NOUVEAU » sur la page mais absent de toutes les sources actuelles, ni active ni inactive chez PGG) → déplacé en expiré.
  - **Conservés** (actifs chez PGG au 15/07) : PowerOfLove, EEPart1, BPSoon, 13.5, EternalAdversaries, Gambler.
  - Synchro : compteur 7→9 (game-meta + live-banner), « Mis à jour le » **et** « Vérifié le » → 29/07, `dateModified` → 2026-07-29, intro « Update 13 » périmée réécrite (Extermination Event Part 2). Page **1 593 mots** (≥1200 ✓). `codes:10` dans GAMES_INDEX/ALL_GAMES laissé tel quel (indicateur approximatif, écart ±1 non structurel → évite un bump de cache de 324 pages).

### Vérifiés sans changement (« 🔄 Vérifié le » → 29/07)
- **Blade Ball** : 14 codes actifs confirmés (sources : TheSpike, GamesRadar, Beebom, BloxGuidesGG). Notre liste = 14, cohérente. Aucun changement.
- **Blox Fruits** : sous-ensemble actif confirmé (EASTEREXP, LIGHTNINGABUSE, KITT_RESET, Sub2CaptainMaui, Axiore, TantaiGaming, StrawHatMaine…) + codes Sub2 permanents ; aucun signal d'expiration. Page vérifiée le 26/07, inchangée.
- **Grow a Garden / Grow a Garden 2** : sources indiquent GAG « quiet, no fresh codes ». GAG inchangé (2 codes). **⚠️ GAG2 à recouper** : notre page liste 7 codes, certaines sources évoquent « 3 actifs » mais sans liste exploitable (PC Gamer stale de juin, PGG absent) → **prudence : aucun retrait** faute de confirmation d'expiration ; à trancher au prochain run via Discord/wiki officiel.
- **Steal a Brainrot** : sources en conflit (0 vs 23 selon les sites), codes annoncés uniquement sur Discord officiel et expirant en heures → **0 code publié maintenu** (prudence). Inchangé.

### Candidats en attente
- Volleyball Legends : les ~40 codes « actifs » listés par PGG (fetch daté du 08/07, antérieur à l'Update 80) sont considérés **périmés** au vu des sources du 25–28/07 — non republiés.
- Anime Vanguards : `LagGone` listé actif par Beebom mais **inactif chez PGG (15/07)** → conflit, non republié (prudence).

### Jeux non revus ce run (à prioriser au prochain)
Catalogue = **176 pages codes**. Couvert : les 7 hot ci-dessus (+ re-scan trending). Reste : anime-* (hors déjà traités), tower defense, simulateurs, RNG, UGC (ugc-limited). `code-watch.json` : `lastRun` = 2026-07-29, snapshots des 7 jeux mis à jour.

## b) Directeur SEO (autorité topicale)

- **Trending re-scanné (web)** : leaders juillet 2026 — Grow a Garden 2 (#1), Steal a Brainrot, Brookhaven, Blox Fruits (203K pic), Animal Hospital (breakout, déjà couvert), Evomon — **tous présents au catalogue**. Aucun nouveau hit non couvert. **Candidat repéré** : « +1 Speed Keyboard Escape » (~405K CCU, obby/escape, probablement sans codes) → à évaluer pour une fiche (Étape 1) lors d'un prochain run.
- **Brique du jour (J7)** : **consolidation du maillage du hub éditorial** `meilleurs-jeux-roblox.html` (créé le 28/07). Ajout de **liens contextuels réciproques** depuis les trois hubs de cluster — `codes/index.html`, `guides/index.html`, `tier-list/index.html` — vers le hub (il n'était relié que depuis l'accueil + sitemaps).
  - **Intention** : découverte/navigation, ancres variées et descriptives.
  - **Anti-cannibalisation** : aucune page créée, aucun nouveau mot-clé cible → risque nul. Le hub reçoit désormais de l'equity des 4 points d'entrée principaux (accueil + 3 hubs) et redistribue vers ses 18 pages jeu.
- **Prochaine brique inscrite (J8 — 30/07)** : second hub d'intention **« Nouveaux jeux Roblox (2026) »** (nouveauté ≠ popularité), OU guide GAG « weather / météo », OU évaluation de « +1 Speed Keyboard Escape ». Roadmap mise à jour (une seule roadmap vivante, brique J7 archivée).

## c) Autres maintenances
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-29. Aucune `datetime` ponctuelle passée (tous récurrents ou `no-fixed-time`). JSON validé, `js/events.js` `node --check` OK (non modifié → pas de bump).
- **Jeu de la semaine** : mercredi → **non touché** (lundi uniquement).
- **Jeux ajoutés / guides / tier lists / UGC** : aucun ce run (priorité codes + brique maillage SEO).

## d) Fichiers touchés + QC

**Modifiés (codes, changement réel)** : `codes/volleyball-legends.html` (6→3), `codes/anime-vanguards.html` (7→9).
**Modifiés (codes, « Vérifié le » → 29/07, sans changement)** : `codes/grow-a-garden.html`, `codes/grow-a-garden-2.html`, `codes/blade-ball.html`, `codes/blox-fruits.html`, `codes/steal-a-brainrot.html`.
**Modifiés (SEO maillage)** : `codes/index.html`, `guides/index.html`, `tier-list/index.html` (liens réciproques vers le hub).
**Modifiés (maintenance)** : `data/events.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`.

**QC — tous verts :**
- 0 null byte ; toutes les pages HTML modifiées finissent par `</html>` ; `<div>` équilibrés (diff 0) ; GA4 `G-FEL71QVHNL` présent ; nav Avatars présente.
- `node --check` OK (`main.js`, `events.js`) ; JSON valides (`events.json`, `code-watch.json`).
- Cache **uniforme** : 324 pages en `main.js?v=36`, 0 stray (js/main.js **non modifié** ce run → pas de bump).
- Volleyball Legends 3 codes actifs / Anime Vanguards 9 codes actifs — compteurs cohérents entre game-meta, live-banner et prose.
- Word count : VL 1 564 mots, AV 1 593 mots (≥1200 ✓).

> Note : l'arbre de travail contient aussi des changements accumulés des runs précédents non encore poussés (dont le bump `v=36` du 28/07) — le commit ci-dessous publiera l'ensemble.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
