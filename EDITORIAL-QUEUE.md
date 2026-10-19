# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-19 (run 05h — lundi)**

## ✅ FAIT — RUN 05h 2026-10-19

- **Codes — 0 édition (run propre).** Tous les hot games vérifiés et **défendables** vs sources fraîches : **blue-lock-rivals** (la page = le set actif de Dexerto 18/10 — NELAIKU/HALLOWEEN/WSNAKE/SORRYFORDELAYAIKU ; EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT désormais **confirmés expirés** par Dexerto → page correcte), **steal-a-brainrot** (BESTBRAINROTEVER, Dexerto 12/10), **volleyball-legends** (UPDATE_91/REPLAYS/MVP, samlover 13/10), **anime-vanguards** (8 codes confirmés actifs par samlover 12/10), **anime-last-stand** (3 codes confirmés par pockettactics 03/10), **fisch** (4 codes défendables ; Dexerto FR stale 04/09 = 3 permanents, pas de code Halloween propre), **grow-a-garden** (RDCAward/BEANORLEAVE10 ; FREESEED/torigate chez roonby **sans récompenses** → non ajoutés). Conforme à « EXACTITUDE > FRAÎCHEUR ».
- **Rotation — 5 jeux vérifiés** (catalogVerify → 19/10) : shindo-life, grand-piece-online, da-hood, car-dealership-tycoon, toilet-tower-defense.
- **Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents** du code (index.html + tous HTML) → étape non exécutable, **rien touché** (décision Peter en attente).
- **GTA 6** : release **19/11/2026 reconfirmée** (Rockstar Newswire officiel). Chatter « Extended Look ce mois » / « trailer décembre 25 ans » = marketing/rumeur → page evergreen inchangée.
- **FC 26 Ultimate Scream** : Scream Team 2 + Halloween Puzzle Crafting **LIVE** (ea.com officiel) → **bloqué par décision naming Peter**. MONITOR.
- **Aniimo** : 15 codes actifs reconfirmés (khelnow 04/10) → inchangé.
- **Régénération** : non lancée (0 édition de contenu/données du site → rien à régénérer ; éviter le churn de timestamps). Seuls les fichiers d'état mis à jour.

---

## 🔥 URGENT

- **GTA 6** — À ~1 mois du lancement (19/11/2026), surveiller les **confirmations pré-lancement Rockstar Newswire** à chaque run. Séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. **UPDATE evergreen uniquement.**

## 🟢 À PUBLIER

_(rien)_ — kill switch maintenu sur tous les conflits ; aucun nouveau jeu Roblox avec preuve d'intérêt multi-source + codes réels cette nuit.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **Grand Piece Online — MUST_UPDATE (2 sources, besoin 3ᵉ).** Dexerto 18/10 + g2a 01/10 **concordants** → ajouter **FREE_Drops8** (24h 2× Drop) + **5FREETAILORVOUCHERS_2** (5 Tailor Vouchers). ⚠️ NE PAS retirer FREE_Drops7/FREE_EXP6 (conflit, pas de preuve d'expiration). ILOVEGPO_3 double-confirmé.
- **Da Hood — candidat + conflit.** MACRO! (1M DHC) + ETERNAL (500K DHC) = **2 sources fraîches concordantes** (robloxden 18/10 + progameguides 12/10) → ajouter si 3ᵉ source. **DOG/SHARK : KILL SWITCH** (robloxden=expirés vs progameguides+allthings=actifs) → pas de retrait sans 2ᵉ preuve d'expiration.
- **Noob Incremental — MUST_UPDATE (report).** Set actif double-confirmé (Dexerto 10/10 + RobloxDen 15/10). Rewrite reporté : récompenses fiables par code + resync `#activeList`/`const ACTIVE`/compteur/« Mis à jour le ».
- **fish-an-anime-rng — conflit 3 voies non tranché.** 2 sources fraîches concordantes requises avant réécriture (page très probablement périmée).
- **type-soul — page vide.** Insider Gaming ~55 codes mais **sans récompenses** → besoin de 2-3 sources propres avec récompenses pour peupler (anti-invention).
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : republier un set fiable là où il en existe un.

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Naming FC 27 vs FC 26** : le titre EA live = **FC 26** (promo **Ultimate Scream** / Halloween en cours, ea.com officiel). **Bloque la couverture Ultimate Scream.** À trancher.
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **absents du code**. À Peter : confirmer le mécanisme / ajouter les marqueurs (sinon l'étape du lundi reste non exécutable).
- **⚠️ Grosses listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35) : rebuild autour du set vérifié-actif, ou maintien ? Rotation en retard (~39 j, depuis 10/09).
- **Dette technique copyAll** : `const ACTIVE` diverge de la liste visible sur plusieurs pages (fish-an-anime-rng, bloxstrike, catch-and-tame…). Synchroniser à chaque édition, ou supprimer la duplication.

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : da-hood (DOG/SHARK), fish-an-anime-rng (3 voies), bloxstrike, catch-and-tame, iron-soul-dungeon, anime-expeditions, anime-defenders, dig-and-clean, fifa-super-soccer, vv-ultimatum, spin-a-soccer-card ; build-a-boat (fuzzy friend / Lurking Legend : 2ᵉ source).
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées) ; toilet-tower-defense (⚠️ vérifier le **vrai** TTD, pas le clone « Toilet Verse »).
- **toilet-tower-defense** : page vide ; les codes « Toilet Verse Tower Defense » (nerdschalk) sont un **jeu différent** — ne pas cross-peupler.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 20/10)

1. **Grand Piece Online** : 3ᵉ source fiable → ajouter FREE_Drops8 + 5FREETAILORVOUCHERS_2 (édition propre, non destructive).
2. **Da Hood** : 3ᵉ source fraîche → ajouter MACRO!/ETERNAL ; retrancher DOG/SHARK (preuve d'expiration 2ᵉ source).
3. **Hot games** : re-vérifier BLR (EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT), steal-a-brainrot, grow-a-garden, anime-vanguards (candidats 2ndAnniDay1/Prepare/1DayDelay/25thHour → 2ᵉ source), fisch (FischFright2026 Halloween → confirmation propre).
4. **noob-incremental** : exécuter le rewrite une fois les récompenses sourcées.
5. **fish-an-anime-rng** / **type-soul** : sources fraîches avec récompenses.
6. **FC 26 Ultimate Scream** (si naming tranché) · **GTA 6** Newswire (confirmations pré-lancement) · **Aniimo** codes.
7. **Rotation suite** : grosses listes gonflées + jamais vérifiés.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
