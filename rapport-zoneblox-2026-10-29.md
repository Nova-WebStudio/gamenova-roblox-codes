# Rapport ZoneBlox — 2026-10-29 (run 05h, jeudi)

**Mode : FULL MAINTENANCE + EDITORIAL.** Philosophie appliquée : EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ > SEO > QUANTITÉ. **3 changements de codes bien sourcés** (dont la résolution de **2 conflits laissés ouverts hier**), **9 hotGames revérifiés inchangés**, ingestion éditoriale Aniimo Part II + GTA 6 Edge. Aucune invention ; kill switch sur les cas ambigus. **Git non poussé** (bloc de publication en fin de rapport).

---

## CODES

### hotGames — changements publiés (≥ 2 sources concordantes)

1. **Blue Lock Rivals — conflit d'hier TRANCHÉ.** Hier la page était bloquée (conflit 3 voies, kill switch). Aujourd'hui 2 sources récentes concordantes — **Dexerto (25/10)** + **Game.guide (28/10)** — confirment que les codes ont tourné avec l'update Aiku :
   - **Actifs désormais** : `SKELETON` (5 Lucky Spins), `AIKUCHANGES` (5 Lucky Flow Spins), `SPOOKY` (récompense non détaillée par les sources).
   - **Expirés** : `NELAIKU`, `HALLOWEEN`, `WSNAKE`, `SORRYFORDELAYAIKU` (nos 4 anciens).
   - TimeSaver (22/10) listait encore les anciens = simplement **antérieur** à l'update, pas un conflit.
   - Synchronisé : liste actifs/expirés, compteur hero (4→3), `const ACTIVE`, prose + section « Dernière mise à jour », `verifDate` 29/10, JSON-LD `dateModified` 2026-10-29 + ItemList.

2. **Fisch — code Halloween `FischFright2026` ajouté** (actif, expire 09/11), confirmé par **TimeSaver (27/10)** + **Roonby (24/10)**. `scarlet` + `CARBON` reconfirmés actifs. `MarianaIsGoingCrazy` / `TemporarySubmarine` conservés (non listés actifs par TimeSaver mais **pas de preuve d'expiration**, règle §4). JSON-LD + compteur (4→5) + dates synchronisés.

3. **Fruit Battlegrounds — conflit d'hier RÉSOLU.** `OMGUPDATE22` (**disputé** : certains trackers l'indiquent expiré — TimeSaver 18/10 ; cohérent avec la note interne du 03/09) repassé en **expiré**. Actifs confirmés gardés : `EVENHIGHER!`, `HIGHER1M120K`, `YOO1M110K!` (TimeSaver 18/10). `verifDate` 29/10, `dateModified` 2026-10-29.

### hotGames revérifiés — inchangés (verifDate → 29/10, catalogVerify → 29/10)

- **grow-a-garden** : match exact (RDCAward, BEANORLEAVE10) — gfinityesports (vérifié 28/10).
- **steal-a-brainrot** : `BESTBRAINROTEVER` seul confirmé (Dexerto 12/10 + TimeSaver 08/10) ; `saturn` non confirmé → non ajouté.
- **volleyball-legends** : match exact `UPDATE_93 / CURSED / TOURNAMENT` (TimeSaver 24/10).
- **king-legacy** : core 5 confirmé (TimeSaver 20/10), nos 9 = **superset** (codes YouTuber longue durée) — pas de preuve d'expiration.
- **blade-ball** : superset OK (TimeSaver 20/10) — pas de preuve d'expiration sur SERPENT / DUNGEONSRELEASE.
- **anime-vanguards** : set 2ᵉ anniversaire présent (Roonby 13-24/10).
- **pet-simulator-99** : **0 code** confirmé (gfinity 26/10 : jeu arrêté, codes merch uniquement) — page déjà à 0.
- **tower-defense-simulator** : 2 codes `1MILCOMMUNITY / 2MILLION` (TimeSaver 26/10 + Dexerto 15/09), **aucun** code Halloween actif.
- **squid-game-x** : nos 6 codes confirmés actifs (next-stage.fr 29/10).

### Codes ajoutés / expirés (bilan)
- **Ajoutés** : `FischFright2026` (Fisch) ; `SKELETON`, `AIKUCHANGES`, `SPOOKY` (Blue Lock Rivals).
- **Expirés** : `OMGUPDATE22` (Fruit Battlegrounds) ; `NELAIKU`, `HALLOWEEN`, `WSNAKE`, `SORRYFORDELAYAIKU` (Blue Lock Rivals).
- Total codes actifs du site : **1334** (vs 1335 hier).

### Candidats en attente / kill switch
- **squid-game-x** : next-stage.fr (29/10) liste **59 codes** actifs ; nos 6 y figurent, mais les ~53 autres sont majoritairement des **codes génériques single-source** (STACKED, NEVERLOSE, WINBIG…) → **NON ajoutés** (risque faux-actifs §4). MONITOR, 2ᵉ source requise.
- **brainrot-evolution** : sources en vrac (dexerto.fr + allthings = dumps mélangés, mal datés). Codes Halloween possibles (HALLOWEEN2026…) **non confirmables proprement** → page inchangée, source fraîche propre requise.
- **Blue Lock Rivals `SPOOKY`** : récompense exacte non détaillée par les sources → à préciser (source officielle).
- **Fisch Mariana / TemporarySubmarine** : expiration à confirmer via 2ᵉ source (gardés faute de preuve).

### Sources officielles consultées
- Aniimo : roadmap officielle devs (gamewith.ai, maj 22/10). GTA 6 : couverture Edge #430 (29/10). FC 27 : fut.gg (dates promo). Canaux in-game/Discord non accessibles depuis cet environnement → recoupement via médias fiables datés.

### Rotation (lot 05h)
- **Non traité ce run.** Le lot de rotation (38 pages non-hot, dont ~30 jamais vérifiées — majorité novelty FR + clones anime à désambiguïser) a été laissé au profit de la vérification approfondie et exacte des 12 hotGames ci-dessus. Backlog chronique : **~165 pages non-hot > 3 j**. À reprendre avec sources fraîches/officielles (voir Editorial Queue).

---

## SEO
- **Intentions travaillées** : « codes blue lock rivals », « codes fisch » (hotGames, MAJ fréquentes, long-tail winnable) — **mise à jour** des pages existantes (UPDATE before CREATE), aucune nouvelle URL.
- **Anti-cannibalisation** : aucune page créée ; maillage/CTA des pages touchées intacts (CTA unique vérifié).
- **Fraîcheur** : `dateModified` (JSON-LD) resynchronisé **uniquement** là où les codes ont réellement changé (Blue Lock Rivals, Fisch, Fruit Battlegrounds) ; `verifDate` rafraîchi sur les 12 pages revérifiées ; `sitemap.xml` régénéré (lastmod : 205 via verifDate, 12 via « Mis à jour le », 201 via mtime).
- **Prochaine brique** : cluster Aniimo Part II (data-driven) dès le passage LIVE officiel.

## NOUVEAUX JEUX
- **Aucun ajout.** Aucun nouveau jeu avec **preuve d'intérêt multi-source + codes réels** détecté cette nuit (recherches tendances = listicles SEO / spam recyclé). Kill switch, 0 nouvelle URL.

## CONTENU
- **Guides / events** : couverture Halloween — code `FischFright2026` publié (Fisch) ; `SPOOKY` publié (Blue Lock Rivals) ; Tower Defense Simulator vérifié = **aucun** code Halloween. Pas de nouvelle section de guide dédiée écrite (récompenses non détaillées par les sources → kill switch sur les détails).
- **Tier lists** : aucune modification (pas d'évolution réelle justifiant une nouvelle version).
- **Articles** : aucun.
- **Mises à jour** : 3 pages codes modifiées + 9 revérifications + 2 feeds d'actualité (Aniimo, GTA 6).

## ANIIMO
- **Season 1 Part II / Whisperwake Isles** : entrée ajoutée à `data/aniimo/updates.json` (contenu **annoncé** par la roadmap officielle devs, gamewith.ai maj 22/10) : région archipel Whisperwake Isles (4 zones), **32 nouvelles espèces** (4 formes Prismana), 3 quêtes, **PvP 1v1 permanent** + Egg Heist fair-play, Aniimo Dash / Holo-Battle (temps limité), Aniimo saisonniers (Hypnyto/Ekrim 29/10→09/12, Hoptail 06-19/11, Jaguaraun 20/11→09/12), déblocage Lv.55 / I Trailblazer, Vein Abundance 30/10→29/11, Prismana Carnival 30/11→06/12. **Aucun nouveau code annoncé.**
- **Statut** : la roadmap (maj 22/10) présente l'update comme **prévu le 29/10**, pas encore confirmé LIVE à l'heure du run. **Stats des 32 créatures NON inventées** → ingestion data détaillée (`creatures.json`/`locations.json`/`tier-list.json`) seulement une fois l'update **LIVE** et les données officielles disponibles (runs 15h/22h).

## GTA 6
- **Edge #430** (en kiosque et **gratuit en ligne le 29/10**) : dossier exclusif de 16 pages — visite du studio Rockstar North (Édimbourg), nouvelles images, interviews, couverture gatefold Jason/Lucia. Ajouté à `data/gta-6/updates.json`. **Aucun report** : sortie **19/11** maintenue, préchargement **12/11**. Séparation CONFIRMÉ / RAPPORTÉ / RUMEUR maintenue. Surveillance Newswire poursuivie à chaque run.

## FC 27
- **Ultimate Scream Team 2** : toujours **« attendue » ~30/10 18:00 UTC**, **NON confirmée par EA** (fut.gg 22/10). **Pas de publication** (kill switch sur non-confirmé). Confirmés : promo Ultimate Scream jusqu'au **06/11**, token store jusqu'au **13/11**, upgrade Beaver Moon 24/11→01/12. Token players confirmés (Jill Scott, Verón, Le Fée, El Mala, Tverskov). À publier dès la sortie réelle (+ 1 solution DCE Woltemade vérifiée, sans invention).

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) Aniimo Part II — ingestion data dès LIVE ; (2) FC 27 Ultimate Scream Team 2 ~30/10 ; (3) GTA 6 pré-lancement (Edge #430 aujourd'hui).
- **Tendances** : aucune nouvelle tendance Roblox exploitable (bruit/spam sur les recherches overnight).
- **Articles créés** : 0 (qualité > quantité).
- **Pages mises à jour** : 3 pages codes (Blue Lock Rivals, Fisch, Fruit Battlegrounds) + 9 revérifs + feeds Aniimo & GTA 6.
- **Sujets ignorés** : squid-game-x (53 codes single-source), brainrot-evolution (sources en vrac).
- **Sujets à surveiller** : Aniimo LIVE, FC 27 Team 2, GTA 6 Newswire, Blue Lock Rivals (reward SPOOKY), Volleyball Legends (prochain Update).
- `tools/editorial-intelligence.json` mis à jour (68 sujets ; meta 29/10 ; blue-lock-rivals → UPDATED, fisch-fischfright → PUBLISHED, aniimo-s1-partii → UPDATED, gta6 note Edge). `tools/code-watch.json` : snapshots des 3 jeux modifiés + `_notes2026-10-29` + 9 `catalogVerify` du jour.

## EDITORIAL QUEUE
- **Urgents** : Aniimo (confirmer LIVE + ingérer data) ; GTA 6 (Newswire).
- **À publier** : rien de neuf.
- **À mettre à jour** : FC 27 Team 2 (~30/10) ; brainrot-evolution, grimoires-era, rivals, type-soul ; Blue Lock Rivals (reward SPOOKY) ; Fisch (Mariana/TemporarySubmarine) ; listes gonflées (preuve d'expiration requise).
- **À préparer / décision Peter** : bloc « Jeu de la semaine » (marqueurs absents — bloqué) ; feed prix cartes FC 27 ; /avatar/ en cache v=43 (dossier NE PAS MODIFIER).
- **Prochain run (15h/22h 29/10 ; 05h 30/10)** : Aniimo LIVE ; FC 27 Team 2 ; GTA 6 Newswire ; Blue Lock Rivals (reward) ; backlog rotation (~30 jamais vérifiées désambiguïsables) ; retrait sections Halloween après 31/10.

## QC
- **Fichiers modifiés (25)** : 12 pages codes + EDITORIAL-QUEUE.md + data/aniimo/updates.json + data/gta-6/updates.json + tools/editorial-intelligence.json + tools/code-watch.json + régénérés (data/codes.json, data/games-index.json, index.html, actualites/index.html, games/aniimo/updates, games/gta-6/updates, sitemap.xml, sitemap-games.xml).
- **Tests** : `node --check js/main.js` OK ; déséquilibre `<div>` site entier = **0** ; **0 null byte** ; toutes les pages touchées finissent par `</html>` ; `data/codes.json`, `data/games-index.json`, les 2 updates.json + les 2 JSON tools **valides** ; `sitemap.xml` XML valide (418 URLs, se termine par `</urlset>`) ; GA4 (G-FEL71QVHNL) / nav / `data-cta="guidelink"` (unique) présents sur les pages codes ; cache `main.js?v=48` cohérent (186 pages ; 3 pages `/avatar/` en v=43 = dossier hors périmètre, NE PAS MODIFIER).
- **Build** : `build_site` → `build_home` → `build_codes_json` → `build_sitemap` (ordre respecté). Pas de drift sur les pages data-driven ; entrées Aniimo (Whisperwake) et GTA 6 (Edge #430) bien rendues dans les pages générées.
- **Erreurs corrigées** : une tentative d'écriture de `EDITORIAL-QUEUE.md` via base64 en shell a produit un fichier corrompu ; **détecté et corrigé** immédiatement (réécriture propre, UTF-8 validé). Aucune autre corruption.
- `js/main.js` non modifié → pas de bump de cache nécessaire.

---

**Pour publier** : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)
