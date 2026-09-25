# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-09-25 ~05h30 (run 05h — full maintenance)**

## ✅ FAIT CE MATIN (run 05h 2026-09-25)

- **Codes hotGames** vérifiés (7) : anime-vanguards, blue-lock-rivals, volleyball-legends, fruit-battlegrounds, squid-game-x, pet-simulator-99, tower-defense-simulator.
  - **blue-lock-rivals** — ✏️ MODIFIÉ : les codes ont tourné. NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK! → expirés ; ajout **SNUFFYSOON, BUGFIXES, UBERSCONTINUES** (2 sources : PC Gamer 21 sept + Beebom 19 sept qui marque les 3 anciens expirés). Reste 3 actifs.
  - **fruit-battlegrounds** — ✏️ MODIFIÉ : ajout **EVENHIGHER! + OMGUPDATE22** (800 gemmes, 2 sources : Pocket Tactics + Pro Game Guides 22 sept). HIGHER1M120K/YOO1M110K! gardés. Page 2→4.
  - anime-vanguards (4), volleyball-legends (3), squid-game-x (6), pet-simulator-99 (0, correct), tower-defense-simulator (2) : **aucun changement** (keeps prudents), dates « Vérifié le » rafraîchies.
- **Traitements queue de la veille** :
  - **catch-a-monster** — ✏️ MODIFIÉ : ajout **stowerbug** (2k tower gems + points de tâche) + **stellawolf** (points de tâche), 2 sources (Pocket Tactics 16 sept + Fossbytes 20 sept). **nexa** non confirmé → abandonné. Page 9→11.
  - **untitled-tag-game** — ✏️ MODIFIÉ : ajout **roblox_rtc** (500)/**thankyou** (500)/**bombplushie** (250), code+récompense concordants Beebom + RobloxDen. seeyousoon/happyholidays (récompenses en conflit) + sorry (non confirmé) laissés. Page 0→3.
- **Rotation** (10 pages non-hot vérifiées) :
  - **100-days-at-sea** — ✏️ MODIFIÉ : CLASSES/DECORATE/20Pearls expirés (2 sources : Dexerto + PGG). Page 3→0. (SKELLY 1 source + conflit → non ajouté.)
  - **skibidi-masters-tower-defense** — ✏️ MODIFIÉ : SUMMER2026/ROYAL/125KLIKES/120KLIKES expirés (Beebom+PGG) ; 130KLIKES retiré (conflit tranché sur source récente PGG). Ajout 135/140/145/150KLIKES + FREETRAIT + POTIONS (2 sources). Page 5→6.
  - **peroxide** — ✏️ MODIFIÉ : 7 anciens codes expirés (4 confirmés PT+PGG, 3 événementiels périmés). Ajout **StayHydrated + JesterMiniUpdate** (2 sources). Page 7→2.
  - **my-gym** — ✏️ MODIFIÉ : 1MVISITS/Boxing expirés (Beebom+TryHardGuides). Ajout **Update**, ILiked gardé. Page 3→2.
  - **anime-apocalypse** — ✏️ MODIFIÉ (nettoyage majeur) : page **totalement périmée** (15 vieux codes event). Ajout **JOHNNY + STEELRIDER** (actifs confirmés PT ET Beebom). Page 15→2.
  - **untitled-boxing-game** (9, sous-listage stable), **pet-simulator-x** (0, correct), **all-star-tower-defense** (16, tous actifs) : confirmés, dates rafraîchies.
- **Aniimo** : 11 codes stables (concordance Beebom+Destructoid). aniimofreetoplay = source unique → non ajouté. lastChecked rafraîchi. Aucune nouvelle créature.
- **GTA 6** : sortie 19 nov. 2026 toujours confirmée → evergreen inchangé (MONITOR).
- **FC 27** : ✅ **LANCEMENT MONDIAL confirmé (25 sept)**. Contenu day-one capté (voir À METTRE À JOUR).
- **Régénération** : build_site → build_home → build_codes_json (**1222 codes actifs / 183 jeux**) → build_sitemap (381 URLs). **QC OK** (node --check, JSON, sitemap, HTML intègres, comptes exacts).

---

## 🔥 URGENT

_(rien)_ — aucune information ne justifie de modification urgente supplémentaire.

---

## 🟢 À PUBLIER

_(rien)_ — kill switch éditorial appliqué. Aucun nouveau jeu ne réunit traction réelle + codes réels + absence de page. Grow a Garden / Steal a Brainrot dominent toujours (déjà couverts). « 2 excellents > 20 faibles ».

---

## 🛠️ À METTRE À JOUR

- **FC 27 — contenu de lancement** · haute · EVERGREEN→UPDATE post-J0 · **ACTION AU RUN 05h DU 26 SEPT (J+1)**
  - Jeu **live mondial depuis le 25 sept**. UPDATE `data/fc-27/updates.json` (pas de nouvelle URL) avec : Season 1 **Ones to Watch** (18 sept) + **Destined for Glory** (25 sept, joueurs votés) ; chimie **Icons/Heroes réduite** (+1 Ligue/+1 Nation, Icons 88 OVR min) ; **15 promos/an** (vs 26) ; nouveaux **formats de packs** (Mini/Small/Large/Jumbo/Giant) ; récompenses **Rivals/Champions/Squad Battles** améliorées (Div 6 retiré, TOTW hebdo voté) ; **The Grounds** (hub open-world, archétypes AXP+Grounds Coins) ; **Manager Career** (gros update) ; **FC 27 Lite** gratuit. Vérifier notes des tops joueurs à J+1.
- **all-star-tower-defense** · basse : ajouter **ReturnOfTheLobbies, ALateSummerAwaits, AwesomeBeginnerCode, game11** (vus actifs sur Pocket Tactics 21 sept) après confirmation 2e source.

---

## 🟡 À PRÉPARER / SURVEILLER (tendances)

- **GTA 6** · EVERGREEN · MONITOR : sortie **19 nov. 2026** confirmée. Actus marketing = faible valeur joueur → evergreen inchangé.
- **RELL Seas** (jeu à venir, pas de date) · MONITOR : surveiller l'annonce d'une date de sortie.
- **Roblox Everywhere** (annonce 11 sept.) · MONITOR : attendre déploiement joueur réel.
- **Roblox Fall Games 2026** · MONITOR · trendScore ~35/100 : Showdown ~240 CCU = pas un hit. Kill switch → **ne PAS créer de page**. Réévaluer si un titre décolle + a des codes.
- **Aniimo** · event **Aniimo Together se termine le 27 sept** : revérifier codes + nouvelle créature après cette date.

---

## 👀 À REVÉRIFIER (codes — mappings/sources ambigus)

- **anime-apocalypse** — codes en **conflit** non ajoutés : TRANSCENDENT/INVASION/HOTFIXESONCEAGAIN/SUBARU/WORLDBOSS/ZOLTRAAK/HOTFIXESARECUTE (PT 21 sept = actifs vs Beebom 13 sept = expirés). Revérifier au prochain run.
- **skibidi-masters-tower-defense** — 130KLIKES (conflit tranché en faveur de PGG=expiré) ; candidats EPISODE81/160KLIKES/155KLIKES/LEAGUES/TRADEPLAZA/50MVISITS/100KLIKES (PGG) à confirmer 2e source.
- **anime-vanguards** — Pocket Tactics liste ~18 codes que PGG+GamesRadar classent expirés (liste PT périmée) → non ajoutés ; 100thTournament = source récente unique (PGG 22 sept), gardé.
- **arene-de-sniper** — Sniper Arena a des codes (Dexerto.fr/PocketTactics) mais **mapping placeId ambigu** vs notre page à 0 → désambiguïser avant tout ajout.
- **Grosses listes NON revérifiées ce run** (sous-listage stable, pas de preuve d'expiration) : anime-astral-simulator (100), dragon-blox (82), anime-battle-rng (35), brainrot-evolution (24), clover-retribution (14) → échantillon prioritaire au prochain run.
- **Reports antérieurs toujours en attente** : blade-ball (GOODVSEVIL/DUNGEONSRELEASE conflit), a-one-piece-game/Re:AOPG, locked/LOCKED:2, grimoires-era, spin-a-brainrot, world-cup-album, fifa-super-soccer. (Détail dans `_rotationARevoir` de code-watch.json.)

---

## 📅 PRIORITÉS DEMAIN (run 05h — 2026-09-26, samedi)

1. **FC 27 (J+1)** — **priorité éditoriale** : UPDATE `data/fc-27/updates.json` avec le contenu de lancement live (Ones to Watch, Destined for Glory, TOTW, SBC/Objectifs d'accès, The Grounds, Manager Career, chimie/packs). Vérifier notes des tops joueurs.
2. **Codes** (priorité absolue) : hotGames (rotation : grow-a-garden, steal-a-brainrot, blade-ball, anime-last-stand, blox-fruits, king-legacy, fisch) + lot de rotation prioritaire = **grosses listes non vérifiées** (échantillon : anime-battle-rng, brainrot-evolution, dragon-blox) + slugs anciens (doors, dress-to-impress, royale-high, slap-battles, 99-nights-in-the-forest).
3. **all-star-tower-defense** : ajouter les 4 nouveaux codes après 2e source.
4. **anime-apocalypse** : trancher le conflit sur les 7 codes en attente.
5. **Régénération** ordre : build_site → build_home → build_codes_json (si codes changés) → build_sitemap.

---

_Sujets obsolètes retirés : bloc « FAIT CE MATIN » du 24/09 (archivé dans editorial-intelligence.json). Rappel : pour publier, git add/commit/push manuel (voir rapport)._
