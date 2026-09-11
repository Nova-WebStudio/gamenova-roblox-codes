# Rapport Zoneblox — 8 septembre 2026 (run quotidien 05h00)

## a) Codes vérifiés (PRIORITÉ)

**3 corrections majeures de faux-actifs / codes fabriqués appliquées ce jour.**

### hotGames (13 vérifiés, 1 modifié)
| Jeu | Résultat | Source(s) datée(s) |
|-----|----------|---------------------|
| grow-a-garden | OK, 2 actifs (RDCAward, BEANORLEAVE10) — **TEAMGREENBEAN écarté = code de Grow a Garden 2** (piège de désambiguïsation) | PCGamer/Beebom, GaG2 fandom |
| steal-a-brainrot | OK, 1 actif (BESTBRAINROTEVER) | GamesRadar/Dexerto |
| blade-ball | OK, 13 actifs confirmés ; **BATTLEROYALE contesté → non ajouté** | Pocket Tactics 1er sept. |
| anime-last-stand | OK, 22 actifs confirmés (PGG « 3 actifs » = outlier isolé) | Roblox Den 7 sept. + Beebom + Destructoid |
| blue-lock-rivals | OK, 4 actifs (NELKING, NIKOSOON, UBERSMONTH, SORRYLOADING) | PCGamer |
| anime-vanguards | OK, 3 actifs (Retribution, Wrath, MiniUpd2) | GamesRadar/PGG |
| **volleyball-legends** | **MODIFIÉ 3→3 (renouvelés)** : UPDATE_85/SHIRO/BLOCKED **expirés** → **UPDATE_86, HAKKA_RETURN, SPIKER** | **PGG 5 sept.** + agrégats |
| fisch | OK, 3 actifs (scarlet, TemporarySubmarine, CARBON) — **SkycrestIsInTheSky confirmé EXPIRÉ** | GamesRadar 7 sept. |
| fruit-battlegrounds | OK, 2 actifs — la « longue liste active » des résumés de recherche était en réalité expirée ; **EVENHIGHER! source unique → non ajouté** | Pocket Tactics 4 sept. |
| blox-fruits | OK, 24 (codes longue durée) | PCGamesN/Beebom |
| king-legacy | OK, 7 (codes stables) | PCGamer/PGG |
| tower-defense-simulator | OK, 2 (sous-listage acceptable) | TheSpike/PGG |
| brainrot-evolution | OK, 24 — **tous confirmés actifs** | Nerdschalk 5 sept. |

### Lot de rotation (ÉTAPE 2ter) — 15 slugs traités (jamais vérifiés)
**Corrections (faux-actifs / fabriqués) :**
- **garden-tower-defense** : nos **19 codes tous périmés** (PGG 5 sept. les liste tous « Inactive » ; recherche 7 sept. : seuls FANTASY + FRONTIER actifs). TD à rotation ~3 jours → **19 → 2** (FANTASY, FRONTIER), 19 déplacés en expirés.
- **pet-simulator-x** : les **8 « codes actifs » étaient FABRIQUÉS** (FURRYFRIEND, SINGLESTRIKE, PET_SQUAD, BIGUPDATE, CRYSTALBOOST, DIAMONDS2026, PSWELCOME, HATCHMASTER — absents des listes actif **et** expiré de Pocket Gamer). Le jeu (GLITCH) n'a plus aucun code valide → page passée honnêtement à **0 code actif** + chargement de la **vraie liste expirée (44 codes)**. *(Correction d'honnêteté — brique EEAT du jour, cf. section b.)*

**Confirmés OK (sous-listage acceptable, aucune preuve d'expiration) :** plants-vs-brainrots (5, Beebom 1er sept.), grow-a-chicken-fighter (4), attack-on-titan-revolution (21), rivals (8/9), muscle-legends (14), skibidi-masters-tower-defense (5 — PGG garde tous les paliers KLIKES), grow-a-garden-2 (3 exacts : WATERYOPLANTS, TEAMGREENBEAN, REMEMBERTODRINKWATER), knockout, character-rng, jules-rng, broken-blade, murder-mystery-2 (0, aucun code depuis des années — page correcte), ninja-legends.

**⚠️ À revérifier au prochain run (prudence — pas touché) :**
- **grimoires-era** : collision de nom Era / Era 2 / Legacy + pas de source datée septembre.
- **anime-story-2** : 17 codes de lancement ; la source liste 7 codes récents différents + « 111 working » non énumérés → frontière actif/expiré incertaine, ne pas élaguer à l'aveugle.
- **mad-city** : conflit Roblox Den (« 6 working ») vs Pocket Gamer (« none »).

**Candidats en attente (`code-watch.json` → `_pending2026-09-08`) :** BATTLEROYALE (blade-ball, 1 source), EVENHIGHER! (fruit-battlegrounds, source unique), SkycrestIsInTheSky (fisch — écarté, expiré).

**« 🔄 Vérifié le »** rafraîchi au **8 septembre 2026** sur **28 pages** réellement vérifiées ce jour. `data/codes.json` régénéré (178 jeux, 1214 codes). `catalogVerify` mis à jour (15 slugs rotation).

## b) Directeur SEO (ÉTAPE 2bis)

- **Trending re-scanné (≥2 sources, rblxdb/rotrends 6 sept.)** : Steal An Egg (~2,45M) #1, Blox Fruits (~717K), Brookhaven, +1 Speed Keyboard Escape (`evasion-clavier`), Murder Mystery 2, Grow a Garden, Steal a Brainrot — **tous couverts**. Aucun nouveau hit ≥4000 non couvert → evergreen.
- **Brique réalisée (EEAT / honnêteté)** : correction **Pet Simulator X** — retrait de 8 codes fabriqués + rétablissement d'une liste expirée authentique sourcée (Pocket Gamer). Des codes inventés nuisent directement à l'EEAT et au classement ; assainir ce signal est prioritaire sur toute nouvelle URL. **Anti-cannibalisation / anti-orphelin** : aucune nouvelle URL, aucune modification de maillage. Le run a été majoritairement consommé par 3 corrections de faux-actifs (priorité absolue).
- **Roadmap mise à jour** (`SEO-directeur-audit-roadmap-2026-07-24.md`) : brique J27 consignée, prochaine brique J28 = grimoires-era (désambiguïsation + élagage) → anime-story-2 (liste expirée propre) → enrichissement tier list Steal an Egg → mad-city.

## c) Jeux ajoutés / guides / tier lists / UGC / Jeu de la semaine
- Aucun nouveau jeu ajouté ce jour (aucun hit trending non couvert ; run consacré aux corrections de codes prioritaires).
- **Jeu de la semaine** : non modifié — on est mardi (`date +%u` = 2), l'ÉTAPE 7 ne s'applique que le lundi.

## d) Fichiers touchés + QC
**Pages codes modifiées structurellement (3)** : `codes-volleyball-legends.html` (3 codes renouvelés), `codes-garden-tower-defense.html` (19→2), `codes-pet-simulator-x.html` (8 fabriqués → 0 + 44 expirés).
**Autres** : 28 pages `codes-*.html` avec « Vérifié le » au 8 sept. ; `data/codes.json` (régénéré) ; `tools/code-watch.json` (catalogVerify + snapshots + pending + lastRun) ; `SEO-directeur-audit-roadmap-2026-07-24.md`.

**QC (ÉTAPE 8) — tout vert :**
- 0 null byte sur l'ensemble des `.html` ✅
- Tous les fichiers finissent par `</html>` ✅
- Balises `<div>` équilibrées partout (0 déséquilibre) ✅
- `data/codes.json` + `tools/code-watch.json` : JSON valides ✅
- `node --check js/main.js` : OK ✅ (js non modifié → pas de bump de cache nécessaire)
- Compteurs hero cohérents : volleyball 3, garden-tower-defense 2, pet-simulator-x 0 ✅
- GA4 (G-FEL71QVHNL) présent sur les 3 pages modifiées ✅

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.

> ℹ️ Note : des modifications non commitées du run précédent (7 sept.) étaient encore présentes dans l'arbre de travail (dernier commit daté du 5 sept.). Le commit ci-dessus inclura donc aussi ces changements du 7 sept. en attente.
