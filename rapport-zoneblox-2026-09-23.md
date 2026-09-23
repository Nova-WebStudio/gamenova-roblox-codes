# Rapport ZoneBlox — 2026-09-23 (run 05h, full maintenance)

Run complet du matin (mercredi, hors « jeu de la semaine »). Exactitude > fraîcheur : les changements de codes ne sont appliqués qu'avec ≥2 sources datées concordantes ou 1 source officielle ; en cas de conflit/ambiguïté, aucune modification (flag « à revérifier »).

## CODES

### hotGames vérifiés (7)
| Jeu | Résultat |
|-----|----------|
| **volleyball-legends** | **MODIFIÉ** — Update 88 : actifs = UPDATE_88, GET_SLIMED (5 Lucky Style Spins), XP_BOOST (potion 2x XP). UPDATE_87 / RONIN_RETURN / KATANA → expirés. Sources : Beebom (19 sept) + Roonby/GamesRadar. |
| **anime-vanguards** | **MODIFIÉ** — ajout de 100thTournament (100 Trait Rerolls, niv. 10) → 4 codes actifs. Sources : Pro Game Guides (18 sept) + agrégat. |
| grow-a-garden | Inchangé (RDCAward, BEANORLEAVE10). Confirmé Beebom (1 sept) + PCGamesN. « Vérifié le » rafraîchi. |
| steal-a-brainrot | Inchangé (0 actif). Confirmé PCGamesN (pas de système de codes). |
| blue-lock-rivals | Inchangé (3 codes gardés). Snapshots sources divergents (rotation ~2 j) → à revérifier. |
| fruit-battlegrounds | Inchangé (HIGHER1M120K, YOO1M110K!) — nos 2 codes = les « NEW » actuels. |
| squid-game-x | Inchangé (6 codes) — aucune preuve de changement. |

### Rotation (10 pages)
- **Confirmées à jour** (date rafraîchie, aucun code modifié) : blockspin (2 codes-tête = « latest », Insider Gaming/PGG), illegal-soccer (aucun système de codes — confirmé), defend-ur-base-with-anime (nos 8 codes tous dans la liste active, dont UPDATE11), merge-a-nuke (DELAY, BOOM — exact), 1-aura-per-click (aucun code confirmé).
- **À revérifier** (non modifiées) : grimoires-era (sources périmées), locked (ambiguïté LOCKED vs LOCKED 2), my-gym (nom ambigu), catch-a-monster (sources contradictoires/périmées), fifa-super-soccer (conflit codes-nom, voir ci-dessous).

### Codes ajoutés
- anime-vanguards : **100thTournament**.
- volleyball-legends : **UPDATE_88**, **GET_SLIMED**, **XP_BOOST**.

### Codes expirés (retirés des actifs)
- volleyball-legends : UPDATE_87, RONIN_RETURN, KATANA.

### Candidats en attente / non publiés (règle 2 sources ou conflit)
- **Grow a Garden — FREESEED** (event The Hunt: Roblox 20) : source unique (PGG 17 sept) → surveillance, non publié. STORY/STARBUD (PGG, récompenses graines) suspects → ignorés. torigate reste expiré (2 sources).
- **fifa-super-soccer — bestfootball / fifasupersoccer** : Insider Gaming (2 sept) les dit « latest active », mais notre page (vérif 20/09, plus récente) les a déjà classés expirés. Conflit non résolu → non réactivés.
- **catch-a-monster — stowerbug / stellawolf / nexa** : source unique → non ajoutés.

### Sources officielles
Trello/Discord/X officiels consultés indirectement via agrégateurs datés (Beebom, Pro Game Guides, Insider Gaming, PCGamesN, GamesRadar, Roonby). Aucun changement sur les codes Trello-privés (blade-ball, blue-lock-rivals) non tranché faute de source datée fraîche concordante.

## SEO
- Aucune nouvelle URL créée (kill switch éditorial : rien ne réunit confirmation + valeur joueur + absence de doublon).
- Update-before-create respecté : Aniimo mis à jour sur les URLs existantes ; FC 27 réservé au run du 26 sept. (post-lancement).
- Brique roadmap J36 (généralisation CTA `data-cta="guidelink"` aux pages codes non-hotGames) : à poursuivre — plusieurs pages (squid-game-x, blockspin, defend-ur-base, merge-a-nuke, 1-aura-per-click) n'ont pas encore le bandeau. Non traité ce run (hors changement de codes), noté pour un run dédié.

## NOUVEAUX JEUX
Aucun ajouté. Mode conquête : pas d'ajout sans preuve d'intérêt réel + codes réels.

## CONTENU
- Guides / tier lists / articles : aucun nouveau (qualité > quantité).
- Mises à jour : Aniimo (données + pages générées).

## ANIIMO
- `codes.json` : `lastChecked`→23 sept ; 9 badges `new:true` périmés remis à `false` ; set de 11 codes conservé (léger écart source unique aniimoparty/aniimofreetoplay laissé tel quel, à recouper).
- `creatures.json` : ajout de **Prismana Glynsera** (Nova, Lumière/Glace, DPS ; event Vein Abundance 21→27 sept, apparaît à Beast Fang Ridge via Prismana Flow). Sources : game8 + mobalytics. Page `/games/aniimo/creatures/prismana-glynsera/` générée + liée au hub.
- `build_site.py` relancé.

## GTA 6
Sortie **19 nov. 2026** toujours confirmée (reveal Netflix 21 sept, ~27 min gameplay near-final). Actus marketing (DualSense édition GTA VI, système relation Lucia/Jason, NDA cast rappelées) = faible valeur joueur → evergreen inchangé, MONITOR.

## FC 27
J-2 avant sortie (25 sept.). Aucun contenu spéculatif ajouté. Gros UPDATE (Ones to Watch, Destined for Glory, TOTW 1-2, SBC d'accès anticipé) prévu au **run 05h du 26 sept.** (post-lancement) sur `data/fc-27/updates.json`.

## EDITORIAL INTELLIGENCE
- **Top opportunité / tendance détectée** : **Roblox Fall Games 2026** (annonce officielle) — 6 nouveaux jeux dont **Showdown** (FPS anime), Monster in the Mansion, GOAT Football League, Nemesis, Fossil Force, Caramel. Ajouté en MONITOR (trendScore ~55/100). Pas de page créée (traction/intention SEO non prouvées).
- **Sujets mis à jour** : aniimo-codes-sep2026 → UPDATED ; gta6-release-nov19 → re-vérifié.
- **Sujets ignorés** : actus marketing GTA 6 (faible valeur joueur).
- **À surveiller** : Roblox Everywhere (déploiement joueur), Steal An Egg (ajout éventuel de codes), blue-lock-rivals (rotation rapide).

## EDITORIAL QUEUE
- Urgents : aucun.
- À publier : aucun.
- À mettre à jour : FC 27 (post-lancement, run 26 sept).
- À préparer / surveiller : Roblox Fall Games (Showdown), GTA 6 marketing, Roblox Everywhere.
- À revérifier (codes) : fifa-super-soccer, catch-a-monster, locked/LOCKED 2, my-gym, grimoires-era, blue-lock-rivals, type-soul/sailor-piece/character-rng/broken-blade.
- Demain (24 sept) : rotation des slugs jamais vérifiés restants + trancher les « à revérifier » + trend-scan Showdown.

## QC
- `build_site` / `build_home` / `build_codes_json` (183 jeux, 1224 codes actifs) / `build_sitemap` (381 URLs) / `sync_month` (0 page — déjà septembre) exécutés dans l'ordre.
- HTML modifiés : tous se terminent par `</html>`, 0 null byte, div équilibrés (0 déséquilibre sur tout le site), GA4 présent.
- JSON valides (codes.json, aniimo/*, code-watch.json, editorial-intelligence.json) ; sitemap.xml valide (`</urlset>`) ; `node --check js/main.js` OK.
- Cache JS : `main.js?v=43` cohérent sur les 167 fichiers concernés (note : le CLAUDE.md mentionne encore `v=19`, valeur périmée — le site est en réalité homogène en v=43).
- Compteurs « X codes actifs » mis à jour par remplacement littéral (volleyball 3, anime-vanguards 4) — aucun compteur cosmétique RELATED touché.

---

Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
