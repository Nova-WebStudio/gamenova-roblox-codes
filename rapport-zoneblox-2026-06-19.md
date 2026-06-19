# Rapport Zoneblox — 19 juin 2026 (vendredi)

## Résumé

Run de maintenance ciblé : surveillance des sources de codes (26 jeux chauds via l'API Roblox), publication de 2 nouveaux codes confirmés, et remédiation du « thin content » sur 6 pages pour sécuriser l'indexation. Vendredi → pas de mise à jour « Jeu de la semaine » (réservée au lundi).

## Étape 0 — Surveillance des sources de codes

Les 26 jeux de `hotGames` ont été vérifiés en une requête multiget sur l'API officielle Roblox (`games.roblox.com/v1/games`), descriptions in-game lues via le navigateur (le shell n'a pas de réseau).

**2 nouveaux codes détectés dans les descriptions in-game officielles, confirmés par une 2ᵉ source fiable, puis publiés :**

| Jeu | Code | Récompense | Sources |
|-----|------|-----------|---------|
| BlockSpin | `W7C28D` | 500 cash (nouveaux joueurs, une seule fois — code de parrainage officiel) | Description in-game + Pocket Tactics / Dexerto |
| Squid Game X | `$1M$` | Coins | Description in-game + Pocket Gamer / RobloxDen |

**Candidats en attente (1 seule source — NON publiés) :** pour Squid Game X, des agrégateurs mentionnent aussi `RISKYPLAY`, `REWARDTIME`, `RAININGCASH`, `$500K$`, `$250K$`, `$100K$`. Faute de 2ᵉ source fiable ou de confirmation in-game, ils restent en attente et seront vérifiés au prochain run.

Les codes mentionnés en description sur les autres jeux (`YOO1M110K` pour Fruit Battlegrounds, `BOOM` pour Merge a Nuke) sont **déjà connus et publiés** — aucune nouveauté. Tous les autres descriptifs et shouts sont inchangés depuis le snapshot de la veille.

`tools/code-watch.json` : `lastChecked` mis à jour pour les 26 jeux (2026-06-19), `knownCodes` enrichis pour BlockSpin (+`W7C28D`) et Squid Game X (+`$1M$`), `descExcerpt` rafraîchis. JSON revérifié valide (se termine par `}`, 26 snapshots).

**Note catalogue :** Anime Last Stand n'affiche plus que ~220 joueurs simultanés (sous le seuil de 4000) — à surveiller, mais reste un classique conservé.

## Étapes 2-3 — Contenu minimum (anti thin-content)

Les 6 pages codes au plus faible volume rédactionnel ont été étoffées avec du contenu français honnête et utile (gameplay, progression, rôle réel des codes, multijoueur, événements). Aucun remplissage creux ; aucun code inventé.

| Page | Mots (corps, après) | Ajout |
|------|--------------------:|-------|
| `codes/tower-of-hell.html` | 1381 | Paragraphe « régénération aléatoire / VIP cosmétique / codes équitables » |
| `codes/toilet-tower-defense.html` | 1392 | Paragraphe « coop / événements / reroll de traits / économie » |
| `codes/brookhaven.html` | 1378 | Paragraphe « mises à jour / gamepasses vs codes / honnêteté » |
| `codes/twenty-one.html` | 1379 | Paragraphe « multijoueur / coordination / rôle du Cash » |
| `codes/fire-force-online.html` | 1412 | Paragraphe « démarrage / rerolls / le hasard reste le hasard » |
| `codes/slime-rng.html` | 1450 | 2 paragraphes « cumul de luck / événements / codes = accélérateurs » |

Les 8 pages éditées contiennent toutes ≥1200 mots, GA4, nav avec lien `/avatar/`, et un descriptif de jeu développé.

### Pages codes encore < ~1300 mots (corps) à étoffer aux prochains runs
fire-force-online désormais OK ; restent notamment : `anime-vanguards`, `blade-ball`, `liminalite-invisible`, `anime-rangers-x`, `spin-a-brainrot`, `cliqueur-phonk`, `anime-reversal`, `grow-a-garden-2`, `grand-piece-online`, `skibidi-masters-tower-defense`, `peroxide`, `untitled-tag-game`, `anime-reborn` (max 6/run).

## Étape 8 — QC intégrité

- `GAMES_INDEX` (153) ↔ `ALL_GAMES` (153) : **synchronisés**, aucun écart.
- `node --check js/main.js` : **OK** (fichier non modifié, donc pas de bump de cache).
- Cache JS : **uniforme `main.js?v=24`** sur 257 fichiers HTML.
- Équilibre des `<div>` et octets nuls : **0 problème** sur l'ensemble du site.
- Les 8 fichiers édités vérifiés un à un via l'outil de lecture fichier (état faisant autorité = machine de Peter) : **tous complets, se terminant par `</html>`**, paragraphes bien insérés.
- `tools/code-watch.json` : valide, 26 snapshots.

### ⚠️ Note technique (artefact du bac à sable, pas un vrai problème)
Comme la veille, le **mount bash du sandbox sert une lecture tronquée** des fichiers réécrits par les outils fichiers : `git diff` (exécuté dans le sandbox) affiche donc de fausses « suppressions » de fin de fichier, et signale même `rapport-zoneblox-2026-06-18.md` comme « modifié » alors qu'il ne l'est pas. Recoupé via l'outil de lecture : **rapport-18 est intact (se termine bien par l'instruction de publication), et les 8 pages éditées se terminent bien par `</html>`**. Le `git` natif de Peter (Windows) lit les vrais fichiers : le commit sera correct. Les écritures bash (`code-watch.json`) se propagent normalement.

## Non traité ce run
Ajout de 6 jeux (Étape 1), nouvelles tier lists (Étape 4), guides complets (Étape 5), UGC (Étape 6) : non abordés ce run, centré sur surveillance des codes + indexation + QC. 10 jeux ayant été ajoutés la veille, le catalogue est récent.

## Ajout d'un jeu (« la totale ») — 100 Days at Sea / 100 jours en mer

Jeu de survie en monde ouvert de **Stranded Devs** (placeId 70411440483149, universeId 9167377564, groupId 425035678), **~41 800 joueurs simultanés** (largement éligible), absent du catalogue. Page complète créée : `codes/100-days-at-sea.html`, **1997 mots** de rédactionnel FR, miniature réelle `tr.rbxcdn.com`, 2 vidéos YouTube vérifiées via oEmbed (CHALLS « Tips & Tricks » `BjXm4F1E9UA` ; Ricoko « NOOB to PRO » `gB_iMCdUkus`), 6 astuces, FAQ (4 questions), section À propos + guide des classes (Sailor, Survivor, Medic, Crewmate, Camper, Adventurer, Knight, Millionaire) + 3 jeux similaires (99 Nights in the Forest, Dead Rails, Squid Game X), bandeau CTA, GA4, nav 7 entrées.

**⚠️ Codes — décision d'honnêteté :** la description in-game ne contient **aucun code**, et aucune source fiable ne confirme de codes. Les seules « listes » qui circulent (ex. Lawod : RAFTBOOST, HARPOONX, OCEANLIFE…) ne sont corroborées par aucune source sérieuse et ont tout du remplissage SEO inventé. **Aucun code n'a donc été publié** : la page affiche honnêtement « Pas de code officiel confirmé », explique la méthode de saisie et où les vrais codes apparaîtront. Dès qu'un code sera confirmé (2 sources), il sera ajouté.

**Intégrations réalisées :** carte sur `index.html` (1ʳᵉ position « Nouveaux jeux »), `ALL_GAMES` + `THUMBS` (codes/index.html), `GAMES_INDEX` + `ROBLOX_THUMBS` + `ROBLOX_UNIVERSE_IDS` (js/main.js), SVG de fallback `images/games/100-days-at-sea.svg`, `<url>` au sitemap, `hotGames` + snapshot de référence (code-watch.json, premier run → aucun signalement). Synchro vérifiée : **GAMES_INDEX 154 = ALL_GAMES 154**, aucun écart.

**Cache JS :** js/main.js modifié → version bumpée **v=24 → v=25** dans les **257 fichiers HTML** (procédure ÉTAPE 9). Vérification : aucun fichier versionné physique sur le serveur (query-string pur sur `/js/main.js`, confirmé via `.htaccess`), le bump est donc sans risque. Les fichiers édités via l'outil ont été bumpés un par un via l'outil (écriture disque réelle), les 253 autres via un script Python avec garde-fou anti-troncature ; aucun fichier corrompu.

## Guide complet (ÉTAPE 5) — guides/100-days-at-sea.html

Guide complet FR créé sur le gabarit `guides/blox-fruits.html` : **1678 mots**, sommaire ancré (TOC, 10 sections), image hero réelle `tr.rbxcdn.com`, contenu **vérifié sur 2 sources** (Sportskeeda + Lawod/Deltia's). Sections : guide débutant, survivre les 100 jours, le harpon & la récolte, construire/fortifier le radeau, économie Pearls & Doubloons, **tableau des 8 classes** (Sailor → Knight, Millionaire) + quelle débloquer en priorité, **tableau des 9 compagnons** (Frog, Turtle, Crab, Dolphin, Shark, Crow, Lava Snail, Salamander, Magma Golem) avec effets, explorer les îles & armes, survivre aux vagues d'ennemis, FAQ (5 questions). JSON-LD Article + Breadcrumb + FAQPage valides.

**Liaisons (codes ↔ guide) :** carte ajoutée en tête de `guides/index.html` (+ `ItemList` JSON-LD position 30), `<url>` au sitemap, **bouton « 📚 Guide complet » ajouté dans le hero** de `codes/100-days-at-sea.html`, et **bandeau CTA `data-cta="guidelink"` mis à jour** pour pointer vers le guide dédié (« Progresse plus vite à 100 Days at Sea » → /guides/100-days-at-sea.html). Liens internes tous vérifiés existants ; pages se terminant bien par `</html>` / `</urlset>` (recoupé via l'outil de lecture, les lectures bash étant tronquées sur les fichiers édités).

## Tier list (ÉTAPE 4) — tier-list/100-days-at-sea.html

Tier list créée sur le gabarit `tier-list/grow-a-garden.html`, contenu **vérifié sur 2 sources** (Sportskeeda + Deltia's/Lawod) : **deux classements** indicatifs (méta juin 2026) avec chips S/A/B/C —
- **Classes** : S = Knight, Millionaire, Adventurer ; A = Medic, Survivor ; B = Camper, Crewmate ; C = Sailor.
- **Compagnons** : S = Salamander, Magma Golem ; A = Crow, Shark, Dolphin ; B = Lava Snail, Crab ; C = Frog, Turtle.

JSON-LD ItemList + Breadcrumb valides, date affichée (19 juin 2026), boutons hero vers codes + guide.

**Liaisons :** carte ajoutée en tête du hub `tier-list/index.html` (**vraie miniature `tr.rbxcdn.com`, jamais d'emoji**) + `ItemList` position 51 ; `<li>` ajouté sur l'accueil (section « Toutes les tier lists ») ; `<url>` au sitemap ; **boutons croisés** mis à jour : la page codes et le guide pointent désormais vers la **tier list dédiée** (et non plus le hub). Les 3 pages (codes ↔ tier list ↔ guide) sont entièrement reliées entre elles.

## Habitude enregistrée — « la totale »

À la demande de Peter, ajout d'une section en tête de `CLAUDE.md` : **« la totale » sur un jeu = page codes + tier list + guide**, complètes et reliées, avec toutes les intégrations (accueil, hubs, sitemap, sources de données, liens croisés). Les prochains runs s'y conformeront automatiquement.

## Fichiers touchés
- `tools/code-watch.json` (lastChecked 26 jeux + 2 nouveaux codes + ajout 100-days-at-sea)
- `tier-list/100-days-at-sea.html` (nouveau) + `tier-list/index.html` (carte + ItemList)
- `CLAUDE.md` (définition de « la totale »)
- `codes/100-days-at-sea.html` (nouveau, 1997 mots) + `images/games/100-days-at-sea.svg` (nouveau)
- `guides/100-days-at-sea.html` (nouveau, guide complet 1678 mots)
- `index.html`, `codes/index.html`, `js/main.js`, `sitemap.xml`, `guides/index.html` (intégration jeu + guide)
- `codes/100-days-at-sea.html` (bouton hero + bandeau CTA vers le guide)
- **Tous les .html** : bump cache `v=24 → v=25`
- `codes/blockspin.html` (+code `W7C28D`, date, FAQ)
- `codes/squid-game-x.html` (+code `$1M$`, date)
- `codes/tower-of-hell.html`, `codes/toilet-tower-defense.html`, `codes/brookhaven.html`, `codes/twenty-one.html`, `codes/fire-force-online.html`, `codes/slime-rng.html` (étoffement)
- `rapport-zoneblox-2026-06-19.md` (ce rapport)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
