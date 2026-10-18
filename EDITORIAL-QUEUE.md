# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-18 (run 05h — dimanche)**

## ✅ FAIT — RUN 05h 2026-10-18

- **🔥 Blue Lock Rivals RÉSOLU (URGENT de longue date).** Preuve d'expiration enfin réunie : l'ancien set de la page (**DONREVAMP / SENDOUNEXT / ACEEATER**) est **expiré selon 3 sources fraîches indépendantes** (Dexerto 18/10 + Twinfinite 17/10 + Pro Game Guides 11/10). **Nouveau set publié** : **NELAIKU** (5 Spins + 5 Flows), **HALLOWEEN** (5 Spins), **WSNAKE** (5 Flows), **SORRYFORDELAYAIKU** (5 Spins) — **double-confirmés par les 2 sources les plus fraîches** (Dexerto 18/10 + Twinfinite 17/10), récompenses concordantes. **EPICSENDOU / ONEMOREWEEK / NELAIKUNEXT NON publiés** : conflit (Dexerto 18/10 = expirés vs Twinfinite/GamesRadar/PGG = actifs) → kill switch sur ces 3. Page, `const ACTIVE`, compteur (4), liste expirés (+3) et « Mis à jour le » synchronisés.
- **Hot games stables (inchangés)** : **steal-a-brainrot** (BESTBRAINROTEVER, Dexerto 12/10 « no new codes »), **volleyball-legends** (UPDATE_91/REPLAYS/MVP, samlover 13/10), **anime-vanguards** (Dexerto ne liste plus les 2ndAnniDay* mais **aucune preuve fraîche d'expiration** → kill switch), **grow-a-garden** (RDCAward/BEANORLEAVE10 ; jeu réputé faux-codes, source faible, pas de preuve d'expiration).
- **Rotation — 5 jeux vérifiés** (catalogVerify → 18/10) : build-a-boat-for-treasure, fish-it, type-soul, jujutsu-shenanigans, murder-mystery-2. **Tous inchangés** (sources stale ou conflit → kill switch ; MM2 & type-soul correctement vides ; GPO & da-hood non re-vérifiés ce run).
- **Conflit fish-an-anime-rng recroisé** : 3 voies divergentes (Dexerto 05/10 ≠ destructoid 04/10 ≠ page/pcgamesn stale) → **kill switch maintenu**.
- **Régénération + QC** : `build_site` + `build_home` + `build_codes_json` + `build_sitemap` OK. QC vert (voir rapport).

---

## 🔥 URGENT

- **GTA 6** — Aucune news officielle nouvelle (recherche = rehash de rumeurs de délai). Statut inchangé : **release 19/11/2026** (MONITOR evergreen) + Netflix « Extended Look » (EVERGREEN). Séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. UPDATE evergreen uniquement. À surveiller : à ~1 mois du lancement, les confirmations pré-lancement Newswire vont arriver.

## 🟢 À PUBLIER

_(rien)_ — qualité > quantité, kill switch maintenu sur tous les conflits. Aucun nouveau jeu Roblox avec preuve d'intérêt multi-source cette nuit.

## 🛠️ À METTRE À JOUR

- **fish-an-anime-rng — conflit 3 voies non tranché.** Page = 1000MEMBERS/2kCCU/1kLIKES/ANGELIA/EXODIA (seul pcgamesn stale « août » les soutient). Dexerto 05/10 = set 100 % différent (Starfall/15MVISITS/Luther/Halloween/35KLIKES) ; destructoid 04/10 = encore un autre set. Seul **35KLIKES** est double-confirmé (Dexerto+destructoid) mais absent de la page. **2 sources fraîches concordantes requises** sur un set remplaçant avant réécriture destructive.
- **type-soul — opportunité.** Page vide alors qu'Insider Gaming (04/10) liste ~55 codes. Mais méga-liste **sans récompenses par code** + dates incohérentes → impossible de peupler (anti-invention). Besoin de 2-3 sources propres **avec récompenses** pour publier un set fiable.
- **build-a-boat-for-treasure** : Dexerto 10/10 marque **fuzzy friend** + **Lurking Legend** expirés (codes légacy/permanents, **1 seule source**) → 2ᵉ source requise avant retrait. Inchangé.
- **noob-incremental — MUST_UPDATE (report).** Set actif double-confirmé (Dexerto 10/10 + RobloxDen 15/10). Rewrite reporté : nécessite récompenses fiables par code + resync `#activeList` **et** `const ACTIVE` **et** compteur **et** « Mis à jour le ».
- **bloxstrike** / **catch-and-tame** : non re-vérifiés ce run (priorité BLR). Conflits toujours ouverts, 2ᵉ source fiable requise.
- **fifa-super-soccer** / **iron-soul-dungeon** / **anime-expeditions** / **anime-defenders** / **dig-and-clean** : candidats mono-source, 2ᵉ/3ᵉ source requise.
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : revue éditoriale (republier un set fiable là où il en existe un).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Naming FC 27 vs FC 26** : le titre EA live = **FC 26** (promo **Ultimate Scream** / Halloween en cours, source officielle ea.com). Les pages « FC 27 » devraient probablement cibler **FC 26**. **Bloque la couverture Ultimate Scream.** À trancher par Peter.
- **🆕 FC 26 Ultimate Scream (Halloween)** : promo confirmée officiellement (ea.com + fut.gg + sportskeeda). Opportunité SEO saisonnière réelle → **UPDATE page evergreen FC** (pas de création) **une fois le naming tranché**. MONITOR en attendant.
- **Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **absents du code**. À Peter : confirmer le mécanisme / ajouter les marqueurs.
- **⚠️ Grosses listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35) : rebuild autour du set vérifié-actif, ou maintien ? Décision Peter. Rotation en retard (~38 j, depuis 09/10).
- **Dette technique copyAll** : `const ACTIVE` diverge de la liste visible sur plusieurs pages (fish-an-anime-rng, bloxstrike, catch-and-tame…). Synchroniser à chaque édition, ou supprimer la duplication (le widget `data/codes.json` lit la liste visible).

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : fish-an-anime-rng (3 voies), bloxstrike, catch-and-tame, iron-soul-dungeon, anime-expeditions, anime-defenders, dig-and-clean, fifa-super-soccer, vv-ultimatum, spin-a-soccer-card ; build-a-boat (fuzzy friend / Lurking Legend : 2ᵉ source) ; BLR (EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT : re-trancher).
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées, ~38 j) ; shindo-life, toilet-tower-defense, da-hood, grand-piece-online, fish-it (set complet).

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 19/10 — lundi = Jeu de la semaine)

1. **⚠️ LUNDI 19/10 = Jeu de la semaine (§30)** — MAIS marqueurs `<!-- FEATURED-WEEK-START/END -->` absents : vérifier/ajouter le mécanisme avant de toucher (décision Peter en attente). Ne rien casser.
2. **Hot games** : re-trancher BLR (EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT), re-vérifier steal-a-brainrot, grow-a-garden, anime-vanguards (2ndAnniDay*), volleyball-legends.
3. **fish-an-anime-rng** : 2 sources fraîches concordantes → valider/réécrire (page très probablement périmée).
4. **type-soul** : trouver 2-3 sources avec récompenses → peupler la page vide si fiable.
5. **bloxstrike** / **catch-and-tame** : 2ᵉ source fiable → trancher.
6. **noob-incremental** : exécuter le rewrite MUST_UPDATE une fois les récompenses sourcées.
7. **Rotation suite** : grosses listes gonflées + jamais/anciennement vérifiés (shindo-life, grand-piece-online, da-hood, fish-it set complet).
8. **FC 26 Ultimate Scream** (si naming tranché) · **GTA 6** Newswire (confirmations pré-lancement) · **Aniimo** codes (surveiller aniimazingfroyo).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
