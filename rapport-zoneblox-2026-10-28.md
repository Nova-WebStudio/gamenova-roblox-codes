# Rapport ZoneBlox — 2026-10-28 (run 05h, mercredi)

**Mode : FULL MAINTENANCE + EDITORIAL.** Philosophie appliquée : EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ > SEO > QUANTITÉ. 1 vrai changement de codes bien sourcé, 5 hotGames revérifiés inchangés, kill switch sur les cas conflictuels. Aucune invention. **Git non poussé** (bloc de publication en fin de rapport).

---

## CODES

### Changement publié (2 sources concordantes)
- **Volleyball Legends — Update 93 « Cursed Tournaments »** : page passée de `UPDATE_91 / REPLAYS / MVP` à :
  - `UPDATE_93` → 5 Lucky Style Spins
  - `CURSED` → 5 Lucky Style Spins
  - `TOURNAMENT` → 5 Lucky Ability Spins
  (3 codes actifs, niveau 15 requis). `UPDATE_91 / REPLAYS / MVP` + `UPDATE_92 / MAMORI / PARRY` passés en expirés.
  **Sources** : TimeSaver.gg (24/10) + Roonby (24/10) — listes concordantes sur l'actif. Dates « Mis à jour le » (prose) + `verifDate` + JSON-LD (`dateModified` 2026-10-28 + ItemList) synchronisées. `build_codes_json` relancé.

### hotGames revérifiés — inchangés (verifDate → 28/10, catalogVerify → 28/10)
- **king-legacy** : **match parfait** 9/9 avec Pocket Tactics (23/10).
- **grow-a-garden** : match exact (RDCAward, BEANORLEAVE10) avec gfinityesports (vérifié 21/10).
- **steal-a-brainrot** : match (BESTBRAINROTEVER) avec Dexerto (12/10).
- **fisch** : 3/4 confirmés (scarlet, TemporarySubmarine, CARBON) via Pocket Tactics (07/10) ; `MarianaIsGoingCrazy` conservé (pas de preuve d'expiration, règle §4).
- **blox-fruits** : jeu statique, aucun nouveau code depuis Pâques (Pocket Tactics 23/10) → inchangé.

### Kill switch / candidats en attente
- **Blue Lock Rivals** : **conflit 3 voies** — Dexerto (25/10) SKELETON/AIKUCHANGES/NEW ; Insider Gaming (codes hiver recyclés) ; notre page (codes Halloween). Aucune paire concordante → **page NON modifiée**. Nos codes Halloween probablement expirés (fin event 31/10). **Source officielle requise** (Discord/Trello/X).
- **Anime Vanguards, Fisch (MarianaIsGoingCrazy), fruit-battlegrounds** : sources agrégées divergentes/périmées → non modifiés.

### Sources officielles consultées
- Aniimo : preview devs (playnews 20/10). GTA 6 : Rockstar Newswire (rien de neuf). FC 27 : fut.gg (dates promo). Les canaux officiels in-game/Discord non accessibles depuis cet environnement (vérification via médias fiables datés).

---

## SEO
- **Intention travaillée** : « codes volleyball legends » (hotGame, MAJ fréquentes, long-tail winnable) — mise à jour (UPDATE before CREATE), pas de nouvelle URL.
- **Anti-cannibalisation** : aucune nouvelle page créée. Maillage/CTA des pages touchées intacts.
- **Fraîcheur** : `dateModified` (JSON-LD) resynchronisé uniquement là où les codes ont réellement changé (Volleyball Legends) ; `verifDate` rafraîchi sur les 6 pages revérifiées.
- **Prochaine brique** : cluster Aniimo Part II (data-driven) dès l'officiel 29/10.

## NOUVEAUX JEUX
- Aucun ajout ce run : aucun nouveau jeu avec **preuve d'intérêt multi-source + codes réels** détecté (recherches tendances = résultats spam/recyclés).

## CONTENU
- Guides : aucune section event écrite (Fisch FischFright 2026 = aucun code confirmé → rien à écrire ; kill switch respecté).
- Tier lists : aucune modification (pas d'évolution réelle justifiant une nouvelle version).
- Articles : aucun.
- Mises à jour : 1 page codes (Volleyball Legends) + 5 rafraîchissements de vérification.

## ANIIMO
- **Season 1 Part II confirmée pour le 29/10 (demain)**. Fin de la Part I : **28/10 23h59 UTC (ce soir)**. Contenu confirmé (preview devs playnews 20/10) : région Whisperwake Isles, 51 nouveaux Aniimo (32 espèces), nouveaux Prismana, PvP 1v1 permanent, Vein Abundance 30/10→06/12. **Aucun nouveau code annoncé.** → Ingestion data-driven (`data/aniimo/` → `build_site.py`) **après l'officiel du 29/10**. Rien publié aujourd'hui (règle : ne rien publier avant l'officiel).

## GTA 6
- **Rien de neuf confirmé au 28/10.** Sortie **19/11/2026** confirmée, préchargement **12/11** confirmé. « News update » toujours **rapporté** (non primaire) pour le **29/10** → surveillance du Rockstar Newswire à chaque run. Pages evergreen inchangées. Séparation CONFIRMÉ / RAPPORTÉ / RUMEUR maintenue.

## FC 27
- **Ultimate Scream Team 2** : seulement **« attendue » ~30/10 18:00 UTC** (NON confirmée EA — fut.gg). **Pas de publication** (kill switch sur non-confirmé). Confirmés : token store jusqu'au 13/11, upgrade Beaver Moon 24/11→01/12. Promo en cours jusqu'au 06/11. À publier dès la sortie réelle (+ 1 solution DCE Woltemade vérifiée, sans invention).

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) Aniimo Part II 29/10 (cluster data-driven) ; (2) FC 27 Ultimate Scream Team 2 ~30/10 ; (3) GTA 6 pré-lancement.
- **Tendances** : pas de nouvelle tendance Roblox exploitable (bruit/spam sur les recherches overnight).
- **Articles créés** : 0 (qualité > quantité).
- **Pages mises à jour** : codes-volleyball-legends.html + 5 revérifs.
- **Sujets ignorés** : Blue Lock Rivals (conflit non tranché), FischFright 2026 (aucun code).
- **Sujets à surveiller** : Aniimo 29/10, FC 27 Team 2, GTA 6 Newswire, Blue Lock Rivals (source officielle).
- `tools/editorial-intelligence.json` mis à jour (68 sujets ; meta 28/10 ; +volleyball-upd93, +fisch-fischfright, +run-log 28/10).

## EDITORIAL QUEUE
- **Urgents** : Aniimo Part II (29/10) ; GTA 6 (Newswire) ; Blue Lock Rivals (conflit).
- **À publier** : rien de neuf.
- **À mettre à jour** : FC 27 Team 2 (~30/10) ; fruit-battlegrounds, grimoires-era, rivals, type-soul ; listes gonflées (preuve d'expiration requise).
- **À préparer / décision Peter** : bloc « Jeu de la semaine » (marqueurs absents — bloqué) ; feed prix cartes FC 27 ; /avatar/ encore en cache v=43 (dossier NE PAS MODIFIER).
- **Demain (05h 29/10)** : ingestion Aniimo officielle ; FC 27 Team 2 ; GTA 6 Newswire ; Blue Lock Rivals source officielle ; Volleyball Legends (prochain Update) ; backlog rotation (~30 jamais vérifiées).

## QC
- **Fichiers** : 6 pages codes + EDITORIAL-QUEUE.md + editorial-intelligence.json + code-watch.json (seules les 6 dates catalogVerify changées, reste identique) + regénérés (data/codes.json, data/games-index.json, sitemap.xml, sitemap-games.xml).
- **Tests** : `node --check js/main.js` OK ; déséquilibre `<div>` site entier = **0** ; 0 null byte ; toutes les pages finissent par `</html>` ; `data/codes.json` & `data/games-index.json` JSON valides ; `sitemap.xml` XML valide (418 URLs, se termine par `</urlset>`) ; GA4 (G-FEL71QVHNL) / nav active / `data-cta="guidelink"` présents sur les 6 pages ; cache `main.js?v=48` cohérent (sauf 3 pages /avatar/ en v=43, dossier hors périmètre).
- **Build** : `build_site` → `build_home` → `build_codes_json` → `build_sitemap` (ordre respecté). Pas de drift sur les pages data-driven.
- **Erreurs corrigées** : aucune (aucune corruption détectée).

---

**Pour publier** : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)
