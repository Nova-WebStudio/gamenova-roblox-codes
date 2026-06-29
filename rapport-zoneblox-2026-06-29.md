# Rapport Zoneblox — 29 juin 2026 (lundi)

> Run de maintenance automatique. **Lundi** → mise à jour du « Jeu de la semaine » effectuée.

## ÉTAPE 0 — Surveillance des codes (27 jeux « hotGames »)
Descriptions in-game + métadonnées des **27 jeux** récupérées en direct via l'API Roblox officielle (`games.roblox.com/v1/games`, exécutée dans Chrome car le shell n'a pas d'accès réseau). Codes potentiels extraits et comparés aux snapshots + pages.

| Jeu | Code dans la description in-game | Statut |
|-----|----------------------------------|--------|
| fruit-battlegrounds | `YOO1M110K` (prochain à 1 120 000 likes) | déjà publié ✓ |
| blockspin | `W7C28D` | déjà publié ✓ |
| merge-a-nuke | `BOOM` | déjà publié ✓ |
| **squid-game-x** | `$1.2M$` (« 1,2 million de dollars ») | **PUBLIÉ ce run ✓** (voir ÉTAPE 2) |

Les autres jeux populaires (blox-fruits, grow-a-garden, king-legacy, fisch, blue-lock-rivals, steal-a-brainrot, etc.) renvoient « rejoignez le groupe / aimez pour des codes » sans token explicite : aucun nouveau code confirmable.

Snapshots des **27 jeux** : `lastChecked` mis au 29 juin 2026. JSON revalidé (parse OK, se termine par `}`).

## ÉTAPE 2 — Codes : NOUVEAU code publié pour Squid Game X
Le candidat `squid-game-x` (en attente depuis le 27 juin) est désormais **confirmé par 2 sources** :
1. **Description officielle en jeu** : « 🌟NOUVEAU CODE🌟 « 1,2 million de dollars » » (prochain code à 1,4 M de likes).
2. **Roblox Den** (vérifié le 28/06/2026) : « NEW CODE — $1.2M — 200 Coins — ACTIVE ».

Le token littéral suit le format établi du jeu (`$1M$`, `$500K$`, `$250K$`, `$100K$` déjà présents) → **`$1.2M$`**. Publié en tête de tableau sur `codes/squid-game-x.html` (récompense : 200 Coins), avec marqueur « 🆕 NOUVEAU ». Dates « Mis à jour le… » / bannière / barre de statut passées au **29 juin 2026** (changement réel → date modifiée à juste titre). `code-watch.json` : candidat marqué « PUBLIÉ », `$1.2M$` ajouté à `knownCodes`.

Aucun autre changement de code confirmable à 2 sources ce run.

## ÉTAPE 7 — Jeu de la semaine (LUNDI) → **Steal a Brainrot**
Le bloc `FEATURED-WEEK` d'`index.html` est passé de *Grow a Garden 2* à **Steal a Brainrot**, le phénomène n°1 des tendances Roblox cette semaine.

Justification (données live, ce run) : Steal a Brainrot est le jeu en tendance dominant de la plateforme — **207 610 joueurs en simultané**, 70,6 milliards de visites, 28,5 M de favoris — confirmé par la recherche web (« biggest concurrent player numbers on Roblox in June 2026 »). Présent au catalogue avec **les 3 pages dédiées** (codes, tier list, guide complet), toutes liées dans le bandeau.

Détails de la carte :
- Miniature réelle fraîchement vérifiée via l'API Roblox : `tr.rbxcdn.com/180DAY-64170d84ffa0cba4ee5af8bd1cd2df66/768/432/Image/Png/noFilter` (fallback SVG `/images/games/steal-a-brainrot.svg`).
- Blurb FR honnête (mécaniques : acheter des Brainrots qui rapportent, voler ceux des autres, renaître, gifles/objets de troll, classement).
- Boutons : 🎁 Codes → `/codes/steal-a-brainrot.html`, 📊 Tier list → `/tier-list/steal-a-brainrot.html`, 📖 Guide → `/guides/steal-a-brainrot.html` (les 3 existent).

## ÉTAPES 1, 3, 4, 5, 6 — Ajout de jeux / thin-content / tier lists / guides / UGC
- **Ajout de 6 jeux (ÉTAPE 1)** : non réalisé ce run (priorité au feature lundi + au code vérifié ; l'ajout complet exige codes 2 sources + 2 vidéos oEmbed + miniatures, à planifier sur un run dédié).
- **Thin-content (ÉTAPE 3)** : audit précédent → tout le catalogue codes ≥ 1200 mots ; aucune page modifiée à étoffer ce run.
- **Tier lists / Guides complets / UGC** : aucun changement méta confirmé à 2 sources nécessitant une refonte ; rien modifié pour ne pas altérer de dates sans changement réel.

## ÉTAPE 9 — Cache JS
`js/main.js` **non modifié** ce run → pas de bump (reste `v=29`, uniforme sur tout le site).

## ÉTAPE 8 — QC final
- Fichiers modifiés vérifiés **intègres côté disque réel** (outil de lecture fichier) : `index.html` se termine par `</body></html>` (902 lignes), `codes/squid-game-x.html` par `</body></html>` (203 lignes). 0 octet nul, divs équilibrées (édits internes à des blocs déjà équilibrés), GA4 présent, nav 7 entrées (Avatars OK), cache `v=29`, bandeau `data-cta="guidelink"` unique conservé.
- `tools/code-watch.json` : JSON valide (parse OK, se termine par `}`).
- ⚠️ Note technique récurrente : le **montage Linux du shell sert des lectures en cache obsolètes/tronquées** des fichiers édités en place (ex. `index.html` affiché à l'ancienne taille sans `</html>`). Vérification réelle confirmée via l'outil de lecture fichier (côté Windows) : **aucune troncature réelle**. Ne pas se fier aux `tail`/`wc` du shell pour les fichiers fraîchement édités.

## ⚠️ À signaler / pistes prochains runs
- **Squid Game X** : surveiller l'expiration de `$1M$` (les paliers de likes tournent vite) et l'arrivée du prochain code à 1,4 M de likes.
- **Ajout de 6 jeux (ÉTAPE 1)** : à planifier sur un run dédié (codes 2 sources + vidéos oEmbed + miniatures tr.rbxcdn.com).
- Prochains guides complets candidats (jeux populaires sans guide) : pet-simulator-99, fruit-battlegrounds, squid-game-x, hypershot, fifa-super-soccer.
- **Miniature steal-a-brainrot** : l'API renvoie désormais un nouveau hash (`64170d84…`) ; le reste du site utilise encore `30a62664…`. À harmoniser (ROBLOX_THUMBS + THUMBS + heros) sur un run dédié avec bump de cache si nécessaire.

## Fichiers touchés
- `index.html` (bloc « Jeu de la semaine » → Steal a Brainrot)
- `codes/squid-game-x.html` (nouveau code `$1.2M$` + 3 dates au 29 juin)
- `tools/code-watch.json` (snapshots 27 hotGames au 29 juin + candidat squid-game-x marqué PUBLIÉ)
- `rapport-zoneblox-2026-06-29.md` (ce rapport)

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`
Hostinger déploie automatiquement après le push.
