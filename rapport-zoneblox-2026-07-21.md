# Rapport Zoneblox — mardi 21 juillet 2026

Run quotidien automatique (05h00). Dernier run enregistré : 20 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **173 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **173/173** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **21 juillet 2026** (motif unique et idempotent, exactement 1 par page, aucun doublon, intégrité vérifiée : 0 null byte, `</html>` présent, `<div>` équilibrés).
- **Vérification approfondie multi-sources** de plusieurs jeux « hot » restés en attente depuis le 19–20/07 : Blue Lock Rivals, Volleyball Legends, Anime Vanguards, Steal a Brainrot, Grow a Garden / Grow a Garden 2, Anime Rangers X.

### Sources utilisées

Pocket Tactics, Beebom, Pro Game Guides, PC Gamer, GamesRadar, Roonby, allthings.how, Fandom (wiki Volleyball Legends), Roblox Den. Croisement systématique (≥3 sources fiables OU source officielle ; en cas de conflit → version la plus prudente + candidat « en attente »).

> Note technique : `web_fetch` renvoie des versions de pages **mises en cache en juin** (Beebom, PGG, PC Gamer) ; les listes actives ont donc été confirmées via les **extraits d'index de recherche datés du 19–20/07** recoupés sur ≥3 sources concordantes, jamais sur une seule source ni sur une valeur inventée.

### Changements réellement appliqués (3 jeux)

**`codes/blue-lock-rivals.html` — +3 codes actifs (3 → 6)**

L'update « Quarter-Finals » a ajouté trois codes confirmés actifs par Pocket Tactics, GamesRadar, Pro Game Guides (édition « SHIDOU + » juillet) et allthings.how :

| Code | Récompense |
|---|---|
| QOLUPD | 5 Lucky Spins + 5 Lucky Flow Spins |
| QUARTERFINALSOON | 5 Lucky Spins |
| REBALANCES | 5 Lucky Flow Spins |

Les 3 codes déjà présents (NELSHIDOU, NEWCHEMSOON, DEMON) restent actifs. GAGAREWORK / ADDRESSME / BEARCLAW restent expirés. Compteurs (game-meta + bandeau live), intro, section « À propos », « Mis à jour le » (13 → 21 juillet) et `dateModified` (2026-06-30 → 2026-07-21) mis à jour.

**`codes/volleyball-legends.html` — +3 codes actifs (3 → 6)**

L'Update 79 a introduit trois nouveaux codes, confirmés par Roonby (UPDATE 79), Beebom, Pro Game Guides, allthings.how et le wiki Fandom :

| Code | Récompense |
|---|---|
| UPDATE_79 | 5 Lucky Style Spins |
| SEASON_17 | 5 Lucky Style Spins |
| FESTIVAL_UPD | 5 Lucky Ability Spins |

UPDATE_78, LEADERBOARD et NEW_PACK restent actifs. Intro réécrite, compteurs, « Mis à jour le » (18 → 21 juillet) et `dateModified` (→ 2026-07-21) mis à jour.

**`codes/anime-vanguards.html` — LateBP expiré (8 → 7 actifs)**

Le code **LateBP** (500 Trait Rerolls) a **expiré le 19 juillet 2026** — confirmé par GamesRadar, Pro Game Guides, PC Gamer et allthings.how. Basculé de la liste active vers la liste des codes expirés. Les 7 autres codes (WhoopsieDaisy, PowerOfLove, EEPart1, BPSoon, 13.5, EternalAdversaries, Gambler) restent actifs, aucun n'étant contredit par une source récente. Compteurs, « Mis à jour le » (18 → 21 juillet) et `dateModified` (→ 2026-07-21) mis à jour.

### Jeux vérifiés sans changement (listes déjà exactes)

- **Steal a Brainrot** — aucun code actif publiquement disponible (Beebom, Pocket Tactics, allthings.how, Roblox Den concordent : le canal codes a été retiré depuis l'UPD 11). La page, sans code, est **correcte**. Date interne « Vérifié le » au 21/07.
- **Grow a Garden 2** — TEAMGREENBEAN confirmé actif (PC Gamer, Beebom, GamesRadar). Aucun retrait requis.

### Candidats « en attente » (non publiés) — `snapshots` de `code-watch.json`

- **anime-vanguards** : patch du 20/07 (refonte de l'« unit builder ») aurait déposé des codes ; **non confirmés** précisément → à vérifier au prochain run.
- **blade-ball** : conflits SERPENT / BATTLEROYALE / GOODVSEVIL / DUNGEONSRELEASE toujours à trancher via source officielle (X/Discord non lisibles en fetch).
- **grow-a-garden (original)** : les sources web confondent fréquemment avec Grow a Garden 2 → vérifier via une source dédiée au prochain run.

### À prioriser au prochain run

Jeux hotGames non revus en profondeur ce run : pet-simulator-99, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital, anime-last-stand, anime-rangers-x, grow-a-garden (original), blade-ball (conflits).

---

## 2. Jeu de la semaine

`date +%u` = 2 (mardi) → **pas de modification** de la bannière « Jeu de la semaine » (mise à jour réservée au lundi). Aucune touche à `index.html`.

---

## 3. Étapes non traitées ce run — et pourquoi

Budget consacré à l'étape 2 (priorité absolue : vérification des codes).

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le 21/07 » (pas de revérification approfondie).

---

## 4. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie. Blue Lock Rivals, Volleyball Legends et Anime Vanguards conservent leur volume rédactionnel (> 1 200 mots) ; seuls listes de codes, compteurs, intros et dates ont bougé.

---

## 5. Contrôle qualité

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ pages modifiées OK |
| Null bytes | ✅ 0 partout (173 pages codes + 3 pages modifiées + `code-watch.json`) |
| Balises `<div>` équilibrées | ✅ delta 0 sur les 3 pages modifiées et l'échantillon rafraîchi |
| GA4 `G-FEL71QVHNL` | ✅ présent |
| Cache JS `main.js?v=35` | ✅ uniforme (320 occurrences, aucune page hors v=35) |
| `🔄 Vérifié le 21 juillet 2026` | ✅ exactement 1 par page codes (173/173) |
| `blue-lock-rivals` | ✅ 6 actifs, compteurs/intro/dates cohérents |
| `volleyball-legends` | ✅ 6 actifs, compteurs/intro/dates cohérents |
| `anime-vanguards` | ✅ 7 actifs, LateBP en expiré, compteurs cohérents |
| `js/main.js` | ✅ `node --check` OK — **non modifié** → pas de bump de cache requis |
| `tools/code-watch.json` | ✅ JSON valide, `lastRun` = 2026-07-21 |

Aucune troncature détectée ce run.

### ⚠️ Anomalie Git pré-existante à signaler (non causée par ce run)

L'index Git contient un état incohérent **antérieur à ce run** : un renommage tronqué `tier-list/steal-a-brainrot.html -> tier-list/stea` et des suppressions indexées (`git rm --cached`) de 9 pages `tier-list/*.html`, de `tools/` (dont `code-watch.json`) et de `ugc-gratuit/index.html`. **Les fichiers réels sont tous présents sur le disque, en version identique à HEAD (0 ligne de différence vérifiée).**

Conséquence : `git add -A` **réconcilie automatiquement** cet état (il ré-ajoute les fichiers de travail identiques et supprime l'entrée fantôme `tier-list/stea`). La commande de publication ci-dessous est donc **sans danger** : aucune page `tier-list` ne sera perdue, elles seront au contraire re-suivies à l'identique. Recommandation : vérifier d'un coup d'œil `git status` avant le push.

---

## 6. Fichiers touchés par ce run

- **173 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 21 juillet 2026 ».
- **`codes/blue-lock-rivals.html`** — +3 codes actifs (QOLUPD, QUARTERFINALSOON, REBALANCES) ; 6 actifs ; compteurs / intro / « Mis à jour le » / `dateModified`.
- **`codes/volleyball-legends.html`** — +3 codes actifs (UPDATE_79, SEASON_17, FESTIVAL_UPD) ; 6 actifs ; intro / compteurs / dates.
- **`codes/anime-vanguards.html`** — LateBP actif → expiré ; 7 actifs ; compteurs / dates.
- **`tools/code-watch.json`** — snapshots blue-lock-rivals / volleyball-legends / anime-vanguards / steal-a-brainrot / grow-a-garden(-2) / anime-rangers-x, `lastRun` = 2026-07-21, candidats en attente 2026-07-21.
- **`rapport-zoneblox-2026-07-21.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
