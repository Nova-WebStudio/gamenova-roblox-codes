# Rapport Zoneblox — 15 septembre 2026 (mardi)

> ⚠️ **Sandbox bash indisponible (4ᵉ run consécutif)** — bug lié à la mise à jour Windows du 8 sept. : le mount Plan9 échoue. Conséquence : `build_codes_json.py`, `build_sitemap.py`, `sync_month.py`, `node --check` et `git` **n'ont pas pu être exécutés**. Toutes les éditions ont été faites via l'outil Edit (remplacement littéral exact, aucun risque de null byte / troncature). **Des codes ont changé ce run → `data/codes.json` et les `lastmod` du sitemap sont à régénérer dès le retour de bash.** (Voir commandes en fin de rapport.)

---

## (a) Codes vérifiés

### hotGames — 2 rotations réelles, le reste stable

| Jeu | Résultat | Source(s) datée(s) |
|-----|----------|--------------------|
| **Volleyball Legends** | 🔄 **CHANGÉ** — Update 87. Actifs : **UPDATE_87 / RONIN_RETURN / KATANA**. Anciens UPDATE_86 / HAKKA_RETURN / SPIKER → expirés. 3→3 | GamesRadar (14 sept., liste active/expirée explicite) + RoCodes + Roonby |
| **Anime Vanguards** | 🔄 **CHANGÉ** — actifs : **Assault / SummerLeaving / AnniNextHopefully**. Anciens MiniUpd2 / Wrath / Retribution → expirés. 3→3 | GamesRadar (14 sept.) + Pocket Gamer + PCGamesN + Beebom |
| Blue Lock Rivals | **inchangé** (4 : NELKING/NIKOSOON/UBERSMONTH/SORRYLOADING). ⚠️ Un set alternatif (NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK!/SORRYFORNIKODELAY) est apparu dans un snippet de recherche **mais introuvable sur une page datée réelle** (PC Gamer fetché = 4 sept., 3 codes ; Pocket Gamer 12 sept. = notre set) → **prudence, en attente** | PC Gamer, Pocket Gamer |
| Fisch | **inchangé** (3 : scarlet/TemporarySubmarine/CARBON). LittleBudlingUpdate = code d'event **déjà expiré le 14 sept.** → non ajouté | PC Gamer (13 sept.), GamesRadar |
| Blade Ball | **inchangé** (13, aucun nouveau code) | GamesRadar, Roblox Den |
| Fruit Battlegrounds | **inchangé** (2, sous-listage acceptable) | Pocket Gamer, PCGamesN |
| Blox Fruits | **inchangé** (24) | Beebom (13 sept.) |
| Grow a Garden | **inchangé** (RDCAward, BEANORLEAVE10) | PGG, Beebom, Pocket Gamer |
| Steal a Brainrot | **inchangé** (1, conflit persistant → prudence) | agrégateurs |

Dates « 🔄 Vérifié le » rafraîchies au **15 sept.** sur toutes ces pages. *(king-legacy et pet-simulator-99 non revérifiés en profondeur ce run — dates non touchées.)*

### Rotation quotidienne (ÉTAPE 2ter) — 10 slugs traités + 3 flaggés

**1 correction majeure de faux-actifs :**
- **Anime Squadron** (jamais vérifié) : nos **8 « codes actifs » étaient tous périmés** (codes de lancement UPD0.5!/Yokoso!/50kCCU!/10MilVisits!/Eclipse!/LongMaintenance!/Tysm60kCCU!/EverythingIsPartOfMyPlan! — le jeu est désormais à l'Update 4.0). GamesRadar (7 sept.) liste explicitement 5 d'entre eux en expirés + les 3 autres absents de la liste active. → **8→5** actifs (10KCCUTHANKS! / CrystalCompensation / UPD4.0! / ThePowerToProtect! / TheCalamity!), 8 déplacés en expirés, compteur hero (8→5) + changelog corrigés.

**Confirmés OK (sous-listage acceptable, aucune preuve d'expiration) :**
- **universal-tower-defense-x** — ⚠️ **désambiguïsation importante** : notre page correspond à **« Universal Tower Defense Z »** (univers anime : ArrancarSupremacy!/DBSUpdPatch!/Wano…), codes confirmés actifs par Insider Gaming/RoCodes. **Le « Universal Tower Defense » de PCGamesN est un AUTRE jeu** (codes hiver, page de mars 2026) — à ne pas confondre.
- **spongebob-tower-defense** (2 ; GetGudKid confirmé actif)
- **weapon-rng** (4 : UPD6/WEAREBACK/UPD4/GRAVEYARD, tous confirmés actifs par Roblox Den 14 sept., 0 expiré ; sous-listage de 10)
- **anime-spirits** (6, tous confirmés actifs parmi 102 — Pocket Gamer 13 sept.)
- **slime-rng** (11, tous confirmés actifs parmi 22)
- **rng-heroes** (2, EasyPotions confirmé actif parmi 21)
- **blox-monsters** (5, tous confirmés actifs parmi 15 — Insider Gaming 2 sept., 0 expiré)
- **case-simulator-rng** (1, UPGRADER nouveau non ajouté <3 sources)
- **survive-the-killer** (0 actif = **honnête**, confirmé « aucun code » par PocketTactics/Beebom/RobloxDen)

Dates « 🔄 Vérifié le » rafraîchies au **15 sept.** + `catalogVerify` mis à jour pour ces 10 slugs (+ blade-ball ajouté).

**⚠️ À revérifier au prochain run (non touchés, dates non rafraîchies) :**
- **anime-stars** — collision de nom/version : nos codes (SRRYRIMULE/UPDATE05/1MVISITS…) sont d'époque « lancement » ; le jeu « Anime Stars » actuel est à l'Update 3.5/4 (4MVISITS) avec des codes tout autres. Risque de confusion Anime Stars / Anime Stars Simulator / Anime Astral Simulator → désambiguïser via placeId.
- **evomon** — nos 4 codes milestone (SeasonComing/20KMEMBERS/20000LIKES/30K-LIKES) ni confirmés ni infirmés (21 actifs listés, liste partielle) → à confirmer sur liste complète.
- **catch-and-tame** — **sous-liste majeure** : notre page affiche « Aucun code » alors que **36 codes actifs existent** (PC Gamer/PGG/Pocket Tactics 8 sept.). À **compléter proprement** (≥3 sources/code + regen codes.json) dès le retour de bash — non ajouté à l'aveugle (plusieurs codes « statut incertain »).

**Candidats en attente :** Blue Lock Rivals set NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK!/SORRYFORNIKODELAY (non confirmé sur page datée) ; Fisch LittleBudlingUpdate (expiré) ; Anime Vanguards « Prepare » (listé actif par GamesRadar mais laissé expiré par prudence).

---

## (b) Directeur SEO (ÉTAPE 2bis)

**Trending re-scanné** (rblxdb / Roblox charts, 7 sept.) : #1 **Steal An Egg** (~1,4M, couvert), leaders evergreen tous couverts. **2 nouveaux hits NON couverts détectés :**
- **Jump for Animals** (~60K CCU, live depuis le 12 août)
- **Search For The Needle** (~36K, depuis le 23 août)

→ Inscrits comme **brique prioritaire J30** (création de page ÉTAPE 1) **dès le retour de bash** (thumbnail API + sitemap + codes.json + QC requis).

**Brique d'autorité du jour :** conformément aux runs J26–J28 et vu l'indisponibilité de bash, la brique retenue est **l'assainissement des signaux de confiance** (correction Anime Squadron 8→5 faux-actifs + 2 rotations hotGames). **Aucune nouvelle URL créée** : créer une page sans pouvoir régénérer sitemap/codes.json ni passer le QC serait un demi-travail (choix honnête). Roadmap mise à jour : J28 archivé, **J29 (15 sept.) écrit**, prochaine brique J30 inscrite.

---

## (c) Jeux ajoutés / guides / tier lists / UGC / Jeu de la semaine

- **Aucun jeu ajouté** ce run (bash indisponible → intégrations sitemap/codes.json impossibles).
- **Jeu de la semaine** : non concerné (mardi ; MAJ le lundi uniquement).
- Guides / tier lists / UGC : non modifiés ce run (priorité codes + contrainte technique).

---

## (d) Fichiers touchés + QC

**Pages codes modifiées (codes réellement changés) :**
- `codes-volleyball-legends.html` (active 3→3 rotation, expirés +3, changelog, Vérifié le)
- `codes-anime-vanguards.html` (active 3→3 rotation, expirés +3, changelog, Vérifié le)
- `codes-anime-squadron.html` (active **8→5**, expirés +8, compteur hero 8→5, changelog, Vérifié le)

**Pages codes — date « Vérifié le » rafraîchie uniquement (aucun code changé) :**
- hotGames : `codes-fisch`, `codes-blade-ball`, `codes-fruit-battlegrounds`, `codes-blue-lock-rivals`, `codes-blox-fruits`, `codes-grow-a-garden`, `codes-steal-a-brainrot`
- rotation OK : `codes-universal-tower-defense-x`, `codes-spongebob-tower-defense`, `codes-weapon-rng`, `codes-anime-spirits`, `codes-slime-rng`, `codes-rng-heroes`, `codes-blox-monsters`, `codes-case-simulator-rng`, `codes-survive-the-killer`

**Autres fichiers :**
- `tools/code-watch.json` (snapshots volleyball/anime-vanguards, catalogVerify +11 slugs & dates, bloc `_pending2026-09-15`)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (J29 + prochaine brique J30)

**QC effectué (dans la limite des outils sans bash) :**
- ✅ Les 3 pages à codes changés se terminent par `</html>` (exactement 1 occurrence chacune).
- ✅ Compteurs hero cohérents (Volleyball 3, Anime Vanguards 3, Anime Squadron 5) ; compteurs de listes expirées mis à jour (Volleyball 27, Anime Vanguards 29, Anime Squadron 8).
- ✅ Éditions par remplacement littéral exact via l'outil Edit → aucun null byte, aucune troncature possible ; blocs `.code` ajoutés/retirés auto-équilibrés (divs).
- ⚠️ **Non exécutés (bash indisponible)** : `build_codes_json.py`, `build_sitemap.py`, `sync_month.py`, `node --check js/main.js`, scan git d'intégrité. `js/main.js` **non modifié** ce run → pas de bump de cache requis.

---

## À faire par Peter — dès que la sandbox / le poste refonctionne

Des codes ont changé (Volleyball Legends, Anime Vanguards, Anime Squadron) → **régénérer les fichiers dérivés** :

```
cd GameNova
python3 tools/build_codes_json.py
python3 tools/build_sitemap.py
python3 -c "import json;json.load(open('data/codes.json'))"
python3 -c "import xml.dom.minidom as m; m.parse('sitemap.xml')"
```

**Pour publier :** dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.
