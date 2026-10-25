# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-25 (run 05h — 2 content gaps comblés, 8 hot games vérifiés, 6 stubs)**

## ✅ FAIT — RUN 05h 2026-10-25 (dimanche, pas de Jeu de la semaine)

- **2 content gaps comblés (codes réellement ajoutés)** :
  - **sell-fries** : 0 → **1 code** `Halloween` (100 Candies, événement Halloween). Confirmé par **3 sources** (ProGameGuides 24/10, Dexerto 21/10, games.gg 21/10). Les 4 autres codes listés par ProGameGuides seul (4000Members, FreeCandy, CoolCode, 3000members) = **mono-source → non publiés**.
  - **tap-simulator-reborn** : 0 → **2 codes** `BOO!` + `SPOOKY` (Halloween, potions + Candy Corn). Confirmé par **2 sources** (Dexerto 20/10 « 1ʳᵉ fournée de codes », games.gg 21/10). ⚠️ Casse de SPOOKY ambiguë (Dexerto minuscule vs games.gg majuscules) → **majuscules retenues**, à reconfirmer.
  - Les deux pages affichaient « aucun code / tout code annoncé est faux » → **récit inversé proprement** (hero, intro, FAQ + JSON-LD, panneaux, ItemList). Synchro complète : page HTML + `const GAMES` (index) + cartes `tous-les-codes` + `data/codes.json` + sitemap.
- **8 hot games vérifiés** (tous **confirmés inchangés** ou **MONITOR**, `verifDate` rafraîchie au 25/10) :
  - blox-fruits (Dexerto 19/10 « no new codes »), **blue-lock-rivals** (Dexerto 18/10 = **4 codes identiques** à la page ; SPOOKY/SKELETON/AIKUCHANGES = roonby seul → MONITOR), volleyball-legends (Samlover 13/10 = 3 codes identiques, reste expiré), anime-vanguards (14 codes anniv maintenus, pas de preuve d'expiration), fisch (ChapelTroubles = roonby mono-source → MONITOR), grow-a-garden, king-legacy (DigitalCitizen = 9 codes concordants), blade-ball.
- **Rotation (stubs)** : ride-a-dino, my-gaming-cafe, steal-from-the-rich, chop-a-forest → **confirmés SANS code** (roonby/absence de source). button-rng-2 & chicken-farm → source au même nom mais **identité non confirmée (pas de placeId)** → kill switch « à revérifier ». 16 pages marquées `catalogVerify=25/10`.
- **Régénération** : `build_codes_json` (codes changés) + `build_home` (sections + GAMES) + `build_sitemap`. QC complet OK (0 null byte, div équilibrés, JSON/XML valides, GA4 présent, cache cohérent).

---

## 🔥 URGENT

- **GTA 6** — ~3,5 semaines avant lancement (**19/11/2026**). Préchargement **12/11** confirmé. Surveiller le **Rockstar Newswire** à chaque run (heure de préchargement, patch day-one). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Rien de neuf confirmé au 25/10.

## 🟢 À PUBLIER

_(rien de nouveau)_ — les 2 content gaps mûrs (sell-fries, tap-simulator-reborn) ont été **publiés ce run**. Aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** cette nuit.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **grimoires-era — PÉRIMÉE (conflit 3 voies CONFIRMÉ).** games.gg vs pocketgamer/pockettactics vs page. Rebuild via **source officielle** (Trello/Discord) requis. Ne rien éditer tant que non tranché.
- **rivals — décalage de version.** Page FREE182 ; Insider 04/10=FREE137 (stale) ; Roonby 06/10=FREE201. Besoin d'une **source fraîche marquant clairement l'actif** + concordance.
- **tap-simulator-reborn — casse SPOOKY à reconfirmer** (publié en majuscules ; Dexerto l'affichait en minuscules). + 1 jeu souvent case-insensitive.
- **sell-fries — 4 codes mono-source** (4000Members, FreeCandy, CoolCode, 3000members ProGameGuides) → publier si 2ᵉ source concordante.
- **anime-battle-rng (~35) / attack-on-titan-revolution (21)** — gonflées, sources syndiquées/partielles → **preuve d'expiration** requise avant tout prune (§4).
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses.
- **8 pages à liste vide historiques** (100-days-at-sea, basketball-zero, be-a-brainrot, encounters, garden-tower-defense, pet-simulator-x, royale-high, slap-battles) : republier **seulement** là où ≥2 sources concordent.

## 🟡 À PRÉPARER / DÉCISION PETER

- **🆕 Aniimo « Season 1 Part II » (29/10)** : update confirmé pour le **29 octobre**. **PRÉPARER** l'ingestion data-driven (`data/aniimo/` → `build_site.py`) **APRÈS** l'officiel. Détails encore spéculatifs (playnews) → **aucune invention** avant confirmation.
- **⚠️ Naming FC 27 vs FC 26** : titre EA live = **FC 26** (promos actives, TOTY/Cornerstones). Vertical du site = `fc-27`. **Décision en attente de Peter** → couverture Ultimate Team bloquée.
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents du code** → étape du lundi non exécutable. À Peter.
- **⚠️ Listes gonflées** (maintien vs rebuild) : anime-battle-rng (~35), anime-astral-simulator (~100), dragon-blox (~82), aotr (21).
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de `data-cta="guidelink"` — pas de guide/tier dédié).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **Identité ambiguë (désambiguïser via placeId)** : **button-rng-2** (robloxden liste 8 codes pour un « Button RNG 2 » — même jeu ?), **chicken-farm** (Dexerto/Insider listent un « Chicken Farm » — même jeu ?). Nos pages = « aucun code ». Ne pas éditer sans confirmation placeId/universeId.
- **Codes** : grimoires-era (3 voies), rivals (version), fisch (ChapelTroubles mono-source), blue-lock-rivals (SPOOKY/SKELETON/AIKUCHANGES = roonby seul), anime-battle-rng, aotr, haze-piece (PHANTOMSHIP/OKUCHI 2/3), aniimo (aniimazingfroyo khelnow vs mein-mmo).
- **Rotation en retard** : anime-astral-simulator, dragon-blox (>45 j) ; clones anime (anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds) à désambiguïser (placeId) — codes = jalons longue durée, pas de preuve d'expiration donc inchangés.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 26/10)

1. **Aniimo** : suivre l'update **29/10** (préparation data-driven ; ne rien publier avant l'officiel).
2. **tap-simulator-reborn** : reconfirmer la casse de `SPOOKY` ; **sell-fries** : 2ᵉ source pour les 4 codes mono-source.
3. **button-rng-2 / chicken-farm** : désambiguïser via placeId/universeId → publier si identité confirmée.
4. **grimoires-era** (source officielle) · **rivals** (source fraîche actif).
5. **Hot games** : GPO (tailor vouchers), Da Hood (ESKETIT), Fisch (ChapelTroubles 2ᵉ source), Blue Lock (SPOOKY/SKELETON 2ᵉ source).
6. **GTA 6** Newswire (préchargement/day-one) · **FC 26** (si naming tranché).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
