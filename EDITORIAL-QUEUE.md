# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-28 (run 05h — mercredi — Volleyball Legends Update 93 publié + 5 hotGames revérifiés)**

## ✅ FAIT — RUN 05h 2026-10-28 (mercredi)

- **Volleyball Legends — mise à jour de codes (Update 93 « Cursed Tournaments »)** : page passée de `UPDATE_91 / REPLAYS / MVP` à **`UPDATE_93` (5 Lucky Style Spins), `CURSED` (5 Lucky Style Spins), `TOURNAMENT` (5 Lucky Ability Spins)** — 3 codes actifs (niveau 15 requis). Anciens codes + `UPDATE_92 / MAMORI / PARRY` passés en expirés. **2 sources fraîches concordantes** : TimeSaver.gg + Roonby (24/10). Dates « Mis à jour le » (prose) + `verifDate` + JSON-LD (`dateModified` 28/10 + ItemList) synchronisées. `build_codes_json` relancé.
- **5 hotGames revérifiés, inchangés** (→ `verifDate` 28/10, `catalogVerify` 28/10) :
  - **king-legacy** : **match parfait** (9 codes) avec Pocket Tactics (23/10).
  - **grow-a-garden** : match exact (RDCAward, BEANORLEAVE10) avec gfinityesports (vérifié 21/10).
  - **steal-a-brainrot** : match (BESTBRAINROTEVER) avec Dexerto (12/10).
  - **fisch** : 3/4 confirmés (scarlet, TemporarySubmarine, CARBON) via Pocket Tactics (07/10) ; `MarianaIsGoingCrazy` gardé (pas de preuve d'expiration).
  - **blox-fruits** : jeu statique, aucun nouveau code depuis Pâques (Pocket Tactics 23/10) → inchangé.
- **Blue Lock Rivals — KILL SWITCH (nouveau conflit 3 voies)** : Dexerto (25/10) = SKELETON/AIKUCHANGES/NEW ; Insider (codes hiver BAROUSNOWLOCK/SNOWLOCK2 recyclés) ; notre page = NELAIKU/HALLOWEEN/WSNAKE/SORRYFORDELAYAIKU. **Aucune paire concordante → page non modifiée.** Besoin d'une **source officielle** (Discord/Trello/X). ⚠️ nos codes Halloween sont probablement expirés (fin event 31/10).
- **Fisch FischFright 2026** : **aucun nouveau code** (tous les FischFright en section expirée — Pocket Tactics). Pas de section event à écrire (kill switch respecté).
- **Régénération** : `build_site` + `build_home` + `build_codes_json` (1335 codes, 198 jeux) + `build_sitemap` (418 URLs). **QC complet OK** (0 null byte, div équilibrés site entier, `node --check main.js` OK, JSON/XML valides, sitemap fermé, GA4/nav/CTA OK, cache `main.js?v=48` cohérent).

---

## 🎃 COUVERTURE HALLOWEEN 2026 (programme — règle « guides d'événements », CLAUDE.md)

> **Règle permanente** : chaque event/MAJ d'un hotGame doit être couvert par un guide/section de guide (UPDATE before CREATE), **détails confirmés uniquement**. **L'événement Halloween se termine le 31/10** → après cette date, retirer/archiver les sections event.
> **État au 28/10** : **Fisch FischFright 2026 = aucun code confirmé** (tous expirés) → rien à écrire. Les autres events saisonniers se terminent cette semaine ; aucun nouveau détail 2026 confirmé sur source fraîche → kill switch maintenu.

| Jeu (suivi) | Event Halloween | Guide cible | Statut |
|---|---|---|---|
| **Fisch** | FischFright | `guides/fisch.html` | ✅ Vérifié 28/10 : aucun code 2026 (tous expirés) → rien à écrire |
| **Grow a Garden** | « Ghoul Garden » | `guides/grow-a-garden.html` | ⏳ Non confirmé 2026 (sources = 2025) |
| **Steal a Brainrot** | Halloween brainrots | `guides/steal-a-brainrot.html` | ⏳ Non confirmé 2026 |
| **100-days-at-sea** | Code `SPOOKY` | page codes (fait 26/10) | ✅ Code publié |
| Autres hotGames | scan continu | — | 🔎 Fin event 31/10 |

## 🔥 URGENT

- **Aniimo « Season 1 Part II » (29/10 — DEMAIN)** — update **confirmé** (preview officielle devs via playnews 20/10) : région **Whisperwake Isles**, **51 nouveaux Aniimo** (32 espèces), nouveaux Prismana, **PvP 1v1 permanent**, Vein Abundance 30/10→06/12. **Fin Part I : 28/10 23h59 UTC (ce soir).** Aucun nouveau code annoncé. → **Préparer l'ingestion data-driven (`data/aniimo/` → `build_site.py`) dès l'officiel du 29/10. NE RIEN inventer / ne rien publier avant l'officiel.**
- **GTA 6** — ~3 semaines avant lancement (**19/11/2026**). Préchargement **12/11** confirmé. **Rien de neuf confirmé au 28/10.** ⚠️ « News update » toujours rapporté pour le **29/10** (non primaire) → **surveiller le Rockstar Newswire chaque run**. **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR.
- **Blue Lock Rivals — conflit 3 voies non résolu** (voir FAIT). Page probablement périmée (codes Halloween). **Trancher via source officielle**, pas via agrégateurs.

## 🟢 À PUBLIER

_(rien de neuf)_ — aucun nouveau jeu avec preuve d'intérêt multi-source **+ codes réels** détecté cette nuit.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **FC 27 Ultimate Scream — Team 2** « attendue » **~30/10 18:00 UTC** (NON confirmée EA, fut.gg) → ajouter dès sortie réelle + **une solution DCE Woltemade vérifiée** (ne pas inventer). Token store jusqu'au 13/11, upgrade Beaver Moon 24/11→01/12 (confirmés). Rafraîchir en fin de promo (06/11).
- **fruit-battlegrounds — à revérifier (conflit).** Dexerto (copie 25/08 périmée) vs notre page ; source unique + stale → **kill switch**, page inchangée (verif 01/10). Besoin d'une **source fraîche**.
- **grimoires-era — PÉRIMÉE (conflit 3 voies).** Rebuild via **source officielle** (Trello/Discord) requis.
- **rivals — décalage de version.** Page FREE182 ; sources divergentes. Besoin d'une **source fraîche**.
- **type-soul — page vide** (~55 codes sans récompenses) → 2-3 sources propres avec récompenses.
- **noob-incremental, attack-on-titan-revolution, anime-battle-rng, anime-astral-simulator (~100), dragon-blox (~82)** : listes gonflées → **preuve d'expiration** requise avant prune (§4).
- **CTA manquant** : codes-da-hood, codes-rivals, codes-knockout (pas de guide/tier dédié).

## 🟡 À PRÉPARER / DÉCISION PETER

- **⚠️ Jeu de la semaine (§30) — BLOQUÉ.** Marqueurs `<!-- FEATURED-WEEK-START/END -->` toujours **absents** d'`index.html` et `meilleurs-jeux-roblox.html`. Étape du lundi **non exécutable** sans créer la structure. **→ Peter : indiquer où placer le bloc** (ou valider sa création).
- **FC 27 — Prix des cartes live = NON fait** (nécessite un feed type Futbin/Futwiz — à cadrer).
- **/avatar/** : 3 pages encore en `main.js?v=43` (reste du site en v=48). Dossier **NE PAS MODIFIER** → laissé tel quel ; à signaler si Peter veut aligner le cache.

## 👀 À REVÉRIFIER (conflits / identité non tranchés)

- **Blue Lock Rivals** (conflit 3 voies — voir URGENT), **fruit-battlegrounds** (source unique stale), **spin-a-soccer-card** (conflit total, page à 0), **100-days-at-sea** (`RIVAL` conflit), **grimoires-era** (3 voies), **rivals** (version), **haze-piece** (PHANTOMSHIP/OKUCHI 2/3).
- **Identité ambiguë (désambiguïser via placeId)** : button-rng-2, chicken-farm ; clones anime : anime-rng, anime-fighters, anime-fighting-simulator(-reborn), anime-reversal, scroll-a-brainrot, heroes-battlegrounds.
- **Rotation en retard** : **~150 pages > 3 j (dont ~30 jamais vérifiées)** — backlog chronique. Rotation approfondie **non traitée ce run** (priorité donnée aux hotGames + Volleyball ; sources agrégées conflictuelles/recyclées sur le reste). À reprendre avec sources fraîches/officielles.

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h 28/10 ; 05h 29/10)

1. **Aniimo** : update **officiel 29/10** (Part I finit ce soir 23h59 UTC) → ingérer la data (`data/aniimo/`) dès l'officiel, puis `build_site.py`. Ne rien publier avant.
2. **FC 27 Ultimate Scream Team 2** (~30/10) + solution DCE Woltemade vérifiée dès sortie.
3. **GTA 6** : surveiller Newswire (« news update » rapporté 29/10 ; heure préchargement / taille fichier / patch day-one).
4. **Blue Lock Rivals** : trancher via source officielle (codes Halloween à expirer au 31/10).
5. **Volleyball Legends** : revérifier au prochain Update (codes éphémères par patch).
6. **Rotation backlog** : attaquer les ~30 « jamais vérifiées » désambiguïsables (placeId) + fruit-battlegrounds (2ᵉ source fraîche).
7. **Décisions Peter** : bloc « Jeu de la semaine » ; feed prix cartes FC 27.

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
