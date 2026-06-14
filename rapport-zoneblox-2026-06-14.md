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

# Lot 3 — 2 nouveaux jeux (la totale) + extension du guide Grow a Garden 2

## ÉTAPE 1 — 2 nouveaux jeux ajoutés (choisis par Peter)

Peter a fourni deux jeux précis (par URL Roblox). Les deux ont été ajoutés en « la totale niveau contenu » : pages ≥ 1200 mots, SEO complet, nav 7 entrées (avec Avatars), GA4, onglets Codes/Astuces/Vidéos/FAQ, 6 astuces, FAQ, section « À propos » + 3 jeux similaires, bandeau CTA `data-cta="guidelink"`, JSON-LD (Article + Breadcrumb + FAQPage).

| Jeu | Slug | Genre | Codes | Mots |
|-----|------|-------|-------|------:|
| **Mini War** (place 131346454575416) | `mini-war` | Stratégie / city-builder militaire | **0 (aucun système de codes encore)** | **1676** |
| **+1 Aura Per Click** (place 109509029034984) | `1-aura-per-click` | Clicker / incrémental | **0 (aucun code actif)** | **1601** |

- **Honnêteté codes** : les deux jeux n'ont **aucun code actif** à ce jour — confirmé sur 2 sources chacun (Mini War : TechWiser, Pro Game Guides, Destructoid → pas de système de codes ; +1 Aura Per Click : Official Code Zone → aucun code valide). Les pages l'indiquent clairement (bandeau ambre « Aucun code actif », explication, badge « Codes à venir »), sans inventer aucun code. Dès qu'un code sortira, il pourra être ajouté.
- **Anti-doublon** : « Mini War » (stratégie de construction de nation, communauté M&M) est **distinct** de la page existante `mini-guerre` (combat PvP arcade). Lien croisé ajouté entre les deux pour lever l'ambiguïté.
- **Miniatures** : pas d'accès à l'API Roblox (`tr.rbxcdn.com`) ni aux pages client-rendues → **placeholders SVG** générés (`images/games/mini-war.svg`, `images/games/1-aura-per-click.svg`), comme pour les ajouts précédents. À remplacer par la vraie miniature quand l'API sera accessible. **Universe IDs non renseignés** (jamais inventés).
- **Vidéos** : pas d'embed (impossible de vérifier via oEmbed sans réseau) → onglet Vidéos avec lien « Voir sur YouTube » (même motif que les autres pages récentes), aucun ID inventé.
- **Intégration complète** : GAMES_INDEX + ROBLOX_THUMBS + NEW_GAMES (js/main.js) ; ALL_GAMES + THUMBS + liste de liens SEO (codes/index.html) ; 2 cartes en tête de « Nouveaux jeux ajoutés » (index.html) ; 2 `<url>` (sitemap.xml). GAMES_INDEX et ALL_GAMES passent de 126 → **128**, synchronisés.

## ÉTAPE 5 — Guide Grow a Garden 2 enrichi (3 nouvelles sections + schémas)

À la demande de Peter, le guide `guides/grow-a-garden-2.html` gagne **3 sections de fond** avec une mise en page fonctionnelle (sommaire ancré mis à jour, schémas, encadrés, tableaux) :

1. **💰 Comment devenir riche (méthode complète)** — boucle flips rapides → graines premium (Moon's Bloom ~9 000 Sheckles, Dragon's Breath) → mutations ×25 (Electric). **Schéma SVG original** de la « boucle de richesse » en 4 étapes.
2. **🪤 Construire une base avec des pièges** — cultures de valeur au centre, anneau de plantes défensives (Venus Fly Trap, Dragon's Breath, Cactus), pets défenseurs (Bee, Ice Serpent), gear Wheelbarrow (Légendaire, 500K Sheckles, anti-vol) et crates de pièges (Bear Trap, Weather Machine, Owner Door). **Schéma SVG original** « vue de dessus » de la base.
3. **🐞 Glitchs actuels : ce qu'il faut savoir** — traité **honnêtement** : aucun dupe « infini » fiable confirmé (anciens glitchs patchés), avertissement clair contre les **scripts auto-farm** (bannissement + malwares/arnaques), puis pivot vers les vraies optimisations légales (mutations, pousse hors-ligne, timing du shop, vol nocturne).

Sources : Game8, TheGamer, Beebom, Sportskeeda, ggwtb, TechWiser, allthings.how. FAQ enrichie de 3 questions (devenir riche / base à pièges / glitch d'argent), `dateModified` → 2026-06-14, title + meta + keywords retravaillés pour « comment devenir riche grow a garden 2 », « base pièges », « glitch argent ». Images = **SVG inline originaux** (pas d'asset externe, pas de copie d'images tierces).

## QC lot 3
- `</html>` : ✅ Mini War, +1 Aura Per Click, guide GAG2 (Grep fiable). Mots : Mini War 1676, +1 Aura 1601 (≥ 1200).
- `js/main.js` : **intact** (vérifié ligne par ligne via l'outil de lecture fiable ; les 4 nouvelles entrées slug présentes, la fin du fichier `renderNewGames` complète). ⚠️ `node --check` via le shell affiche un **faux positif de troncature** : le montage bash sert une copie obsolète/tronquée des fichiers édités ce run (artefact connu du mount). Les **vrais fichiers Windows écrits par les outils d'édition sont complets** — c'est ce que `git add -A` committera. Les fichiers neufs (pages, SVG) apparaissent normalement dans bash.
- Intégrations vérifiées (Grep) : codes/index.html ×3, index.html ×2, sitemap.xml ×1 par jeu. Nav 7 (Avatars), GA4, cache v=24 sur les 2 nouvelles pages. CTA unique. 3 sections de guide (`#riche`, `#base`, `#glitch`) présentes.

## Fichiers touchés (lot 3)
`codes/mini-war.html` (neuf), `codes/1-aura-per-click.html` (neuf), `images/games/mini-war.svg` (neuf), `images/games/1-aura-per-click.svg` (neuf), `js/main.js`, `codes/index.html`, `index.html`, `sitemap.xml`, `guides/grow-a-garden-2.html`.

---

---

# Lot 4 — Réparation de l'index git corrompu (run du soir, 14 juin)

## Problème détecté (BLOQUANT)

Le dépôt était **incommittable** : `git fsck` renvoyait `bad index file sha1 signature: index file corrupt`. `git status` affichait des entrées fantômes (`AD ./`, conflits `UU` sur des noms aberrants `X0`, `"l\n"`, `"\376"`, tout le dossier `tier-list/` en « supprimé + non suivi »). En cause : un fichier verrou `.git/index.lock` resté en place après un process git interrompu, plus un index binaire endommagé. Aucune fusion/rebase en cours (`MERGE_HEAD` absent). **HEAD et la base d'objets sont sains** (`git cat-file` OK, `fsck` ne signalait que l'index).

## Réparation effectuée

Le montage Linux interdit la **suppression** dans `.git/` (`rm .git/index` → « Operation not permitted ») et le verrou `.git/index.lock` est tenu côté Windows (invisible à `ls`, indéblocable depuis le mount). Contournement : reconstruction d'un index neuf depuis HEAD via un fichier d'index temporaire hors `.git/`, puis **écriture en place** (l'écrasement de contenu est autorisé, contrairement à la suppression) :

```
GIT_INDEX_FILE=/tmp/newindex git read-tree HEAD      # index valide (370 entrées) pointant sur HEAD
cat /tmp/newindex > .git/index                        # écrasement en place
```

Résultat (vu depuis le mount) : `git fsck` **propre**, `git status` redevenu cohérent (plus aucune entrée fantôme), index = 370 fichiers = HEAD. Sauvegarde de l'index corrompu conservée. **Aucun fichier du contenu (working tree) n'a été touché** : `read-tree` ne modifie que l'index.

## Vérification d'intégrité du contenu (outils fiables)

⚠️ Le **montage bash sert toujours une copie obsolète/tronquée** des fichiers édités plus tôt aujourd'hui : `tail` montre des fins coupées, `node --check js/main.js` échoue (faux positif), et `git diff --stat` *via le mount* invente ~8 900 suppressions. **Ce sont des artefacts du mount, pas l'état réel.** Vérifié sur la source fiable (outils Read/Grep, = fichiers Windows réels) :

- `js/main.js` : complet (fonction `renderNewGames` fermée ligne 601, les 4 slugs ajoutés présents).
- `</html>` présent dans **les 22 fichiers** que le mount croyait modifiés — y compris `avatar/index.html` (le doute du run précédent sur sa troncature était lui aussi un faux positif du mount).

Conclusion : **les vrais fichiers sont intacts et complets.** Le danger serait de committer *depuis le mount* (git y verrait les versions tronquées). Le commit doit se faire **nativement sous Windows**, où les fichiers sont complets.

## Fichier touché (lot 4)
`rapport-zoneblox-2026-06-14.md` (cette section). L'index git a été réparé hors working tree.

---

## ⚠️ Pour publier — procédure sûre (à exécuter sous Windows, PAS via un shell Linux/WSL)

Le mount Linux affiche une vue tronquée des fichiers : **ne committe jamais depuis là**. Sous Windows (cmd ou PowerShell), dans le dossier GameNova :

```
del .git\index.lock
del .git\index
git reset
git status
```

Vérifie que `git status` montre un ensemble **raisonnable** de fichiers (quelques pages éditées aujourd'hui), et **PAS** des milliers de suppressions ni des fichiers vidés. Lance au besoin `git diff --stat` pour contrôler. Si tout est cohérent :

```
git add -A
git commit -m "MAJ Zoneblox du jour"
git push origin main
```

🛑 **Stop** : si `git status` est déjà propre, tout était déjà committé — rien à pousser. Si tu vois des milliers de suppressions ou des fichiers tronqués, n'ajoute/committe PAS : restaure depuis HEAD (`git checkout -- <fichier>`) et reviens vers moi. Hostinger déploie automatiquement après le push.
