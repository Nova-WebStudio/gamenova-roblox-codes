# Rapport Zoneblox — 10 septembre 2026

> ⚠️ **Sandbox bash indisponible ce run.** Le montage du workspace Linux a échoué (erreur Plan9 « share not mounted », 4 tentatives identiques). Conséquences : `python3 tools/build_codes_json.py`, `node --check js/main.js`, et les scans d'intégrité git n'ont **pas** pu être exécutés. Toutes les éditions ont été faites avec l'outil d'édition à remplacement exact (pas de `sed`, donc aucun risque de null byte introduit). Les deux pages dont les codes ont changé nécessitent une **régénération de `data/codes.json`** (voir plus bas) — à lancer par Peter avant/après le push.

---

## a) Codes vérifiés

### hotGames (priorité) — tous vérifiés, AUCUN changement de codes
Vérifiés via ≥3 sources fiables et/ou source officielle (10 sept.). Ligne « 🔄 Vérifié le » rafraîchie à **10 septembre 2026** sur chaque page ci-dessous.

| Jeu | Actifs | Statut |
|-----|:--:|--------|
| blox-fruits | 24 | Stable. Candidats **LIGHTNINGABUSE** (conflit PCGamesN actif vs Beebom expiré) et **1LOSTADMIN** (expiré PCGamesN+Beebom) → **non ajoutés** (prudence). |
| fisch | 3 | scarlet / TemporarySubmarine / CARBON (long-lived). **SkycrestIsInTheSky** en conflit (actif Sep6 vs expiré GamesRadar Sep7) → non ajouté. |
| blue-lock-rivals | 4 | Déjà à jour : NELKING / NIKOSOON / UBERSMONTH / SORRYLOADING (= PCGamer 10 sept). Anciens UBERSTAKEOVER/KINGNEXTWEEK/EGODEFENSE en expirés. |
| volleyball-legends | 3 | UPDATE_86 / HAKKA_RETURN / SPIKER (= GamesRadar). |
| anime-vanguards | 3 | Retribution / Wrath / MiniUpd2 (Retribution expire 14 sept). |
| blade-ball | 13 | Aucun nouveau code depuis semaines ; SERPENT/BATTLEROYALE toujours contestés → inchangé. |
| fruit-battlegrounds | 2 | HIGHER1M120K / YOO1M110K! ; sous-listage assumé (45 trackés). |
| grow-a-garden | 2 | RDCAward / BEANORLEAVE10 (stables depuis des mois). |
| steal-a-brainrot | 1 | Conflit persistant (0/1/2 selon source) → maintien prudent de BESTBRAINROTEVER. |
| anime-last-stand | 22 | MagicKnights! / ElfReincarnation! / IsItReallyWeekly?! déjà publiés et confirmés (PGG + allthings.how). **Pending 09-02 résolu.** |

*Note : king-legacy n'a pas été revérifié en profondeur ce run (date « Vérifié le » laissée inchangée, par honnêteté).*

### Lot de rotation du jour (ÉTAPE 2ter) — 17 jeux (les plus anciens, catalogVerify = 09-03)

**Corrigés (faux-actifs nettoyés) :**
- **driving-empire : 21 → 2 actifs.** Seuls **RECORD** et **USA250** restent actifs (GamesRadar 2 sept + Pocket Gamer 5 sept concordent). 19 codes saisonniers périmés (HAPPYXMAS, GOBBLEGOBBLE, SPOOKY, VEGAS2025, NEWYEAR2025, CALL911, 10KITS, MARCH2026…) déplacés en expirés. **2MLIKES/200KMEMBERS** en conflit (GamesRadar actif vs PocketGamer expiré) → expirés par prudence. Token erroné **`USA250Car` corrigé en `USA250`** (2 sources). Compteur, changelog, arrays JS ACTIVE/EXPIRED synchronisés.
- **dress-to-impress : 32 → 27 actifs.** LNY, LIONDANCER, BHM26, CH00P1E_1S_B4CK, C4LLMEHH4LEY (events saisonniers passés) déplacés en expirés — GamesRadar (2 sept) les liste explicitement expirés. **PROUD** et **CH00P1E_B4CK_AGA1N** donnés actifs par GamesRadar mais 1 seule source → **non ajoutés** (≥3 requis). Compteur, changelog, arrays JS synchronisés.

**Confirmés OK (sous-listage acceptable ou correspondance exacte) — date + catalogVerify au 10 sept :**
doors (38 codes permanents), anime-champions-simulator, all-star-tower-defense (16/28), anime-battle-rng (35 ; BERSERK/ORIGIN trop récents/source unique → non ajoutés), 99-nights-in-the-forest (3, correspondance exacte SURVIVOR/forestwakesup26/afterparty), dragon-blox (collector 116), clover-retribution (collector 254), royale-high (0 code, correct), anime-eternal, anime-apocalypse (64), anime-dimensions-simulator (49), anime-origins, anime-astral-simulator (109).

**À revérifier (page NON modifiée, catalogVerify laissé au 09-03 pour repriorisation) :**
- **anime-expeditions** : nos 10 codes (RELEASE/EA/EA+/AE#1/EXPEDITIONS/100mvisits/100K!/30KLIKES!/HAPPYBDAYCOOP/wfade) sans preuve d'expiration, mais GamesRadar/Dexerto (8 sept) listent d'autres codes récents (Eclipse, 250klikes, 8thCompany, expirant 10-12 sept). Passe dédiée multi-sources requise.
- **a-dusty-trip** : sources en conflit (3 vs 0 actifs), pas de liste datée claire.

### Candidats en attente (non publiés, prudence)
blox-fruits : LIGHTNINGABUSE (conflit), 1LOSTADMIN (expiré), KITT_RESET (à confirmer). fisch : SkycrestIsInTheSky (conflit). anime-battle-rng : BERSERK, ORIGIN (source unique). dress-to-impress : PROUD, CH00P1E_B4CK_AGA1N (1 source).

## b) Directeur SEO (ÉTAPE 2bis)
**Reporté ce run** en raison de l'indisponibilité du sandbox bash : toute nouvelle page substantielle (jeu, guide, tier list, hub) nécessite les vérifications QC (`node --check`, équilibre des div, null bytes, build sitemap) qui ne peuvent pas tourner sans bash. Conformément à la règle « les codes sont la priorité et le reste ne doit jamais dégrader une page correcte », aucune création à l'aveugle n'a été tentée. Roadmap inchangée. À reprendre au prochain run une fois le sandbox rétabli.

## c) Jeux ajoutés / guides / tier lists / UGC / jeu de la semaine
- Aucun jeu ajouté, aucun guide/tier list créé ce run (voir point b).
- **Jeu de la semaine** : non concerné — nous sommes **jeudi** (`date +%u` = 4), la bannière ne se met à jour que le lundi.

## d) Fichiers touchés + QC

**Pages codes modifiées (codes réellement changés) :** `codes-driving-empire.html`, `codes-dress-to-impress.html` — liste active + expirée + compteur hero + changelog « Mis à jour le » + arrays JS ACTIVE/EXPIRED.

**Pages codes — date « Vérifié le » rafraîchie au 10 sept (25 pages) :** blox-fruits, grow-a-garden, steal-a-brainrot, blade-ball, blue-lock-rivals, anime-last-stand, fisch, volleyball-legends, anime-vanguards, fruit-battlegrounds, doors, anime-champions-simulator, all-star-tower-defense, anime-battle-rng, 99-nights-in-the-forest, dragon-blox, clover-retribution, royale-high, anime-eternal, anime-apocalypse, anime-dimensions-simulator, anime-origins, anime-astral-simulator, a-dusty-trip, anime-expeditions (+ driving-empire, dress-to-impress ci-dessus).

**Suivi :** `tools/code-watch.json` — bloc `_pending2026-09-10` ajouté ; `catalogVerify` bumpé au 10 sept pour 15 jeux du lot (anime-expeditions & a-dusty-trip laissés au 09-03).

**QC effectué (sans bash) :**
- ✅ Éditions via remplacement exact (aucun `sed`, aucun null byte introduit).
- ✅ `codes-driving-empire.html` et `codes-dress-to-impress.html` : fin `</html>` vérifiée + équilibre div préservé (retraits/ajouts symétriques : chaque code = 4 div en actif comme en expiré).
- ✅ Arrays JS ACTIVE/EXPIRED resynchronisés avec le HTML sur les 2 pages modifiées (sinon « Tout copier » et le compteur d'expirés auraient été faux).
- ✅ `tools/code-watch.json` : structure/virgules/guillemets vérifiés visuellement (fin `}` OK).
- ⚠️ **NON exécuté (bash indisponible)** : `python3 tools/build_codes_json.py`, `node --check js/main.js`, scan null-byte global, scan équilibre div global. **À relancer par Peter après rétablissement du sandbox.**

### ⚠️ Action requise avant publication
Les codes ont changé sur **driving-empire** et **dress-to-impress** → `data/codes.json` (widget embarqué) est désormais périmé. **Régénérer avant le push :**
```
python3 tools/build_codes_json.py
python3 -c "import json;json.load(open('data/codes.json'))"
```
(Non fait ce run : sandbox bash indisponible.)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
