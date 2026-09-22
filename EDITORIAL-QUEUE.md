# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json`.
> **Dernière MAJ : 2026-09-22 ~19h40 (run du soir + « totale » +1 Loot To Forge)**

## ✅ FAIT CE SOIR

- **+1 Loot To Forge** — cluster « totale » complet créé et intégré (statut PUBLISHED) :
  - `codes-1-loot-to-forge.html` (2 codes actifs : 30000CCU, 20000CCU — 2 sources + description in-game),
  - `tier-list/1-loot-to-forge.html` (tier list des **priorités** — pas d'armes inventées, stats en aperçu live),
  - `guides/1-loot-to-forge.html` (guide complet + 2 vidéos oEmbed vérifiées).
  - Intégrations : main.js (GAMES_INDEX/ROBLOX_THUMBS/ROBLOX_UNIVERSE_IDS), const GAMES (accueil), hubs tous-les-codes/tier-lists/guides, sitemap, régénérations (build_site/home/codes_json/sitemap) + QC OK.
  - Suivi : surveiller le prochain code de palier (40000CCU probable) et les patchs.


---

## 🔥 URGENT

_(rien)_ — aucune information ne justifie une modification urgente du site ce soir. Codes traités au run 05h ; verticales evergreen (FC 27, GTA 6) à jour ; Aniimo codes courants et sourcés.

---

## 🟢 À PUBLIER

_(rien)_ — kill switch éditorial appliqué : aucun sujet ne réunit à la fois confirmation solide, valeur joueur nette et absence de page équivalente. « 2 excellents articles > 20 faibles ».

---

## 🛠️ À METTRE À JOUR (priorité run 05h)

- **Aniimo — codes & créature** · importance moyenne · statut UPDATE_REQUIRED
  - Sources : game8, Beebom, Destructoid, PC Gamer, GamesRadar (agrégat, HIGH)
  - Action : (1) rafraîchir `data/aniimo/codes.json` `lastChecked`→jour et passer les **9 flags `new:true` périmés** (datés 16 sept.) à `false` ; (2) ajouter la créature **Prismana Glynsera** (MAJ 17 sept.) à `data/aniimo/creatures.json` (absente — 8 créatures listées). Puis `python3 tools/build_site.py`.
  - URL existante : `/games/aniimo/codes/` — **UPDATE, pas create**. Set de 11 codes stable, ne rien inventer.
  - Non fait ce soir : `build_site.py` réservé au run 05h ; bénéfice = fraîcheur de badge, risque non justifié en off-cycle.

- **FC 27 — contenu de lancement** · importance haute · statut EVERGREEN→UPDATE post-J0
  - Sources : EA Sports (officiel), Dot Esports (patch notes lancement)
  - Action au **run 05h du 26 sept.** (post-sortie 25 sept.) : détailler Season 1 Ones to Watch (17 sept.→22 oct.), **Destined for Glory** (Mbappé + Rogers, Fernandes, Isak, Mbeumo — démarre 25 sept.), TOTW 1-2, SBC/Objectifs d'accès anticipé ; vérifier les notes des tops joueurs à J0.
  - URL : `data/fc-27/updates.json` — **UPDATE**. Déjà HIGH ; enrichir le détail promo une fois le contenu live.

---

## 🟡 À PRÉPARER

- **GTA 6 — actus marketing pré-lancement** · importance basse (valeur joueur faible)
  - Confirmé non couvert : **« GTA VI: The Album »** (annonce officielle) ; stunt **« Welcome to Vice City »** au Kaseya Center de Miami (~1M$).
  - Décision : NE PAS créer d'URL. Éventuelle ligne « actus » sur la page evergreen `/games/gta-6.html` au run 05h **seulement si** une section news y est ajoutée. Sinon rester en MONITOR (spec : evergreen mis à jour uniquement pour annonce **majeure**).

- **Roblox Everywhere** (annonce plateforme 11 sept.) · article explicatif potentiel
  - Attendre un déploiement réel côté joueurs / une intention de recherche avérée avant d'écrire. MONITOR.

---

## 👀 À SURVEILLER

- **Steal a Brainrot** — codes de spawn éphémères (BESTBRAINROTEVER / saturn) : expirent en heures, sources en conflit (23 vs « un seul »). Cible connue de faux-actifs → **rester à 0 actif** tant que pas de set durable ×2 sources.
- **type-soul** — désaccord massif PGG (64) vs Beebom (7) : page laissée vide, reconstruction non fiable (report 05h).
- **sailor-piece** / **grow-a-chicken-fighter** / **character-rng** / **broken-blade** — codes récents à recouper, mappings ambigus (voir `_rotationARevoir2026-09-22`).
- **Candidats en attente** (`_pending2026-09-22`) : TDS CHRISTMAS2025 · Hypershot THANKSGIVING · Fisch PeaceLoveUnityRespect/LittleBudlingUpdate · muscle-legends bossstrike · AOTR LIKES1M400K · car-dealership VACATION/STYLE/SEPTEMBER · jules-rng ARC6.
- **Steal An Egg** (#1, ~1,7M) — surveiller l'ajout d'un système de codes (absent).
- **Aniimo** — prochains patchs/créatures après le 17 sept.

---

## 📅 PRIORITÉS DEMAIN (run 05h — 2026-09-23, mercredi)

1. **Codes** (priorité absolue) : hotGames + lot de rotation (prioriser slugs jamais vérifiés / plus anciens). Trancher si possible les « à revérifier » (type-soul, sailor-piece, character-rng, broken-blade).
2. **Aniimo** : appliquer l'UPDATE ci-dessus (badges `new` + créature Prismana Glynsera) puis `build_site.py`.
3. **FC 27** : dernier run avant sortie (J-2) — vérifier que updates.json couvre bien le contenu d'accès anticipé et prépare le post-lancement.
4. **Directeur SEO** : poursuivre la généralisation du bandeau CTA `data-cta="guidelink"` aux pages codes non-hotGames à cluster complet (brique J36 de la roadmap).
5. **Trend detector** : re-scan rotrends/robloxden — aucun nouveau hit ≥4000 non couvert au 22 sept.
6. **Régénération** ordre : build_site → build_home → (si codes changés) build_codes_json → build_sitemap.

---

_Sujets obsolètes retirés : aucun (première édition de la queue)._
