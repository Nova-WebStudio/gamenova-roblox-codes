# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-21 (run 05h — mercredi)**

## ✅ FAIT — RUN 05h 2026-10-21

- **Codes — 3 éditions propres (multi-sources, non destructives) :**
  - **Anime Vanguards** → ajout **2ndAnniDay1** (100 rerolls de traits). **2 sources concordantes** : samlover 11/10 + Roonby 13/10. Page 13 → **14 codes**. `Prepare` maintenu **expiré** (2 sources antérieures > samlover seul). `1DayDelay`/`25thHour` = 1 source (samlover) → non ajoutés.
  - **Da Hood** → ajout **PRESIDENT** + **PVP** + **BUFF** (500 000 DHC chacun). **2 sources** : TechWiser 12/10 + NerdSchalk. Page 4 → **7 codes**. `ESKETIT` = 1 source (TechWiser) → non ajouté. MACRO!/ETERNAL/DOG/SHARK conservés.
  - **Rivals** → retrait **SORRY** (**expiré** : Insider Gaming le marque expiré + absent de Roonby 06/10). Page 9 → **8 codes**. Gros décalage de version (page FREE182 vs Roonby FREE201) **non comblé** faute de source propre marquant l'actif → à re-sourcer.
- **Hot games — re-vérifiés, défendables, 0 autre édition** : grand-piece-online (conflit tailor-vouchers 5FREETAILOR/ANOTHER persiste), steal-a-brainrot (BESTBRAINROTEVER, Dexerto 12/10 « no new »), blue-lock-rivals (page récente conservée), grow-a-garden (RDCAward/BEANORLEAVE10), fisch (FischFright 3 lancé 17/10 mais aucun code propre), haze-piece (PHANTOMSHIP/OKUCHI = Roonby seul, PocketTactics ne confirme pas → non ajoutés). Dates « 🔄 Vérifié le » rafraîchies.
- **KILL SWITCH — grimoires-era** : conflit **3 voies non tranché** → **AUCUNE édition**, date « Vérifié le » **NON** rafraîchie (page connue périmée mais set de remplacement non confirmable). PocketGamer 03/10 (REVAMPSOON!/25SPINS!/2025BOOSTS!/CLOVER) vs games.gg 03/10 (NEXTCHAPTER!/MINING!/UPDATE0.6!/SYSTEMREWORK!) vs page (11 codes tous expirés).
- **Rotation — character-rng CONFIRMÉ inchangé** (10/10 match thespike 06/09) → catalogVerify 21/10. 3 flags (voir « À REVÉRIFIER »).
- **GTA 6 / FC 26 / Aniimo** : aucun changement nécessaire (voir sections). 
- **Régénération** : build_site + build_home + build_codes_json (**1317 codes actifs / 191 jeux**) + build_sitemap (**396 URLs**). **QC OK** (node main.js, JSON ×6, sitemap XML, `</html>`, 0 null byte, divs équilibrés site, ACTIVE=compteur=visibles sur les 3 pages éditées).

---

## 🔥 URGENT

- **GTA 6** — ~1 mois avant lancement (**19/11/2026**). Launch Trailer sorti (15/10), **préchargement 12/11** confirmé (digital + physique). Surveiller à chaque run le **Rockstar Newswire** (patchs day-one, heure de préchargement). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Rien de neuf 20→21/10.

## 🟢 À PUBLIER

_(rien)_ — kill switch maintenu sur tous les conflits ; aucun nouveau jeu Roblox avec preuve d'intérêt multi-source **+ codes réels** cette nuit (steal-an-egg « viral » = déjà hot).

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **grimoires-era — PÉRIMÉE (conflit 3 voies).** Rebuild via **source officielle** (Trello/Discord) requis ; 2 sources web fraîches ne concordent pas. Ne rien éditer tant que non tranché.
- **rivals — gros décalage de version.** Page FREE182 vs Roonby 06/10 FREE201/COMMUNITY26. Besoin d'une source **marquant clairement l'actif** (Insider Gaming stale = FREE137). SORRY déjà retiré ce run.
- **knockout — probablement gonflée (7 codes).** dexerto 13/08 (stale) : seuls EMPERORRETURNS/THANKSFORPLAYING confirmés actifs ; PUNCHMONKEY expiré (1 source). Besoin 2ᵉ source fraîche pour élaguer CRABRAVE/SOCIALHUB/DOOMSDAY/ADMINABUSE/PUNCHMONKEY.
- **anime-battle-rng — gonflée (35 codes, verif 10/09).** nerdschalk 06/08 marque expirés : SMALLFIXESS/3MVISIT/SUMMER/DESTRUCTIONKING/GIVEMEROCK/NEWTRAITS/D3MONS (1 source stale). 2ᵉ source fraîche requise pour pruner.
- **haze-piece** — PHANTOMSHIP + OKUCHI (5 Race Spins) → Roonby 13/10 seul ; besoin 2ᵉ source.
- **noob-incremental — MUST_UPDATE (report).** Rewrite à exécuter une fois récompenses re-sourcées + resync `const ACTIVE`/compteur (non traité ce run).
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses.
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : republier un set fiable **seulement** là où ≥2 sources concordent (garden-tower-defense = conflit, voir ci-dessous).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Naming FC 27 vs FC 26** : titre EA live = **FC 26**. Bloque la couverture Ultimate Team / Halloween. **À trancher.**
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents du code** → étape du lundi non exécutable. À Peter : ajouter les marqueurs ou confirmer le mécanisme.
- **⚠️ Listes gonflées** : knockout (7), anime-battle-rng (~35), anime-astral-simulator (~100), dragon-blox (~82) : rebuild autour du set vérifié-actif, ou maintien ? **Rotation en retard** (anime-astral-simulator/anime-battle-rng/dragon-blox depuis 10/09).
- **CTA manquant** : `codes-da-hood.html` et `codes-rivals.html` n'ont **pas** de `data-cta="guidelink"` (pré-existant). À ajouter si des pages guide/tier dédiées existent pour ces jeux.
- **Note cache obsolète** : CLAUDE.md dit « main.js?v=19 » mais le site est à **v47** (171 HTML) + 3 stragglers **v43** (tous `/avatar/` = off-limits). À corriger dans CLAUDE.md.

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : grimoires-era (conflit 3 voies), rivals (version en retard), knockout (gonflée), anime-battle-rng (gonflée), haze-piece (PHANTOMSHIP/OKUCHI), grand-piece-online (5FREETAILORVOUCHERS_2/ANOTHER), da-hood (ESKETIT 1 source), garden-tower-defense (gtd vs set dexerto.fr — **conflit, rien publié**), grimoires-era, fish-an-anime-rng, aniimo (aniimazingfroyo).
- **Rotation en retard** : anime-astral-simulator, anime-battle-rng, dragon-blox (listes gonflées, >40 j) ; ~30 jeux jamais entrés dans catalogVerify (beaucoup = stubs sans codes).

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 22/10)

1. **grimoires-era** : source officielle (Trello/Discord) → rebuild propre.
2. **knockout + anime-battle-rng** : 2ᵉ source fraîche → élaguer les codes expirés (1 source stale actuellement).
3. **rivals** : source fraîche marquant l'actif → combler le décalage FREE182→FREE201.
4. **haze-piece** : 2ᵉ source → PHANTOMSHIP + OKUCHI.
5. **Hot games** : re-vérifier GPO (tailor vouchers), Da Hood (ESKETIT), BLR, Anime Vanguards, SAB, GAG, fisch (codes FischFright 3 ?).
6. **GTA 6** Newswire (préchargement/day-one) · **FC 26** (si naming tranché) · **Aniimo** (aniimazingfroyo 2ᵉ source).
7. **Rotation suite** : inflated lists (décision Peter) + jeux jamais vérifiés.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
