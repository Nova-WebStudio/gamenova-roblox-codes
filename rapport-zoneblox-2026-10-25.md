# 🗞️ RAPPORT ZONEBLOX — 2026-10-25 (RUN 05h, dimanche)

> Run complet « FULL MAINTENANCE + EDITORIAL ». Pas de *Jeu de la semaine* (lundi uniquement, §30).
> Principe appliqué : **EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ TOPIQUE > SEO > QUANTITÉ.**
> **Résultat net : 2 pages codes mises à jour (content gaps comblés, +3 codes au total), 8 hot games vérifiés, 6 stubs traités, fraîcheur rafraîchie sur 16 pages.** Toutes les additions sont multi-sources ; aucune invention ; kill switch maintenu sur tous les conflits.

---

## CODES

Priorité absolue (§2). Baseline extraite des pages, comparée aux sources (fenêtre 12-24 h, règle 3 sources indépendantes **ou** 1 officielle). **2 contenus réellement modifiés, 2 sources minimum chacun.**

### ✅ Codes ajoutés (content gaps comblés)
- **sell-fries** : 0 → **1 code** — `Halloween` (🎃 100 Candies, événement Halloween). **3 sources** concordantes : ProGameGuides (24/10), Dexerto (21/10), games.gg (21/10) — même récompense. Les 4 autres codes listés par ProGameGuides seul (`4000Members`, `FreeCandy`, `CoolCode`, `3000members`) sont restés **mono-source → non publiés** (MONITOR).
- **tap-simulator-reborn** : 0 → **2 codes** — `BOO!` (🎃 1 Potion de Chance I + 100 Candy Corn) et `SPOOKY` (🎃 Potion Chance II + Pièces II + Gemmes I + 250 Candy Corn). **2 sources** : Dexerto (20/10, « 1ʳᵉ fournée de codes du jeu »), games.gg (21/10). ⚠️ **Casse de SPOOKY ambiguë** (Dexerto minuscule / games.gg majuscules) → **majuscules retenues** (games.gg explicite + style `BOO!` + jeu souvent case-insensitive) ; à reconfirmer.
- Les deux pages affirmaient « aucun code / tout code annoncé est faux » : **récit inversé proprement** (hero pill, intro SEO, panneaux Statut/Faux codes/À-propos, FAQ **visible + JSON-LD**, ItemList ZB-SEO-LD `dateModified`=25/10). Synchro complète des 3 sources de données + widget : page HTML, `const GAMES` (index.html), cartes `tous-les-codes.html`, `data/codes.json`, `sitemap.xml`.

### ✅ Hot games confirmés inchangés / MONITOR (verifDate 25/10)
- **blox-fruits** — Dexerto (19/10) « no new codes found » → inchangé (23 codes).
- **blue-lock-rivals** — Dexerto (18/10) liste exactement les **4 codes de la page** (NELAIKU, HALLOWEEN, WSNAKE, SORRYFORDELAYAIKU). `SPOOKY`/`SKELETON`/`AIKUCHANGES` apparaissent chez Roonby seul (non marqués actifs) → **MONITOR, non ajoutés**.
- **volleyball-legends** — Samlover (13/10) = **3 codes identiques** (UPDATE_91, REPLAYS, MVP) ; UPDATE_90/SKELETON_BUNDLE/JINX/SLOT_REWORK marqués expirés 10/10 (déjà absents) → inchangé.
- **anime-vanguards** — 14 codes 2ᵉ anniversaire (Roonby 13/10, même liste) ; aucune **preuve d'expiration** → maintien (§4).
- **fisch** — Roonby (24/10) liste `ChapelTroubles (NEW)` mais **source unique** + page auto-contradictoire ; pcgamesn stale (Nov 2025) → **MONITOR**, page inchangée (4 codes).
- **grow-a-garden** (RDCAward/BEANORLEAVE10 — « FREESEED » concerne grow-a-garden-2, hors sujet), **king-legacy** (DigitalCitizen = 9 codes concordants), **blade-ball** → inchangés.

### 🛑 Kill switch / listes gonflées non prunables (§4)
- grimoires-era (conflit 3 voies), rivals (décalage version), anime-battle-rng (~35, sources syndiquées), attack-on-titan-revolution (21, Dexerto ne confirme que 2 actifs). **Aucune suppression sans preuve d'expiration.**

### Rotation (lot 05h, rattrapage)
- **Confirmés SANS code** : ride-a-dino (Roonby 20/10 « pas de menu de codes »), my-gaming-cafe & steal-from-the-rich (aucune source dédiée — jeux distincts des homonymes), chop-a-forest (Roonby 15/10 « any active codes ? » = aucun).
- **Identité ambiguë → à revérifier (placeId requis)** : `button-rng-2` (robloxden liste 8 codes pour un « Button RNG 2 »), `chicken-farm` (Dexerto/Insider listent un « Chicken Farm »). Nos pages = « aucun code ». **Non éditées** faute de confirmation d'identité (prudence > exhaustivité).
- `catalogVerify` rafraîchi au 25/10 sur **16 pages**.

---

## SEO

- **UPDATE-before-CREATE respecté** : aucune nouvelle URL ; les 2 ajouts sont des **mises à jour** de pages existantes vides.
- **Fraîcheur (§4, avantage décisif)** : `verifDate` rafraîchie sur 16 pages vérifiées + `const GAMES.date` au 25/10 (hot games + 2 gaps) → homepage « Jeux du moment / Codes » et `sitemap.lastmod` (195 URLs datées via verifDate) à jour.
- **Données structurées** : `ItemList` ZB-SEO-LD ajoutée aux 2 pages comblées, `dateModified`=25/10, FAQPage JSON-LD resynchronisée.
- **Maillage** : liens internes/CTA des 2 pages préservés (guide débutant lié).
- **Anti-cannibalisation** : OK (long-tail « codes <jeu> » faible difficulté, pages auparavant vides).

## NOUVEAUX JEUX

- **Aucun ajout de jeu.** Les 2 pages déjà existantes (sell-fries, tap-simulator-reborn) ont été **comblées**, pas créées. Mode conquête (§15) non déclenché : **Steal an Egg** reste viral (page existante) et **Brookhaven** (RP, pas de codes) dominent la tendance — aucun entrant nécessitant une page immédiate.

## CONTENU

- Guides : 0. Tier lists : 0 (aucune évolution réelle, §23). Articles : 0.
- Mises à jour de codes : **2 pages** (sell-fries, tap-simulator-reborn). Règle « 2 excellents > 20 faibles » respectée.

## ANIIMO

- **« Season 1 Part II » confirmé pour le 29/10.** Couverture détaillée côté médias (playnews) mais **spécifics encore spéculatifs**. **Aucune édition** (data-driven : `data/aniimo/` → `build_site.py`, jamais d'édition directe sous `/games/`). Action : **préparer** l'ingestion du contenu officiel du 29/10, sans rien inventer d'ici là.
- Conflit codes `aniimazingfroyo` (khelnow 04/10 actif vs mein-mmo 09/10 expiré) toujours non tranché → inchangé.

## GTA 6

- **Préchargement 12/11** + **sortie 19/11/2026** toujours confirmés (DigitalCitizen). Rien de **nouveau confirmé** sur le Newswire au 25/10 (pas d'heure de préchargement ni de détails day-one). Evergreen **inchangé**. Séparation CONFIRMÉ / RAPPORTÉ / RUMEUR maintenue.

## FC 27

- Titre **live côté EA = FC 26** (promos actives : TOTY Edition, Cornerstones ; calendrier de promos en cours). Vertical du site nommé `fc-27`. **Décision naming (FC 27 vs FC 26) toujours en attente de Peter** → couverture Ultimate Team bloquée. Aucune modification structurelle autonome.

## EDITORIAL INTELLIGENCE

- **Top opportunités** : (1) **sell-fries** & **tap-simulator-reborn** → PUBLIÉS ce run ; (2) Aniimo S1 Part II 29/10 ; (3) grimoires-era (si source officielle) ; (4) rivals (si source fraîche actif).
- **Tendances** : Halloween Roblox actif (codes saisonniers BOO!/SPOOKY/Halloween), Steal an Egg viral, Aniimo en montée (patch rapide).
- **Articles créés** : 0. **Pages codes mises à jour** : 2. **Pages re-datées** : 16.
- **Sujets ignorés** (bar non atteint) : codes mono-source (sell-fries ×4, fisch ChapelTroubles, blue-lock SPOOKY/SKELETON/AIKUCHANGES, anime-vanguards extras).
- **À surveiller** : button-rng-2 & chicken-farm (identité), SPOOKY (casse), grimoires-era, rivals, anime-battle-rng, aotr, GTA 6 Newswire, FC 26 naming.
- `tools/editorial-intelligence.json` : +3 sujets (sell-fries-halloween, tap-simulator-reborn-halloween, run-2026-10-25-05h), meta rafraîchie, aniimo re-daté. **60 sujets au total.**

## EDITORIAL QUEUE

- **Urgents** : GTA 6 (watch Newswire).
- **À publier** : rien de nouveau (2 gaps publiés ce run).
- **À mettre à jour** : SPOOKY (casse), sell-fries (4 codes mono-source), grimoires-era, rivals, anime-battle-rng, aotr, type-soul, 8 pages vides.
- **À préparer** : Aniimo 29/10 ; décisions Peter (FC 26 naming, marqueurs Jeu de la semaine, listes gonflées).
- **Demain** : Aniimo 29/10 ; reconfirmer SPOOKY + 2ᵉ source sell-fries ; désambiguïser button-rng-2 & chicken-farm (placeId).

## QC

- Fichiers édités : `codes-sell-fries.html`, `codes-tap-simulator-reborn.html` (+ 14 `verifDate`), `index.html` (const GAMES + sections), `tous-les-codes.html` (2 cartes), `data/codes.json`, `sitemap.xml`, `tools/code-watch.json`, `tools/editorial-intelligence.json`, `EDITORIAL-QUEUE.md`.
- Tests : **0 null byte**, **div équilibrés sur tout le site (0 imbalance)**, toutes pages finissent par `</html>`, **tous les JSON-LD valides**, `data/codes.json` valide (196 jeux, 1320 codes), `sitemap.xml` valide (411 URLs, finit par `</urlset>`), GA4 (`G-FEL71QVHNL`) présent, cache JS cohérent (181× v47 hors `/avatar/`).
- Régénération dans l'ordre (§29) : `build_codes_json` → `build_home` → `build_sitemap`. `build_site` non lancé (aucune donnée data-driven `/games/` modifiée).
- Erreurs corrigées en cours de run : bug d'échappement `\'` dans un 1ᵉʳ script (JSON-LD invalide) → page restaurée depuis git et ré-éditée via regex à wildcards (0 transcription de texte source). `git checkout` impossible (suppression non autorisée dans le dossier) → restauration par `git show HEAD:… > …`.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
