# Rapport Zoneblox — 6 juillet 2026 (lundi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = **lundi** → mise à jour du « Jeu de la semaine ».

---

## 1. Codes vérifiés ce run (jeux « hot »)

Vérification via WebSearch + croisement avec les trackers de référence (Pocket Tactics, Beebom, Pro Game Guides, Destructoid, PCGamesN, PC Gamer, GamesRadar) et `code-watch.json`. Règle appliquée : code maintenu ACTIF seulement si confirmé par **≥3 sources fiables OU source officielle** ; conflit → version la plus prudente.

| Jeu | Résultat | Constat |
|-----|----------|---------|
| **Grow a Garden 2** | **Inchangé** | Page = `TEAMGREENBEAN` (1 actif) ; conforme aux sources July 2026 (seul code actif confirmé du jeu). |
| **Grow a Garden** (original) | **Inchangé** | Page = `RDCAward`, `BEANORLEAVE10`. Confusion fréquente GaG/GaG2 dans les trackers → prudence, aucun changement. |
| **Steal a Brainrot** | **Inchangé** | Sources en conflit (0 code actif vs listes douteuses ; codes qui expirent en heures). Prudence → page laissée telle quelle. |
| **Blox Fruits** | **Inchangé** | Peu de nouveaux codes fiables ; listes des trackers polluées d'anciens codes. Aucun ajout confirmable ≥3 sources. |
| **Anime Vanguards** | **Inchangé** | Actifs page = `13.5`, `EternalAdversaries`, `Gambler` → correspond exactement à Beebom/Pocket Tactics/Destructoid/PGG (July 2026). |
| **Pet Simulator 99** | **Inchangé** | Page « Aucun code » ; conforme (jeu sans codes classiques, uniquement merch). |
| **Tower Defense Simulator** | **Inchangé** | Page « Aucun code » ; cohérent (codes = skins liés aux tours, non des récompenses génériques ; 0 code générique actif). Un code skin ajouté le 03/07 côté sources — non listable proprement sans la tour, laissé de côté. |
| **Squid Game X** | **Inchangé** | Codes page cohérents avec les sources (nouveau `$1.2M`, likes milestones). |
| **Run a Restaurant** | **Inchangé** | `RAR4EVER` toujours actif. |
| **Noob Incremental** | **Inchangé** | Codes CCU/community milestones cohérents. |
| **Fisch / Blade Ball / Blue Lock Rivals / Volleyball Legends / Anime Last Stand / World Fighters** | **Inchangés** | Vérifiés ; cohérents avec les listes récentes. World Fighters toujours affecté par l'homonyme « World Fighters Simulator » côté PGG → à re-vérifier. |

**Codes ajoutés :** 0. **Codes expirés déplacés :** 0. **Candidats en attente ajoutés :** 0.

Aucun changement réel de liste ce run → aucune date « Mis à jour le… » ni compteur modifié (règle d'honnêteté respectée).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **6 juillet 2026** sur **les 164 pages** `codes/<slug>.html` (idempotent, exactement 1 par page, 0 doublon). Les dates « Mis à jour le » n'ont **pas** été touchées.

## 3. Jeu de la semaine (lundi)

Bloc `FEATURED-WEEK` d'`index.html` remplacé : **Evomon → Grow a Garden 2** (jeu en tête des tendances Roblox cette semaine, ~500k joueurs simultanés, présent au catalogue avec codes + tier list + guide). Miniature réelle `tr.rbxcdn.com`, blurb FR honnête, 3 boutons (Codes / Tier list / Guide) vers les pages dédiées.

## 4. Jeux « hot » à prioriser au prochain run

`defend-ur-base-with-anime`, `spin-a-soccer-card`, `merge-a-nuke`, `vv-ultimatum`, `fifa-super-soccer`, `hypershot`, `catch-a-monster`, `brainrot-evolution`, `100-days-at-sea`, `king-legacy` (conflit en attente : `DinoxLive`/`Peodiz`/`SKGames`), `world-fighters` (homonyme à trancher). Reste du catalogue (~140 pages) : rafraîchissement de date reçu.

## 5. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`, 307 références).

## 6. QC (résultat)

- ✅ 164 pages `codes/*.html` : « 🔄 Vérifié le 6 juillet 2026 » présent (1 par page), 0 null byte, se terminent par `</html>`.
- ✅ `index.html` : featured = Grow a Garden 2, GA4 `G-FEL71QVHNL` présent, nav 7 entrées (Avatars OK), 0 null byte, `</html>`, div équilibrés.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (307 refs).
- ✅ `tools/code-watch.json` : JSON valide, se termine par `}`, 0 null byte ; 15 snapshots `lastChecked` mis à `2026-07-06`.

**Fichiers touchés :** 164 pages `codes/*.html` (rafraîchissement date) + `index.html` (Jeu de la semaine) + `tools/code-watch.json` + ce rapport.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
