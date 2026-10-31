# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-31 (run 05h — samedi — 4 hotGames vérifiés : blade-ball +GOODVSEVIL ; king-legacy / pet-sim-99 / 100-days-at-sea inchangés. GTA6/FC27/Aniimo en MONITOR.)**

## ✅ FAIT — RUN 05h 2026-10-31 (samedi)

- **4 hotGames vérifiés via sources datées fraîches** (`verifDate` 31/10, `catalogVerify` 31/10) :
  - **blade-ball** : **+`GOODVSEVIL`** (🎡 spin gratuit) — **2 sources** (next-stage.fr 31/10 + fossbytes). `SORRY4DELAY` / `LIVEEVENTS` = **conflit** (next-stage actif vs fossbytes expiré) → non ajoutés. 15 codes existants tous confirmés actifs → **16 codes actifs**. `dateModified` JSON-LD → 31/10.
  - **king-legacy** : set confirmé (next-stage.fr 29/10). `UPDATE3_16` / `ALLO` = dumps sans récompense → MONITOR (non ajoutés). Aucun changement de code.
  - **pet-simulator-99** : **0 code actif confirmé** (gamewave.fr 28/10 + Pocket Tactics). Inchangé.
  - **100-days-at-sea** : `SPOOKY` **actif** (20 Pearls, robloxden vérifié 31/10 05:02 UTC). `RIVAL` = 1 source + conflit historique → MONITOR (non ajouté). Aucun changement de code.
- **Autres hotGames** : vérifiés hier (30/10), aucune source plus fraîche contredisante trouvée ce run → **inchangés** (qualité > quantité ; pas de re-bump de date sans vraie revérification).
- **Total codes actifs du site : 1339** (data/codes.json régénéré). Build (site→home→codes_json→sitemap) + QC OK.

## 🎃 COUVERTURE HALLOWEEN 2026 — DERNIER JOUR (31/10)

> ⚠️ **Aujourd'hui = dernier jour de l'événement.** **Au run 05h du 01/11 : retirer / archiver les codes & sections event Halloween**, SAUF `FischFright2026` (Fisch) à garder jusqu'au **09/11** (date d'expiration).

| Jeu (suivi) | Event Halloween | Statut au 31/10 |
|---|---|---|
| **Fisch** | FischFright 2026 | ✅ `FischFright2026` actif (garder jusqu'au 09/11) |
| **Blue Lock Rivals** | code `SPOOKY` | ✅ Publié (récompense exacte toujours à confirmer) |
| **100-days-at-sea** | code `SPOOKY` | ✅ Actif confirmé 31/10 (20 Pearls) |
| **Blade Ball** | `SPOOKYSEASON` | ✅ Actif |
| Autres hotGames | scan continu | 🔎 Retrait des sections event au 01/11 |

## 🔥 URGENT

- **FC 27 Ultimate Scream Team 2 — LIVE mais à confirmer proprement.** beebom confirme l'équipe en jeu (Dembélé, Dybala, Pulisic, Griezmann, J.Félix, Frimpong, héros Sneijder/Touré/Futre/Marchisio/Matuidi/Ljungberg…). **⚠️ Conflit d'attribution de version** : beebom/futbin la labellisent « FC 26 » alors qu'**EA Sports FC 27 est sorti le 25/09/2026** (PSU/Insider Gaming — cohérent avec notre feed). Escouade listée **sans notes ni DCE recoupés par 2 sources exactes** → **kill switch, NON publié**. À traiter aux runs 15h/22h dès confirmation propre (équipe + éventuelle solution DCE vérifiée). **Décision Peter souhaitée** sur le libellé FC 26 vs FC 27 côté médias.
- **GTA 6** — ~3 semaines avant lancement (**19/11**, préchargement **12/11** confirmés). Rapport **Edge Magazine** (via Insider Gaming/OpenCritic, 29/10) : carte **~2× GTA 5**, développement principal terminé = **RAPPORTÉ** (pas un post Newswire officiel) → **non publié**. **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Surveiller le Newswire chaque run.
- **Aniimo Part II LIVE** — feed à jour (51 Aniimo, cap 70). **Stats officielles détaillées des 51 créatures toujours indisponibles en données structurées** → **NON ingérées** (pas d'invention). Dès publication officielle : `data/aniimo/creatures.json` / `locations.json` / `tier-list.json` → `build_site.py`. Aucun code de lancement annoncé.

## 🟢 À PUBLIER

- **✅ FAIT (session interactive, demande Peter) — « la totale » sur 2 nouveaux jeux tendance :**
  - **Throw Food For Animals** (129k joueurs / 19,3M visites) — codes + guide + tier list (priorités). **Aucun système de codes** → page codes honnête.
  - **Steal A Pet And Ride It** (44k joueurs / 11,6M visites) — codes + guide + tier list (priorités). **Aucun système de codes** → page codes honnête (pet légendaire gratuit via groupe Snail Riders signalé).
  - Intégrations complètes :  (index), / (main.js), hubs (tous-les-codes / guides / tier-lists), sitemap (+6 URLs), vraies miniatures , cross-links codes↔guide↔tier, cache bump **v=48→v=49** (192 pages). ⇒ **À pousser.**
- _(reste)_ aucun autre nouveau jeu avec preuve d'intérêt multi-source détecté via la veille overnight.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **FC 27 Ultimate Scream Team 2** (voir URGENT) : `data/fc-27/updates.json` + guides data-driven dès confirmation propre. Confirmés : promo Scream fin **06/11**, token store **13/11**, Beaver Moon **24/11→01/12**.
- **blade-ball `SORRY4DELAY` / `LIVEEVENTS`** : conflit (next-stage actif vs fossbytes expiré) → 2e source alignée requise avant ajout.
- **100-days-at-sea `RIVAL`** : robloxden l'affiche actif (31/10) mais 1 source + conflit historique → 2e source requise.
- **Fisch `ChapelTroubles`** (mono-source, pas de récompense) : 2e source datée requise.
- **Anime Vanguards `2ndAnniDay7`** : confirmé par next-stage.fr seul (timesaver 17/10 trop ancien) → 2e source avant ajout (compléterait la série Day1-6).
- **grow-a-garden `torigate`** (disputé) → non ajouté.
- **Blue Lock Rivals — récompense de `SPOOKY`** à préciser (source officielle).
- **brainrot-evolution** (sources en vrac → source fraîche propre requise) ; **grimoires-era** (conflit 3 voies) ; **rivals** (décalage de version) ; **type-soul** (page vide).
- **Listes gonflées** (anime-astral-simulator ~100, dragon-blox ~82, anime-battle-rng ~35, world-fighters 24, AoTR 21) : **preuve d'expiration requise** avant prune (§4) — décision Peter.
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de guide/tier dédié).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Libellé FC 26 vs FC 27** : les médias (beebom/futbin) parlent de « FC 26 » pour la promo en cours, alors que notre feed suit **FC 27 (sortie 25/09/2026, confirmée PSU/Insider)**. À trancher pour éviter toute confusion de version.
- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Marqueurs `<!-- FEATURED-WEEK-START/END -->` toujours **absents** d'`index.html` et `meilleurs-jeux-roblox.html`. **→ Peter : indiquer où placer le bloc** (ou valider sa création). (Samedi → N/A ce jour ; prochaine échéance lundi 02/11.)
- **FC 27 — Prix des cartes live = NON fait** (feed type Futbin/Futwiz à cadrer).
- **/avatar/** : 3 pages encore en cache ancien (`main.js?v=43`). Dossier **NE PAS MODIFIER** → laissé tel quel ; à signaler si Peter veut aligner le cache.
- **Backlog rotation chronique** : décider d'un plan de rattrapage (voir ci-dessous).

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **MONITOR 2ᵉ source** : blade-ball `SORRY4DELAY`/`LIVEEVENTS`, 100-days-at-sea `RIVAL`, Fisch `ChapelTroubles`, Anime Vanguards `2ndAnniDay7`, grow-a-garden `torigate`, king-legacy `UPDATE3_16`/`ALLO`.
- **squid-game-x** (extras single-source), **grimoires-era** (3 voies), **rivals** (version), **haze-piece** (PHANTOMSHIP/OKUCHI 2/3).
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm ; clones anime : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.
- **Rotation en retard** : **169 pages non-hot > 3 j (dont 31 jamais vérifiées)** — backlog chronique. Le lot de rotation 05h (38 pages, majorité novelty FR + clones anime) **non traité ce run** (priorité donnée à l'exactitude des hotGames + verticales éditoriales). À reprendre avec sources fraîches/officielles.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h 31/10 ; 05h 01/11)

1. **05h 01/11 : RETRAIT des sections & codes event Halloween** (sauf `FischFright2026` jusqu'au 09/11). Règle standing CLAUDE.md.
2. **FC 27 Ultimate Scream Team 2** : publier dès confirmation propre (2 sources alignées : équipe + éventuelle solution DCE vérifiée). Trancher le libellé FC 26/FC 27.
3. **Aniimo** : ingérer les **données officielles** des 51 créatures / lieux / tier-list dès disponibles → `build_site.py`. Vérifier codes de lancement. Ne rien inventer.
4. **GTA 6** : surveiller Newswire (préchargement 12/11, patch day-one, éventuel trailer de lancement).
5. **Blue Lock Rivals** : confirmer la récompense de `SPOOKY` ; revérifier au prochain drop hebdo.
6. **Volleyball Legends** : revérifier au prochain Update (codes éphémères par patch).
7. **Rotation backlog** : attaquer les ~31 « jamais vérifiées » désambiguïsables (placeId) + brainrot-evolution (source propre).
8. **Dimanche 02/11** : retour à l'heure standard US (events.json non chargé → aucune action requise).
9. **Lundi 02/11** : Jeu de la semaine (si marqueurs débloqués par Peter).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
