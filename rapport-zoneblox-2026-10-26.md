# 📊 Rapport ZoneBlox — 2026-10-26 (run 05h, lundi)

Heure locale Belgique : ~05h00. Mode : **FULL MAINTENANCE + EDITORIAL**.
Fenêtre de recherche : nuit du 25 au 26/10 (12–24 h). Aucun `git push` (publication manuelle).

---

## CODES

**Priorité absolue traitée en premier.** 13 pages vérifiées sur sources datées (ProGameGuides, Dexerto .com/.fr, Roblox Den, Nerdschalk, Samlover, Destructoid, TryhardGuides, roonby) + 1 vertical data-driven (Aniimo).

### 2 corrections de contenu (preuve à l'appui)
- **hypershot** : `ONEBILLION` **retiré → expiré**. Preuve d'expiration par **2 sources** (Dexerto.fr 01/10 + Dexerto.com). Page → **0 code actif**. `sixstoreys` (« 6 new codes ») contredit par les 2 sources fiables → **ignoré** (kill switch). Panneau « Dernière mise à jour » réécrit, listings synchronisés (index + tous-les-codes + codes.json).
- **100-days-at-sea** : `SPOOKY` (20 Pearls, Halloween) **ajouté**. Confirmé par **2 sources fraîches concordantes** (ProGameGuides 24/10 + Roblox Den 26/10), cohérent avec l'événement d'Halloween en cours. Page → **1 code actif**. `RIVAL` écarté (conflit actif/inactif entre les 2 sources).

### hotGames confirmés inchangés (verifDate → 26/10)
- **steal-a-brainrot** : `BESTBRAINROTEVER` = Dexerto 12/10 ✔
- **volleyball-legends** : `UPDATE_91 / REPLAYS / MVP` = Samlover 13/10 ✔
- **grow-a-garden** : `RDCAward / BEANORLEAVE10` = ProGameGuides 03/10 + Dexerto ✔
- **blue-lock-rivals** : 4 codes (`NELAIKU / HALLOWEEN / WSNAKE / SORRYFORDELAYAIKU`) présents sur roonby (modifié 24/10) ✔ (jeu très volatil — à resuivre)
- **pet-simulator-99** : 0 code (Nerdschalk : « no active codes ») ✔
- **anime-vanguards** : 14 codes anniversaire maintenus (aucune preuve d'expiration ; notre liste 25/10 plus fraîche que les agrégateurs) ✔
- **fisch** : 3/4 codes confirmés par Dexerto (`scarlet/SCARLET`, `TemporarySubmarine`, `CARBON`) ; `MarianaIsGoingCrazy` conservée ✔
- **steal-an-egg** : 0 code — **pas de système de codes** dans le jeu (Destructoid 22/10) ✔
- **spin-a-soccer-card** : **kill switch** (conflit total tryhardguides `release` vs Dexerto `STAR-STORM/THUNDER-DIAMOND`) → page reste à 0, à revérifier.

### Rotation
- **grow-a-garden-2** : 4 codes (`TEAMGREENBEAN / WATERYOPLANTS / REMEMBERTODRINKWATER / FREESEED`) = ProGameGuides 14/10 ✔
- **catalogVerify** : 12 jeux datés au 26/10.
- ⚠️ **Backlog rotation : 151 pages > 3 jours (dont 30 jamais vérifiées).** Chronique (voir CLAUDE.md). Priorisé ce run : hot games + qualité de contenu + éditorial (principe exactitude > quantité). Plan de rattrapage dans la queue.

### Candidats en attente (MONITOR, non publiés)
- `100-days` RIVAL (conflit) · `fisch` `CAVERN`/`ChapelTroubles` (mono-source roonby, FischFright) · `spin-a-soccer-card` (conflit) · `aniimazingfroyo` (expiré mono-source, US-only).

### Sources officielles
- GTA 6 : Rockstar Newswire (rien de neuf). Aniimo : via agrégateurs fiables (mein-mmo). Trello Blox Fruits/ALS déjà cartographiés (`code-watch.json`).

---

## SEO

- **Update before create respecté** : 2 pages existantes corrigées, **aucune nouvelle URL** créée (pas d'intention nouvelle justifiée cette nuit).
- **Fraîcheur** : verifDate rafraîchie sur 13 pages + `data/codes.json` (1329 codes actifs / 196 jeux) + sitemap (412 URLs, lastmod recalculés).
- **Anti-cannibalisation** : rien créé → aucun risque introduit.
- **Prochaine brique** : désambiguïsation placeId des clones anime (backlog) ; décision bloc « Jeu de la semaine ».

---

## NOUVEAUX JEUX
- Aucun ajout. **Steal an Egg** reste viral (Roblox trending oct.) mais page déjà au catalogue (0 code — pas de système). Aucun nouveau jeu avec **preuve d'intérêt multi-source + codes réels** cette nuit → **kill switch** (ne rien publier).

## CONTENU
- Guides / tier lists : aucune modification justifiée (pas d'évolution réelle — §23).
- Articles : aucun (pas de news confirmée nécessitant un article dédié).
- Mises à jour : 2 pages codes (hypershot, 100-days) + queue + intelligence.

## ANIIMO
- **Revérifié** : 15 codes reconfirmés (mein-mmo 09/10 : « no new codes, old ones still valid »). `data/aniimo/codes.json` → `lastChecked` 26/10, régénéré via `build_site.py`. `aniimazingfroyo` donné expiré par mein-mmo seul (code **US-only**) → conservé sous surveillance (pas de 2ᵉ source).
- **🆕 Season 1 Part II = 29/10** (confirmé). Préparer l'ingestion data-driven **après** l'officiel (nouveaux codes/créatures probables). Aucune invention avant confirmation.

## GTA 6
- **Inchangé.** Sortie **19/11/2026**, préchargement **12/11** + perks pré-commande = déjà connus. Newswire : rien de neuf cette nuit. Evergreen maintenu, séparation CONFIRMÉ/RAPPORTÉ/RUMEUR OK. Surveillance (heure préchargement / Trailer 3 / day-one).

## FC 27
- **Bloqué — décision Peter.** Les sources (EA, Dexerto, RealSport) confirment **EA Sports FC 27 (sorti 25/09/2026)** comme titre live, avec son calendrier de promos Ultimate Team d'automne ; le vertical `fc-27` est cohérent. La note du 25/10 (« FC 26 live / TOTY ») paraît erronée (TOTY = janvier). → **Peter : valider la couverture FC 27** pour débloquer l'Ultimate Team.

---

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) Aniimo S1 Part II 29/10 — à préparer ; (2) GTA 6 pré-lancement — monitorer Newswire ; (3) FischFright (codes Halloween) — 2ᵉ source requise.
- **Tendances** : Halloween partout (codes SPOOKY/BOO!/Halloween multi-jeux) ; Steal an Egg viral ; pré-lancement GTA 6.
- **Articles créés** : 0 (kill switch — rien de mûr/confirmé).
- **Pages mises à jour** : hypershot, 100-days-at-sea (+ data Aniimo).
- **Sujets ignorés** : « 6 new codes » Hypershot (sixstoreys, contredit) ; codes spin-a-soccer-card (conflit).
- **À surveiller** : RIVAL (100-days), ChapelTroubles/CAVERN (fisch), aniimazingfroyo (Aniimo), grimoires-era, rivals.
- `tools/editorial-intelligence.json` : topic `run-2026-10-26-05h` ajouté (61 topics), meta à jour.

## EDITORIAL QUEUE
- **Urgents** : GTA 6 (pré-lancement, Newswire).
- **À publier** : rien de neuf.
- **À mettre à jour** : grimoires-era (officiel), rivals (source fraîche), tap-simulator-reborn (casse SPOOKY), sell-fries (2ᵉ source 4 codes), type-soul (récompenses), listes gonflées (preuve d'expiration).
- **À préparer** : Aniimo 29/10 ; décisions Peter (naming FC 27, bloc Jeu de la semaine).
- **Demain (27/10)** : backlog rotation (30 jamais vérifiées, désambiguïsation placeId) ; FischFright 2ᵉ source ; spin-a-soccer-card ; GTA 6 Newswire.
- `EDITORIAL-QUEUE.md` réécrit.

---

## QC
- **Fichiers** : 23 modifiés. Tous terminés par `</html>` / `</urlset>`, **0 null byte** (vérif Python), structure HTML OK.
- **Tests** : `node --check js/main.js` ✔ · JSON valides (`codes.json`, `code-watch.json`, `editorial-intelligence.json`, `aniimo/codes.json`) ✔ · `sitemap.xml` well-formed (412 URLs) ✔.
- **Cohérence** : `data/codes.json` (hypershot count 0 ; 100-days SPOOKY/1) ✔ ; listings (index GAMES + tous-les-codes) synchronisés ✔ ; GA4 + navigation/Avatars présents sur hubs ✔.
- **CTA** : 100-days = 1 `guidelink` (OK) ; hypershot sans guide dédié (pré-existant, suivi dans la queue). Aucune duplication introduite.
- **Régénération** (ordre §29) : `build_site` → `build_home` → `build_codes_json` → `build_sitemap` ✔. `/avatar/` et `/games/` (hors Aniimo data-driven) non touchés.
- **Erreurs corrigées** : fausse alerte null-byte de `grep` (UTF-8 multi-octets) levée par contrôle binaire Python.

---

**Non exécuté (bloqué, escaladé Peter)** : « Jeu de la semaine » du lundi — les marqueurs `<!-- FEATURED-WEEK-START/END -->` restent **absents** d'`index.html`/`meilleurs-jeux-roblox.html` ; création à l'aveugle écartée (prudence).

---

Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
