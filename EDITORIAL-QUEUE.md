# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-30 (run 05h — vendredi — 9 hotGames revérifiés inchangés + correction du feed Aniimo avec les patch notes OFFICIELS)**

## ✅ FAIT — RUN 05h 2026-10-30 (vendredi)

- **9 hotGames revérifiés via sources datées fraîches — AUCUN changement de code** (qualité > quantité ; → `verifDate` 30/10, `catalogVerify` 30/10) :
  - **steal-a-brainrot** : `BESTBRAINROTEVER` seul actif (TimeSaver 08/10 + esportnow 04/10) ; `saturn` toujours non confirmé → non ajouté.
  - **grow-a-garden** : `RDCAward` + `BEANORLEAVE10` — **disputés** (TimeSaver 27/10 = « try it » ; wiki = aucun actif depuis 13/10). Conflit → gardés (pas de preuve d'expiration, §4) ; `torigate` NON ajouté (disputé/mono).
  - **blue-lock-rivals** : les sources accessibles (dexerto.fr 02/10, beatcopgame 17/10) sont **antérieures à l'update Aiku** → ne contredisent pas notre set du 25-28/10. `SKELETON / AIKUCHANGES / SPOOKY` maintenus.
  - **volleyball-legends** : `UPDATE_93 / CURSED / TOURNAMENT` (Roonby 24/10, Update 93) — match.
  - **fisch** : dumps sans statut (Roonby 24/10). `ChapelTroubles` **NOUVEAU** mais mono-source sans récompense → MONITOR. Set inchangé.
  - **fruit-battlegrounds** : `EVENHIGHER!` (officiel) + `HIGHER1M120K` + `YOO1M110K!` (TimeSaver 18/10) — match. Prochain code à 1 140 000 likes.
  - **anime-vanguards** : next-stage.fr (29/10) liste un **superset** (28 codes) ; nos 14 = sous-liste (OK, §4). `2ndAnniDay7` mono-source → MONITOR (2ᵉ source avant ajout).
  - **blox-fruits** : next-stage.fr (30/10) confirme nos 23 actifs ; `Chandler` (erreur probable) + `pleasezakineedthis` (mono) non ajoutés.
  - **anime-last-stand** : `MagicKnights! / ElfReincarnation! / IsItReallyWeekly?!` (switchbladegaming 26/10) — match (`ElfReincarnation!` disputé, gardé).
- **Aniimo — feed CORRIGÉ avec les patch notes OFFICIELS ✅** : `data/aniimo/updates.json` mis à jour. Les **patch notes Pawprint/Steam** (via gamerfuzion 27/10) **supersèdent la roadmap du 29/10** : **51 nouveaux Aniimo** (pas 32) dont **Jaguaraun** (1er co-créé communauté), **niveau max 70**, **Spar 4v4** (pas 1v1), Egg Heist PvP 3 équipes (en test), Magical Wonder Night jusqu'au **10/12**. **LIVE** après la maintenance 28-29/10. Aucun code annoncé. **Stats des 51 créatures NON ingérées** (données officielles détaillées attendues — ne pas inventer).
- **GTA 6** : aucun nouveau post Newswire officiel depuis Edge #430 (29/10). Sortie **19/11** + préchargement **12/11** maintenus. Rumeurs website/Instagram = spéculation (non publiable).
- **FC 27** : Ultimate Scream **Team 2** attendue **30/10 18:00 UTC** (après l'heure du run 05h) — **non confirmée EA**. Rien publié ce run → runs 15h/22h.
- **Régénération + QC** : voir rapport du jour (ordre build respecté ; QC complet).

---

## 🎃 COUVERTURE HALLOWEEN 2026 (programme — règle « guides d'événements », CLAUDE.md)

> **Règle permanente** : chaque event/MAJ d'un hotGame doit être couvert (UPDATE before CREATE), **détails confirmés uniquement**. ⚠️ **L'événement Halloween se termine le 31/10** → **dès le run 05h du 01/11, retirer/archiver les codes & sections event** (FischFright2026 expire le 09/11 : à garder jusque-là).

| Jeu (suivi) | Event Halloween | Statut au 30/10 |
|---|---|---|
| **Fisch** | FischFright 2026 | ✅ `FischFright2026` actif (expire 09/11) — garder après le 31/10 jusqu'à expiration |
| **Blue Lock Rivals** | code `SPOOKY` | ✅ Publié (récompense exacte toujours à confirmer) |
| **100-days-at-sea** | code `SPOOKY` | ✅ Publié (26/10) |
| **Tower Defense Simulator** | — | ⛔ Aucun code Halloween actif (vérifié 29/10) |
| Grow a Garden / Steal a Brainrot | event 2026 | ⏳ Pas d'event-code 2026 confirmé → kill switch |
| Autres hotGames | scan continu | 🔎 Retrait des sections event au 01/11 |

## 🔥 URGENT

- **Aniimo — Part II LIVE : ingérer les DONNÉES OFFICIELLES dès publication détaillée.** Le feed est à jour (51 Aniimo, cap 70). Dès que la liste détaillée + stats des 51 créatures sont publiées officiellement : `data/aniimo/creatures.json` / `locations.json` / `tier-list.json` → `python3 tools/build_site.py`. **NE RIEN inventer.** Vérifier aussi d'éventuels **codes de lancement** de la Part II.
- **GTA 6** — ~3 semaines avant lancement (**19/11**). **Surveiller le Rockstar Newswire chaque run** (préchargement 12/11, taille fichier, patch day-one). **UPDATE evergreen uniquement** ; séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.
- **FC 27 Ultimate Scream Team 2 — sortie attendue aujourd'hui 30/10 18:00 UTC** : à traiter aux runs **15h/22h** si confirmée live (equipe + éventuelle solution DCE vérifiée, sans invention).

## 🟢 À PUBLIER

_(rien de neuf)_ — aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** détecté (recherches overnight = listicles SEO / dumps recyclés).

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **FC 27 Ultimate Scream — Team 2** (voir URGENT) : dès la sortie réelle, mettre à jour `data/fc-27/updates.json` + guides data-driven. Token store 13/11, promo Scream fin **06/11**, Beaver Moon 24/11→01/12 (confirmés).
- **Fisch — `ChapelTroubles` (NOUVEAU, mono-source)** : chercher une 2ᵉ source datée + la récompense avant d'ajouter. Indice d'une update « Chapel » récente à surveiller.
- **Anime Vanguards — `2ndAnniDay7`** (next-stage.fr 29/10, mono-source) : confirmer via 2ᵉ source (Roonby/samlover) avant d'ajouter — complèterait notre série Day1-6.
- **brainrot-evolution — à revérifier (sources en vrac).** Dumps mélangés mal datés → **source fraîche propre requise**.
- **Blue Lock Rivals — récompense de `SPOOKY`** à préciser (source officielle).
- **Fisch — `MarianaIsGoingCrazy` / `TemporarySubmarine`** : confirmer l'expiration via 2ᵉ source (gardés faute de preuve).
- **grimoires-era — PÉRIMÉE (conflit 3 voies)** ; **rivals — décalage de version** ; **type-soul — page vide** (2-3 sources propres requises).
- **Listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35, noob-incremental, world-fighters 24) : **preuve d'expiration requise** avant prune (§4) — décision Peter.
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de guide/tier dédié).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Marqueurs `<!-- FEATURED-WEEK-START/END -->` toujours **absents** d'`index.html` et `meilleurs-jeux-roblox.html`. **→ Peter : indiquer où placer le bloc** (ou valider sa création). (Vendredi → N/A ce jour.)
- **FC 27 — Prix des cartes live = NON fait** (feed type Futbin/Futwiz à cadrer).
- **/avatar/** : 3 pages encore en cache ancien. Dossier **NE PAS MODIFIER** → laissé tel quel ; à signaler si Peter veut aligner le cache.
- **Backlog rotation chronique** : décider d'un plan de rattrapage (voir ci-dessous).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **MONITOR 2ᵉ source** : Fisch `ChapelTroubles`, Anime Vanguards `2ndAnniDay7`, grow-a-garden `torigate`.
- **squid-game-x** (extras single-source → MONITOR), **grimoires-era** (3 voies), **rivals** (version), **haze-piece** (PHANTOMSHIP/OKUCHI 2/3), **100-days-at-sea** (`RIVAL` conflit historique).
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm ; clones anime : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.
- **Rotation en retard** : **167 pages non-hot > 3 j (dont 31 jamais vérifiées)** — backlog chronique. Le lot de rotation 05h (38 pages, majorité novelty FR + clones anime) **non traité ce run** (priorité donnée aux 9 hotGames vérifiés avec exactitude + verticales éditoriales). À reprendre avec sources fraîches/officielles.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h 30/10 ; 05h 31/10)

1. **FC 27 Ultimate Scream Team 2** (sortie ~30/10 18:00 UTC) : publier dès confirmation live + éventuelle solution DCE vérifiée.
2. **Aniimo** : ingérer les **données officielles** des 51 créatures / lieux / tier-list dès disponibles → `build_site.py`. Vérifier codes de lancement Part II. Ne rien inventer.
3. **GTA 6** : surveiller Newswire (préchargement 12/11, patch day-one).
4. **Blue Lock Rivals** : confirmer la récompense de `SPOOKY` ; revérifier au prochain drop hebdo.
5. **Volleyball Legends** : revérifier au prochain Update (codes éphémères par patch).
6. **Rotation backlog** : attaquer les ~31 « jamais vérifiées » désambiguïsables (placeId) + brainrot-evolution (source propre).
7. **Halloween** : **au run 05h du 01/11**, retirer/archiver les sections & codes event (sauf FischFright2026 jusqu'au 09/11).
8. **Décisions Peter** : bloc « Jeu de la semaine » ; feed prix cartes FC 27.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
