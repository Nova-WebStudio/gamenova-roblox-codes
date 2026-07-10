# Rapport Zoneblox — 10 juillet 2026 (vendredi)

Run quotidien automatique. Priorité absolue : vérification des codes. Jour = vendredi → **pas** de mise à jour « Jeu de la semaine » (réservée au lundi).

Règle de sourcing appliquée : un code n'est ACTIF que s'il est confirmé par **≥3 sources fiables OU une source officielle** (Trello / Twitter-X / description in-game / shout du groupe). Conflit entre sources → version la **plus prudente** + candidat « en attente » dans `code-watch.json`.

---

## 1. Changements de codes réels ce run

| Jeu | Résultat | Sources | Action |
|-----|----------|---------|--------|
| **Catch a Monster** | **CHANGEMENT — passe dédiée : conflit résolu + nettoyage** | **Pocket Tactics (1 juil.)** + **Pro Game Guides (3 juil.)** + **Destructoid (9 juil., la plus fraîche)** | La page listait **15 codes** dont plusieurs **expirés** (ELECTNOV, BHCOIN, BRWAD, OVERVOLT — dans les listes « expired » de PT et Destructoid) et deux introuvables dans les sources actuelles (MEOWLY, SCAREEP, + PECTSHALL douteux). Destructoid (9 juil.) **corrobore PGG** : `graon`/`magmorus`/`moovik`/`danvok` **actifs** (seul PT, plus ancien, les disait expirés). `crysting` confirmé actif par **les 3** sources / 2 réseaux. Nouveaux confirmés (PGG + Destructoid) : `clacerglaw`, `massglaw`, `cabshark`. **Set actif nettoyé et reconstruit : 6 → 11 codes** (clacerglaw, massglaw, cabshark, ungolem, crysting, graon, magmorus, moovik, danvok, LIVEXP, LIVECOIN). Titre/H1/og/JSON-LD « juin » → « juillet 2026 », `dateModified` 2026-07-10, `Mis à jour le 10 juillet 2026`, compteur 11, FAQ (2 emplacements) mise à jour. Page = **1551 mots**. |
| **Spin a Soccer Card** | **CHANGEMENT — rotation hebdomadaire** | Pocket Gamer, Pocket Tactics, Dexerto, PCGamesN, PGG, Destructoid, Roblox Den, Beebom, TechWiser (~9 sources) | Codes hebdomadaires (1 par semaine, expirent chaque semaine). Nouveau code actif **`BLAZE-STORM`** (2 packs + 3 spins) largement confirmé ; l'ancien `PHOENIX-MYTHIC` (semaine précédente) déplacé en **expirés (7 → 8)**. Titre/H1/og/JSON-LD → « juillet 2026 », `dateModified` 2026-07-10, `Mis à jour le 10 juillet 2026`. Page = **1630 mots**. |

**Codes ajoutés (actifs) :** Catch a Monster +6 nets (clacerglaw, massglaw, cabshark, crysting, ungolem réactivés/ajoutés) ; Spin a Soccer Card +1 (BLAZE-STORM).
**Codes retirés (expirés/non confirmés) :** Catch a Monster −7 (ELECTNOV, BHCOIN, BRWAD, OVERVOLT, MEOWLY, SCAREEP, PECTSHALL) ; Spin a Soccer Card −1 actif (PHOENIX-MYTHIC → expirés).

## 2. Autres jeux « hot » vérifiés — aucun changement (prudence)

| Jeu | Sources | Décision |
|-----|---------|----------|
| **Hypershot** | Beebom, Dexerto, Destructoid, RoCodes, Pocket Tactics | ONEBILLION/SIXSEVEN/HAPPYMAY/NEWUPDATE toujours actifs. Candidat **`100K`** cité par des agrégateurs mais **non confirmé ≥3 sources nommées** → « en attente ». Inchangé. |
| **FIFA Super Soccer** | Beebom, Dexerto, Destructoid, Insider Gaming | WorldCupSecret (event Coupe du monde jusqu'au 31/07), bestfootball, fifasupersoccer confirmés. sub2fssdevilz = code sub permanent conservé. Inchangé. |
| **Merge a Nuke** | Dexerto, Pocket Tactics, GamesRadar, Beebom | ATOMIC/UPDATE2 confirmés actifs (aucun expiré) ; BOOM présent dans la description in-game (officiel). Inchangé. |
| **Grow a Garden** | PC Gamer, PGG, Roblox Den, Beebom | RDCAward/BEANORLEAVE10 cohérents. Candidat **`TEAMGREENBEAN`** enregistré « en attente » : les sources **confondent Grow a Garden et Grow a Garden 2** — à rattacher au bon jeu avant publication. Inchangé. |
| **Steal a Brainrot** | PCGamesN, Beebom, Pocket Tactics, RBLXGUIDE | Sources toujours en conflit (« 0 code » vs « 22 codes » non listés). Prudence : page sans code maintenue. |
| **Blade Ball** | Beebom, Pocket Tactics, GamesRadar, The Click | **Divergence forte** : un agrégateur liste un set très différent du nôtre (5BVISITS/DRAGONS/DELAYBALL/1.5BTHANKS… vs SERPENT/4BVISITS/2BTHANKS…). « Aucun nouveau code depuis un moment, anciens valides » (01/07). Page **non modifiée** (ne pas dégrader) → **passe dédiée requise** au prochain run pour reconcilier. |

## 3. Rafraîchissement « Vérifié le » (toutes les pages codes)

Ligne « 🔄 Vérifié le » mise à jour au **10 juillet 2026** sur **les 166 pages** `codes/<slug>.html` (idempotent, exactement 1 par page, 0 doublon, 0 insertion nécessaire, 0 page restée au 9 juillet). Les dates « Mis à jour le » n'ont **pas** été touchées, sauf **Catch a Monster** et **Spin a Soccer Card** (changements réels de liste).

## 4. Incident d'intégrité corrigé (anti-troncature)

Au 1er passage, l'édition de `codes/catch-a-monster.html` (774 null bytes en fin de fichier) et `codes/spin-a-soccer-card.html` (troncature en fin de script) a été détectée par le QC. **Les deux fichiers ont été restaurés depuis `git show HEAD:` puis toutes les modifications ré-appliquées via un script Python à ancres uniques**, avec re-vérification : 0 null byte, fin `</body></html>`, `<div>` équilibrés. Aucun fichier tronqué n'a été conservé.

## 5. Jeux « hot » NON revus en profondeur ce run (à prioriser au prochain run)

**Blade Ball** (passe dédiée multi-sources pour reconcilier la divergence), **Grow a Garden / Grow a Garden 2** (identifier le jeu propriétaire de TEAMGREENBEAN), puis `run-a-restaurant`, `noob-incremental`, `tower-defense-simulator`, `pet-simulator-99`, `100-days-at-sea`, `defend-ur-base-with-anime`, `vv-ultimatum`, `world-fighters`, `king-legacy`. Blox Fruits / Anime Vanguards / Fisch / Blue Lock Rivals / Volleyball Legends / Anime Last Stand / Fruit Battlegrounds / Squid Game X : vérifiés 05–09/07 (inchangés). Reste du catalogue (~150 pages) : rafraîchissement de date reçu.

## 6. Autres étapes

- **Ajout de jeux :** aucun ce run (priorité vérification codes).
- **Guides / tier lists / UGC :** aucun créé/modifié ce run.
- **Jeu de la semaine :** non touché (vendredi).
- **js/main.js :** non modifié → **pas** de bump de cache (site uniformément en `main.js?v=32`, 311/311 pages).

## 7. QC (résultat)

- ✅ **0 null byte** sur l'ensemble des pages `codes/*.html` ; toutes finissent par `</html>`.
- ✅ Balises `<div>` équilibrées sur **tout le site** (0 fichier déséquilibré).
- ✅ Version cache JS uniforme : `main.js?v=32` (311/311 pages).
- ✅ Les 166 pages codes : « 🔄 Vérifié le 10 juillet 2026 » (1 par page, 0 doublon) ; 0 page restée au 9 juillet.
- ✅ Pages éditées (Catch a Monster, Spin a Soccer Card) : GA4 `G-FEL71QVHNL` présent, `data-cta="guidelink"` (1 seul), nav 7 entrées (Avatars OK), cache `main.js?v=32`, **≥1200 mots** (1551 / 1630), titres/H1/og/JSON-LD « juillet 2026 », `dateModified` 2026-07-10, compteurs cohérents (11 / 1 actif).
- ✅ `tools/code-watch.json` : JSON valide, 0 null byte, finit par `}` ; snapshots `lastChecked` au 2026-07-10 pour catch-a-monster (11 knownCodes), spin-a-soccer-card (BLAZE-STORM), hypershot, fifa-super-soccer, merge-a-nuke, grow-a-garden, steal-a-brainrot, blade-ball.
- ✅ Aucun rédactionnel anglais introduit.

**Fichiers touchés :** 166 pages `codes/*.html` (rafraîchissement date) dont `codes/catch-a-monster.html` et `codes/spin-a-soccer-card.html` (changements de codes réels) + `tools/code-watch.json` + ce rapport. (167 fichiers suivis modifiés, 0 fichier non suivi.)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.

---

# Complément — Passe dédiée « Animal Hospital » (demande de Peter, 10 juillet, soir)

Peter a signalé que **Animal Hospital** (https://www.roblox.com/games/78515283254292/Animal-Hospital) est en train de percer et demande de tout développer. Vérification et mise à jour des **3 pages dédiées**.

## Données live Roblox (vérifiées via Chrome, 10 juillet 2026)
- **placeId** 78515283254292 → **universeId** 10148749921 (nom confirmé « Hôpital pour animaux (anomalie) 🧪 »).
- **Joueurs simultanés : 908 914** · **visites : 675 691 750** (675 M) · **favoris : 1 168 885** · maxPlayers 30.
- Créé le **10 mai 2026**, dernière MAJ Roblox **10 juillet 2026 15:59 UTC** (un update est sorti aujourd'hui).
- Créateur : groupe **Animal Anomaly** (id 344908697, badge vérifié, propriétaire **Roytt**). → Confirme un vrai phénomène en pleine ascension.
- **Miniature** : hash `db27bdc698b088f2d8352327f7dc64f6` — déjà correcte sur la page (tr.rbxcdn.com), inchangée.

## Codes — statut (règle de sourcing appliquée)
**Toujours AUCUN système de codes** au 10 juillet 2026. Confirmé par : **Pro Game Guides** (« Are There Any? »), **Dexerto.fr**, **Destructoid**, le **shout du groupe Roblox officiel** (= null, aucune annonce) et la **description in-game** (aucun code). → On maintient honnêtement « Pas encore de codes ». `code-watch.json` : ajout d'`animal-hospital` dans **hotGames** (id/groupId/placeId) + **snapshot** de référence (baseline, knownCodes vide, codeSystem=false) pour surveiller l'apparition d'une zone de rédemption aux prochains runs.

## Modifications appliquées
- **codes/animal-hospital.html** : refresh **juin → juillet 2026** (title, meta, og, H1, JSON-LD headline, FAQ ×2, intro, bannière, conclusion) ; `dateModified` → 2026-07-10 ; **stats actualisées** (79 M → **675 M visites, 1 M+ favoris, 900 K+ joueurs simultanés**, mention update du 10 juillet + entité « Ghost » fin juin) ; bannière sources renforcée (Pro Game Guides + groupe officiel + in-game) ; section « À propos » enrichie (phénomène, Roytt, Ghost). **1850 mots**.
- **guides/animal-hospital.html** : `dateModified` → 2026-07-10 ; méta classes « juin → juillet 2026 » ; **ajout de l'ennemi « Ghost »** (couloir, drain de Sanity, contré au taser/arme) dans la table des ennemis. **2088 mots**. *(NB : un incident de troncature de fin de fichier détecté au QC → fichier restauré depuis git puis 3 modifs ré-appliquées en 1 script Python ; revérifié : fin `</html>`, 0 null byte, div équilibrés.)*
- **tier-list/animal-hospital.html** : refresh **juin → juillet 2026** (title, meta, og, FAQ, H1, intro, consensus) ; **« Mis à jour le » 25 juin → 10 juillet 2026** (méta re-vérifiée : Surgeon = meilleure gratuite, Secret Agent = meilleure payante — consensus reconfirmé par Sportskeeda juillet 2026, Pocket Gamer, Pro Game Guides). Classement inchangé (aucun changement de méta confirmé). **2111 mots**.
- **tools/code-watch.json** : +1 hotGame, +1 snapshot ; JSON valide, finit par `}`.

## QC
- ✅ Les 3 pages : finissent par `</html>`, **0 null byte**, `<div>` équilibrés (0), **≥1200 mots** (1850 / 2088 / 2111), GA4 `G-FEL71QVHNL`, nav 7 entrées (Avatars OK), `data-cta="guidelink"` (codes, 1 seul), JSON-LD valides (3 blocs/page).
- ✅ Seule occurrence « juin 2026 » restante = **« fin juin 2026 »** (ajout Ghost, correct) ; « mai 2026 » = date de sortie (correct).
- ✅ `js/main.js` **non modifié** → pas de bump de cache (reste `v=32`). `node --check js/main.js` OK.
- ✅ `code-watch.json` valide.

**Fichiers touchés (cette passe) :** codes/animal-hospital.html, guides/animal-hospital.html, tier-list/animal-hospital.html, tools/code-watch.json.

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
