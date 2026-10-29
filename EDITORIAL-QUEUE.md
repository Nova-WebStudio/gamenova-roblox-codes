# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-29 (run 05h — jeudi — 3 changements de codes bien sourcés + 9 hotGames revérifiés + Aniimo Part II / GTA 6 Edge ingérés)**

## ✅ FAIT — RUN 05h 2026-10-29 (jeudi)

- **Blue Lock Rivals — CONFLIT D'HIER TRANCHÉ ✅** : la page passait de `NELAIKU / HALLOWEEN / WSNAKE / SORRYFORDELAYAIKU` (codes désormais **expirés**) à **`SKELETON` (5 Lucky Spins), `AIKUCHANGES` (5 Lucky Flow Spins), `SPOOKY` (récompense non détaillée)** — **3 codes actifs**. 2 sources récentes concordantes : **Dexerto (25/10)** + **Game.guide (28/10)**. TimeSaver (22/10) listait encore les anciens = simplement antérieur à l'update Aiku, pas un conflit. Tout synchronisé (actifs/expirés, compteur hero, `const ACTIVE`, prose + « Dernière mise à jour », `verifDate` 29/10, JSON-LD `dateModified` 2026-10-29 + ItemList).
- **Fisch — FischFright2026 ajouté ✅** : nouveau code **actif** de l'évènement Halloween (expire 09/11), confirmé par **TimeSaver (27/10)** + **Roonby (24/10)**. `scarlet` + `CARBON` reconfirmés. `MarianaIsGoingCrazy` / `TemporarySubmarine` conservés (non listés actifs par TimeSaver mais **pas de preuve d'expiration**, règle §4). JSON-LD + compteur + dates synchronisés.
- **Fruit Battlegrounds — CONFLIT D'HIER RÉSOLU ✅** : `OMGUPDATE22` (**disputé** — certains trackers l'indiquent expiré, TimeSaver 18/10 ; cohérent avec la note interne 03/09) repassé en **expiré**. Actifs confirmés gardés : `EVENHIGHER!`, `HIGHER1M120K`, `YOO1M110K!` (TimeSaver 18/10). Page re-datée (verifDate 29/10, `dateModified` 2026-10-29).
- **9 hotGames revérifiés — inchangés** (→ `verifDate` 29/10, `catalogVerify` 29/10) :
  - **grow-a-garden** : match exact (RDCAward, BEANORLEAVE10) — gfinityesports (vérifié 28/10).
  - **steal-a-brainrot** : `BESTBRAINROTEVER` seul confirmé (Dexerto 12/10 + TimeSaver 08/10) ; `saturn` non confirmé → non ajouté.
  - **volleyball-legends** : match exact `UPDATE_93 / CURSED / TOURNAMENT` (TimeSaver 24/10).
  - **king-legacy** : core 5 confirmé (TimeSaver 20/10), nos 9 = **superset** (codes YouTuber longue durée), pas de preuve d'expiration.
  - **blade-ball** : superset OK (TimeSaver 20/10, antérieur à notre dernière vérif) — pas de preuve d'expiration sur SERPENT / DUNGEONSRELEASE.
  - **anime-vanguards** : set 2ᵉ anniversaire présent (Roonby 13-24/10).
  - **pet-simulator-99** : **0 code** confirmé (gfinity 26/10 : jeu arrêté, codes merch uniquement) — page déjà à 0.
  - **tower-defense-simulator** : 2 codes `1MILCOMMUNITY / 2MILLION` (TimeSaver 26/10 + Dexerto 15/09), **aucun** code Halloween actif.
  - **squid-game-x** : nos 6 codes confirmés actifs (next-stage.fr 29/10). La liste source de 59 codes = majorité **génériques single-source** → **NON ajoutés** (risque faux-actifs §4, kill switch).
- **Aniimo Season 1 Part II / Whisperwake Isles** : entrée ajoutée à `data/aniimo/updates.json` (contenu **annoncé** par la roadmap officielle devs — gamewith.ai maj 22/10). Région + 32 espèces + PvP 1v1 permanent + calendrier d'évènements (Vein Abundance 30/10→29/11…). **Stats des 32 créatures NON inventées** → ingestion data détaillée seulement une fois l'update **LIVE** et les données officielles disponibles.
- **GTA 6 — Edge #430** : dossier exclusif de 16 pages (visite studio Rockstar North, nouvelles images, interviews, gratuit en ligne le 29/10) ajouté à `data/gta-6/updates.json`. **Aucun report** : sortie 19/11 maintenue, préload 12/11.
- **Régénération** : `build_site` + `build_home` + `build_codes_json` + `build_sitemap` (ordre respecté). **QC complet OK** (0 null byte, div équilibrés, `node --check main.js`, JSON/XML valides, sitemap fermé, GA4/nav/CTA OK, cache cohérent).

---

## 🎃 COUVERTURE HALLOWEEN 2026 (programme — règle « guides d'événements », CLAUDE.md)

> **Règle permanente** : chaque event/MAJ d'un hotGame doit être couvert par un guide/section de guide (UPDATE before CREATE), **détails confirmés uniquement**. **L'événement Halloween se termine le 31/10** → après cette date, retirer/archiver les sections event.

| Jeu (suivi) | Event Halloween | Statut au 29/10 |
|---|---|---|
| **Fisch** | FischFright 2026 | ✅ Code `FischFright2026` publié (actif jusqu'au 09/11) — couverture code faite ; section guide dédiée non requise (récompense non détaillée par les sources) |
| **Blue Lock Rivals** | code `SPOOKY` | ✅ Publié (récompense exacte à confirmer) |
| **100-days-at-sea** | code `SPOOKY` | ✅ Publié (26/10) |
| **Tower Defense Simulator** | — | ⛔ Aucun code Halloween actif (vérifié 29/10) |
| Grow a Garden / Steal a Brainrot | event 2026 | ⏳ Non confirmé 2026 (sources = 2025) → kill switch |
| Autres hotGames | scan continu | 🔎 Fin event 31/10 (retirer les sections event après) |

## 🔥 URGENT

- **Aniimo — confirmer le passage LIVE de la Part II (aujourd'hui 29/10)** : entrée roadmap déjà ingérée ; dès que l'update est **live** (runs 15h/22h), ingérer les **données créatures officielles** (`data/aniimo/creatures.json`, `locations.json`, `tier-list.json`) → `build_site.py`. **NE RIEN inventer** (stats des 32 espèces).
- **GTA 6** — ~3 semaines avant lancement (**19/11**). Edge #430 sorti aujourd'hui (ingéré). **Surveiller le Rockstar Newswire chaque run** (heure préchargement 12/11, taille fichier, patch day-one). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.

## 🟢 À PUBLIER

_(rien de neuf)_ — aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** détecté (recherches tendances overnight = listicles SEO / spam recyclé).

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **FC 27 Ultimate Scream — Team 2** « attendue » **~30/10 18:00 UTC** (NON confirmée EA — fut.gg) → publier dès la sortie réelle + **une solution DCE Woltemade vérifiée** (ne pas inventer). Token store jusqu'au 13/11, promo Ultimate Scream jusqu'au **06/11**, upgrade Beaver Moon 24/11→01/12 (confirmés).
- **brainrot-evolution — à revérifier (sources en vrac).** dexerto.fr + allthings = dumps mélangés, mal datés (HALLOWEEN2026/HALLOWEENFUSION possibles mais non confirmables proprement) → page inchangée, **source fraîche propre requise**.
- **Blue Lock Rivals — récompense de `SPOOKY`** à préciser (non détaillée par Dexerto/Game.guide) → source officielle.
- **Fisch — `MarianaIsGoingCrazy` / `TemporarySubmarine`** : confirmer l'expiration via 2ᵉ source (gardés faute de preuve).
- **grimoires-era — PÉRIMÉE (conflit 3 voies).** Rebuild via source officielle (Trello/Discord) requis.
- **rivals — décalage de version** ; **type-soul — page vide** (~55 codes sans récompenses, 2-3 sources propres requises).
- **Listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35, noob-incremental, world-fighters 24) : **preuve d'expiration requise** avant prune (§4) — décision Peter.
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de guide/tier dédié).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Marqueurs `<!-- FEATURED-WEEK-START/END -->` toujours **absents** d'`index.html` et `meilleurs-jeux-roblox.html`. **→ Peter : indiquer où placer le bloc** (ou valider sa création). (Jeudi aujourd'hui → N/A ce jour de toute façon.)
- **FC 27 — Prix des cartes live = NON fait** (nécessite un feed type Futbin/Futwiz — à cadrer).
- **/avatar/** : 3 pages encore en cache ancien (reste du site aligné). Dossier **NE PAS MODIFIER** → laissé tel quel ; à signaler si Peter veut aligner le cache.
- **Backlog rotation chronique** : décider d'un plan de rattrapage (voir ci-dessous).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **squid-game-x** (53 codes extras single-source next-stage.fr → MONITOR, 2ᵉ source requise), **grimoires-era** (3 voies), **rivals** (version), **haze-piece** (PHANTOMSHIP/OKUCHI 2/3), **100-days-at-sea** (`RIVAL` conflit historique).
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm ; clones anime : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.
- **Rotation en retard** : **~165 pages non-hot > 3 j (dont ~30 jamais vérifiées)** — backlog chronique. Le lot de rotation 05h (38 pages, majorité novelty FR + clones anime) **non traité ce run** (priorité donnée aux 12 hotGames vérifiés + exactitude ; sources agrégées conflictuelles/recyclées sur le reste). À reprendre avec sources fraîches/officielles.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h 29/10 ; 05h 30/10)

1. **Aniimo** : confirmer le passage **LIVE** de la Part II et ingérer les **données officielles** (créatures/lieux/tier-list) dès disponibles → `build_site.py`. Ne rien inventer.
2. **FC 27 Ultimate Scream Team 2** (sortie réelle ~30/10 18:00 UTC) + solution DCE Woltemade vérifiée.
3. **GTA 6** : surveiller Newswire (préchargement 12/11, patch day-one).
4. **Blue Lock Rivals** : confirmer la récompense de `SPOOKY` ; revérifier au prochain drop hebdo.
5. **Volleyball Legends** : revérifier au prochain Update (codes éphémères par patch).
6. **Rotation backlog** : attaquer les ~30 « jamais vérifiées » désambiguïsables (placeId) + brainrot-evolution (source propre) + fisch Mariana/TemporarySubmarine (2ᵉ source).
7. **Halloween** : préparer le retrait des sections/codes event après le 31/10.
8. **Décisions Peter** : bloc « Jeu de la semaine » ; feed prix cartes FC 27.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
