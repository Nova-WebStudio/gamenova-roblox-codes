# Rapport Zoneblox — 20 septembre 2026 (dimanche)

Run quotidien automatisé. Priorité absolue tenue : vérification des **codes** (hotGames + rotation) avant tout le reste. Pas de lundi → pas de MAJ « Jeu de la semaine ».

---

## (a) CODES VÉRIFIÉS — priorité absolue

### hotGames (15 vérifiés, 5 modifiés)

**Modifiés (corrections réelles / faux-actifs) :**
| Jeu | Avant → Après | Détail & sources |
|-----|---------------|------------------|
| **steal-a-brainrot** | 1 → 0 | BESTBRAINROTEVER périmé → expiré. Pocket Tactics (1er sept.) + GamesRadar/PCGamesN : « aucun code actif ». |
| **merge-a-nuke** | 3 → 2 | UPDATE2 & ATOMIC périmés → expirés ; **+DELAY** (300 déchets nucléaires). Pocket Tactics 16 sept. |
| **defend-ur-base-with-anime** | 5 → 8 | Nos 5 (JJKUPDATE, NEWMUTATIONS, BURAH, SRYFORSHUTDOWN!, CRAFTNERF!) périmés → expirés ; rebâtie sur les 8 actifs Beebom (1er sept.) : UPDATE11, BLUE, GOALKEEPER, UPDATE10, DIOBOSS, TRAVELLINGMERCHANT, LUCKYSPINS, FLEXAVATARS. |
| **vv-ultimatum** | 1 → 6 | +BANKAIONTHEWAY, SEP11TH, GOODMORNING, SORRY4DELAY, LINI_MOZZARELLA (UPD2 conservé). Pocket Tactics 18 sept. + aggregat concordants. 160KLIKES/35ROLLS **laissés en expiré** (déjà expirés côté tracker, prudence). |
| **run-a-restaurant** | 1 → 2 | +FISHIES (MAJ Fishing), RAR4EVER conservé. Sources datées 20 sept. (pcgamesn/dexerto/pockettactics). |

**Confirmés stables (« 🔄 Vérifié le » rafraîchi au 20 sept.) :** grow-a-garden (2 exacts, BlueStacks), tower-defense-simulator (2 — CHRISTMAS2025 en attente sur 1 source), world-fighters (24), brainrot-evolution (24/88 — sous-listage OK), noob-incremental (11), fifa-super-soccer (WorldCupSecret ; bestfootball/fifasupersoccer écartés — doute), hypershot (ONEBILLING conservé ; NEWUPDATE candidat 1 source), spin-a-soccer-card (0 — STAR-STORM PT 7 sept. source unique 13j sur code hebdo → non publié), animal-hospital (0 = jeu sans système de codes, confirmé).

### Rotation quotidienne — ÉTAPE 2ter (18 slugs traités)

**Modifiés (corrections réelles) :**
| Jeu | Avant → Après | Détail & sources |
|-----|---------------|------------------|
| **anime-expeditions** | 10 → 7 | **Correction MAJEURE** : nos 10 « actifs » TOUS périmés (Pocket Tactics 15 sept. les liste en expirés) → 7 actifs : restartsorry!, fastrestart!, Eclipse, 250klikes, 8thCompany, SummerSiege, LighthingGod. |
| **basketball-zero** | 4 → 2 | Nos IZURE/15IZURE/TATLISV2/15TATLISV2 périmés (Pocket Tactics 19 sept.) → SCARYMONSTER + 15SCARYMONSTER. |
| **anime-defenders** | 0 → 12 | Page vide alors que 12 actifs (Pocket Tactics + aggregat concordants) : REDONE, ELEMENTS, SKILLTREES, incredibilli, MEMBEREREBREWRERES, subcool, sub2×6. |

**Confirmés OK (« Vérifié le » au 20 sept., sous-listage acceptable) :** sakura-stand (RTZREWORK/JOJOMONTH), dandys-world (ICHOR), a-dusty-trip (3 exacts), arm-wrestle-simulator (Celebration + brainrot), arsenal (subset de 15, codes permanents), bubble-gum-simulator-infinity (throwback/ogbgs confirmés), dragon-adventures (SeasonXP confirmé), **jailbreak** (YoutubeHelloItsVG + YoutubeNoobFreak — confirmés PT 18 sept. ; l'aggregat listant 8billion/apr26 était trompeur, ceux-ci sont expirés), bee-swarm-simulator (codes permanents), build-a-boat-for-treasure (codes permanents), shindo-life (batch UPD 249 courant).

**À revérifier (source unique / ambiguë — non modifiés) :**
- **toilet-tower-defense** : collision de nom (les sources renvoient surtout « Toilet **Verse** Tower Defense », jeu différent) → 0 code conservé, pas de liste propre pour le TTD original.
- **fish-it** : conflit — Pocket Tactics (2 sept.) liste DIVING actif mais notre tracker l'a déjà expiré ; codes à expiration rapide + source 18j → prudence, 0 code conservé.
- **type-soul** : PALACEUPDATE2060 / Cristi2026 = source unique, codes très volatils → non publiés.
- **da-hood** : nos DOG/SHARK absents des listes actives courantes (WORLDCUP26/BOSS/PRESIDENT cités) mais pas de preuve d'expiration propre → non modifiés.

**Candidats « en attente » enregistrés** dans `tools/code-watch.json` (`_pending2026-09-20`) : TDS CHRISTMAS2025, World Fighters 25kLIKE, Hypershot NEWUPDATE, Spin a Soccer Card STAR-STORM, Arm Wrestle permamining/dropthatnuke/goodbyemining/axel.

`catalogVerify` mis à jour (14 slugs traités OK) ; les 4 « à revérifier » laissés absents exprès. `lastRun` mis à jour.

---

## (b) DIRECTEUR SEO (ÉTAPE 2bis)

**Trending re-scanné** (rblxdb / games.gg, 16–20 sept.) : #1 Steal An Egg (~1,7M CCU) ; leaders (Blox Fruits, Rivals, Jujutsu Shenanigans, Steal a Brainrot, Grow a Garden, Plants vs Brainrots) **tous couverts**. Aucun nouveau hit ≥4000 non couvert.

**Brique réalisée = clôture du cluster « Plants vs Brainrots »** (codes ✓ · tier ✓ · **guide ✗ → ✓**). PvB est un des plus gros cartons de sept. 2026 (croissance ×2 plusieurs semaines, ~916K CCU, 3ᵉ le plus joué) mais orphelin de guide.
- Création de **`guides/plants-vs-brainrots.html`** (~1 484 mots FR) : découverte, boucle planter-défendre-encaisser, meilleures plantes (Cactus/Sunflower/Dragon Fruit/Strawberry ; top-tier Shroombino/Tomatrio/Commando Apple/King Limone), Brainrots en revenu passif, Fusion/Rebirth/Mutations (Gold ×2, Diamond ×3, Frozen ×4, Neon ×4,5), réglages Auto-Sell & Equip Best, 6 astuces, FAQ 4 Q.
- **Intention how-to** distincte des codes (transactionnel) et de la tier list (classement) → **aucune cannibalisation**.
- **Sources ≥2 datées** : games.gg/gam3s.gg (guide débutant & « how to make money fast ») + Plants vs Brainrots Wiki (Fandom, Mechanics) + Sportskeeda. Aucune valeur inventée ; note d'évolutivité + renvoi wiki/Discord officiels.
- **EEAT** : byline « L'équipe Zoneblox » + politique éditoriale. **Schema** Article + BreadcrumbList + FAQPage.
- **Maillage (anti-orphelin)** : vraie miniature tr.rbxcdn.com (réutilisée), carte hub `guides.html`, `<url>` `sitemap.xml`, **liens croisés codes ↔ tier ↔ guide** (guide→codes+tier ; codes→guide+tier ; tier→guide).

**Prochaine brique (J34)** inscrite dans la roadmap : (1) 2 vidéos oEmbed vérifiées sur les guides PvB/SFTN dès que l'accès oEmbed est disponible ; (2) guide pour un autre top hit sans guide ; (3) bandeau `data-cta="guidelink"` sur `codes-plants-vs-brainrots.html` (template ancien) ; (4) enrichir Aniimo.

---

## (c) Jeux ajoutés / guides / tier lists / Aniimo / UGC / Jeu de la semaine

- **Jeux ajoutés** : aucun (aucun nouveau hit ≥4000 non couvert ce run).
- **Guides** : +1 → `guides/plants-vs-brainrots.html` (voir b).
- **Tier lists** : aucune création (cluster PvB déjà pourvu).
- **Aniimo** : pas de nouvelle info vérifiable ≥2 sources ce run ; la régénération a (re)généré la fiche guide `heritage-inherit` depuis les données existantes (valide, dans les sitemaps, liée au hub).
- **UGC** : pas de changement nécessaire.
- **Jeu de la semaine** : non (dimanche).

---

## (d) Régénération automatique (ÉTAPE 7bis)

- `build_site.py` ✅ (pages /games/ + Aniimo régénérées ; sitemap-games.xml : 39 URLs)
- `build_home.py` ✅ (5 sections dynamiques retriées par fraîcheur) — **idempotence confirmée** (2ᵉ passage : hash identique)
- `build_codes_json.py` ✅ (codes réellement modifiés) → `data/codes.json` : **179 jeux, 1196 codes actifs** (JSON valide)
- `build_sitemap.py` ✅ → `sitemap.xml` : **368 URLs**, valide, finit par `</urlset>` (lastmod : verifDate=179, MAJ=11, mtime=178)

---

## (e) Fichiers touchés + QC

**Pages codes éditées (30)** : steal-a-brainrot, merge-a-nuke, defend-ur-base-with-anime, vv-ultimatum, run-a-restaurant, anime-expeditions, basketball-zero, anime-defenders (codes modifiés) + grow-a-garden, tower-defense-simulator, world-fighters, brainrot-evolution, noob-incremental, fifa-super-soccer, hypershot, spin-a-soccer-card, animal-hospital, sakura-stand, dandys-world, a-dusty-trip, arm-wrestle-simulator, arsenal, bubble-gum-simulator-infinity, dragon-adventures, jailbreak, bee-swarm-simulator, build-a-boat-for-treasure, shindo-life (verifDate) + codes-plants-vs-brainrots (lien guide/tier).
**Nouveau** : `guides/plants-vs-brainrots.html`. **Édités** : `guides.html`, `tier-list/plants-vs-brainrots.html`, `sitemap.xml`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`. **Régénérés** : `index.html`, `actualites/index.html`, `games/**`, `data/codes.json`, `sitemap-games.xml`, etc.

**QC (ÉTAPE 8) — tout vert :**
- 42 fichiers HTML modifiés : tous finissent par `</html>`, **0 null byte**, `<div>` équilibrés, GA4 (G-FEL71QVHNL) présent, cache **v=42** partout (344 fichiers uniformes).
- `node --check js/main.js` ✅ · JSON valides (codes.json, code-watch.json, games-index.json) · sitemap.xml XML valide.
- Cache JS/CSS inchangé (js/main.js et CSS non modifiés → pas de bump).

⚠️ **Note pour Peter** : un fichier verrou `.git/index.lock` (0 octet) est présent et non supprimable depuis l'environnement (permission refusée). Si ton `git add`/`commit` échoue avec « index.lock exists », supprime-le d'abord : `del .git\index.lock` (Windows).

---

## (f) VOLET ÉDITORIAL — 4 verticales

**🔥 TOP NEWS :** rien de nouveau nécessitant publication ce run (leaders déjà couverts).

- **Roblox** : contribution du jour = le **guide Plants vs Brainrots** (jeu en pleine explosion). Aucun autre nouveau hit ≥4000 non couvert.
- **Aniimo** : aucune actu/patch officiel vérifiable ≥2 sources dans la fenêtre 24-72 h. Rien publié (pas de remplissage).
- **GTA 6** : **rien de neuf** — sortie **19 novembre 2026** (PS5/Xbox Series) verrouillée (Rockstar Newswire), précommandes ouvertes depuis juin, 2ᵉ trailer déjà sorti. Nos pages evergreen `/games/gta-6/` sont à jour. → MONITOR.
- **EA Sports FC 27** : **lancement mondial le 25 septembre 2026** (dans 5 jours) — **déjà correctement affiché** sur nos pages `/games/fc-27/` (« Sortie mondiale le 25 septembre 2026 »). Aucune correction nécessaire ; pas d'ajout de détail non vérifié. → à surveiller la semaine de lancement.

**👀 À SURVEILLER :** FC 27 (semaine de lancement 25/09) ; hotGames Sep-9 non revus ce run (pet-simulator-99, blockspin, squid-game-x, catch-a-monster, 100-days-at-sea, steal-an-egg) → prioritaires au prochain run ; les 4 slugs rotation « à revérifier ».

---

**Pour publier : dans le dossier GameNova, lance** `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` **. Hostinger déploie automatiquement après le push.**
