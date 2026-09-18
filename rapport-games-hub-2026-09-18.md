# /GAMES/ REDESIGN COMPLETED — Hub de découverte gaming — 18 septembre 2026

`/games/` passe d'une **liste de jeux** à un **hub de découverte** où chaque jeu communique son **écosystème de contenu**. Page **générée** par `tools/build_site.py` (data-driven), donc un futur GTA 6 s'ajoutera par la donnée. H1 unique, URLs Roblox préservées.

### UX
La page répond désormais aux 3 questions clés : quels jeux Zoneblox couvre, lesquels sont mis en avant, et **ce qu'on trouve pour chaque jeu**. Structure : Hero (H1) → **🔥 À découvrir** (featured) → **🎮 Le catalogue complet** (recherche + filtres + tri + 174 cartes).

### Visual design
Section « À découvrir » avec **2 grandes cartes écosystème** (Roblox, Aniimo) : visuel dominant, badge, plateforme·genre, **types de contenu**, CTA « Explorer → ». Catalogue en grille responsive de cartes compactes. Hover subtil (remontée + bordure). Aucune fausse popularité : la sélection est éditoriale (« Sélection Zoneblox »).

### Game discovery
- **Featured** : Roblox (plateforme, 173 jeux, Codes·Guides·Tier lists) + Aniimo (NOUVEAU, RPG · PC/Console/Mobile, Codes + « Guides/Créatures · bientôt »).
- **Catalogue complet** : 174 jeux (173 Roblox + Aniimo), chaque carte affichant ses **vrais types de contenu**.

### Search
Recherche instantanée par nom (client-side sur les cartes bakées) : « blox » → Blox Fruits, « ani » → Aniimo. Placeholder « Blox Fruits, Aniimo, GTA 6… ». Prête pour de futurs jeux (data-driven).

### Filters
Filtres **data-driven** (uniquement les valeurs présentes) : Plateforme (Roblox / PC · Console / Mobile) + Genre (Simulateur, Anime, Combat, RPG, Tycoon, Tower Defense, Sport, Obby, Horreur) + Tri (Récemment mis à jour / A → Z). 100 % client-side, **sans paramètre d'URL** → aucune URL de filtre indexable en double.

### Game cards
Chaque carte = **écosystème** : miniature, nom, plateforme · genre, **badges de types de contenu réellement présents**, CTA. La liste des types est calculée à la génération (existence des fichiers) : 92 jeux → « Codes » seul, 48 → « Codes · Guides · Tier list », 18 → « Codes · Tier list », 16 → « Codes · Guides ». **Jamais de type vide affiché.** Aniimo montre ses types disponibles + « bientôt » pour les autres.

### Roblox
**Préservé intégralement.** Les 173 jeux Roblox pointent vers leurs **pages existantes** `codes-<slug>.html` (0 URL déplacée, 0 redirection créée). Roblox est aussi la carte featured principale (plateforme, 173 jeux).

### Aniimo
Jeu de première classe : carte featured (grande, NOUVEAU, écosystème + CTA « Explorer Aniimo »), présent dans le catalogue, recherchable et filtrable (RPG, PC/Console/Mobile). Lien vers le hub `/games/aniimo/`.

### Data architecture
Aucun changement de modèle : `data/games/*.json` (standalone) + les 173 jeux Roblox lus depuis `index.html` → fusionnés par le générateur en `data/games-index.json`. Les types de contenu sont dérivés de l'existence réelle des fichiers (`guides/`, `tier-list/`). **Zéro logique par jeu en dur** ; tout est piloté par la donnée.

### SEO preserved/improved
- **H1 unique** « Tous les jeux » ; `<title>` « Jeux vidéo : codes, guides, tier lists & actualités | Zoneblox » ; `canonical` /games/.
- `BreadcrumbList` + `ItemList` (174 jeux) valides ; aucune fausse note/avis/popularité.
- `sitemap.xml` (335) et `sitemap-games.xml` intacts ; **aucune URL Roblox cassée**.

### Files changed
- `tools/build_site.py` : `build_directory()` enrichie (types de contenu data-driven, section featured « À découvrir »).
- `css/platform.css` : styles `.featured-grid` / `.fcard`.
- `games/index.html` : **régénéré**.

### Tests
- **1 seul H1** ; `<div>` équilibrés (0) ; fin `</html>` ; **0 null byte** (site entier).
- 174 cartes + 2 featured ; recherche/filtres/tri présents et câblés sur les bons IDs ; 173 miniatures en `loading="lazy"` ; canonical correct ; JSON-LD valides.
- Types de contenu vérifiés **par jeu** (distribution réelle 92/48/18/16) — pas d'application uniforme.
- Grilles responsives (featured stack < 720px ; catalogue minmax) → mobile OK.
- **Non vérifié en navigateur réel** (l'outil n'ouvre pas les fichiers locaux) : rendu visuel à valider après déploiement (Ctrl+F5).

### Remaining improvements (réel)
1. **Groupes visuels** « Roblox » / « Autres jeux » avec en-têtes dans le catalogue (aujourd'hui : filtre plateforme + tri, un seul flux). Faisable côté JS si tu le souhaites.
2. **Hubs Roblox par jeu** (`/games/roblox/<slug>/`) : non créés volontairement pour ne pas dupliquer les URLs `codes-<slug>.html` existantes (SEO).
3. **Contenu Aniimo** (guides, tier list, créatures) → enrichira automatiquement sa carte et son featured.
4. Passe **design** fine après revue visuelle en ligne.

---

**Pour publier** : `del .git\index.lock` puis
`git add -A && git commit -m "/games/ : hub de decouverte (featured + types de contenu par jeu)" && git push origin main` — puis **Ctrl+F5**.
