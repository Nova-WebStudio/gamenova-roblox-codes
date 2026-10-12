# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-12 (run 05h + session interactive Peter : 3 jeux + Halloween)**

## ✅ FAIT — SESSION INTERACTIVE 2026-10-12 (3 jeux + Halloween)

- **Anime Zero — NOUVEAU CLUSTER publié** : `codes-anime-zero.html` (25 codes, ≥2 sources : Pocket Tactics 9/10 + Dexerto 8/10 + igeeksblog) + `guides/anime-zero.html` (guide débutant) + SVG fallback. Intégration complète (GAMES, GAMES_INDEX, ROBLOX_THUMBS, hub codes, hub guides, sitemap, liens croisés). Miniature rbxcdn réelle. Jeu en dev actif.
- **Dandy's World — refresh** : ICHOR confirmé actif (samlover 2/10), verifDate → 12/10. SPOOKYSEASON expiré (non ajouté). RESEARCHMOBILE = candidat mono-source.
- **Slayers 2 — ⚠️ CONFLIT** : roonby 7/10 (12 actifs) vs Pocket Tactics 12/10 (aucun actif / wipe probable). Kill switch, aucun changement, à trancher au prochain run (3ᵉ source).
- **Audit Halloween** : blade-ball a déjà SPOOKYSEASON ; événements Halloween en cours (Steal a Brainrot Haunted Fuse/Phoenix = pas un code, Adopt Me/Brookhaven sans codes) mais aucun code Halloween neuf confirmé à ajouter. Candidats mono-source rejetés (FREEOCTOBLOCK777, saturn).

## ✅ FAIT — RUN 05h 2026-10-12

- **volleyball-legends** : UPDATE 91 publié (UPDATE_91/REPLAYS/MVP ; ancien set Update 90 expiré). **dragon-adventures** : SeasonXP expiré. Re-vérifs : anime-vanguards, blue-lock-rivals, arm-wrestle-simulator. GTA 6 Trailer 3 = rumeur non confirmée (19 nov tenu). FC 27 / Aniimo : MONITOR.

---

## 🔥 URGENT

- **GTA 6** — veille **Rockstar Newswire officiel** (Trailer 3 « imminent » rapporté, non confirmé) d'ici le **19 nov 2026**. UPDATE evergreen uniquement, jamais de nouvelle URL. Séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.
- **Slayers 2** — trancher le conflit roonby (actif) vs Pocket Tactics (wipe) avec une 3ᵉ source fraîche. Possible shutdown à confirmer avant tout retrait de codes.

## 🟢 À PUBLIER

_(rien)_ — kill switch maintenu.

## 🛠️ À METTRE À JOUR

- **blue-lock-rivals — drop hebdo** : EPICSENDOU / ONEMOREWEEK / NELAIKUNEXT = Dexerto 11/10 seul (en conflit avec RobloxDen 10/10). 2ᵉ source fraîche requise.
- **anime-defenders** : RobloxDen 11/10 marque MEMBEREREBREWRERES + incredibilli expirés + nouveaux (SKILLTRESS/MEGAUPD/RAIDSAREBACK). Mono-source → 2ᵉ source.
- **Dandy's World — RESEARCHMOBILE** (skin Rodger) : candidat mono-source (samlover) → ajouter après 2ᵉ source.
- **FC 27** : promo live (Destined for Glory / Future Stars estimée) via **ea.com / Pitch Notes uniquement**.
- **da-hood** (PVP/BUFF/WORLDCUP26) & **blox-fruits** (LIGHTNINGABUSE) : mono-source → 2ᵉ source.
- **Aniimo _Irisalis_** : ajouter aux data `creatures.json` uniquement quand les stats combat seront publiées.
- **⚠️ DÉCISION PETER — grosses listes gonflées** (anime-astral-simulator 100, dragon-blox 82, anime-battle-rng 35) : rebuild autour du set vérifié-actif, ou maintien ?

## 🟡 À PRÉPARER / SURVEILLER

- **Anime Zero** : surveiller nouveaux codes (jeu en dev actif) ; créer une **tier list** quand des données d'unités fiables seront sourcées ; 2ᵉ guide forte intention si traction. Renseigner `ROBLOX_UNIVERSE_IDS['anime-zero']` si l'API Roblox redevient joignable.
- **Steal a Brainrot — guide Halloween** : secret **Phoenix** via **Haunted Fuse** (événement Halloween) — pas un code. Angle guide « comment obtenir Phoenix » si traction (2 sources).
- **Jeu de la semaine (§30)** : ⚠️ marqueurs `<!-- FEATURED-WEEK-START/END -->` **absents du code**. Non modifié (pas d'édition structurelle risquée). Recommandation : **Steal An Egg** (#1 viral). À Peter : confirmer le mécanisme / ajouter les marqueurs.
- **CTA §28** : plusieurs pages codes (gabarit anime-eternal, dont la nouvelle anime-zero) sans bandeau `data-cta="guidelink"` — maillage assuré via sidebar + liens in-text. Pass CTA dédié à prévoir.

## 👀 À REVÉRIFIER (conflits non tranchés)

- **slayers-2** : roonby 7/10 (actif) vs Pocket Tactics 12/10 (wipe) — 3ᵉ source.
- **blue-lock-rivals**, **anime-defenders** : nouveaux drops mono-source.
- **fisch** (MarianaIsGoingCrazy), conflits antérieurs : basketball-zero, blade-ball (SERPENT), anime-squadron, clover-retribution, etc.
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées), dungeon-quest-reborn, dig-and-clean, iron-soul-dungeon, bloxstrike, catch-and-tame.

## 📅 PRIORITÉS PROCHAIN RUN

1. **Codes hot** : blue-lock-rivals (2ᵉ source drop), volleyball-legends (Update 92), anime-vanguards, grow-a-garden, steal-a-brainrot.
2. **Slayers 2** : trancher le conflit (3ᵉ source / shutdown ?).
3. **Anime Zero** : surveiller drops (jeu en dev actif).
4. **Candidats 2ᵉ source** : anime-defenders, da-hood, blox-fruits, Dandy's World RESEARCHMOBILE.
5. **GTA 6** Newswire · **FC 27** ea.com · **Aniimo** stats Irisalis · **§30** décision Peter.

---

_Pour publier : dans le dossier GameNova, `git add -A && git commit -m "MAJ Zoneblox" && git push origin main`. Hostinger déploie après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
