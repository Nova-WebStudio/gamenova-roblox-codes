# Rapport Zoneblox — lundi 22 juin 2026 (run du soir)

Complément au run du matin (`rapport-zoneblox-2026-06-22.md`). Le « Jeu de la semaine » et les codes Volleyball Legends / Mini War avaient déjà été traités ce matin ; ce run du soir corrige le point de suivi laissé en attente (miniature GAG2) et rafraîchit la surveillance.

## Réparation préalable (BLOCAGE résolu) — `tools/code-watch.json`

Le fichier `tools/code-watch.json` était **tronqué** dans l'arbre de travail (coupé en pleine chaîne à la ligne 459, snapshot `100-days-at-sea`) — séquelle d'une écriture interrompue du run précédent, malgré le rapport du matin qui l'annonçait valide.

- La version **committée (HEAD)** était, elle, **complète et valide** (27 hotGames / 27 snapshots, tous au timestamp du matin).
- Restauré depuis HEAD (`git show HEAD:tools/code-watch.json > tools/code-watch.json`). Re-parse JSON **OK**, se termine par `}`, 27/27. Aucune donnée perdue (l'arbre de travail tronqué ne contenait que les mêmes données du matin, coupées).

## Étape 2 / suivi — Miniature Grow a Garden 2 synchronisée (point en attente résolu)

Le run du matin avait mis le **nouveau hash** dans la bannière d'accueil mais laissé les autres fichiers sur l'**ancien hash** `d3506c96…`, en reportant la propagation.

Vérification rigoureuse via l'API officielle Roblox (Chrome, le shell n'a pas de réseau), en appliquant la règle CLAUDE.md « toujours vérifier que l'universeId correspond au BON jeu » :

- ⚠️ Piège évité : l'universe `7436755782` du code-watch (slug `grow-a-garden`) est **« [🔥] Grow a Garden 🌶️ »**, le jeu **original** — PAS Grow a Garden 2. Sa miniature (`b1a54c3e…`) ne concerne donc pas GAG2.
- Le bon universe de **Grow a Garden 2** est **`10200395747`** → API : nom « Faites pousser un jardin 2 / Grow a Garden 2 », créateur **Strawberreh Squad** (badge vérifié), **507 304 joueurs** en simultané. Confirmé.
- Sa **vraie miniature live actuelle** = `tr.rbxcdn.com/180DAY-71ae7859135fc45f2a0e6d580572d5c0` → **identique au hash que le run du matin avait mis dans la bannière**. La bannière était donc correcte ; c'étaient les 8 autres fichiers qui étaient en retard.

Propagation de `d3506c96…` → `71ae7859…` (hash vérifié) dans les **8 fichiers** concernés :
`js/main.js` (ROBLOX_THUMBS), `codes/index.html` (THUMBS), `codes/grow-a-garden-2.html` (hero), `codes/simulator/index.html`, `guides/grow-a-garden-2.html`, `guides/index.html`, `tier-list/grow-a-garden-2.html`, `tier-list/index.html`. Plus aucune occurrence de l'ancien hash dans le code (vérifié sur le disque réel) ; il ne subsiste que dans les rapports (texte historique).

> **Cache JS** : pas de bump nécessaire. `js/main.js` n'a vu qu'un changement de **contenu** (URL de miniature) ; la version `v=27` est déjà universelle (committée, non encore déployée). Les clients récupéreront `main.js?v=27` à jour au prochain push de Peter. Bumper vers v28 toucherait 266 fichiers sans bénéfice (v27 pas encore servie aux navigateurs).

## Étape 0 — Surveillance des codes (re-vérification du soir)

Descriptions in-game **live** des **27 jeux** `hotGames` re-récupérées via l'API officielle (`games.roblox.com/v1/games`, requêtes groupées).

- **Aucun nouveau code candidat.** Les seuls codes présents dans les descriptions restent ceux déjà connus/snapshotés : `YOO1M110K` (Fruit Battlegrounds), `BOOM` (Merge a Nuke), `W7C28D` (BlockSpin), `$1M$` (Squid Game X). Les mentions type « 25kLIKE = NOUVEAU CODE » (World Fighters), « Aimez pour des codes » (Anime Last Stand, VV: Ultimatum) n'exposent aucun code concret.
- `snapshots[*].lastChecked` rafraîchi au **2026-06-22T20:08:40Z** pour les 27 jeux via un round-trip `json.dump` (écriture atomique — évite la troncature qui avait corrompu le fichier). JSON re-vérifié valide, se termine par `}`, 27/27, propagé sur le disque réel (27 timestamps confirmés via l'outil fichier).

## Étapes 1, 3, 4, 5, 6 — Ajouts / contenu / tier lists / guides / UGC

Pas d'ajout de jeux ni de nouveaux guides/tier lists ce run du soir (le run du matin avait déjà fait le gros œuvre, et l'ajout de 6 jeux demande un volume de vérifications incompatible avec un complément de soirée fiable). Priorité donnée à la **justesse** : réparation du fichier de surveillance corrompu + cohérence de la miniature du jeu de la semaine.

## Étape 8 — QC

| Vérification | Résultat |
|--------------|----------|
| `node --check js/main.js` | OK ✓ |
| `tools/code-watch.json` valide / `}` final / 27-27 | ✓ |
| Tous les HTML modifiés finissent par `</html>` | ✓ (disque réel : index.html L892, mini-war L111, volleyball-legends L212, + 8 fichiers édités) |
| Octets nuls (12 fichiers modifiés) | 0 partout ✓ |
| Équilibre des `<div>` (7 fichiers édités) | 0 partout ✓ |
| Ancien hash `d3506c96` dans le code | 0 (uniquement dans les rapports) ✓ |
| Cache JS `main.js?v=27` | uniforme, 266 fichiers ✓ |
| Miniature GAG2 = vraie URL `tr.rbxcdn.com` vérifiée | ✓ (universe 10200395747 confirmé) |

> **Note technique (récurrente)** : le **mount bash du sandbox sert par intermittence des copies en cache** des fichiers édités via les outils fichier — `tail` y montrait à tort 3 fichiers « sans `</html>` ». Les outils fichier (Grep/Read), qui lisent le **disque réel**, ont confirmé que les 3 fichiers sont complets. Les écritures faites par bash ce run (8 fichiers + code-watch.json) ont, elles, bien été propagées au disque réel (re-vérifié via l'outil fichier).
>
> ⚠️ **`.git/index.lock` (0 octet)** : un fichier-verrou résiduel est apparu dans le `.git` du sandbox et n'a pas pu être supprimé (permission refusée côté bac à sable). `git status` fonctionne normalement. **Si** `git commit` se plaint d'un `index.lock`, supprime-le manuellement : `del .git\index.lock` (Windows) avant de committer.

## Fichiers touchés ce run du soir
- `tools/code-watch.json` — restauré (troncature) + 27 `lastChecked` rafraîchis
- `js/main.js`, `codes/index.html`, `codes/grow-a-garden-2.html`, `codes/simulator/index.html`, `guides/grow-a-garden-2.html`, `guides/index.html`, `tier-list/grow-a-garden-2.html`, `tier-list/index.html` — miniature GAG2 (`d3506c96…` → `71ae7859…`)
- `rapport-zoneblox-2026-06-22-soir.md` — ce rapport

(Restent aussi en attente de commit, hérités du run du matin : `index.html`, `codes/mini-war.html`, `codes/volleyball-legends.html`.)

## Pour publier
Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push. *(Si un `index.lock` bloque le commit : `del .git\index.lock` d'abord.)*
