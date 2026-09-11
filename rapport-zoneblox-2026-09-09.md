# Rapport Zoneblox — 9 septembre 2026 (run automatique)

## (a) Codes vérifiés — PRIORITÉ

### hotGames (6 vérifiés, 2 modifiés)
| Jeu | Résultat | Source datée |
|-----|----------|--------------|
| **blockspin** ✏️ | 2 → **4** actifs : ajout de `BLOCKSPIN_GRIPS_UPDATE` + `UNDER_THE_BARREL` (nos 2 existants confirmés actifs) | Pocket Gamer 5 sept. |
| **catch-a-monster** ✏️ | 11 → **9** actifs : 6 de nos codes marqués expirés (massglaw, crysting, graon, magmorus, moovik, danvok) + 5 hors actifs → tous en expirés ; nouvelle liste (mutatebug, achievebug, turret, Oblivion, Plagcannon, Gearif, coin, xp, cam) | Pocket Tactics 2 sept. |
| squid-game-x | OK — nos 6 codes tous confirmés actifs (sous-listage acceptable) | Roblox Den 8 sept. |
| 100-days-at-sea | OK — 3 exacts (CLASSES, DECORATE, 20Pearls) | GamesRadar/Dexerto 7 sept. |
| steal-an-egg | OK — 0 code (le jeu n'en a jamais eu) | PCGamesN sept. |
| pet-simulator-99 | OK — 0 code public (merch codes only) | Beebom/GameRant sept. |

### Rotation ÉTAPE 2ter (8 vérifiés en profondeur, 6 modifiés)
| Slug | Résultat | Source datée |
|------|----------|--------------|
| **sailor-piece** ✏️ | **16 → 2** — nos 16 « actifs » TOUS périmés ; seuls TojiDanteUpdate + Weloveyou actifs. Correction majeure de faux-actifs. | Pocket Tactics 7 sept. |
| **grand-piece-online** ✏️ | **3 → 2** — nos 3 codes tous listés expirés ; remplacés par FREE_Drops6, ILOVEGPO_2 | Pocket Tactics 2 sept. |
| **peroxide** ✏️ | **4 → 7** — YayAHalloweenUpdate expiré, 4 codes courants ajoutés | Pocket Gamer 5 sept. |
| **jujutsu-shenanigans** ✏️ | **5 → 1** — 4 codes basculés en expirés (dont SLATECONCRETE en conflit, retiré par prudence) | Beebom 1 sept. + PC Gamer |
| **haze-piece** ✏️ | **3 → 4** — ajout du nouveau ABYSSALCTHULHU | Pocket Tactics 5 sept. |
| **project-mugetsu** ✏️ | **4 → 7** — ajout TheD1Gambler26, SUPPORTANIMEOVERSEAS, ProjectSoon | Pro Game Guides 1 sept. |
| untitled-boxing-game | OK — nos 9 codes tous confirmés actifs | Pocket Gamer 5 sept. |
| slap-battles | OK — Happy5lappiversary + spookyseason25 confirmés (+1x1x1x1x1x1 permanent) | Dexerto/Beebom sept. |

**⚠️ Laissés « à revérifier » (prudence) :** `sonic-speed-simulator` (conflit 0 vs 5 actifs + version RE-RAN), `fire-force-online` (MAJ du 2 sept. a retiré beaucoup de codes ; statut de nos 3 non confirmé). Aucune modification à l'aveugle.

**Candidats en attente (`_pending2026-09-09`) :** SLATECONCRETE (conflit JJS), nexa (catch-a-monster, source unique), UPDATE11RELEASE (squid-game-x, source crowd unique).

**Sourcing :** toutes les corrections s'appuient sur une source tier-1 datée du mois courant avec **liste expirée explicite** (Pocket Tactics / Pocket Gamer / Pro Game Guides / Beebom). Aucun code inventé. Conflits → version la plus prudente.

## (b) Directeur SEO (ÉTAPE 2bis)
- **Trending re-scanné** : leaders (Steal An Egg, Blox Fruits, Steal a Brainrot, Grow a Garden, Brookhaven, Murder Mystery 2, Adopt Me) tous couverts. Aucun nouveau hit ≥4000 non couvert → evergreen.
- **Brique du jour (EEAT/honnêteté)** : conformément au précédent J26/J27, le run étant dominé par des corrections de faux-actifs prioritaires (2 majeures : Sailor Piece 16→2, Catch a Monster 11→9), l'assainissement des signaux de confiance **est** la brique d'autorité. **Aucune nouvelle URL** : la tier list « meilleurs pets Steal an Egg » n'a pas été publiée car les valeurs de revenus **divergent entre sources** (Unicorn $1B/s vs Oni Tiger $600M/s) — honnêteté > remplissage.
- **Roadmap mise à jour** : entrée J28 ajoutée, prochaine brique J29 inscrite (réconcilier les sources pour la tier list Steal an Egg ; puis grimoires-era, anime-story-2).

## (c) Jeux ajoutés / guides / tier lists / UGC / jeu de la semaine
- Aucun nouveau jeu ajouté ce run (temps consommé par les corrections de codes prioritaires).
- Jeu de la semaine : non concerné (mercredi ; MAJ uniquement le lundi).

## (d) Fichiers touchés + QC
**Pages codes modifiées (8, codes changés) :** codes-blockspin, codes-catch-a-monster, codes-sailor-piece, codes-grand-piece-online, codes-peroxide, codes-jujutsu-shenanigans, codes-haze-piece, codes-project-mugetsu.
**Pages codes confirmées OK (verifDate rafraîchie) :** codes-squid-game-x, codes-100-days-at-sea, codes-steal-an-egg, codes-pet-simulator-99, codes-untitled-boxing-game, codes-slap-battles.
**Autres :** `data/codes.json` régénéré (178 jeux, 1202 codes actifs), `tools/code-watch.json` (catalogVerify +8, lastRun, _pending), `SEO-directeur-audit-roadmap-2026-07-24.md` (entrée J28).

**QC :** toutes les pages modifiées → fin `</html>`, 0 null byte, `<div>` équilibrés (0), GA4 présent, cache `main.js?v=41` uniforme (note : CLAUDE.md indique encore v=19, valeur périmée — le site est en v=41). `node --check js/main.js` OK. `data/codes.json` et `tools/code-watch.json` valides. Cohérence compteur hero = liste active = tableau ACTIF vérifiée sur les 8 pages éditées ; libellés « codes expirés (N) » alignés sur les listes peuplées.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
