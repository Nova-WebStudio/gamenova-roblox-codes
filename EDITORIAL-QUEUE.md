# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-22 (run 05h — jeudi)**

## ✅ FAIT — RUN 05h 2026-10-22

- **Codes — 1 édition propre, non destructive :**
  - **Knockout** → **PRUNE 7 → 2** (EMPERORRETURNS + THANKSFORPLAYING). Retirés **CRABRAVE / SOCIALHUB / PUNCHMONKEY / DOOMSDAY / ADMINABUSE** = expirés confirmés par **2 sources concordantes** (Dexerto 13/08 + Nerdschalk 23/09). numberOfItems + counter hero + ItemList JSON-LD + dateModified + GAMES_INDEX (main.js) + carte hub (tous-les-codes) tous resynchronisés. CORALCRUSHER (nerdschalk seul, sans récompense) → non ajouté.
- **Hot games — re-vérifiés, confirmés, 0 autre édition** : anime-vanguards (Roonby 13/10 = notre set), grow-a-garden (PocketGamer 03/10 + Roonby 08/10 = RDCAward/BEANORLEAVE10), steal-a-brainrot (Dexerto 12/10 = BESTBRAINROTEVER), blox-fruits (PocketTactics 16/10), blue-lock-rivals (sources + anciennes que page → conservée), fisch (Roonby 17/10 contradictoire → inchangé). Dates « 🔄 Vérifié le » rafraîchies (6 pages).
- **KILL SWITCH maintenu** : grimoires-era (conflit 3 voies, PocketGamer stale 11/2025 vs Games.gg sans récompenses — date NON rafraîchie), anime-battle-rng (nerdschalk = allthings.how = même contenu syndiqué Aug 6, 1 source stale dupliquée), aniimo-froyo (mein-mmo 09/10 expiré vs khelnow 04/10 actif = 1 source fraîche d'expiration), grow-a-garden FREESEED/torigate (1 source / conflit).
- **GTA 6 / FC 26 / Aniimo** : aucun changement actionnable (voir sections rapport).
- **Régénération** : build_site + build_home + build_codes_json (**1317 codes / 196 jeux**) + build_sitemap (**411 URLs**). **QC OK** (node main.js, JSON ×5, sitemap XML, `</html>`, 0 null byte, divs équilibrés, knockout ACTIVE=counter=ItemList=GAMES_INDEX=hub=2).

---

## 🔥 URGENT

- **GTA 6** — ~1 mois avant lancement (**19/11/2026**). Préchargement **12/11** confirmé (digital + physique). Surveiller le **Rockstar Newswire** à chaque run (heure de préchargement, patch day-one). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Rien de neuf 21→22/10.

## 🟢 À PUBLIER

_(rien)_ — kill switch sur tous les conflits ; aucun nouveau jeu Roblox avec preuve d'intérêt multi-source **+ codes réels** cette nuit.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **grimoires-era — PÉRIMÉE (conflit 3 voies).** Rebuild via **source officielle** (Trello/Discord) requis ; sources web discordantes/stales. Ne rien éditer tant que non tranché.
- **rivals — gros décalage de version.** Page FREE182 vs sources FREE201/COMMUNITY26. Besoin d'une source **marquant clairement l'actif**.
- **anime-battle-rng — gonflée (~35 codes).** Les 2 sources trouvées (nerdschalk, allthings.how) sont le **même contenu syndiqué** (Aug 6) → il faut 2 sources **indépendantes et fraîches** pour pruner.
- **haze-piece** — PHANTOMSHIP + OKUCHI → Roonby seul ; besoin 2ᵉ source.
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses.
- **noob-incremental — MUST_UPDATE.** Rewrite + resync `const ACTIVE`/compteur.
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : republier **seulement** là où ≥2 sources concordent.

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Naming FC 27 vs FC 26** : titre EA live = **FC 26** (promo Ultimate Scream / Halloween LIVE). Bloque la couverture Ultimate Team. **À trancher.**
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents du code** → étape du lundi non exécutable. À Peter : ajouter les marqueurs ou confirmer le mécanisme.
- **⚠️ Listes gonflées** : anime-battle-rng (~35), anime-astral-simulator (~100), dragon-blox (~82) : rebuild sur set vérifié-actif, ou maintien ? **Rotation en retard** depuis 10/09.
- **CTA manquant** : `codes-da-hood.html`, `codes-rivals.html`, `codes-knockout.html` n'ont **pas** de `data-cta="guidelink"` (pré-existant, pas de guide/tier dédié). À ajouter si des pages dédiées existent.
- **Note cache obsolète** : CLAUDE.md dit « main.js?v=19 » mais le site est à **v47** (181 HTML) + 3 stragglers **v43** (tous `/avatar/` = off-limits). À corriger dans CLAUDE.md.

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : grimoires-era (conflit 3 voies), rivals (version en retard), anime-battle-rng (gonflée, sources syndiquées), haze-piece (PHANTOMSHIP/OKUCHI), grand-piece-online (5FREETAILORVOUCHERS_2/ANOTHER), da-hood (ESKETIT 1 source), garden-tower-defense (conflit), aniimo (aniimazingfroyo = 1 source fraîche d'expiration).
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (>40 j) ; ~30 jeux jamais entrés dans catalogVerify (beaucoup = stubs sans codes).

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 23/10)

1. **grimoires-era** : source officielle (Trello/Discord) → rebuild propre.
2. **anime-battle-rng** : 2 sources **indépendantes + fraîches** (non syndiquées Aug 6) → élaguer.
3. **rivals** : source fraîche marquant l'actif → combler le décalage FREE182→FREE201.
4. **aniimo-froyo** : 2ᵉ source d'expiration (sinon maintien).
5. **haze-piece** : 2ᵉ source → PHANTOMSHIP + OKUCHI.
6. **Hot games** : GPO (tailor vouchers), Da Hood (ESKETIT), Anime Vanguards (fin anniversaire ?), Fisch (FischFright 3 code propre ?), GAG (FREESEED 2ᵉ source).
7. **GTA 6** Newswire (préchargement/day-one) · **FC 26** (si naming tranché) · **Rotation** : inflated lists (décision Peter) + jeux jamais vérifiés.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
