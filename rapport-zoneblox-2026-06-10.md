# Rapport de maintenance Zoneblox — 10 juin 2026

## Résumé

Maintenance quotidienne complète. 6 nouvelles pages codes créées, 4 pages existantes mises à jour, version JS bumpée sur 135 fichiers HTML.

---

## Étape 1 — 6 nouveaux jeux ajoutés

Fichiers créés + ROBLOX_THUMBS + ROBLOX_UNIVERSE_IDS + GAMES_INDEX dans `js/main.js` + ALL_GAMES dans `codes/index.html` :

| Jeu | Slug | Codes | Catégorie | Universe ID |
|-----|------|-------|-----------|-------------|
| Evade | evade | 0 | battle | 3647333358 |
| Dragon Adventures | dragon-adventures | 6 | rpg | 1235188606 |
| Car Dealership Tycoon | car-dealership-tycoon | 14 | tycoon | 605887098 |
| PLS DONATE | pls-donate | 7 | tycoon | 3317679266 |
| Wizard Alchemy | wizard-alchemy | 10 | rpg | 10006104044 |
| Restaurant Tycoon 3 | restaurant-tycoon-3 | 11 | tycoon | 7094518649 |

**Codes/pages créés :**
- `codes/evade.html` — 0 codes actifs (tous expirés juin 2026), notice + 6 astuces survie
- `codes/dragon-adventures.html` — 6 codes (JUSTYBLOX, AESUBREALM, FLUFFY, GALIFRAN, SHAMEWING, SeasonXP)
- `codes/car-dealership-tycoon.html` — 14 codes (ZOOMZOOM, QUARTERMILE, MAZDASPEED, MAZES, MUSCLE, OFFROAD, OLDSCHOOL, SAFARI, TRAILBLAZING, UTOPIA, FACTORY, GRIDIRON, INFILTRATE, RIPPINLIPS)
- `codes/pls-donate.html` — 7 codes (hazem, Quataun, HAUNTED, plsdonate2, PLSDONATENEWS15, Eagle_15, PIXEL)
- `codes/wizard-alchemy.html` — 10 codes (100KMEMBERS, 60KMEMBERS, UPDATE1, DRUID, QILIN, SUMMON, 80KMEMBERS, Broom, NewWorld, MERCHANT)
- `codes/restaurant-tycoon-3.html` — 11 codes (Pizza123, fishyfriday, auto123, Vitolinecode, FULMOON, Seniac, WeirdBlox, SANTY22, Photon, 01, UltrawEats)

---

## Étape 2 — Codes mis à jour

| Jeu | Avant | Après | Note |
|-----|-------|-------|------|
| Fisch | 10 (index/main.js désyncronisé) | 23 | Page déjà à jour depuis le 9 juin, compteurs index/main.js rattrapés |
| Grow a Garden | 2 (index/main.js) | 3 | Page déjà à jour depuis le 9 juin, compteurs rattrapés |
| Shindo Life | 11 | 18 | Codes majeurs mis à jour : 8 anciens expirés, 15 nouveaux confirmés |

**Shindo Life — codes entrés (vérifiés ≥ 2 sources, juin 2026) :**
2mLikesC0d3d! (40k RELLcoins + 400 spins), ShindoXm4z1! (50k + 300), kemekaAkumnaB! (32k + 200), ShindoXm4z2! (30k + 200), m4dar4kum5! (5k + 100), LiGhTweighT!, BiccB0i!, SHINDO50!, RabbitNoJutsu!, Underdog!, BaconBread!, Sou1b3ad!, R341G4M35!, GlitchesFixes!, Alchemist!, BigFatBunny!, EasterIsH3re!, EggHaunt!

**Codes inchangés (déjà à jour, vérifiés) :**
- Blox Fruits : 23 ✅
- Bee Swarm Simulator : 17 ✅ (FOURtunate/DiscordMillion/777 confirmés actifs)
- Jailbreak : 4 ✅ (apr26, rich100rich, 25pass50, 20KCASH4U)
- Blade Ball : 23 ✅

---

## Étapes 3, 4, 5, 6 — Non modifiées

Aucun changement SEO/vidéos, tier lists, guides complets ou UGC ce jour — priorité donnée à l'étape 1 (nouveaux jeux).

---

## Étape 7 — Jeu de la semaine

**Ignoré** — mercredi (uniquement le lundi).

---

## QC — Résultats sur les fichiers modifiés

| Fichier | GA4 | Nav 6 | data-cta | v=17 |
|---------|-----|-------|----------|------|
| codes/evade.html | ✅ | ✅ | ✅ | ✅ |
| codes/dragon-adventures.html | ✅ | ✅ | ✅ | ✅ |
| codes/car-dealership-tycoon.html | ✅ | ✅ | ✅ | ✅ |
| codes/pls-donate.html | ✅ | ✅ | ✅ | ✅ |
| codes/wizard-alchemy.html | ✅ | ✅ | ✅ | ✅ |
| codes/restaurant-tycoon-3.html | ✅ | ✅ | ✅ | ✅ |
| codes/shindo-life.html | ✅ | ✅ | ✅ | ✅ |

---

## Étape 9 — Bump cache JS

`main.js?v=16` → `main.js?v=17` appliqué sur **135 fichiers HTML** (racine, codes/, tier-list/, ugc-gratuit/, guides/).

Vérification : 0 fichier restant en v=16, 135 en v=17. ✅

---

## Fichiers modifiés ce jour

```
codes/evade.html               ← nouveau
codes/dragon-adventures.html   ← nouveau
codes/car-dealership-tycoon.html ← nouveau
codes/pls-donate.html          ← nouveau
codes/wizard-alchemy.html      ← nouveau
codes/restaurant-tycoon-3.html ← nouveau
codes/shindo-life.html         ← codes mis à jour (11→18)
codes/index.html               ← +6 entrées ALL_GAMES, sync Fisch/GaG/Shindo
js/main.js                     ← +6 ROBLOX_THUMBS, +6 ROBLOX_UNIVERSE_IDS, +6 GAMES_INDEX, sync Fisch/GaG/Shindo
+ 135 fichiers HTML            ← main.js?v=16 → v=17
```

---

## Pour publier

Dans le dossier GameNova, lance :

```bash
git add -A && git commit -m "MAJ Zoneblox du 10 juin 2026 — +6 jeux (Evade, Dragon Adventures, CDT, PLS DONATE, Wizard Alchemy, RT3), codes Shindo Life v18, cache v17" && git push origin main
```

Hostinger déploie automatiquement après le push.
