# Rapport Zoneblox — jeudi 23 juillet 2026

Run quotidien automatique (05h00). Dernier run enregistré : 22 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **173 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **173/173** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **23 juillet 2026** (motif unique et idempotent, exactement 1 par page, 0 doublon, 0 page sans correspondance). Intégrité vérifiée : 0 null byte, `</html>` présent, `<div>` équilibrés partout.
- **Vérification approfondie multi-sources** des jeux « hot » ciblés en priorité (ceux non revus en profondeur au dernier run + candidats en attente) : Blue Lock Rivals, Volleyball Legends, Steal a Brainrot, Pet Simulator 99, 100 Days at Sea, Blade Ball, Squid Game X, Grow a Garden / Grow a Garden 2, Anime Vanguards, Brainrot Evolution.

### Sources utilisées

Pro Game Guides, GamesRadar+, PC Gamer, Beebom, TheSpike, RoCodes, Pocket Tactics, Destructoid, PCGamesN, GameRant, Roonby, Dexerto. Croisement systématique (≥3 sources fiables OU source officielle ; conflit → version la plus prudente + candidat « en attente »).

### Changements réellement appliqués (2 jeux)

**`codes/100-days-at-sea.html` — 1 → 4 codes actifs**

La liste était en retard (1 seul actif « HERO », `20Pearls` classé expiré). Cinq sources fiables concordantes (Pro Game Guides, GamesRadar+, Beebom, RoCodes, GameRant — au 20/07) listent **4 codes actifs**, tous récompensant 20 Pearls :

| Code | Récompense |
|---|---|
| CORRUPT (nouveau) | 🦪 20 Pearls |
| HERO | 🦪 20 Pearls |
| ALIENS | 🦪 20 Pearls |
| 20Pearls | 🦪 20 Pearls |

Aucun conflit entre les sources fiables sur cette liste → ajout de **CORRUPT** et **ALIENS**, reclassement de **20Pearls** en actif. Compteurs (game-meta 1→4, bandeau live 1→4), « Mis à jour le » (13 → 23 juillet), status-bar « Vérifié le » (18 → 23 juillet) et `dateModified` (2026-06-19 → 2026-07-23) mis à jour. Section « codes expirés » retirée (0 expiré).

**`codes/blade-ball.html` — 13 → 14 codes actifs**

Le candidat **DUNGEONSRELEASE** (en attente depuis le 21/07) est désormais **confirmé par ≥3 sources fiables** (TheSpike, GamesRadar+, Beebom) : il accorde **50 Runes de Donjon**. Publié comme actif (ajouté en tête de tableau avec le badge NOUVEAU). Les 13 codes existants restent actifs et confirmés. Compteurs (game-meta 13→14, bandeau live 13→14, phrase « Il reste 14 codes actifs »), « Mis à jour le » (14 → 23 juillet), status-bar (18 → 23 juillet) et `dateModified` (2026-06-14 → 2026-07-23) mis à jour.

### Jeux vérifiés sans changement (listes déjà exactes / prudence)

- **Blue Lock Rivals** — 6 actifs (QOLUPD, QUARTERFINALSOON, REBALANCES, NELSHIDOU, DEMON, NEWCHEMSOON) : la page correspond exactement aux sources (Pro Game Guides, PC Gamer, RoCodes, Beebom) → inchangé.
- **Volleyball Legends** — 3 actifs (UPDATE_79, SEASON_17, FESTIVAL_UPD) : conforme à GamesRadar, Roonby, Pro Game Guides, Dexerto → inchangé.
- **Steal a Brainrot** — sources en conflit (aucune liste fiable stable ; certaines annoncent « aucun code ») → maintien de la version la plus prudente (aucun code publié) → inchangé.
- **Pet Simulator 99** — aucun code promotionnel actif (uniquement codes merch), confirmé par Beebom/RoCodes/TechWiser → inchangé.
- **Squid Game X** — sources en conflit (ensembles de codes divergents ; la page contient `$1.2M$` absent de l'agrégat, tandis que l'agrégat cite des codes anciens type `$500K$`/`$250K$`) → **inchangé par prudence** (ne pas retirer un code potentiellement actif ni ajouter des codes douteux).
- **Grow a Garden / Grow a Garden 2** — l'agrégat ne distingue toujours pas les deux jeux et n'énumère pas de nouveau code confirmé distinctement → inchangé.
- **Anime Vanguards** — 7 actifs ; LateBP et WhoopsieDaisy confirmés **expirés le 19/07** (GamesRadar/Pro Game Guides) → la page (LateBP en expiré) est correcte ; EEPart1 déjà présent → inchangé.
- **Brainrot Evolution** — aucune liste concrète confirmée par ≥3 sources concordantes → inchangé.

### Candidats « en attente » résolus / restants

- **Résolu** : blade-ball `DUNGEONSRELEASE` → publié (3 sources).
- **Résolu** : 100-days-at-sea `ALIENS` / `20Pearls` → publiés (5 sources concordantes, plus de conflit).
- **Restants** (non publiés, source unique/vague) : blox-fruits `1LOSTADMIN`, anime-rangers-x `AdminAbuseNeedsABuff`, blockspin `UNDER_THE_BARREL`.

### À prioriser au prochain run

Jeux hotGames encore non revus en profondeur (snapshot du 14–15/07) : tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, run-a-restaurant, catch-a-monster, animal-hospital. Ainsi que trancher les 3 candidats restants ci-dessus.

---

## 2. Jeu de la semaine

`date +%u` = 4 (jeudi) → **pas de modification** de la bannière « Jeu de la semaine » (réservée au lundi). Aucune touche à `index.html`.

---

## 3. Étapes non traitées ce run — et pourquoi

Budget consacré à l'étape 2 (priorité absolue : vérification des codes).

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le 23/07 » (pas de revérification approfondie).

---

## 4. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie. 100 Days at Sea et Blade Ball conservent leur volume rédactionnel ; seuls la liste de codes, les compteurs et les dates ont bougé.

---

## 5. Contrôle qualité

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 173/173 pages codes OK |
| Null bytes | ✅ 0 partout (173 pages + `code-watch.json`) |
| Balises `<div>` équilibrées | ✅ delta 0 sur toutes les pages modifiées |
| GA4 `G-FEL71QVHNL` | ✅ présent (100-days-at-sea, blade-ball) |
| Cache JS `main.js?v=35` | ✅ uniforme (aucune page passée hors v=35) |
| `🔄 Vérifié le 23 juillet 2026` | ✅ exactement 1 par page codes (173/173) |
| `codes/100-days-at-sea.html` | ✅ 4 actifs, compteurs/dates/table cohérents |
| `codes/blade-ball.html` | ✅ 14 actifs, compteurs/dates/table cohérents |
| `data-cta="guidelink"` | ✅ présent (1 seul) sur les 2 pages modifiées |
| `js/main.js` | ✅ **non modifié** → pas de bump de cache requis |
| `tools/code-watch.json` | ✅ JSON valide, `lastRun` = 2026-07-23 |

Aucune troncature détectée ce run.

### ⚠️ Anomalie Git pré-existante à signaler (non causée par ce run)

Comme signalé les jours précédents, l'index Git peut contenir un état incohérent antérieur (renommages/suppressions indexés de pages `tier-list/*.html`, `tools/`, `ugc-gratuit/index.html`). Les fichiers réels sont tous présents sur le disque. `git add -A` réconcilie automatiquement cet état ; la commande de publication ci-dessous est sans danger. Recommandation : un coup d'œil à `git status` avant le push.

---

## 6. Fichiers touchés par ce run

- **173 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 23 juillet 2026 ».
- **`codes/100-days-at-sea.html`** — 1 → 4 codes actifs (CORRUPT, HERO, ALIENS, 20Pearls) ; compteurs / table / status-bar / « Mis à jour le » / `dateModified`.
- **`codes/blade-ball.html`** — 13 → 14 codes actifs (+DUNGEONSRELEASE) ; compteurs / table / status-bar / « Mis à jour le » / `dateModified`.
- **`tools/code-watch.json`** — snapshots 100-days-at-sea (+2 codes), blade-ball (+DUNGEONSRELEASE, candidat résolu) ; refresh lastChecked des jeux revus ; `lastRun` = 2026-07-23 ; candidats en attente 2026-07-23.
- **`rapport-zoneblox-2026-07-23.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
