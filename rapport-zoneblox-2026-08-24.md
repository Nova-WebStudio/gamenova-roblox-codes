# Rapport Zoneblox — 24 août 2026 (lundi)

## (a) Codes vérifiés (priorité absolue)

**Portée :** arbre **servi** `codes-<slug>.html` (les `codes/<slug>.html` restent 301-redirigés → gelés). Jeux chauds revérifiés via web (≥3 sources) et/ou sources officielles (API Roblox, shout de groupe, Trello).

| Jeu | Source(s) | Verdict |
|---|---|---|
| **Anime Vanguards** | GamesRadar + PC Gamer + PGG | **CHANGEMENT** : `2BVisits` **expiré le 23/08** (confirmé GamesRadar) → retiré de la liste active servie (**6 → 5 codes**). `Miniupdate1` encore listé actif par PGG malgré le label 23/08 → conservé par prudence. |
| Grow a Garden | Beebom (04/08) + PCGamesN (15/08) + X officiel | `RDCAward` + `BEANORLEAVE10` = set servi confirmé actif → **inchangé** |
| Grow a Garden 2 | Beebom, G2A, PC Gamer, GamesRadar | `TEAMGREENBEAN / WATERYOPLANTS / REMEMBERTODRINKWATER` confirmés → inchangé. `FREESEED` (annoncé « NOUVEAU » par Beebom/G2A) **non confirmé** par recherche ciblée → **non publié (prudence)**, gardé en `pending` dans code-watch.json. |
| Steal a Brainrot | Beebom (1 code, 22/08) vs autres (23) | Conflit fort persistant → set servi `BESTBRAINROTEVER` conservé (prudence) → inchangé |
| Blox Fruits | PC Gamer, PCGamesN, Dexerto | Aucun nouveau code depuis la MAJ PVP ; set evergreen stable → inchangé |
| Blade Ball | GamesRadar, Pocket Tactics, Skycoach | Comptes en conflit (14 vs 24) ; set servi (13) → inchangé par prudence |

**« 🔄 Vérifié le » rafraîchi au 24 août 2026 sur les 177 pages servies** (idempotent, 1 par page ; inclut la nouvelle fiche).

**Étape 0 (sources officielles) :** résolution + vérification via Chrome (API Roblox) du nouveau hit **Steal An Egg** (universeId 10563114921 confirmé = « Steal An Egg », groupId 825735094, shout = null → aucun code). Snapshot de référence enregistré dans `tools/code-watch.json`.

**Candidats / à prioriser prochain run :** GAG2 `FREESEED` (en attente, à reconfirmer) ; Steal a Brainrot (conflit à re-surveiller) ; Anime Origins (à ficher avec Chrome, report du 23/08).

## (b) Directeur SEO (ÉTAPE 2bis) — trending-first

**Trending re-scanné (web, multi-sources) :** détection d'un **nouveau hit majeur NON couvert** → **Steal An Egg** (créé le 25/07/2026, ~496K–724K joueurs simultanés selon les trackers, 284M visites, genre Simulation/Tycoon). Conforme à la règle « un vrai nouveau hit ≥4000 joueurs passe DEVANT l'evergreen ».

**Brique réalisée (ÉTAPE 1) :** nouvelle fiche **`codes-steal-an-egg.html`** (~1 650 mots FR).
- **Honnêteté codes :** le jeu **n'a pas de système de codes public** (PGG 17/08 + description in-game + shout du groupe créateur null). La page l'affiche clairement (« Aucun code public ») sans rien inventer, et explique où les codes apparaîtraient s'ils existaient.
- **Intention distincte** (« codes Steal An Egg », « Steal An Egg a-t-il des codes ») ; aucune cannibalisation (jeu absent du catalogue jusqu'ici).
- **Contenu :** « C'est quoi », « Comment jouer » (biomes, gardiens, vitesse/treadmill, éclosion, revenu/s, fusion 3→1, mutations, vol PvP), `<h3>Guide de progression Steal An Egg</h3>` + 8 astuces, **2 vidéos réelles vérifiées oEmbed** (CHALLS `8d7Qrz7jDrU`, Radex Tips `aTV1JJpHUXY`), « Où trouver les codes », À propos + 3 similaires, FAQ 4 Q. Schema **BreadcrumbList + FAQPage**.
- **Miniature réelle** tr.rbxcdn.com + SVG fallback créé.
- **Maillage (anti-orphelin) :** carte `tous-les-codes.html` + objet `index.html` (GAMES) + `js/main.js` (GAMES_INDEX + ROBLOX_THUMBS + ROBLOX_UNIVERSE_IDS) + `<url>` `sitemap.xml` + redirect `.htaccess`.

**Prochaine brique inscrite dans la roadmap (J17) :** (1) **tier list Steal An Egg** (pets/œufs/biomes par revenu/s) ; (2) guide complet Steal An Egg ; (3) ficher Anime Origins.

## (c) Autres maintenances

- **Jeu de la semaine (lundi) :** bannière `FEATURED-WEEK` d'`index.html` basculée de Grow a Garden 2 → **Steal An Egg** (le phénomène du moment), miniature réelle + blurb FR + boutons « Voir la fiche » / « Tous les codes ».
- **Encart évènements :** `data/events.json` → `meta.updated` au 24/08/2026. Aucune date ponctuelle passée à purger, aucune heure d'admin abuse confirmée à promouvoir (honnêteté). `js/events.js` inchangé → pas de bump events.
- **UGC, tier lists, guides existants :** pas de changement requis ce run.

## (d) Fichiers touchés & QC

**Modifiés (~512 fichiers suivis) :** 177 pages servies `codes-*.html` (« Vérifié le » ; + `codes-anime-vanguards.html` code retiré), **bump cache `main.js?v=37 → v=38` sur les 326 HTML**, `index.html` (featured + GAMES), `tous-les-codes.html` (carte), `js/main.js` (3 objets), `sitemap.xml`, `.htaccess`, `data/events.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`.
**Nouveaux :** `codes-steal-an-egg.html`, `images/games/steal-an-egg.svg`, ce rapport.

**QC (tout vert) :**
- Scan d'intégrité sur les **506 fichiers HTML/XML** modifiés/nouveaux : **0 null byte**, toutes les pages finissent par `</html>`, sitemaps par `</urlset>`, **équilibre `<div>` intact** (0 déséquilibre).
- `node --check js/main.js` et `node --check js/events.js` OK ; `data/events.json` et `tools/code-watch.json` = JSON valide.
- Cache JS **uniforme v=38** (0 page restée en v=37, 326 refs).
- Nouvelle fiche : 1 650 mots FR (> 1 200), GA4 présent, nav (Avatars inclus), 2 JSON-LD valides, 2 iframes oEmbed vérifiées (aucun `dQw4w9WgXcQ`), miniature tr.rbxcdn.com, canonical/og cohérents, ROBLOX_THUMBS/THUMBS/UNIVERSE_IDS synchronisés.

## Pour publier

Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.

Sources : [PGG Anime Vanguards](https://progameguides.com/roblox/anime-vanguards-codes/) · [GamesRadar Anime Vanguards](https://www.gamesradar.com/games/strategy/anime-vanguards-codes/) · [Beebom Grow a Garden](https://beebom.com/roblox-grow-a-garden-codes/) · [Beebom Grow a Garden 2](https://beebom.com/grow-a-garden-2-codes/) · [PGG Steal An Egg](https://progameguides.com/roblox/steal-an-egg-codes/) · [Rolimon's Steal An Egg](https://www.rolimons.com/game/107778070777162)
