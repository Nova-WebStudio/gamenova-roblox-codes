# Rapport Zoneblox — 4 juillet 2026 (samedi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = samedi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

---

## 1. Codes vérifiés ce run (jeux « hot »)

Vérification web (WebSearch + fetch des pages sources) et croisement avec `code-watch.json`. Règle appliquée : code maintenu ACTIF seulement si confirmé par ≥3 sources fiables OU source officielle ; conflit → version la plus prudente.

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Anime Vanguards** | **CHANGEMENT** — `LagGone` expiré | Pocket Tactics (01/07, liste active de 7 codes sans LagGone), agrégat Beebom/PGG/GamesRadar (LagGone expiré ~03/07) | Page passée de **8 → 7 codes actifs**. Restent : 13.5, EternalAdversaries, Gambler, DMCAFree, Liberation, 223, Cog5th. « Mis à jour le » → 4 juillet ; compteur, bannière et paragraphe actualisés ; LagGone déplacé en expirés. |
| **Fisch** | **CHANGEMENT** — `Fischfest2026` + `AquariumCustomization` expirés | Pocket Tactics (01/07 : les deux en « Expired »), PCGamer, GamesRadar ; RoCodes encore actifs (conflit) | Conflit tranché par **prudence** : les 2 codes déplacés en expirés. Page passée de **6 → 4 codes actifs** (KingCrabstle, scarlet, TemporarySubmarine, CARBON). Dates/compteur/bannière/paragraphe MAJ ; libellé expirés 20 → 22. |
| **Anime Last Stand** | **Inchangé** (concern de trim levé) | Destructoid (01/07), Beebom, Twinfinite, bloxodes (« 22 active »), Fossbytes, GAMES.GG | La page (21 actifs) est en fait **corroborée par ≥3 sources**. Le doute du 2/07 (RoCodes = 5 seulement) était un outlier. Aucun trim. Date « Vérifié le » rafraîchie. |
| **Grow a Garden** | **Inchangé** | Beebom (actifs = RDCAward, BEANORLEAVE10 ; `torigate` en **expirés**) | Le résumé WebSearch listait `torigate` comme actif, mais Beebom (source concrète) confirme qu'il est **expiré** — la page Zoneblox est déjà correcte (2 actifs). Aucun changement. |
| **Blox Fruits** | **Inchangé** | RoCodes (« 23 Active Codes »), PCGamer, Pocket Tactics, Dexerto | Les 23 codes de la page correspondent exactement à la liste active. Aucun changement. |
| **Steal a Brainrot** | **Inchangé** | Beebom, PCGamesN, Pocket Tactics | Toujours **aucun code** publié par les devs. Une source isolée évoque « 12 codes » mais confond avec « Split or Steal Brainrot » (autre jeu). Prudence : rien publié. |

**Codes ajoutés :** 0.
**Codes expirés retirés (déplacés en « expirés ») :** 3 — Anime Vanguards : `LagGone` ; Fisch : `Fischfest2026`, `AquariumCustomization`.
**Candidats en attente enregistrés :** Fisch (`Fischfest2026`/`AquariumCustomization` : RoCodes vs Pocket Tactics/PCGamer — retirés par prudence, à re-surveiller).

## 2. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **4 juillet 2026** sur **les 164 pages** `codes/<slug>.html` (idempotent, exactement 1 par page). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf Anime Vanguards et Fisch (changements réels de codes).

## 3. Jeux « hot » NON revus individuellement ce run (à prioriser)

Budget d'appels réseau : 6 jeux « hot » vérifiés en profondeur ce run. À prioriser aux prochains runs : pet-simulator-99, king-legacy, fruit-battlegrounds, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea. Blade Ball / Blue Lock Rivals / Volleyball Legends : vérifiés le 2/07, non ré-audités aujourd'hui. Reste du catalogue (~140 pages) : rotation habituelle + rafraîchissement de date reçu.

## 4. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité à la vérification des codes).
- **Guides / tier lists :** aucun créé/modifié ce run.
- **UGC :** non revu ce run.
- **Jeu de la semaine :** non touché (samedi).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`, 307 références).

## 5. QC (résultat)

- ✅ Pages modifiées (`anime-vanguards.html`, `fisch.html`) : se terminent par `</html>`, 0 null byte, `<div>` équilibrés (0), GA4 `G-FEL71QVHNL` présent, bandeau `data-cta="guidelink"` présent (1 seul), ≥1200 mots (AV ~1350, Fisch ~1320).
- ✅ Toutes les 164 pages codes : « 🔄 Vérifié le 4 juillet 2026 » présent, 0 null byte.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (307 refs).
- ✅ `tools/code-watch.json` : JSON valide, se termine par `}`, 0 null byte ; snapshots des 6 jeux vérifiés mis à `2026-07-04`.

**Fichiers touchés :** 164 pages `codes/*.html` (rafraîchissement date) dont `codes/anime-vanguards.html` et `codes/fisch.html` (changements de codes réels) + `tools/code-watch.json` + ce rapport.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
