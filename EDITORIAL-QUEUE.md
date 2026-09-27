# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-09-27 ~05h30 (run 05h — full maintenance dimanche)**

## ✅ FAIT CE MATIN (run 05h 2026-09-27)

- **Codes — 4 pages modifiées (2 sources indépendantes minimum)** :
  - **blue-lock-rivals** — ✏️ ROTATION : SNUFFYSOON/BUGFIXES/UBERSCONTINUES **expirés**, remplacés par **SNUFFYUPD/NEWMASTER/UBERSVOTE/WSNUFFY** (Beebom 26 + Pro Game Guides 26 concordants ; GamesRadar 21 / Fossbytes 20 = listes périmées, minoritaires). Page 3 → 4.
  - **doors** — ✏️ NETTOYAGE + COMPLÉTION : **SIX2025/5B/THEHUNT/4B expirés** (Pocket Tactics 25 + Beebom 14), et **ajout du set evergreen** confirmé par les 2 sources (18 codes créateurs/streamers à 5 Knobs + FE4R_RBX/3rd/CHEDDAR BALLS + codes Stardust). Page 8 → **30**. 777 gardé (conflit, PT récent le donne actif).
  - **anime-apocalypse** — ✏️ AJOUT : **TRANSCENDENT/INVASION/SUBARU/WORLDBOSS/GUILDBATTLES** (PGG 24 + GamesRadar 21). Page 2 → **7**. HOTFIXESARECUTE (PGG seul) non ajouté.
  - **slap-battles** — ✏️ EXPIRATION : les 3 codes (1x1x1x1x1x1/Happy5lappiversary/spookyseason25) passés expirés. **Aucun code actif** confirmé par Dexerto 14 + Pocket Gamer 5. Page 3 → **0**.
- **Codes — 6 pages « aucun changement », date « Vérifié le » rafraîchie (2 sources concordantes)** : grow-a-garden (RDCAward/BEANORLEAVE10), steal-a-brainrot (BESTBRAINROTEVER), fruit-battlegrounds (4, match PT 22), volleyball-legends (3, match GamesRadar 21), 99-nights-in-the-forest (3 ; SURVIVOR non confirmé mais aucune preuve d'expiration → gardé, à surveiller), royale-high (0, pas de système de codes).
- **Aniimo (data-driven)** — ✏️ `data/aniimo/codes.json` : **aniimoparty expiré** (Beebom 25 + GamesRadar 23), **aniimofreetoplay ajouté** (2 sources) ; **7 récompenses désormais confirmées** par 2 sources (aniimotogether, aniimoidyll, aniimowelcome, twinewithaniimo, anyoneaniimo, aniimobonus, aniimolaunch2026). 11 codes actifs.
- **all-star-tower-defense** — ✏️ ajout du bandeau **CTA `data-cta="guidelink"`** manquant (📖 Guides + 📊 Tier list ASTD) → conformité section 28.
- **Régénération** ordre respecté : build_site → build_home → build_codes_json (**1250 codes actifs / 184 jeux**, +25 net) → build_sitemap (383 URLs). **QC OK** (node --check main.js/events.js, tous JSON valides, sitemaps XML valides, pages éditées : fin `</html>`, 0 null byte, div équilibrés, badges/compteurs cohérents, CTA unique).

---

## 🔥 URGENT

- **GTA 6** · le **29 sept** : reveal **Game Informer CONFIRMÉ** (couverture 14 pages, 12 nouveaux screenshots, détails devs Rockstar — multi-sources). Dès la parution → **UPDATE de la page evergreen GTA 6** (screenshots + détails concrets), **PAS de nouvelle URL**. Rien à publier avant (pas de contenu concret publié).

---

## 🟢 À PUBLIER

_(rien)_ — kill switch éditorial appliqué. Grow a Garden / Steal a Brainrot dominent (déjà couverts). Aucun nouveau jeu ne réunit traction réelle + codes réels + absence de page. « 2 excellents > 20 faibles ».

---

## 🛠️ À METTRE À JOUR

- **dress-to-impress** · moyenne : 27 codes non revérifiés depuis le 7 sept (liste rotative, 20 j) → **priorité codes du prochain run** (date volontairement NON rafraîchie).
- **anime-apocalypse** · basse : ajouter **HOTFIXESARECUTE** si une 2e source fraîche le confirme (PGG seul le liste).
- **99-nights-in-the-forest** · basse : trancher **AWARDWINNER_YAY** (GamesRadar seul) et **« yay fishing »** (2 sources mais méthode spéciale via pêche, pas un code standard) ; **SURVIVOR** à surveiller (non confirmé par 2 sources fraîches, mais pas de preuve d'expiration).

---

## 🟡 À PRÉPARER / SURVEILLER (tendances)

- **GTA 6** · sortie **19 nov. 2026** confirmée (Zelnick, pas de report). Marketing = faible valeur joueur → evergreen inchangé sauf reveal du 29 sept (ci-dessus).
- **FC 27** · post-lancement (J+2) : pas de promo/SBC concrète nouvelle depuis le lancement du 25. Suivre les 1res promos Saison 1 (**Destined for Glory** hebdo, **TOTW votés**) et notes des tops joueurs.
- **Aniimo** · event web **Aniimo Together** se termine le **27 sept** (squad codes) ; les codes cadeaux restent actifs. Surveiller nouvelle créature / patch après l'event. 4 codes Beebom-seul (aniimonow/anywhereaniimo/anythinganiimo/aniimazingfroyo) en attente d'une 2e source.
- **blue-lock-rivals** · rotation très rapide (codes quasi quotidiens) → revérifier chaque run. Récompenses NEWMASTER/UBERSVOTE en conflit entre sources (libellés neutres en place).
- **RELL Seas** / **Roblox Everywhere** / **Roblox Fall Games 2026** · MONITOR : pas de titre qui décolle avec des codes réels → kill switch, pas de page.

---

## 👀 À REVÉRIFIER (codes — conflits / sources à retrouver)

- **doors** : 777 (conflit PT actif 25 vs Beebom expiré 14) ; reward SCREECHSUCKS en conflit (PT 50 / Beebom 25).
- **anime-apocalypse** : SUBARU/WORLDBOSS/GUILDBATTLES (existence 2 sources OK ; récompenses PGG seul).
- **Petites rotations** encore à faire avec URL à jour : slap-battles OK ce run ; restent **grosses listes** (anime-astral-simulator 100, dragon-blox 82, anime-battle-rng 35, brainrot-evolution 24, clover-retribution 14) → sous-listage stable, échantillon prioritaire.
- **Reports antérieurs toujours en attente** : a-one-piece-game/Re:AOPG, locked/LOCKED:2, grimoires-era, spin-a-brainrot, world-cup-album, fifa-super-soccer, arene-de-sniper (mapping placeId). (Détail dans `_rotationARevoir` de code-watch.json.)

---

## 📅 PRIORITÉS DEMAIN (run 05h — 2026-09-28, lundi)

1. **Codes** (priorité absolue) : hotGames (grow-a-garden, steal-a-brainrot, blade-ball, anime-last-stand, anime-vanguards, volleyball-legends, fruit-battlegrounds, **blue-lock-rivals** = rotation rapide) + **dress-to-impress** (prioritaire, non fait ce run).
2. **GTA 6** : le reveal Game Informer est le **29** (pas le 28) → préparer le canevas d'UPDATE evergreen ; rien à publier avant.
3. **Aniimo** : vérifier fin d'event Aniimo Together (créature/patch) + 2e source pour les 4 codes Beebom-seul.
4. **LUNDI = Jeu de la semaine** : mettre à jour le bloc `<!-- FEATURED-WEEK-START/END -->` avec le jeu #1 des tendances présent au catalogue (`date +%u == 1`).
5. **Régénération** ordre : build_site → build_home → build_codes_json (si codes changés) → build_sitemap.

---

_Sujets obsolètes retirés : bloc « FAIT CE MATIN » du 26/09 (archivé dans editorial-intelligence.json → topic code-maintenance-2026-09-26). Rappel : pour publier, git add/commit/push manuel (voir rapport)._
