# Rapport Zoneblox — dimanche 21 juin 2026

Run de maintenance automatique. Dimanche (`date +%u` = 7) → **pas de « Jeu de la semaine »** (réservé au lundi).

## Étape 0 — Surveillance des sources de codes

Lecture de `tools/code-watch.json` (27 jeux suivis). Pour les jeux les plus actifs, récupération via l'API Roblox (Chrome) :
- **Descriptions in-game** des 27 universes (1 appel groupé `games.roblox.com/v1/games`).
- **Shouts de groupe** des 6 jeux à plus forte vélocité (Grow a Garden, Steal a Brainrot, Blade Ball, Blue Lock Rivals, Volleyball Legends, Fruit Battlegrounds) → tous `shout: null`.

**Résultat : aucun nouveau code candidat détecté.** Les codes présents dans les descriptions (`YOO1M110K`, `BOOM`, `W7C28D`, `$1M$`) figurent déjà dans les snapshots. Snapshots rafraîchis (`lastChecked` → 2026-06-21). JSON revérifié valide (se termine par `}`, 27 snapshots).

## Étape 2/3 — Vérification des codes (2 sources)

### Blue Lock Rivals — MISE À JOUR (page très consultée, codes obsolètes)

Deux sources fraîches et concordantes :
- **Beebom** (maj 20 juin 2026) : 3 codes actifs.
- **Bloxodes** (vérifié « aujourd'hui » 21 juin 2026) : 7 actifs.

Intersection confirmée par **2 sources** : `NELEVENT`, `NEL2.0`, `MASSIVEUPDATE`. Les deux sources s'accordent pour classer **expirés** tous les anciens codes de notre page (SNOWFLAKE, HIORIREWORK, MASTEROFALLTRADES, OTOYAUPD, CHARLESTIME, TONGUESOUT, etc.). Les codes du 13 juin (KIYORARELEASE, BREAKDANCE, NELTEAMSHYPE, NELHIORI) sont **en litige** (actifs chez Bloxodes, expirés chez Beebom) → par prudence (règle « 2 sources »), non conservés comme actifs.

`codes/blue-lock-rivals.html` mis à jour :
- Tableau des codes : 29 → **3 codes actifs** (`NELEVENT`, `NEL2.0`, `MASSIVEUPDATE`), badges « NOUVEAU ».
- Compteurs « codes actifs » synchronisés (badge hero, bannière live, **3 codes**) ; dates « Mis à jour le » / « Vérifié le » → **21 juin 2026** ; `dateModified` JSON-LD → 2026-06-21.
- Paragraphes intro + « À propos » corrigés (références aux anciens codes remplacées).
- Snapshot `code-watch.json` synchronisé (`knownCodes` BLR = les 3 actifs).

Contenu vérifié : la page conserve son rédactionnel FR complet (intro hero, 6 astuces, FAQ 7 questions, « À propos » 4 paragraphes) → bien **> 1200 mots** ; retirer des lignes de codes (tokens + libellés EN) n'affecte pas le volume éditorial français.

### Volleyball Legends — NON modifié (corroboration insuffisante)

Notre page : `UPDATE_73`, `JUNGLE_MAP`, `JUNE_2026`. Une recherche évoque `UPDATE_74` / `SEASON_16` / `SUMMER_UPDATE` (15 juin), mais la seule source vérifiable directement (Bloxodes) est **périmée** (16 mai, `UPDATE_70`). Faute de 2e source fraîche concordante, **pas de modification** (notre page est déjà plus récente que la source vérifiable). À revérifier au prochain run.

### Blade Ball — NON modifié

Pocket Tactics (10 mai) est plus ancien que notre page. Aucun changement justifié.

## Étapes 1, 4, 5, 6 — Ajouts / tier lists / guides / UGC

Pas d'ajout ce run. Priorité donnée à une mise à jour de codes **bien sourcée** plutôt qu'à des ajouts en masse, l'environnement sandbox servant des lectures bash/git **tronquées** (voir note) qui rendent les grosses écritures HTML risquées à vérifier.

## Étape 7 — Jeu de la semaine

Dimanche → **non touché** (réservé au lundi). Conforme.

## Étape 8 — QC

Fichiers réellement modifiés ce run : `codes/blue-lock-rivals.html`, `tools/code-watch.json`.
- `blue-lock-rivals.html` (via l'outil fichier, fiable) : se termine par `</html>`, `main.js?v=26`, GA4 `G-FEL71QVHNL` présent, nav avec lien `/avatar/`, **1 seul** `data-cta="guidelink"`, structure des `<div>` préservée (remplacement de lignes `<tr>` équilibrées uniquement). Aucune référence prose résiduelle à « 29 codes ».
- `code-watch.json` (via l'outil fichier) : JSON valide, 27 snapshots, se termine par `}`.

### ⚠️ Note environnement (importante)
Le **mount bash/git du sandbox sert des lectures tronquées** : `git diff`, `node --check`, `tail`, `wc` voient tous les fichiers volumineux coupés en plein contenu (ex. `js/main.js` « tronqué » à la ligne 705, `sitemap.xml` « coupé »…). Vérification croisée via **l'outil fichier (Read)**, qui lit les vrais fichiers Windows : `js/main.js` est **complet** (ferme bien `renderNewGames()` et finit le script), `sitemap.xml` est **complet** (300+ URLs, `</urlset>`), `blue-lock-rivals.html` complet (`</html>` l. 209), `code-watch.json` complet. **Ce n'est donc PAS une corruption disque** : Peter committe depuis Windows sur les vrais fichiers (intacts), pas sur la vue tronquée du sandbox. `js/main.js` non modifié par ce run → pas de bump de cache nécessaire (Étape 9 sans objet).

### Changements pré-existants dans l'arbre de travail
`git status` liste ~60 fichiers modifiés **non committés** (issus des runs précédents : « la totale » Anime Fighting Simulator, guides SEO des tier lists, `index.html`, `sitemap.xml`, `my-gaming-cafe.html`, etc.). Le spot-check via l'outil fichier (sitemap complet) indique qu'ils sont intègres. Ils seront inclus au prochain commit.

## Fichiers touchés ce run
- `codes/blue-lock-rivals.html` — codes actualisés (29 → 3, 2 sources), dates, compteurs, prose.
- `tools/code-watch.json` — `lastChecked` rafraîchis ; `knownCodes` BLR synchronisés.
- `rapport-zoneblox-2026-06-21.md` — ce rapport.

## À suivre au prochain run
- **Volleyball Legends** : confirmer `UPDATE_74`/`SEASON_16`/`SUMMER_UPDATE` avec une 2e source fraîche, puis mettre à jour si validé.
- Re-vérifier les jeux à forte vélocité (Blade Ball, Grow a Garden, Steal a Brainrot) dont les sources tierces étaient encore périmées aujourd'hui.

## Pour publier
Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
