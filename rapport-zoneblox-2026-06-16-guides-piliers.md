# Rapport Zoneblox — 16 juin 2026 (guides piliers : King Legacy & Fisch)

Première vague de production des **pages piliers /guides/** à partir du blueprint SEO. Priorité donnée à deux jeux à fort trafic sans guide existant : **King Legacy** et **Fisch**.

## Guides créés
- **`guides/king-legacy.html`** — gabarit `blox-fruits`, 12 sections : débutant, leveling, meilleur fruit (Pteranodon/Dragon/Phoenix/Magma), meilleure race (Angel V3 PvP / Sea Beast V3 PvE / Human V3 grind), farm Beli (Easy Raid ~1M/run), épées & styles, awakening, raids/boss, mers Sea 2/3, build PvP, Gems, FAQ.
- **`guides/fisch.html`** — gabarit `blox-fruits`, 12 sections : débutant, farm d'argent (Veil of the Forsaken ~500K C$/h ; The Depths nuit 200-300K), meilleure canne (Carbon → Trident → Rod of the Elements → Masterline / Sword of Darkness), appâts, spots de poissons rares (Deep Ocean Trench, Volcano Crater Lake, Northern Aurora Sea), légendaires/Mythic, mutations, météo (Rainbow 10x / Aurora 9x), bestiaire, zones, codes, FAQ.

Contenu **vérifié sur 2 sources** par jeu (King Legacy : Sportskeeda/Driffle/VideoGamer/Pro Game Guides ; Fisch : LDPlayer/U7Buy/PositionIsEverything/FischCalculator). Aucune donnée inventée ; formulations prudentes là où le méta évolue.

## SEO intégré
- **Titres** « Guide <Jeu> (2026) – … | Zoneblox », **meta** 150-160 caractères, **keywords**, **canonical**, **OG** avec vraie miniature `tr.rbxcdn.com`.
- **JSON-LD** : Article + BreadcrumbList + **FAQPage** (6 Q/R → éligibilité rich snippets).
- **TOC ancré** (sommaire cliquable) + sections H2/H3 + tableaux (tier list fruits / progression cannes).

## Maillage interne (codes ↔ tier list ↔ guide)
- **guides/index.html** : 2 cartes ajoutées (avec vraie miniature).
- **sitemap.xml** : 2 `<url>` guides ajoutés (lastmod 2026-06-16).
- **codes/king-legacy.html** & **codes/fisch.html** : bandeau CTA `data-cta="guidelink"` mis à jour → bouton « 📖 Guide complet » (vers le guide dédié) + « 📊 Tier list ».
- **tier-list/king-legacy.html** & **tier-list/fisch.html** : bouton « 📚 Guide complet » ajouté dans le hero.

## QC (outils fiables Read/Grep)
- Les 2 guides : se terminent par `</html>`, GA4 = 2, équilibre `<div>` = 0, **aucun octet nul**, nav 7 entrées (Avatars), FAQPage + TOC présents.
- Liens vérifiés : guide↔codes (1 chacun), 2 cartes dans le hub, 2 URL sitemap.
- `js/main.js` **non modifié** ce run → pas de bump de cache nécessaire (reste `v=24`, cohérent).

## Reste à produire (depuis le blueprint, sans doublon)
Anime Reborn, Dead Rails, Volleyball Legends, Basketball Zero, Defend Ur Base With Anime, Anime Rangers X, Project Egoist*, Sailor Piece, Pet Simulator 99, All Star Tower Defense X* (*créer d'abord la page codes, absente du catalogue).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "Guides piliers King Legacy + Fisch (SEO)" && git push origin main` . Hostinger déploie automatiquement après le push.
