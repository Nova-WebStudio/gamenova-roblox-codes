# Rapport Zoneblox — 11 juillet 2026 (samedi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = samedi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

Règle de sourcing appliquée : un code n'est ACTIF que s'il est confirmé par **≥3 sources fiables OU une source officielle** (Trello / Twitter-X / description in-game / shout du groupe). Conflit entre sources → version la **plus prudente** + candidat « en attente » dans `code-watch.json`.

---

## 1. Changements de codes réels ce run

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Grow a Garden 2** | **CHANGEMENT — 1 → 2 codes actifs** | PCGamesN, Pro Game Guides, PC Gamer, Beebom, FRVR, gag.gg (≥6 sources concordantes) | Ajout de **`WATERYOPLANTS`** (10 arrosoirs communs), introduit par la **MAJ 1.07.1 du 1er juillet 2026**. Confirmé actif par ≥3 sources fiables. Nouvelle ligne ajoutée au tableau, compteur **1 → 2 codes actifs** (game-meta + bannière live), FAQ et « En résumé » réécrits (juin→juillet, 2 codes), statut « fonctionne en juillet 2026 », `Mis à jour le` **24 juin → 11 juillet 2026**, dates de vérification internes → 11 juillet. Rappel intégré : les codes de l'original et du sequel **ne sont pas interchangeables** (RDCAward/torigate ≠ jeu 2). Page = **3797 mots**. |

**Codes ajoutés (actifs) :** Grow a Garden 2 +1 (`WATERYOPLANTS`).
**Codes retirés :** aucun.

## 2. Autres jeux « hot » vérifiés — aucun changement (prudence)

| Jeu | Sources | Décision |
|-----|---------|----------|
| **Blade Ball** | Beebom, GamesRadar, Pocket Tactics (juillet 2026) | Passe dédiée demandée au dernier run. Résultat : « aucun nouveau code depuis un moment, les codes existants restent valides ». Le cœur de la liste actuelle (RAMADAN, SPOOKYSEASON, 4BVISITS, SHARKATTACK, SUMMERWHEEL, SUMMERSTARTSHERE, ENERGYSWORDS, GIVEMELUCK, SERPENT…) est corroboré. **Liste maintenue telle quelle** (prudence, pas de changement réel de liste → « Mis à jour le » non touché). |
| **Grow a Garden (original)** | PCGamesN, Pro Game Guides, Beebom | Liste de l'original inchangée. Le candidat `TEAMGREENBEAN` (flaggé « en attente » le 10/07) est **définitivement rattaché à Grow a Garden 2**, pas à l'original — confusion des agrégateurs résolue. Inchangé. |
| **Steal a Brainrot** | PCGamesN, Beebom, Pocket Tactics, RBLXGUIDE, Roblox Den | Sources toujours en **conflit fort** (« 22 codes » vs « 0 code »). Candidats `BESTBRAINROTEVER` / `FREEOCTOBLOCK777` cités mais non confirmés ≥3 sources fiables ni source officielle → enregistrés **« en attente »** dans `code-watch.json`. Page maintenue **sans code** (prudence). |

## 3. SEO — mise à niveau du mois dans les titres (grosse correction)

Au début du run, **159 pages `codes/*.html` sur 166 affichaient encore « (juin 2026) »** dans leurs balises SEO alors qu'on est en juillet — signal de fraîcheur périmé pour la requête « codes <jeu> (juillet 2026) ».

Correction **chirurgicale** (Python, champ par champ) du tag mensuel `(juin 2026) → (juillet 2026)` **uniquement** dans : `<title>`, `<meta name="description">`, `<meta property="og:title">`, `<meta property="og:description">`, `"headline"` (JSON-LD) et `<p class="desc">` (hero), plus les H3 de section « Tous les codes … actifs » / « Codes Mini-Guerre actifs ».

- **166/166 titres** sont désormais en « (juillet 2026) » (0 restant en juin, hors `mini-war.html` = stub de redirection).
- **Non touché** (règle d'honnêteté) : les `dateModified`, les dates « Mis à jour le… », et les **faits historiques en prose** (ex. Anime Fighting Simulator « codes signalés actifs par plusieurs sources (juin 2026) », Grow a Garden 2 « sorti le 12 juin 2026 », label vidéo Speed Keyboard Escape) — laissés en juin volontairement.

## 4. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » passée au **11 juillet 2026** sur **les 166 pages** `codes/<slug>.html` (idempotent, exactement 1 par page, 0 doublon, 0 insertion nécessaire, 0 page restée au 10 juillet). Dates « Mis à jour le » non touchées, sauf **Grow a Garden 2** (changement réel de liste).

## 5. Incident d'intégrité corrigé (anti-troncature)

Après le batch d'édition SEO, le QC a détecté que **`codes/mini-guerre.html` était tronqué en fin de fichier** (se terminait par `</htm` au lieu de `</html>`, 0 null byte mais fin perdue). Fichier **restauré depuis `git show HEAD:`** puis toutes les modifications du run (Vérifié le 11 juillet, tags SEO juillet, H3) **ré-appliquées en un seul script Python à ancres uniques**, avec re-vérification : fin `</html>`, 0 null byte, `<div>` équilibrés. Un **scan d'intégrité complet sur les 312 pages HTML du site** confirme ensuite 0 fichier tronqué, 0 null byte, `<div>` équilibrés partout. Aucun fichier tronqué n'a été conservé.

## 6. Jeux « hot » NON revus en profondeur ce run (à prioriser au prochain run)

`blockspin`, `brainrot-evolution`, `world-fighters`, `noob-incremental`, `run-a-restaurant`, `100-days-at-sea`, `defend-ur-base-with-anime`, `vv-ultimatum`, `tower-defense-simulator`, `king-legacy`, `catch-a-monster` (vérifié en profondeur le 10/07), `spin-a-soccer-card` (10/07). Blox Fruits / Anime Vanguards / Fisch / Blue Lock Rivals / Volleyball Legends / Anime Last Stand / Fruit Battlegrounds / Squid Game X / FIFA Super Soccer / Merge a Nuke / Hypershot : vérifiés 05–10/07 (inchangés). Reste du catalogue (~150 pages) : rafraîchissement de date + mise à niveau du mois SEO reçus.

## 7. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes + correction SEO de masse).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **Jeu de la semaine :** non touché (samedi).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`).

## 8. QC (résultat)

- ✅ **0 null byte** sur les 312 pages HTML du site ; toutes finissent par `</html>`.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (0 page hors v=32).
- ✅ Les 166 pages codes : « 🔄 Vérifié le 11 juillet 2026 » (1 par page, 0 doublon) ; 0 page restée au 10 juillet.
- ✅ **166/166 titres** en « (juillet 2026) ».
- ✅ Page éditée (Grow a Garden 2) : GA4 `G-FEL71QVHNL` présent, `data-cta="guidelink"` (1 seul), nav 7 entrées (Avatars OK), cache `main.js?v=32`, **≥1200 mots** (3797), compteur cohérent (2 actifs), « Mis à jour le 11 juillet 2026 ».
- ✅ `tools/code-watch.json` : JSON valide, 0 null byte, finit par `}` ; snapshots `lastChecked` au 2026-07-11 pour grow-a-garden-2 (2 knownCodes), grow-a-garden, blade-ball, steal-a-brainrot (2 candidats « en attente »).
- ✅ Aucun rédactionnel anglais introduit.

**Fichiers touchés :** 166 pages `codes/*.html` (rafraîchissement date + mois SEO) dont `codes/grow-a-garden-2.html` (changement de codes réel) et `codes/mini-guerre.html` (restauré + réédité) + `tools/code-watch.json` + ce rapport. (167 fichiers suivis modifiés.)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
