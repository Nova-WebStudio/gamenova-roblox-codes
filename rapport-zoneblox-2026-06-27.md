# Rapport Zoneblox — 27 juin 2026 (samedi)

> Run de maintenance automatique. Samedi → pas de mise à jour « Jeu de la semaine » (réservée au lundi).

## État général du site (sain)
- **285 fichiers HTML** : tous se terminent par `</html>`, **0 octet nul réel** (vérifié via Python — le scan `grep` remonte des faux positifs sur ces fichiers, ignorer), balises `<div>` équilibrées partout.
- **157 jeux** au catalogue : `GAMES_INDEX` ↔ `ALL_GAMES` parfaitement synchronisés (0 écart dans les deux sens).
- `node --check js/main.js` : OK.
- `sitemap.xml` valide (se termine par `</urlset>`).
- Cache JS uniforme : **`main.js?v=29`** sur les 285 pages (aucun écart).
- Audit thin-content : **0 page codes sous 1200 mots** (les 158 pages codes passent le seuil d'indexation ; seule `codes/index.html`, page de listing, est courte — normal).

## ÉTAPE 0 — Surveillance des codes (27 jeux « hotGames »)
Descriptions in-game + métadonnées des **27 jeux** récupérées en direct via l'API Roblox officielle (`games.roblox.com/v1/games`, exécutée dans Chrome car le shell n'a pas d'accès réseau). Codes potentiels extraits des descriptions et comparés aux snapshots + pages :

| Jeu | Code dans la description in-game | Statut |
|-----|----------------------------------|--------|
| fruit-battlegrounds | `YOO1M110K` | déjà publié ✓ |
| blockspin | `W7C28D` | déjà publié ✓ |
| merge-a-nuke | `BOOM` | déjà publié ✓ |
| squid-game-x | « 1,2 million de dollars » (nouveau palier) | **en attente** ⏳ |

**Changement détecté — Squid Game X :** la description officielle a été mise à jour. L'ancien snapshot annonçait `$1M$` (« prochain gros code à 1,2 M de likes ») ; la description actuelle promeut désormais le **nouveau code « 1,2 million de dollars »** et tease le suivant à 1,4 M de likes (Saison 3, nouveaux modes Sky Squid / Cache-cache / Corde à sauter / Dîner final, V11.0.0).

Le token exact de ce nouveau code suit vraisemblablement le motif `$1.2M$`, mais **il n'a pas pu être confirmé par une 2ᵉ source fiable** (les agrégateurs consultés se contredisaient : « VALENTINES » / « aucun code actif »). Conformément à la règle d'honnêteté (jamais publier un candidat non confirmé à 2 sources OU par token in-game exact), **ce code n'a PAS été ajouté à la page**. Il est enregistré comme `pendingCandidate` dans `code-watch.json` pour vérification au prochain run.

> Les autres jeux populaires (blox-fruits, grow-a-garden, king-legacy, fisch, blue-lock-rivals, etc.) renvoient « rejoignez le groupe / aimez pour des codes » sans token explicite dans la description : aucun nouveau code confirmable côté in-game.

Snapshots des **27 jeux** mis à jour (`lastChecked` au 27 juin 2026 ; `descExcerpt`/`descLen` de squid-game-x rafraîchis). JSON revalidé : se termine par `}`, parse OK.

## ÉTAPE 2 — Codes (vérification 2 sources)
Vérification croisée des jeux les plus populaires via la source la plus autoritaire (description in-game live) + recherche web. **Aucun changement de code confirmable à 2 sources ce run** : les pages refreshées la veille (king-legacy, grow-a-garden le 26 juin) restent exactes, et aucun nouveau code vérifié n'est apparu. Rien n'a été modifié pour éviter d'altérer des dates « Mis à jour le… » sans changement réel.

## ÉTAPE 1 — Ajout de jeux
Non réalisé ce run. L'ajout de 6 jeux complets exige des codes vérifiés à 2 sources fiables **et** 2 vidéos YouTube vérifiées par oEmbed **et** miniatures `tr.rbxcdn.com` — or les agrégateurs de codes consultés depuis cet environnement se sont révélés peu fiables/contradictoires. Par respect de la règle « jamais inventer codes/vidéos/miniatures », j'ai préféré ne rien ajouter plutôt que de publier du contenu non vérifié. **À reprendre sur un run dédié** (budget + vérifications navigateur approfondies).

## ÉTAPES 3-6 — Guides / tier lists / UGC
- Thin-content : tout le catalogue codes est déjà ≥ 1200 mots → aucune mise à niveau prioritaire requise.
- Aucune création de guide/tier list ce run (pas de nouveau jeu ajouté ; pas de changement méta confirmé nécessitant une refonte).

## ÉTAPE 7 — Jeu de la semaine
Samedi (`date +%u` = 6) → **non modifié** (réservé au lundi).

## ÉTAPE 9 — Cache JS
`js/main.js` **non modifié** ce run → pas de bump de version (reste `v=29`, uniforme).

## ÉTAPE 8 — QC final
- Aucune page HTML modifiée ce run (seul `tools/code-watch.json` a changé).
- Intégrité globale revérifiée : `</html>`, divs, octets nuls, `node --check`, sitemap, sync catalogue, cache JS → **tout vert**.
- `tools/code-watch.json` : JSON valide, se termine par `}`.

## ⚠️ À signaler / pistes prochains runs
- **Squid Game X** : confirmer le token exact du nouveau code « 1,2 million de dollars » (probable `$1.2M$`) dès qu'une 2ᵉ source fiable le publie, puis l'ajouter et vérifier si `$1M$` est passé expiré.
- **Anime Last Stand** : seulement ~254 joueurs en live (vs >4000 attendu) — jeu en perte de vitesse, à surveiller pour la pertinence de la surveillance hotGames.
- **Ajout de 6 jeux (ÉTAPE 1)** : à planifier sur un run dédié avec vérification navigateur complète (codes 2 sources, vidéos oEmbed, miniatures tr.rbxcdn.com).

## Fichiers touchés
- `tools/code-watch.json` (snapshots des 27 hotGames + candidat en attente squid-game-x)
- `rapport-zoneblox-2026-06-27.md` (ce rapport)

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`
Hostinger déploie automatiquement après le push.
