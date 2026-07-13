# Rapport Zoneblox — 12 juillet 2026 (dimanche)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = dimanche → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

Règle de sourcing appliquée : un code n'est ACTIF que s'il est confirmé par **≥3 sources fiables OU une source officielle** (Trello / Twitter-X / description in-game / shout du groupe). Conflit entre sources → version la **plus prudente** + candidat « en attente » dans `code-watch.json`.

---

## 1. Changements de codes réels ce run (2 pages)

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Tower Defense Simulator** | **CHANGEMENT — 0 → 2 codes actifs** | Pro Game Guides, Pocket Tactics (10/07), PCGamesN (06/07) — 3 sources concordantes | La page affichait « Aucun code actif » depuis le 9 juin. Ajout de **`1MILCOMMUNITY`** (skin gratuit, palier 1 M de membres) et **`2MILLION`** (crate / skin Mercenary). Tableau de codes recréé, bandeau live, compteur `Aucun code actif` → **2 codes actifs**, statut « fonctionnent en juillet 2026 », FAQ réécrite, `Mis à jour le` **9 juin → 12 juillet 2026**. `CHRISTMAS2025` et `NOTESLA?` sont donnés **actifs par PGG mais expirés par Pocket Tactics** → conflit → **non publiés** (prudence), enregistrés en attente. Page = **1676 mots**. |
| **Noob Incremental** | **CHANGEMENT — 14 → 11 codes actifs** | Pocket Tactics (29/06), PCGamesN (11/07), Beebom (02/07), Try Hard Guides (23/06) | **Ajouts** (≥3 sources) : `REFUNDPRISM`, `10MVISITS!`, `HOPERUNESFIXEDONG!`, `SORRYWEIRDANDANNOYINGBUGS!!`. **Retraits — expirés** selon 3 sources : `12KCCU!!`, `11KCCU!!`, `10KCCU!!`, `9KCCU!!`. **Retraits — plus confirmés par aucune source fiable** : `YouFoundMe`, `GetBetterSon`, `BAZALRIGHT`. Compteurs (game-meta, bannière live, FAQ) et `Mis à jour le` **21 juin → 12 juillet 2026**. Page = **1540 mots**. |

**Codes ajoutés (actifs) :** TDS +2, Noob Incremental +4.
**Codes retirés :** Noob Incremental −7.

### Candidats « en attente » (non publiés, prudence)

- **Noob Incremental** : `SORRYSHUTDOWN67`, `SORRYSHUTDOWN68`, `SORRYSHUTDOWN69`, `FOOTBALLEVENT` — seulement **2 sources** (PCGamesN + Beebom), pas de confirmation officielle. Le titre in-game est bien `[⚽ÉVÉNEMENT]` (événement football en cours), ce qui est un indice mais **pas** une source de code.
- **Tower Defense Simulator** : `CHRISTMAS2025`, `NOTESLA?` (conflit direct entre sources).
- **100 Days at Sea** : `HERO`, `ALIENS`, `CODE`, `20Pearls` (voir §3).
- **World Fighters** : `UPDATE10`, `15MVISITS!`, `UPDATE9PT2`, `TEMPESTINVASIONHARD`, `HYPEEEE`, `UPDATE8PT2`, `ThanksForAllTheSupport`.
- **Steal a Brainrot** : `BESTBRAINROTEVER`, `FREEOCTOBLOCK777` (conflit persistant, page maintenue sans code).

## 2. Étape 0 — Sources officielles (API Roblox, via Chrome)

Descriptions in-game et shouts de groupe récupérés pour les 16 jeux « hot » prioritaires.

- **BlockSpin** : la **description in-game officielle** contient explicitement « Utilisez le code **W7C28D** pour 500 $ d'argent gratuit si vous êtes un nouveau joueur ». → code confirmé **par source officielle**, déjà présent sur la page. `officialSource: "ingame"` renseigné dans `code-watch.json`. Aucun changement de liste.
- **World Fighters** : description = « 25kLIKE = NOUVEAU CODE !!! » (annonce, pas de code).
- **Blox Fruits / Grow a Garden / Steal a Brainrot / Blade Ball / King Legacy / TDS / 100 Days at Sea / Animal Hospital / Catch a Monster / Run a Restaurant / Brainrot Evolution / VV Ultimatum / Defend ur Base** : aucun code dans la description in-game.
- **Shout du groupe Stranded Devs** (100 Days at Sea, groupe 425035678) : `shout: null` → aucune source officielle exploitable.

## 3. Jeux vérifiés sans changement (prudence)

| Jeu | Sources | Décision |
|-----|---------|----------|
| **100 Days at Sea** | PCGamesN (09/07), Pro Game Guides (27/06), Sportskeeda/GamesRadar (11/07) | **Conflit fort** : PCGamesN dit `ALIENS` actif **mais expirant le 10 juillet** (donc périmé aujourd'hui) et `20Pearls` expiré ; PGG ne connaît que `CODE` ; Sportskeeda annonce `HERO`+`ALIENS`+`20Pearls`. Shout du groupe = vide. → **page maintenue sans code**. À reprioriser au prochain run. |
| **King Legacy** | Pocket Tactics, PC Gamer, Beebom (03/07) | « Aucun nouveau code depuis mi-mars » → les 13 codes de la page sont maintenus tels quels. |
| **Run a Restaurant** | Pocket Tactics, PCGamesN, Roblox Den, Dexerto (10/07) | `RAR4EVER` reste le **seul** code actif — identique à notre page. Aucun changement. |
| **BlockSpin** | Description in-game (officielle), Pocket Gamer, Roblox Den, Pocket Tactics | Les 4 codes de la page sont corroborés. Aucun changement. |
| **World Fighters** | Beebom, PGG, Pocket Tactics (figé au 15/05) | Sources **fortement désynchronisées** et contradictoires ; le jeu est retombé à ~91 joueurs connectés. Liste maintenue telle quelle, candidats en attente. |
| **Blox Fruits, Grow a Garden, Steal a Brainrot, Blade Ball, Brainrot Evolution, Catch a Monster, VV Ultimatum, Defend ur Base with Anime, Animal Hospital** | Sources juillet 2026 + description in-game | Aucun changement de liste. |

## 4. Rafraîchissement « Vérifié le »

Ligne « 🔄 Vérifié le » passée au **12 juillet 2026** sur **les 166 pages** `codes/<slug>.html` (idempotent : 166 mises à jour, 0 insertion nécessaire, **0 doublon**, 0 page restée au 11 juillet). Dates « Mis à jour le » **non touchées**, sauf Tower Defense Simulator et Noob Incremental (changements de codes réels).

## 5. Jeux « hot » non revus en profondeur ce run (à prioriser au prochain)

`spin-a-soccer-card`, `merge-a-nuke`, `squid-game-x`, `fifa-super-soccer`, `hypershot`, `fisch`, `volleyball-legends`, `anime-vanguards`, `anime-last-stand`, `blue-lock-rivals`, `fruit-battlegrounds`, `pet-simulator-99` (tous vérifiés entre le 05 et le 10/07, inchangés à l'époque). **`100-days-at-sea` et `world-fighters`** restent les deux dossiers ouverts (conflits de sources). Reste du catalogue (~150 pages) : rafraîchissement de date reçu.

## 6. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité donnée à la vérification des codes et aux 2 mises à jour de listes).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **Jeu de la semaine :** non touché (dimanche).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`).
- **Contenu minimum :** les 2 pages éditées dépassent le seuil (1676 et 1540 mots).

## 7. QC (résultat)

- ✅ **312 pages HTML** scannées : toutes finissent par `</html>`, **0 null byte**, balises `<div>` **équilibrées partout**.
- ✅ `sitemap.xml` valide (finit par `</sitemapindex>`), `node --check js/main.js` OK, `tools/code-watch.json` = JSON valide, 0 null byte, finit par `}`.
- ✅ GA4 `G-FEL71QVHNL` présent sur toutes les pages (seule exception attendue : `codes/mini-war.html`, stub de redirection).
- ✅ Version cache JS uniforme : `main.js?v=32` (0 page hors v=32).
- ✅ Les 166 pages codes : « 🔄 Vérifié le 12 juillet 2026 » (1 par page, 0 doublon).
- ✅ Pages éditées (TDS, Noob Incremental) : nav 7 entrées (Avatars OK), `data-cta="guidelink"` présent **1 seule fois**, ≥1200 mots, compteurs cohérents avec le tableau de codes.
- ✅ Aucun rédactionnel anglais introduit ; aucun code inventé.

**Fichiers touchés :** 166 pages `codes/*.html` (rafraîchissement « Vérifié le ») dont `codes/tower-defense-simulator.html` et `codes/noob-incremental.html` (changements de codes réels) + `tools/code-watch.json` + ce rapport. (**167 fichiers suivis modifiés.**)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
