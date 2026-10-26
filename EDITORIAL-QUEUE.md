# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-26 (run 05h — lundi — 2 corrections codes + 12 pages vérifiées + Aniimo revérifié)**

## ✅ FAIT — RUN 05h 2026-10-26 (lundi)

- **2 corrections de codes (contenu réellement modifié)** :
  - **hypershot** : `ONEBILLION` **retiré** (expiré) → page passe à **0 code actif**. Preuve : **2 sources** concordantes (Dexerto.fr 01/10 + Dexerto.com) le donnent expiré. `sixstoreys` annonce « 6 new codes » mais contredit par les 2 sources fiables → **ignoré** (kill switch). Panneau « Dernière mise à jour » réécrit.
  - **100-days-at-sea** : `SPOOKY` (20 Pearls, Halloween) **ajouté** → page passe à **1 code actif**. Confirmé par **2 sources fraîches** (Pro Game Guides 24/10 + Roblox Den 26/10), cohérent avec l'événement d'Halloween en cours. `RIVAL` = conflit (actif RobloxDen / inactif ProGameGuides) → **non publié**.
- **12 pages vérifiées, confirmées inchangées** (`verifDate` rafraîchie au 26/10) :
  - **Hot** : steal-a-brainrot (BESTBRAINROTEVER, Dexerto 12/10), volleyball-legends (UPDATE_91/REPLAYS/MVP, Samlover 13/10), grow-a-garden (RDCAward/BEANORLEAVE10, ProGameGuides 03/10 + Dexerto), blue-lock-rivals (4 codes, roonby modifié 24/10 corrobore), pet-simulator-99 (0 code, Nerdschalk), anime-vanguards (14 codes anniv, notre liste 25/10 plus fraîche que les sources), fisch (3/4 confirmés Dexerto), steal-an-egg (0 — **pas de système de codes**, Destructoid 22/10), spin-a-soccer-card (kill switch, voir ci-dessous).
  - **Rotation** : grow-a-garden-2 (4 codes TEAMGREENBEAN/WATERYOPLANTS/REMEMBERTODRINKWATER/FREESEED = ProGameGuides 14/10).
- **Aniimo revérifié** (data-driven) : 15 codes reconfirmés par mein-mmo (09/10), `data/aniimo/codes.json` → `lastChecked` 26/10. `aniimazingfroyo` donné expiré par mein-mmo seul (code **US-only**) → conservé sous surveillance.
- **Régénération** : `build_codes_json` (codes changés) + `build_site` + `build_home` + `build_sitemap`. QC complet.

---

## 🔥 URGENT

- **GTA 6** — ~3,3 semaines avant lancement (**19/11/2026**). Préchargement **12/11** confirmé, perks de pré-commande confirmés. **Rien de neuf confirmé au 26/10** (Rockstar Newswire = préload/pré-commande déjà connus). Surveiller le Newswire à chaque run (heure exacte de préchargement, patch day-one, Trailer 3 éventuel). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.

## 🟢 À PUBLIER

_(rien de neuf)_ — aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** détecté cette nuit. Les 2 corrections mûres (hypershot, 100-days) ont été traitées ce run.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **grimoires-era — PÉRIMÉE (conflit 3 voies).** games.gg vs pocketgamer/pockettactics vs page. Rebuild via **source officielle** (Trello/Discord) requis.
- **rivals — décalage de version.** Page FREE182 ; sources divergentes (Insider 04/10 stale, Roonby 06/10=FREE201). Besoin d'une **source fraîche marquant clairement l'actif**.
- **tap-simulator-reborn — casse `SPOOKY` à reconfirmer** (publié majuscules le 25/10 ; Dexerto l'affichait minuscule).
- **sell-fries — 4 codes mono-source** (4000Members, FreeCandy, CoolCode, 3000members ProGameGuides) → publier si 2ᵉ source concordante.
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses.
- **Listes gonflées (maintien vs rebuild)** : anime-battle-rng (~35), anime-astral-simulator (~100), dragon-blox (~82), attack-on-titan-revolution (21) → **preuve d'expiration** requise avant tout prune (§4).

## 🟡 À PRÉPARER / DÉCISION PETER

- **🆕 Aniimo « Season 1 Part II » (29/10)** : update confirmé pour le **29 octobre**. **PRÉPARER** l'ingestion data-driven (`data/aniimo/` → `build_site.py`) **APRÈS** l'officiel. Nouveaux codes probables à cette occasion. Aucune invention avant confirmation.
- **✅ FC 27 — DÉBLOQUÉ (26/10).** Nommage résolu (FC 27 sorti le 25/09/2026). Vertical passé en `released`, rubrique « Guides & tutos » + 3 pages créées : **Méta joueurs** (pilote sourcé), **SBC & solutions** (structure), **Tuto Ultimate Team débutant**. À MAINTENIR : rafraîchir la méta à chaque promo, ajouter les solutions SBC actives au fil des sorties, suivre les promos UT. **Tier list joueurs désormais EN LIGNE** (`/games/fc-27/tier-list/` : classement notes officielles + méta par poste ; renderer tier-list rendu générique, réutilisable pour tout jeu non-Aniimo). **Prix des cartes live = NON fait** (nécessite un feed type Futbin/Futwiz — à cadrer).
- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Les marqueurs `<!-- FEATURED-WEEK-START/END -->` restent **absents d'`index.html` et de `meilleurs-jeux-roblox.html`**. L'étape du lundi n'est **pas exécutable** sans créer cette structure (risqué sans gabarit). **→ Peter : indiquer où placer le bloc « Jeu de la semaine »** (ou valider sa création).
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de `data-cta="guidelink"` — pas de guide/tier dédié).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **spin-a-soccer-card** : conflit total — tryhardguides=`release` (actif) ; Dexerto.fr 01/09=`STAR-STORM`/`THUNDER-DIAMOND`. Aucune concordance → **kill switch, page reste à 0**, revérifier avec source fraîche.
- **fisch** : `CAVERN` (roonby ≠ notre `CARBON`) et `ChapelTroubles` (NEW roonby) = **source unique contradictoire** → non publiés, surveiller FischFright.
- **100-days-at-sea** : `RIVAL` (conflit RobloxDen/ProGameGuides) → surveiller.
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm (sources same-name, identité non confirmée).
- **Codes** : grimoires-era (3 voies), rivals (version), haze-piece (PHANTOMSHIP/OKUCHI 2/3).
- **Rotation en retard** : **151 pages > 3 jours (dont 30 jamais vérifiées)** — backlog chronique. Clones anime à désambiguïser (placeId) : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 27/10)

1. **Aniimo** : suivre l'update **29/10** (préparation data-driven ; ne rien publier avant l'officiel).
2. **Rotation backlog** : attaquer les 30 « jamais vérifiées » désambiguïsables (placeId) — prioriser les jeux à vrai trafic/codes.
3. **FischFright** : `ChapelTroubles`/`CAVERN` 2ᵉ source ; **spin-a-soccer-card** source fraîche.
4. **tap-simulator-reborn** (casse `SPOOKY`) · **sell-fries** (2ᵉ source 4 codes) · **grimoires-era** (officiel) · **rivals** (source fraîche).
5. **GTA 6** Newswire (heure préchargement / Trailer 3 / day-one).
6. **Décisions Peter** : naming FC 27, bloc « Jeu de la semaine ».

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
