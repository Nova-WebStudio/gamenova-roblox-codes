# Rapport ZoneBlox — 2026-10-31 (run 05h, samedi)

> Fenêtre de recherche : nuit (12-24 h). Exécution autonome. Devise : **EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ TOPIQUE > SEO > QUANTITÉ.**
> Note horaire : tâche programmée 04:09 UTC (= 05:09 Belgique, CET), déclenchée 07:07 UTC. Traitée comme le run **05h full maintenance**.

## CODES

### hotGames vérifiés (sources datées fraîches) — 4
| Jeu | Décision | Source(s) | Changement |
|---|---|---|---|
| **blade-ball** | **+`GOODVSEVIL`** (🎡 spin gratuit) ; 15 existants confirmés actifs | next-stage.fr (31/10) **+** fossbytes (2 sources) | **Oui** → 16 codes, `dateModified` 31/10 |
| **king-legacy** | Set confirmé inchangé | next-stage.fr (29/10) | Non |
| **pet-simulator-99** | 0 code actif confirmé | gamewave.fr (28/10) + Pocket Tactics | Non |
| **100-days-at-sea** | `SPOOKY` actif (20 Pearls) | robloxden (vérifié 31/10 05:02 UTC) | Non |

- **`verifDate` 31/10** sur ces 4 pages ; **`catalogVerify` 31/10** enregistré.
- **Codes ajoutés : 1** (`GOODVSEVIL`, 2 sources). **Codes expirés retirés : 0** (aucune preuve d'expiration, §4).
- **Total codes actifs du site : 1339** (était 1338 ; `data/codes.json` régénéré).

### Candidats en attente / kill switch (MONITOR)
- **blade-ball `SORRY4DELAY` / `LIVEEVENTS`** : conflit (next-stage = actifs / fossbytes = expirés) → non ajoutés.
- **100-days-at-sea `RIVAL`** : robloxden l'affiche actif, mais 1 source + conflit historique → non ajouté.
- **king-legacy `UPDATE3_16` / `ALLO`** : dumps sans récompense → non ajoutés.
- **Fisch `ChapelTroubles`**, **Anime Vanguards `2ndAnniDay7`**, **grow-a-garden `torigate`** : mono-source → 2ᵉ source requise.

### Rotation (lot 05h)
- **Non traité ce run.** Lot de 38 pages (dont 31 jamais vérifiées — majorité novelty FR + clones anime à désambiguïser). Priorité donnée à l'exactitude des hotGames + verticales éditoriales. Backlog chronique : **169 pages non-hot > 3 j**. À reprendre avec sources fraîches/officielles.

### Sources officielles / honnêteté
Descriptions in-game / notices via médias fiables datés (next-stage.fr, fossbytes, robloxden, gamewave.fr, Pocket Tactics). Canaux Discord/Trello officiels non accessibles depuis cet environnement → recoupement multi-sources daté. « Mis à jour le » (= `dateModified`) touché **uniquement** sur blade-ball (codes réellement modifiés) ; « Vérifié le » rafraîchi sur les 4 pages parcourues.

## SEO
- **Intentions travaillées** : « codes <hotGame> » (long-tail winnable) — fraîcheur/exactitude des pages existantes. **Aucune nouvelle URL** (UPDATE before CREATE respecté).
- **Anti-cannibalisation** : aucune page créée ; maillage/CTA intacts (CTA `data-cta="guidelink"` **unique** vérifié sur les 4 pages).
- **Données structurées** : JSON-LD `ItemList` blade-ball resynchronisé (16 items + `dateModified` 31/10). Les 3 autres : `dateModified` **non touché** (codes inchangés — règle d'honnêteté).
- **Fraîcheur** : `sitemap.xml` régénéré (421 URLs ; lastmod : verifDate=206, « Mis à jour »=12, mtime=203, aucun fichier absent).
- **Prochaine brique** : cluster Aniimo Part II **data-driven** dès publication des données officielles des 51 créatures.

## NOUVEAUX JEUX
- **Aucun ajout.** Aucun nouveau jeu avec **preuve d'intérêt multi-source + codes réels** détecté (overnight = listicles/dumps recyclés). Kill switch, 0 nouvelle URL.

## CONTENU
- **Guides / events (Halloween)** : couverture déjà en place (Fisch `FischFright2026` ≤ 09/11, Blue Lock Rivals / 100-days-at-sea / Blade Ball = `SPOOKY`/`SPOOKYSEASON`). **Aucune nouvelle section** justifiée (pas de nouvel event confirmé ni de récompense détaillée). ⚠️ **Retrait des sections event programmé au run 05h du 01/11** (sauf `FischFright2026`).
- **Tier lists** : aucune modification (pas d'évolution réelle justifiant une nouvelle version).
- **Articles** : 0 (qualité > quantité).
- **Jeu de la semaine** : samedi → **N/A** (règle §30 : lundi uniquement).

## ANIIMO
- **Feed à jour** (`data/aniimo/updates.json`, 51 Aniimo, cap 70, Spar 4v4, LIVE 28-29/10). **Stats détaillées des 51 créatures toujours indisponibles en données officielles structurées** → **NON ingérées** (pas d'invention). Aucun code de lancement annoncé. Ingestion `creatures.json`/`locations.json`/`tier-list.json` dès disponibilité officielle.

## GTA 6
- **Aucun nouveau post Newswire officiel.** Le « rapport Edge Magazine » (via Insider Gaming / OpenCritic, 29/10) — carte **~2× GTA 5**, développement principal terminé — est **RAPPORTÉ**, pas une annonce officielle Rockstar → **non publié** (séparation CONFIRMÉ / RAPPORTÉ / RUMEUR). **Confirmés** : sortie **19/11**, préchargement **12/11**, bonus Vintage Vice City (préco avant 20/11), The Game Awards 10/12. Surveillance Newswire poursuivie.

## FC 27
- **Ultimate Scream Team 2 : LIVE** (beebom — équipe en jeu : Dembélé, Dybala, Pulisic, Griezmann, J.Félix, Frimpong + héros Sneijder/Touré/Futre/Marchisio/Matuidi/Ljungberg). **MAIS** : (1) **conflit d'attribution de version** — beebom/futbin labellisent « FC 26 » alors qu'**EA Sports FC 27 est sorti le 25/09/2026** (confirmé PSU / Insider Gaming, cohérent avec notre feed) ; (2) escouade listée **sans notes ni DCE recoupés par 2 sources exactes**. → **Kill switch exactitude : NON publié ce run.** À traiter 15h/22h dès confirmation propre. **Confirmés (feed)** : promo Scream fin **06/11**, token store **13/11**, Beaver Moon **24/11→01/12**. **Décision Peter** souhaitée sur le libellé FC 26/FC 27.

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) FC 27 Ultimate Scream Team 2 (live, à confirmer proprement) ; (2) Aniimo Part II — ingestion data créatures dès dispo ; (3) GTA 6 pré-lancement (Newswire, J-19).
- **Tendances** : aucune nouvelle tendance Roblox exploitable cette nuit (bruit/spam sur les recherches overnight).
- **Articles créés** : 0. **Pages mises à jour** : 4 pages codes (1 code ajouté + verifDate) + feeds régénérés.
- **Sujets ignorés** : rotation novelty FR / dumps recyclés sans preuve.
- **Sujets à surveiller** : FC 27 Team 2 (+ libellé version), Aniimo (data + codes), GTA 6 (Newswire), Blue Lock Rivals (reward `SPOOKY`), Fisch (`ChapelTroubles`), Anime Vanguards (`2ndAnniDay7`), 100-days-at-sea (`RIVAL`).
- `tools/editorial-intelligence.json` : 70 topics (meta 31/10 ; run-log 31/10 ajouté ; gta6 / fc27 / aniimo / anime-vanguards / steal-a-brainrot re-datés). `tools/code-watch.json` : `_notes2026-10-31` + `lastRun` 31/10 + 4 `catalogVerify`.

## EDITORIAL QUEUE
- **Urgents** : FC 27 Team 2 (confirmation propre + libellé) ; Aniimo (data officielle 51 créatures + codes) ; GTA 6 (Newswire).
- **À publier** : rien de neuf.
- **À mettre à jour** : FC 27 Team 2 ; monitors 2ᵉ source (blade-ball SORRY4DELAY/LIVEEVENTS, 100days RIVAL, Fisch ChapelTroubles, AV 2ndAnniDay7, GAG torigate) ; brainrot-evolution ; Blue Lock Rivals (reward SPOOKY) ; listes gonflées (preuve d'expiration).
- **À préparer / décision Peter** : libellé FC 26/FC 27 ; bloc « Jeu de la semaine » (marqueurs absents — bloqué) ; feed prix cartes FC 27 ; /avatar/ (NE PAS MODIFIER).
- **Prochain run (15h/22h 31/10 ; 05h 01/11)** : **retrait sections Halloween au 05h 01/11** (sauf FischFright2026 ≤ 09/11) ; FC 27 Team 2 ; Aniimo data ; GTA 6 Newswire ; backlog rotation (31 jamais vérifiées).

## QC
- **Fichiers modifiés (9)** : codes-blade-ball.html, codes-king-legacy.html, codes-pet-simulator-99.html, codes-100-days-at-sea.html + régénérés data/codes.json, data/games-index.json, sitemap.xml, sitemap-games.xml, tools/code-watch.json. (+ tools/editorial-intelligence.json, EDITORIAL-QUEUE.md, ce rapport.)
- **Tests** : `node --check js/main.js` **OK** ; déséquilibre `<div>` site entier (hors /avatar/) = **0** ; **0 null byte** sur les 4 pages touchées ; toutes finissent par `</html>` ; `data/codes.json` (199 jeux, 1339 codes), `data/games-index.json`, `tools/code-watch.json`, `tools/editorial-intelligence.json` (70 topics) **valides** ; `sitemap.xml` XML valide (421 URLs, se termine par `</urlset>`) ; GA4 (`G-FEL71QVHNL`) + nav + `data-cta="guidelink"` **unique** présents sur les 4 pages codes.
- **Cache JS** : `js/main.js` **non modifié** → pas de bump. Les pages `codes-<slug>.html` sont autonomes (pas de référence `main.js` — normal). Les hubs restent `main.js?v=48` (188 pages) ; 3 pages `/avatar/` en `v=43` (hors périmètre, inchangé).
- **Build** : `build_site` → `build_home` → `build_codes_json` → `build_sitemap` (ordre §29 respecté).
- **Erreurs corrigées** : aucune corruption (édition des pages codes via Python avec assertions de correspondance exacte, conformément à CLAUDE.md).

---

**Pour publier** : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)

---

# SESSION INTERACTIVE (après le run 05h) — « la totale » sur 2 jeux (demande de Peter)

Peter a demandé **la totale** (codes + guide + tier list, dans le ton du site) sur deux jeux Roblox qui montent, confirmés très populaires via l'API Roblox :

- **Throw Food For Animals** (Goofy Chupacabra) — **129 695 joueurs simultanés, 19,3 M de visites**. universeId 10766972131.
- **Steal A Pet And Ride It** (Snail Riders) — **44 538 joueurs simultanés, 11,6 M de visites**. universeId 10769315427.

### Décisions clés (exactitude > fraîcheur)
- **Aucun des deux jeux n'a de système de codes** (vérifié : gamewave 28/10 pour Throw Food ; aucune source propre pour Steal A Pet, à ne pas confondre avec « Ride a Pet »/« Steal a Ride »). → Les 2 **pages codes sont honnêtes** (« aucun code confirmé ») — ce qui est aussi la bonne réponse SEO pour « codes <jeu> ». Jamais de code inventé.
- **Tier lists = priorités de progression** (choix validé par Peter) : classement des systèmes du jeu basé **uniquement sur la description officielle**, pas de stats d'items inventées (même modèle que la tier list 1-anime-eyes).
- **Vraies miniatures** `tr.rbxcdn.com` (API officielle), jamais de SVG en src.

### Livré (6 pages + intégrations)
- `codes-throw-food-for-animals.html`, `guides/throw-food-for-animals.html`, `tier-list/throw-food-for-animals.html`
- `codes-steal-a-pet-and-ride-it.html`, `guides/steal-a-pet-and-ride-it.html`, `tier-list/steal-a-pet-and-ride-it.html`
- Intégrations : `const GAMES` (index.html), `ROBLOX_THUMBS` + `ROBLOX_UNIVERSE_IDS` (js/main.js), cartes sur `tous-les-codes.html` / `guides.html` / `tier-lists.html`, **+6 URLs au sitemap**, cross-links codes↔guide↔tier, bandeau CTA `data-cta="guidelink"` unique sur les pages codes.
- **Cache bump `main.js?v=48` → `v=49`** sur 192 pages (main.js modifié). /avatar/ laissé en v=43 (hors périmètre).
- Régénération : build_site → build_home → build_codes_json (201 jeux) → build_sitemap (427 URLs).

### QC
0 déséquilibre `<div>` (hors /avatar/) ; 0 null byte ; les 6 pages finissent par `</html>` ; GA4 présent ; CTA `guidelink` unique sur les pages codes ; `node --check js/main.js` OK ; `data/codes.json` + `data/games-index.json` valides (2 jeux présents, 0 code) ; `sitemap.xml` XML valide (`</urlset>`) ; 0 page en `v=48` hors /avatar/.

### Reste (non bloquant)
- **Épingles Pinterest** des 2 jeux (génération cloud) : voir ci-dessous / à générer.
- Tier lists d'items détaillées : à créer **quand** des données communautaires fiables (2 sources) existeront.
