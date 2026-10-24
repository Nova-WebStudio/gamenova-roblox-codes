# Audit SEO — ZoneBlox.com

**Date :** 24 octobre 2026, mis à jour le même jour avec les exports GSC par motif et l'export GA4 · **Périmètre :** zoneblox.com (site statique HTML, dépôt `GameNova`)
**Méthode :** exports Google Search Console (fichiers), code source local, tests HTTP en ligne le 24/10, exports SE Ranking déjà présents. Lecture seule : aucun fichier du site n'a été modifié.

> **Légende.** **[Fait]** = vérifié dans une donnée ou un test. **[Hypothèse]** = explication plausible, non prouvée. **[Reco]** = recommandation.

---

## 1. Résumé exécutif

1. **Le trafic de recherche Web Google est quasi nul depuis juillet.** [Fait] 73 clics la semaine du 8 juin, 45 la suivante, puis 0 à 4 clics par semaine du 22 juin au 24 septembre (exports GSC du 11/09 et du 27/09).
   - [Fait] GA4 (26/07-23/10) compte pourtant **2 069 utilisateurs « organic »** (73 % du total, soit ~160 par semaine), plus 152 venus d'assistants IA.
   - [Fait, GA4 Source / support, 28 derniers jours] **Bing apporte 67 % des sessions** (1 219 sur 1 831), et ~87 % avec les moteurs qui s'appuient sur son index (Yahoo, DuckDuckGo, Qwant, Ecosia). **Google organique : 2 sessions.**
   - Les 8 pages d'entrée principales (guides Steal an Egg, Slayers 2…) **n'ont jamais été explorées par Google** (§3.4).
2. **Le pic de juin reposait sur une seule page tendance.** [Fait] `guides/vendre-des-citrons.html` a fait 69 + 2 clics (www + apex) sur l'export du 11/09, puis 2 clics sur l'export du 27/09. [Hypothèse] La recherche autour du jeu est retombée.
3. **L'indexation recule pendant que le catalogue grossit.** [Fait] Courbe GSC : 248 pages indexées (15/08), 221 (05/09), 227 (15/09). Pages non indexées : 237 (29/08), puis 427 (15/09). Vos chiffres actuels (183 indexées, 505 non indexées) prolongent cette tendance, mais **aucun export ne les contient**.
4. **Le problème n°1 : Google n'explore pas les pages.** Ce n'est pas un rejet de leur contenu. [Fait, exports du 24/10]
   - **193 pages « Détectée, actuellement non indexée »** : toutes des URL actuelles, en 200, **jamais explorées**. Parmi elles : 95 pages codes (48 % du catalogue codes), 39 guides, 26 tier lists, 26 pages `games/`, ainsi que `meilleurs-jeux-roblox.html` et `nouveaux-jeux-roblox.html`.
   - **46 de ces 95 pages codes sont la cible 301 d'une ancienne URL** que Google a déjà explorée. La migration du 22/07 a remis leur indexation à zéro, et Google n'est pas encore revenu.
   - **102 « Explorée, non indexée »** : 65 sont d'anciennes variantes (www, `/codes/`) qui redirigent, donc sans gravité. Seules **35 URL actuelles** ont été réellement écartées : 24 guides et 11 tier lists, toutes de juin.
   - **24 « Autre canonique » et 8 « Doublon »** : uniquement d'anciennes URL, vues en juin-juillet avant les redirections. Sans gravité.
   - Au total, **227 URL du sitemap sur 432 ne sont pas indexées**.
5. **Défauts techniques confirmés, tous simples à corriger :**
   - H1 au mauvais mois sur 169 pages codes (« septembre » alors que le title dit « octobre ») ;
   - 101 pages codes vérifiées pour la dernière fois en septembre, alors que la page promet une mise à jour quotidienne ;
   - 2 jeux en double (même universeId Roblox) ;
   - 6 hubs sans balise canonical ;
   - liens `href="#"` sur 181 pages ;
   - 2 liens internes en 404 ;
   - SearchAction pointant vers une page 404.
6. **Le frein de fond, c'est l'autorité, pas le volume de pages.** [Fait, source tierce] SE Ranking (27/09) : Domain Trust 1, environ 35 backlinks, 0 mot-clé en page 1. [Reco] Moratoire sur les nouvelles pages ; concentrer l'effort sur les ~150 URL que Google montre déjà.

**Les 5 actions des 30 prochains jours :** (1) faire découvrir les 95 pages codes jamais explorées : liens depuis l'accueil et les pages indexées, demandes d'indexation, et aucun nouveau changement d'URL ; (2) corriger le H1, les canonicals, les liens `#` et les 404 ; (3) consolider les 2 doublons de jeu ; (4) travailler les 9 pages en positions 5-30 ; (5) consolider Bing, la source réelle du trafic : Bing Webmaster Tools et IndexNow.

---

## 2. Phase 1 — Inventaire des sources

| Source | Emplacement | Période / date | Contenu | Limites |
|---|---|---|---|---|
| GSC Performance | `Downloads/zoneblox.com-Performance-on-Search-2026-09-27.zip` | 3 mois, ~25/06 → 24/09 | Graphique quotidien, 192 pages, 528 requêtes, pays, appareils | Requêtes anonymisées : seulement 4 clics attribués à des requêtes sur 24. Pas de croisement requête × page. |
| GSC Performance | `…-2026-09-11.zip` | 3 mois, ~09/06 → 04/09 | Idem | Chevauche fortement l'export du 27/09 : ce n'est pas une période précédente propre. |
| GSC Performance | `…-08-19`, `…-08-24`, `…-08-26` (7 et 28 j) ; `…-06-16` (HTML) | août ; juin | Idem | Périodes courtes. |
| GSC Couverture | `zoneblox.com-Coverage-2026-08-29 / 09-11 / 09-21.zip` | courbe 02/06 → 18/09 | Comptes par motif, courbe indexées / non indexées | **Aucune liste d'URL par motif**, sauf ci-dessous. |
| GSC Drilldown | `zoneblox.com-Coverage-Drilldown-2026-08-29 / 09-21.zip` | → 19/09 | 162 URL « Page avec redirection » | Un seul motif exporté. |
| SE Ranking | `Downloads/export_research_fr_domain_history_eur_2026-09_zoneblox.com.csv` + `opportunites-mots-cles-2026-09-27.md` | sept. 2026 | 51 mots-clés FR, volumes, KD, positions | Estimations tierces ; les URL listées sont encore les anciennes `/codes/…`. |
| DataForSEO | MCP connecté | 24/10 | Testé : **solde 0 $** (3 $ consommés) | Aucun appel payant possible. Un fichier `disavow-zoneblox-2026-10-20.txt` (1 000 domaines) issu d'une collecte antérieure. |
| Code source | `Documents/Claude/Projects/GameNova` (git, 319 commits) | HEAD 24/10 | 445 fichiers HTML, `.htaccess`, `robots.txt`, 8 sitemaps, scripts `tools/` | Le déploiement en ligne correspond au code local (title, H1, date et nombre d'URL du sitemap comparés le 24/10). |
| Audits antérieurs | `analyse-seo-gsc-2026-09-11.md`, `GSC-indexation-plan-2026-09-21.md`, `indexation-priorite-2026-09-14.md`, `SEO-directeur-audit-roadmap-2026-07-24.md`, `AUDIT-SEO-zoneblox-Partie1-6` (juin) | juin → sept. | Diagnostics précédents | Repris uniquement quand ils sont revérifiés ici. |
| Absent | `data/gsc/` n'existe pas | — | — | Pas d'accès API Search Console, pas d'export GA4. PageSpeed API : quota journalier dépassé le 24/10. |

> Je n'ai **pas** accédé à Search Console en direct. Tous les chiffres GSC viennent des fichiers exportés, et le plus récent date du 27/09.

---

## 3. Phase 2 — Performances Google

### 3.1 Tendance (les exports du 11/09 et du 27/09 combinés, par semaine)

| Semaine du | Clics | Impressions |
|---|---|---|
| 08/06 | 73 | 991 |
| 15/06 | 45 | 534 |
| 22/06 | 7 | 102 |
| 06/07 | 2 | 326 |
| 27/07 | 1 | 402 |
| 10/08 | 0 | 378 |
| 24/08 | 1 | 337 |
| 07/09 | 0 | 78 |
| 14/09 | 4 | 79 |
| 21/09 (partielle) | 0 | 22 |

[Fait] Les impressions se maintiennent autour de 200-400 par semaine en juillet-août, puis chutent en septembre (78-79 par semaine). Cette chute coïncide avec le bond des pages non indexées du 05/09 (237 → 398).

**Totaux de l'export du 27/09 (3 mois) :** 24 clics, 2 801 impressions.

| Appareil | Clics | Impressions | Position moy. |
|---|---|---|---|
| Ordinateur | 12 | 2 447 | 49,5 |
| Mobile | 11 | 336 | 12,9 |
| Tablette | 1 | 18 | 8,7 |

- [Fait] **Pays :** la France concentre 19 clics sur 24 (1 153 impressions, position moyenne 40,9). Le Maroc (448 impressions) et l'Algérie (299) produisent 0 et 1 clic.
- [Hypothèse] Les impressions ordinateur en position ~50 correspondent surtout à des requêtes génériques (« code roblox », « roblox code »). Elles ne représentent pas une demande réellement accessible.

### 3.2 Pages (URL consolidées : www, `/codes/x.html` et `codes-x.html` regroupées)

Export 27/09 : 192 lignes de pages, ramenées à **152 URL actuelles**. **34 URL actuelles ont leurs signaux répartis sur 2 à 4 variantes** (exemple : `/codes/mini-guerre.html` + `/codes-mini-guerre.html`). [Fait] La consolidation post-migration n'était donc pas terminée au 24/09.

| Famille | URL vues | Clics | Impressions |
|---|---|---|---|
| tier-list | 41 | 8 | 1 076 |
| hub/accueil | 5 | 2 | 857 (dont accueil 600, pos. 70,5) |
| codes | 78 | 9 | 783 |
| guide | 19 | 4 | 95 |
| games/ (hors Roblox) | 3 | 0 | 11 |

**Pages en positions 5-30 avec au moins 10 impressions** (les seules où un gain rapide est plausible) :

| URL | Impr. | Clics | Pos. pondérée |
|---|---|---|---|
| /codes-mini-guerre.html | 89 | 1 | 7,9 |
| /codes-iron-soul-dungeon.html | 70 | 2 | 6,3 |
| /tier-list/blue-lock-rivals.html | 40 | 1 | 18,6 (84 impr. / 6 clics dans l'export du 11/09) |
| /codes-ugc-limited.html | 38 | 0 | 24,6 |
| /guides/vendre-des-citrons.html | 36 | 2 | 5,2 |
| /codes-build-a-ring-farm.html | 15 | 0 | 11,4 |
| /codes-99-nights-in-the-forest.html | 13 | 0 | 29,6 |
| /codes-evasion-clavier.html | 13 | 0 | 9,8 |
| /guides/grow-a-garden-2.html | 12 | 0 | 5,8 |

**Pages à impressions mais trop loin** (position > 30) : `/tier-list/grand-piece-online.html` (128 impr., pos. 42), `/tier-list/anime-reborn.html` (125, pos. 55, dont 57 impressions sur la requête espagnole « anime reborn objetos »), `/tier-list/anime-adventures.html` (108, pos. 38), `/tier-list/peroxide.html` (90, pos. 37), `/guides.html` (152, pos. 62).

> La position moyenne est une moyenne pondérée par les impressions sur l'ensemble des requêtes. Elle ne correspond pas à une position fixe sur une requête donnée.

### 3.3 Requêtes

- [Fait] 528 requêtes, mais seulement 892 impressions et 4 clics leur sont attribués. Le reste est anonymisé par Google, et les conclusions par requête sont donc **peu fiables**.
- **Signaux utiles :**
  - « code mini guerre » : 47 impressions, position 10,3 ;
  - « construire une ferme d anneaux » : position 10,3 ;
  - « guerriers d'anime iii » : position 10,3 ;
  - « liminalité invisible » : position 10 ;
  - « unseen liminality update » : position 9,3.
- [Fait] Les requêtes têtes (« code roblox » 17 impressions en position 67, « roblox code », « codes robux ») sont en positions 60-90. Le CLAUDE.md interdit déjà de les cibler, et les données confirment ce choix.
- **Cannibalisation :** l'export ne croise pas requêtes et pages, donc on ne peut pas la prouver requête par requête. Elle est en revanche **certaine au niveau des URL** pour les deux paires de jeux en double (§4.4) et pour les variantes ancien/nouveau schéma.

Détail complet : `GSC-PERFORMANCE-ANALYSIS.csv`.

### 3.4 GA4 — d'où viennent les visiteurs

**a) Premier support de l'utilisateur, 26/07 → 23/10 (export CSV)**

| Premier support | Utilisateurs | Durée d'engagement moy. |
|---|---|---|
| organic | 2 069 | 28 s |
| referral | 370 | 24 s |
| (none) | 225 | 27 s |
| ai-assistant | 152 | 37 s |

**b) Source / support de la session, 28 derniers jours (26/09 → 23/10), lu dans GA4 via Chrome le 24/10**

| Source / support | Sessions | % | Taux d'engagement |
|---|---|---|---|
| **bing / organic** | **1 219** | **66,6 %** | 60 % |
| fr.search.yahoo.com / referral | 205 | 11,2 % | 61 % |
| (direct) / (none) | 142 | 7,8 % | 34 % |
| duckduckgo / organic | 75 | 4,1 % | 41 % |
| chatgpt.com / ai-assistant | 61 | 3,3 % | 54 % (40 s) |
| ecosia.org / organic | 53 | 2,9 % | 45 % |
| qwant.com / organic | 26 | 1,4 % | 58 % |
| tiktok.com / referral | 11 | 0,6 % | 0 % |
| yahoo / organic | 9 | 0,5 % | 56 % |
| **google / organic** | **2** | **0,1 %** | — |
| **Total** | **1 831** | | 56 % |

- [Fait] **Le trafic de ZoneBlox vient de Bing**, pas de Google. Bing direct fait 1 219 sessions. En ajoutant les moteurs qui s'appuient sur l'index Bing (Yahoo 214, DuckDuckGo 75, Qwant 26, et Ecosia 53, qui utilise en partie Bing), on arrive à **≈ 1 587 sessions sur 1 831, soit ~87 %**. [Fait externe] Yahoo, DuckDuckGo et Qwant affichent en grande partie des résultats Bing.
- [Fait] Google organique : **2 sessions en 28 jours**. C'est cohérent avec Search Console.
- [Fait] ChatGPT : 61 sessions, avec l'engagement le plus long (40 s).

**c) Pages de destination, 28 derniers jours**

| Page | Sessions | Statut Google (export du 24/10) |
|---|---|---|
| /guides/steal-an-egg-mutations.html | 255 | **jamais explorée** |
| /guides/slayers-2.html | 223 | **jamais explorée** |
| /guides/steal-an-egg.html | 211 | **jamais explorée** |
| /games/aniimo/guides/heritage-inherit | 65 | **jamais explorée** |
| /guides/ride-a-pet.html | 49 | **jamais explorée** |
| /codes-search-for-the-needle.html | 44 | **jamais explorée** |
| /guides/1-loot-to-forge.html | 40 | **jamais explorée** |
| /tier-list/blox-fruits-races.html | 39 | **jamais explorée** |
| /codes-anime-rng.html | 38 | indexée (vérification > 24 jours) |

- [Fait] **Les 8 premières pages d'entrée n'ont jamais été explorées par Google.** Bing les classe et y envoie des visiteurs : la demande et le contenu sont donc réels. Pour Google, le blocage vient de la découverte et du crawl, pas de la qualité. Cela confirme le diagnostic du §4.3.
- [Fait] Ces pages ont été créées entre le 28/08 et le 22/09, sur des jeux tendance (Steal an Egg, Slayers 2, Ride a Pet). Bing indexe vite les nouveautés, alors que Google n'est pas encore passé.
- [Fait] La famille la plus rentable aujourd'hui est celle des **guides**, alors que 71 % d'entre eux ne sont pas indexés par Google.
- [Fait] Aucun événement clé n'est configuré : aucune conversion n'est mesurée.

---

## 4. Phase 3 — Diagnostic des pages non indexées

### 4.1 Motifs exportés le 24/10/2026

Source : 4 exports « Coverage-Drilldown-2026-10-24 » (courbes jusqu'au 16/10). Chaque URL a été testée en ligne le 24/10.

| Motif | Pages | URL listées | Nature des URL | Statut en ligne | Verdict |
|---|---|---|---|---|---|
| **Détectée, actuellement non indexée** | 193 | 193 | **193 URL actuelles**, dernière exploration vide (jamais explorées) | 193 en 200 direct | **Problème n°1** : demande de crawl insuffisante, pas un jugement de qualité |
| **Explorée, actuellement non indexée** | 102 | 102 | 65 anciennes variantes (www, `/codes/`), 35 URL actuelles, `sitemap.xml` ×2 | 37 en 200 direct, 65 redirigées vers 200 | 65 sans gravité. **35 vraiment écartées** (24 guides, 11 tier lists) |
| Autre page avec balise canonique correcte | 24 | 24 | Uniquement `www.zoneblox.com/…`, explorées les 11-13/06 | 24 redirigées vers 200 | Sans gravité (vue antérieure à la redirection www) |
| Page en double : Google n'a pas choisi la même canonique | 8 | 8 | Uniquement `zoneblox.com/codes/…`, explorées 18/06-16/07 | 8 redirigées vers 200 | Sans gravité (ancien schéma) |
| *Non exporté le 24/10* | ≈ 178 | — | Probablement « Page avec redirection » (162 au 21/09) et motifs mineurs | — | À confirmer avec l'export manquant |

**Évolution** (courbes des exports) :
- « Détectée » : 146 (05/09), 174 (15/09), 192 (22/09), 193 (05/10), puis stable.
- « Explorée » : 36-42 en août, 49 (05/09), 90 (22/09), 102 (13/10).
- « Doublon » : en baisse, de 23 (18/08) à 8 (05/10). Les anciennes URL se résorbent.

**Absents des exports :** noindex, 404, robots.txt, soft 404. [Fait] Aucun `noindex` dans les pages du sitemap.

### 4.2 Statut réel des 432 URL du sitemap

Croisement entre les 4 listes exportées, les impressions GSC sur 3 mois et l'inventaire du code. Détail URL par URL : `INDEXATION-ANALYSIS.csv`.

| Famille | URL | Jamais explorée | Explorée, écartée | Indexée (impressions) | Probablement indexée* | **% non indexé** |
|---|---|---|---|---|---|---|
| codes | 196 | 95 | 0 | 67 | 34 | **48 %** |
| guides | 89 | 39 | 24 | 6 | 20 | **71 %** |
| tier-list | 83 | 26 | 11 | 38 | 8 | **45 %** |
| games/ (hors Roblox) | 51 | 26 | 0 | 3 | 22 | **51 %** |
| hubs / autres | 13 | 6 | 0 | 6 | 0 | 46 % |
| **Total** | **432** | **192** (+ `/embed/`) | **35** | **120** | **84** | **53 %** |

\* Absente des 4 listes d'exclusion et sans impression. Ce total (204) concorde avec vos 183 indexées, à environ 20 pages récentes près, pas encore connues de Google.

### 4.3 Pourquoi Google n'explore pas : ce que montrent les données

- [Fait] **La migration du 22/07 a remis l'indexation à zéro pour une partie des pages codes.** 46 des 95 pages codes jamais explorées sont la cible 301 d'une ancienne URL que Google a explorée. Exemples : `codes-pressure.html` et `codes-fish-it.html` ont eu des impressions sur leur ancienne adresse `/codes/…`, alors que la nouvelle URL n'a jamais été explorée. Google a enregistré la redirection mais n'est pas allé chercher la cible.
- [Fait] **Le maillage interne est corrélé à l'exploration.** Pages codes avec ≤ 2 liens statiques entrants : 63 % « jamais explorées » (48/76), contre 39 % (47/120) avec 3 liens ou plus. Pages codes liées depuis l'accueil : 23 % jamais explorées (5/22), contre 52 % (90/174) pour les autres.
  - Les pages jamais explorées ont une médiane de 2 liens entrants, contre 4 pour les pages indexées.
  - Leurs principales sources de liens sont `tous-les-codes.html` et `games/`.
- [Fait] **La similarité de gabarit n'explique pas la non-exploration.** Les pages codes jamais explorées sont *moins* semblables à leur voisine (médiane 0,22) que les pages indexées (0,31). Google ne les a de toute façon pas lues.
- [Hypothèse] **La cause de fond est la faible demande de crawl d'un domaine sans autorité** (Domain Trust 1, ~35 backlinks), face à 432 URL déclarées et à plusieurs vagues d'ajouts. Le maillage aide à répartir ce que Google accepte d'explorer, mais ne remplace pas l'autorité.
- [Fait] **Les « écartées » sont des guides et tier lists de juin**, souvent sur les plus gros jeux : guides `blox-fruits` (2 205 mots), `grow-a-garden`, `steal-a-brainrot`, `fisch`, `blade-ball`, `king-legacy`. Deux tier lists qui avaient des impressions sont passées en « Explorée, non indexée » : `spongebob-tower-defense` (26 impr.) et `blade-ball` (20 impr.).
  - [Hypothèse] Sur ces sujets très concurrentiels, Google ne voit pas assez de valeur ajoutée face aux sites établis. Les guides de juin n'ont pas été mis à jour depuis.
- [Fait] Les deux hubs éditoriaux `meilleurs-jeux-roblox.html` et `nouveaux-jeux-roblox.html`, ainsi que `guide-utiliser-codes-roblox.html`, n'ont jamais été explorés.

### 4.4 Causes techniques vérifiées dans le code

- [Fait] **Doublons de jeu** : même universeId dans `ROBLOX_UNIVERSE_IDS` (`js/main.js`), deux pages en 200, toutes deux dans le sitemap.
  - `codes-demonology.html` et `codes-demonologie.html` (6170143659) ;
  - `codes-build-a-ring-farm.html` et `codes-ferme-d-anneaux.html` (10039338037).
  - Le cas `mini-war` → `mini-guerre` a déjà été traité en 301 : c'est le modèle à reproduire.
- [Fait] **Hubs sans canonical** : `tous-les-codes.html`, `guides.html`, `tier-lists.html`, `avatars.html`, `ugc-gratuits.html`, `guide-utiliser-codes-roblox.html`. `tous-les-codes.html?cat=rpg` répond 200 et apparaît dans GSC (11 impressions).
- [Fait] **Pages hors schéma** :
  - `tier-list-blox-fruits.html` : 200, hors sitemap, 0 lien entrant, doublon de `/tier-list/blox-fruits.html` ;
  - `tier-list-anime-expeditions.html` et `guide-anime-expeditions.html` : à la racine, dans le sitemap.
- [Fait] **Orphelines** : `guides/clean-the-supermarket.html` et `guides/drain-the-lake.html` n'ont aucun lien statique entrant.
- [Fait] Le sitemap est cohérent avec les fichiers (aucune URL redirigée ni inexistante), sauf `/embed/` (page widget, sans intérêt pour la recherche).

**Ce qu'il ne faut pas faire sans données :** désindexer, fusionner ou supprimer des pages des familles `games/`, guides ou codes vides. Chaque décision doit partir de l'export par motif et de l'inspection d'URL (fonction de la page, liens, impressions).

---

## 5. Phase 4 — Audit technique et architecture

### 5.1 Contrôles (sur 432 URL du sitemap, sauf mention contraire)

| Contrôle | Résultat | Preuve |
|---|---|---|
| Codes HTTP | OK : home, pages codes et sitemaps en 200 ; www → apex en 301 ; 404 réel sur URL inconnue | curl 24/10 |
| Liens internes cassés | **2 cassés** : `/games/bike-universe/updates/` et `/games/dont-splash/updates/` (404), liés depuis `/actualites/` | curl 24/10 |
| Liens placeholder | **169 pages** : lien sidebar « 📖 Guide débutant — Bien démarrer » en `href="#"`. **12 pages** (dont les 3 hubs) : footer « Jeux populaires » en `href="#"` | regex sur `<a href="#">` |
| Title | 0 doublon, 0 manquant ; 4 > 65 caractères | inventaire |
| Meta description | 0 doublon, 0 manquante ; 16 > 160 caractères ; 20 < 70 caractères | inventaire |
| H1 | 1 H1 par page partout. **169/196 pages codes : mois du H1 ≠ mois du title** | ex. `codes-blox-fruits.html` : title « (octobre 2026) », H1 « — septembre 2026 » (en ligne) |
| Canonical | Auto-référente partout, **sauf 6 hubs sans balise** | §4.4 |
| Robots / noindex | Aucun noindex dans le sitemap ; `robots.txt` avec Allow + 2 sitemaps | fichiers |
| Sitemaps | `sitemap.xml` (411) + `sitemap-games.xml` (52, dont `/embed/`) = 432 URL distinctes. 5 sous-sitemaps non déclarés et `sitemap-en.xml` vide toujours servis | fichiers |
| Redirections | 173 règles `Redirect` par jeu + règle générique de réécriture. 35 doubles sauts possibles (www + ancien schéma) | `.htaccess`, curl |
| Profondeur | Accueil → `tous-les-codes.html` (196 liens statiques vers chaque page codes) → page codes = 2 clics. L'accueil lie directement 24 pages codes en statique | inventaire |
| Rendu HTML | Les codes, les « jeux similaires » et le hub sont en HTML statique : crawlables sans JS | lecture du HTML |
| Données structurées | Pages codes : WebPage, BreadcrumbList, FAQPage (196/196), ItemList (141/196). Guides : Article (89/89). **SearchAction de l'accueil vers `/recherche?q=` → 404** | regex, curl |
| Résultats enrichis | Aucun dans GSC (« Apparence » vide). [Fait externe] Depuis 2023, Google n'affiche les FAQ en résultats enrichis que pour des sites gouvernementaux ou de santé : il ne faut rien en attendre | export GSC |
| Performance / mobile | **Non mesurée** (quota PageSpeed API dépassé le 24/10, pas de données CrUX exportées). AdSense est chargé dans le `<head>` de chaque page ; son effet sur le LCP n'est pas mesuré | — |

### 5.2 Fraîcheur affichée

- [Fait] Dates « 🔄 Vérifié le » : 101/195 pages codes sont en septembre (dont 26 au 7 septembre). Seules 94 sont en octobre.
- L'intro de chaque page dit « vérifiés à la main et mis à jour chaque jour ». C'est faux pour la moitié des pages.
- C'est un problème de confiance (EEAT) avant d'être un problème de classement.

---

## 6. Phase 5 — Contenu et intentions

| Famille | Nb | Intention | Valeur joueur | Différenciation (similarité max., médiane) | Constats | Opportunité |
|---|---|---|---|---|---|---|
| **Codes** (`codes-*.html`) | 196 | Transactionnelle : « codes <jeu> » | Forte quand il y a des codes (médiane : 3 codes actifs) | **0,28** (max 0,48) : gabarit dominant | 53 pages à 0 code actif ; FR/EN en double sur 2 jeux ; 45 ne lient pas leur tier list | Contenu propre au jeu sur les pages qui ont des impressions ; pages honnêtes « pas de code » orientées récompenses ; consolidation des doublons |
| **Tier lists** | 83 | Informationnelle / classement | Moyenne à forte | 0,07 | Meilleur réservoir d'impressions (1 076 en 3 mois) mais positions 35-55 | Mise à jour méta + liens depuis les pages codes |
| **Guides** | 89 | Informationnelle / how-to | Variable (375 à 2 739 mots) | 0,06 | 70/89 sans impression ; 1 succès lié à une tendance passée | Ne pas en créer ; relier et rafraîchir les jeux encore populaires |
| **Hubs** | 6 | Navigation | Forte (porte d'entrée) | — | Pas de canonical ; footer en `#` | Correctifs techniques |
| **games/** (Aniimo, GTA 6, FC 27, The Hollow…) | 51 | Actualités / guides hors Roblox | Hors cœur de cible | médiane 484 mots | 48/51 sans impression ; 2 liens 404 | Gel des créations ; réévaluation avec les données |
| **Autres** (avatar/, musique/, ugc) | 6 | Divers | — | — | `avatar/` et `musique/` hors sitemap (`musique/` vue dans GSC, 3 impressions) | Décider s'ils restent dans le sitemap |

**Cannibalisation :**
- [Fait] Paires de jeux en double (§4.4).
- [Hypothèse] Pour certains jeux, la page codes et la tier list peuvent concourir sur « <jeu> » seul. Exemple : « pet simulator 99 » fait ranker la tier list (SE Ranking, pos. 54-62). À vérifier dans GSC avec un filtre par requête.

**Ce que je ne recommande pas :** créer de nouvelles pages pour augmenter le nombre d'URL. L'historique montre que chaque vague d'ajouts (13/06, 25/07, 15/08, 05/09) fait grimper les non indexées sans faire monter les indexées.

---

## 7. Phase 6 — Concurrence et DataForSEO

- [Fait] Le MCP DataForSEO répond, mais le **solde du compte est de 0 $**. Je n'ai lancé aucun appel payant.
- **Données réutilisées :** SE Ranking (FR, sept. 2026, 51 mots-clés). Ce sont des **estimations de volume**, à ne pas confondre avec les données réelles de Search Console. Exemples :
  - « mugetsu » 480/mois, KD 10, pos. 45 ;
  - « pet simulator 99 » 590, KD 24, pos. 62 ;
  - « codes arsenal » 210, KD 9, pos. 63 ;
  - « code roblox » 5 400, KD 92, pos. 89.

**Plan de collecte minimal, quand le crédit sera rechargé** (ordres de grandeur à confirmer sur la grille DataForSEO avant lancement) :

| Étape | API | Échantillon | Coût estimé |
|---|---|---|---|
| 1 | SERP Google Organic (FR, mobile), mode standard | 15 requêtes : les 9 pages en 5-30 + 6 tier lists à impressions | ≈ 0,01-0,03 $ |
| 2 | Keywords Data — volumes Google Ads FR | 1 tâche, ≤ 100 mots-clés (noms FR et EN des jeux du catalogue ayant des impressions) | ≈ 0,05-0,10 $ |
| 3 | Labs — domaines concurrents / mots-clés classés | 1-2 tâches (zoneblox.com + 1 concurrent FR identifié à l'étape 1) | ≈ 0,05-0,20 $ |
| 4 | Backlinks — résumé seulement | Uniquement si l'étape 3 montre un écart d'autorité à documenter | ≈ 0,02-0,05 $ |

Élargir uniquement si l'étape 1 révèle des SERP gagnables (concurrents peu autoritaires, contenus datés).

---

## 8. Phase 7 — Plan d'action priorisé

Backlog complet (24 lignes, avec preuve, cause, confiance, impact, difficulté, validation) : **`SEO-PRIORITIES.csv`**. Les identifiants ci-dessous renvoient à ce fichier.

### 8.1 Corrections techniques urgentes

| ID | Problème | Preuve | Action | Validation | Prio |
|---|---|---|---|---|---|
| T1 | H1 au mauvais mois (169 pages) | title octobre / H1 septembre | Étendre `tools/sync_month.py` au H1 | 0 écart title/H1 | P1 |
| T2 | « Mis à jour chaque jour » faux sur 101 pages | dates verifDate | Tenir la rotation ou reformuler l'intro | 0 page > 14 jours | P1 |
| T3 | 2 jeux en double | même universeId | Garder 1 URL par jeu, 301 de l'autre (après inspection GSC) | curl 301 + GSC | P1 |
| T4 | 2 liens 404 | curl | Retirer ou générer les pages | curl | P1 |
| T5 | 6 hubs sans canonical, `?cat=` indexé | grep, GSC | Canonical auto-référente | Inspection d'URL | P1 |
| T6 | SearchAction → 404 | curl | Retirer le bloc ou le corriger | Test résultats enrichis | P2 |
| T7-T9 | Pages hors schéma, `/embed/` dans le sitemap, doubles sauts | voir CSV | Nettoyage | curl / GSC | P2-P3 |

### 8.2 Améliorations des pages existantes

| ID | Problème | Action | Prio |
|---|---|---|---|
| E1 | 9 pages en positions 5-30 | Title/meta sur le nom FR réellement tapé, maillage, contenu spécifique | P1 |
| E2 | 53 pages codes à 0 code | Décision au cas par cas (page « récompenses » honnête, ou consolidation vers le guide) ; pas de suppression d'office | P2 |
| E3 | Gabarit codes répétitif (n'explique pas la non-indexation, cf. §4.3) | Contenu propre au jeu, en commençant par les 67 pages codes indexées | P3 |
| E4 | Tier lists en positions 37-55 | Mise à jour méta + liens | P2 |
| E5 | Guides invisibles | Relier et rafraîchir ; aucun nouveau guide | P3 |

### 8.3 Maillage interne et architecture (détail : `INTERNAL-LINKING-PLAN.csv`)

| ID | Problème | Action | Prio |
|---|---|---|---|
| M1 | 45 pages codes ne lient pas leur tier list | Bouton dans le bandeau `data-cta="guidelink"` | P1 |
| M2 | 181 pages avec `href="#"` | Vrais liens (guide d'utilisation des codes, pages codes populaires) | P1 |
| M3 | 76 pages codes avec ≤ 2 liens entrants | Liens contextuels par catégorie | P2 |
| M4 | 2 guides orphelins | Liens depuis `guides.html` | P3 |

### 8.4 Croissance organique

| ID | Sujet | Action | Prio |
|---|---|---|---|
| D1 | ✅ Résolu : le trafic vient de Bing (67 % des sessions, ~87 % avec les moteurs adossés), Google 2 sessions | — | fait |
| C6 | Bing = canal principal, non outillé | Bing Webmaster Tools + sitemap ; IndexNow à chaque run quotidien | **P1** |
| C7 | 8 pages à forte demande (Bing) jamais explorées par Google | Demandes d'indexation prioritaires + ajout au bloc de découverte de l'accueil | **P1** |
| D0 | Exports restants | Motif « Page avec redirection » du 24/10 ; Performance après le 24/09 | P0 |
| C5 | 95 pages codes jamais explorées (46 = cibles 301) | Liens depuis l'accueil et les pages indexées ; demandes d'indexation (10-15/jour) ; plus aucun changement d'URL | **P1** |
| C3 | Indexation en recul | Moratoire sur la création de pages | P1 |
| E6 | 24 guides + 11 tier lists explorés puis écartés | Mise à jour substantielle ou fusion, au cas par cas | P2 |
| C1 | Autorité | Liens éditoriaux réels (widget embed, communautés FR) ; désaveu non prioritaire | P2 |
| C2 | Verticale games/ | Gel, puis réévaluation avec les données | P2 |
| C4 | Requêtes FR | Noms FR dans title/H1 ; valider avec DataForSEO quand le crédit sera rechargé | P3 |

---

## 9. Plan sur 30 jours

Aucun résultat d'indexation ni de trafic n'est garanti. Chaque semaine se termine par un relevé GSC.

**Semaine 1 — Découverte et correctifs sûrs**
- Après votre validation : T1 (H1), T4 (404), T5 (canonicals), M2 (`href="#"`), T6 (SearchAction). Tous sont réversibles et sans risque de contenu.
- C5 : bloc de liens statiques vers les pages codes jamais explorées, depuis l'accueil et des pages indexées du même genre. La liste est dans `INTERNAL-LINKING-PLAN.csv` (type « découverte crawl »).
- Peter : demandes d'indexation (10-15/jour) sur les cibles 301 jamais explorées qui avaient des impressions (`codes-pressure`, `codes-fish-it`, `codes-1-aura-per-click`…), puis sur les hubs `meilleurs-jeux-roblox.html` et `nouveaux-jeux-roblox.html`. Exporter GA4 avec Source / support.
- Relevé de référence au 24/10 : Détectée 193, Explorée 102 (dont 35 URL actuelles), Autre canonique 24, Doublon 8.

**Semaine 2 — Consolidation**
- Décider des 2 consolidations de jeux (T3) après inspection d'URL. Appliquer les 301.
- M1 : ajouter les liens codes → tier list (45 pages).
- E6 : trier les 35 guides et tier lists écartés entre « mettre à jour » et « fusionner », avec votre validation.

**Semaine 3 — Pages à potentiel**
- E1 : retravailler les 9 pages en positions 5-30 (title, meta, intro spécifique, 2-3 liens entrants chacune).
- T2 : rattraper la vérification des pages qui ont des impressions, ou reformuler la promesse.
- Demandes d'indexation manuelles uniquement pour les pages corrigées (10-15).

**Semaine 4 — Mesure et arbitrage**
- Comparer à la semaine 1 : pages indexées, motifs, positions des 9 pages.
- Décider du sort des 53 pages sans code et de la verticale `games/` selon les données.
- Si le crédit DataForSEO est rechargé : étapes 1-2 du §7 (≈ 0,15 $ maximum).

---

## 10. Limites des données

- **505 non indexées** : les 4 motifs exportés le 24/10 couvrent 327 pages. Les ≈ 178 restantes (probablement « Page avec redirection » et motifs mineurs) n'ont pas été exportées à cette date. La liste « Page avec redirection » utilisée date du 21/09.
- **Statut « probablement indexée »** : déduit par absence des 4 listes, et non confirmé page par page (l'inspection d'URL fait foi).
- **Cause de la non-exploration** : la corrélation avec le maillage est mesurée ; la causalité, et le rôle de l'autorité, restent des hypothèses.
- **Période de comparaison** : les exports de 3 mois du 11/09 et du 27/09 se chevauchent (~09/06-04/09 contre ~25/06-24/09). La comparaison se fait par semaine, pas période contre période. Aucune donnée GSC après le 24/09.
- **Requêtes** : 4 clics sur 24 sont attribués à une requête. Les conclusions par requête sont indicatives.
- **Croisement requête × page** : absent, donc la cannibalisation n'est prouvable qu'au niveau des URL.
- **GA4** : la source détaillée a été lue sur 28 jours seulement (26/09-23/10), à l'écran et sans export. Le premier support porte sur 90 jours. Aucun événement clé n'est configuré.
- **Bing** : aucune donnée Bing Webmaster Tools (requêtes, positions, pages indexées) n'a été consultée.
- **Performance / Core Web Vitals** : non mesurés (quota PageSpeed dépassé, pas de CrUX).
- **Liens entrants internes** : je n'ai compté que les liens HTML statiques. Les liens injectés par JavaScript (`GAMES_INDEX`) ne sont pas comptés.
- **Similarité de contenu** : indicateur local (Jaccard sur 5-grammes du `<main>`). Ce n'est pas un critère publié par Google.
- **Backlinks / autorité** : données SE Ranking du 27/09 et liste de désaveu du 20/10 (DataForSEO). Pas de mesure fraîche (crédit à 0 $).
- **Déploiement** : la correspondance local = en ligne est vérifiée sur un échantillon (home, une page codes, sitemaps), pas page par page.

---

## Fichiers livrés (`audit-seo-2026-10-24/`)

| Fichier | Contenu |
|---|---|
| `AUDIT-SEO-ZONEBLOX.md` | Ce rapport |
| `GSC-PERFORMANCE-ANALYSIS.csv` | 152 pages consolidées (variantes, clics, impressions, position pondérée, segment, opportunité) + requêtes ≥ 3 impressions |
| `INDEXATION-ANALYSIS.csv` | 703 lignes : motif GSC réel (exports du 24/10) pour chaque URL, 162 redirections (21/09) et 97 anciennes variantes testées en ligne, signaux de risque, statut et action |
| `SEO-PRIORITIES.csv` | Backlog de 28 actions (problème, preuve, cause, confiance, impact, difficulté, action, validation, priorité) |
| `INTERNAL-LINKING-PLAN.csv` | 104 recommandations de liens (découverte des pages codes jamais explorées, cluster codes → tier list, pages à potentiel, liens cassés, `href="#"`, orphelines) |

CSV en UTF-8 avec BOM, séparateur `;` (ouverture directe dans Excel FR).

> ⚠️ Ce dossier se trouve dans le dépôt du site. S'il est poussé, il sera publié sur zoneblox.com. Ajoutez `audit-seo-2026-10-24/` au `.gitignore` ou déplacez-le avant le prochain `git push`.
