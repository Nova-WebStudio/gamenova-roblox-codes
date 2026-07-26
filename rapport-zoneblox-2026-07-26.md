# Rapport Zoneblox — 26 juillet 2026 (dimanche)

## a) Codes vérifiés (priorité absolue)

**12 jeux « hot » vérifiés** avec ≥3 sources fiables et/ou source officielle. Sources principales : Pro Game Guides, Beebom, GamesRadar, PCGamer, PCGamesN, Pocket Tactics, Dexerto, Destructoid, Nerdschalk, Roonby, Fossbytes, Try Hard Guides, Twinfinite, bloxodes.

### Changements réels appliqués
- **Volleyball Legends** — l'**Update 80** ajoute 3 codes actifs : **UPDATE_80**, **HIDARI_FINALLY** (5 Lucky Style Spins) et **ENCHO_NERF** (5 Lucky Ability Spins). Les 3 codes de l'Update 79 (UPDATE_79, SEASON_17, FESTIVAL_UPD) restent **actifs** (confirmé Nerdschalk, Roonby, PGG, Fossbytes, GamesRadar). Compteur 3 → **6 actifs**. Narratif « Dernière mise à jour » réécrit, arrays JS + cartes HTML synchronisés, « Vérifié le » → 26 juillet.
- **Blue Lock Rivals** — la mise à jour **Semi-Finals** ajoute 3 codes : **SEMIFINALS** (5 Lucky Spins + 5 Lucky Flow), **WORLDTOURNAMENTPART3** (5 Lucky Spins), **NEWMAP** (5 Lucky Flow). Confirmé Beebom, PGG, PCGamesN, Pocket Tactics, Twinfinite. Les 6 codes précédents restent actifs. Compteur 6 → **9 actifs**. Prose + arrays + cartes synchronisés.
- **Anime Last Stand** — la mise à jour **JoJo Part 7** ajoute 5 codes : **DelaySorryals** (50 rerolls), **ALSUPD2** (15 rerolls + 2 000 diamants), **BleachSS** (5 000 diamants), **HuntersMark** (55 rerolls + items d'évo Guts), **SaveRukia** (15 000 diamants + 3 Star Dust). Confirmé Pocket Tactics, Fossbytes, Beebom, Try Hard Guides, Destructoid. Compteur 21 → **26 actifs**. Prose « Dernière mise à jour » (qui datait du 12 juin) réécrite.

### Vérifiés sans changement (« Vérifié le » rafraîchi au 26 juillet)
- **Blox Fruits** : 24 codes actifs, aucun nouveau depuis des mois (confirmé). Aligné.
- **Grow a Garden** : RDCAward + BEANORLEAVE10 actifs (BEANORLEAVE10 **confirmé encore actif**, ce qui lève le doute de la veille). Aligné.
- **Grow a Garden 2** : 3 actifs (TEAMGREENBEAN, WATERYOPLANTS, REMEMBERTODRINKWATER). Aligné.
- **Blade Ball** : 14 actifs. Aligné.
- **Fisch** : 7 actifs (RoamingFishAndWaterPark le plus récent). Aligné.
- **King Legacy** : jeu dormant, aucun nouveau code. Aligné.
- **Fruit Battlegrounds** : aligné.
- **Anime Vanguards** : LateBP expiré (19/07), non ajouté. Aligné.

### Candidats « en attente » / prudence (consignés dans `tools/code-watch.json`)
- **Grow a Garden — torigate (Whispering Torii)** : **sources en conflit**. Plusieurs sources actuelles (PCGamesN, RobloxDen, Mein-MMO, FindingDulcinea) le listent de nouveau **actif**, mais sa validité est publiquement disputée et notre page le classe **expiré**. Application de la règle de prudence → **non publié comme actif**, laissé en expiré. À revérifier.
- **Steal a Brainrot** : toujours en conflit (0 vs 22 actifs selon les sources ; codes = drops admin très courts, aucun consensus ≥3). **Page laissée sans code** (prudence maintenue). À revoir via le Discord officiel.

### Jeux non revus ce run (à prioriser au prochain)
Le catalogue compte **176 pages codes**. Ce run a couvert les 12 jeux « hot ». Le reste (anime-*, tower defense, simulateurs, UGC, RNG…) n'a pas été revérifié aujourd'hui → à traiter en priorité aux prochains runs. `code-watch.json` : `lastRun` = 2026-07-26.

## b) Directeur SEO (autorité topicale)

- **Trending vérifié (web)** : leaders actuels (Grow a Garden 2 #1, Steal a Brainrot Tycoon, Brookhaven, Animal Hospital, Blox Fruits, Evomon) **tous déjà couverts**. Aucun nouveau hit ≥4000 joueurs non couvert → priorité à l'approfondissement du cluster phare.
- **Brique du jour** : nouvelle page **`tier-list/grow-a-garden-2-pets.html`** (Tier List Pets Grow a Garden 2, ~1 930 mots).
  - **Intention ciblée** : « grow a garden 2 pets tier list », « meilleurs pets grow a garden 2 », « grow a garden 2 best pets ».
  - **Anti-cannibalisation** : la roadmap suggérait une « tier list pets GAG » — mais `tier-list/grow-a-garden.html` **est déjà** une tier list de pets (jeu original). J'ai donc ciblé le jeu **#1 actuel (GAG2)**, dont seule la tier list des **graines** existait. Intention distincte des 3 pages voisines : graines GAG2 (rendement) ≠ pets GAG2 (effets) ≠ pets GAG (autre jeu).
  - **Classement sourcé** (Beebom, Pro Game Guides, FRVR, u7buy, Skycoach, bo3) : S = Unicorn (mutation Rainbow), Ice Serpent + Black Dragon (défense nocturne), Raccoon (vol) · A = Golden Dragonfly (mutation Gold), Queen Bee, Deer (meilleur rapport prix/effet) · B/C détaillés.
  - **EEAT + honnêteté** : byline « L'équipe Zoneblox », politique éditoriale liée, note explicite d'évolutivité des prix/effets (aucune valeur inventée), distinction familles mutation/défense/croissance.
  - **Schema** : Article + BreadcrumbList + **ItemList** + FAQPage (tous validés).
  - **Maillage (anti-orphelin)** : carte ajoutée au hub `tier-lists.html` (vraie miniature tr.rbxcdn.com) ; cross-links réciproques graines ↔ pets ↔ codes ↔ guide ; bloc « Articles liés » ; entrées `sitemap-tier-list.xml` + `sitemap.xml`.
- **Prochaine brique inscrite dans la roadmap (J5 — 27/07)** : page **« mutations » Grow a Garden** (intention how-to « comment obtenir mutation Rainbow/Gold/Wet »), ou à défaut le **hub éditorial « Meilleurs jeux Roblox juillet 2026 »**.

## c) Autres maintenances
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-26. Aucune `datetime` ponctuelle passée à retirer (tous les events sont récurrents `everyMinutes`/`weekly` ou `no-fixed-time`). JSON validé, `js/events.js` `node --check` OK.
- **Jeu de la semaine** : non modifié (règle : lundi uniquement ; aujourd'hui = dimanche).
- **Jeux ajoutés / guides / UGC** : aucun ce run (pas de nouveau hit trending ; priorité codes + brique SEO).

## d) Fichiers touchés + QC

**Modifiés (codes) :** codes-volleyball-legends.html, codes-blue-lock-rivals.html, codes-anime-last-stand.html (changements de codes) ; codes-blox-fruits / grow-a-garden / grow-a-garden-2 / steal-a-brainrot / blade-ball / fisch / king-legacy / fruit-battlegrounds / anime-vanguards .html (« Vérifié le » → 26/07).
**Modifiés (SEO/maintenance) :** tier-lists.html (carte hub), tier-list/grow-a-garden-2.html (cross-link), sitemap-tier-list.xml, sitemap.xml, data/events.json, tools/code-watch.json, SEO-directeur-audit-roadmap-2026-07-24.md.
**Créé :** tier-list/grow-a-garden-2-pets.html.

**QC (tous verts) :** 0 null byte sur tous les fichiers modifiés ; toutes les pages HTML finissent par `</html>`, sitemaps par `</urlset>` ; `<div>` équilibrés partout (diff 0) ; `node --check` OK (main.js, events.js) ; JSON valides (events.json, code-watch.json) ; XML sitemaps bien formés ; JSON-LD valides sur les pages codes modifiées et la nouvelle tier list ; cache JS **uniforme `main.js?v=35`** sur les 322 pages (js/main.js non modifié → pas de bump) ; nav 7 entrées + GA4 sur la nouvelle page ; miniature hub = vraie tr.rbxcdn.com (pas d'emoji) ; cohérence cartes/array/compteur vérifiée (Volleyball 6, BLR 9, ALS 26).

> Note : les compteurs `codes:` de `GAMES_INDEX` (js/main.js) n'ont volontairement pas été modifiés pour les 3 jeux à codes changés, afin d'éviter un bump de cache sur 322 pages en run non supervisé (précédent du 25/07). Les compteurs affichés font foi sur chaque page et sur le hub `tous-les-codes.html`.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
