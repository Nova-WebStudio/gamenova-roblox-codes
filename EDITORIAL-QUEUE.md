# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-12 (slot 05h — full maintenance, lundi)**

## ✅ FAIT CE RUN (2026-10-12)

- **Codes hot — 5 vérifiés, 1 publication** :
  - **volleyball-legends** : 🔥 **UPDATE 91 (Instant Replay) PUBLIÉ**. Actifs = **UPDATE_91 / REPLAYS / MVP** ; l'ancien set Update 90 (UPDATE_90, SKELETON_BUNDLE, JINX, SLOT_REWORK) passe **expiré**. Base : **2 sources fraîches concordantes = Roonby (10/10) + Dexerto (11/10)** (Dexerto marque explicitement Update 90 expiré ; rotation conforme au pattern documenté du jeu). RobloxDen 10/10 = check antérieur au drop.
  - **anime-vanguards** : 8 codes INCHANGÉS confirmés Pockettactics 10/10 (2ndAnniDay2-6 + Assault + SummerLeaving + AnniNextHopefully). **Pas de 2ndAnniDay7**, événement anniversaire non confirmé terminé → aucune suppression. verifDate 12/10.
  - **blue-lock-rivals** : set actuel (DONREVAMP/SENDOUNEXT/ACEEATER) confirmé **toujours actif** (RobloxDen 10/10 + Pockettactics 04/10). verifDate 12/10.
  - **grow-a-garden / steal-a-brainrot** : vérifiés 11/10 (hier), stables → non reverifiés en profondeur.
- **Rotation — 1 expiration propre** :
  - **dragon-adventures** : **SeasonXP passé expiré** (RobloxDen 10/10 + Pockettactics 24/08 = 2 sources indépendantes « expiré », aucune source « actif »). 5 codes restants confirmés actifs (JUSTYBLOX/AESUBREALM/FLUFFY/GALIFRAN/SHAMEWING). Incohérence pré-existante du compteur « expirés » corrigée au passage.
  - **arm-wrestle-simulator** : Celebration + brainrot confirmés actifs RobloxDen 10/10 → verifDate 12/10.
- **Éditorial** : GTA 6 = Trailer 3 « imminent / extended look ce mois-ci » amplifié (TheGamePost, Player.one) mais **AUCUNE confirmation officielle Rockstar Newswire** → reste RUMEUR, 19 nov 2026 tenu. FC 27 = Destined for Glory probablement live, Future Stars estimée (non confirmée EA). Aniimo = « plus gros update depuis le lancement » + hotfix rapportés, stats combat Irisalis **toujours non publiées** → MONITOR. Roblox = viral du moment (**Steal An Egg**) déjà couvert, **aucun breakout neuf**.
- **Régénération** (build_site → build_codes_json → build_home → build_sitemap) + QC complet : voir rapport du jour.

---

## 🔥 URGENT

- **GTA 6** — veille **annonce officielle Rockstar Newswire** (Trailer 3 / extended look donnés « imminents » par plusieurs médias, **non confirmés officiellement**) d'ici la sortie du **19 nov 2026**. UPDATE evergreen uniquement, jamais de nouvelle URL. Séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Ignorer les titres « trailer 3 is here » tant qu'absents du Newswire officiel.

## 🟢 À PUBLIER

_(rien)_ — kill switch maintenu. « 2 excellents > 20 faibles ». La seule publication réunissant traction réelle + sources suffisantes ce run était VL Update 91 → déjà faite.

## 🛠️ À METTRE À JOUR

- **blue-lock-rivals — drop hebdo candidat** : **EPICSENDOU / ONEMOREWEEK / NELAIKUNEXT** = Dexerto 11/10 **seul** (qui marque aussi DONREVAMP/SENDOUNEXT/ACEEATER expirés, en **conflit** avec RobloxDen 10/10 qui les donne actifs). Ajouter uniquement après **2ᵉ source fraîche**.
- **anime-defenders** : RobloxDen 11/10 marque **MEMBEREREBREWRERES + incredibilli expirés** (notre page les a actifs) et liste de nouveaux (SKILLTRESS/MEGAUPD/RAIDSAREBACK) → **mono-source**, divergence non tranchée, verifDate NON bumpé. 2ᵉ source requise avant tout retrait/ajout.
- **FC 27 — Destined for Glory / Future Stars** : brique data-driven mesurée. **Sources EA officielles uniquement (ea.com / Pitch Notes)** — Future Stars estimée ~9 oct, Ultimate Scream ~23 oct (non confirmés). Ne pas publier de squads leakés.
- **da-hood** : candidats PVP / BUFF / WORLDCUP26 (Pockettactics 23/09, mono-source) → besoin 2ᵉ source fraîche. DOG/SHARK confirmés actifs.
- **blox-fruits** : candidat LIGHTNINGABUSE (mono-source) → 2ᵉ source avant ajout.
- **Aniimo _Irisalis_** : ajouter à `data/aniimo/creatures.json` **uniquement quand les stats de combat seront publiées**. Ne rien inventer.
- **⚠️ DÉCISION PETER — grosses listes gonflées** (anime-astral-simulator 100, dragon-blox 82, anime-battle-rng 35, verifDate 10/09) : trim non prouvable, non revérifiées. Peter doit trancher : rebuild autour du set vérifié-actif, ou maintien.

## 🟡 À PRÉPARER / SURVEILLER

- **Jeu de la semaine (§30)** : ⚠️ **les marqueurs `<!-- FEATURED-WEEK-START/END -->` n'existent pas dans le code** (ni dans index.html ni dans build_home.py). Bloc non modifiable sans ajout structurel risqué. **Recommandation jeu #1 présent au catalogue : Steal An Egg** (viral oct. 2026, hotGames, page codes existante). → **Peter : confirmer le mécanisme / ajouter les marqueurs** pour que ce soit automatisable.
- **Steal a Brainrot — angle guide Halloween** : secret **Phoenix** via machine **Haunted Fuse** (MAJ Halloween) — pas un code. Guide « comment obtenir Phoenix » si traction confirmée (2 sources).
- **volleyball-legends** : surveiller Update 92 ; vérifier l'**expiration réelle** de l'Update 90 via 2ᵉ source (publiée sur base Roonby+Dexerto + pattern du jeu).
- **anime-expeditions** : candidats UPD 3.5 (Bossrush/Hellfire/Update3/RDC26 — RobloxDen 02/10 en « Check », pas frais). Attendre 2 sources fiables fraîches.
- **Nouveaux jeux Roblox** : aucun breakout neuf (viraux « steal » déjà couverts). Continuer la veille.
- **CTA §28** : plusieurs pages codes sans `data-cta="guidelink"` (ex. dragon-adventures, arm-wrestle-simulator) — pré-existant, non régressif → pass dédié à prévoir.

## 👀 À REVÉRIFIER (conflits/divergences non tranchés)

- **blue-lock-rivals** : conflit Dexerto 11/10 (ancien set expiré + nouveau drop) vs RobloxDen 10/10 (ancien set actif) → set actuel maintenu, nouveau drop en attente 2ᵉ source.
- **anime-defenders** : expiration MEMBEREREBREWRERES/incredibilli + nouveaux SKILLTRESS/MEGAUPD/RAIDSAREBACK (RobloxDen 11/10 seul).
- **fisch — MarianaIsGoingCrazy** : absent de Pockettactics 07/10 mais pas de preuve d'expiration → conservé.
- Conflits antérieurs toujours ouverts : basketball-zero, spongebob-tower-defense, anime-dimensions-simulator, blade-ball (SERPENT), a-one-piece-game, grimoires-era, anime-squadron, clover-retribution (13), anime-stars.
- **Rotation en retard** (verifDate anciens, sources agrégateurs périmées) : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées — décision Peter), dungeon-quest-reborn, dig-and-clean, iron-soul-dungeon, bloxstrike, catch-and-tame, fish-an-anime-rng.

## 📅 PRIORITÉS PROCHAIN RUN (2026-10-12 15h → puis 22h)

1. **Codes hot** (priorité absolue) : blue-lock-rivals (**2ᵉ source EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT**), volleyball-legends (Update 92 ? expiration Update 90 confirmée ?), anime-vanguards (fin anniversaire / 2ndAnniDay7 ?), grow-a-garden, steal-a-brainrot.
2. **Candidats à confirmer (2ᵉ source)** : anime-defenders (MEMBEREREBREWRERES/incredibilli expirés + SKILLTRESS/MEGAUPD/RAIDSAREBACK), da-hood PVP/BUFF/WORLDCUP26, blox-fruits LIGHTNINGABUSE.
3. **GTA 6** : veille Rockstar Newswire officiel (rumeur Trailer 3 renforcée). **FC 27** : promo live via ea.com uniquement. **Aniimo** : publication stats Irisalis.
4. **§30 jeu de la semaine** : décision Peter sur les marqueurs manquants.

---

_Note : bloc « jeu de la semaine » (spec §30) non modifié — marqueurs absents du code (voir § À PRÉPARER). Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push._
