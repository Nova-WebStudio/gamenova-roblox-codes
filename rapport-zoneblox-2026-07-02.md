# Rapport Zoneblox — 2 juillet 2026 (jeudi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = jeudi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

---

## 1. Codes vérifiés ce run (jeux « hot »)

Vérification web (WebSearch + fetch des pages sources) et croisement avec `code-watch.json`.

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Volleyball Legends** | **CHANGEMENT** — Update 76 sorti, anciens codes expirés | RoCodes (liste explicite actifs/expirés), Beebom, GamesRadar, The Click, Roonby (01–02/07) | Page passée de **9 → 3 codes actifs** : `UPDATE_76`, `ENCHO_RETURNS`, `BALANCE_76`. « Mis à jour le » → 2 juillet 2026, compteur + paragraphes descriptifs actualisés. |
| **Blade Ball** | Inchangé | Pocket Tactics, The Click, GamesRadar | Aucun nouveau code. Set maintenu. |
| **Blue Lock Rivals** | Inchangé (set prudent conservé) | Pro Game Guides (MAJ 27/06, liste `GAGAREWORK`/`ADDRESSME`/`BEARCLAW` en NEW/actif) | PGG affiche 35 codes cumulés mais les sources sont en conflit sur les anciens ; on garde les **3 codes** confirmés récents. |
| **Anime Vanguards** | **CONFLIT — non modifié (prudence)** | Beebom (MAJ 22/06) : 13.5/EternalAdversaries/Gambler actifs ; agrégateurs (01/07) : « aucun code actif, LagGone expiré » | Page (8 actifs) laissée **inchangée**. À réconcilier au prochain run avec une source datée du jour. |
| **Anime Last Stand** | **À corriger — non modifié ce run** | RoCodes (01/07) : seulement **5 actifs** (`TheATDSituationIsCrazy`, `JoJoCurse`, `DemonicCyborg`, `ALSUPD1`, `World3Patch2`) | La page en affiche **21** (contenu figé au 10/06, probablement gonflé). 1 seule source datée → non modifié par prudence. **À trimmer au prochain run après cross-check ≥3 sources.** |

**Codes ajoutés :** 3 (Volleyball Legends : UPDATE_76, ENCHO_RETURNS, BALANCE_76).
**Codes expirés retirés :** 9 (Volleyball Legends : UPDATE_75, SPECTATING, SHOW_OFF, UPDATE_74, SEASON_16, SUMMER_UPDATE, UPDATE_73, JUNGLE_MAP, JUNE_2026).
**Candidats en attente enregistrés :** Anime Vanguards (conflit de sources), Anime Last Stand (sur-listage à trimmer).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Conformément à la règle des deux dates : ligne « 🔄 Vérifié le » mise à jour au **2 juillet 2026** sur **les 164 pages** `codes/<slug>.html` (idempotent, exactement 1 par page). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf Volleyball Legends (changement réel de codes).

## 3. Jeux NON revus individuellement ce run (à prioriser)

Faute de budget d'appels réseau, seuls 5 jeux « hot » ont été vérifiés sur le web ce run. Les autres pages n'ont reçu que le rafraîchissement de date. **À prioriser aux prochains runs :**

- Jeux « hot » restants de `code-watch.json` : grow-a-garden, steal-a-brainrot, fisch, anime-vanguards *(à réconcilier)*, pet-simulator-99, king-legacy, fruit-battlegrounds, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, blox-fruits.
- **anime-last-stand** : trim urgent (21 → ~5 actifs) après cross-check.
- Reste du catalogue (~140 pages) : rotation habituelle.

## 4. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité donnée à la vérification des codes).
- **Guides / tier lists :** aucun créé/modifié ce run.
- **UGC :** non revu ce run.
- **Jeu de la semaine :** non touché (jeudi).
- **js/main.js :** non modifié → **pas** de bump de cache (le site est uniformément en `main.js?v=32`, 306 références — la note « v=19 » du CLAUDE.md est obsolète).

## 5. QC (résultat)

- ✅ Toutes les pages codes se terminent par `</html>`.
- ✅ 0 null byte sur toutes les pages codes.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (306 refs).
- ✅ Volleyball Legends : GA4 (`G-FEL71QVHNL`) présent, bandeau `data-cta="guidelink"` présent (1 seul), ≥1200 mots (1469 mots).
- ✅ `tools/code-watch.json` : JSON valide, se termine par `}`, 0 null byte.

**Fichiers touchés :** 164 pages `codes/*.html` (rafraîchissement date) dont `codes/volleyball-legends.html` (changement de codes) + `tools/code-watch.json`.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
