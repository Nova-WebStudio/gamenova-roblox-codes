# Rapport Zoneblox — 28 juin 2026 (dimanche)

> Run de maintenance automatique. Dimanche → pas de mise à jour « Jeu de la semaine » (réservée au lundi).

## État général du site (sain)
- **285 fichiers HTML** (avant ce run) : tous se terminent par `</html>`, 0 octet nul, balises `<div>` équilibrées.
- **157 jeux** au catalogue : `GAMES_INDEX` ↔ `ALL_GAMES` parfaitement synchronisés (0 écart).
- `node --check js/main.js` : OK. `sitemap.xml` valide (`</urlset>`).
- Cache JS uniforme : **`main.js?v=29`** sur toutes les pages.
- Audit thin-content : **0 page codes réelle sous 1200 mots** (158 pages codes ≥ seuil ; seul `codes/_TEMPLATE.html`, un gabarit, est court — normal).

## ÉTAPE 0 — Surveillance des codes (27 jeux « hotGames »)
Descriptions in-game + métadonnées des **27 jeux** récupérées en direct via l'API Roblox officielle (`games.roblox.com/v1/games`, exécutée dans Chrome car le shell n'a pas d'accès réseau). Codes potentiels extraits et comparés aux snapshots + pages.

| Jeu | Code dans la description in-game | Statut |
|-----|----------------------------------|--------|
| fruit-battlegrounds | `YOO1M110K` (prochain à 1 120 000 likes) | déjà publié ✓ |
| blockspin | `W7C28D` | déjà publié ✓ |
| merge-a-nuke | `BOOM` | déjà publié ✓ |
| squid-game-x | « 1,2 million de dollars » (token probable `$1.2M$`) | **en attente** ⏳ |

**Squid Game X — candidat toujours en attente.** La description officielle annonce le NOUVEAU code « 1,2 million de dollars » (prochain à 1,4 M de likes). Vérification croisée ce run : **Roblox Den** (contrôlé le 23 juin) et **Try Hard Guides** (figé en nov. 2025) ne listent **pas encore** de token `$1.2M$` — les agrégateurs n'ont pas rattrapé ce code. Le token exact n'étant pas confirmé par une 2ᵉ source fiable (et n'apparaissant pas littéralement dans la description, seulement sa traduction française), **il n'a PAS été publié** par respect de la règle d'honnêteté. Reste enregistré comme `pendingCandidate` dans `code-watch.json`.

> Les autres jeux populaires (blox-fruits, grow-a-garden, king-legacy, fisch, blue-lock-rivals, steal-a-brainrot, etc.) renvoient « rejoignez le groupe / aimez pour des codes » sans token explicite : aucun nouveau code confirmable.

Snapshots des **27 jeux** : `lastChecked` mis au 28 juin 2026. JSON revalidé (se termine par `}`, parse OK).

## ÉTAPE 2 — Codes (vérification 2 sources)
Aucun changement de code confirmable à 2 sources ce run. Les pages restent exactes ; aucune date « Mis à jour le… » modifiée sans changement réel (règle d'honnêteté).

## ÉTAPE 5 — GUIDE COMPLET créé : Volleyball Legends
Création de **`guides/volleyball-legends.html`** (1 529 mots, FR), le jeu le plus populaire du catalogue encore **sans guide complet** (~47 000 joueurs en live). Sources croisées : **description officielle en jeu** (commandes, service, +10 % Yen Premium, MAJ chaque samedi 11h30 EST) + **Pro Game Guides** (tableau complet des commandes, mécaniques service/smash/contre/réception/passe/plongeon, Styles & raretés, reroll 100 Yen/spin, Lucky Spins, déblocage du ranked au niveau 15).

Contenu : sommaire TOC ancré + 6 sections (guide débutant, toutes les commandes PC/Xbox/PS en tableau, maîtrise des coups, Styles & reroll, gagner du Yen & ranked, FAQ 5 questions) ; JSON-LD Article + BreadcrumbList + FAQPage ; CTA vers codes & tier list ; nav 7 entrées + GA4 ; miniature réelle `tr.rbxcdn.com`.

**Intégrations réalisées :**
- Carte visuelle dans `guides/index.html` (vraie miniature) + entrée `ItemList` position 36 + catégorie `volleyball-legends:'anime'` dans le filtre JS.
- `<url>` ajoutée au `sitemap.xml` (lastmod 2026-06-28).
- `codes/volleyball-legends.html` : bouton hero « 📚 Guide complet → » ajouté ; bandeau CTA `data-cta="guidelink"` mis à jour (bouton « 📖 Guide complet » plein dégradé + « 📊 Tier list » contour) ; onglet « 📖 Guide » pointe désormais vers `/guides/volleyball-legends.html` ; lien « Articles liés » mis à jour.
- `tier-list/volleyball-legends.html` : bouton hero « 📚 Guide complet → » ajouté ; lien « Articles liés » pointant vers le guide dédié.

## ÉTAPES 1, 3, 4, 6 — Ajout de jeux / thin-content / tier lists / UGC
- **Ajout de 6 jeux (ÉTAPE 1)** : non réalisé ce run (priorité donnée au guide complet vérifié ; l'ajout complet exige codes 2 sources + 2 vidéos oEmbed + miniatures, à planifier sur un run dédié).
- **Thin-content** : tout le catalogue codes est ≥ 1200 mots → aucune mise à niveau requise.
- **Tier lists / UGC** : aucun changement méta confirmé nécessitant une refonte ; rien modifié pour ne pas altérer de dates sans changement réel.

## ÉTAPE 7 — Jeu de la semaine
Dimanche (`date +%u` = 7) → **non modifié** (réservé au lundi).

## ÉTAPE 9 — Cache JS
`js/main.js` **non modifié** ce run → pas de bump (reste `v=29`, uniforme).

## ÉTAPE 8 — QC final
- Tous les fichiers modifiés vérifiés **intègres** (fin `</html>` / `</urlset>`, divs équilibrées, 0 octet nul, JSON-LD valides) via lecture côté Windows.
- ⚠️ Note technique : le montage Linux du shell a servi des **lectures en cache obsolètes** des fichiers édités en place (ex. `sitemap.xml` affiché tronqué/à l'ancienne taille). Vérification confirmée par l'outil de lecture fichier (côté disque réel) : `sitemap.xml` se termine bien par `</urlset>` (336 lignes, nouvelle entrée présente), `guides/index.html` par `</html>` (209 lignes), `codes/` et `tier-list/volleyball-legends.html` par `</html>`. Aucune troncature réelle.
- Guide Volleyball Legends : 1 529 mots, nav 7 entrées (Avatars présent), GA4 OK, cache v=29, JSON-LD valide.

## ⚠️ À signaler / pistes prochains runs
- **Squid Game X** : publier le code « 1,2 million de dollars » dès qu'une 2ᵉ source fiable confirme le token exact (probable `$1.2M$`) ; vérifier alors si `$1M$` passe expiré.
- **Anime Last Stand** (~252 joueurs) et **World Fighters** (~373) : sous le seuil 4000 en live — surveiller la pertinence de leur suivi hotGames.
- **Ajout de 6 jeux (ÉTAPE 1)** : à planifier sur un run dédié (codes 2 sources + vidéos oEmbed + miniatures tr.rbxcdn.com).
- Prochains guides candidats (jeux populaires sans guide) : pet-simulator-99, fruit-battlegrounds, squid-game-x, hypershot, fifa-super-soccer.

## Fichiers touchés
- `guides/volleyball-legends.html` (nouveau guide complet)
- `guides/index.html` (carte + ItemList + catégorie JS)
- `codes/volleyball-legends.html` (hero + CTA + onglet guide + lien)
- `tier-list/volleyball-legends.html` (hero + lien guide)
- `sitemap.xml` (url du guide)
- `tools/code-watch.json` (snapshots 27 hotGames + candidat squid-game-x)
- `rapport-zoneblox-2026-06-28.md` (ce rapport)

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`
Hostinger déploie automatiquement après le push.
