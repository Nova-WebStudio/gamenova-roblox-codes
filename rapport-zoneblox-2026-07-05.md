# Rapport Zoneblox — 5 juillet 2026 (dimanche)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = dimanche → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

---

## 1. Codes vérifiés ce run (jeux « hot »)

Vérification via WebSearch + fetch des pages sources concrètes, croisement avec `code-watch.json`. Règle appliquée : code maintenu ACTIF seulement si confirmé par **≥3 sources fiables OU source officielle** ; conflit → version la plus prudente + candidat « en attente ».

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Fruit Battlegrounds** | **CHANGEMENT** — liste active trop large, ramenée de **9 → 4 codes** | Pro Game Guides (01/07), Destructoid (12/06), Pocket Tactics (08/05) | Actifs confirmés conservés : **BIGMILLIHUNNID!, ITSTHEBILLION!, CODEFIX, 1M60WOWZER**. Déplacés en expirés (non confirmés / marqués inactifs par PGG) : `YOO1M110K`, `MILLI90SWAG`, `1M50INSANE`, `4MPUTAT3`, `1M40KRAZY!!`. Compteurs (4 codes actifs), libellé expirés (10), titres/paragraphe/bannière et dates « Mis à jour le » + « Vérifié le » actualisés au 5 juillet. |
| **King Legacy** | **Inchangé** (prudence sur conflit) | Pocket Tactics (01/07) + PC Gamer : `DinoxLive`/`Peodiz`/`SKGames` **actifs** ; Pro Game Guides (22/06) : les mêmes **inactifs** | Conflit → **prudence** : page maintenue à ses 5 codes (`<3LEEPUNGG`, `2MFAV`, `FREESTATSRESET`, `WELCOMETOKINGLEGACY`, `DragonColorRefund`). Candidats `DinoxLive`, `Peodiz`, `SKGames` enregistrés « en attente » dans `code-watch.json`. |
| **World Fighters** | **Inchangé** (à re-vérifier) | WebSearch (worldfighters.org, Beebom, PCGamesN…) | La page Zoneblox affiche déjà les codes de l'ère Berserk (`BERSERKUPDATE`, `SORRYYSACRIFICEBUG`, `SRRY4DELAY`), cohérents avec les sources. Pas de liste 3-sources propre pour le **bon** jeu (homonyme « World Fighters Simulator » de StarX chez PGG). Aucun changement, priorisé au prochain run. |
| **Blockspin** | **Inchangé** | Dexerto, Insider Gaming, Pocket Tactics | Trackers = 0 code « classique » actif ; `HURRICANE_RELEASE` / `UNDER_THE_BARREL` sont des codes referral/1-fois **persistants**. Page laissée telle quelle. |

**Codes ajoutés :** 0.
**Codes déplacés en « expirés » :** 5 (Fruit Battlegrounds).
**Candidats en attente enregistrés :** King Legacy — `DinoxLive`, `Peodiz`, `SKGames` (Pocket Tactics/PC Gamer actifs vs PGG inactifs).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **5 juillet 2026** sur **les 164 pages** `codes/<slug>.html` (idempotent, exactement 1 par page). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf **Fruit Battlegrounds** (changement réel de codes).

## 3. Jeux « hot » NON revus en profondeur ce run (à prioriser)

pet-simulator-99, tower-defense-simulator, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, world-fighters (re-vérifier). Blade Ball / Blue Lock Rivals / Volleyball Legends : vérifiés le 02/07. Blox Fruits / Grow a Garden / Steal a Brainrot / Anime Vanguards / Fisch / Anime Last Stand : vérifiés le 04/07. Reste du catalogue (~140 pages) : rafraîchissement de date reçu.

## 4. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes).
- **Guides / tier lists :** aucun créé/modifié ce run.
- **UGC :** non revu ce run.
- **Jeu de la semaine :** non touché (dimanche).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`, 307 références).

## 5. QC (résultat)

- ✅ `codes/fruit-battlegrounds.html` : se termine par `</html>`, 0 null byte, `<div>` équilibrés, GA4 `G-FEL71QVHNL` présent, `data-cta="guidelink"` présent (1 seul), **1512 mots** (≥1200). Table active = 4 lignes, expirés = 10 lignes.
- ✅ Les 164 pages codes : « 🔄 Vérifié le 5 juillet 2026 » présent (1 par page), 0 null byte, se terminent par `</html>`.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (307 refs).
- ✅ `tools/code-watch.json` : JSON valide, se termine par `}`, 0 null byte ; snapshots `fruit-battlegrounds`, `king-legacy`, `world-fighters`, `blockspin` mis à `2026-07-05`.

**Fichiers touchés :** 164 pages `codes/*.html` (rafraîchissement date) dont `codes/fruit-battlegrounds.html` (changement de codes réel) + `tools/code-watch.json` + ce rapport.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
