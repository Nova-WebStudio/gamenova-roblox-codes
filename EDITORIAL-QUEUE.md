# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json`.
> **Dernière MAJ : 2026-09-23 ~05h30 (run 05h — full maintenance)**

## ✅ FAIT CE MATIN (run 05h 2026-09-23)

- **Codes hotGames** vérifiés (7) : grow-a-garden, steal-a-brainrot, volleyball-legends, blue-lock-rivals, anime-vanguards, fruit-battlegrounds, squid-game-x.
  - **volleyball-legends** — MODIFIÉ : Update 88 fait tourner la liste. Actifs = UPDATE_88, GET_SLIMED (5 Lucky Style Spins), XP_BOOST (potion 2x XP) ; UPDATE_87/RONIN_RETURN/KATANA passés en expirés. Sources : Beebom (19 sept) + Roonby/GamesRadar (Update 88).
  - **anime-vanguards** — MODIFIÉ : ajout de **100thTournament** (100 Trait Rerolls, niv. 10) → 4 codes actifs. Sources : Pro Game Guides (18 sept) + agrégat GamesRadar/Pocket Tactics. MiniUpd2 laissé inactif (listé inactif par PGG).
  - grow-a-garden / steal-a-brainrot / fruit-battlegrounds / squid-game-x / blue-lock-rivals : inchangés, « Vérifié le » rafraîchi.
- **Rotation** (10 pages) : blockspin, illegal-soccer, defend-ur-base-with-anime, merge-a-nuke, 1-aura-per-click **confirmées à jour** (date rafraîchie). grimoires-era, locked, my-gym, catch-a-monster, fifa-super-soccer laissées **à revérifier** (voir plus bas).
- **Aniimo** — UPDATE appliqué : badges `new` périmés (9) remis à `false`, `lastChecked`→23 sept, et créature **Prismana Glynsera** (Nova, Lumière/Glace, DPS ; event Vein Abundance 21→27 sept, Beast Fang Ridge) ajoutée à `creatures.json`. `build_site.py` relancé.

---

## 🔥 URGENT

_(rien)_ — aucune information ne justifie une modification urgente supplémentaire.

---

## 🟢 À PUBLIER

_(rien)_ — kill switch éditorial appliqué. Aucun sujet ne réunit confirmation solide + valeur joueur nette + absence de page équivalente. « 2 excellents articles > 20 faibles ».

---

## 🛠️ À METTRE À JOUR

- **FC 27 — contenu de lancement** · importance haute · statut EVERGREEN→UPDATE post-J0
  - Sortie **25 sept.** (J-2 aujourd'hui). Action au **run 05h du 26 sept.** (post-sortie) : détailler Season 1 Ones to Watch, **Destined for Glory** (Mbappé + Rogers, Fernandes, Isak, Mbeumo), TOTW 1-2, SBC/Objectifs d'accès anticipé ; vérifier les notes des tops joueurs à J0.
  - URL : `data/fc-27/updates.json` — **UPDATE**, pas de nouvelle URL. Ne rien détailler de spéculatif avant que le contenu soit live.

---

## 🟡 À PRÉPARER / SURVEILLER (tendances)

- **Roblox Fall Games 2026** (annonce officielle) · statut MONITOR · trendScore ~55/100
  - 6 nouveaux jeux : **Showdown** (FPS anime), Monster in the Mansion (co-op horror), GOAT Football League, Nemesis, Fossil Force, Caramel.
  - Décision : NE PAS créer de page prématurément (mode conquête). Surveiller CCU/visites (rotrends/robloxden). Si un titre décolle **et** a des codes réels → page principale + codes d'abord. Showdown = candidat le plus prometteur.
- **GTA 6** · EVERGREEN · MONITOR : sortie **19 nov. 2026** toujours confirmée (reveal Netflix 21 sept, ~27 min gameplay near-final). Actus marketing (DualSense édition GTA VI, système relation Lucia/Jason, NDA cast) = faible valeur joueur → evergreen inchangé.
- **Roblox Everywhere** (annonce plateforme 11 sept.) · MONITOR : attendre déploiement joueur réel / intention de recherche avérée.

---

## 👀 À REVÉRIFIER (codes — mappings/sources ambigus)

- **fifa-super-soccer** — codes-nom `bestfootball`/`fifasupersoccer` : Insider Gaming (2 sept) les dit actifs, mais notre page (vérif 20/09, plus récente) les a **déjà classés expirés**. Conflit non résolu → ne pas réactiver sans preuve fraîche ×2 sources.
- **catch-a-monster** — sources périmées (PCGamesN mars 2026) / nouveaux codes `stowerbug`/`stellawolf`/`nexa` en source unique. Attendre 2 sources concordantes datées.
- **locked** — ambiguïté **LOCKED vs LOCKED 2** : jeux de codes différents. Désambiguïser au placeId avant toute édition.
- **my-gym** — nom ambigu (My Gym vs Run a Gym vs Gym League vs Ultimate Gym Game) : pas de liste datée fiable pour NOTRE jeu.
- **grimoires-era** — sources datées introuvables (Fandom/PGG périmés) ; garder les 11 codes, revérifier via wiki Fandom.
- **blue-lock-rivals** — codes rotant tous les ~2 j ; snapshots sources divergents (Beebom 5 sept ≠ pcgamer 20 sept ≠ notre page 21 sept). Nos 3 codes gardés (pas de preuve d'expiration) — recouper au prochain run avec source datée ≥ 21 sept.
- **type-soul** / **sailor-piece** / **character-rng** / **broken-blade** — voir `_rotationARevoir` antérieurs.

**Candidats en attente** (`_pending2026-09-23`) : Grow a Garden **FREESEED** (event The Hunt: Roblox 20, source unique PGG 17 sept → surveillance). STORY/STARBUD (PGG, récompenses graines) suspects → ignorés.

---

## 📅 PRIORITÉS DEMAIN (run 05h — 2026-09-24, jeudi)

1. **Codes** (priorité absolue) : hotGames + lot de rotation. Prioriser les slugs **jamais vérifiés** restants (clickers 1-magic-evolution/1-mine-per-click, animal-hospital, noob-incremental non-tracés…) et trancher les « à revérifier » (fifa-super-soccer name-codes, catch-a-monster, locked/LOCKED 2).
2. **Trend detector** : re-scan Roblox Fall Games (Showdown surtout) — vérifier traction CCU/visites.
3. **Directeur SEO** : poursuivre la généralisation du bandeau CTA `data-cta="guidelink"` aux pages codes non-hotGames à cluster complet.
4. **FC 27** : préparer le gros UPDATE post-lancement pour le run du 26 sept.
5. **Régénération** ordre : build_site → build_home → (si codes changés) build_codes_json → build_sitemap.

---

_Sujets obsolètes retirés : bloc « FAIT CE SOIR » du 22/09 (+1 Loot To Forge, cluster publié — archivé dans editorial-intelligence.json)._
