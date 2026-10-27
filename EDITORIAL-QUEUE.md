# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-27 (run 05h — mardi — FC 27 Ultimate Scream publié + anime-last-stand revérifié)**

## ✅ FAIT — RUN 05h 2026-10-27 (mardi)

- **FC 27 — Promo Ultimate Scream (Halloween) publiée** (data-driven, `data/fc-27/guides.json` → `build_site.py`) :
  - **SBC & solutions** : nouvelle section « Promo en cours : Ultimate Scream » (Team 1 le 23/10, fin **06/11**, boutique jetons 13/11, upgrade **Beaver Moon 24/11–01/12**) + mise en avant du **DCE Nick Woltemade (85, MOC)** actif + nouvelle FAQ « SBC actifs ». Rubrique « solutions pas chères » actualisée (solution vérifiée à ajouter, pas d'invention).
  - **Méta joueurs** : nouvelle section « Promo en cours : Ultimate Scream (cartes fortes) » — Raphinha (90 MOC), Ronaldo (89 BU), Paralluelo (88 BU), Szoboszlai (88 MDC), Palmer (87 MOC), Héros Zola/Stam + DCE Woltemade. Source **FUT.GG (22/10)** + dexerto fc-27 (ajoutées aux sources FC 27).
  - **Correction naming entérinée** : Ultimate Scream = **FC 27** (jeu courant, sorti 25/09/2026), confirmé par EA/FUT.GG/dexerto/realsport101. L'étiquette « FC 26 » du 18/10 (basée sur un calendrier dexerto périmé) est corrigée dans `editorial-intelligence.json`.
- **Codes — 1 page revérifiée, inchangée** :
  - **anime-last-stand** : 3 codes actifs (MagicKnights!, ElfReincarnation!, IsItReallyWeekly?!) **confirmés par Dexerto.com 24/10** (match exact) → `verifDate` 16/10 → **27/10**. `catalogVerify` mis à jour.
- **Codes — hot games croisés, aucun changement (kill switch)** : blox-fruits (liste plus fraîche que les sources recyclées ; jeu statique), grow-a-garden & steal-a-brainrot (déjà vérifiés 26/10, stables), blade-ball (cohérent, SPOOKYSEASON Halloween plausible). Sources de codes massivement **recyclées/périmées** ce run → pas de modification sans preuve fraîche.
- **Régénération** : `build_site` + `build_home` + `build_codes_json` (verifDate ALS) + `build_sitemap`. **QC complet OK** (0 null byte, fins de fichiers, JSON/JS valides, sitemaps fermés, GA4/nav/CTA OK).

---

## 🔥 URGENT

- **GTA 6** — ~3,2 semaines avant lancement (**19/11/2026**). Préchargement **12/11** confirmé (Forbes 26/10 via BusinessWire), mais **heure de préchargement et taille de fichier toujours non officielles**. **Rien de neuf confirmé au 27/10**. ⚠️ **« Official news update » rapporté pour le 29/10** (gamerant, non vérifiable en primaire) → **surveiller le Newswire chaque run**. **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.
- **Aniimo « Season 1 Part II » (29/10)** — update **confirmé** (preview officielle des devs via playnews 20/10) : région **Whisperwake Isles**, **51 nouveaux Aniimo** (32 espèces), nouveaux Prismana, **PvP 1v1 permanent**, Vein Abundance 30/10→06/12. **Aucun nouveau code annoncé.** Fin Part I : 28/10 23h59 UTC. → **Préparer l'ingestion data-driven APRÈS l'officiel du 29/10** (`data/aniimo/` → `build_site.py`). Ne rien inventer.

## 🟢 À PUBLIER

_(rien de neuf)_ — aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** détecté cette nuit (recherches tendances = résultats spam/recyclés).

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **FC 27 Ultimate Scream — Team 2** attendue **~30/10** (non confirmée EA) → ajouter dès sortie + **une solution DCE Woltemade vérifiée** (ne pas inventer de recette). Rafraîchir en fin de promo (06/11).
- **fruit-battlegrounds — à revérifier (conflit).** Dexerto.com (copie 25/08 périmée) liste BIGMILLIHUNNID!/ITSTHEBILLION!/CODEFIX (absents de notre page) et ignore nos EVENHIGHER!/OMGUPDATE22. Source unique + stale → **kill switch**, page inchangée (verif 01/10). Besoin d'une **source fraîche**.
- **grimoires-era — PÉRIMÉE (conflit 3 voies).** Rebuild via **source officielle** (Trello/Discord) requis.
- **rivals — décalage de version.** Page FREE182 ; sources divergentes. Besoin d'une **source fraîche marquant clairement l'actif**.
- **tap-simulator-reborn — casse `SPOOKY` à reconfirmer.**
- **sell-fries — 4 codes mono-source** → publier si 2ᵉ source concordante.
- **type-soul — page vide** (~55 codes sans récompenses) → 2-3 sources propres avec récompenses.
- **Listes gonflées (maintien vs rebuild)** : anime-battle-rng, anime-astral-simulator (~100), dragon-blox (~82), attack-on-titan-revolution → **preuve d'expiration** requise avant prune (§4).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Marqueurs `<!-- FEATURED-WEEK-START/END -->` toujours **absents** d'`index.html` et `meilleurs-jeux-roblox.html`. Étape du lundi **non exécutable** sans créer la structure. **→ Peter : indiquer où placer le bloc** (ou valider sa création).
- **FC 27 — Prix des cartes live = NON fait** (nécessite un feed type Futbin/Futwiz — à cadrer).
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de guide/tier dédié).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **fruit-battlegrounds** (voir ci-dessus), **spin-a-soccer-card** (conflit total, page à 0), **fisch** (`CAVERN`/`ChapelTroubles` source unique), **100-days-at-sea** (`RIVAL` conflit).
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm ; clones anime : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.
- **Codes** : grimoires-era (3 voies), rivals (version), haze-piece (PHANTOMSHIP/OKUCHI 2/3).
- **Rotation en retard** : **>150 pages > 10 j (dont ~30 jamais vérifiées)** — backlog chronique. Rotation approfondie **non réalisée ce run** (sources recyclées → vérif fiable impossible). À reprendre avec sources fraîches.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 28–29/10)

1. **Aniimo** : fin Part I le 28/10 23h59 UTC, update **29/10** → préparer l'ingestion data-driven (ne rien publier avant l'officiel).
2. **FC 27 Ultimate Scream Team 2** (~30/10) + solution DCE Woltemade vérifiée.
3. **GTA 6** : surveiller Newswire (« news update » rapporté 29/10 ; heure préchargement / taille fichier / patch day-one).
4. **Rotation backlog** : attaquer les ~30 « jamais vérifiées » désambiguïsables (placeId) avec sources fraîches ; **fruit-battlegrounds** (2ᵉ source).
5. **Décisions Peter** : bloc « Jeu de la semaine » ; feed prix cartes FC 27.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
