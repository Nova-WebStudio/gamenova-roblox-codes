# HOMEPAGE REDESIGN COMPLETED — 18 septembre 2026

Refonte de la hiérarchie de l'accueil pour une identité **plateforme gaming**, sans rien casser ni inventer. H1 Roblox préservé, aucune URL déplacée, stack existant (statique).

### Homepage — nouvelle hiérarchie (ordre des H2)
1. **🎮 Choisis ton jeu** (découverte multigaming — juste sous le hero)
2. ⭐ Jeu de la semaine (mise en avant)
3. **🆕 Nouveautés** (nouveau — faits réels : Aniimo, page Search For The Needle, nouvel annuaire)
4. **📚 Guides à découvrir** (nouveau — 6 guides réels + CTA vers /guides.html)
5. **🎁 Codes récemment mis à jour** (ex-« Codes du jour », reformulé multigaming)
6. 🧭 Parcourir par catégorie (Roblox)
7. 🔥 Jeux & codes (Roblox populaires)
8. 📊 Tier lists populaires
9. **🎮 Jeux disponibles** (ex-« Tous les jeux couverts » ; CTA corrigé vers **/games/**)
10. ❓ Questions fréquentes (en bas)

La première moitié communique le multigaming ; la seconde préserve l'autorité Roblox. **Un seul H1**, inchangé : `Tous les codes Roblox actifs, au même endroit`.

### Navigation
Inchangée depuis la passe précédente : entrée **« Jeux » → /games/**, header identique sur les 194 pages (logo réel + 7 entrées uniformes).

### Game Discovery
Section « Choisis ton jeu » en tête (Roblox / Aniimo / Tous les jeux) + CTA hero « Explorer les jeux » et « Découvrir Aniimo ». Le compteur Roblox est exact (173).

### Featured Content
« Jeu de la semaine » conservé tel quel (contenu réel, mis à jour chaque lundi par la tâche planifiée) — **non renommé exprès** pour ne pas entrer en conflit avec cette maintenance automatique.

### News
Ajout d'une section **🆕 Nouveautés** avec **3 cartes 100 % factuelles** (sortie d'Aniimo sur la plateforme, page codes Search For The Needle, nouvel annuaire /games/). **Aucune fausse actualité** : je n'ai pas créé de fil « actualités gaming » fictif (règle d'honnêteté). La brique reste extensible quand un vrai flux d'actus existera.

### Guides
Nouvelle section **📚 Guides à découvrir** : 6 **guides réels existants** (Blox Fruits, Search For The Needle, Anime Vanguards, Volleyball Legends, Blade Ball, Steal an Egg) + CTA « Voir tous les guides → » vers /guides.html. Prête à accueillir des guides d'autres jeux (Aniimo…) dès qu'ils existent.

### Codes
Section « Codes du jour » reformulée en **« Codes récemment mis à jour »** (signal multigaming) — le mécanisme et le contenu Roblox existants sont conservés.

### Roblox
**Rien supprimé.** Les sections Roblox (catégories, jeux populaires, tier lists, liste A→Z) sont **conservées et repositionnées plus bas**, sous les sections de découverte. La section liste renvoie désormais vers l'annuaire **/games/**.

### Aniimo
Jeu de première classe : carte « Choisis ton jeu », carte « Nouveautés », hub /games/aniimo/ et page codes /games/aniimo/codes/ (données vérifiées). Présent dans l'annuaire et recherchable.

### /games/
Inchangé cette passe (déjà refondu : 174 jeux, recherche + filtres plateforme/genre + tri, cartes indexables, miniatures lazy). La section « Jeux disponibles » de l'accueil y renvoie maintenant.

### Data architecture
Inchangée : `data/games/*.json`, `data/games-index.json`, générateur `tools/build_site.py`. Les nouvelles sections d'accueil pointent vers du contenu réel existant (aucune duplication de métadonnées).

### SEO
Préservé : **H1 unique intact**, `<title>` inchangé, `canonical` présent, `sitemap.xml` (335) et `sitemap-games.xml` intacts, robots intact, structured data valides. Nouveaux H2 bien hiérarchisés sous un seul H1. Maillage interne renforcé vers /games/, /games/aniimo/, /guides.html.

### Testing
- index.html : **1 seul H1**, `<div>` équilibrés (0), fin `</html>`, **0 null byte**, title/canonical intacts.
- **10/10 liens** des nouvelles sections résolus vers des fichiers existants (0 manquant).
- Scan null-byte **sur tout le site** : aucun fichier atteint.
- Sections neuves en grilles responsives (`auto-fill minmax`) → adaptées mobile, pas de débordement horizontal.
- **Non testé en navigateur réel** (le navigateur intégré n'ouvre pas les fichiers locaux) : à confirmer visuellement après déploiement (Ctrl+F5). Le JS existant n'a pas été modifié (uniquement ajout de sections + renommage de H2).

### Remaining improvements (réels)
1. **Fil d'actualités gaming** véritable (au-delà des nouveautés du site) — à brancher quand une source de news existe ; ne pas fabriquer.
2. **Guides/tier lists Aniimo** : dès qu'ils existent, ils remonteront automatiquement dans « Guides à découvrir » et le hub.
3. **Aperçu condensé** de la liste A→Z sur l'accueil (aujourd'hui elle affiche encore beaucoup de jeux) — la découverte complète est déjà sur /games/.
4. Regénérer /games/ après ajout de jeux : `python3 tools/build_site.py`.

---

**Pour publier** : `del .git\index.lock` puis
`git add -A && git commit -m "Refonte accueil multigaming (hiérarchie, Nouveautés, Guides, reframe codes)" && git push origin main` — puis **Ctrl+F5**.
