# Rapport Zoneblox — 14 juin 2026 (dimanche)

Dimanche → **pas** de mise à jour « Jeu de la semaine » (lundi uniquement). Aucun nouveau jeu ajouté ce run (l'ajout exige l'API Roblox pour éligibilité ≥4000, universe IDs, miniatures `tr.rbxcdn.com` et vidéos vérifiées via oEmbed — voir contrainte réseau ci-dessous).

## Contrainte d'environnement (inchangée)

- **Shell sans accès réseau sortant** : `curl` renvoie HTTP 000 sur tous les domaines (games.roblox.com, groups.roblox.com, apis.roblox.com, etc.). `web_fetch` reste limité au *provenance set*. → L'**ÉTAPE 0 automatisée** (résolution universeId, description in-game, shout de groupe via `code-watch.json`) **n'a pas pu s'exécuter**.
- **WebSearch disponible** : utilisé en repli pour vérifier les codes des jeux chauds sur 2+ sources fiables.
- **Mount shell désynchronisé en écriture** : après édition via l'outil de fichiers, la vue `bash` affiche une version **tronquée/obsolète** des fichiers modifiés (faux positifs « pas de `</html>` », fausses imbalances `<div>`). Vérification des fichiers édités faite via l'outil de lecture fiable + `Grep` (tous confirmés complets, voir QC).

## ÉTAPE 0 / 2 — Vérification des codes (repli WebSearch, 2 sources)

| Jeu | Statut | Action |
|-----|--------|--------|
| **Blox Fruits** | Tableau principal déjà à jour (23 codes, EASTEREXP en tête). Mais FAQ JSON-LD, bandeau et « update-highlight » citaient encore des codes périmés du 5 juin (TRIPLEABOMB, Sub2Brawlexecution) absents du tableau. | **Harmonisé** : FAQ, bandeau et highlight réécrits sur la liste réelle ; date → 14 juin 2026 ; `dateModified` → 2026-06-14. Sources : PC Gamer, BlueStacks, PCGamesN. |
| **Volleyball Legends** | **3 nouveaux codes** confirmés sur 2+ sources : `UPDATE_74` (5 Lucky Style Spins), `SEASON_16` (5 Lucky Style Spins), `SUMMER_UPDATE` (5 Lucky Ability Spins). | **Ajoutés** au tableau (en tête) ; compteur 3 → **6 codes actifs** ; bandeau, statut, FAQ et dates → 14 juin 2026 ; `dateModified` → 2026-06-14. Sources : Beebom, Pro Game Guides, Roonby, GamesRadar, PCGamesN. |
| **Blue Lock Rivals** | Inchangé — 26 codes en page (NELHIORI, SNOWFLAKE, HIORIREWORK, MASTEROFALLTRADES, OTOYAUPD…) déjà alignés sur ProGameGuides/PC Gamer. | Aucune modification (date laissée honnêtement au 11 juin). |
| **Grow a Garden** (original) | Inchangé — aucun nouveau code (le studio a sorti « Grow a Garden 2 », jeu distinct). RDCAward, BEANORLEAVE10, torigate toujours listés. | Aucune modification. |

`tools/code-watch.json` **non modifié** : sans fetch réel des descriptions in-game (API down), renseigner `descLen`/`descExcerpt`/`lastChecked` serait malhonnête. Snapshots laissés intacts, conformément aux runs précédents.

⚠️ **Rappel backlog** : *Grow a Garden 2* (lancé le 12 juin, code de lancement TEAMGREENBEAN) reste un **candidat à ajouter en ÉTAPE 1** dès rétablissement de l'API (éligibilité ≥4000, universe ID, miniature). Une page `grow-a-garden-2` existe déjà au catalogue (126 jeux) — à vérifier/maintenir, ne pas confondre avec l'original.

## ÉTAPE 3 — Contenu minimum (indexation) : étoffement honnête

Mesure stricte des mots de texte **visible** (corps `<body>` hors `<script>`/`<style>`, tokens de mots) : **38 pages** sous le seuil de 1200 par cette méthode (la mesure du run précédent était plus permissive ; il s'agit surtout de pages à 1109–1199). Étoffement des **3 plus courtes** ce run (max 6/run), via ajout de prose française honnête et utile (aucun chiffre/mécanique inventé) :

| Page | Avant | Ajout | Après (est.) |
|------|------:|-------|------:|
| codes/king-legacy.html | 1109 | +2 paragraphes « À propos » (structure des mers, méta mouvant, gestion des Gems) | ~1300 |
| codes/dragon-blox.html | 1114 | +2 paragraphes « À propos » (boucle d'entraînement/transformations, système d'invocation des Wish Tokens) | ~1340 |
| codes/arsenal.html | 1128 | +2 paragraphes « À propos » (mode Gun Game, équilibrage cosmétique des codes) | ~1360 |

📋 **Backlog indexation (à étoffer aux prochains runs, par ma mesure stricte, ~150-250 mots chacune)** : scroll-a-brainrot, restaurant-tycoon-3, grow-a-garden, fruit-battlegrounds, dig, tour-needoh, arene-de-sniper, pls-donate, project-mugetsu, car-dealership-tycoon, fish-it, sailor-piece, volleyball-legends, doors, royale-high, work-at-a-pizza-place, combat-warriors, dead-rails, wizard-alchemy, fisch, bedwars, dandys-world, slap-battles, jailbreak, pet-simulator-99, project-slayers, anime-vanguards, slime-rng, be-a-brainrot, toilet-tower-defense, tower-of-hell, adopt-me, my-gaming-cafe, brookhaven, grow-a-garden-2 (toutes 1109–1199).

## ÉTAPE 8 — QC

- **`</html>` présent** : ✅ 128/128 pages codes (vérifié via `Grep` fiable, y compris les 5 pages éditées).
- **GA4 `G-FEL71QVHNL`** : ✅ présent sur 100 % des pages HTML du site.
- **Cache JS** : uniforme **`main.js?v=24`** sur les 218 fichiers HTML ; `js/main.js` non modifié → pas de bump. `node --check js/main.js` ✅.
- **Nav** : lien `/avatar/` présent sur 216/216 pages (hors dossier avatar). 0 page sans Avatars.
- **GAMES_INDEX (126) ↔ ALL_GAMES (126)** : 0 écart.
- **Équilibre `<div>`** : 0 déséquilibre sur le site (hors `avatar/index.html`, voir ci-dessous). Mes ajouts sont du `<p>` pur ou des lignes de tableau équilibrées → balance préservée.
- **Octets nuls** : 0 sur tout le site.
- **JSON-LD** : valide sur blox-fruits et volleyball-legends après édition (FAQPage/Article).

### ⚠️ À signaler (non corrigé, hors périmètre)

- **`avatar/index.html`** est **non suivi par git** (`?? avatar/`) et apparaît **tronqué** (se termine en plein `<div class="social-link`, sans `</body></html>` ; ~19,5 Ko). Le dossier `/avatar/` a son propre pipeline manuel (build-items.mjs) — **je n'y touche pas** par consigne. À vérifier par Peter : soit le fichier est réellement coupé (à régénérer via le pipeline), soit c'est encore un artefact de mount. `git add -A` l'ajouterait au dépôt en l'état.

## Fichiers touchés ce run

- `codes/blox-fruits.html` (harmonisation codes périmés + dates)
- `codes/volleyball-legends.html` (+3 codes vérifiés, compteurs, dates)
- `codes/king-legacy.html`, `codes/dragon-blox.html`, `codes/arsenal.html` (étoffement ≥1200 mots)
- `rapport-zoneblox-2026-06-14.md` (ce rapport)

## Étapes 1, 4, 5, 6 — non réalisées ce run

Ajout de jeux / nouvelles tier lists / guides complets / vérif UGC : dépendent de l'API Roblox (données non inventables). Reportées au rétablissement de l'accès réseau. Candidat prioritaire : *Grow a Garden 2*.

---

# Suite du run (lot 2)

## Codes — vérifications supplémentaires (WebSearch, 2+ sources)

| Jeu | Statut | Action |
|-----|--------|--------|
| **Fisch** | La page n'affichait que **4 codes actifs** (nettoyage du 12 juin), alors que 7+ agrégateurs (Pro Game Guides, Pocket Gamer, Beebom, BlueStacks, Game8, PC Gamer, RoCodes) listent ~23 codes actifs en juin 2026 — Fisch étant connu pour des codes qui **expirent rarement**. | **Sovereign** et **Companions** rétablis en actifs avec récompenses vérifiées (≈ 1 000 C$ + objets spécifiques), retirés de la liste expirée (19 → 17). Compteur 4 → **6 codes**, dates → 14 juin, intro et `dateModified` mis à jour. |
| **Anime Vanguards** | Page déjà à jour avec des codes récents (OopsiePoopsie2, HeHasArrived, BumBum, Spring26, SorryForAutoSell). Liste AV très volatile côté agrégateurs. | Aucune modification (pas de nouveau code confirmable proprement). |

⚠️ **À surveiller (Fisch)** : au-delà de Sovereign/Companions, les agrégateurs listent encore une quinzaine de codes en « actifs » que la page Zoneblox a passés en expirés le 12 juin (LivyatanAndCompanions, Shady, BIGGLE, MermaidCove, WrathOfOlympus, EverturnForest…). Je ne les ai **pas** restaurés en masse faute de récompenses individuellement vérifiées et parce que plusieurs sont saisonniers — mais la divergence mérite une revue : le « grand nettoyage » du 12 juin a probablement été trop agressif pour un jeu dont les codes n'expirent quasiment jamais.

## Contenu minimum (indexation) — lot 2 (3 pages)

| Page | Avant | Ajout | Après (est.) |
|------|------:|-------|------:|
| codes/restaurant-tycoon-3.html | 1128 | +2 paragraphes (équilibrage dépenses/revenus, social & saisonnier) | ~1330 |
| codes/fruit-battlegrounds.html | 1132 | +2 paragraphes (combat pur vs RPG, méta des fruits) | ~1340 |
| codes/scroll-a-brainrot.html | 1125 | +2 paragraphes (boucle collecte/revenus, mises à jour fréquentes) | ~1330 |

**Total étoffement ce run : 6 pages** (king-legacy, dragon-blox, arsenal, restaurant-tycoon-3, fruit-battlegrounds, scroll-a-brainrot) — limite de 6/run atteinte.

## QC lot 2
- `</html>` : ✅ 9/9 fichiers édités (Grep fiable). Octets nuls : 0. JSON-LD inchangé hors `dateModified`.
- Édits = `<p>` purs ou lignes de tableau équilibrées → balance `<div>` préservée.
- Aucune référence périmée résiduelle sur Fisch (« 4 codes », « 12 juin ») après mise à jour.

## Fichiers touchés (total run)
`codes/blox-fruits.html`, `codes/volleyball-legends.html`, `codes/fisch.html`, `codes/king-legacy.html`, `codes/dragon-blox.html`, `codes/arsenal.html`, `codes/restaurant-tycoon-3.html`, `codes/fruit-battlegrounds.html`, `codes/scroll-a-brainrot.html`, `rapport-zoneblox-2026-06-14.md`.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
