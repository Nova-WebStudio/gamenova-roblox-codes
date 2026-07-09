# Rapport Zoneblox — 9 juillet 2026 (jeudi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = jeudi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

---

## 1. Codes vérifiés ce run (jeux « hot » prioritaires)

Vérification via WebSearch + fetch des pages sources, croisement avec `code-watch.json`. Règle appliquée : code maintenu ACTIF seulement si confirmé par **≥3 sources fiables OU source officielle** ; conflit → version la plus prudente + candidat « en attente ».

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Brainrot Evolution** | **CHANGEMENT (mise à niveau réelle)** — la page ne listait que **6** codes (Krang, Luck, Patrick, Fishybara, Tsunami, Love), tous encore actifs mais liste très incomplète | **Beebom (màj 4 juil.)** + **Pocket Gamer (màj 4 juil.)** — les deux listent exactement les mêmes nouveaux codes ; **Pocket Tactics** confirme le noyau | Liste **étendue à 24 codes actifs** bien corroborés. Nouveaux publiés : `Uncle`, `ZAPYBARA`, `BWAB`, `Capybara`, `Brainblock`, `Season10`, `Dragoni`, `EVIL`, `Combinasion`, `Beowl`, `Easter2026`, `Ding`, `Dididididi`, `Brainheaven`, `2026`, `List`, `Cheese`, `OP` (+ les 6 existants conservés). Compteur 6→24, titre/H1/JSON-LD « juin »→« juillet 2026 », `Mis à jour le 9 juillet 2026`, `dateModified` 2026-07-09, status-date table 9 juil. Page = **2194 mots**, 3 JSON-LD valides. |
| **Catch a Monster** | **Inchangé — conflit fort persistant (prudence)** | Pocket Tactics (1 juil.) vs Pro Game Guides (3 juil.) | PGG marque `graon`/`magmorus`/`danvok`/`moovik` **actifs** ; PT les marque **expirés**. Les deux sources fiables se contredisent sur la majorité des codes ; une 3ᵉ source (« CAM Hub », codes préfixés `LIVENEW…`) ne corrobore ni l'une ni l'autre. **Page non modifiée** (ne pas dégrader). Candidats enregistrés « en attente » dans `code-watch.json`. |
| **World Fighters** | **Inchangé — sourcing ambigu (prudence)** | PGG (avril) + Pocket Tactics (mai) couvrent un **autre** jeu « World Fighters » (StarX / Dragon Ball, place 95630541662383) ; Beebom (juillet) seule source concordante avec notre jeu | Une seule source fiable concordante → insuffisant (règle ≥3). **Page non modifiée**. Note ajoutée : re-vérifier l'universeId `10032271327` et identifier la source dédiée avant tout remaniement. |
| **Blockspin** | **Inchangé** | Pocket Tactics, Dexerto, Pocket Gamer | Système de **codes referral** (1 par compte). `HURRICANE_RELEASE`, `UNDER_THE_BARREL`, `M16_RELEASE`, `W7C28D` confirmés. Rien à changer. `lastChecked` bumpé. |

**Codes ajoutés (actifs) :** 18 (Brainrot Evolution).
**Codes déplacés en « expirés » :** 0.
**Candidats « en attente » enregistrés :** Catch a Monster (`massglaw`, `clacerglaw`, `cabshark`, `ungolem`, `teravok`, `dueggy`, `bullordy`, `jokairy`, `solguard`, `stumfoxy`, `poseidive`, `nampyra` — conflit PT↔PGG).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **9 juillet 2026** sur **les 166 pages** `codes/<slug>.html` (idempotent, exactement 1 par page, 0 doublon, 0 page sans ligne). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf **Brainrot Evolution** (changement réel de liste → « Mis à jour le 9 juillet 2026 »).

## 3. Correctif d'intégrité — version cache JS

Détecté au QC : **4 pages non suivies (untracked, en attente de commit)** référençaient `main.js?v=33` alors que tout le reste du site (et `js/main.js`, inchangé) est en **`v=32`** : `codes/clean-the-supermarket.html`, `codes/drain-the-lake.html`, `guides/clean-the-supermarket.html`, `guides/drain-the-lake.html`. Ces 4 pages ont été **ramenées à `main.js?v=32`** pour restaurer l'uniformité (311/311 pages en `v=32`). Non causé par ce run — corrigé par prudence.

## 4. Jeux « hot » NON revus en profondeur ce run (à prioriser au prochain run)

**Catch a Monster** (passe dédiée requise dès qu'une 3ᵉ source fiable tranche le conflit PT↔PGG), **World Fighters** (identifier la bonne source dédiée + vérifier l'universeId), puis `run-a-restaurant`, `noob-incremental`, `tower-defense-simulator`, `pet-simulator-99`, `100-days-at-sea`, `spin-a-soccer-card`, `merge-a-nuke`, `defend-ur-base-with-anime`, `fifa-super-soccer`, `hypershot`, `catch-a-monster`. Blox Fruits / Grow a Garden / Steal a Brainrot / Anime Vanguards / Fisch / Blade Ball / Blue Lock Rivals / Volleyball Legends / Anime Last Stand / King Legacy / Fruit Battlegrounds / Squid Game X / VV: ULTIMATUM : vérifiés les 05–08/07 (inchangés). Reste du catalogue (~150 pages) : rafraîchissement de date reçu.

## 5. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **Jeu de la semaine :** non touché (jeudi).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32` après correctif §3).

## 6. QC (résultat)

- ✅ **~170 fichiers** scannés (166 pages codes + 4 pages correctif cache + `code-watch.json`) : **0 null byte**, toutes les pages HTML finissent par `</html>`, `code-watch.json` finit par `}` (JSON valide, 27 snapshots).
- ✅ Les 166 pages codes : « 🔄 Vérifié le 9 juillet 2026 » présent (1 par page, 0 doublon) ; 0 page restée au 8 juillet.
- ✅ Page éditée (Brainrot Evolution) : GA4 `G-FEL71QVHNL` présent, `data-cta="guidelink"` (1 seul), nav 7 entrées (Avatars OK), cache `main.js?v=32`, **≥1200 mots** (2194), 3 blocs JSON-LD valides, compteur 24, titre/H1 « juillet 2026 ».
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (311/311 pages).
- ✅ `js/main.js` non modifié → pas de `node --check` requis (inchangé).
- ✅ `tools/code-watch.json` : JSON valide, 0 null byte ; snapshots `lastChecked` au 2026-07-09 pour brainrot-evolution (24 knownCodes), catch-a-monster (pending), world-fighters (note), blockspin.
- ✅ Aucun rédactionnel anglais introduit (reward-tags FR).

**Fichiers touchés :** 166 pages `codes/*.html` (rafraîchissement date) dont `codes/brainrot-evolution.html` (changement de codes réel) + 4 pages correctif cache (`codes/clean-the-supermarket.html`, `codes/drain-the-lake.html`, `guides/clean-the-supermarket.html`, `guides/drain-the-lake.html`) + `tools/code-watch.json` + ce rapport.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
