# Rapport Zoneblox — samedi 18 juillet 2026

Run quotidien automatique. Dernier run enregistré : 15 juillet 2026 (3 jours d'écart).

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **167 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **164 pages** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **18 juillet 2026** (les 3 restantes étaient déjà à jour).
- **Aucun doublon** de ligne « Vérifié le » — l'insertion est restée idempotente.
- **8 jeux « hot » ont fait l'objet d'une vérification approfondie multi-sources** : Blox Fruits, Grow a Garden, Blade Ball, Blue Lock Rivals, Volleyball Legends, Anime Vanguards, Fisch, Anime Last Stand.

### Sources utilisées

Pocket Tactics (12/07), Beebom (06/07 et 30/06), GamesRadar (01/06), Pro Game Guides (13/07), Destructoid, PCGamer, bloxodes, Fischipedia (wiki officiel), wiki.vanguards.gg, Trello officiel Blox Fruits (board `imb75BzG`).

### Changements réellement appliqués

**`codes/volleyball-legends.html` — 9 codes actifs → 3**

Six codes des Updates 76 et 77 sont expirés, confirmé par ≥3 sources concordantes (Pro Game Guides, GamesRadar, Destructoid, bloxodes qui titre explicitement « 3 Active Codes ») :

| Code basculé en expiré | Récompense |
|---|---|
| UPDATE_77 | 5 Lucky Style Spins |
| RIKU | 5 Lucky Style Spins |
| HOLO_WALLS | 5 Lucky Ability Spins |
| UPDATE_76 | 5 Lucky Style Spins |
| ENCHO_RETURNS | 5 Lucky Style Spins |
| BALANCE_76 | 5 Lucky Ability Spins |

Restent actifs : **UPDATE_78, LEADERBOARD, NEW_PACK**. Un bloc « Voir les codes expirés (6) » a été créé sur la page (elle n'en avait pas). Compteurs, date « Mis à jour le », `dateModified` JSON-LD et paragraphe d'introduction réécrits en conséquence. Au passage : la meta description disait encore « juin 2026 » → corrigée en « juillet 2026 ».

**`codes/fisch.html` — 3 codes actifs → 7**

La mise à jour **Drylands** a apporté de nouveaux codes :

| Code ajouté | Récompense | Source |
|---|---|---|
| DrylandsIsFire | 1 000 C$, bateau Cactus, titre 🏜️ + objets | PGG, PCGamer, GamesRadar, Beebom |
| HAPPY4TH | 74 C$, skin MERICAAA + titre | PGG, PCGamer, GamesRadar, Beebom |
| OllieAndFinWhale | 1 000 C$, bateau Smudged Titan (niveau 25) | PGG, PCGamer, GamesRadar |
| KingCrabstle | Bateau Duck Floatie + objets | PGG, PCGamer, GamesRadar (remonté depuis les expirés) |

**`codes/anime-vanguards.html` — 21 codes actifs → 22**

Ajout de **WhoopsieDaisy** (100 Memoria Shards, niveau 30), confirmé par Beebom, Pro Game Guides, Destructoid et Pocket Tactics.

### Jeux vérifiés sans changement

- **Blox Fruits** — 24 actifs. Les agrégateurs en listent 23 : seul `SUB2GAMERROBOT_EXP1` n'est pas repris partout. Conservé (historiquement présent sur le Trello officiel). Aucun code nouveau.
- **Grow a Garden** — 2 actifs (RDCAward, BEANORLEAVE10), cohérent avec toutes les sources de juillet.
- **Blade Ball** — les 13 actifs de la page sont tous confirmés par Pocket Tactics (12/07) et GamesRadar. Aucun ajout (voir conflits ci-dessous).
- **Blue Lock Rivals** — la page Zoneblox est **en avance** sur Beebom : NELSHIDOU / NEWCHEMSOON / DEMON actifs, tandis que Beebom (30/06) liste encore GAGAREWORK / ADDRESSME / BEARCLAW comme « nouveaux » alors que la page les a déjà passés en expirés. Version la plus récente conservée.

### Candidats « en attente » (non publiés, conflits de sources)

Enregistrés dans `tools/code-watch.json` sous `_pending2026-07-18` :

- **Blade Ball / BATTLEROYALE, DUNGEONSRELEASE, GOODVSEVIL** — 2 sources les donnent actifs, 1 les donne expirés. Non publiés (règle de prudence).
- **Blade Ball / SERPENT** — Beebom le dit expiré, Pocket Tactics et GamesRadar le donnent actif. Conservé actif (2 contre 1, et PT est la source la plus récente).
- **Fisch** — Pro Game Guides annonce **29 codes actifs** au 13/07, incluant ~22 codes que Zoneblox liste en expirés. Écart non tranché : par prudence, seuls les 4 codes confirmés par plusieurs sources ont été remontés. Un code listé à tort comme expiré ne trompe personne ; l'inverse serait un mensonge.
- **Anime Last Stand** — la page publie **31 codes actifs** alors que les agrégateurs n'en confirment que 4 récents (DemonicCyborg, TheATDSituationIsCrazy, ALSUPD1, JoJoCurse). Écart trop important pour être tranché sur une seule passe.
- **Anime Vanguards** — 22 actifs publiés vs 7 annoncés par Pro Game Guides.
- **Anime Rangers X** — ~15 codes PGG additionnels toujours non vérifiés (report du 15/07).

### À prioriser au prochain run

1. **Anime Last Stand** — trancher l'écart 31 vs 4 (vérification dédiée, Trello `m1Mqaqkh` + Discord + X @shockz_Dev).
2. **Fisch** — trancher l'écart sur les 22 codes en expirés via Fischipedia (wiki officiel) + 2 agrégateurs.
3. **Anime Vanguards** — trancher l'écart 22 vs 7 via wiki.vanguards.gg.
4. **Anime Rangers X** — les ~15 candidats PGG en report depuis le 15/07.
5. Les 20 autres jeux `hotGames` non revus en profondeur ce run (steal-a-brainrot, pet-simulator-99, king-legacy, fruit-battlegrounds, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital).

---

## 2. Étapes non traitées ce run — et pourquoi

Le budget du run a été absorbé par l'étape 2, qui est la priorité absolue déclarée. Les étapes suivantes n'ont pas produit de modification :

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le » mais pas de revérification approfondie de ses codes.
- **Étape 7 (Jeu de la semaine)** — non applicable, on est **samedi** (`date +%u` = 6). La bannière `FEATURED-WEEK` n'a pas été touchée.

---

## 3. Contenu minimum (indexation)

Contrôle automatique du volume de texte visible sur les 167 pages codes : **aucune page sous le seuil de 1 200 mots**. Aucun étoffement nécessaire ce run.

---

## 4. Contrôle qualité

Scan d'intégrité sur les **167 fichiers modifiés** :

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 167/167 |
| Null bytes | ✅ 0 sur tous les fichiers |
| Balises `<div>` équilibrées | ✅ delta 0 partout |
| GA4 `G-FEL71QVHNL` | ✅ présent partout |
| Cache JS `main.js?v=34` | ✅ uniforme |
| Nav 7 entrées (dont Avatars) | ✅ complète partout |
| Bandeau `data-cta="guidelink"` unique | ✅ exactement 1 par page codes |
| Aucun `dQw4w9WgXcQ` | ✅ |
| `node --check js/main.js` | ✅ (fichier non modifié) |
| `tools/code-watch.json` | ✅ JSON valide, 30 snapshots |

### ⚠️ Incident de troncature détecté et réparé

`codes/volleyball-legends.html` s'est retrouvé tronqué après édition : le fichier se terminait par `</body>\n<` au lieu de `</body>\n</html>`. Détecté par le scan d'intégrité, réparé, revérifié. **Aucun autre fichier n'était affecté.** Rappel : ce type de troncature n'est pas un artefact d'affichage, il faut toujours revérifier après écriture.

### Note sur `CLAUDE.md`

Le fichier `CLAUDE.md` indique encore `main.js?v=19` comme version de référence. La version réellement déployée est **`main.js?v=34`**, uniforme sur tout le site. La commande de vérification documentée dans `CLAUDE.md` est donc à corriger — je ne l'ai pas modifiée d'office.

---

## 5. Fichiers touchés

- **164 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 18 juillet 2026 ».
- **`codes/volleyball-legends.html`** — 6 codes expirés, bloc expirés créé, compteurs / dates / intro / meta description mis à jour.
- **`codes/fisch.html`** — 4 codes ajoutés en actifs, compteurs / dates / intro mis à jour.
- **`codes/anime-vanguards.html`** — WhoopsieDaisy ajouté, compteurs / dates mis à jour.
- **`tools/code-watch.json`** — snapshots des 8 jeux vérifiés, `lastRun`, candidats `_pending2026-07-18`.
- **`rapport-zoneblox-2026-07-18.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
