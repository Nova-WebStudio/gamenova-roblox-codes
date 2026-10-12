# Rapport ZoneBlox — 2026-10-02 (slot 05h, vendredi)

> Full maintenance + editorial. Run planifié **03h00 UTC (05h Belgique)**, **exécuté avec fort retard** (livré ~15h12 UTC / 17h12 Belgique via le bridge). Aucun run n'avait tourné aujourd'hui (dernier rapport = 01/10, arbre de travail propre au démarrage). Toutes les modifs ci-dessous sont **sur disque, régénérées et QC-validées**. **Rien n'est poussé sur Git (push manuel).**

## CODES

### Corrections réelles (3 pages)
- **🔧 anime-eternal 13 → 33 codes.** Page très sous-listée (plafonnée à Update 55) alors que le jeu est à **Update 60P4**. Ajout de **20 codes Update 56 → 60P4** (Update56, Update56Delay, Update56P2, Update57, Update57HunterFix, Update57P2, Update58, Update58P2, Update59…, Update60…, JustAniceCode, SummerPart2) **confirmés par Pocket Tactics 23/09 + ProGameGuides** (les deux listent la série ; codes « update » permanents). h1 « septembre » → « octobre 2026 », verifDate → 02/10.
- **🔧 clover-retribution 14 → 13 codes.** **−3 codes périmés** explicitement marqués expirés par **PGG 28/09** (`!gravitydevilstuff`, `!wspainplusdelay`, `!earlybirdgetsdaspins`). **+2 codes** double-confirmés actifs (`!SPINS200`, `!DOUBLEUP` — **PT 23/09 + PGG 28/09**). ⚠️ Conflit de sources fort (PT 23/09 vs PGG 28/09 divergent beaucoup) → les autres chips anciens laissés en place faute de preuve explicite par code ; **nettoyage complet reporté** (voir queue).
- **🔧 anime-origins 9 → 7 codes.** **−5 périmés** explicitement expirés par **GamesRadar 01/10** (`100K!`, `ChallengesFixed`, `GAMESPEED`, `TYKaito!`, `THANKYOU!`). **+3 codes** double-confirmés (`HolyGrail`, `Update2`, `Labyrinth` — **Beebom 30/09 + GamesRadar 01/10**). `HappyPatch!` laissé (pas de preuve explicite d'expiration).

### Hot games revérifiés — aucun changement de chips (verifDate → 02/10)
- **blue-lock-rivals** (4 : SNUFFYUPD, NEWMASTER, UBERSVOTE, WSNUFFY) = **Beebom 30/09 + PGG 01/10** (match exact).
- **volleyball-legends** (3 : UPDATE_89, WE_CURSED, SKELETON) = **Fossbytes 01/10 + PGG 26/09** (match exact).
- **grow-a-garden** (2 : RDCAward, BEANORLEAVE10) = **Beebom 01/10** (torigate confirmé expiré).
- **anime-vanguards** (22) = **Pocket Tactics 27/09** (match exact).
- **steal-a-brainrot** (1 : BESTBRAINROTEVER) = **conflit résolu** : **mmoculture 30/09** le confirme actif (La Vacca Saturno). Gardé.

### Rotation catalogue (catalogVerify → 02/10)
- 8 jeux horodatés aujourd'hui : les 5 hot ci-dessus + anime-eternal + clover-retribution + anime-origins.
- **universal-tower-defense-x** : revu (theclick 28/09 ne confirme que les 3 codes football) — **non modifié** (corrigé hier, pas de preuve d'expiration pour les 4 UTDZ). Divergence notée.

### Non revérifié / conflits laissés en attente
- **anime-champions-simulator** : **aucune source datée du mois courant** (PocketGamer juin 2025, PCGamesN févr. 2025 = inexploitables). 11 chips **non touchés**, verifDate **non rafraîchie** (reste 09-10). Jeu possiblement en fin de vie côté codes → envisager dé-priorisation.
- **candidats non ajoutés faute de 2e source** : clover `!changedmainmenu`/`!imtiredbutweballsolosoon`/`!lephos999thbirthday` (PGG seul) ; anime-origins `TowerFixed`/`RBD!`/`AuraMonster`/`Update1` (GamesRadar seul) ; aniimo 4 codes Beebom.

### Candidats en attente / sources officielles
- Rotation la plus ancienne encore à traiter (09-10 → 09-17) : anime-astral-simulator (100), anime-battle-rng (35), dragon-blox (82), anime-spirits, slime-rng, rng-heroes, anime-squadron, blox-monsters, fire-force-online, jujutsu-infinite, evade. Reportés faute de temps sur ce run unique tardif.

## SEO
- Aucune nouvelle URL (**kill switch** maintenu). Valeur du jour = **fiabilité + fraîcheur** : 3 pages périmées/sous-listées corrigées (anime-eternal, clover-retribution, anime-origins), hot games reconfirmés, un conflit tranché (steal-a-brainrot).
- `update-before-create` appliqué : GTA 6 = enrichissement evergreen, jamais de nouvelle URL.
- `sitemap.xml` régénéré : **383 URLs** (lastmod : verifDate 184, Mis à jour 11, mtime 188).

## NOUVEAUX JEUX
- Aucun ajout. Roblox Fall Games Preview (officiel) = marketing ; aucun titre neuf réunissant traction réelle + codes réels + page manquante.

## CONTENU
- Aucun guide / tier list / article créé (« 2 excellents > 20 faibles »).

## ANIIMO (data-driven)
- `lastChecked` → 02/10. **11 codes reconfirmés actifs** par **Beebom 01/10** (résout la divergence « seulement 2 codes » des runs précédents : PGG/Destructoid ne listaient qu'un sous-ensemble). 4 codes potentiels repérés chez Beebom (aniimazingfroyo, aniimonow, anywhereaniimo, anythinganiimo) — **source unique**, non ajoutés. `build_site.py` relancé.

## GTA 6
- **Backfill evergreen** : ajout du jalon **Netflix « An Extended Look »** (27/08/2026, **27 min de gameplay officiel PS5**, Jason & Lucia / Leonida) à `data/gta-6/updates.json` (confiance HIGH, Variety + PC Gamer). Jalon officiel majeur qui manquait à l'evergreen. **UPDATE evergreen, aucune nouvelle URL, aucun asset copyrighté intégré.**
- Veille : pas d'annonce officielle Rockstar nouvelle en 24h (rumeurs « annonce cette semaine » techradar + trailer 3 attendu novembre, **non confirmés**). Sortie maintenue **19 nov 2026**. CONFIRMÉ/RAPPORTÉ/RUMEUR séparés.

## FC (vertical `data/fc-27/`)
- ⚠️ **Note de périmètre** : la spec vise « FC 27 » mais le jeu **live** en octobre 2026 est **EA Sports FC 26** (sorti sept. 2026). Promos Saison 1 connues (Ultimate Scream / Rewind). **Monitor** : rien de concret (SBC/promo daté) justifiant une page. **À clarifier avec Peter** : le vertical doit-il couvrir FC 26 (live) ou rester en préparation FC 27 (sept. 2027) ?

## EDITORIAL INTELLIGENCE
- **Top actions** : anime-eternal (+20 codes, Update 56→60), anime-origins & clover-retribution (pages périmées nettoyées), GTA 6 evergreen enrichi, steal-a-brainrot conflit tranché.
- Articles créés : 0. Pages codes modifiées : **3 corrections de contenu** + **5 revérifications** (verifDate). GTA 6 + Aniimo mis à jour (data).
- Sujets ignorés : marketing GTA 6/Fall Preview sans valeur joueur, nouveaux jeux sans traction+codes.
- `tools/editorial-intelligence.json` : meta 02/10, +topics `code-maintenance-2026-10-02` et `gta6-netflix-extended-look` (EVERGREEN). 18 topics.

## EDITORIAL QUEUE
- `EDITORIAL-QUEUE.md` régénéré. **URGENT** : veille officielle GTA 6. **À mettre à jour** : clover (nettoyage complet), anime-origins (candidats mono-source), anime-champions (source fraîche introuvable → dé-prioriser), aniimo (2e source). **Prochain run (03/10, samedi)** : hotGames + rotation des plus anciens restants (09-10→09-17).

## QC
- `node --check js/main.js` : **OK**.
- JSON valides : data/codes.json (**184 jeux, 1277 codes**), data/aniimo/codes.json, data/gta-6/updates.json, tools/code-watch.json, tools/editorial-intelligence.json, data/games-index.json.
- XML valides : sitemap.xml (**383 URLs**, finit `</urlset>`) + sitemap-games.xml (40 URLs).
- Pages modifiées : toutes finissent par `</html>`, **0 null byte**, **div équilibrés** (anime-eternal 206/206, clover 230/230, anime-origins 97/97), **GA4 `G-FEL71QVHNL` présent**.
- Cache JS : `main.js?v=47` inchangé (ni JS ni CSS modifiés → pas de bump).
- Changeset git : 20 fichiers (3 corrections contenu + 5 verifDate + data + sitemaps + mémoire + pages régénérées). Aucun fichier non lié touché. `/avatar/` non modifié ; fichiers `/games/` non édités à la main (régénérés via build_site).
- ⚠️ **Observation pré-existante (non régression)** : codes-anime-eternal / clover-retribution / anime-origins n'ont **pas** de bloc `data-cta="guidelink"` (déjà absent dans les sauvegardes). À corriger lors d'une passe CTA dédiée, hors périmètre codes.

## SAUVEGARDES
- Backups avant édition conservés sur la machine (hors dossier connecté) : anime-eternal, clover, origins, gta6, aniimo, code-watch, editorial-intelligence, EDITORIAL-QUEUE.

---

**Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.**
