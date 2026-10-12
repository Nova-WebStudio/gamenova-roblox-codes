# Rapport ZoneBlox — 2026-10-05 (run 05h, lundi, full maintenance + editorial)

Fenêtre de veille : nuit 04/10 15h → 05/10 05h (+ codes 12-24 h). Mode autonome, aucune décision risquée prise ; les points incertains sont laissés « à vérifier » et notés.

## CODES
- **hotGames** revérifiés : blue-lock-rivals (3, PGG 04/10 ✔ ; GamesRadar lag écarté), grow-a-garden (2, Beebom 01/10 ✔), steal-a-brainrot (1, GamesRadar 02/10 ✔), anime-vanguards (3 ✔), volleyball-legends (**rotation, voir ci-dessous**).
- **Codes ajoutés / modifiés** :
  - **volleyball-legends 3 → 4** — Update 90 (3 sources : PGG 03/10 + Fossbytes 04/10 + RoCodes 05/10). +UPDATE_90, SKELETON_BUNDLE, JINX, SLOT_REWORK ; −UPDATE_89, WE_CURSED, SKELETON (expirés).
  - **pressure 4 → 3** — −YOURTAKINGTOOLONG, −MiserableLaunchOnceAgain (expirés, Beebom + Pocket Tactics) ; +Gullible (code piège −300 Kroner).
  - **war-tycoon 4 → 6** — +Boom, +Wiki200K (Beebom 01/10 + The Click 29/09).
- **Codes expirés retirés** : UPDATE_89/WE_CURSED/SKELETON (volleyball), YOURTAKINGTOOLONG/MiserableLaunchOnceAgain (pressure).
- **Candidats en attente (conflit / source unique)** : anime-vanguards 2ndAnniDay1 (2 sources actives vs 1 expiré) & 100thTournament (1 source) ; clover !wspainplusdelay (1 source) ; war-tycoon New Map!/Mega (1 source) ; survive-the-killer MINING (contradictoire).
- **Sources officielles** : aucun Trello/X officiel exploitable neuf cette nuit sur les hot games prioritaires (rotation confirmée par agrégateurs croisés).
- **QC codes** : 5 compteurs « N codes actifs » du hero resynchronisés avec les chips (désync laissée par le run 04/10) : anime-spirits, anime-squadron, anime-vanguards, blue-lock-rivals, case-simulator-rng.

## SEO
- **Tendance détectée** : aucune à transformer en cluster (nouveaux jeux d'octobre sans traction mesurable au 01/10).
- **Cluster travaillé** : aucun (update-before-create → aucune nouvelle URL justifiée).
- **Anti-cannibalisation / intention** : respectée — rotation Update 90 traitée en UPDATE de la page existante, jamais en nouvelle URL.
- **Prochaine brique** : grosses listes de codes (autorité topicale) à fiabiliser avant toute expansion.

## NOUVEAUX JEUX
- Aucun ajouté. Candidats observés (Prime Heroes, Octane, Starforged, Scrapbook Saga) : **aucun dans le top joueurs/trending Roblox au 01/10** → pas de preuve d'intérêt réel → kill switch.

## CONTENU
- Guides : aucun créé/modifié (rien de justifié).
- Tier lists : aucune modification (pas d'évolution méta avérée).
- Articles : aucun (kill switch éditorial).
- Mises à jour : 3 pages codes (volleyball-legends, pressure, war-tycoon) + 16 pages « Vérifié le » rafraîchies ; carte Aniimo de l'accueil corrigée.

## ANIIMO
- 15 codes actifs confirmés exacts (GamesRadar 01/10). lastChecked → 05/10. Régénéré via build_site.py.
- **Fix structurel** : `tools/build_home.py` avait la carte Aniimo d'accueil **hardcodée** (« 11 codes / 28 sept. ») → rendue dynamique (lecture de `data/aniimo/codes.json`), affiche maintenant 15 codes / 5 oct.

## GTA 6
- CONFIRMÉ : sortie **19 novembre 2026**. 05/10 = feature magazine **Love** (promo). RAPPORTÉ/RUMEUR : aucun trailer 3 daté. → page evergreen à jour, **aucune nouvelle URL**.

## FC 27
- Live en octobre 2026 = **EA Sports FC 26** (ambiguïté FC26/FC27 non tranchée). Aucune action — à clarifier avec Peter.

## EDITORIAL INTELLIGENCE
- Top opportunités : aucune nouvelle (confiance insuffisante / traction absente).
- Tendances : overnight calme, pas de breakout.
- Articles créés : 0. Pages mises à jour : 3 codes + Aniimo accueil.
- Sujets ignorés : nouveaux jeux d'octobre (pas de signal), GTA6 Love mag (promo), FC (ambigu).
- Sujets à surveiller : grosses listes codes, 2ndAnniDay1, breakout nouveaux jeux.
- `editorial-intelligence.json` : meta → 05/10, +1 topic maint-2026-10-05, dates GTA6/FC/Aniimo/fall-games/steal-a-brainrot bumpées.

## EDITORIAL QUEUE
- Urgents : veille annonce officielle GTA 6.
- À publier : rien (kill switch).
- À mettre à jour : grosses listes (anime-astral-simulator, dragon-blox, anime-battle-rng) — **reportées, priorité absolue prochain run** ; conflits 2ndAnniDay1 / clover / restaurant-tycoon-3 / untitled-aot.
- À préparer : FC périmètre (Peter), CTA §28.
- Demain : hotGames + grosses listes + conflits (voir EDITORIAL-QUEUE.md).

## QC
- Fichiers : 36 HTML modifiés — tous `</html>`, 0 null byte, div équilibrés, GA4 présent, CTA unique. /avatar/ non touché. 3 fichiers /avatar/ restent en `main.js?v=43` (gelé, hors périmètre) ; reste du site en `v=47`.
- Tests : `node --check js/main.js` OK ; 5 JSON valides (codes, games-index, code-watch, editorial-intelligence, aniimo) ; `sitemap.xml` well-formed, finit par `</urlset>`.
- Builds : build_site → build_home → build_codes_json (**1271 codes / 184 jeux**) → build_sitemap (**383 URLs**), dans l'ordre.
- Erreurs corrigées : désync des 5 compteurs hero ; carte Aniimo accueil hardcodée.

---

Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
