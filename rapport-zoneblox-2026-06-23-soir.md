# Rapport Zoneblox — mardi 23 juin 2026 (run du soir)

Run de maintenance autonome. Mardi → pas de mise à jour « Jeu de la semaine » (réservée au lundi). Priorité à la **justesse des codes** sur le volume.

## Étape 0 — Surveillance des codes (27 hotGames)

Descriptions in-game **live** des 27 jeux `hotGames` récupérées via l'API officielle (`games.roblox.com/v1/games`, requête groupée unique, exécutée dans Chrome — le shell n'a pas de réseau).

- **Aucun nouveau code candidat.** Les seuls codes concrets dans les descriptions restent ceux déjà snapshotés : `YOO1M110K` (Fruit Battlegrounds), `BOOM` (Merge a Nuke), `W7C28D` (BlockSpin), `$1M$` (Squid Game X). Les mentions « 25kLIKE = NOUVEAU CODE » (World Fighters), « Aimez pour des codes » (Anime Last Stand, VV: Ultimatum) n'exposent aucun code exploitable.
- `snapshots[*].lastChecked` rafraîchi au **2026-06-23T20:05:14Z** pour les 27 jeux (écriture `json.dump`). JSON revérifié valide, se termine par `}`, 27 hotGames / 27 snapshots.

## Étape 2 — Codes : vérifications croisées (2 sources)

### ✅ Anime Vanguards — mise à jour appliquée (page obsolète)

La page (datée du 19 juin) listait 13 codes « actifs » dont la plupart sont désormais expirés. Vérification sur **Pocket Tactics (maj 22 juin, source la plus fraîche)** + **Pro Game Guides** : les codes tournent en ~2 semaines.

- **Nouveau tableau « codes actifs » (7)** : `13.5`, `EternalAdversaries`, `Gambler`, `DMCAFree`, `Liberation`, `223`, `Cog5th`.
  - `DMCAFree`, `Liberation`, `223`, `Cog5th` → confirmés actifs par **les deux** sources.
  - `13.5`, `EternalAdversaries`, `Gambler` → nouveaux codes (Update « Eternal Adversaries »), confirmés par Pocket Tactics + l'agrégat multi-sources.
- **Déplacés en « ❌ Codes expirés »** (nouvelle section ajoutée) : `OopsiePoopsie`, `OopsiePoopsie2`, `HeHasArrived`, `BumBum`, `Spring26`, `SorryForAutoSell`, `TooMuchPain`, `ExtraWeek`, `Shinobi` (tous listés expirés par Pocket Tactics le 22 juin).
- `kat` **non publié** : annoncé « nouveau » par un agrégat mais classé *expiré* par Pocket Tactics → exclu par prudence.
- Compteurs « 10 codes actifs » → **7** ; date « Mis à jour le » et « Vérifié le » → **23 juin 2026** ; `dateModified` JSON-LD → `2026-06-23` ; `snapshots['anime-vanguards'].knownCodes` synchronisé sur les 7 actifs ; `<lastmod>` sitemap → `2026-06-23`.

### ✅ Volleyball Legends — vérifié, aucun changement

Les **9 codes** de la page (UPDATE_75, SPECTATING, SHOW_OFF, UPDATE_74, SEASON_16, SUMMER_UPDATE, UPDATE_73, JUNGLE_MAP, JUNE_2026) sont **tous confirmés actifs** par Pro Game Guides (maj 20 juin, qui en liste même davantage). Beebom est trop ancien (23 mai). **Aucune modification** — date inchangée (règle d'honnêteté).

## Étapes 1, 3, 4, 5, 6 — Ajouts / thin content / tier lists / guides / UGC

Pas d'ajout de jeux, de tier list, de guide ni de modification UGC ce run : l'ajout de 6 jeux exige un volume de vérifications (éligibilité, miniatures réelles, vidéos oEmbed, doubles sources) incompatible avec un run fiable centré sur la justesse des codes. Reporté à un run dédié. (Audit antérieur : les 156 pages codes dépassent 1200 mots — pas de thin content connu.)

## Étape 8 — QC

| Vérification | Résultat |
|--------------|----------|
| `node --check js/main.js` | OK ✓ |
| `tools/code-watch.json` valide / `}` final / 27-27 | ✓ |
| `codes/anime-vanguards.html` — GA4 / `main.js?v=27` / 1 `data-cta="guidelink"` / nav Avatars | ✓ |
| `codes/anime-vanguards.html` — équilibre `<div>` (disque réel) | 0 ✓ |
| `codes/anime-vanguards.html` — fin réelle `</body></html>` (L175-176) | ✓ |
| `sitemap.xml` se termine par `</urlset>` | ✓ |
| Octets nuls (fichiers modifiés) | 0 ✓ |

> **Note technique récurrente** : le mount bash sert par intermittence des **copies cache tronquées**. Exemple ce run : `tail` bash signalait `codes/mini-war.html` à 106 lignes sans `</html>` et un déséquilibre `<div>` de 1 sur index.html / mini-war.html / volleyball-legends.html. Vérifié via l'outil fichier (disque réel) : `mini-war.html` fait **111 lignes** et se termine bien par `</html>`. Ce sont des faux positifs de cache, pas des troncatures réelles. Les seuls fichiers édités ce run (anime-vanguards.html, code-watch.json, sitemap.xml) sont complets et valides.

## Fichiers touchés ce run
- `codes/anime-vanguards.html` — refonte tableau codes actifs (7), nouvelle section expirés (9), compteurs + dates + JSON-LD
- `tools/code-watch.json` — 27 `lastChecked` rafraîchis + `knownCodes` Anime Vanguards synchronisé
- `sitemap.xml` — `<lastmod>` Anime Vanguards → 2026-06-23
- `rapport-zoneblox-2026-06-23-soir.md` — ce rapport

*(Restent aussi en attente de commit, hérités de runs précédents non encore poussés : `codes/grow-a-garden.html`, `codes/grow-a-garden-2.html`, `codes/index.html`, `codes/mini-war.html`, `codes/simulator/index.html`, `codes/volleyball-legends.html`, `guides/grow-a-garden-2.html`, `guides/index.html`, `index.html`, `js/main.js`, `tier-list/grow-a-garden-2.html`, `tier-list/index.html`, + rapports 06-22-soir / 06-23.)*

## À étoffer aux prochains runs
- Ajout de 6 nouveaux jeux (≥4000 joueurs) — run dédié.
- Re-vérifier Anime Vanguards sous ~10 jours (codes expirent vite).

## Pour publier
Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push. *(Si un `index.lock` bloque le commit : `del .git\index.lock` d'abord.)*
