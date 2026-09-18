# ZoneBlox — Fondation multigaming (Phase 1) — 17 septembre 2026

Objectif de la passe : poser une **fondation « game-first » réutilisable** sur le stack existant (statique, Apache/Hostinger, sans framework) et livrer le **hub Aniimo + la page Codes Aniimo**, sans toucher aux URLs Roblox. Approche validée : *statique + générateur Python*, périmètre *fondation + hub + Codes*, données Aniimo *recherchées et uniquement vérifiables*.

> Note : ces changements s'ajoutent à ceux du run de maintenance du matin (encore non commités). Un seul `git push` publiera l'ensemble.

## 1. Ce qui a changé
- Introduction d'une **couche données → générateur → HTML statique** : ajouter un jeu devient une **opération data** (déposer un JSON + relancer le générateur), pas du développement.
- Nouvelle arborescence **`/games/`** : annuaire des jeux, hub par jeu, une page par type de contenu.
- **Aniimo** intégré comme premier vertical non-Roblox (hub + Codes vérifiés).
- **Roblox 100 % préservé** : aucune URL déplacée ; Roblox apparaît comme « plateforme » dans l'annuaire `/games/` (carte pointant vers `tous-les-codes.html`).
- Entrée **« Jeux »** ajoutée à la navigation (desktop + mobile) sur 191 pages.

## 2. Fichiers créés
- `css/platform.css` — design system partagé (extrait du gabarit + composants plateforme : annuaire, hub, chips de contenu, cartes).
- `tools/build_site.py` — **générateur statique réutilisable** (pur stdlib, idempotent).
- `data/games/aniimo.json` — entité jeu Aniimo + `contentTypes` déclarés.
- `data/aniimo/codes.json` — codes Aniimo vérifiés + FAQ + sources.
- `games/index.html` — annuaire des jeux.
- `games/aniimo/index.html` — hub Aniimo.
- `games/aniimo/codes/index.html` — page Codes Aniimo.
- `sitemap-games.xml` — sitemap dédié au nouveau vertical.

## 3. Fichiers modifiés
- `robots.txt` — ajout de `Sitemap: …/sitemap-games.xml` (le `sitemap.xml` existant reste inchangé).
- **191 pages HTML** — ajout du lien de nav « Jeux » (après « Accueil »), desktop + menu mobile. Aucune autre modification, aucun contenu ni URL touché.

## 4. Changements de schéma / données
- Pas de base de données (site statique). Nouveau **modèle data** :
  - `data/games/<slug>.json` = entité jeu (`slug, name, platform, publisher, genre, description, releaseDate, platforms, status, officialWebsite, contentTypes[]…`).
  - `data/<slug>/<type>.json` = données d'un type de contenu (ici `codes.json`).
  - Le générateur mappe chaque `contentType` déclaré `available` à un moteur de rendu (`RENDERERS` — aujourd'hui `codes`). Les types `soon` s'affichent honnêtement en « bientôt » sur le hub.

## 5. Nouvelles routes
- `/games/` (annuaire) · `/games/aniimo/` (hub) · `/games/aniimo/codes/` (codes). URLs propres via dossiers `index.html` (aucun rewrite Apache requis, trailing slash canonique).

## 6. Routes existantes préservées
- **Toutes.** Aucune URL Roblox déplacée ou redirigée. `codes-<slug>.html`, `tier-list/…`, `guides/…`, `avatar/…`, `tous-les-codes.html`, `sitemap.xml` : intacts. Le `.htaccess` (301 hérités) n'a pas été touché.

## 7. Contenu Aniimo créé (uniquement vérifié)
- **Identité** : RPG open-world free-to-play de capture de créatures (« Pathfinder », continent d'Idyll) ; sortie **16 sept. 2026** (PC/PS5/Xbox), **23 sept.** (iOS/Android) ; éditeur **FunPlus**. Aucun visuel officiel inventé → vignette de marque (monogramme sur dégradé).
- **Codes actifs (≥5 sources concordantes — Game8, Beebom, Pro Game Guides, Destructoid, Insider Gaming)** :
  - **ANIIMOGIFT** → 10 Glimmer, 20 000 Credits, 10 Growth Flowers, 5 Aniipod Pro
  - **Aniimo2026** → 1× Œuf SUSUTA, 2× Aniipod Ultra, 200× Glimmer
- Procédure d'échange (Paramètres → Compte → Gift Code Redemption), section « pourquoi ça ne marche pas », FAQ (dont clarification des *Squad Codes* de l'évènement « Aniimo Together »), sources listées. Types guides/tier-list/créatures/objets/lieux/équipes/MAJ/actus déclarés « bientôt » (pas de données inventées).

## 8. Changements SEO
- Métadonnées générées par page (title, meta description, canonical, OpenGraph, Twitter card) — mois/année dynamiques sur la page codes.
- **JSON-LD** : `BreadcrumbList` (toutes), `VideoGame` (hub), `ItemList` + `FAQPage` (codes). Aucune fausse note/avis.
- Fil d'ariane visible + structuré représentant la nouvelle taxonomie (Accueil › Jeux › Aniimo › Codes) **sans** casser les URLs plates existantes.
- `sitemap-games.xml` déclaré dans `robots.txt` ; maillage interne (hub ↔ codes ↔ annuaire ↔ footer) → aucune page orpheline.

## 9. Risques potentiels
- **Nav sur 191/194 pages** : 3 pages à structure de nav atypique n'ont pas reçu « Jeux » (à compléter). Aucune régression (ajout d'un lien seulement, `<div>` équilibrés, 0 null byte vérifiés).
- **Duplication des données** encore présente sur l'existant Roblox (main.js / index / tous-les-codes) — non convergée volontairement (hors périmètre, éviterait tout big-bang risqué).
- **Portabilité du générateur** : pur stdlib, donc exécutable tel quel par toi en local (Windows) via `python3 tools/build_site.py`, sans dépendance à installer.
- Éditeur/développeur Aniimo : sources en léger conflit (FunPlus vs Pawprint/Kingsglory) → seul **FunPlus** (site officiel) est affiché ; développeur laissé vide par prudence.

## 10. Tests réalisés
- 3 pages générées : `<div>`/`<section>` équilibrés (0), GA4 présent, fin `</html>`, **0 null byte**, tous les blocs JSON-LD valides.
- `sitemap-games.xml` : XML valide, 3 URLs.
- Injection nav : `<div>` équilibrés + 0 null byte sur échantillon (index, codes, hub, tous-les-codes, tier-list) ; « Jeux » bien placé après « Accueil ».
- Liens internes des pages générées vérifiés existants (tous-les-codes, tier-lists, guides, a-propos, ugc-gratuits, avatar, css/platform.css).
- Scan null-byte **sur tout le site** : aucun fichier atteint.

## 11. Travaux recommandés (prochaines passes)
1. **Bloc « Nouveau jeu » sur l'accueil** (index.html) mettant Aniimo/`/games/` en avant, pour renforcer l'aspect natif au-delà de la nav.
2. **Étendre le vertical Aniimo** au rythme des données vérifiables : guides (débutant), puis tier list / créatures / objets / lieux — chacun = un nouveau `data/aniimo/<type>.json` + un moteur de rendu dans `build_site.py`.
3. **Recherche globale** multigaming (jeux + codes + contenus) — index JSON généré par `build_site.py`.
4. **Convergence progressive** de la donnée Roblox vers le même modèle `data/games/` (sans casser les pages existantes), pour unifier à terme.
5. Compléter la nav « Jeux » sur les 3 pages restantes + rollout d'un vrai include de nav partagé pour les futurs jeux.
6. Ajouter le vertical **Aniimo** aux fils « Derniers contenus » quand les feeds seront branchés sur des données réelles.

---

**Pour publier** : dans le dossier GameNova,
`git add -A && git commit -m "Fondation multigaming + vertical Aniimo (hub + codes)" && git push origin main`.
Hostinger déploie automatiquement. Pour régénérer les pages `/games/` après une modif de données : `python3 tools/build_site.py`.
