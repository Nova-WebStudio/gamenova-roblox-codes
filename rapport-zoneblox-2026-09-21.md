# Rapport Zoneblox — 21 septembre 2026 (lundi)

Run quotidien automatique. Priorité respectée : **vérification des codes d'abord**, puis Directeur SEO, éditorial et régénération. Aucun `git push` effectué (Peter pousse manuellement).

---

## (a) CODES VÉRIFIÉS

### hotGames (12 vérifiés — 1 modifié)

**Modifié :**
- **Anime Vanguards 8 → 3 actifs.** Pro Game Guides (18 sept.) ne liste que **4 actifs** et classe explicitement MiniUpd2 / Wrath / Retribution en *inactifs* ; codes qui expirent ~2 semaines après sortie. Retirés de la liste active (ils étaient déjà présents en « expirés ») : **MiniUpd2, Wrath, Retribution, 1DayDelay, 25thHour**. Conservés (confirmés Pocket Tactics 16 sept. + PGG 18 sept.) : **Assault, SummerLeaving, AnniNextHopefully**. Compteur héro 8→3. *En attente* : 100thTournament (PGG seul).

**Confirmés stables (« Vérifié le » → 21 sept.) :**
- **Blade Ball** (15) — identique à GamesRadar 18 sept.
- **Blue Lock Rivals** (3 : NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK!) — confirmés GamesRadar 14 sept. *En attente* : SNUFFYSOON/BUGFIXES/UBERSCONTINUES/SORRYFORNIKODELAY (candidats plus récents non confirmés par ≥3 sources ; Pocket Gamer = aggregat sur-inclusif écarté).
- **Volleyball Legends** (3 : UPDATE_87/RONIN_RETURN/KATANA) — confirmés GamesRadar 14 sept. *En attente* : UPDATE_88/GET_SLIMED/XP_BOOST (source unique 21 sept.).
- **King Legacy** (8) — Pocket Tactics 18 sept. *En attente* : <3LEEPUNGG (source unique).
- **Fruit Battlegrounds** (2) — sous-listage volontaire (~45 codes milestone existent, non expirants) : acceptable.
- **Grow a Garden** (2 : RDCAward/BEANORLEAVE10) — confirmés (torigate reste expiré).
- **Steal a Brainrot** (0) — confirmé « aucun code actif ».
- **Pet Simulator 99** (0) — plus de codes publics (merch only).
- **Steal an Egg** (0) — pas de système de codes (confirmé PCGamesN/Pocket Tactics).
- **Catch a Monster** (8) — jeu neuf sans expiration, sous-listage acceptable.
- **Squid Game X** (5) — tous encore « Active » sur Roblox Den (20 sept.). *En attente* : UPDATE11RELEASE (source unique).

### Rotation quotidienne (16 slugs — 4 modifiés, 5 confirmés OK, 7 à revérifier)

**Modifiés :**
- **Garden Tower Defense 2 → 0.** PGG (19 sept.) classe FANTASY/FRONTIER en *inactifs* (nos codes dataient du 5 sept., soit 13 j > cycle de 3 j de ce TD). Déplacés en expirés. TRIANGLE/SNIPER en attente (source unique PGG, autres sources encore sur SLAY/POTION → conflit).
- **Grow a Garden 2 3 → 4.** Ajout de **FREESEED** (confirmé PC Gamer + Pocket Tactics + GamesRadar — ≥3 sources ; noté « invites parfois bugués »). Nos 3 codes existants confirmés actifs.
- **Knockout 8 → 7.** **CIRCUSEVENT** retiré par le dev le 2 sept. → déplacé en expirés (faux-actif). Les 7 autres confirmés (PC Gamer/game8/Beebom).
- **Be a Brainrot 2 → 0.** BRAINROT / RELEASE étaient des **faux-actifs** : Beebom confirme « aucun code publié à ce jour » pour ce jeu. Liste active vidée, texte corrigé honnêtement.

**Confirmés OK (« Vérifié le » → 21 sept.) :**
- **Plants vs Brainrots** (5) — evergreen, aucune expiration.
- **Rivals** (8) — evergreen ; sous-listage (21 codes existent) acceptable.
- **Da Hood** (DOG/SHARK) — **confirmés actifs par Pocket Gamer** → lève le flag « à revérifier » du J33.
- **Toilet Tower Defense** (0) — le jeu **original a été supprimé de Roblox** (0 code = correct ; la variante « Toilet Verse » est un autre jeu).
- **Murder Mystery 2** (0) — plus aucun code depuis des années (confirmé).

**À revérifier / à enrichir (non modifiés, prudence) :**
- **fish-it** — page vide alors que **~45 codes actifs** existent (PC Gamer/Insider Gaming). Enrichissement prioritaire prévu J35 (fast-expiry → cross-check ≥3 sources).
- **type-soul** — page vide, codes actifs existants (fast-expiry).
- **anime-reborn** — page vide, ~10 codes actifs (fast-expiry).
- **skibidi-masters-tower-defense** — seule source datée = 3 sept. (périmée) ; codes milestone ambigus (105K/160K vs nos 120/125/130K).
- **grimoires-era** — collision de noms sévère (Era / Legacy / Clover), aucune source datée sept. 2026 (**5ᵉ report**).
- **character-rng** — source Sept 9 annonce 7 actifs sans liste (vs nos 10) ; code « RNGHeroSquad » possiblement mal mappé.
- **button-rng-2** — sources périmées (juil./août) + collision RNG.

`tools/code-watch.json` mis à jour : `catalogVerify` (9 slugs), `lastRun`, `_rotationARevoir2026-09-21`, `_pending2026-09-21`.

> Note : les snapshots officiels Roblox (ÉTAPE 0, API univers/description/shout) n'ont pas été rafraîchis ce run — le shell n'a pas d'accès réseau aux endpoints Roblox et la vérification web multi-sources (substance de la priorité codes) a été privilégiée.

---

## (b) DIRECTEUR SEO — brique du jour + trending

**Trending re-scanné** (rblxdb / Roblox charts, sem. 13-21 sept.) : leaders — Steal an Egg (~1,7M), Steal a Brainrot, Blox Fruits, Grow a Garden, Plants vs Brainrots, 99 Nights, Sailor Piece, Forsaken, Knockout — **tous couverts** au catalogue (sailor-piece et forsaken présents en pages codes + ALL_GAMES). Aucun nouveau hit ≥4000 non couvert détecté.

**Brique J34 = homogénéisation du maillage du cluster « Plants vs Brainrots »** (top-5 hit, ~916K CCU). Ajout du bandeau CTA `data-cta="guidelink"` **manquant** sur `codes-plants-vs-brainrots.html` (page au template ancien) → boutons vers `/guides/plants-vs-brainrots.html` et `/tier-list/plants-vs-brainrots.html`. Cluster déjà complet (codes ✓ · guide ✓ · tier ✓) mais la page codes n'avait aucun lien sortant vers ses sœurs → maillage désormais bidirectionnel. Anti-cannibalisation : maillage interne uniquement, aucune nouvelle page. Roadmap J35 inscrite (priorité : enrichir `codes-fish-it.html`, page vide alors que ~45 codes existent).

---

## (c) Jeux ajoutés / guides / tier lists / Aniimo / UGC / jeu de la semaine

- **Jeu de la semaine (lundi)** : le bloc `<!-- FEATURED-WEEK-START/END -->` **n'existe plus** dans `index.html` (site refondu — marqueur `REFONTE-DONE` ; l'accueil expose désormais une section curatée « 🔥 À la une »). Aucun encart FEATURED-WEEK réintroduit (cohérent avec les encarts déjà retirés à la demande de Peter). **ÉTAPE 7 sans objet ce run.**
- **Aniimo** : les 10 codes actifs officiels (confirmés GamesRadar 19 sept.) sont tous présents dans `data/aniimo/codes.json` ; date de vérification rafraîchie au 21 sept. (`aniimoparty` conservé, aucune preuve d'expiration). Aucun code manquant.
- Aucun nouveau jeu ajouté, aucun nouveau guide/tier list créé ce run (pas de hit non couvert ; priorité donnée à la correction des faux-actifs).

**Volet éditorial (4 verticales) :**
- 🔥 **FC 27** : accès anticipé **en cours** (Ultimate/Ultimate Plus depuis le 18 sept.), sortie mondiale **25 sept.** ; Season 1 « Ones to Watch » du 17 sept. au 22 oct. → `data/games/fc-27.json` est **déjà à jour et exact** (releaseNote + sourcesNote au 19 sept.) : aucune correction nécessaire.
- 👀 **GTA 6** : sortie **19 novembre 2026** confirmée (Rockstar, depuis nov. 2025) ; précommandes ouvertes depuis juin. `data/games/gta-6.json` exact — rien de neuf à publier (MONITOR).
- **Roblox / Aniimo** : couverts ci-dessus.
- **Conclusion éditoriale** : aucune actualité assez importante et vérifiable pour justifier un nouvel article aujourd'hui au-delà de ce qui est déjà couvert/exact (qualité > quantité).

---

## (d) Régénération automatique

- `python3 tools/build_site.py` → OK (pages /games/ + Aniimo, `sitemap-games.xml` 39 URLs). Seul `games/aniimo/codes/index.html` modifié (reste idempotent).
- `python3 tools/build_home.py` → OK (5 sections) ; **2ᵉ passage identique → idempotence confirmée**.
- `python3 tools/build_codes_json.py` → OK (`data/codes.json` : 179 jeux, 1187 codes actifs).
- `python3 tools/build_sitemap.py` → OK (`sitemap.xml` : 368 URLs ; lastmod : verifDate=179, MàJ=11, mtime=178).

---

## (e) Fichiers touchés + QC

**30 fichiers modifiés** (21 pages codes-*.html, roadmap, `data/aniimo/codes.json`, `data/codes.json`, `data/games-index.json`, `games/aniimo/codes/index.html`, `sitemap.xml`, `sitemap-games.xml`, `tools/code-watch.json`).

**QC — tout vert :**
- `node --check js/main.js` : OK.
- Scan site complet : **0** fichier avec null bytes / sans `</html>` / `<div>` déséquilibrés.
- Fichiers modifiés : tous terminent correctement (`</html>` / `</urlset>` / JSON valide), 0 null byte.
- Compteurs héro corrigés : Anime Vanguards 3, Garden TD 0, GAG2 4, Knockout 7, Be a Brainrot 0.
- `data/codes.json` et `sitemap.xml` valides (JSON/XML).
- Cache JS **uniforme** : 344 références `main.js?v=42` (js/main.js non modifié → pas de bump).

---

## (f) Rubriques éditoriales

- 🔥 **TOP NEWS** : FC 27 — accès anticipé live (18 sept.), sortie 25 sept. (page déjà à jour). GTA 6 — sortie 19 nov. confirmée (rien de neuf).
- 🆕 **NOUVEAUX JEUX ROBLOX** : aucun nouveau hit ≥4000 non couvert détecté.
- 📰 **NOUVEAUX ARTICLES CRÉÉS** : aucun (rien ne dépassait le seuil de publication).
- 🛠️ **PAGES MISES À JOUR** : Anime Vanguards (8→3), Garden TD (2→0), GAG2 (3→4, +FREESEED), Knockout (8→7, −CIRCUSEVENT), Be a Brainrot (2→0), + bandeau CTA Plants vs Brainrots ; 16 dates « Vérifié le » rafraîchies.
- 🎁 **NOUVEAUX CODES** : FREESEED (Grow a Garden 2, ≥3 sources).
- 📊 **TIER LISTS MISES À JOUR** : aucune (pas de patch/rééquilibrage justifiant un changement).
- 🔎 **OPPORTUNITÉS SEO** : enrichir les pages codes vides à fort potentiel (fish-it ~45 codes, type-soul, anime-reborn) ; généraliser le bandeau CTA guidelink (11/179 pages seulement).
- 👀 **À SURVEILLER** : candidats « en attente » (BLR, VL, King Legacy, Squid Game X, Anime Vanguards) ; collision grimoires-era.

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.

---

## (g) Vérification export Search Console — « Page avec redirection » (162 pages)

**Fichier analysé** : `zoneblox.com-Coverage-Drilldown-2026-09-21.zip` (problème = *Page avec redirection*, tendance 40 → 162 pages de juin à sept.).

**Décomposition des 162 URL** : 106 vieux `/codes/<slug>.html`, 78 variantes `www.`, 14 `/tier-list/…` (variantes www), 6 `/codes/?cat=…` / `?q=…`, racines de dossiers `/codes/ /guides/ /tier-list/ /`.

**Diagnostic — l'essentiel du rapport est NORMAL et bénin.** « Page avec redirection » n'est pas une erreur : Google signale qu'une URL redirige (301) et indexe la cible. Ces redirections sont le résultat **attendu** de deux chantiers volontaires :
- la migration du 11 sept. `codes/<slug>.html` → `codes-<slug>.html` (301 corrects),
- la canonicalisation `www` → non-www et `http` → https.

Vérifs faites : le **sitemap.xml est propre** (format `codes-<slug>.html`, 0 vieux `/codes/`, 0 `?cat=`, 0 `www`), et **js/main.js génère déjà le bon format** `/codes-`. Le compteur grossit simplement parce que Google accumule d'anciennes URL en mémoire ; il se stabilisera/décroîtra. **Aucune action requise pour ces cas.**

**MAIS 2 vrais bugs trouvés et corrigés ce run :**

1. **Redirections cassées (301 → 404)** — `codes/clean-the-supermarket.html` et `codes/drain-the-lake.html` tombaient sur la règle générique `codes/<slug>.html → codes-<slug>.html`, or ces pages `codes-*.html` **n'existent pas** (ces 3 jeux — + `paint-and-seek` — n'ont qu'un guide, pas de page codes). Correctif `.htaccess` : ajout de 2 règles spécifiques (comme celle déjà présente pour paint-and-seek) redirigeant vers `/guides/<slug>.html`.
2. **20 liens internes** (pages servies) pointaient vers `/codes/<slug>.html` pour ces 3 jeux sans page codes → repointés : boutons « Codes » des guides `clean-the-supermarket`, `drain-the-lake`, `paint-and-seek` → `/tous-les-codes.html` ; cross-links de `tier-list/paint-and-seek.html` → `/guides/paint-and-seek.html`. Plus aucun lien vers une URL qui redirige/404 dans les pages servies (hors vieux dossier `codes/` qui redirige de toute façon).

**Note** : les 3 fichiers résiduels `en/…` existent encore physiquement mais sont déjà redirigés en 301 par `.htaccess` (aucun impact) — Peter peut les supprimer pour faire propre.

**Recommandation** : dans Search Console, pour le problème « Page avec redirection », inutile de lancer « Valider la correction » sur les URL de migration/www (comportement normal). Les 2 bugs 301→404 ci-dessus, eux, valaient le correctif. Pour réduire le volume à terme, on peut à un prochain run nettoyer les liens internes restants **dans les vieux fichiers `codes/*.html`** (1199 liens) — sans effet SEO (ils redirigent) mais bon pour la cohérence.

**Fichiers modifiés (correctif GSC)** : `.htaccess`, `guides/clean-the-supermarket.html`, `guides/drain-the-lake.html`, `guides/paint-and-seek.html`, `tier-list/paint-and-seek.html`. QC : fin `</html>` OK, 0 null byte, `<div>` équilibrés, `node --check js/main.js` OK.
