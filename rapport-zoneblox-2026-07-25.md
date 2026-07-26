# Rapport Zoneblox — 25 juillet 2026 (samedi)

## a) Codes vérifiés (priorité absolue)

**12 jeux « hot » vérifiés** avec ≥3 sources fiables et/ou source officielle. Sources principales : Pro Game Guides, Beebom, GamesRadar, PCGamer, Dexerto, Pocket Tactics, Destructoid, TheClick, bloxodes, PCGamesN.

### Changements réels appliqués
- **Volleyball Legends** — 3 codes actifs désormais (UPDATE_79, SEASON_17, FESTIVAL_UPD). Les 3 codes de l'Update 78 (**UPDATE_78, LEADERBOARD, NEW_PACK**) ont expiré → déplacés dans la liste des expirés. Confirmé par Beebom, GamesRadar, Pro Game Guides, TheClick et bloxodes (« 3 Active Codes »). Compteur 6→3, compteur expirés 6→9, narratif « Dernière mise à jour » réécrit, arrays JS synchronisés, « Vérifié le » → 25 juillet.
- **Grow a Garden 2** — ajout du code confirmé **REMEMBERTODRINKWATER** (1 arrosoir commun). Total 2→3 actifs (avec TEAMGREENBEAN, WATERYOPLANTS). Confirmé par PCGamer, Beebom, Pocket Gamer, Destructoid, GamesRadar.

### Vérifiés sans changement (« Vérifié le » rafraîchi au 25 juillet)
- **Blox Fruits** : 24 codes actifs, EASTEREXP le plus récent, resets KITT_RESET / Sub2UncleKizaru / SUB2GAMERROBOT_RESET1. Aligné.
- **Blue Lock Rivals** : 6 actifs + GAGAREWORK (confirmé encore actif par AnalyticsInsight + PGG). Aligné.
- **Grow a Garden** : RDCAward + BEANORLEAVE10. RDCAward actif confirmé. Aligné.
- **Anime Vanguards** : LateBP (nouveau) déjà **expiré** le 19/07 → non ajouté. Liste alignée.
- **Blade Ball** : 14 actifs, aucun nouveau code depuis longtemps. Aligné.
- **Fisch** : 7 actifs (RoamingFishAndWaterPark le plus récent). Aligné.
- **King Legacy** : liste alignée, aucun nouveau code.
- **Fruit Battlegrounds** : mise à jour OPE V2, liste alignée.
- **Anime Last Stand** : liste alignée (DemonicCyborg, ALSUPD1, WORLD3REBALANCE…).

### Candidats « en attente » / à surveiller (consignés dans `tools/code-watch.json`)
- **Steal a Brainrot** : sources en **conflit** (0 vs 22 actifs). Les codes sont des drops admin/merch très courts (BESTBRAINROTEVER, DIVINECURSED cités isolément ; BRAINROT2025 / STEALIT = **faux**). Aucun consensus ≥3 sources → **page laissée sans code (prudence)**. À revérifier via le Discord officiel au prochain run.
- **Grow a Garden** : BEANORLEAVE10 possiblement expiré (signal faible, 1 source) → conservé, à surveiller.

### Jeux non revus ce run (à prioriser au prochain)
Le catalogue compte **176 pages codes**. Ce run a couvert les 12 jeux les plus « hot ». Le reste du catalogue (anime-*, tower defense, simulateurs, UGC, etc.) n'a pas été revérifié aujourd'hui → à traiter en priorité aux prochains runs. `code-watch.json` : `lastRun` = 2026-07-25, snapshots des 12 jeux datés.

## b) Directeur SEO (autorité topicale)

- **Trending vérifié (web)** : leaders actuels (Grow a Garden 2 #1, Blox Fruits, Steal a Brainrot, Animal Hospital, Brookhaven) **tous déjà couverts**. Aucun nouveau hit ≥4000 joueurs non couvert → priorité à l'approfondissement du cluster phare.
- **Brique du jour** : nouvelle page **`tier-list/blox-fruits-swords.html`** (Blox Fruits Sword Tier List, juillet 2026, ~1 730 mots).
  - **Intention ciblée** : « best sword blox fruits », « meilleure épée blox fruits », « blox fruits swords 2026 ».
  - **Anti-cannibalisation** : intention distincte de la tier list des fruits (fruits), des races (races) et du guide (how-to). Choix de la brique la **plus stable** (classement de puissance, pas de valeurs de trading fluctuantes à maintenir).
  - **Classement sourcé** (PlayHub, RobloxDen, TierMaker, bloxfruit.io, RBLXGUIDE, DungeonPath) : S = True Triple Katana, Yama, Cursed Dual Katana, Soul Cane · A = Fox Lamp, Hallow Scythe, Dark Blade, Tushita, Dragonheart, Spikey Trident, Bisento · B/C/D détaillés.
  - **EEAT** : byline « L'équipe Zoneblox », politique éditoriale liée, prérequis évolutifs renvoyés au wiki (aucune invention de conditions d'obtention).
  - **Schema** : ItemList + BreadcrumbList + FAQPage (tous validés).
  - **Maillage** : carte ajoutée au hub `tier-lists.html` (vraie miniature tr.rbxcdn.com) ; boutons hero + « articles liés » croisés depuis `tier-list/blox-fruits.html` ET `tier-list/blox-fruits-races.html` ; liens sortants vers fruits, races, guide, codes ; entrées ajoutées à `sitemap-tier-list.xml` et `sitemap.xml`. **Aucun orphelin.**
- **Prochaine brique inscrite dans la roadmap** : basculer sur **Grow a Garden** (jeu #1 trafic) — tier list des pets/animaux GAG (stable, fort volume), reliée guide + codes + encart évènements.

## c) Autres maintenances
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-25. Aucune `datetime` ponctuelle passée à retirer (tous les events sont récurrents `everyMinutes`/`weekly` ou `no-fixed-time`). JSON validé, `js/events.js` `node --check` OK.
- **Jeu de la semaine** : non modifié (règle : lundi uniquement ; aujourd'hui = samedi).
- **Jeux ajoutés / guides / UGC** : aucun ce run (pas de nouveau hit trending ; priorité codes + brique SEO).

## d) Fichiers touchés + QC

**Modifiés :** codes-volleyball-legends.html, codes-grow-a-garden-2.html (changements codes) ; codes-blox-fruits / blue-lock-rivals / grow-a-garden / anime-vanguards / blade-ball / fisch / king-legacy / fruit-battlegrounds / anime-last-stand / steal-a-brainrot .html (Vérifié le) ; data/events.json ; tools/code-watch.json ; tier-lists.html ; tier-list/blox-fruits.html ; tier-list/blox-fruits-races.html ; sitemap-tier-list.xml ; sitemap.xml ; SEO-directeur-audit-roadmap-2026-07-24.md.
**Créé :** tier-list/blox-fruits-swords.html.

**QC (tous verts) :** 0 null byte sur tous les fichiers ; toutes les pages HTML finissent par `</html>`, sitemaps par `</urlset>` ; `<div>` équilibrés partout (diff 0) ; JSON-LD de la page épées valides ; `node --check` OK (main.js, events.js) ; JSON valides (events.json, code-watch.json) ; cache JS uniforme **`main.js?v=35`** sur les 321 pages (js/main.js non modifié → pas de bump) ; nav 7 entrées + GA4 sur la nouvelle page ; miniature hub = vraie tr.rbxcdn.com (pas d'emoji).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
