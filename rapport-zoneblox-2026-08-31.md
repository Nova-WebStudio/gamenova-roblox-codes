# Rapport Zoneblox — 31 août 2026 (lundi)

## a) Codes vérifiés (priorité)

Re-scan multi-sources (Pro Game Guides, PCGamesN, PC Gamer, GamesRadar, Beebom) sur les jeux chauds. **2 changements appliqués :**

1. **Blue Lock Rivals — 6 → 9 codes actifs.** Ajout de **UBERSTAKEOVER**, **KINGNEXTWEEK**, **EGODEFENSE**. Sources : Pro Game Guides (29/08, liste les 9 comme actifs) + agrégat multi-sources (30/08 : gamesradar/pocketgamer/rocodes…). Les 6 codes déjà servis restent actifs d'après PGG. Compteur hero 6→9 ; prose « Dernière mise à jour » réécrite au 31/08.
2. **Anime Vanguards — renouvelé à 3 codes actifs.** Page devenue obsolète : anciens **Prepare, 1DayDelay, 25thHour, LetTheLarpingBegin** passés en expirés (PGG 30/08 les liste inactifs, dont Prepare) ; nouveaux **Retribution, Wrath, MiniUpd2** (update « Holy Retribution »). Compteur actifs 4→3, expirés 22→26 ; prose réécrite.

**Stables (aucun changement) :**

- **Blox Fruits** — 24 codes servis conformes à PCGamesN (28/08). Le seul extra de PCGamesN, « Chandler », **donne 0** → ignoré. `1LOSTADMIN` **confirmé expiré** par PCGamesN → **candidat en attente retiré**.
- **Grow a Garden** — RDCAward + BEANORLEAVE10. Conflit sur `torigate` (PGG actif vs Beebom expiré) → **gardé expiré par prudence**. « TEAMGREENBEAN » vu en recherche appartient à **GAG 2**, pas GAG.
- **Steal a Brainrot** — BESTBRAINROTEVER toujours actif.
- **Volleyball Legends** — Update 85 (UPDATE_85/SHIRO/BLOCKED) inchangé depuis le 30/08.

**Candidat en attente (prudence)** : **Fisch `SkycrestNextWeek`** — cité par des agrégateurs le 30/08 mais **GamesRadar (24/08, autorité) ne le liste pas** et < 3 sources nommées → non publié, à retester. Enregistré dans `tools/code-watch.json` (`_pending2026-08-31`).

**« Vérifié le »** rafraîchi au **31 août 2026** sur les **177 pages codes servies** (idempotent, 1 par page). `data/codes.json` régénéré : **177 jeux, 1230 codes actifs**.

**Jeux chauds non re-vérifiés en profondeur ce run** (stables au 30/08, à re-prioriser demain) : King Legacy, Anime Last Stand, Pet Simulator 99, Fruit Battlegrounds, World Fighters, Noob Incremental, et le reste du catalogue evergreen.

## b) Directeur SEO

- **Trending re-scanné (lundi)** : Steal An Egg #1 (~1,4 M CCU), Murder Mystery 2, Brookhaven, Grow a Garden, Steal a Brainrot, +1 Speed Keyboard Escape (= `evasion-clavier`, couvert), Anime Expeditions (couvert). **Aucun nouveau hit ≥ 4000 non couvert** → evergreen.
- **Brique réalisée** : **refonte de `tier-list/volleyball-legends.html`** (méta obsolète du 5 juin → 31 août). Le cluster Volleyball Legends était déjà **complet** (codes ✓ · tier list ✓ · guide ✓, reliés), la reco J21 « créer la tier list » était caduque. **Information gain** à la place : ajout d'un **tier S+** avec les 2 styles Secret de l'**Update 40** — **Hidari** (« Lefty Arm ») et **Jinko** (all-rounder serve/spike 100 %+) — que les concurrents classent au sommet et qui manquaient à la page ; réorg S+/S/A ; 2 write-ups FR sourcés ; ItemList + notice + date + og:description mis à jour. **Sources** : Pocket Gamer (04/08) + findingDulcinea (méta sept. 2026). **Intention** : *classement* (inchangée) → aucune cannibalisation, aucune nouvelle URL.
- **Prochaine brique (J22)** inscrite dans la roadmap : approfondir le guide how-to Volleyball Legends (mécaniques de spin/pity) OU compléter le maillon manquant du cluster Anime Vanguards.

## c) Autres

- **Jeux ajoutés** : aucun (pas de nouveau hit non couvert).
- **Guides / tier lists créés** : aucun nouveau ; tier list Volleyball Legends mise à jour (voir ci-dessus).
- **UGC** : non modifié ce run.
- **Encart évènements** : non touché (encart retiré de l'accueil à la demande de Peter — `js/events.js` non chargé).
- **Jeu de la semaine (lundi)** : **maintenu sur Steal An Egg** (toujours #1 des tendances) — aucun changement de bannière requis.

## d) Fichiers touchés + QC

**Modifiés :** `codes-blue-lock-rivals.html`, `codes-anime-vanguards.html`, `tier-list/volleyball-legends.html`, les 175 autres `codes-*.html` (date « Vérifié le »), `data/codes.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`, ce rapport. (Le diff inclut aussi le travail non encore commité du 30/08.)

**QC (tout vert) :**

- Null bytes : **0** sur les 186 fichiers modifiés.
- 181 fichiers HTML modifiés : tous se terminent par `</html>`, `<div>` équilibrés (delta 0).
- `sitemap.xml` finit par `</urlset>`.
- `node --check js/main.js` et `js/events.js` : OK. `data/codes.json`, `data/events.json`, `tools/code-watch.json` : JSON valides.
- Cache JS uniforme : `main.js?v=39` partout (main.js non modifié → pas de bump).
- GA4 (G-FEL71QVHNL) + nav active présents sur les 3 pages éditées à la main. JSON-LD de la tier list : 3 blocs valides. Aucune vidéo ajoutée (pas de risque dQw4w9WgXcQ).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
