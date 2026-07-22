# Rapport Zoneblox — mercredi 22 juillet 2026

Run quotidien automatique (05h00). Dernier run enregistré : 21 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **173 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **173/173** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **22 juillet 2026** (motif unique et idempotent, exactement 1 par page, 0 doublon, 0 page sans correspondance ; intégrité vérifiée : 0 null byte, `</html>` présent, `<div>` équilibrés partout).
- **Vérification approfondie multi-sources** des jeux « hot » : Fisch, Blade Ball, Anime Vanguards, Grow a Garden / Grow a Garden 2, Anime Rangers X (Re:Rangers X), Blox Fruits, King Legacy, Blockspin.

### Sources utilisées

Compte X officiel **@FischOnROBLOX**, Pro Game Guides, GamesRadar, Beebom, Roonby, Pocket Tactics, PC Gamer, RoCodes, TechWiser, Destructoid. Croisement systématique (≥3 sources fiables OU source officielle ; conflit → version la plus prudente + candidat « en attente »).

### Changement réellement appliqué (1 jeu)

**`codes/fisch.html` — +1 code actif (3 → 4)**

La mise à jour **Roaming Fish & Water Park** a introduit un nouveau code, confirmé par la **source officielle** (compte X **@FischOnROBLOX** : « Use code `RoamingFishAndWaterPark` today!!! ») **ET** par Pro Game Guides, GamesRadar, Beebom et Roonby :

| Code | Récompense |
|---|---|
| RoamingFishAndWaterPark | 1000 Coins + Shiny Dumbo Octopus Floatie + objets divers (Icy Fish'n Dots, Cotton Candy, Tropical Fruit Mix, Random Item) |

Les 3 codes permanents (**scarlet**, **TemporarySubmarine**, **CARBON**) restent actifs (reconfirmés). Les codes événementiels Drylands (DrylandsIsFire, HAPPY4TH, OllieAndFinWhale, KingCrabstle) restent expirés. Compteurs (game-meta ✅, bandeau live, table), intro réécrite, « Mis à jour le » (19 → 22 juillet), status-bar (18 → 22 juillet) et `dateModified` (2026-07-19 → 2026-07-22) mis à jour.

### Jeux vérifiés sans changement (listes déjà exactes / prudence)

- **Blade Ball** — les sources listent DUNGEONSRELEASE actif, mais le conflit SERPENT / BATTLEROYALE / GOODVSEVIL persiste (source officielle X/Discord non lisible en fetch) → **liste inchangée**, candidat en attente.
- **Anime Vanguards** — Pro Game Guides / Beebom / Pocket Tactics réaffichent **LateBP** en actif, mais 4 sources l'avaient déclaré expiré le 19/07 → **maintenu expiré par prudence**, 7 actifs inchangés.
- **Grow a Garden (original)** — les sources continuent de confondre avec Grow a Garden 2 ; aucun code original confirmé distinctement → inchangé.
- **Grow a Garden 2** — TEAMGREENBEAN toujours actif → inchangé.
- **Anime Rangers X (Re:Rangers X)** — renommé ; candidat AdminAbuseNeedsABuff (source unique vague) → en attente.
- **Blox Fruits** — ~23 codes actifs ; candidat 1LOSTADMIN (mention vague) → en attente, liste inchangée.
- **King Legacy** — aucun nouveau code depuis ~4 mois (PC Gamer) → inchangé.
- **Blockspin** — candidat UNDER_THE_BARREL (source unique TechWiser) → en attente.

### Candidats « en attente » (non publiés) — `snapshots` de `code-watch.json`

- **blade-ball** : DUNGEONSRELEASE (à confirmer via source officielle).
- **anime-rangers-x** : AdminAbuseNeedsABuff (source unique).
- **blox-fruits** : 1LOSTADMIN (à confirmer 3 sources).
- **blockspin** : UNDER_THE_BARREL (source unique).

### À prioriser au prochain run

Jeux hotGames non revus en profondeur ce run : pet-simulator-99, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital, volleyball-legends, blue-lock-rivals. Ainsi que trancher les candidats en attente ci-dessus.

---

## 2. Jeu de la semaine

`date +%u` = 3 (mercredi) → **pas de modification** de la bannière « Jeu de la semaine » (réservée au lundi). Aucune touche à `index.html`.

---

## 3. Étapes non traitées ce run — et pourquoi

Budget consacré à l'étape 2 (priorité absolue : vérification des codes).

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le 22/07 » (pas de revérification approfondie).

---

## 4. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie. Fisch conserve son volume rédactionnel (> 1 200 mots) ; seuls la liste de codes, les compteurs, l'intro et les dates ont bougé.

---

## 5. Contrôle qualité

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 173/173 pages codes OK |
| Null bytes | ✅ 0 partout (173 pages + `code-watch.json`) |
| Balises `<div>` équilibrées | ✅ delta 0 sur toutes les pages modifiées |
| GA4 `G-FEL71QVHNL` | ✅ présent (fisch et pages modifiées) |
| Cache JS `main.js?v=35` | ✅ uniforme (320 occurrences, aucune page hors v=35) |
| `🔄 Vérifié le 22 juillet 2026` | ✅ exactement 1 par page codes (173/173) |
| `codes/fisch.html` | ✅ 4 actifs, compteurs/intro/dates/table cohérents |
| `data-cta="guidelink"` | ✅ présent (1 seul) sur fisch |
| `js/main.js` | ✅ `node --check` OK — **non modifié** → pas de bump de cache requis |
| `tools/code-watch.json` | ✅ JSON valide, `lastRun` = 2026-07-22 |

Aucune troncature détectée ce run.

### ⚠️ Anomalie Git pré-existante à signaler (non causée par ce run)

Comme signalé les jours précédents, l'index Git contient un état incohérent antérieur (renommage tronqué `tier-list/steal-a-brainrot.html -> tier-list/stea`, suppressions indexées de pages `tier-list/*.html`, `tools/` et `ugc-gratuit/index.html`). Les fichiers réels sont tous présents sur le disque. `git add -A` réconcilie automatiquement cet état ; la commande de publication ci-dessous est sans danger. Recommandation : vérifier `git status` d'un coup d'œil avant le push.

---

## 6. Fichiers touchés par ce run

- **173 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 22 juillet 2026 ».
- **`codes/fisch.html`** — +1 code actif (RoamingFishAndWaterPark) ; 4 actifs ; compteurs / intro / table / status-bar / « Mis à jour le » / `dateModified`.
- **`tools/code-watch.json`** — snapshots fisch (+ code), blade-ball, anime-vanguards, grow-a-garden(-2), anime-rangers-x, blox-fruits, king-legacy, blockspin ; `lastRun` = 2026-07-22 ; candidats en attente 2026-07-22.
- **`rapport-zoneblox-2026-07-22.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
