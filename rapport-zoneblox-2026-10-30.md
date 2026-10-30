# Rapport ZoneBlox — 2026-10-30 (run 05h, vendredi)

**Mode : FULL MAINTENANCE + EDITORIAL.** Philosophie appliquée : EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ > SEO > QUANTITÉ. **Journée « reverification propre »** : 9 hotGames revérifiés via sources datées fraîches → **aucun changement de code justifié** (rien à inventer, kill switch maintenu sur les cas ambigus). **Correction importante du feed Aniimo** avec les patch notes officiels. **Git non poussé** (bloc de publication en fin de rapport).

---

## CODES

### hotGames — 9 revérifiés via sources datées, AUCUN changement

| Jeu | Source(s) datée(s) | Verdict |
|---|---|---|
| **steal-a-brainrot** | TimeSaver 08/10 + esportnow 04/10 | `BESTBRAINROTEVER` seul actif. `saturn` toujours non confirmé → non ajouté. |
| **grow-a-garden** | TimeSaver 27/10 (+ wiki) | `RDCAward` + `BEANORLEAVE10` **disputés** (wiki = aucun actif depuis 13/10 ; trackers = « try it »). Conflit → **gardés** (pas de preuve d'expiration, §4) ; `torigate` NON ajouté. |
| **blue-lock-rivals** | dexerto.fr 02/10, beatcopgame 17/10 | Sources accessibles **antérieures à l'update Aiku (~25/10)** → ne contredisent pas notre set. `SKELETON / AIKUCHANGES / SPOOKY` **maintenus**. |
| **volleyball-legends** | Roonby 24/10 (Update 93) | `UPDATE_93 / CURSED / TOURNAMENT` — match. |
| **fisch** | Roonby 24/10 (dump) | Nos 5 codes inchangés. `ChapelTroubles` **NOUVEAU** mais mono-source sans récompense → **MONITOR**. |
| **fruit-battlegrounds** | TimeSaver 18/10 | `EVENHIGHER!` (officiel) + `HIGHER1M120K` + `YOO1M110K!` — match. Prochain code à 1 140 000 likes. |
| **anime-vanguards** | next-stage.fr 29/10 | Source = **superset** (28 codes) ; nos 14 = sous-liste (under-list OK, §4). `2ndAnniDay7` mono-source → **MONITOR** (2ᵉ source avant ajout). |
| **blox-fruits** | next-stage.fr 30/10 | Nos 23 **tous confirmés actifs**. `Chandler` (erreur probable) + `pleasezakineedthis` (mono) non ajoutés. |
| **anime-last-stand** | switchbladegaming 26/10 | `MagicKnights! / ElfReincarnation! / IsItReallyWeekly?!` — match (`ElfReincarnation!` disputé, gardé §4). |

- **hotGames** : rafraîchi `verifDate` → **30/10** sur les 9 pages + `catalogVerify` 30/10.
- **Codes ajoutés** : 0. **Codes expirés** : 0. (Aucune preuve de changement ⇒ aucune modification — règle d'honnêteté.)
- **« Mis à jour le »** et `dateModified` (JSON-LD) : **inchangés** (codes non modifiés). Seul `verifDate` « rajeunit » les pages.
- **Total codes actifs du site** : **1338** (data/codes.json régénéré).

### Candidats en attente / kill switch
- **Fisch `ChapelTroubles`** (mono-source, pas de récompense) → MONITOR, 2ᵉ source datée requise.
- **Anime Vanguards `2ndAnniDay7`** (next-stage.fr 29/10 seul) → MONITOR ; complèterait la série Day1-6.
- **grow-a-garden `torigate`** (disputé) → non ajouté.
- **blue-lock-rivals `SPOOKY`** : récompense exacte toujours non détaillée par les sources.

### Sources officielles consultées
Descriptions in-game / notices via médias fiables datés (TimeSaver, Roonby, next-stage.fr, switchbladegaming, esportnow). Canaux Discord/Trello officiels non accessibles depuis cet environnement → recoupement multi-sources daté.

### Rotation (lot 05h)
- **Non traité ce run.** Le lot (38 pages non-hot, dont 31 jamais vérifiées — majorité novelty FR + clones anime à désambiguïser) laissé au profit de la vérification exacte des 9 hotGames + verticales éditoriales. Backlog chronique : **167 pages non-hot > 3 j**. À reprendre avec sources fraîches/officielles.

---

## SEO
- **Intentions travaillées** : « codes <hotGame> » (long-tail winnable) — **revérification/fraîcheur** des pages existantes, **aucune nouvelle URL** (UPDATE before CREATE respecté).
- **Anti-cannibalisation** : aucune page créée ; maillage/CTA intacts (CTA `guidelink` unique vérifié sur les 9 pages).
- **Fraîcheur** : `verifDate` 30/10 sur 9 pages ; `sitemap.xml` régénéré (421 URLs ; lastmod : 206 via verifDate, 12 via « Mis à jour le », 203 via mtime). `dateModified` non touché (codes inchangés).
- **Prochaine brique** : cluster Aniimo Part II **data-driven** dès publication des données officielles des 51 créatures.

## NOUVEAUX JEUX
- **Aucun ajout.** Aucun nouveau jeu avec **preuve d'intérêt multi-source + codes réels** détecté (recherches overnight = listicles/dumps recyclés). Kill switch, 0 nouvelle URL.

## CONTENU
- **Guides / events (Halloween)** : couverture déjà en place (Fisch `FischFright2026` actif jusqu'au 09/11, Blue Lock Rivals `SPOOKY`, 100-days-at-sea `SPOOKY`). **Aucune nouvelle section** justifiée ce run (pas de nouvel event confirmé ni de récompense détaillée). ⚠️ **Retrait des sections event programmé au run 05h du 01/11** (sauf FischFright2026 jusqu'au 09/11).
- **Tier lists** : aucune modification (pas d'évolution réelle justifiant une nouvelle version).
- **Articles** : 0 (qualité > quantité).

## ANIIMO
- **Correction majeure du feed** `data/aniimo/updates.json` : les **patch notes officiels** (Pawprint Studio / notice Steam, via gamerfuzion 27/10) **supersèdent la roadmap du 29/10** ingérée hier. Chiffres corrigés :
  - **51 nouveaux Aniimo** (et non 32), dont **Jaguaraun** (1er Aniimo co-créé par la communauté).
  - **Niveau maximum porté à 70** (personnage + Aniimo).
  - **Spar = duels PvP 4v4 en temps réel** (et non « 1v1 » de la roadmap) ; **Operation: Egg Heist** = PvP 3 équipes (en test).
  - Refonte Sparkling Hue, titres Trailblazer II/III, Orbe Prismana modifié ; Holo-Battle (paliers + difficulté Trial) ; Home (camping-car 3 étages, météo, blueprints partageables, Glow Scooter niv. 20) ; évènement **Magical Wonder Night jusqu'au 10/12**.
  - **LIVE** après la maintenance 28-29/10. **Aucun nouveau code** annoncé.
- **Stats détaillées des 51 créatures NON ingérées** (données officielles complètes attendues) → ingestion `creatures.json`/`locations.json`/`tier-list.json` dès disponibilité, sans invention. Page régénérée (`build_site.py`) : figures corrigées rendues.

## GTA 6
- **Aucun nouveau post Newswire officiel** depuis Edge #430 (29/10). Sortie **19/11** + préchargement **12/11** maintenus. Rumeurs « website update » / Instagram = **spéculation non publiable**. Séparation CONFIRMÉ / RAPPORTÉ / RUMEUR maintenue. Surveillance Newswire poursuivie.

## FC 27
- **Ultimate Scream Team 2** : attendue **ven 30/10 18:00 UTC** (= **après** l'heure du run 05h) et **NON confirmée par EA** (fut.gg 23/10, basé sur l'historique). **Pas de publication** ce run (kill switch sur non-confirmé + sortie postérieure au run). Confirmés : promo Ultimate Scream jusqu'au **06/11**, token store **13/11**, upgrade Beaver Moon 24/11→01/12. **À traiter aux runs 15h/22h** dès la sortie réelle (équipe + éventuelle solution DCE vérifiée, sans invention).

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) FC 27 Ultimate Scream Team 2 (aujourd'hui 18:00 UTC) ; (2) Aniimo Part II LIVE — ingestion data créatures ; (3) GTA 6 pré-lancement (Newswire).
- **Tendances** : aucune nouvelle tendance Roblox exploitable cette nuit (bruit/spam sur les recherches overnight).
- **Articles créés** : 0.
- **Pages mises à jour** : 9 pages codes (verifDate) + feed Aniimo corrigé + feeds régénérés.
- **Sujets ignorés** : squid-game-x (extras single-source), brainrot-evolution (sources en vrac).
- **Sujets à surveiller** : Aniimo LIVE (data + codes de lancement), FC 27 Team 2, GTA 6 Newswire, Blue Lock Rivals (reward SPOOKY), Fisch (ChapelTroubles), Anime Vanguards (2ndAnniDay7).
- `tools/editorial-intelligence.json` mis à jour (69 sujets ; meta 30/10 ; aniimo-s1-partii corrigé → figures officielles ; fc27 + gta6 re-datés ; run-log 30/10 ajouté). `tools/code-watch.json` : `_notes2026-10-30` + `lastRun` 30/10 + 9 `catalogVerify`.

## EDITORIAL QUEUE
- **Urgents** : Aniimo (ingérer data officielle 51 créatures dès dispo + codes de lancement) ; GTA 6 (Newswire) ; FC 27 Team 2 (15h/22h).
- **À publier** : rien de neuf.
- **À mettre à jour** : FC 27 Team 2 ; Fisch `ChapelTroubles` (2ᵉ source) ; Anime Vanguards `2ndAnniDay7` (2ᵉ source) ; brainrot-evolution ; Blue Lock Rivals (reward `SPOOKY`) ; Fisch Mariana/TemporarySubmarine ; grimoires-era/rivals/type-soul ; listes gonflées (preuve d'expiration).
- **À préparer / décision Peter** : bloc « Jeu de la semaine » (marqueurs absents — bloqué) ; feed prix cartes FC 27 ; /avatar/ (NE PAS MODIFIER).
- **Prochain run (15h/22h 30/10 ; 05h 31/10)** : FC 27 Team 2 ; Aniimo data ; GTA 6 Newswire ; Blue Lock Rivals (reward) ; backlog rotation (31 jamais vérifiées) ; **retrait sections Halloween au 01/11**.

## QC
- **Fichiers modifiés (20)** : 9 pages codes (verifDate) + EDITORIAL-QUEUE.md + data/aniimo/updates.json + tools/editorial-intelligence.json + tools/code-watch.json + régénérés (data/codes.json, data/games-index.json, index.html, actualites/index.html, games/aniimo/updates/index.html, sitemap.xml, sitemap-games.xml).
- **Tests** : `node --check js/main.js` **OK** ; déséquilibre `<div>` site entier (hors /avatar/) = **0** ; **0 null byte** sur les pages touchées ; toutes finissent par `</html>` ; `data/codes.json` (199 jeux, 1338 codes), `data/games-index.json`, `data/aniimo/updates.json`, les 2 JSON tools **valides** ; `sitemap.xml` XML valide (421 URLs, se termine par `</urlset>`) ; GA4 (`G-FEL71QVHNL`) / nav / `data-cta="guidelink"` **unique** présents sur les 9 pages codes ; cache `main.js?v=48` cohérent (188 pages ; /avatar/ hors périmètre).
- **Build** : `build_site` → `build_home` → `build_codes_json` → `build_sitemap` (ordre §29 respecté). Figures Aniimo corrigées bien rendues dans la page générée.
- **Erreurs corrigées** : aucune corruption. `js/main.js` non modifié → pas de bump de cache.

---

**Pour publier** : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)
