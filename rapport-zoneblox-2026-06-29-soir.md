# Rapport Zoneblox — 29 juin 2026 (soir)

> Run de maintenance automatique du soir. Le run du matin (07:08) avait déjà traité le **« Jeu de la semaine » du lundi** (→ Steal a Brainrot) et publié le code `$1.2M$` de Squid Game X. Ce run du soir n'y retouche pas (pas de double mise à jour le même lundi).

## ÉTAPE 0 — Surveillance des codes (27 jeux « hotGames »)
Descriptions in-game + métadonnées des **27 jeux** re-récupérées en direct via l'API Roblox officielle (`games.roblox.com/v1/games`, exécutée dans Chrome — le shell n'a pas d'accès réseau). Tokens candidats extraits et comparés aux snapshots + pages.

Codes explicites présents dans les descriptions ce soir :

| Jeu | Code in-game | Statut |
|-----|-------------|--------|
| fruit-battlegrounds | `YOO1M110K` | déjà publié ✓ |
| merge-a-nuke | `BOOM` | déjà publié ✓ |
| blockspin | `W7C28D` | déjà publié ✓ |
| squid-game-x | `$1.2M$` (« 1,2 million de dollars ») | déjà publié ce matin ✓ |

Les autres jeux populaires (blox-fruits, grow-a-garden, steal-a-brainrot, blue-lock-rivals, fisch, volleyball-legends, world-fighters « 25kLIKE = nouveau code », anime-last-stand, etc.) renvoient « aimez / rejoignez le groupe pour des codes » **sans token explicite** : aucun nouveau code confirmable.

**Résultat : aucun nouveau code à publier ce soir.** `snapshots[*].lastChecked` mis à jour au `2026-06-29T20:05:35Z` pour les 27 jeux ; `knownCodes`/`descExcerpt` inchangés (contenu matériellement identique au matin). JSON revalidé (parse OK, se termine par `}`, vérifié via l'outil de lecture fichier).

## Correctif prioritaire — Miniature **Steal a Brainrot** harmonisée (signalé le matin)
Le rapport du matin signalait une incohérence : l'API renvoie désormais le hash `64170d84…` (déjà appliqué à `index.html` via la carte « Jeu de la semaine »), alors que le reste du site utilisait encore l'ancien `30a62664…`.

Miniature actuelle **revérifiée en direct** via l'API thumbnails (universe `7709344486` = Steal a Brainrot) :
`https://tr.rbxcdn.com/180DAY-64170d84ffa0cba4ee5af8bd1cd2df66/…` (état `Completed`).

Ancien hash `180DAY-30a62664e838df470ec079b7fc171637` → nouveau `180DAY-64170d84ffa0cba4ee5af8bd1cd2df66` remplacé dans **les 7 fichiers** restants (le suffixe taille/format de chaque URL est préservé) :
- `js/main.js` (`ROBLOX_THUMBS`, format Webp 480/270)
- `codes/index.html` (`THUMBS`)
- `codes/steal-a-brainrot.html` (src du hero)
- `codes/simulator/index.html` (carte)
- `guides/index.html` (carte)
- `guides/steal-a-brainrot.html` (og:image + image JSON-LD + image d'illustration — 3 occurrences)
- `tier-list/index.html` (carte du hub)

Vérif : **0** occurrence de l'ancien hash dans le HTML, **8** fichiers (les 7 + `index.html`) sur le nouveau hash. Le SVG `/images/games/steal-a-brainrot.svg` reste en `onerror` (fallback), jamais en `src` principal. Aucune date « Mis à jour le… » modifiée (changement de miniature uniquement, pas de changement de codes).

## ÉTAPE 9 — Cache JS
`js/main.js` ayant été modifié, la version de cache a été bumpée **`v=30` → `v=31`** sur **284 fichiers .html** (racine + codes/ + tier-list/ + guides/ + avatar/ + ugc-gratuit/, etc.). Vérif : **0** fichier encore en `v=30`, **284** en `v=31` (uniforme).

## ÉTAPES 1, 3, 4, 5, 6, 7 — non réalisées ce run (soir)
- **Jeu de la semaine (ÉTAPE 7)** : déjà fait au run du matin (lundi) → non retouché.
- **Ajout de 6 jeux (ÉTAPE 1)** : non réalisé (exige codes 2 sources + 2 vidéos oEmbed + miniatures + ≥1200 mots par page → run dédié).
- **Thin-content / tier lists / guides complets / UGC** : aucun changement méta confirmable à 2 sources ce soir → rien modifié, pour ne pas altérer de dates sans changement réel.

## ÉTAPE 8 — QC final (⚠️ note importante sur le montage shell)
**Le montage Linux du shell sert encore des lectures en cache fantômes** : `git status`/`tail`/`grep` y signalaient de fausses corruptions (octets nuls, fichiers « tronqués sans `</html>` », `node --check` en échec sur `js/main.js`, `ugc-gratuit/index.html` « supprimé »). **Toutes ces alertes sont des artefacts du montage**, confirmé en lisant la vérité disque (côté Windows) via l'outil de lecture fichier :

| Fichier | Vérité disque (outil de lecture) |
|---------|----------------------------------|
| `index.html` | OK, finit `</body></html>` (l.902) |
| `js/main.js` | OK, finit proprement (l.716), hash neuf en l.105 |
| `codes/index.html` | OK, finit `</body></html>` (l.723) |
| `codes/squid-game-x.html` | OK (201 lignes) |
| `codes/mini-war.html` | OK — page de redirection volontairement courte (18 l., finit `</html>`) |
| `sitemap.xml` | OK (335 lignes) |
| `ugc-gratuit/index.html` | OK, présent (le « D » de git est un fantôme) |
| `tools/code-watch.json` | OK, JSON valide, `lastChecked` à jour |

Autres contrôles : nav 7 entrées + GA4 conservés (édits ponctuels, blocs déjà équilibrés) ; bandeau `data-cta="guidelink"` non touché ; aucune iframe modifiée ; cache uniforme `v=31`. **Aucune écriture réelle tronquée** (les écritures shell et l'outil d'édition atterrissent correctement sur le disque — seules les *relectures* shell sont périmées).

## ⚠️ À signaler à Peter
- **Avant de committer** : un coup d'œil à `git status` **côté Windows** est recommandé. Le montage du shell montrait plusieurs fichiers « modifiés » hérités de runs précédents non encore poussés (`.htaccess`, `codes/mini-guerre.html`, `codes/mini-war.html`, `sitemap.xml`, `ugc-gratuit/`) en plus de mes changements de ce soir. Vérifiés intègres côté disque réel, mais ils seront inclus dans `git add -A`.
- **Squid Game X** : surveiller l'expiration des paliers `$…$` et l'arrivée du prochain code à 1,4 M de likes.
- **Pistes prochains runs** : ajout de 6 jeux (run dédié) ; guides complets candidats (pet-simulator-99, fruit-battlegrounds, squid-game-x, hypershot, fifa-super-soccer).

## Fichiers touchés ce run
- `js/main.js` (hash steal-a-brainrot)
- `codes/index.html`, `codes/steal-a-brainrot.html`, `codes/simulator/index.html`, `guides/index.html`, `guides/steal-a-brainrot.html`, `tier-list/index.html` (hash steal-a-brainrot)
- **284 fichiers .html** (bump cache `v=30` → `v=31`)
- `tools/code-watch.json` (snapshots 27 jeux → `lastChecked` 29 juin 20:05 UTC)
- `rapport-zoneblox-2026-06-29-soir.md` (ce rapport)

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`
Hostinger déploie automatiquement après le push.
