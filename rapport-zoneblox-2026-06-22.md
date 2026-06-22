# Rapport Zoneblox — lundi 22 juin 2026

## Réparation préalable (BLOQUANT résolu)

Deux pages étaient **corrompues par des octets nuls** (non committées, héritées d'un run précédent tronqué) :
- `codes/anime-squadron.html` — 1028 octets nuls, fichier tronqué (pas de `</html>`)
- `codes/noob-incremental.html` — 459 octets nuls, fichier tronqué

Les deux ont été **restaurées depuis `HEAD`** (`git show HEAD:<fichier> > <fichier>`). Vérifié après restauration : 0 octet nul, se terminent par `</html>`, tailles cohérentes (29 394 / 33 184 octets).

## Étape 0 — Surveillance des codes (code-watch)

Les **27 jeux** de `hotGames` ont été re-vérifiés via l'API officielle Roblox (`games.roblox.com/v1/games`) en récupérant les descriptions live.

- **Aucun nouveau code candidat** détecté dans les descriptions in-game. Tous les codes présents dans les descriptions (`YOO1M110K` pour Fruit Battlegrounds, `BOOM` pour Merge a Nuke, `W7C28D` pour BlockSpin, `$1M$` pour Squid Game X) figuraient déjà dans les snapshots.
- `tools/code-watch.json` mis à jour : `lastChecked` rafraîchi au **2026-06-22T02:15:00Z** pour les 27 snapshots ; `knownCodes` de Volleyball Legends synchronisé (voir Étape 2).
- **Bonus surveillance** : renseigné les `groupId` officiels (récupérés via l'API) pour 10 jeux qui étaient à `null` (spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution) → active la surveillance des shouts de groupe à partir du prochain run.
- JSON re-vérifié : valide, se termine par `}`, 27 hotGames / 27 snapshots.

## Étape 2 — Codes actualisés : Volleyball Legends

Nouveaux codes confirmés sur **2 sources** (Pro Game Guides [UPD 75] + agrégat Beebom/GamesRadar/Twinfinite). Ajout de **3 codes** en tête de tableau sur `codes/volleyball-legends.html` :
- `UPDATE_75`, `SPECTATING`, `SHOW_OFF` (5 Lucky Style Spins chacun)

La page passe de **6 à 9 codes actifs** (les 6 précédents restent valides). Dates « Mis à jour le » et « Vérifié le » passées au **22 juin 2026** ; compteurs (meta, bannière, intro) mis à jour de façon cohérente. Snapshot code-watch synchronisé.

> Autres jeux à forte vélocité (Blade Ball, Anime Vanguards, Anime Last Stand, Fisch, Grow a Garden, Steal a Brainrot, Fruit Battlegrounds…) : descriptions inchangées vs snapshots, aucun nouveau code à publier.

## Étape 7 — Jeu de la semaine (lundi)

Détermination du **#1 réel des tendances** par comptage live des joueurs en simultané (API Roblox, 22 juin ~07h UTC) sur les principaux jeux du catalogue :

| Jeu | Joueurs en simultané |
|-----|----------------------|
| **Grow a Garden 2** | **441 355** ⭐ |
| Brookhaven RP | 389 812 |
| Adopt Me | 299 000 |
| 99 Nights in the Forest | 260 714 |
| Blox Fruits | 228 656 |
| Steal a Brainrot | 188 814 |
| Rivals | 150 940 |
| Fish It | 141 861 |

→ **Grow a Garden 2** est le n°1 incontesté cette semaine (breakout 2026, sorti le 21 mai, déjà 489 M de visites). Les 3 pages dédiées existent déjà (codes + tier list + guide), idéal pour la bannière.

Bannière `<!-- FEATURED-WEEK -->` d'`index.html` remplacée : miniature réelle `tr.rbxcdn.com`, blurb FR honnête (guildes, vols nocturnes, 440 K joueurs), boutons Codes / Tier list / Guide pointant vers les pages dédiées.

⚠️ **Miniature** : la vraie miniature live de Grow a Garden 2 a changé de hash (`71ae7859…` au lieu de l'ancien `d3506c96…` encore stocké). La bannière utilise le **nouveau hash vérifié**. À synchroniser au prochain run dans `ROBLOX_THUMBS`, `THUMBS`, la carte d'accueil, le hero de `codes/grow-a-garden-2.html`, la carte tier-list (forcerait un bump de cache car `js/main.js` serait touché — reporté pour éviter une opération à risque sur 267 fichiers ce run).

## Étape 3 — Contenu / indexation

`codes/grow-a-garden-2.html` (jeu de la semaine) vérifié : **1293 mots** de rédactionnel FR visible ≥ 1200 → conforme à la règle d'indexation. Code TEAMGREENBEAN confirmé comme **seul code actif** sur 2 sources (toujours d'actualité) → date inchangée (honnêteté).

## Étapes 1, 4, 5, 6 — Ajouts / tier lists / guides / UGC

Pas d'ajout massif ce run. Le **mount bash du sandbox accuse un retard de synchronisation** sur les fichiers édités via les outils fichier, ce qui rend la vérification d'intégrité des grosses écritures peu fiable côté shell ; priorité donnée à la justesse (codes, jeu de la semaine) via les outils fichier (lecture/écriture fiables sur le disque réel).

## Étape 8 — QC

| Vérification | Résultat |
|--------------|----------|
| Octets nuls (fichiers réparés) | 0 ✓ |
| `</html>` final | index.html, volleyball-legends.html, anime-squadron, noob-incremental ✓ |
| `code-watch.json` valide / se termine par `}` | ✓ (464 lignes) |
| `node --check js/main.js` | OK ✓ |
| Nav 7 entrées (Avatars incluse) | index.html ✓ |
| GA4 `G-FEL71QVHNL` | pages modifiées ✓ |
| Cache JS `main.js?v=26` | inchangé (js/main.js non modifié) ✓ |
| CTA `data-cta="guidelink"` | volleyball-legends.html ✓ |
| GAG2 ≥ 1200 mots | 1293 ✓ |

**Note sandbox** : `git status` exécuté dans le bac à sable ne liste que `tools/code-watch.json` car le mount Linux est en retard sur les écritures des outils fichier. Les modifications d'`index.html` et `codes/volleyball-legends.html` sont bien présentes sur le disque Windows réel (confirmé via l'outil de lecture) et seront prises par `git add -A` côté Peter.

## Fichiers touchés ce run
- `codes/anime-squadron.html` — restauré (corruption octets nuls)
- `codes/noob-incremental.html` — restauré (corruption octets nuls)
- `tools/code-watch.json` — 27 snapshots rafraîchis + groupIds ajoutés + codes Volleyball Legends
- `codes/volleyball-legends.html` — 3 nouveaux codes, dates et compteurs au 22 juin
- `index.html` — bannière « Jeu de la semaine » → Grow a Garden 2
- `rapport-zoneblox-2026-06-22.md` — ce rapport

## À suivre au prochain run
- Synchroniser la **miniature Grow a Garden 2** (nouveau hash `71ae7859…`) partout + bump cache.
- Re-vérifier Volleyball Legends (cadence d'updates rapide).
- Pages codes existantes à auditer pour le seuil 1200 mots.

## Mise à jour Mini War (demande de Peter, en cours de journée)

**Changement majeur détecté** : la mise à jour du 20 juin 2026 de Mini War a introduit son **tout premier système de codes** (confirmé dans la description live + Pro Game Guides + Pocket Tactics). La page était jusque-là en mode « pas de code ».

`codes/mini-war.html` entièrement basculée en page à code actif :
- **Code ajouté** : `MINIWAR` → 5 000 Cash + 50 Gems (vérifié sur 2 sources le 22 juin).
- Tableau de codes réel + étapes de redeem exactes (Boutique → « Redeem a code »).
- **Miniature corrigée** : le hero utilisait un SVG (interdit) → remplacé par la vraie miniature `tr.rbxcdn.com/180DAY-2cb3c3df…` (vérifiée live via l'API, hash inchangé), SVG conservé en fallback `onerror`.
- Dates « Vérifié le » → 22 juin ; intro, section « Y a-t-il des codes », FAQ visible, JSON-LD FAQ, dateModified, About et meta/og-description mis à jour pour refléter l'existence du code.
- Listings synchronisés : `codes:1` + date 22 juin dans `GAMES_INDEX` et la carte d'accueil (`js/main.js`) ainsi que dans `ALL_GAMES` (`codes/index.html`).

**Étape 9 — Cache JS** : `js/main.js` ayant été modifié, la version a été bumpée **v=26 → v=27** dans **tous les fichiers HTML** (266 fichiers + les 3 édités aujourd'hui via l'outil fichier). Vérifié via l'outil fichier (lecture disque réelle) : **0 fichier reste en v=26**, tous en v=27 ; `node --check js/main.js` OK (710 lignes, régénéré proprement depuis HEAD + 2 éditions de valeur).

> Note technique : le mount bash a servi par intermittence des copies gelées/tronquées des fichiers édités via l'outil fichier — les vérifications finales ont donc été faites via l'outil fichier (Grep/Read), qui lit le disque réel. Le bump de cache via bash n'avait pas propagé les 3 fichiers édités à la main ; corrigé ensuite via l'outil fichier.

### Fichiers touchés (ajout Mini War)
- `codes/mini-war.html`, `codes/index.html`, `js/main.js` + bump `v=27` sur l'ensemble des pages HTML.

## Pour publier
Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
