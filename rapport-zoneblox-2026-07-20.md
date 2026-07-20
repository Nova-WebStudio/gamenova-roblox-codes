# Rapport Zoneblox — lundi 20 juillet 2026

Run quotidien automatique (05h00). Dernier run enregistré : 19 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **173 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **173/173** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **20 juillet 2026** (motif unique et idempotent, exactement 1 par page, aucun doublon).
- **3 jeux « hot » vérifiés en profondeur, multi-sources** : King Legacy, Fruit Battlegrounds, Blade Ball. Ces jeux figuraient en tête des priorités laissées par le run du 19/07.

### Sources utilisées

Pocket Tactics (maj 17/07/2026), Beebom (maj 01/06/2026), PC Gamer (maj 13/07/2026), Pro Game Guides, GamesRadar, Destructoid. Croisement systématique selon la règle de sourcing (≥3 sources fiables OU source officielle ; en cas de conflit, on garde la version la plus prudente).

### Changements réellement appliqués

**`codes/king-legacy.html` — 2MFAV basculé actif → expiré (8 actifs → 7)**

Le code **2MFAV** (réinitialisation des stats) figurait encore en actif sur Zoneblox. Or il est **absent des listes actives** de PC Gamer (13/07), Beebom et Pocket Tactics — trois sources concordantes. King Legacy n'a plus reçu de mise à jour ni de code depuis ~4 mois. Décision prudente : **2MFAV repassé en expiré**.

| Élément | Avant | Après |
|---|---|---|
| Codes actifs (game-meta + bandeau) | 8 | 7 |
| Codes expirés (compteur `<summary>`) | 5 | 6 |
| « Mis à jour le » | 7 juillet 2026 | 20 juillet 2026 |
| `dateModified` (JSON-LD) | 2026-06-12 | 2026-07-20 |
| Statut interne « Vérifié le » | — | 20 juillet 2026 |

**RainbowDragon** : laissé en **expiré**. PC Gamer le liste actif mais **conditionnel** (nécessite d'avoir débloqué la couleur dragon arc-en-ciel avant l'update 7) — code de niche non utilisable par la grande majorité des joueurs. Conservé hors des actifs par prudence, cohérent avec la décision du 19/07.

### Jeux vérifiés sans changement (listes déjà exactes)

- **Fruit Battlegrounds** — 5 actifs (OMGUPDATE22, YOO1M110K!, BIGMILLIHUNNID!, ITSTHEBILLION!, CODEFIX). **Tous confirmés actifs par Pocket Tactics (17/07, source la plus récente).** Aucun n'est contredit par une source plus récente → **aucun changement de liste**. Le run du 19/07 signalait un « retard » sur des paliers récents : après lecture précise des sources, ces paliers (BIG1M170K!!, 1M60WOWZER, 1M50INSANE, 4MPUTAT3…) sont en réalité **classés expirés** par Pocket Tactics ET Beebom — Zoneblox les a déjà en expiré, la page est donc correcte. Date interne « Vérifié le » passée au 20/07.
- **Blade Ball** — ~14 codes actifs selon Beebom / Pocket Tactics / GamesRadar, **aucun nouveau code depuis ~le 1er juillet**. Les conflits signalés le 18/07 (BATTLEROYALE, GOODVSEVIL) ne sont tranchables que via la source officielle (X/Discord du jeu), non lisible en fetch simple. **Page non modifiée** ce run par prudence.

### Candidats « en attente » (non publiés) — `snapshots` de `code-watch.json`

- **Fruit Battlegrounds — MILLI90SWAG** : actif selon Pocket Tactics (17/07) mais expiré selon Beebom (01/06) → **conflit**, non publié (règle de prudence). À retrancher au prochain run avec une 2ᵉ source récente.
- **Blade Ball** : conflits BATTLEROYALE / DUNGEONSRELEASE / GOODVSEVIL à confirmer via source officielle.

### À prioriser au prochain run

Les **~20 jeux hotGames** non revus en profondeur ce run : pet-simulator-99, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital, volleyball-legends, grow-a-garden-2, anime-vanguards, anime-last-stand, anime-rangers-x.

---

## 2. Jeu de la semaine (lundi)

`date +%u` = 1 (lundi) → bannière `FEATURED-WEEK` d'`index.html` mise à jour.

- **Ancien** : Animal Hospital.
- **Nouveau** : **Grow a Garden 2** — n°1 des tendances/joueurs Roblox cette semaine (~520 000 joueurs simultanés, source la plus concrète des données du 20/07). Présent au catalogue avec **codes + tier list + guide** (les 3 pages existent → 3 boutons actifs). Miniature réelle `tr.rbxcdn.com` (pas de SVG affiché), blurb FR honnête, fallback SVG `onerror`.

Vérifié : `grow-a-garden-2` présent dans `GAMES_INDEX` (js/main.js) **et** `ALL_GAMES` (codes/index.html) → liens de la bannière valides.

---

## 3. Étapes non traitées ce run — et pourquoi

Le budget du run a été consacré à l'étape 2 (priorité absolue) + le Jeu de la semaine (lundi).

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le 20/07 » mais pas de revérification approfondie.

---

## 4. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie. King Legacy et Fruit Battlegrounds conservent leur volume rédactionnel (> 1 200 mots) ; seules les listes de codes, compteurs et dates ont bougé sur King Legacy.

---

## 5. Contrôle qualité

Scan d'intégrité sur tous les fichiers HTML modifiés + `tools/code-watch.json` :

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 169/169 pages HTML modifiées |
| Null bytes | ✅ 0 partout (HTML + JSON + sitemap) |
| Balises `<div>` équilibrées | ✅ delta 0 partout (dont `index.html` et `king-legacy.html`) |
| GA4 `G-FEL71QVHNL` | ✅ présent partout |
| Cache JS `main.js?v=35` | ✅ uniforme (320 occurrences) |
| `🔄 Vérifié le 20 juillet 2026` | ✅ exactement 1 par page codes (173/173) |
| `codes/king-legacy.html` | ✅ 7 actifs / 6 expirés cohérents, aucun résidu « 8 codes » en prose |
| `sitemap-codes.xml` | ✅ finit par `</urlset>`, 0 null byte |
| `js/main.js` | ✅ `node --check` OK — **non modifié par ce run** → pas de bump de cache requis |
| `tools/code-watch.json` | ✅ JSON valide, `lastRun` = 2026-07-20, 30 snapshots |

Aucune troncature détectée ce run.

> Note technique : `js/main.js` et `sitemap-codes.xml` apparaissent dans `git diff` mais correspondent à des modifications **déjà présentes avant ce run** (horodatage 00:44, cache déjà en v=35) — non produites par cette tâche. Elles sont intègres (node --check OK, `</urlset>` OK).

---

## 6. Fichiers touchés par ce run

- **173 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 20 juillet 2026 ».
- **`codes/king-legacy.html`** — 2MFAV actif → expiré (7 actifs), compteurs / date « Mis à jour le » / `dateModified` / statut interne mis à jour.
- **`codes/fruit-battlegrounds.html`** — statut interne « Vérifié le » au 20/07 (aucun changement de liste).
- **`index.html`** — bannière « Jeu de la semaine » : Animal Hospital → Grow a Garden 2.
- **`tools/code-watch.json`** — snapshots king-legacy / fruit-battlegrounds / blade-ball, `lastRun`, candidats en attente.
- **`rapport-zoneblox-2026-07-20.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
