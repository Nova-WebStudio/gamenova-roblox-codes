# ZoneBlox — Audit SEO & Roadmap (Directeur SEO)

**Date :** 24 juillet 2026 · **Langue primaire retenue :** Français (moat existant ; EN plus tard) · **KPI unique :** faire croître chaque jour l'autorité topicale de ZoneBlox.

---

## 📌 Dernière brique — J33 (20 septembre 2026)

**Codes (PRIORITÉ) — hotGames + rotation, plusieurs corrections réelles de faux-actifs :**
- **hotGames (15 vérifiés, 5 modifiés)** : Steal a Brainrot **1→0** (BESTBRAINROTEVER périmé — Pocket Tactics 1er sept. + GamesRadar/PCGamesN concordants « aucun code actif ») ; Merge a Nuke **3→2** (UPDATE2 & ATOMIC périmés, +DELAY — Pocket Tactics 16 sept.) ; Defend Ur Base With Anime **5→8** (nos 5 anciens périmés, rebâtie sur les 8 actifs Beebom 1er sept. : UPDATE11/BLUE/GOALKEEPER/UPDATE10/DIOBOSS/TRAVELLINGMERCHANT/LUCKYSPINS/FLEXAVATARS) ; VV Ultimatum **1→6** (Pocket Tactics 18 sept.) ; Run a Restaurant **1→2** (+FISHIES, sources datées 20 sept.). Confirmés stables (« Vérifié le » au 20 sept.) : Grow a Garden (2), Tower Defense Simulator (2), World Fighters (24), Brainrot Evolution (24/88), Noob Incremental (11), FIFA Super Soccer (WorldCupSecret), Hypershot (ONEBILLION), Spin a Soccer Card (0, STAR-STORM en attente), Animal Hospital (0 = pas de système de codes), Sakura Stand (2).
- **Rotation (18 slugs — 3 modifiés, 11 confirmés OK, 4 à revérifier)** : **Anime Expeditions** correction MAJEURE — nos 10 « actifs » TOUS périmés (Pocket Tactics 15 sept.) → rebâtie sur les 7 actifs (restartsorry!/fastrestart!/Eclipse/250klikes/8thCompany/SummerSiege/LighthingGod) ; **Basketball Zero** nos 4 (IZURE/15IZURE/TATLISV2/15TATLISV2) périmés (Pocket Tactics 19 sept.) → SCARYMONSTER + 15SCARYMONSTER (4→2) ; **Anime Defenders** page vide → 12 actifs (Pocket Tactics + aggregat concordants, 0→12). Confirmés OK : sakura-stand, dandys-world, a-dusty-trip, arm-wrestle-simulator, arsenal, bubble-gum-simulator-infinity, dragon-adventures, jailbreak (2 codes YouTube confirmés PT 18 sept. — aggregat trompeur écarté), bee-swarm-simulator, build-a-boat-for-treasure, shindo-life. `catalogVerify` MAJ (14 slugs).
- **À revérifier** : toilet-tower-defense (collision Toilet VERSE / original), fish-it (conflit DIVING actif PT vs notre historique + source 18j, codes rapides), type-soul (source unique fast-expiring), da-hood (DOG/SHARK absents des listes actives mais pas de preuve propre).

**BRIQUE ÉTAPE 2bis = clôture du cluster « Plants vs Brainrots » (codes ✓ · tier ✓ · guide ✗ → ✓).** Le jeu est un des plus gros hits de sept. 2026 (croissance x2 plusieurs semaines, ~916K CCU, 3ᵉ le plus joué) mais son cluster était orphelin de guide. Création de **`guides/plants-vs-brainrots.html`** (~1 484 mots FR) : découverte, boucle planter-défendre-encaisser, meilleures plantes (Cactus/Sunflower/Dragon Fruit/Strawberry ; top-tier Shroombino/Tomatrio/Commando Apple/King Limone), Brainrots en revenu passif, Fusion/Rebirth/Mutations (Gold x2, Diamond x3, Frozen x4, Neon x4,5), réglages Auto-Sell & Equip Best, 6 astuces, FAQ 4 Q. Intention *how-to* distincte des codes (transactionnel) et de la tier list (classement) → **aucune cannibalisation**. Sourcé ≥2 datés : **games.gg/gam3s.gg** (guide débutant & « how to make money fast ») + **Plants vs Brainrots Wiki (Fandom, Mechanics)** + **Sportskeeda**. **EEAT** : byline « L'équipe Zoneblox » + politique éditoriale + note d'évolutivité + renvoi wiki/Discord officiels ; aucune valeur inventée. **Schema** Article + BreadcrumbList + FAQPage. **Maillage (anti-orphelin)** : vraie miniature tr.rbxcdn.com (réutilisée de la page codes), carte hub `guides.html`, `<url>` sitemap.xml, **liens croisés codes ↔ tier ↔ guide** (guide → codes+tier ; codes → guide+tier ; tier → guide). Cache JS inchangé (v=42).

**Trending re-scanné (rblxdb/games.gg 16-20 sept.) :** #1 Steal An Egg (~1,7M), leaders (Blox Fruits, Rivals, Jujutsu Shenanigans, Steal a Brainrot, Grow a Garden, Plants vs Brainrots) tous couverts. Aucun nouveau hit ≥4000 non couvert détecté ce run.

**Prochaine brique recommandée (J34), par ordre de priorité :**

1. **Ajouter 2 vidéos oEmbed vérifiées** aux clusters Plants vs Brainrots et/ou Search For The Needle (guides sans vidéo) — dès que l'accès oEmbed YouTube est disponible (bloqué en run non-interactif : endpoint hors provenance).
2. **Guide complet pour un autre top hit sans guide** (ex. vérifier la couverture des tops trending), intention how-to distincte + maillage codes↔tier↔guide.
3. **Ajouter le bandeau CTA `data-cta="guidelink"`** manquant sur `codes-plants-vs-brainrots.html` (template ancien) pour homogénéiser le maillage codes→guide/tier.
4. **Enrichir la verticale Aniimo** (fiche créature/objet ou guide d'intention) via les JSON de `data/aniimo/` puis build_site.py, si ≥2 sources fiables disponibles.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Dernière brique — J32 (19 septembre 2026)

**Codes (PRIORITÉ) — hotGames + rotation, plusieurs corrections réelles de faux-actifs :**
- **hotGames (7 vérifiés, 3 modifiés)** : Anime Last Stand **22→3 actifs** (Destructoid 15 sept. + Pro Game Guides 1er sept. concordants : seuls MagicKnights!, ElfReincarnation!, IsItReallyWeekly?! actifs ; Beebom = outlier périmé écarté) → 19 codes déplacés en expirés ; King Legacy **7→9** (+RainbowDragon, +2MFAV, confirmés Pocket Tactics 18 sept. + PC Gamer) ; Blade Ball **13→15** (+GOODVSEVIL, +DUNGEONSRELEASE, GamesRadar 18 sept. + Beebom concordants ; SERPENT gardé malgré conflit GR actif/Beebom expiré = source récente prioritaire). Blox Fruits (23), Grow a Garden (2), Steal a Brainrot (1), Fruit Battlegrounds (2) confirmés stables, « Vérifié le » au 19 sept.
- **Rotation (jamais vérifiés — 5 traités, 6 flaggés)** : **Iron Soul Dungeon** correction MAJEURE — nos 11 « actifs » TOUS périmés (Pocket Tactics 12 sept. + Beebom 18 sept. concordants) → rebâtie sur les 23 actifs confirmés par les 2 sources (11→23) ; **Bloxstrike** SUPERSOAKED périmé (Beebom) → +MICHAELSRETURN/HAPPYBDAYYUUTO/LORE/RIANOMINATED2026 (1→4) ; **Catch and Tame** page vide → +PLUSHIECODE +FISHINGCLAW (Pocket Tactics 15 sept., 0→2) ; **Dig and Clean** +UPDATE3 (3→4) ; **Fish an Anime RNG** confirmé OK (sous-listage). `catalogVerify` MAJ (5 slugs).
- **À revérifier** (source unique/ambiguë) : grimoires-era (Era vs Era 2), twenty-one (19995 vs 1999), survive-zombie-arena, spin-a-brainrot, be-a-brainrot (conflit « aucun code » vs BRAINROT/RELEASE), button-rng-2.

**BRIQUE ÉTAPE 2bis = clôture du cluster « Search For The Needle » (codes ✓ · guide ✓ · tier ✗ → ✓).** Création de **`tier-list/search-for-the-needle.html`** (~2 320 mots FR) : classement des 10 classes S→D (Ultimate Farmer, The Chosen One, Demolitionist, Drone Specialist, Forkmaster, Pack Mule, Hay Merchant, Hoover, Prospector, Starter) avec taux de drop, explications, stratégie Gems, conseils débutants, FAQ 6 Q. Intention *classement* distincte du guide *how-to* et des codes *transactionnels* → **aucune cannibalisation**. Sourcé ≥2 datés : **Beebom (11 sept.)** + **games.gg (14 sept.)** ; « The Chosen One » & « Hoover » attribués explicitement à games.gg (plus récent), aucune valeur inventée. **EEAT** : byline « L'équipe Zoneblox » + politique éditoriale ; note d'évolutivité + renvoi menu Classes en jeu. **Schema** ItemList (10) + BreadcrumbList + FAQPage. **Maillage (anti-orphelin)** : vraie miniature tr.rbxcdn.com (réutilisée de la page codes), carte hub `tier-lists.html`, `<url>` sitemap.xml, **liens croisés codes ↔ guide ↔ tier** (bouton CTA guidelink de la page codes + bouton hero du guide pointent désormais vers la tier list dédiée). Cache JS inchangé (v=42).

**Trending re-scanné :** leaders evergreen tous couverts ; aucun nouveau hit ≥4000 non couvert détecté ce run.

**Prochaine brique recommandée (J33), par ordre de priorité :**

1. **Ajouter 2 vidéos oEmbed vérifiées** au guide et/ou à la page codes Search For The Needle (cluster complet mais sans vidéo) — enrichit l'EEAT et l'information gain.
2. **Value/trading list** (GAG pets ou Blox Fruits) uniquement si la maintenance quotidienne des valeurs (≥2 sources datées) est tenable.
3. **Enrichir la verticale Aniimo** (nouvelle fiche créature/objet ou guide d'intention) via les JSON de `data/aniimo/` puis build_site.py.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Dernière brique — J31 (18 septembre 2026)

**Codes (PRIORITÉ) — 2 corrections réelles + hotGames + 11 jeux de rotation vérifiés :**
- **Be a Fish Bait (rotation, jamais vérifié — correction majeure de faux-actifs)** : nos **8 « codes actifs » étaient TOUS périmés** (BAITAURA, 4000LIKES, 2500CCU, 2000/1500/1000/500LIKES, OFFICIAL) — Pro Game Guides (1er sept.) les liste explicitement en « Inactive ». Remplacés par les **2 vrais actifs HOOLALALA + SHARDS** (PGG + PC Gamer + Beebom). 8→2, 8 déplacés en expirés, compteur hero + body 8→2.
- **Anime Card Farm (rotation, jamais vérifié)** : notre page affichait **0 code** alors que 4 sont actifs (Dexerto 10 sept. + PGG 1er sept. concordants) → ajout **BRUTALCOMEBACK!, PRODUCTION!, TRAITS!, POTIONS** (TRADING! écarté = source unique Dexerto), compteur 0→4.
- **hotGames confirmés stables** (« Vérifié le » rafraîchi au 18 sept.) : Grow a Garden (2 exacts — FREESEED/STORY/STARBUD = PGG seul le 17/09 → en `_pending` ; torigate reste expiré car Beebom+PCGamesN concordants), Steal a Brainrot (1), Blue Lock Rivals (3 exacts — SORRYFORNIKODELAY vu en snippet mais absent de la table active PGG → prudence), Volleyball Legends (3), Fisch (3), Anime Vanguards (8).
- **Rotation confirmés OK (jamais vérifiés, sous-listage acceptable)** : wizard-alchemy (10/10 actifs confirmés), anime-stars (6/6 actifs, Dexerto 2-3 sept.), dig (1 exact, PocketGamer 12 sept.), search-for-the-needle (2 exacts WEATHER/PETS), evomon (4/4 actifs, PGG), encounters (IKES=515 cristaux confirmé RobloxDen), steal-a-fish (ADMINFISH confirmé), dungeon-quest-reborn (0 = pas de système de codes, confirmé), kick-a-lucky-block (0 = pas de système de codes, confirmé). `catalogVerify` mis à jour (11 slugs), « Vérifié le » au 18 sept.
- **⚠️ À revérifier au prochain run :** **grimoires-era** (aucune source datée 2026 fiable — PCGamesN=2024 périmé ; 4ᵉ report), **bloxstrike** (codes à usages limités MICHAELSRETURN/HAPPYBDAYYUUTO non confirmables sans risque ; SUPERSOAKED probablement expiré), **be-a-brainrot** (conflit : « aucun code actif » vs BRAINROT/RELEASE affichés), **catch-and-tame** (page vide mais ~36 codes actifs — à ENRICHIR), **button-rng-2** (page vide ; pas de liste datée sept. 2026).

**Trending re-scanné (rblxdb/roblox charts 16 sept.) :** #1 Steal An Egg (~1,7M, couvert), leaders evergreen (Grow a Garden, Brookhaven, Rivals, 99 Nights) tous couverts. Aucun nouveau hit ≥4000 non couvert détecté ce run.

**BRIQUE ÉTAPE 2bis = approfondissement du cluster « Search For The Needle » (hit ~38K CCU couvert par sa page codes au J30, mais orphelin de cluster).** → Création de **`guides/search-for-the-needle.html`** (~1 690 mots FR) : intention how-to distincte (« guide / comment jouer / meilleures classes / comment avoir des gemmes / pets ») **≠** l'intention transactionnelle de la page codes → **aucune cannibalisation**. Contenu sourcé ≥2 (Pocket Tactics 17 sept. + Pro Game Guides/games.gg guides débutant & tier list des classes) : boucle de jeu, améliorations Main (Hold/Speed/Grasp) + sac, 8 classes (Pack Mule, Hay Merchant, Forkmaster, Demolitionist, Drone Specialist, Ultimate Farmer…), gemmes, pets (Cow/Dog), 6 astuces, FAQ 4 Q. **EEAT/honnêteté** : byline « L'équipe Zoneblox » + lien politique éditoriale + note d'évolutivité + renvoi wiki officiel ; aucun chiffre inventé. **Schema** Article + BreadcrumbList + FAQPage. **Maillage (anti-orphelin)** : vraie miniature tr.rbxcdn.com, carte hub `guides.html`, `<url>` sitemap.xml, **liens croisés codes ↔ guide** (bouton hero du guide + ajout du bandeau CTA `data-cta="guidelink"` manquant sur la page codes → 📖 Guide complet + 📊 Tier lists). Cache JS inchangé (js/main.js non modifié → reste v=42).

**Prochaine brique recommandée (J32), par ordre de priorité :**

1. **Tier list Search For The Needle** (`tier-list/search-for-the-needle.html`) : classement des 8 classes (S/A/B) sourcé ≥2 (games.gg + wiki) — complète le cluster SFTN (codes ✓ · guide ✓ · tier ✗) ; relier codes ↔ guide ↔ tier + carte hub tier-lists. Ajouter aussi 2 vidéos oEmbed au guide/codes SFTN quand l'accès YouTube est disponible.
2. **catch-and-tame** : page vide alors que ~36 codes actifs existent (PC Gamer/PGG 8 sept.) — compléter proprement (≥3 sources datées) + regen codes.json.
3. **grimoires-era** — lever enfin la collision de nom via placeId puis élaguer contre une liste expirée datée (4 reports).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J30 (17 septembre 2026)

✅ **Sandbox bash de nouveau disponible** → `build_codes_json.py`, `build_sitemap.py`, `node --check`, `git` opérationnels. Régénérations faites ce run.

**Codes (PRIORITÉ) — 6 corrections/rotations réelles + 18 jeux de rotation vérifiés :**
- **Blue Lock Rivals (hotGame)** : rotation Niko — nos 4 codes (NELKING/NIKOSOON/UBERSMONTH/SORRYLOADING) désormais TOUS en « Inactive » chez Pro Game Guides (15 sept.). Remplacés par **NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK!** (PGG + GamesRadar 14 sept.), 4 anciens déplacés en expirés, compteur 4→3, changelog corrigé. (La confirmation attendue au J29 est faite.)
- **Blox Fruits (hotGame)** : `Lightningabuse` déplacé en expiré (Beebom 13 sept. explicite). 24→23.
- **Anime Vanguards (hotGame)** : ajout de 5 actifs confirmés (Pocket Tactics 16 sept. + GamesRadar) — MiniUpd2, Wrath, Retribution, 1DayDelay, 25thHour. 3→8.
- **Fire Force Online (rotation, laissé « à revérifier » au J28)** : nos 3 codes (REIGNITION/REIGNITION2/55KLIKES) **tous listés expirés** par Roblox Den (vérif du jour). Remplacés par **MOREFRAMES** (page Roblox officielle) **+ LEAKPATCHED** (≥2 sources) ; ENDGATEKEEP tenu en attente (source unique). 3→2.
- **Jujutsu Infinite (rotation)** : notre page affichait 0 code alors que **HELLO_JJI** (50 Spins) est actif (PGG 15 sept. « Active (1) » — les 400K_SUBS/JUDGEMAN_REWORK/JUDGE_SOON vus en snippet sont en réalité INACTIFS, piège de conflit évité). 0→1.
- **Evade (rotation)** : notre page affichait 0 code alors que **HAPPY4THBIRTHDAYEVADE** (40 Points) est actif (GamesRadar/PGG/PocketTactics 8 sept.). 0→1.

**hotGames confirmés stables (sous-listage acceptable, « Vérifié le » rafraîchi au 17 sept.) :** Grow a Garden (2), Steal a Brainrot (1), Blade Ball (13), Volleyball Legends (⚠️ 3 exacts — GamesRadar 14 sept. place UPDATE_86/HAKKA_RETURN/SPIKER/UPDATE_85/SHIRO/BLOCKED en EXPIRÉS, ne pas les rajouter ; snippet de recherche trompeur), Fisch (3 exacts — LittleBudlingUpdate confirmé expiré 14 sept.).

**Rotation confirmés OK (jamais vérifiés, sous-listage acceptable)** : mad-city (6), car-crushers-2 (6), anime-story-2 (17/111), restaurant-tycoon-3 (11/36), war-tycoon (4), untitled-attack-on-titan (6, dont 390k = palier le plus récent), pressure (4), sonic-speed-simulator (8), strongman-simulator (8), anime-souls-simulator-x (3), anime-warriors-iii (0 = pas de système de codes), adopt-me / brookhaven / tower-of-hell / work-at-a-pizza-place (0 = jamais de codes). `catalogVerify` mis à jour (18 slugs), « Vérifié le » au 17 sept.

**⚠️ À revérifier au prochain run :** **grimoires-era** (collision Era / Era 2 / Legacy / Clover — sources datées sept. portent sur d'autres jeux ; désambiguïser via placeId avant tout retrait — 3ᵉ run consécutif de report).

**Trending re-scanné (rblxdb/rolimons 14-17 sept.) :** leaders evergreen couverts. **1 gros hit NON couvert traité** : **Search For The Needle** (~38K joueurs en simultané, pic 85K ; universeId 10756011174 ; Garage Games ; sorti le 23/08). → **BRIQUE ÉTAPE 2bis = création de page ÉTAPE 1** : nouvelle page `codes-search-for-the-needle.html` (1857 mots FR, vraie miniature tr.rbxcdn.com, codes **WEATHER**/**PETS** actifs + ALIEN expiré vérifiés GamesRadar 17 sept., description/mécaniques développées, 6 astuces, FAQ 4 Q, About). Intention distincte (transaction « codes <jeu> »), aucune cannibalisation (aucune page existante). Intégrée partout : carte `index.html` (const GAMES), carte `tous-les-codes.html`, `GAMES_INDEX`+`ROBLOX_THUMBS`+`ROBLOX_UNIVERSE_IDS` (js/main.js, node --check OK), `<url>` sitemap.xml, `data/codes.json` régénéré (179 jeux, 1181 codes). Cache JS bumpé **v=41 → v=42** sur 341 fichiers. ⚠️ Pas de vidéos oEmbed (accès YouTube refusé dans le run non-interactif) — à compléter ; pas encore de guide/tier-list dédiés SFTN.

**Prochaine brique recommandée (J31), par ordre de priorité :**

1. **Compléter Search For The Needle** : ajouter 2 vidéos oEmbed vérifiées quand l'accès YouTube est disponible + créer `tier-list/search-for-the-needle.html` (classes) et/ou `guides/search-for-the-needle.html`, puis lier codes ↔ guide ↔ tier.
2. **catch-and-tame** (flaggé J28/J29) : notre page affiche « aucun code » alors que ~36 codes existent (PC Gamer/PGG) — compléter proprement + regen codes.json.
3. **grimoires-era** — lever enfin la collision de nom (placeId) puis élaguer contre une liste expirée datée.
4. Autre hit trending à surveiller : **Jump for Animals** (~60K, flaggé J29) — créer sa page si momentum confirmé.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J29 (15 septembre 2026)

⚠️ **Contexte technique :** sandbox bash toujours indisponible (bug Windows update du 8 sept.) → `build_codes_json.py` / `build_sitemap.py` / `sync_month.py` / `node --check` / `git` **non exécutables**. Toutes les éditions faites via l'outil Edit (remplacement exact, 0 null byte). **`data/codes.json` et les `lastmod` du sitemap sont à régénérer dès le retour de bash** (des codes ont changé ce run).

**Codes (PRIORITÉ — run dominé par 3 rotations/corrections de faux-actifs) :**
- **Volleyball Legends (hotGame)** : rotation Update 87 — UPDATE_86/HAKKA_RETURN/SPIKER **expirés** (GamesRadar 14 sept. explicite), remplacés par **UPDATE_87/RONIN_RETURN/KATANA** (GamesRadar + RoCodes + Roonby). 3→3.
- **Anime Vanguards (hotGame)** : rotation — MiniUpd2/Wrath/Retribution **expirés** (GamesRadar 14 sept.), remplacés par **Assault/SummerLeaving/AnniNextHopefully** (GamesRadar + PocketGamer + PCGamesN + Beebom). 3→3.
- **Anime Squadron (rotation, jamais vérifié — correction majeure de faux-actifs)** : nos **8 « codes actifs » étaient tous périmés** (codes de lancement UPD0.5!/Yokoso!/50kCCU!/10MilVisits!… ; jeu désormais à l'Update 4.0). GamesRadar (7 sept.) liste explicitement 5 des 8 en expirés + les 3 autres absents de la liste active. → **8→5** (10KCCUTHANKS!/CrystalCompensation/UPD4.0!/ThePowerToProtect!/TheCalamity!), 8 déplacés en expirés, compteur hero + changelog corrigés.

**Confirmés stables / sous-listage acceptable :** Blue Lock Rivals (4 : NELKING/NIKOSOON/UBERSMONTH/SORRYLOADING = PocketGamer 12 sept. servie ; set NIKOHERE/GATEKEEPOVER/QOLNEXTWEEK!/SORRYFORNIKODELAY vu en snippet de recherche mais **non confirmé sur une page datée** → prudence, en attente), Fisch (3 ; LittleBudlingUpdate = code d'event déjà expiré 14 sept., non ajouté), Blade Ball (13), Fruit Battlegrounds (2), Blox Fruits (24), Grow a Garden (2), Steal a Brainrot (1). **Rotation confirmés OK (jamais vérifiés)** : universal-tower-defense-x (⚠️ = « Universal Tower Defense **Z** » anime, à ne pas confondre avec le « Universal Tower Defense » de PCGamesN = autre jeu), spongebob-tower-defense (2), weapon-rng (4, Roblox Den 14 sept. 0 expiré), anime-spirits (6/102), slime-rng (11/22), rng-heroes (2/21), blox-monsters (5/15, Insider Gaming 0 expiré), case-simulator-rng (1), survive-the-killer (0 = honnête, confirmé multi-sources).

**⚠️ À revérifier au prochain run :** **anime-stars** (collision de nom/version : nos codes launch-era ≠ liste active courante Update 3.5/4 ; désambiguïser via placeId), **evomon** (nos 4 codes milestone ni confirmés ni infirmés), **catch-and-tame** (notre page affiche « aucun code » mais **36 codes actifs existent** — PC Gamer/PGG 8 sept. — à compléter proprement + regen codes.json quand bash revient).

**Trending re-scanné (rblxdb/roblox charts, 7 sept.) :** #1 **Steal An Egg** (~1,4M, **couvert**), leaders evergreen tous couverts. **2 nouveaux hits NON couverts détectés** : **Jump for Animals** (~60K CCU, live 12 août) et **Search For The Needle** (~36K, 23 août) → candidats prioritaires pour une nouvelle page (ÉTAPE 1) **dès le retour de bash** (thumbnail API + sitemap + codes.json + QC requis).

**Brique ÉTAPE 2bis (EEAT/honnêteté) :** conformément aux runs J26–J28 et vu l'indisponibilité de bash, la brique d'autorité du jour est **l'assainissement des signaux de confiance** (correction Anime Squadron 8→5 faux-actifs + 2 rotations hotGames). **Aucune nouvelle URL créée** : bash étant indisponible, créer une page sans régénérer sitemap/codes.json ni passer le QC serait un demi-travail (choix honnête vs. gonfler le nombre de pages).

**Prochaine brique recommandée (J30), par ordre de priorité :**

1. **Créer les pages des 2 nouveaux hits** — **Jump for Animals** et **Search For The Needle** (≥4000 joueurs, momentum réel, non couverts) selon ÉTAPE 1 (thumbnail tr.rbxcdn.com, ≥1200 mots, intégrations complètes + sitemap + codes.json) **dès que bash est rétabli**.
2. **catch-and-tame** — compléter la page (aujourd'hui vide) avec la liste active réelle (≥3 sources datées : PC Gamer/PGG/Pocket Tactics 8 sept.) + regen codes.json.
3. **Tier list Steal an Egg** — « meilleurs pets par revenu/biome » (réconcilier ≥2 sources datées concordantes avant publication ; cluster #1).
4. **anime-stars / evomon** — finir les 2 slugs « à revérifier » avec liste complète datée + désambiguïsation placeId.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen. (Jump for Animals / Search For The Needle = à traiter en priorité dès bash rétabli.)

---

## 📌 Archive — J28 (9 septembre 2026)

**Codes (PRIORITÉ — run dominé par 8 corrections de faux-actifs, dont 2 majeures) :**
- **Sailor Piece (rotation, jamais vérifié)** : nos **16 « codes actifs » étaient TOUS périmés** — Pocket Tactics (7 sept.) ne liste plus que **TojiDanteUpdate + Weloveyou** en actifs et place explicitement nos 16 (KINGUPDATEHASARRIVED, RAIDUPDATENOW, GHOULUPDATE, MASTERY, RAIDS, 1B100/200/300MVISITS…) en expirés. Jeu one-piece à fort turnover. → **16→2**, 16 déplacés en expirés, compteur hero + `data/codes.json` corrigés. Correction d'honnêteté majeure.
- **Catch a Monster (hotGame)** : liste ré-auditée contre Pocket Tactics (2 sept., liste expirée explicite) — **6 de nos 11 codes marqués expirés** (massglaw, crysting, graon, magmorus, moovik, danvok) + 5 autres (clacerglaw, cabshark, ungolem, LIVEXP, LIVECOIN) absents des actifs courants. → **11→9** codes courants (mutatebug, achievebug, turret, Oblivion, Plagcannon, Gearif, coin, xp, cam), 11 anciens en expirés. Jeu neuf à turnover rapide.
- **Grand Piece Online (rotation)** : nos 3 codes (FREE_Drops3, FREE_EXP3, 5FREETAILORVOUCHERS_3) **tous listés expirés** par Pocket Tactics (2 sept.) → remplacés par **FREE_Drops6, ILOVEGPO_2**. 3→2.
- **Peroxide (rotation)** : `YayAHalloweenUpdate` expiré (Pocket Gamer 5 sept.) + 4 codes courants manquants ajoutés → **4→7** (445kLikesYipee, 4thJuly2026, OneMillionPE, EgxcellentEggventure + TasteTheRainbow/440kLikes/The1HourOfDoomAndDespair conservés).
- **Jujutsu Shenanigans (rotation)** : Beebom (1er sept.) place SLATECONCRETE/X6X31F47UN8JM1NEP/RIPBOWE/67 en expirés → **5→1** (A7D2L26RNEPG74A3Q). ⚠️ **SLATECONCRETE en conflit** (Beebom expiré vs PC Gamer actif) → retiré des actifs **par prudence**, consigné en `_pending`.
- **Haze Piece (rotation)** : ajout du nouveau **ABYSSALCTHULHU** (5 race spins, PT 5 sept.) ; les 3 existants confirmés actifs. 3→4.
- **Project Mugetsu (rotation)** : ajout de 3 codes courants confirmés PGG (1er sept.) **TheD1Gambler26, SUPPORTANIMEOVERSEAS, ProjectSoon** ; existants conservés. 4→7.
- **Blockspin (hotGame)** : ajout **BLOCKSPIN_GRIPS_UPDATE + UNDER_THE_BARREL** (Pocket Gamer 5 sept.) ; nos 2 confirmés actifs. 2→4.

**Confirmés stables / sous-listage acceptable :** Steal an Egg (0 — jamais de codes, Collect Rare Pets ; PCGamesN), Pet Simulator 99 (0 — merch codes only), Squid Game X (6 confirmés actifs Roblox Den 8 sept. ; UPDATE11RELEASE non ajouté, source unique crowd), 100 Days at Sea (3 exacts : CLASSES/DECORATE/20Pearls, GamesRadar/Dexerto 7 sept.), Untitled Boxing Game (nos 9 confirmés actifs Pocket Gamer 5 sept.), Slap Battles (Happy5lappiversary/spookyseason25 confirmés + 1x1x1x1x1x1 permanent).

**⚠️ À revérifier au prochain run :** **sonic-speed-simulator** (conflit 0 vs 5 actifs + version « RE-RAN » → liste complète requise), **fire-force-online** (MAJ 2 sept. a retiré beaucoup de codes ; statut REIGNITION/REIGNITION2/55KLIKES non confirmé). `catalogVerify` mis à jour (8 slugs rotation), « Vérifié le » rafraîchi au **9 sept.** sur les pages traitées, `data/codes.json` régénéré (178 jeux, 1202 codes actifs).

**Trending re-scanné :** leaders (Steal An Egg, Blox Fruits, Steal a Brainrot, Grow a Garden, Brookhaven, Murder Mystery 2, Adopt Me) — **tous couverts**. Aucun nouveau hit ≥4000 non couvert → evergreen.

**Brique ÉTAPE 2bis (EEAT/honnêteté) :** conformément au précédent J26/J27, le run ayant été **majoritairement consommé par des corrections de faux-actifs prioritaires** (dont 2 majeures : Sailor Piece 16→2 et Catch a Monster 11→9), **la brique d'autorité du jour est cet assainissement de signaux de confiance** — retirer des codes morts/possiblement invalides améliore directement l'EEAT et évite de tromper l'utilisateur. **Aucune nouvelle URL créée** (choix honnête : les valeurs « meilleurs pets par revenu » de Steal an Egg **divergent entre sources** — Unicorn $1B/s vs Oni Tiger $600M/s — donc pas de tier list publiée sur des chiffres non concordants, plutôt que d'inventer un classement).

**Prochaine brique recommandée (J29), par ordre de priorité :**

1. **Tier list Steal an Egg — « meilleurs pets par revenu/biome »** : réconcilier ≥2 sources datées concordantes (games.gg / timesaver / joytify) sur les revenus/seconde AVANT de publier (les valeurs divergent aujourd'hui) ; cluster #1, vraie brique de contenu.
2. **grimoires-era** — lever la collision de nom (placeId de `codes-grimoires-era.html`) puis élaguer contre une liste expirée propre (Roblox Den / Pocket Tactics).
3. **anime-story-2** — récupérer liste active **et** expirée explicite (PGG « Worlds Collide » / Roblox Den) avant tout retrait (jeu qui garde beaucoup de codes).
4. **sonic-speed-simulator / fire-force-online** — finir les 2 slugs laissés « à revérifier » ce run avec une liste complète datée.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J27 (8 septembre 2026)

**Codes (PRIORITÉ — 3 corrections majeures de faux-actifs) :**
- **Garden Tower Defense (rotation, jamais vérifié)** : nos **19 codes tous périmés** — Pro Game Guides (5 sept.) les liste **tous en « Inactive »**, recoupé par la recherche datée du 7 sept. (seuls FANTASY + FRONTIER actifs). Ce TD fait tourner ses codes ~tous les 3 jours. → **19→2** (FANTASY 500 Seeds, FRONTIER 750 Seeds), les 19 déplacés en expirés, compteur hero corrigé, `data/codes.json` régénéré.
- **Pet Simulator X (rotation, brique roadmap J27 #1 — EEAT/honnêteté)** : les **8 « codes actifs » étaient FABRIQUÉS** (FURRYFRIEND, SINGLESTRIKE, PET_SQUAD, BIGUPDATE, CRYSTALBOOST, DIAMONDS2026, PSWELCOME, HATCHMASTER) — **absents des listes actif ET expiré** de Pocket Gamer (1ᵉʳ sept., « no active codes »). Le jeu (GLITCH) n'a plus aucun code valide. → page passée honnêtement à **0 code actif** + chargement de la **vraie liste expirée** (44 codes PGG). Correction d'honnêteté majeure.
- **Volleyball Legends (hotGame)** : rotation Update 86 — nos UPDATE_85/SHIRO/BLOCKED **expirés** (PGG 5 sept.) → nouveaux **UPDATE_86, HAKKA_RETURN, SPIKER** (PGG + agrégats datés). 3→3 (renouvelés), `data/codes.json` régénéré.

**Confirmés stables / sous-listage acceptable (hotGames)** : Grow a Garden (RDCAward/BEANORLEAVE10 ; TEAMGREENBEAN écarté = code GAG **2**, piège de désambiguïsation), Blade Ball (13 confirmés Pocket Tactics 1er sept. ; BATTLEROYALE contesté → non ajouté), Anime Last Stand (22 confirmés Roblox Den 7 sept. + Beebom ; PGG outlier à 3), Blue Lock Rivals (4), Anime Vanguards (3), Fisch (3 ; **SkycrestIsInTheSky confirmé expiré** GamesRadar 7 sept.), Fruit Battlegrounds (2 ; EVENHIGHER! source unique → non ajouté), Blox Fruits (24), King Legacy (7), Tower Defense Simulator (2), Brainrot Evolution (24, tous confirmés Nerdschalk 5 sept.), Steal a Brainrot (1).

**Rotation confirmés OK (jamais vérifiés, sous-listage acceptable)** : plants-vs-brainrots (5, Beebom 1er sept.), grow-a-chicken-fighter (4), attack-on-titan-revolution (21), rivals (8/9), muscle-legends (14), skibidi-masters-tower-defense (5, PGG garde tous les paliers), grow-a-garden-2 (3 exacts), knockout, character-rng, jules-rng, broken-blade, murder-mystery-2 (0, confirmé sans code depuis des années), ninja-legends.

**⚠️ À revérifier au prochain run** : **grimoires-era** (collision Era/Era 2/Legacy, pas de source datée sept.), **anime-story-2** (17 codes de lancement ; frontière actif/expiré incertaine, 111 « working » non énumérés), **mad-city** (conflit Roblox Den « 6 working » vs Pocket Gamer « none »). `catalogVerify` mis à jour (14 slugs rotation + pet-simulator-x), « Vérifié le » rafraîchi au **8 sept.** sur les pages traitées.

**Trending re-scanné (≥2 sources, rblxdb/rotrends 6 sept.) :** #1 Steal An Egg (~2,45M), Blox Fruits (~717K), Brookhaven, +1 Speed Keyboard Escape (`evasion-clavier`), Murder Mystery 2, Grow a Garden, Steal a Brainrot — **tous couverts**. Aucun nouveau hit ≥4000 non couvert → evergreen.

**Brique ÉTAPE 2bis (EEAT/honnêteté) :** la correction Pet Simulator X (retrait de 8 codes fabriqués + rétablissement d'une liste expirée authentique sourcée) constitue la brique d'autorité du jour — elle assainit un signal de confiance critique (des codes inventés nuisent directement à l'EEAT et au classement). Le run ayant été majoritairement consommé par 3 corrections de faux-actifs (priorité absolue), aucune nouvelle URL n'a été créée (choix honnête vs. gonfler le nombre de pages).

**Prochaine brique recommandée (J28), par ordre de priorité :**

1. **grimoires-era** — lever la collision de nom (confronter au placeId Roblox de notre page : `codes-grimoires-era.html`) puis élaguer contre une source à liste expirée propre (Roblox Den / Pocket Tactics).
2. **anime-story-2** — récupérer la liste active **et** expirée explicite (PGG « Worlds Collide » / Roblox Den) pour confirmer ou élaguer les 17 codes de lancement ; jeu qui garde beaucoup de codes → vérifier avant tout retrait.
3. **Tier list Steal an Egg — enrichissement « meilleurs pets par revenu / par biome »** (≥2 sources datées) pour compléter le cluster n°1 (~2,45M joueurs) — vraie brique de contenu si aucun faux-actif prioritaire.
4. **mad-city** — trancher le conflit Roblox Den vs Pocket Gamer avec une 3ᵉ source datée.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J26 (7 septembre 2026)

**Codes (PRIORITÉ — 4 corrections majeures de faux-actifs) :**
- **Anime Last Stand (hotGame + brique roadmap J26 #1)** : liste de 41 codes ré-auditée contre Roblox Den (checké le 7 sept.) + Pro Game Guides (1er sept.). **19 codes déplacés en expirés** (ALSISBACK!, World3Patch2, WORLD3REBALANCE, StellarWorld, SorryForDelay1/2/3, HypeWorld3, ReleaseCode!, Update0, ALSUPD1/2, BleachSS, HuntersMark, SaveRukia, DelaySorryals, BalancePatch3/3.1, GACHIAKUTA!?, Update83! — aucun listé actif par les deux sources). **22 actifs conservés** (confirmés actifs par Roblox Den 7 sept. ; PGG en conflit → prudence, non retirés). ~24 actifs supplémentaires de Roblox Den NON ajoutés (PGG les marque inactifs). 41→22, compteur hero corrigé.
- **Blue Lock Rivals (hotGame)** : rotation hebdo — UBERSTAKEOVER/KINGNEXTWEEK/EGODEFENSE **expirés** ; nouveaux **NELKING, NIKOSOON, UBERSMONTH, SORRYLOADING** (PGG màj 6 sept. + GamesRadar/Beebom/Pocket Gamer). 3→4.
- **Da Hood (rotation)** : 18 codes **tous périmés** (PGG 3 sept. **et** Pocket Tactics 3 sept. concordent, seasonals 2024/2025) → remplacés par **DOG, SHARK** (300k DHC chacun, 2 sources tier-1). 18→2.
- **Shindo Life (rotation)** : nos 11 codes **tous périmés** (Roblox Den + PGG concordent) → nouvelle liste **29 actifs** = intersection PGG (1er sept.) ∩ Roblox Den (TickDamageBugs!, FixingShindoBuggyTimes!, PatchUpdate249point5!, RELLGIFTbag!, RELLGIFTsc!…). 11→29.
- **Bubble Gum Simulator Infinity** : typo corrigé `ogbfs`→`ogbgs` (Roblox Den + Insider Gaming).
- **Confirmés stables (hotGames)** : Grow a Garden (RDCAward/BEANORLEAVE10, PCGamesN), Anime Vanguards (Retribution/Wrath/MiniUpd2), Volleyball Legends (UPDATE_85/SHIRO/BLOCKED, GamesRadar 3 sept. — candidats UPDATE_86/HAKKA_RETURN/SPIKER NON confirmés → non ajoutés), Steal a Brainrot (BESTBRAINROTEVER), Fruit Battlegrounds (2 actifs).
- **Rotation confirmés OK (sous-listage acceptable)** : Arsenal (5, codes permanents), Dragon Adventures (6/11), Car Dealership Tycoon (14/23), Bee Swarm Simulator (17, aucun nouveau depuis février).
- **⚠️ À revérifier au prochain run** : **pet-simulator-x** (liste de 8 actifs suspecte/probablement périmée ; PocketGamer indique 0 code actif — vérifier Roblox Den) ; **grimoires-era** (collision de nom Era/Legacy/Era 2, sources périmées). `data/codes.json` régénéré. « Vérifié le » rafraîchi au **7 sept.** sur les 178 pages.

**Trending re-scanné (≥2 sources, rblxdb/blox-merch 7 sept.) :** #1 **Steal An Egg ~1,4M** (déjà Jeu de la semaine, inchangé), Blox Fruits, Rivals, Jujutsu Shenanigans, Steal a Brainrot, Adopt Me — **tous couverts**. Aucun nouveau hit ≥4000 non couvert → evergreen.

**Brique ÉTAPE 2bis :** le run a été consommé par **4 corrections majeures de codes** (priorité absolue, qui prime sur la brique cluster). Brique EEAT/honnêteté réalisée : correction d'une ligne de changelog ALS rendue incohérente par le nettoyage (compteur historique redaté « à l'époque »). Le **Jeu de la semaine (lundi)** reste Steal An Egg (toujours #1, honnête de ne pas fabriquer un changement).

**Prochaine brique recommandée (J27), par ordre de priorité :**

1. **pet-simulator-x** — vérifier d'urgence contre Roblox Den (liste active/expirée explicite) : la liste actuelle (8 codes) semble périmée/fabriquée ; corriger honnêtement.
2. **Tier list Steal an Egg — enrichissement « meilleurs pets par revenu / par biome »** (≥2 sources datées) pour compléter le cluster #1 (~1,4M joueurs).
3. **Fish It / Type Soul** — compléter les listes actives (≥3 sources concordantes une fois les conflits levés).
4. **grimoires-era** — lever la collision de nom (confronter au placeId Roblox de notre page) puis élaguer sur une source à liste expirée propre.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Dernière brique — J25 (5 septembre 2026)

**Codes (priorité) — run supplémentaire (run du 04/09 manqué) :** re-scan des jeux chauds les plus volatils (Beebom/Dexerto/PCGamesN/Pocket Tactics/Pro Game Guides/GamesRadar, màj 1-4 sept.). **Confirmés inchangés :** Grow a Garden (2 : RDCAward/BEANORLEAVE10), Steal a Brainrot (1 : BESTBRAINROTEVER, Dexerto 1ᵉʳ sept.), Blue Lock Rivals (3 : UBERSTAKEOVER/KINGNEXTWEEK/EGODEFENSE), Volleyball Legends (3 : UPDATE_85/SHIRO/BLOCKED), Anime Vanguards (3 : Retribution/Wrath/MiniUpd2), Blade Ball (~24 trackés, sous-listage 13 OK, aucun expiré). **1 correction hotGame — Fruit Battlegrounds :** `BIGMILLIHUNNID!`, `ITSTHEBILLION!`, `CODEFIX` **passés expirés** (Pocket Tactics 4 sept., sweep d'expiration explicite ; absents des actifs PGG) → 5→**2 actifs** (HIGHER1M120K, YOO1M110K!) ; `EVENHIGHER!`/`OMGUPDATE22` **non ajoutés** (conflit / <3 sources). **Fisch** `SkycrestNextWeek` **non publié** (conflit Beebom actif vs autre expiré → prudence). `data/codes.json` régénéré (178 jeux, 1255 codes). « Vérifié le » rafraîchi au **5 sept.** sur toutes les pages traitées.

**ÉTAPE 2ter — rotation approfondie (jamais vérifiées) :** 12+ jeux traités. **4 corrections majeures de faux-actifs :** (1) **Jailbreak** 4 actifs tous périmés (apr26/rich100rich/25pass50/20KCASH4U, confirmés expirés Roblox Den 05/09 + Pocket Tactics) → remplacés par les 2 codes stickers permanents `YoutubeHelloItsVG`/`YoutubeNoobFreak` (3 sources). (2) **Basketball Zero** turnover total : 10 codes tous inactifs (PGG 1ᵉʳ sept.) → 4 actifs courants IZURE/15IZURE/TATLISV2/15TATLISV2 (PGG+GamesRadar+agrégats). (3) **Sakura Stand** 8→2 (Touhou/Flandre/Scarlet/NoSleep40HoursGG/Christmas2025!/NewYear2026! expirés, Pocket Gamer 1ᵉʳ sept.). (4) **Dandy's World** fiche inversée corrigée : `ICHOR` (code permanent, actif, 3 sources) remis actif, `2HUNDREDMILLION` (expiré Roblox Den) sorti. **Confirmés OK / sous-listage acceptable :** Arm Wrestle Simulator, Bee Swarm Simulator (14/17 confirmés, codes permanents), Build a Boat (codes permanents), Bubble Gum Sim Infinity (throwback actif ; ⚠️ vérifier « ogbfs » vs « ogbgs »), Toilet Tower Defense (0, jeu retiré). **Laissés à 0 par prudence (codes existent mais conflit/1 source/dump) :** Fish It (conflit majeur pcgamer↔Pocket Tactics), Type Soul (codes rapides, 1 source), Anime Defenders (dump mélangé + risque désambiguïsation vs Anime RNG Defense). **⚠️ À revérifier (sources périmées / pas de liste expirée propre) :** grimoires-era, shindo-life. Suivi `catalogVerify` mis à jour.

**Trending re-scanné (≥2 sources, rblxdb + dualshockers 5 sept.) :** leaders (Steal An Egg #1 ~1,92M, Brookhaven, Blox Fruits, +1 Speed Keyboard Escape=`evasion-clavier`, Murder Mystery 2, Grow a Garden, Steal a Brainrot, Adopt Me) **tous couverts** ; aucun nouveau hit ≥4000 avec codes non couvert → evergreen.

**Brique réalisée (ÉTAPE 2bis — approfondissement du cluster n°1 « Steal an Egg », information gain sans nouvelle URL) :** ajout d'une section **« 10. L'événement Great Bloom & l'incubateur Sakura »** (~450 mots) au guide de base `guides/steal-an-egg.html` (2 654 → ~3 099 mots). **Intention distincte (anti-cannibalisation) :** *how-to événement/mécanique* — débloquer l'incubateur via le pet Crane, farmer les Cristaux Sakura pendant le Great Bloom (~toutes les 30 min, ~3 min), charger à 100/150 % et muter — **complémentaire** de la page `steal-an-egg-mutations.html` (référence des multiplicateurs), vers laquelle elle renvoie sans dupliquer la table. **Aucune nouvelle URL** → zéro risque d'orphelin. **EEAT** : encart « info communautaire » daté + byline ; **sources ≥2 datées** (Beebom + Sportskeeda, concordantes sur fréquence/durée/taux 97,5 %/2,5 %). TOC mis à jour, FAQ renumérotée (10→11), `dateModified` au 5 sept. QC : div équilibrés (0), 0 null byte, fin `</html>`.

**Prochaine brique recommandée (J26), par ordre de priorité :**

1. **Anime Last Stand** — re-vérifier la liste de **41 codes** contre ≥3 sources datées (Beebom + PGG + Fandom) et élaguer les expirés / ajouter les nouveaux avec récompenses exactes (jeu très actif, liste longue, éviter toute régression).
2. **Rotation approfondie — finir grimoires-era & shindo-life** avec une source à **liste expirée propre** (Roblox Den / Pocket Tactics) pour confirmer/élaguer les codes probablement périmés, puis reprendre la rotation (adopt-me, murder-mystery-2, dead-rails, jujutsu-infinite, anime-defenders proprement).
3. **Compléter Fish It / Type Soul** (codes actifs existants) avec ≥3 sources datées concordantes une fois le conflit levé.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J24 (3 septembre 2026)

**Codes (priorité) :** re-scan multi-sources des jeux chauds (Beebom màj 1ᵉʳ sept., PCGamesN, Pocket Tactics, Dexerto). **Aucun changement de liste — tout confirmé stable.** Blue Lock Rivals **3 actifs** (UBERSTAKEOVER/KINGNEXTWEEK/EGODEFENSE — Pocket Tactics 30/08 **ET** Beebom 1ᵉʳ sept. concordent exactement ; les INSANETRAILERSOON/DESTROYERMODE/RINTODAY… sont bien listés **expirés** par les deux → nos 3 sont corrects). Grow a Garden **2 actifs** (RDCAward/BEANORLEAVE10 — Beebom + PCGamesN concordent ; `torigate` **désormais expiré des deux côtés**, conflit clos, correctement hors liste). Steal a Brainrot **1 actif** (`BESTBRAINROTEVER` — Dexerto màj 1ᵉʳ sept. « one active code », conflit PCGamesN clos → notre fiche est correcte). Fruit Battlegrounds **5 actifs** = liste Beebom (aucun nouveau). Blox Fruits, Volleyball Legends, King Legacy, Anime Vanguards, Anime Last Stand (41) inchangés. « Vérifié le » rafraîchi au **3 septembre** sur les **178 pages** ; snapshots code-watch mis à jour (blox-fruits, fruit-battlegrounds, blue-lock-rivals, grow-a-garden, steal-a-brainrot).

**Trending re-scanné (≥2 sources) :** leaders vérifiés (Steal An Egg #1 ~1,77M joueurs, Brookhaven, Blox Fruits, Murder Mystery 2, Grow a Garden, Adopt Me) — **tous couverts**. Seul top-item non couvert : **« +1 Speed Keyboard Escape | Candy & Chocolate »** (~329K joueurs) = obby sans système de codes, déjà fiché comme guide `evasion-clavier` et déféré de longue date (pas de codes à publier). Aucun nouveau hit ≥4000 avec codes non couvert → evergreen.

**Brique réalisée (ÉTAPE 2bis — approfondissement du cluster n°1 « Steal an Egg » + correction d'orphelin) :** nouvelle page **`guides/steal-an-egg-mutations.html`** (~1 600 mots) — « Mutations Steal an Egg (2026) : liste, multiplicateurs & comment les obtenir ». **Intention distincte ciblée** : head terms « steal an egg mutations », « steal an egg multipliers », « spirit bloom steal an egg », « sakura incubator » — intention *référence mécanique* (table des 5 mutations : Silver ×1,25, Bloom ×1,5, Golden ×2, Rainbow ×2,5, Spirit Bloom ×3, taux 97,5 %/2,5 %), **complémentaire mais distincte** du guide complet (how-to général) et de la tier list (classement pets). **Anti-cannibalisation** : aucune page existante ne visait ces head terms mutations ; liens réciproques guide↔mutations↔codes↔tier list. **EEAT/honnêteté** : byline « L'équipe Zoneblox », encart « info communautaire » daté, sources ≥2 croisées (Beebom màj 24/08 **et** games.gg/Sportskeeda/Stealthy Gaming, tous concordants sur les 5 multiplicateurs), aucune valeur inventée. **Schema** Article + BreadcrumbList + FAQPage (5 Q). **Maillage (anti-orphelin)** : carte hub `guides/index.html` avec **vraie miniature tr.rbxcdn.com** (768/432) + ItemList position 54 ; **bonus** — la page **`guides/steal-an-egg.html` (guide de base) était orpheline du hub** (présente aux sitemaps mais sans carte), carte ajoutée (position 53) → trou de maillage corrigé ; entrées `sitemap-guides.xml` + `sitemap.xml` ; liens depuis `codes-steal-an-egg.html` (« Va plus loin ») et `guides/steal-an-egg.html` (articles liés). **Effet SEO** : le cluster du jeu #1 du site (~1,77M joueurs) gagne une brique de référence à fort volume et récupère l'equity vers codes/tier list/guide, tout en réparant un orphelin.

**Prochaine brique recommandée (J25), par ordre de priorité :**

1. **Tier list Steal an Egg — enrichissement « meilleurs pets par biome / revenu par seconde »** ou **value list pets** (≥2 sources datées), pour compléter le cluster #1 ; sinon un how-to « Sakura Incubator / événement Great Bloom » (intention distincte du guide mutations).
2. **Anime Last Stand** — re-vérifier la liste de 41 codes contre ≥3 sources datées (jeu très actif) et élaguer/ajouter si besoin.
3. **Cluster Dungeon Quest Reborn** — surveiller l'apparition d'un système de codes (Discord officiel) ; sinon enrichir la tier list (armes par donjon).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J23 (2 septembre 2026)

**Codes (priorité) :** re-scan multi-sources (Beebom màj 1ᵉʳ sept., PCGamesN, Pro Game Guides, GamesRadar, PC Gamer, Dexerto, Pocket Tactics). **1 changement appliqué.** **Fruit Battlegrounds** → nouveau code actif **HIGHER1M120K** (800 Gems) confirmé **NOUVEAU** par Beebom (page datée 1ᵉʳ sept.) et recoupé Pocket Tactics + Pro Game Guides ; **OMGUPDATE22** basculé en **expiré** (Beebom 1ᵉʳ sept. le liste expiré ; PGG restait sur un snapshot du 6 août). Total actifs inchangé (5), compteur expirés 6→7, note « Mis à jour le 2 septembre » ajoutée sur la fiche + `data/codes.json` régénéré (178 jeux, 1224 codes). **Stables confirmés** : Blox Fruits (24, PCGamesN/PC Gamer — aucun nouveau code depuis l'Update PvP d'été), Steal a Brainrot (1 actif `BESTBRAINROTEVER`, Dexerto/Beebom « un seul code »), Anime Vanguards (3 : Retribution/Wrath/MiniUpd2, tous confirmés actifs), Blue Lock Rivals (3 : UBERSTAKEOVER/KINGNEXTWEEK/EGODEFENSE — les 6 anciens gardés **hors liste par prudence**, conflit sources actif/expiré), Volleyball Legends (3 : UPDATE_85/SHIRO/BLOCKED), King Legacy (7, aucun conflit), Grow a Garden (2 : RDCAward/BEANORLEAVE10). **Résolu** : Fisch `SkycrestNextWeek` **confirmé expiré** (Beebom/Pocket Gamer 1ᵉʳ sept.) — n'avait jamais été publié, candidat clos. **Candidats en attente (prudence)** : Anime Last Stand `MagicKnights!` / `ElfReincarnation!` (nouveaux vus Beebom+PGG+Destructoid 1-2/09 — ajout au prochain run après vérif fine des récompenses, pour ne pas altérer à la légère une liste de 38 codes) ; GAG `torigate` (PCGamesN 29/08 + PGG actif vs Beebom expiré → conflit). « Vérifié le » rafraîchi au **2 septembre** sur les **178 pages**.

**Trending re-scanné :** leaders vérifiés (Steal An Egg #1 ~1,4M CCU, Blox Fruits, Grow a Garden, Steal a Brainrot, Brookhaven, GAG2, Adopt Me) — **tous couverts, aucun nouveau hit ≥4000 non couvert**. Dungeon Quest Reborn toujours **sans système de codes** (état « aucun code » de la fiche confirmé, PCGamesN/PGG 1ᵉʳ sept.) → evergreen.

**Brique réalisée (ÉTAPE 2bis — maillage / autorité des hubs éditoriaux) :** ajout de **liens de découverte réciproques** depuis les **3 hubs servis** (`tous-les-codes.html`, `tier-lists.html`, `guides.html`) vers les **2 hubs éditoriaux** (`meilleurs-jeux-roblox.html`, `nouveaux-jeux-roblox.html`). **Constat corrigé :** seuls les anciens hubs `codes/index.html`, `tier-list/index.html`, `guides/index.html` (legacy, 301-redirigés) pointaient vers l'éditorial — les **pages réellement servies** ne le faisaient pas, laissant les deux hubs éditoriaux sous-maillés côté crawl. Ligne « À découvrir aussi : les meilleurs jeux Roblox et les nouveaux jeux Roblox » insérée sous le chapô de chaque hub. **Intention distincte (anti-cannibalisation) :** navigation/découverte, ≠ codes (transaction) / tier lists (classement) / guides (how-to) ; aucune nouvelle URL, aucune cible de mot-clé dupliquée. **Effet SEO :** consolide le maillage vers deux hubs qui redistribuent l'equity vers 18+ pages jeu du catalogue ; réciprocité complète (les hubs éditoriaux pointent déjà vers les 3 hubs servis via nav + corps). QC : div équilibrés (0), fin `</html>` sur les 3 fichiers.

**Prochaine brique recommandée (J24), par ordre de priorité :**

1. **Anime Last Stand** — ajouter proprement les nouveaux codes `MagicKnights!` / `ElfReincarnation!` après vérif ≥3 sources datées (Beebom + PGG + Fandom wiki), avec récompenses exactes ; c'est un jeu très actif à liste longue, éviter toute régression.
2. **Cluster Dungeon Quest Reborn** — surveiller l'apparition d'un système de codes (Discord officiel) ; sinon enrichir la tier list (armes par donjon / méta Terres du Nord) ou un how-to « meilleur build Mage/Guerrier » sans cannibaliser le guide existant (qui couvre déjà les classes).
3. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J22 (1 septembre 2026)

**Codes (priorité) :** re-scan multi-sources (Beebom, PCGamesN, Pro Game Guides, PC Gamer, GamesRadar). **1 changement appliqué + 2 confirmations.** (1) **Blue Lock Rivals → 3 codes actifs** : les 6 codes du patch précédent (INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!!) ont **expiré** (Beebom màj 1ᵉʳ sept.) ; actifs = **UBERSTAKEOVER, KINGNEXTWEEK, EGODEFENSE** (prose + compteurs + JSON-LD corrigés sur `codes-blue-lock-rivals.html`). (2) **Volleyball Legends** confirmé à **UPDATE_85 / SHIRO / BLOCKED** (Beebom 1ᵉʳ sept.) — déjà à jour. (3) **Anime Vanguards** confirmé à **Retribution / Wrath / MiniUpd2** (PGG 30/08 + PC Gamer) — déjà à jour. **Stables** : Blox Fruits (24, PCGamesN), Grow a Garden (RDCAward/BEANORLEAVE10). **Candidat en attente (prudence)** : Steal a Brainrot `BESTBRAINROTEVER` — PCGamesN (31/08) affirme « aucun code », mais 3 sources l'ont confirmé actif le 30/08 → **gardé actif, à re-vérifier au prochain run**. « Vérifié le » rafraîchi au **1ᵉʳ septembre** + titres/H1 basculés en **(septembre 2026)** sur les **177 pages servies** ; `data/codes.json` régénéré (178 jeux avec DQR).

**Trending re-scanné :** leaders vérifiés (Blox Fruits, Grow a Garden, Steal a Brainrot, Brookhaven, GAG2, Adopt Me, 99 Nights, Steal An Egg, Anime Expeditions) — tous couverts. **Nouveau hit détecté & fiché** : **Dungeon Quest Reborn** (~43,8K CCU, Action RPG, non couvert) → « totale » créée (voir ci-dessous). Aucun autre hit ≥4000 non couvert.

**Brique réalisée (ÉTAPE 1 — nouveau jeu « la totale ») :** **Dungeon Quest Reborn** (universe 9931749389, groupe 496909722, ~43,8K joueurs). 3 pages créées : `codes-dungeon-quest-reborn.html` (~1 690 mots, état « aucun code » honnête et sourcé — le jeu n'a pas de système de codes, comme le Dungeon Quest original ; confirmé PGG + PCGamesN + Destructoid + All Things How ; 2 vidéos oEmbed vérifiées ItsChalls/Cocajola ; bandeau CTA guidelink), `tier-list/dungeon-quest-reborn.html` (armes & capacités : Eden's Vengeance/Reaper, EIR/IEF, Voidspire/Effigy/Hofund ; sources PGG + BloxRant) et `guides/dungeon-quest-reborn.html` (~1 680 mots, 8 sections : classes Mage→Guerrier, donjons+niveaux, leveling/leech, ordre game pass, armes, trading ; sources All Things How + PGG). **Intégration complète** : carte accueil (`GAMES`), `GAMES_INDEX`+`ROBLOX_THUMBS`+`ROBLOX_UNIVERSE_IDS` (main.js, cache **v=40→v=41** site-wide), carte `tous-les-codes.html` + hubs `tier-lists.html`/`guides.html` (vraies miniatures tr.rbxcdn), 4 sitemaps, SVG fallback, liens croisés codes↔tier↔guide. Vraie miniature `tr.rbxcdn.com/180DAY-70c1d4c8…` (768/432 hero, 480/270 cartes).

**Brique SEO complémentaire (cluster Volleyball Legends — information gain) :** ajout d'une section **« Spins & système de pity »** au guide `guides/volleyball-legends.html` (mécaniques de pity 50/200/400, coûts de spins, stratégie 2× Luck, meilleurs styles), intention *how-to* distincte de la tier list, sourcée (Sportskeeda + Dot Esports + wiki VL). Guide passé de ~1 900 à ~2 200 mots, TOC + renumérotation propres, dateModified au 1ᵉʳ sept.

**Prochaine brique recommandée (J23), par ordre de priorité :**

1. **Cluster Dungeon Quest Reborn** — vérifier l'engagement (nouveau jeu très actif) et, si besoin, enrichir la tier list (armes par donjon) ou ajouter une page how-to « meilleur build Mage / Guerrier ». Surveiller l'apparition éventuelle de codes (Discord officiel).
2. **Re-vérifier Steal a Brainrot** `BESTBRAINROTEVER` (conflit PCGamesN) et les jeux chauds non re-vérifiés en profondeur (King Legacy, Fisch, Fruit Battlegrounds, Anime Last Stand, Pet Simulator 99).
3. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J21 (31 août 2026)

**Codes (priorité) :** re-scan multi-sources (progameguides, pcgamesn, pcgamer, gamesradar, beebom). **2 changements appliqués.** (1) **Blue Lock Rivals → 6 codes actifs devient 9** : ajout de **UBERSTAKEOVER, KINGNEXTWEEK, EGODEFENSE** (Pro Game Guides 29/08 liste les 9 actifs + confirmation multi-sources 30/08 ; les 6 anciens INSANETRAILERSOON/DESTROYERMODE/BIGTRAILERSOON/RINTODAY/FIXESLATERTODAY/SORRY4DELAY!! toujours actifs selon PGG). (2) **Anime Vanguards → renouvelé à 3 codes actifs** : anciens (Prepare, 1DayDelay, 25thHour, LetTheLarpingBegin) expirés ; nouveaux **Retribution, Wrath, MiniUpd2** (Holy Retribution, PGG 30/08 recoupé multi-sources ; compteur expirés 22→26). **Stables** : Blox Fruits (24 servis ; « Chandler » ignoré = donne 0 ; `1LOSTADMIN` **confirmé expiré** par PCGamesN → candidat retiré), GAG (RDCAward/BEANORLEAVE10 ; `torigate` conflit PGG actif vs Beebom expiré → gardé **expiré** par prudence), Steal a Brainrot (BESTBRAINROTEVER), Volleyball Legends (Update 85 inchangé). **Candidat en attente (prudence)** : Fisch `SkycrestNextWeek` (agrégateurs 30/08 mais GamesRadar 24/08 ne le liste pas → <3 sources nommées). « Vérifié le » rafraîchi au **31 août** sur les **177 pages servies**. Jeux chauds non re-vérifiés en profondeur ce run (stables au 30/08, à re-prioriser) : King Legacy, Anime Last Stand, Pet Simulator 99, Fruit Battlegrounds, World Fighters, Noob Incremental.

**Trending re-scanné (lundi) :** leaders vérifiés — Steal An Egg #1 (~1,4M CCU), Murder Mystery 2, Brookhaven, Grow a Garden, Steal a Brainrot, +1 Speed Keyboard Escape (=`evasion-clavier`, couvert), Anime Expeditions (couvert). **Aucun nouveau hit ≥4000 non couvert** → evergreen. **Jeu de la semaine** maintenu sur **Steal An Egg** (toujours #1).

**Brique réalisée (ÉTAPE 2bis / maintenance-fraîcheur cluster Volleyball Legends) :** **refonte de `tier-list/volleyball-legends.html`** (méta obsolète du 5 juin 2026 → 31 août 2026). Le cluster Volleyball Legends était déjà **complet** (codes ✓ · tier list ✓ · guide ✓, reliés dans les deux sens) — la reco J21 « créer la tier list » était donc caduque. À la place : **information gain** — ajout d'un **tier S+** avec les deux styles Secret de l'**Update 40** (**Hidari**, capacité « Lefty Arm » ; **Jinko**, all-rounder serve/spike 100 %+) que les concurrents classent désormais au sommet et qui manquaient à notre page ; réorganisation S+/S/A (Timeskip Hinto & Timeskip Kyamo remontés en S+ ; Taichou/Mikage/Kazana ajoutés en S ; Kisuki/Bakuri/Hirakumi en A), 2 nouveaux write-ups FR sourcés, **ItemList** mis à jour (Hidari/Jinko en tête), notice + date + og:description rafraîchis. **Sources (≥2, datées)** : Pocket Gamer (04/08) + findingDulcinea (méta sept. 2026, stats détaillées). **Anti-cannibalisation** : aucune nouvelle URL, page existante mise à jour (intention *classement* inchangée). **EEAT** : classement daté + « recoupé Pocket Gamer + findingDulcinea » + caveat évolutivité.

**Prochaine brique recommandée (J22), par ordre de priorité :**

1. **Guide how-to Volleyball Legends « comment obtenir les meilleurs styles / spins / pity »** — le guide existe mais peut être approfondi (mécaniques de spin, pity 200, 2× Secret le week-end, meilleurs styles par poste) : intention *how-to* distincte de la tier list. OU cluster **Anime Vanguards** (fiche codes très active « Holy Retribution ») : vérifier existence tier list/guide dédiés et compléter le maillon manquant.
2. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable ; sinon reporter.
3. **Hub éditorial** enrichir « Nouveaux jeux Roblox (2026) » (Steal An Egg, Animal Hospital, GAG2, Anime Expeditions) — maillage transversal.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J20 (30 août 2026)

**Codes (priorité) :** re-scan multi-sources (gamesradar, progameguides, beebom, pcgamer, pcgamesn, twinfinite, roonby, dexerto). **1 changement appliqué : Volleyball Legends → Update 85.** Nouveaux actifs **UPDATE_85 / SHIRO / BLOCKED** (confirmés ≥4 sources : gamesradar, progameguides, twinfinite, roonby « UPDATE 85 ») ; les anciens **UPDATE_84 / SEASON_18 / PIRATE_SZN** passés en expirés (compteur expirés 15→18, prose « Dernière mise à jour » au 30/08). Reste **stable** : Blue Lock Rivals (6 codes, match), Steal a Brainrot (BESTBRAINROTEVER confirmé actif gamesradar/dexerto/beebom), GAG (RDCAward/BEANORLEAVE10 actifs), Blox Fruits (24 servis, inchangé). **Candidats en attente (prudence)** : GAG `FREESEED` (rapporté glitché) ; Blox Fruits `1LOSTADMIN` (1 seule source) ; GAG `torigate` (report). « Vérifié le » rafraîchi au **30 août** sur les **177 pages servies** ; `data/codes.json` régénéré (177 jeux, 1228 codes).

**Trending re-scanné :** leaders vérifiés (Steal An Egg #1 ~1,4M CCU, Murder Mystery 2, Brookhaven, Grow a Garden, +1 Speed Keyboard Escape [couvert = `evasion-clavier`], Anime Expeditions) — **aucun nouveau hit ≥4000 non couvert** → on clôt le cluster.

**Brique réalisée (ÉTAPE 2bis / cluster Anime Origins — guide complet, 3ᵉ et dernière pièce) :** nouveau **`guides/anime-origins.html`** (~2 250 mots FR, gabarit `guides/anime-last-stand.html`).
- **Intention distincte (anti-cannibalisation) :** « guide anime origins / comment évoluer / meilleure équipe / comment farmer » — intention *how-to*, distincte de la fiche codes (transactionnelle) et de la tier list (classement). Aucune page existante ne visait cette intention.
- **Contenu à information gain :** TOC ancré 8 sections ; **ordre de progression optimal** (Story Normal→Hard→Legend Stages→Challenges→évolution→modes avancés) ; route d'évolution Vegita (Halo/Power Scouters + Remnants) ; **tableau équipe débutant** (6 rôles) ; **tableau priorités ressources** (Gems/Trait Rerolls/Stat Prisms/Remnants/Or/Fusion Cores) ; **tableau modes avancés** (Raids/Rifts/Infinite Mansion/World Bosses + point d'entrée) ; 8 erreurs à éviter ; FAQ 5 Q. Schema **Article + BreadcrumbList + FAQPage** (3 blocs valides).
- **EEAT/honnêteté :** byline « L'équipe Zoneblox » + politique éditoriale ; **sources datées recoupées** (Pocket Tactics 20/08 + Pro Game Guides + Sportskeeda + guide débutant LDPlayer 26/08) ; encart « version fin août 2026, taux/récompenses évoluent → vérifier en jeu » ; rien d'inventé.
- **Maillage (anti-orphelin) :** carte hub `guides.html` (`.card`) **et** `guides/index.html` (`.g-card` + ItemList position 45 + map CATS `anime`, vraie miniature tr.rbxcdn.com) ; `sitemap-guides.xml` + `sitemap.xml` ; **liens croisés bidirectionnels** : fiche `codes-anime-origins.html` (bouton hero « 📖 Guide complet ») + tier list `tier-list/anime-origins.html` (bouton hero « 📖 Guide complet ») → guide, et guide → codes + tier list (CTA + « articles liés »).

Le cluster Anime Origins est désormais **COMPLET** : **fiche codes ✓ · tier list ✓ · guide complet ✓** (codes↔tier↔guide reliés dans les deux sens).

**Prochaine brique recommandée (J21), par ordre de priorité :**

1. **Cluster Volleyball Legends** — la fiche codes est très active (Update 85) mais le jeu n'a ni tier list ni guide complet dédiés. Créer **`tier-list/volleyball-legends.html`** (meilleurs personnages/styles, intention *classement* distincte de la fiche codes) ou le guide how-to ; fort trafic saisonnier. Sourcer ≥2 (gamesradar/progameguides/fandom).
2. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable.
3. **Hub éditorial** enrichir « Nouveaux jeux Roblox (2026) » (Animal Hospital, Steal An Egg, GAG2, Anime Expeditions) — maillage transversal.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J19 (29 août 2026)

**Codes (priorité) :** re-scan multi-sources (pcgamesn, gamesradar, progameguides, beebom, pcgamer) sur les jeux chauds — **tout stable, identique au 28/08**, aucun changement de codes appliqué. Blox Fruits (24, sync pcgamesn incl. Lightningabuse), Blue Lock Rivals (6, match PC Gamer), Volleyball Legends (3, match), GAG (2 actifs). Conflit GAG « torigate » (zoneblox=expiré vs 4 sites=actif) → gardé **expiré par prudence** (en attente, code cosmétique event que les sites laissent traîner). « Vérifié le » rafraîchi au **29 août** sur les **177 pages servies**.

**Trending re-scanné :** leaders vérifiés contre le catalogue — aucun nouveau hit ≥4000 non couvert. On continue l'evergreen.

**Brique réalisée (ÉTAPE 2bis / cluster Anime Origins — tier list) :** nouvelle **`tier-list/anime-origins.html`** (~1 910 mots FR).
- **Intention distincte (anti-cannibalisation) :** « anime origins tier list » / « meilleures unités anime origins » — intention *classement*, distincte de la fiche codes (transactionnelle). Aucune page existante ne visait cette intention ; le report récurrent « ficher Anime Origins » (J17→J19) était **obsolète** : `codes-anime-origins.html` existe déjà (dans GAMES_INDEX, ~1 880 mots).
- **Contenu à information gain :** classement complet **SS→C** (51 unités) recopié depuis Pocket Tactics ; write-ups FR détaillés des 13 unités SS+S ; section **meilleurs traits** (Immortal/Overseer/Rupture/Decay/Hustler/Looting/Scholar/Hawkeye) ; meilleure équipe + conseils débutants ; FAQ 5 Q. Schema **ItemList + BreadcrumbList + FAQPage** (3 blocs valides).
- **EEAT/honnêteté :** byline « L'équipe Zoneblox » + politique éditoriale ; **source principale datée** Pocket Tactics (20/08/2026) **recoupée** avec Sportskeeda + Pro Game Guides ; caveat « noms d'unités variables selon les sites, vérifier en jeu » ; rien d'inventé (descriptions génériques là où pas de spécificité sourcée ; specifics Valcrad sourcés).
- **Maillage (anti-orphelin) :** carte hub `tier-lists.html` (vraie miniature tr.rbxcdn.com), `sitemap-tier-list.xml` + `sitemap.xml` ; **lien croisé** fiche `codes-anime-origins.html` (bouton hero « 📊 Tier list Anime Origins ») ↔ tier list (bouton hero « 🎁 Voir les codes »).

Cluster Anime Origins : **fiche codes ✓ · tier list ✓** · guide complet ✗ (candidat J20).

**Prochaine brique recommandée (J20), par ordre de priorité :**

1. **Guide complet `guides/anime-origins.html`** (gabarit `guides/blox-fruits.html`) — clôt le cluster Anime Origins (codes↔tier↔guide). Intention *how-to* (« comment jouer / farmer / évoluer / meilleure équipe Anime Origins ») distincte de la fiche codes et de la tier list. Relier hub `guides.html` + sitemaps + boutons croisés.
2. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable.
3. **Hub éditorial** enrichir « Nouveaux jeux Roblox (2026) » (Animal Hospital, Steal An Egg, GAG2, Anime Expeditions) — maillage transversal.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J18 (28 août 2026)

**Trending re-scanné (web, multi-sources) :** leaders vérifiés contre le catalogue — Murder Mystery 2 (~1M CCU, couvert), Grow a Garden (couvert), Steal a Brainrot (couvert), Brookhaven (couvert), **Animal Hospital** (~350K CCU, couvert), Anime Expeditions (couvert), Steal An Egg (couvert), GAG2 (couvert). **Aucun nouveau hit ≥4000 non couvert** → on termine le cluster porteur (règle evergreen).

**Brique réalisée (ÉTAPE 2bis / cluster Steal An Egg — 3ᵉ et dernière pièce) :** nouveau **`guides/steal-an-egg.html`** (~2 140 mots FR, gabarit `guides/blox-fruits.html`).
- **Intention distincte (anti-cannibalisation) :** « guide steal an egg » / « comment jouer steal an egg » / « comment augmenter vitesse » / « rebirth steal an egg » — intention *how-to*, distincte de la fiche codes (transactionnelle) et de la tier list (classement). Aucune page existante ne visait cette intention.
- **Contenu à information gain :** TOC ancré 10 sections ; **table des 9 biomes et seuils de vitesse** (Forest→Cosmic : Lake 900 … Cosmic 700 M) ; treadmill vs base (piège classique), 10 trails ; reset œufs 5 min + fermeture 13 s ; gardiens = contrôles de vitesse ; pets (78, taille+mutations=revenu) ; outils de vol PvP (batte, piège à ours) ; **Rebirth** (+5 %/palier, vitesse 150 = ×2 mutation Legendary) ; ordre de progression optimal + erreurs classiques ; FAQ 6 Q. Schema **Article + BreadcrumbList + FAQPage**.
- **EEAT/honnêteté :** byline « L'équipe Zoneblox » + politique éditoriale ; **2 sources datées** (All Things How / Sehaj Padda 16/08/2026 + Sportskeeda) ; encarts « valeurs communautaires susceptibles d'évoluer → vérifier en jeu » ; aucune valeur inventée.
- **Maillage (anti-orphelin) :** carte hub `guides.html` (vraie miniature tr.rbxcdn.com), `sitemap-guides.xml` + `sitemap.xml` ; **liens croisés bidirectionnels** : fiche `codes-steal-an-egg.html` (bouton CTA `data-cta="guidelink"` → guide) ↔ guide ↔ tier list `tier-list/steal-an-egg.html` (bouton hero « Guide complet » ajouté).

Le cluster Steal An Egg est désormais **COMPLET** : **fiche codes ✓ · tier list pets ✓ · guide complet ✓** (codes↔tier↔guide reliés dans les deux sens).

**Prochaine brique recommandée (J19), par ordre de priorité :**

1. **Ficher Anime Origins** (report récurrent depuis le 23/08) — vérifier éligibilité ≥4000, miniature réelle (Chrome/API), codes (≥3 sources ou officiel), guide 6 astuces + 2 vidéos oEmbed ; intégrer hub/sitemap/GAMES_INDEX. Élargit la couverture d'entités anime.
2. **Value/trading list** (Steal An Egg pets ou GAG2 graines) uniquement si la maintenance quotidienne des valeurs datées (≥2 sources) est tenable ; sinon reporter.
3. **Hub éditorial « Nouveaux jeux Roblox (2026) »** (intention *nouveauté* ≠ *popularité*) ciblant Animal Hospital, Steal An Egg, GAG2, Anime Expeditions — maillage transversal, complète le cluster hub.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J17 (26 août 2026)

**Trending re-scanné (web, multi-sources) :** leaders du moment vérifiés contre le catalogue — Murder Mystery 2 (~1M CCU, couvert), **Steal An Egg** (#1 trending, ~724K CCU, couvert), +1 Speed Keyboard Escape (~500K CCU, **déjà couvert** sous le slug FR `evasion-clavier`), Anime Expeditions (couvert). **Aucun nouveau hit ≥4000 non couvert** → on approfondit le cluster porteur (règle evergreen).

**Brique réalisée (ÉTAPE 2bis / cluster Steal An Egg) :** nouvelle **`tier-list/steal-an-egg.html`** (~2 317 mots FR).
- **Intention distincte (anti-cannibalisation) :** « steal an egg tier list » / « meilleur pet steal an egg » / « steal an egg best pets » — intention *classement*, distincte de la fiche codes (transactionnelle) du même jeu. Aucune tier list existante ne visait ce jeu.
- **Contenu à information gain :** classement S/A/B **par revenu/seconde** (Unicorn Divine ~1 Md/s → Eternal dragons → paliers Legendary réalistes), **tableau meilleur pet par biome** (Forest→Cosmic), section début de partie, encart **honnêteté mutations** (multiplicateurs non publiés → renvoi à l'UI en jeu), section Rebirth, FAQ 5 Q. Schema **ItemList + BreadcrumbList + FAQPage**.
- **EEAT/honnêteté :** byline « L'équipe Zoneblox » + politique éditoriale ; sources datées (**index communautaire IGN via timesaver.gg, relevé 21–24/08/2026** + corroboration bloxspot/stealthygaming/ldplayer/eldorado — ≥2 sources) ; distinction claire info officielle / valeurs communautaires / non publié ; note d'évolutivité (jeu très récent).
- **Maillage (anti-orphelin) :** carte + entrée JSON-LD ItemList du hub `tier-list/index.html` (vraie miniature tr.rbxcdn.com), `sitemap-tier-list.xml` + `sitemap.xml`, **liens croisés** fiche `codes-steal-an-egg.html` (nouveau bandeau CTA `data-cta="guidelink"` + lien « jeux similaires ») ↔ tier list, bouton hero « Voir la fiche ».
- **Bonus fiche :** ajout du bandeau CTA `data-cta="guidelink"` qui manquait sur `codes-steal-an-egg.html`.

Le cluster Steal An Egg compte désormais : **fiche codes ✓ · tier list pets ✓** (reste : guide complet).

**Prochaine brique recommandée (J18), par ordre de priorité :**

1. **Guide complet Steal An Egg** (`guides/steal-an-egg.html`, gabarit `guides/blox-fruits.html`) : how-to progression (Speed/treadmill, ordre des biomes Forest→Cosmic, quand Rebirth, mutations, vol PvP) — 3ᵉ brique du cluster, relie fiche ↔ tier ↔ guide. Sourcer ≥2 (IGN + timesaver/Beebom).
2. Ficher **Anime Origins** (report récurrent depuis le 23/08).
3. **Value list** (Steal An Egg ou GAG2) uniquement si la maintenance des valeurs datées (≥2 sources) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 📌 Archive — J16 (24 août 2026)

**Trending re-scanné (web, multi-sources) :** découverte d'un **nouveau hit majeur non couvert** — **Steal An Egg** (créé le 25/07/2026, ~496K–724K joueurs simultanés selon les trackers, 284M visites, genre Simulation/Tycoon). Conforme à la règle « un vrai nouveau hit ≥4000 joueurs passe DEVANT l'evergreen », il a été fiché en priorité.

**Brique réalisée (ÉTAPE 1, trending-first) :** nouvelle fiche **`codes-steal-an-egg.html`** (~1 650 mots FR).
- **Honnêteté codes :** le jeu **n'a pas de système de codes public** (PGG 17/08 + description in-game + shout du groupe créateur = null). La page l'affiche clairement (« Aucun code public ») au lieu d'inventer — et explique où les codes apparaîtraient s'ils existaient.
- **Intention ciblée distincte :** « codes Steal An Egg » / « Steal An Egg a-t-il des codes » (intention transactionnelle + réassurance), aucune cannibalisation (aucune page existante ne visait ce jeu).
- **Contenu :** « C'est quoi », « Comment jouer » (biomes, gardiens, vitesse/treadmill, éclosion, revenu/s, fusion 3→1, mutations, vol PvP), <h3>Guide de progression</h3> avec 8 astuces, 2 vidéos réelles vérifiées oEmbed (CHALLS `8d7Qrz7jDrU`, Radex Tips `aTV1JJpHUXY`), « Où trouver les codes », À propos + 3 similaires, FAQ 4 Q. Schema Breadcrumb + FAQPage.
- **Miniature réelle** tr.rbxcdn.com (universeId 10563114921 vérifié via games.roblox.com = « Steal An Egg »), SVG fallback créé.
- **Maillage (anti-orphelin) :** carte `tous-les-codes.html` + objet `index.html` (GAMES) + `js/main.js` (GAMES_INDEX + ROBLOX_THUMBS + ROBLOX_UNIVERSE_IDS) + `sitemap.xml` + redirect `.htaccess`. **Jeu de la semaine (lundi)** pointé sur Steal An Egg.

**Prochaine brique recommandée (J17), par ordre de priorité :**

1. **Tier list Steal An Egg** (`tier-list/steal-an-egg.html`) : classement des **pets / œufs / biomes** par revenu-par-seconde (intention « meilleurs pets Steal An Egg », distincte de la fiche) → approfondit immédiatement le nouveau cluster porteur. Sourcer ≥2 (wiki + Beebom/PGG).
2. **Guide complet Steal An Egg** (`guides/steal-an-egg.html`) : how-to progression (vitesse, biomes, fusion, mutations, PvP) — complète le cluster, relie fiche ↔ tier ↔ guide.
3. Ficher **Anime Origins** (report du 23/08, à faire avec Chrome).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

## 1. Décision stratégique validée

Le mandat déclarait l'anglais en langue primaire, mais le site réel est **100 % français** (`html lang="fr"`, ~300 pages indexées, dossier `en/` réduit à 3 fichiers). Décision prise avec Peter : **rester français-first**. Raison SEO : la SERP Roblox anglophone est saturée d'acteurs très établis (Pro Game Guides, Beebom, Pocket Tactics, GamesRadar, Dexerto). Le français est un marché où ZoneBlox a déjà de l'autorité et bien moins de concurrence — c'est là que le ROI marginal est le plus élevé. L'anglais reste une phase ultérieure (via `/en/` + hreflang propre), pas une priorité 2026.

---

## 2. État des lieux (audit de couverture)

| Cluster | Pages | Lecture SEO |
|---|---|---|
| Codes | 173 | Colonne vertébrale du site, rafraîchie quotidiennement. Solide. |
| Tier lists | 65 → **66** | Bon maillage, vraies miniatures. Peu de sous-tier-lists par jeu (opportunité). |
| Guides complets | 56 | Piliers longs (ex. Blox Fruits 2 556 mots). Qualité correcte. |
| Encart évènements | 1 (accueil) | Nouveau : comptes à rebours restocks/admin abuses (GAG, Steal a Brainrot). |

**Forces** : fraîcheur (run quotidien), maillage codes↔tier↔guide, honnêteté éditoriale (règles anti-invention), vraies miniatures Roblox, JSON-LD présent.

**Faiblesses / dettes** :
1. **Profondeur de cluster faible.** Chaque jeu = ~3 pages (codes/tier/guide). Les jeux phares méritent des sous-entités (races, awakening, value list, boss, builds) — c'est là que se gagne l'autorité topicale.
2. **Risque de cannibalisation** si on fragmente mal : les guides piliers couvrent déjà beaucoup de sous-sujets en H2. Toute sous-page doit cibler une **intention distincte** (ex. « tier list des races » ≠ « guide »), et s'interlier au pilier.
3. **Intentions éditoriales/hub non couvertes** : « meilleurs jeux Roblox », « nouveaux jeux Roblox », « jeux Roblox tendance », value lists / trading — fort volume, peu ou pas présents.
4. **Anglais** : `en/` orphelin (3 pages) — soit l'assumer plus tard proprement, soit le retirer de l'index pour éviter du thin content.

---

## 3. Analyse « trending » (avant tout evergreen)

Vérifié ce jour : les leaders actuels sont **déjà couverts** (Grow a Garden 2 #1, Steal a Brainrot, 99 Nights in the Forest, Animal Hospital, Brookhaven, Blox Fruits). **Pas de gros jeu neuf non couvert** à ce run. Conséquence : la priorité du jour bascule légitimement de « nouveau jeu » vers **approfondissement des clusters phares** (conforme à la règle « si rien de neuf, améliore l'existant »). À re-vérifier chaque jour — un nouveau hit Roblox peut surgir en 48 h.

---

## 4. Scoring des opportunités (framework ROI)

Score = Potentiel trafic (1-5) × Valeur topicale (1-5) − Difficulté (1-5), pondéré par Fraîcheur. Top opportunités :

| # | Opportunité | Trafic | Autorité | Difficulté | Priorité | Statut |
|---|---|:--:|:--:|:--:|:--:|---|
| 1 | **Blox Fruits — sous-cluster** (races ✓, value list, awakening en page dédiée, best build) | 5 | 5 | 2 | **★★★★★** | Races **FAIT aujourd'hui** |
| 2 | Hub éditorial « Meilleurs jeux Roblox (mois) » + « Nouveaux jeux Roblox » | 5 | 4 | 3 | ★★★★☆ | À faire |
| 3 | Value / Trading lists (Blox Fruits, Adopt Me, Murder Mystery 2, Grow a Garden) | 5 | 4 | 3 | ★★★★☆ | À faire (maintenance requise) |
| 4 | Sous-tier-lists par jeu phare (Blox Fruits swords, GAG pets/seeds, AV units) | 4 | 4 | 2 | ★★★★☆ | Swords **FAIT le 25/07** ; GAG pets/seeds + AV units à faire |
| 5 | Cluster « comment awaken / débloquer » (verbes d'intention) sur top jeux | 4 | 4 | 2 | ★★★☆☆ | À faire |
| 6 | Nettoyage `en/` orphelin (noindex ou plan hreflang) | 2 | 3 | 1 | ★★★☆☆ | À arbitrer |
| 7 | Grow a Garden — cluster (mutations, weather, calculator, value) | 5 | 5 | 3 | ★★★★☆ | Tier list **pets GAG2 FAITE le 26/07** ; mutations + value à faire |

---

## 5. Travail exécuté aujourd'hui

**Nouvelle page : `tier-list/blox-fruits-races.html`** (Blox Fruits Race Tier List, juillet 2026).
- **Intention distincte** ciblée : « meilleure race blox fruits », « blox fruits race tier list », « blox fruits v4 » — sans cannibaliser le guide (qui garde l'intention how-to) ni la tier list des fruits.
- Classement sourcé (multi-sources : ssegold, bloxfruitsai, gamingpromax, poxelio) : S = Draco, Ghoul · A = Cyborg, Angel, Rabbit · B = Human, Shark · C = Mink. Nuances honnêtes (Shark = S pour le farm en mer).
- 2 009 mots, sections « meilleure race par objectif », « débloquer le V4 » (prérequis marqués comme évolutifs → renvoi wiki, aucune invention), FAQ 6 questions.
- **EEAT** : byline équipe, politique éditoriale liée, ton d'expérience réelle.
- **Schema** : ItemList + BreadcrumbList + FAQPage (tous validés).
- **Maillage** : carte ajoutée au hub `tier-lists.html` ; boutons + « articles liés » croisés depuis `tier-list/blox-fruits.html` ; liens sortants vers codes + guide Blox Fruits ; entrées ajoutées à `sitemap-tier-list.xml` et `sitemap.xml`.
- **QC** : 0 null byte, `</html>` OK, `<div>`/`<section>` équilibrés, GA4, nav 7 entrées, `main.js?v=35`.

Effet топ­ique : renforce le **hub Blox Fruits** (codes ↔ tier fruits ↔ **tier races** ↔ guide) et distribue de l'equity interne — la page sert tout le cluster, pas seulement elle-même.

---

## 6. Roadmap 30 jours (français-first)

**Semaine 1 — Approfondir Blox Fruits (jeu-modèle du sous-cluster)**
- J1 : Tier list des races ✓ (fait).
- J2/J3 : Blox Fruits **Sword Tier List** ✓ (fait le 25/07). Choix de la brique la plus **stable** (classement de puissance, pas de valeurs fluctuantes à maintenir), conforme au repli recommandé en section 7. Intention « best sword blox fruits » / « meilleure épée blox fruits », distincte de la tier list des fruits (fruits) et des races (races) → aucune cannibalisation. Interliée aux 3 autres pages du cluster (fruits, races, guide, codes).
- J4 : Blox Fruits **Value List** (valeurs de trading) — reportée : n'entreprendre que si l'engagement de maintenance quotidienne (redate + resource des valeurs, ≥2 sources) est tenable. Sinon enchaîner sur GAG (semaine 2).
- J4 : Page « comment awaken » dédiée si le volume le justifie, sinon renforcer la section du pilier + interliens.
- J5 : Audit interne du cluster Blox Fruits (anti-orphelin, anti-cannibalisation, ancres descriptives).

**Semaine 2 — Répliquer le modèle sur Grow a Garden (jeu #1)**
- Mutations (liste + valeurs), pets/seeds tier list, calculateur/valeur, guide events (relié à l'encart). GAG est le plus gros trafic actuel : priorité maximale en volume.

**Semaine 3 — Hubs éditoriaux à fort volume**
- « Meilleurs jeux Roblox (mois) », « Nouveaux jeux Roblox », « Jeux Roblox tendance » : pages hub qui **redistribuent l'equity** vers 30-50 pages jeu et captent des head terms. Fort effet crawl + maillage.

**Semaine 4 — Steal a Brainrot + hygiène technique**
- Sous-cluster Steal a Brainrot (brainrots value/tier, admin abuse guide relié à l'encart). Puis hygiène : arbitrage `en/` (noindex ou plan hreflang), audit liens internes global, pages fines < 1200 mots à étoffer.

**Principe permanent** : chaque jour, (1) re-scan trending → si nouveau hit, il passe devant l'evergreen ; (2) sinon, avancer d'une brique le cluster prioritaire ; (3) jamais d'orphelin, toujours interlier au hub.

---

## 7. Suggestion pour demain (J14 — 23/08)

**Run du 23/08/2026 — priorité codes (ÉTAPE 2) puis nouvelle brique de contenu cluster GAG.** Priorité absolue tenue : re-vérification web (≥3 sources / sources officielles) des jeux chauds sur l'arbre **servi** `codes-<slug>.html`. Résultat : jeux chauds **déjà à jour** depuis le run du 22/08 — Anime Vanguards (6 actifs, Miniupdate1/2BVisits/Prepare/1DayDelay/25thHour/LetTheLarpingBegin), Volleyball Legends (UPDATE_83/MIKAGE_REVIVED/SCHOOL_SOON, confirmés Aug 22), Blue Lock Rivals (SAEREWORK/HALFBAKED/RINSOON/SAERRY4DELAY, match exact PGG/Beebom/GamesRadar/RoCodes), Fisch (SCARLET/TemporarySubmarine/CARBON confirmés long-lived), Blade Ball, Fruit Battlegrounds, King Legacy — **inchangés par prudence**, aucun signal d'expiration multi-sources. Date « 🔄 Vérifié le » rafraîchie au **23 août 2026** sur les **176 pages servies**. Steal a Brainrot : sources en conflit fort (1 à 23 codes selon la source) → maintien de l'état prudent (aucun code publié). **Note technique** : un `.git/index.lock` résiduel bloque les écritures git dans l'environnement — **Peter doit le supprimer** (`del .git\index.lock`) avant `git add`/`commit`. L'arbre legacy `codes/` (301-redirigé) a été laissé **gelé** (aucune modification, conformément à la décision d'arbitrage en attente).

**Brique de cluster (nouveau contenu — ÉTAPE 5)** : création du guide how-to **`guides/grow-a-garden-pets.html`** (« Pets Grow a Garden : œufs, éclosion & meilleurs pets », ~1 656 mots). **Intention distincte ciblée** : « grow a garden pets », « meilleurs pets grow a garden », « comment faire éclore œuf grow a garden », « grow a garden eggs guide » — intention *how-to sur l'obtention/éclosion des pets*, **complémentaire mais distincte** de la *tier list pets GAG2* (`tier-list/grow-a-garden-2-pets.html`, qui classe les pets par puissance) et du *guide mutations* (qui liste les multiplicateurs). **Anti-cannibalisation** : aucune page existante ne visait ces head terms « pets/œufs » ; liens réciproques explicites pets ↔ mutations ↔ tier list pets GAG2. **Contenu** : rôle des pets (éclosion/mutation/revenu/utilitaire), mécanique d'éclosion (tirage pondéré, hors ligne, Chicken/Blood Kiwi réducteurs de temps), types d'œufs (Common→Mythical + œufs d'événement), meilleurs pets par objectif (Blood Kiwi éclosion, Dragonfly/Golden Bee Or, Butterfly Arc-en-ciel, Raccoon argent), stratégie de progression, FAQ 6 questions. **EEAT/honnêteté** : byline « L'équipe Zoneblox », encart « info communautaire évolutive » (wiki/Beebom/gagdata, daté août 2026, renvoi wiki), aucun taux/valeur inventé (catégories d'œufs présentées comme repère de progression, pas un tableau de pourcentages figé). **Schema** Article + BreadcrumbList + FAQPage (validés). **Maillage (anti-orphelin)** : carte ajoutée au hub `guides/index.html` (vraie miniature tr.rbxcdn.com) + ItemList (position 47), liens croisés vers codes servis (`/codes-grow-a-garden.html`) / tier list graines / tier list pets GAG2 / guide complet / mutations, + lien réciproque depuis `guides/grow-a-garden-mutations.html`, entrées `sitemap-guides.xml` et `sitemap.xml`. **Effet SEO** : le cluster Grow a Garden gagne une 7ᵉ brique (codes ✓ · guide complet ✓ · tier graines ✓ · GAG2 pets tier ✓ · mutations ✓ · météo ✓ · **pets how-to ✓**) et couvre l'intention how-to « pets/œufs » à fort volume.

**Trending re-scanné** (web ≥3 sources) : leaders (Murder Mystery 2 — pic all-time, couvert ; Grow a Garden/2, Steal a Brainrot, Brookhaven, Anime Expeditions, Animal Hospital) tous couverts. Aucun nouveau hit ≥4000 joueurs non couvert (Fusion Piece ~6 joueurs, négligeable). Candidats toujours en attente d'un run avec Chrome : **Anime Origins** et **+1 Speed Keyboard Escape**.

Prochaine brique recommandée (J15), par ordre de priorité :

1. **Ficher Anime Origins** (Étape 1) lors d'un run avec Chrome connecté (miniature réelle tr.rbxcdn.com + éligibilité ≥4000 + codes ≥3 sources) — hit anime TD en croissance non couvert.
2. **Arbitrage Peter** : trancher l'arbre codes à conserver (servi `codes-<slug>.html`), puis brique technique (CTA `guidelink` + nav 7 entrées homogènes + gel/suppression de l'arbre `codes/`).
3. **Guide GAG « calculateur / valeur »** ou **value list graines** — uniquement si la maintenance quotidienne des valeurs (≥2 sources datées) est tenable ; sinon poursuivre un autre cluster phare (Blox Fruits awakening how-to, Steal a Brainrot brainrots).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J13 (22/08)

**Run du 22/08/2026 — priorité codes (ÉTAPE 2) puis brique de maillage cluster GAG.** Priorité absolue tenue : re-vérification web (≥3 sources) des jeux chauds. **Réconciliation majeure Anime Vanguards** (report des runs précédents, sources en conflit) tranchée grâce à deux sources récentes concordantes (GamesRadar & Beebom, MAJ 17/08) : la page servie passe de **16 → 6 codes actifs**. Ajout des 3 codes confirmés actifs par ≥3 agrégateurs (Miniupdate1, 2BVisits — expirent le 23/08 —, Prepare) ; conservation des 3 encore listés actifs par Beebom/PGG (1DayDelay, 25thHour, LetTheLarpingBegin) ; **13 codes déplacés en « expirés »** (WhoopsieDaisy, LateBP, PowerOfLove, EEPart1, BPSoon, LagGone, 13.5, EternalAdversaries, Gambler, DMCAFree, Liberation, 223, Cog5th) — dont un **bug de doublon corrigé** (6 codes figuraient à la fois en actifs et en expirés). Carte du hub `tous-les-codes.html` resynchronisée (compteur + date + mois). Autres jeux chauds (Fisch, Blade Ball, Grow a Garden/GAG2, Anime Last Stand, Fruit Battlegrounds) : sources trop fluides ou conflit GAG/GAG2 → **inchangés par prudence**, candidats notés. **Brique de cluster (maillage / anti-orphelin)** : sur `codes-grow-a-garden.html` (page GAG la plus trafiquée), **correction d'un lien mort** (« Guide débutant » pointait vers `#`) → `guides/grow-a-garden.html`, et **ajout de 2 liens profonds** vers `guides/grow-a-garden-mutations.html` et `guides/grow-a-garden-weather.html`. Effet : la page codes redistribue désormais de l'equity vers 3 pages how-to profondes du cluster GAG (au lieu d'un lien générique cassé). **Anti-cannibalisation** : aucune nouvelle page, ancres distinctes (tier list / mutations / météo) → nulle. **Trending re-scanné** (web) : leaders (Murder Mystery 2, Grow a Garden/2, Steal a Brainrot, Brookhaven, Anime Expeditions) tous couverts. Deux hits éligibles NON couverts — **Anime Origins** (anime TD, codes déjà suivis par Beebom/GamesRadar/PGG) et **+1 Speed Keyboard Escape** (~500K CCU, 3,8 Md visites) — mais **impossible de créer une fiche conforme ce run** (Chrome non connecté + shell sans réseau → API miniatures Roblox inaccessible ; règle absolue « jamais de SVG en miniature affichée »). À ficher lors d'un run avec accès Chrome.

**Constat structurel (rappel à Peter, non tranché autonome)** : les 171 pages **servies** `codes-<slug>.html` n'ont **aucun** bandeau `data-cta="guidelink"` et lient un hub générique `guides.html` (jamais le guide spécifique), contrairement à l'arbre `codes/` (legacy, 301-redirigé) qui, lui, respecte le gabarit. La nav servie compte **6 entrées** (sans « À propos »). Ces écarts découlent de la divergence des deux arbres (déjà remontée) : à corriger en masse **seulement après** que Peter ait tranché quel arbre garder — un mass-edit des 171 pages servies serait risqué et prématuré tant que l'arbitrage n'est pas fait.

Prochaine brique recommandée (J14), par ordre de priorité :

1. **Arbitrage Peter requis puis brique technique** : décider de ne conserver QUE l'arbre servi `codes-<slug>.html`, puis (a) y ré-injecter le bandeau CTA `data-cta="guidelink"` + liens guide spécifiques, (b) porter la nav à 7 entrées (ajout « À propos »), (c) geler/supprimer l'arbre `codes/` redondant. Fort impact honnêteté + maillage.
2. **Ficher Anime Origins** (Étape 1) lors d'un run avec Chrome connecté (miniature réelle tr.rbxcdn.com + éligibilité + codes ≥3 sources) — c'est un hit anime TD en croissance non couvert.
3. **Réconcilier Fruit Battlegrounds** (paliers récents BIG1M170K!!, OPE V2… à trancher ≥3 sources) et **Anime Last Stand** (liste active exacte).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J12 (21/08)

**Run du 21/08/2026 — brique EEAT « FAQPage ↔ FAQ visible » (report J10/J11 réalisé) :** priorité codes d'abord (vérif web ≥3 sources des jeux chauds : Blox Fruits, Blue Lock Rivals, Volleyball Legends, Anime Vanguards → stables ; **Steal a Brainrot : ajout de `BESTBRAINROTEVER`**, seul code actif confirmé par ≥5 sources fiables — la page servie passait à tort de 0 à 1 code, carte hub + snapshot resynchronisés). Puis **brique de cluster substantielle : alignement du `FAQPage` JSON-LD sur la FAQ VISIBLE des 171 pages codes servies.** Depuis le J10, le JSON-LD portait le bon nom de jeu mais **3 questions génériques ne correspondaient pas à la FAQ affichée** (ex. Blox Fruits : JSON-LD « …les codes sont-ils *ajoutés* ? » vs visible « …*vérifiés* ? » ; réponse Q1 JSON-LD « menu Paramètres » vs visible « zone dédiée aux codes ») → non-conformité Google FAQ (le balisage doit refléter le contenu visible). **Correction (script Python validé)** : pour chaque page, extraction des paires question/réponse visibles (`<div class="q">…<div class="a">`), nettoyage des balises internes + décodage des entités, reconstruction du `mainEntity` du bloc `FAQPage` à l'identique du visible. **QC** : `json.loads` OK sur les 171 blocs réécrits + tous les autres blocs ld+json ; 0 null byte ; toutes finissent par `</html>` ; équilibre `<div>` intact ; `BreadcrumbList` non touché. **Effet SEO/EEAT** : données structurées FAQ désormais conformes (JSON-LD = contenu visible) sur tout le catalogue codes servi → éligibilité rich-results restaurée, transversal, **sans création de page** (anti-cannibalisation nulle). **Intention ciblée** : renforcement de la couverture SERP (FAQ rich results) des pages transactionnelles « codes <jeu> », sans empiéter sur guides (how-to) ni tier lists (classement). **Trending re-scanné** (web) : Grow a Garden, Steal a Brainrot, Brookhaven en tête — tous couverts (Anime Expeditions est déjà fiché : `codes-anime-expeditions.html`) ; candidats à surveiller : **Anime Origins** & **Wonderland** (sorties août 2026, momentum à confirmer), **+1 Speed Keyboard Escape** (~500K, obby, probablement sans codes). Aucun nouveau hit non couvert n'a pu être fiché ce run faute d'accès fiable à l'API miniatures Roblox (règle « jamais de SVG en miniature »).

Prochaine brique recommandée (J13), par ordre de priorité :

1. **Brique technique — réconcilier les deux arbres codes** (`codes-<slug>.html` servis vs `codes/<slug>.html` redirigés) : décider de ne maintenir QUE l'arbre servi (les `codes/` sont 301-redirigés donc invisibles), puis retirer/geler l'arbre redondant pour supprimer la dette de synchronisation. Impact honnêteté/maintenance élevé.
2. **Reconcilier Anime Vanguards** (candidats Miniupdate1 / 2BVisits / Prepare confirmés par plusieurs agrégateurs, absents de la page ; vérifier expiration des anciens) — laissé en attente ce run par prudence (sources en conflit sur l'ensemble actif exact).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J11 (20/08)

**Run du 20/08/2026 — rattrapage codes prioritaire (écart de ~19 jours depuis le dernier run) :** la priorité absolue (vérif codes des jeux hot) a mobilisé tout le budget d'édition. Codes revérifiés (≥3 sources fiables + source officielle Trello/X quand dispo) et **mis à jour sur les pages SERVIES `codes-<slug>.html`** ET les copies `codes/<slug>.html` : **Blue Lock Rivals** (Sae Rework → 4 actifs : SAEREWORK, HALFBAKED, RINSOON, SAERRY4DELAY), **Volleyball Legends** (Update 83 → 3 actifs : UPDATE_83, MIKAGE_REVIVED, SCHOOL_SOON), **Anime Vanguards** (v9.0 → 16 actifs), **Anime Last Stand** (Shibuya Pt.1 → 38 actifs). Dates « Vérifié le » rafraîchies au 20/08 sur Blox Fruits, Blade Ball, Grow a Garden, GAG2, Fisch (inchangés). Cartes du hub `tous-les-codes.html` resynchronisées (comptes + dates) pour les 4 jeux modifiés. **⚠️ Dette d'architecture confirmée (déjà remontée le 01/08)** : les deux arbres `codes-<slug>.html` (servis) et `codes/<slug>.html` (301-redirigés) avaient **divergé** (templates + données différentes ; ex. BLR servi affichait encore 9 codes « Semi-Finals », les `codes/` en affichaient 6 « Quarter-Finals »). Ce run a corrigé les 4 jeux chauds sur les deux arbres, mais **le reste du catalogue reste potentiellement désynchronisé** → à traiter comme brique technique prioritaire. **Trending re-scanné** (web, ≥3 sources) : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Anime Expeditions, Murder Mystery 2, +1 Speed Keyboard Escape) tous couverts ou déjà fichés ; aucun nouveau hit non couvert. **Aucune nouvelle page de cluster créée ce run** (légitime : « ne jamais empiéter sur la vérif codes »).

Prochaine brique recommandée (prochain run), par ordre de priorité :

1. **Brique technique — réconcilier les deux arbres codes** (`codes-<slug>.html` servis vs `codes/<slug>.html` redirigés) : soit synchroniser le contenu, soit décider de ne maintenir QUE l'arbre servi et retirer/rebâtir l'autre. Impact SEO/honnêteté élevé (des pages servies affichent des codes périmés).
2. **Génériquiser le `FAQPage` JSON-LD** des pages codes pour refléter la FAQ visible (report du J10).
3. **Guide GAG « pets / œufs »** (how-to distinct) — si le budget code le permet.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

**Travail fait le 01/08 (J10) — correctif structuré prioritaire (brique technique) :** découverte et correction d'un **défaut de données structurées systémique sur les 170 pages codes SERVIES** (`codes-<slug>.html`). Depuis la migration « URLs plates » du 22/07, chaque page servie embarquait un **JSON-LD `BreadcrumbList` + `FAQPage` copié tel quel depuis Blox Fruits** : fil d'Ariane position 3 = « Codes Blox Fruits » → `/codes/blox-fruits`, et 3 questions FAQ toutes rédigées « … Blox Fruits … » — sur des pages Fisch, Adopt Me, King Legacy, etc. **Correction appliquée** (script Python validé) : breadcrumb position 3 = « Codes <NomDuJeu> » pointant vers le **canonical réel** de la page (URL plate), et les 3 questions FAQ reprennent le bon nom de jeu ; la réponse Q1 (« comment entrer un code ») **génériquisée** (« ouvre la zone dédiée aux codes… ») pour ne pas laisser d'instructions propres à Blox Fruits sur les autres jeux. **QC** : chaque bloc `<script type="application/ld+json">` re-parsé (`json.loads`) OK sur les 171 pages ; 0 null byte ; toutes finissent par `</html>` ; 0 breadcrumb « Blox Fruits » résiduel. **Bonus** : nettoyage d'une corruption de nom (« Ferme d\ » → « Ferme d'Anneaux ») sur `codes-ferme-d-anneaux.html`. **Effet SEO** : structured data valide et cohérente par entité sur tout le catalogue codes servi (crawl/rich-results/EEAT) — correctif à fort impact, transversal, sans création de page (donc anti-cannibalisation nulle). **Anomalie majeure remontée à Peter** (voir rapport du jour) : la maintenance quotidienne éditait `codes/<slug>.html` (301-redirigés) au lieu des `codes-<slug>.html` **servis** → « Vérifié le » figé au 22–26 juillet sur le site live ; corrigé ce run (refresh au 1 août sur les 171 pages servies).

Prochaine brique recommandée (J11), par ordre de priorité :

1. **Génériquiser complètement le `FAQPage` JSON-LD** des pages codes pour qu'il **reflète la FAQ visible** de chaque page (aujourd'hui : bon nom de jeu mais 3 questions génériques ≠ FAQ visible → conformité Google FAQ imparfaite). Aligner JSON-LD ↔ contenu visible, page par page ou par lot.
2. **Value/trading list GAG (graines ou pets)** — uniquement si la maintenance quotidienne des valeurs (≥2 sources datées) est tenable ; sinon reporter.
3. **Guide GAG « pets / œufs »** (comment obtenir, meilleurs pets, éclosion) — intention how-to distincte, complète le cluster GAG.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J9 (31/07)

**Travail fait le 31/07 (J9) :** nouveau **guide how-to `guides/grow-a-garden-weather.html`** (« Événements météo Grow a Garden (2026) – Liste & comment les déclencher », ~1 800 mots). **Intention distincte ciblée** : « grow a garden météo », « événements météo grow a garden / weather events », « comment déclencher pluie / orage / blood moon grow a garden » — intention *how-to sur la météo*, **complémentaire mais distincte** du guide des mutations (`grow-a-garden-mutations.html`, qui liste les multiplicateurs) : la page météo explique le **cycle météo** et **quelle météo déclenche quelle mutation**, sans dupliquer la table des multiplicateurs (renvoyée au guide mutations). **Anti-cannibalisation** : aucune page existante ne visait ces head terms météo ; liens réciproques explicites météo ↔ mutations (la page mutations pointe désormais « météo » vers ce guide). **Contenu** : cycle météo (propre au serveur, automatique vs outils vs admin), tableau des événements permanents (Rain→Wet, Thunderstorm→Shocked ×100, Frost→Chilled/Frozen, Meteor Shower→Celestial ×120, Blood Moon→Bloodlit, Heatwave→Sundried…), événements liés aux updates (Bee Swarm, Zen/Corrupted, Safari…), tableau des événements admin les plus rentables (Sun God/Dawnbound ×150, Meteoric ×125, Disco, Black Hole/Voidtouched…), stratégie de farm, FAQ 6 questions. **EEAT/honnêteté** : encart « info communautaire » (valeurs wiki/Beebom datées juillet 2026, évolutives → renvoi wiki), byline « L'équipe Zoneblox », aucune heure/valeur inventée ; renvoi à l'encart évènements accueil pour les admin abuses. **Schema** Article + BreadcrumbList + FAQPage. **Maillage (anti-orphelin)** : carte ajoutée au hub `guides/index.html` (vraie miniature tr.rbxcdn.com) + ItemList (position 46), liens croisés vers codes / tier list graines / guide complet / mutations + encart accueil, entrées `sitemap-guides.xml` et `sitemap.xml`. **Effet SEO** : le cluster Grow a Garden gagne une 6ᵉ brique (codes ✓ · guide ✓ · tier graines ✓ · GAG2 pets ✓ · mutations ✓ · **météo ✓**) et couvre désormais l'intention how-to météo à fort volume, en distribuant de l'equity interne au sein du cluster. **Trending re-scanné** (web ≥3 sources) : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Animal Hospital) tous couverts ; aucun nouveau hit non couvert. Candidat toujours en attente : **« +1 Speed Keyboard Escape »** (~500K CCU, obby, probablement sans codes) — à évaluer pour une fiche (Étape 1).

Prochaine brique recommandée (J10), par ordre de priorité :

1. **Value/trading list GAG (graines ou pets)** — uniquement si l'engagement de maintenance quotidienne des valeurs (≥2 sources datées) est tenable ; sinon la reporter.
2. **Guide GAG « pets / œufs »** (comment obtenir, meilleurs pets, éclosion) — intention how-to distincte, complète le cluster GAG et se relie à la tier list pets GAG2 + mutations + météo.
3. **Évaluer « +1 Speed Keyboard Escape »** (~500K CCU) : vérifier éligibilité, miniature réelle, existence de codes ; créer la fiche (Étape 1) si pertinent, sinon l'ajouter comme entrée du hub « nouveaux jeux ».

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J8 (30/07)

**Travail fait le 30/07 (J8) :** nouveau **second hub éditorial `nouveaux-jeux-roblox.html`** (« Nouveaux jeux Roblox (2026) — les sorties et hits récents à essayer », ~1 810 mots). **Intention distincte ciblée** : head terms « nouveaux jeux roblox », « nouveaux jeux roblox 2026 », « dernières sorties roblox », « jeux roblox récents » — intention *nouveauté*, **voisine mais distincte** de l'intention *popularité* du hub `meilleurs-jeux-roblox.html` (J6). **Anti-cannibalisation** : aucune page existante ne visait ces head terms ; le cadrage éditorial (sorties/croissance récentes 2025-2026, pas « les plus joués ») et les liens réciproques explicites entre les deux hubs séparent nettement les intentions. Roster de 12 jeux récents (Grow a Garden 2, Steal a Brainrot, Animal Hospital, Evomon, Plants vs Brainrots, Fish It, 100 Days at Sea, DIG, Dead Rails, Grimoires Era, Brainrot Evolution, 99 Nights). **EEAT/honnêteté** : encart méthodologie + date (30/07) + byline « L'équipe Zoneblox » + mention que la nouveauté est éphémère. **Schema** BreadcrumbList + CollectionPage/ItemList (12) + FAQPage. **Maillage (anti-orphelin)** : vraies miniatures tr.rbxcdn.com, liens réciproques depuis l'accueil, `meilleurs-jeux-roblox.html`, et les 3 hubs de cluster (`codes/index.html`, `guides/index.html`, `tier-list/index.html`), + `sitemap-pages.xml` et `sitemap.xml`. **Effet SEO** : le cluster « hubs éditoriaux » compte désormais 2 pages d'intention complémentaires (popularité + nouveauté) qui se renforcent mutuellement et redistribuent l'equity vers les fiches jeu. **Trending re-scanné** : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Animal Hospital, Anime Expeditions) tous couverts. Candidat toujours en attente : **« +1 Speed Keyboard Escape »** (~500K CCU, obby/incrémental, probablement sans codes) — à évaluer pour une fiche (Étape 1) lors d'un prochain run.

Prochaine brique recommandée (J9), par ordre de priorité :

1. **Guide GAG « weather / événements météo »** (comment déclencher pluie, neige, orage, blood moon, solar flare) — complément how-to du cluster Grow a Garden (à relier à la page mutations et à l'encart évènements), intention distincte.
2. **Évaluer « +1 Speed Keyboard Escape »** (~500K CCU) : vérifier éligibilité, miniature réelle, existence de codes ; créer la fiche (Étape 1) si pertinent, sinon l'ajouter comme entrée du hub « nouveaux jeux ».
3. **Value/trading list** (GAG pets ou Blox Fruits) uniquement si la maintenance quotidienne des valeurs (≥2 sources datées) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J7 (29/07)

**Travail fait le 29/07 (J7) :** consolidation du maillage du hub éditorial `meilleurs-jeux-roblox.html` (créé le 28/07). Ajout de **liens contextuels réciproques** depuis les trois hubs de cluster — `codes/index.html`, `guides/index.html` et `tier-list/index.html` — vers le hub éditorial (il n'était relié que depuis l'accueil + sitemaps). **Effet SEO** : le hub reçoit désormais de l'equity interne des quatre points d'entrée principaux du site (accueil + 3 hubs de cluster), ce qui consolide sa capacité à se positionner sur les head terms « meilleurs jeux roblox » et à redistribuer l'autorité vers les 18 pages jeu qu'il cite. **Anti-cannibalisation** : liens à ancres variées et descriptives (intention découverte), aucune nouvelle page créée → zéro risque de cannibalisation. **Trending re-scanné** : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Animal Hospital) tous couverts. Candidat repéré : **« +1 Speed Keyboard Escape »** (~405K CCU, obby/escape, probablement sans codes) — à évaluer pour une éventuelle fiche (Étape 1) lors d'un prochain run.

Prochaine brique recommandée (J8), par ordre de priorité :

1. **Second hub d'intention « Nouveaux jeux Roblox (2026) »** — intention *nouveauté* distincte de *popularité* (le hub existant). Cible Animal Hospital, Evomon, Grow a Garden 2, Steal a Brainrot ; relie réciproquement au hub « meilleurs jeux » (intentions voisines mais distinctes → pas de cannibalisation) et aux fiches jeu. Fort volume, complète le cluster hub.
2. **Guide GAG « weather / événements météo »** (comment déclencher pluie, neige, orage, blood moon, solar flare) — complément how-to du cluster Grow a Garden, intention distincte.
3. **Évaluer « +1 Speed Keyboard Escape »** (~405K CCU) : vérifier éligibilité, miniature, existence de codes ; créer la fiche si pertinent (Étape 1).

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J6 (28/07)


**Travail fait le 28/07 (J6) :** nouveau **hub éditorial `meilleurs-jeux-roblox.html`** (« Meilleurs jeux Roblox à jouer maintenant — été 2026 », ~1 890 mots). **Intention distincte ciblée** : head terms « meilleurs jeux roblox », « jeux roblox populaires / tendance », « top jeux roblox 2026 » — intention *découverte/navigation*, distincte des pages codes (transaction), guides (how-to) et tier lists (classement d'items) → **aucune cannibalisation** (aucune page existante ne visait ces head terms). **Effet SEO principal** : maillage transversal — le hub distribue de l'equity vers **18 pages jeu** du catalogue (codes + guide + tier list de chacune) et capte des head terms à fort volume. Roster sourcé (palmarès « most played / top games » juillet 2026) : Grow a Garden 2, Steal a Brainrot, Brookhaven (~639K), Blox Fruits (~203K pic), Blade Ball, Blue Lock Rivals, Volleyball Legends, Anime Vanguards, Fisch, Fruit Battlegrounds, Grow a Garden, Animal Hospital, Adopt Me, 99 Nights, DIG, Pet Simulator 99, Anime Last Stand, Evomon. **EEAT/honnêteté** : encart méthodologie + date (28/07) + byline « L'équipe Zoneblox » + mention explicite que le classement évolue ; aucun compteur inventé (chiffres uniquement quand sourcés). **Schema** BreadcrumbList + ItemList (18) + FAQPage. **Maillage (anti-orphelin)** : vraies miniatures tr.rbxcdn.com, lien depuis l'accueil (section « Jeux & codes »), `sitemap-pages.xml` + `sitemap.xml`.

Prochaine brique recommandée (J7), par ordre de priorité :

1. **Renforcer le hub éditorial** : ajouter des liens réciproques depuis les hubs `codes/index.html`, `guides/index.html` et `tier-lists.html` vers `meilleurs-jeux-roblox.html` (aujourd'hui relié depuis l'accueil + sitemaps seulement) pour consolider le maillage ; OU décliner un second hub d'intention voisine mais distincte : **« Nouveaux jeux Roblox (2026) »** (intention *nouveauté* ≠ *popularité*) ciblant Animal Hospital, Evomon, Grow a Garden 2, Steal a Brainrot.
2. **Guide GAG « weather / événements météo »** (comment déclencher pluie, neige, orage, blood moon, solar flare) — complément how-to de la page mutations, intention distincte.
3. **Value/trading list** (GAG pets ou Blox Fruits) uniquement si la maintenance quotidienne des valeurs (≥2 sources datées) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

### Archive — J4 (26/07)

**Travail fait le 26/07 :** nouvelle page **`tier-list/grow-a-garden-2-pets.html`** (Tier List Pets Grow a Garden 2, ~1 930 mots). Intention distincte ciblée : « grow a garden 2 pets tier list », « meilleurs pets grow a garden 2 » — sans cannibaliser la tier list des **graines** GAG2 (intention rendement) ni la tier list des **pets du 1er opus** GAG (jeu différent). Classement sourcé (Beebom, Pro Game Guides, FRVR, u7buy, Skycoach) : S = Unicorn, Ice Serpent, Black Dragon, Raccoon · A = Golden Dragonfly, Queen Bee, Deer · B/C détaillés. Effets honnêtes (mutation Rainbow/Gold, défense nocturne, croissance), note d'évolutivité des prix, schema ItemList + FAQPage + Breadcrumb. Maillage complet : carte hub (vraie miniature), cross-links seeds ↔ pets ↔ codes ↔ guide, sitemap-tier-list.xml + sitemap.xml. Aucun orphelin.

Le cluster Grow a Garden compte désormais : GAG pets ✓ · GAG2 graines ✓ · **GAG2 pets ✓**. Prochaine brique recommandée, par ordre de priorité :

1. **Grow a Garden — page « mutations »** (`guides/` ou `tier-list/`) : intention « grow a garden mutations », « comment obtenir mutation Rainbow / Gold / Wet / Chilled ». Fort volume, intention distincte (how-to, pas un classement) → complète le cluster sans cannibaliser. Sourcer ≥2 (valeurs/multiplicateurs communautaires datés).
2. Alternative : **hub éditorial « Meilleurs jeux Roblox (juillet 2026) »** — forte demande, maillage transversal vers tout le catalogue (opportunité #2 du scoring, encore À faire).
3. Poursuivre le cluster GAG2 : **value list des graines/pets** uniquement si la maintenance des valeurs (≥2 sources datées) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

*Rappel opérationnel : je ne fais jamais `git push` moi-même. Pour publier le travail du jour, dans le dossier GameNova :*

```
git add -A && git commit -m "SEO: tier list races Blox Fruits + encart evenements + audit roadmap" && git push origin main
```
