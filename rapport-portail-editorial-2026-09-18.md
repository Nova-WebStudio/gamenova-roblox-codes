# HOMEPAGE REDESIGN — Portail gaming éditorial — 18 septembre 2026

Transformation de l'accueil vers une **structure de portail gaming éditorial** (inspiration : densité et hiérarchie d'un GameWave, **sans copie**), en gardant le H1 Roblox et **sans aucun contenu inventé**. Stack existant (statique, index.html).

### New visual direction
De « site de codes Roblox » à **« portail gaming »** : une barre de tendances, une une éditoriale image-driven, une section signature Guides & codes, puis les verticales Roblox et Aniimo. Densité organisée, cartes visuelles, vraies miniatures de jeux.

### Structure finale (H1 + H2 dans l'ordre)
1. **Barre « 🔥 Jeux du moment »** (sous le header, sélection éditoriale, mini-miniatures)
2. Hero — **H1 conservé** : *Tous les codes Roblox actifs, au même endroit* + sous-titre multigaming + recherche + CTA
3. **🔥 À la une** — grille éditoriale : 1 grande story (Guide Blox Fruits, image plein cadre) + 3 cartes (Aniimo, Search For The Needle, Anime Vanguards)
4. **🎮 Choisis ton jeu** — découverte (Roblox / Aniimo / Tous les jeux)
5. ⭐ Jeu de la semaine
6. **🆕 Nouveautés** — 3 cartes factuelles (Aniimo, page SFTN, annuaire)
7. **🎯 Guides & codes** — section signature **deux colonnes** (guides réels | codes réels)
8. 🎁 Codes récemment mis à jour
9. **🎮 Roblox** — en-tête de verticale, suivi des sections Roblox (catégories, populaires)
10. 📊 Tier lists populaires
11. **🎮 Jeux disponibles** → /games/
12. **🆕 Aniimo** — verticale dédiée (codes actifs + guides/tier/créatures « bientôt »)
13. ❓ FAQ (bas de page)

**Un seul H1**, inchangé.

### Header
Inchangé (déjà uniforme sur 194 pages) : logo réel + « Accueil · Jeux · Tous les codes · Tier lists · Guides · Avatars · UGC gratuits ». « Jeux » → /games/.

### Trending games
Barre **« Jeux du moment »** horizontale (scroll sur mobile), **sélection éditoriale honnête** (pas de fausse métrique de popularité) : Aniimo + Search For The Needle, Blox Fruits, Grow a Garden, Steal a Brainrot, Blue Lock Rivals, Anime Vanguards, Blade Ball, Volleyball Legends, Anime Last Stand. Miniatures réelles `tr.rbxcdn.com`, liens vers les pages. Data-driven (extraite de la liste de jeux existante) → un futur GTA 6 s'y ajoutera par la donnée.

### Featured content
Grille **« À la une »** image-driven (1 grande + 3 secondaires), alimentée par du **contenu réel existant** (guides + pages codes + hub Aniimo). Aucune story fabriquée.

### News
Section **« Nouveautés »** = équivalent feed d'actus, mais **uniquement des faits réels** (arrivée d'Aniimo, page codes SFTN, nouvel annuaire). **Aucune fausse actualité** — je n'ai pas inventé de fil de news gaming (règle d'honnêteté), la brique reste extensible.

### Guides & Codes
Nouvelle section signature **deux colonnes** : gauche = 6 **guides réels** (Blox Fruits, SFTN, Anime Vanguards, Volleyball Legends, Blade Ball, Steal an Egg) + « Voir tous les guides » ; droite = 6 **pages codes réelles** (Aniimo, Blox Fruits, Steal a Brainrot, Grow a Garden, Blade Ball, SFTN) + « Voir tous les codes ». C'est le différenciateur de Zoneblox, mis en avant.

### Games
Découverte « Choisis ton jeu » + « Jeux disponibles » renvoyant vers l'annuaire **/games/** (déjà refondu : 174 jeux, recherche + filtres + tri).

### Roblox
**Rien supprimé.** Les sections Roblox (catégories, jeux populaires, liste A→Z, tier lists) sont **regroupées sous un en-tête « 🎮 Roblox »** et positionnées après les sections de découverte/éditoriales — présentes mais non dominantes.

### Aniimo
Verticale dédiée **« 🆕 Aniimo »** : visuel de marque, description réelle (RPG de capture de créatures), CTA vers la page codes (données vérifiées) et types de contenu à venir affichés honnêtement « bientôt ». Aniimo apparaît aussi dans la barre tendances, la une, les nouveautés, la découverte et la colonne codes.

### SEO preserved
- **H1 unique intact** ; `<title>` et `canonical` inchangés ; `sitemap.xml` (335) et `sitemap-games.xml` intacts ; robots intact ; JSON-LD existants conservés.
- Hiérarchie propre : 1 H1, puis H2 par section. Maillage interne renforcé (vers /games/, /games/aniimo/, /guides.html, /tous-les-codes.html, guides et pages codes réels).

### Files changed
- `index.html` : barre tendances, « À la une », « Guides & codes » (remplace l'ancienne section guides), verticale Aniimo, en-tête Roblox, reformulations (Codes récemment, Jeux disponibles), `<style>` responsive pour les nouvelles grilles. **Seul fichier modifié cette passe.**

### Tests
- **1 seul H1** (intact) ; `<div>` équilibrés (0) ; fin `</html>` ; **0 null byte** (site entier).
- **12 miniatures éditoriales** = URLs `tr.rbxcdn.com` complètes (non tronquées) ; **31 liens** des nouvelles sections → **0 manquant**.
- 16 images en `loading="lazy"` ; grilles éditoriales avec **règles responsives** (stack < 760px) → mobile OK, pas de débordement.
- **Non vérifié en navigateur réel** : le navigateur intégré n'ouvre pas les fichiers locaux. Le rendu visuel est à valider après déploiement (Ctrl+F5). Le JS existant n'a pas été touché (uniquement ajout de sections HTML/CSS).

### Remaining work (réel)
1. Vrai **fil d'actualités gaming** éditorial (au-delà des nouveautés du site) — quand une source de news existe ; ne pas fabriquer.
2. **Contenu Aniimo** (guides, tier list, créatures) → remontera automatiquement dans « Guides & codes », « À la une » et la verticale.
3. **Aperçu condensé** de la liste A→Z sur l'accueil (elle affiche encore beaucoup de jeux ; la découverte complète est sur /games/).
4. Passe **design** fine (typographie/espacements) après revue visuelle en ligne.
5. Regénérer /games/ après ajout de jeux : `python3 tools/build_site.py`.

---

**Pour publier** : `del .git\index.lock` puis
`git add -A && git commit -m "Accueil : portail gaming editorial (tendances, a la une, guides & codes, verticales)" && git push origin main` — puis **Ctrl+F5**, et dis-moi ce que tu en penses visuellement (je pourrai ajuster densité/typo).
