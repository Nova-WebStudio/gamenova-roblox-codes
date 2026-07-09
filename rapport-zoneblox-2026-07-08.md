# Rapport Zoneblox — 8 juillet 2026 (mercredi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = mercredi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

---

## 1. Codes vérifiés ce run (jeux « hot » prioritaires)

Vérification via WebSearch + fetch des pages sources, croisement avec `code-watch.json`. Règle appliquée : code maintenu ACTIF seulement si confirmé par **≥3 sources fiables OU source officielle** ; conflit → version la plus prudente + candidat « en attente ».

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **VV: ULTIMATUM** | **CHANGEMENT (mise à niveau)** — la page ne listait que `MINIUPDATE` et `MIDVVEEK`, **tous deux expirés** | Pocket Tactics (màj 6 juil.) + RoCodes (màj 8 juil.) — **les deux** listent `UPD2`, `160KLIKES`, `35ROLLS` comme actifs | **3 codes actifs** publiés : `UPD2` (20 ability rerolls + 1 mythical build reset token), `160KLIKES` (20 ability rerolls), `35ROLLS` (35 ability rerolls + 1 mythical reset token). Ancien `MIDVVEEK`/`MINIUPDATE` → nouveau bloc « expirés ». Compteur (3 actifs), bannière, dates « Mis à jour le » + « Vérifié le » au 8 juil., FAQ visible + JSON-LD mis à jour. |
| **Catch a Monster** | **Inchangé ce run — à traiter en priorité (passe dédiée)** | Pocket Tactics (1 juil.) vs PGG/Destructoid (3 juil.) : **conflit fort** | PT liste comme actifs `crablade`/`spabling`/`fspegg`/`skillfix`/`crysting`/`pectshall`/`coin`/`xp`/`cam` et donne `graon`/`magmorus`/`moovik`/`danvok` **expirés** ; les agrégateurs listent `clacerglaw`/`massglaw` (absents de PT). Jeu très volatil, sources non concordantes → **page non modifiée** (prudence, ne pas dégrader). Candidats enregistrés « en attente ». Nécessite une passe dédiée multi-sources (≥3) avant remaniement complet. |
| **Squid Game X** | **Inchangé** | Beebom, Sportskeeda, Fandom | Sources récentes stables (`$1.2M`, prochain palier à 1,4 M de likes). Notre page contient déjà les 8 codes connus. Rien à changer. `lastChecked` bumpé au 8 juil. |

**Codes ajoutés (actifs) :** 3 (VV: ULTIMATUM — `UPD2`, `160KLIKES`, `35ROLLS`).
**Codes déplacés en « expirés » :** 2 (VV: ULTIMATUM — `MIDVVEEK`, `MINIUPDATE`).
**Candidats « en attente » enregistrés :** VV: ULTIMATUM (`UPDATE1`, `140KLIKES`, `SHUTDOWNFIX` — conflit PT↔RoCodes) ; Catch a Monster (`clacerglaw`, `massglaw`, `crablade`, `spabling`, `fspegg`).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **8 juillet 2026** sur **les 164 pages** `codes/<slug>.html` (idempotent, exactement 1 par page, 0 doublon). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf **VV: ULTIMATUM** (changement réel de liste → « Mis à jour le 8 juillet 2026 »). Remplacement ciblé sur la seule ligne « Vérifié le » (Python), sans jamais toucher « Mis à jour le » des pages modifiées le 7 juillet (King Legacy, Spin a Soccer Card, Defend ur base).

## 3. Jeux « hot » NON revus en profondeur ce run (à prioriser au prochain run)

**Catch a Monster** (passe dédiée multi-sources — priorité, conflit fort), **VV: ULTIMATUM** (surveiller si `UPDATE1`/`140KLIKES`/`SHUTDOWNFIX` se confirment actifs sur une 3ᵉ source pour les publier), puis `blockspin`, `run-a-restaurant`, `noob-incremental`, `tower-defense-simulator`, `pet-simulator-99`, `world-fighters`, `brainrot-evolution`, `100-days-at-sea`. Blox Fruits / Grow a Garden / Steal a Brainrot / Anime Vanguards / Fisch / Blade Ball / Blue Lock Rivals / Volleyball Legends / Anime Last Stand / King Legacy / Fruit Battlegrounds : vérifiés les 05–07/07 (inchangés). Reste du catalogue (~150 pages) : rafraîchissement de date reçu.

## 4. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **Jeu de la semaine :** non touché (mercredi).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`).

## 5. Incident maîtrisé (anti-troncature)

La première écriture de `codes/vv-ultimatum.html` via édition ciblée a **tronqué** le fichier (perte des 2 dernières lignes `</script></body></html>`, déséquilibre +2 div). Détecté immédiatement au QC (`tail` ≠ `</html>`, div ≠ 0). **Corrigé** : restauration depuis `git HEAD` + ré-application de **toutes** les modifications en **un seul script Python**, écriture unique, re-vérification. Le fichier se termine désormais par `</html>`, div équilibrés (0), 0 null byte, 1561 mots visibles. Aucun fichier tronqué laissé dans le commit.

## 6. QC (résultat)

- ✅ **165 fichiers modifiés** scannés : 0 null byte, toutes les pages HTML finissent par `</html>`, `code-watch.json` finit par `}`.
- ✅ Les 164 pages codes : « 🔄 Vérifié le 8 juillet 2026 » présent (1 par page, 0 doublon) ; distribution : 164/164.
- ✅ Page éditée (VV: ULTIMATUM) : GA4 `G-FEL71QVHNL` présent, `data-cta="guidelink"` (1 seul), nav 7 entrées (Avatars OK), cache `main.js?v=32`, **≥1200 mots** (1561), 3 blocs JSON-LD valides.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32`.
- ✅ `js/main.js` non modifié → pas de `node --check` requis (inchangé).
- ✅ `tools/code-watch.json` : JSON valide, 0 null byte ; 3 snapshots `lastChecked` au 2026-07-08 (vv-ultimatum, catch-a-monster, squid-game-x) ; VV `knownCodes` = `[UPD2, 160KLIKES, 35ROLLS]`, candidats « en attente » enregistrés.

**Fichiers touchés :** 164 pages `codes/*.html` (rafraîchissement date) dont `codes/vv-ultimatum.html` (changement de codes réel) + `tools/code-watch.json` + ce rapport.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
