# ZoneBlox — Redesign UX multigaming (accueil + annuaire /games/) — 18 septembre 2026

Suite de la fondation multigaming : transformation de l'accueil et refonte complète de `/games/` en véritable annuaire de découverte, sur le stack existant (statique, Apache/Hostinger, générateur Python). **Aucune donnée de jeu inventée. H1 Roblox préservé. Aucune URL Roblox déplacée.**

## IMPLEMENTED

### Homepage
- Section **« 🎮 Choisis ton jeu »** juste sous le hero (déjà posée) : cartes **Roblox** (→ tous-les-codes), **Aniimo** (badge Nouveau → hub), **Tous les jeux** (→ /games/). Compteur Roblox rendu **exact (173 jeux)** au lieu de « 178+ ».
- **CTA hero** ajoutés : « 🎮 Explorer les jeux » (→ /games/) et « ✨ Découvrir Aniimo » (→ /games/aniimo/).
- Sous-titre du hero enrichi : « …Roblox, Aniimo et bientôt d'autres jeux. »
- **H1 SEO intact** : `Tous les codes Roblox actifs, au même endroit` — non modifié (exigence explicite).
- Les sections Roblox existantes (Jeu de la semaine, Codes du jour, Populaires, Tier lists) restent, désormais **sous** le bloc de découverte multigaming → hiérarchie « plateforme d'abord, Roblox ensuite ».

### Games Directory (/games/) — refonte complète
- **174 jeux** listés (173 Roblox + Aniimo), cartes **rendues dans le HTML** (SEO-friendly, pas de contenu JS-only).
- **Recherche instantanée** par nom : « blox fruits » trouve Blox Fruits, « aniimo » trouve Aniimo (client-side, aucun rechargement).
- **Filtres data-driven** : Plateforme (Roblox / PC · Console / Mobile) et Genre (Simulateur, Anime, Combat, RPG, Tycoon, Tower Defense, Sport, Obby, Horreur) — uniquement les valeurs réellement présentes.
- **Tri** : « Récemment mis à jour » (défaut → les nouveautés remontent) et « A → Z ».
- Compteur de résultats en direct + **état vide** avec bouton de réinitialisation.
- **Performance** : 173 miniatures Roblox réelles en `loading="lazy"` ; monogramme de marque pour Aniimo (aucun visuel inventé).
- H1 unique **« Tous les jeux »**, title/description propres, `canonical` /games/. Filtres **côté client sans paramètres d'URL** → zéro URL de filtre indexable en double.

### Data Architecture
- Nouveau **`data/games-index.json`** généré (174 jeux : nom, slug, url, plateformes, genres, date, source roblox/standalone, types de contenu) — base réutilisable pour une future recherche globale.
- Directory **data-driven** : le générateur lit les jeux standalone (`data/games/*.json`) **et** les jeux Roblox (`const GAMES` d'index.html), sans logique `if game === …`. Ajouter un jeu reste une **opération data**.
- Générateur étendu : `tools/build_site.py` (helpers date FR, chargement Roblox, dérivation genres/plateformes, rendu cartes + recherche/filtres/tri).

### Aniimo
- Aniimo est un **jeu de première classe** : carte en tête de l'annuaire (tri par nouveauté), hub `/games/aniimo/`, page codes `/games/aniimo/codes/` (données vérifiées : ANIIMOGIFT, Aniimo2026). Même architecture que les futurs jeux.

### SEO
- H1 accueil préservé ; H1 `/games/` = « Tous les jeux ».
- `sitemap.xml` **intact** (335 URLs, valide) ; `sitemap-games.xml` déclaré dans `robots.txt` ; `/games/` y figure.
- Structured data valide : **ItemList** (174 jeux, `numberOfItems`), **BreadcrumbList**, **VideoGame** (hub) — aucune fausse note/avis/popularité.
- Maillage : accueil → /games/, /games/aniimo/ ; annuaire → chaque page jeu ; footer → jeux. Aucune page orpheline.

### Components (réutilisables, data-driven)
- `GameCard` (annuaire + accueil), toolbar de recherche/filtres, chips, monogramme de marque, `ct-card`/`ct-nav` (types de contenu du hub), tout dans `css/platform.css`.

### Routes
- Nouvelles : `/games/` (annuaire refondu), `/games/aniimo/`, `/games/aniimo/codes/`.
- Roblox : liens directs vers les pages existantes `codes-<slug>.html` (pas de `/games/roblox/` créé, pour ne pas perturber le SEO — la carte « Roblox » pointe vers `tous-les-codes.html`).

### Existing URLs preserved
- **Toutes.** Les 173 liens Roblox de l'annuaire résolvent vers des fichiers existants (0 manquant, vérifié). Aucune page `codes-*.html`, `tier-list/*`, `guides/*` déplacée ni redirigée. `.htaccess` non touché.

### Tests
- QC : H1 Roblox intact ; H1 unique sur /games/ ; **174 cartes** ; recherche/filtres/tri câblés sur les bons IDs ; 173 liens Roblox → 0 fichier manquant ; hub Aniimo présent ; `<div>` équilibrés (0) sur accueil + pages générées ; **0 null byte sur tout le site** ; toutes les pages finissent en `</html>` ; JSON-LD valides ; `sitemap.xml` valide (335) ; robots = 2 sitemaps ; images en lazy-load.
- **Limite** : le comportement JS (recherche/filtres) n'a pas pu être vérifié dans un vrai navigateur (le navigateur intégré n'ouvre pas les fichiers locaux) — le code est du vanilla JS simple, vérifié structurellement. À confirmer visuellement après déploiement (Ctrl+F5).

### Remaining improvements (prochaines passes)
1. **Sections « Dernières actus / guides / codes »** multi-jeux sur l'accueil : construire l'architecture quand il y a du **contenu réel** (pas de fausse actu — volontairement non ajouté).
2. **Recherche globale** (jeux + codes + guides + créatures…) en s'appuyant sur `data/games-index.json`.
3. **Étendre Aniimo** (guides, tier list, créatures) au fil des données vérifiables → nouveaux `data/aniimo/<type>.json` + moteurs de rendu.
4. **Convergence** progressive des données Roblox vers `data/games/` pour unifier le modèle.
5. Regénérer l'annuaire après ajout de jeux : `python3 tools/build_site.py`.

---

**Pour publier** : `del .git\index.lock` puis
`git add -A && git commit -m "Redesign multigaming : accueil + annuaire /games/ (recherche, filtres, tri)" && git push origin main`.
Après déploiement, **Ctrl+F5** pour rafraîchir le cache (nav + nouveau /games/).
