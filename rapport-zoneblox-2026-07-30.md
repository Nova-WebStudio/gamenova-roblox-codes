# Rapport Zoneblox — 30 juillet 2026 (J8)

Run quotidien autonome. Jeudi → pas de « Jeu de la semaine » (lundi uniquement).

## a) Codes vérifiés (PRIORITÉ)

Vérification via recherche web (≥3 sources fiables) et sources officielles. **Note importante** : `web_fetch` renvoyait des versions en cache (juin) pour les pages à forte rotation (PGG, Beebom) → je me suis appuyé sur les résumés de recherche (plus frais) et la prudence pour les cas ambigus.

**Jeux hot revus aujourd'hui (12) :**

| Jeu | Résultat | Sources |
|---|---|---|
| **Anime Last Stand** | **MàJ codes** : +5 codes confirmés (ALSUPD2, BleachSS, HuntersMark, SaveRukia, DelaySorryals) → 26 actifs. Date « Mis à jour le » passée au 30/07. | RoCodes, Beebom, Gadgetbridge, Pocket Tactics, Fossbytes, Destructoid |
| Blox Fruits | Inchangé — 23 codes actifs correspondent exactement à la liste publiée. Vérifié. | RoCodes, PCGamesN, BlueStacks, Skycoach |
| Blue Lock Rivals | Inchangé (9 codes). ⚠️ Une source ne liste que les 3 plus récents comme actifs → conflit noté en `pending`, liste laissée à 9 par prudence. | PGG, Beebom, PC Gamer, Twinfinite |
| Volleyball Legends | Inchangé (UPDATE_80 / HIDARI_FINALLY / ENCHO_NERF). | PCGamesN, GamesRadar, Roonby, PGG |
| Anime Vanguards | Inchangé. LateBP désormais multi-sourcé (noté). | GamesRadar, PGG, Beebom, PCGamesN |
| Grow a Garden / GAG 2 | Inchangés (jeux calmes ; TEAMGREENBEAN, etc.). | PC Gamer, Beebom, PCGamesN, PGG |
| Steal a Brainrot | Inchangé (pas de code stable confirmé — position prudente maintenue). | Beebom, Pocket Tactics, Dexerto, PCGamesN |
| Blade Ball | Inchangé (14 actifs confirmés). | GamesRadar, Pocket Tactics, Beebom, thespike |
| DIG | Inchangé (plsdevshovel). ⚠️ Les codes « sakura/drills/trading » vus en recherche appartiennent à d'AUTRES jeux « Dig » (Digimon Era, Dig N Build…) → non ajoutés. | Pocket Gamer, TheClick, Try Hard Guides |
| Fisch | Inchangé. Candidat **HarpoonGunsNextWeek** en `pending` (liste active exacte incertaine). | u7buy, Beebom, PGG, PC Gamer, GamesRadar |
| Anime Rangers X | Inchangé. Candidats **PT2 Summer** (MonkeyKing, BeachTime, SummerPart2) en `pending` → à valider/publier au prochain run. | PGG, Beebom, driffle, igeeksblog, egamersworld |

Date « 🔄 Vérifié le » passée au **30 juillet 2026** sur les 12 pages ci-dessus (idempotent, 1 par page). « Mis à jour le » modifiée uniquement pour Anime Last Stand (vrai changement).

**Candidats en attente** enregistrés dans `tools/code-watch.json` (snapshots `lastChecked` = 2026-07-30) : Fisch → HarpoonGunsNextWeek ; Anime Rangers X → PT2 Summer ; Blue Lock Rivals → conflit 3 vs 9 ; Anime Last Stand → élaguer anciens codes World 3 avec confirmation en jeu.

**Jeux non revus ce run (à prioriser)** : king-legacy, fruit-battlegrounds, grimoires-era, sakura-stand, world-fighters, noob-incremental et le reste du catalogue (~150 pages) revus les 24-28/07. Aucune page correcte dégradée faute de temps.

## b) Directeur SEO

**Trending re-scanné** : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Animal Hospital, Anime Expeditions) tous couverts. Candidat toujours en attente : « +1 Speed Keyboard Escape » (~500K CCU, obby/incrémental, probablement sans codes) → à évaluer (Étape 1) un prochain run.

**Brique du jour (J8)** : nouveau **second hub éditorial `nouveaux-jeux-roblox.html`** (« Nouveaux jeux Roblox 2026 », ~1 810 mots).
- **Intention ciblée** : « nouveaux jeux roblox », « nouveaux jeux roblox 2026 », « dernières sorties roblox » — intention *nouveauté*, voisine mais **distincte** du hub *popularité* `meilleurs-jeux-roblox.html`. **Anti-cannibalisation** : aucune page existante ne visait ces head terms ; liens réciproques explicites entre les deux hubs.
- **Roster (12)** : Grow a Garden 2, Steal a Brainrot, Animal Hospital, Evomon, Plants vs Brainrots, Fish It, 100 Days at Sea, DIG, Dead Rails, Grimoires Era, Brainrot Evolution, 99 Nights in the Forest.
- **EEAT/honnêteté** : encart méthodologie + date (30/07) + byline « L'équipe Zoneblox » + mention que la nouveauté est éphémère.
- **Schema** : BreadcrumbList + CollectionPage/ItemList (12) + FAQPage.
- **Maillage (anti-orphelin)** : vraies miniatures tr.rbxcdn.com ; liens réciproques depuis l'accueil, `meilleurs-jeux-roblox.html` et les 3 hubs de cluster (`codes/index.html`, `guides/index.html`, `tier-list/index.html`) ; entrées `sitemap-pages.xml` + `sitemap.xml`.

**Prochaine brique (J9, inscrite dans la roadmap)** : Guide GAG « weather / événements météo » (how-to, relié à la page mutations + encart) ; sinon évaluer « +1 Speed Keyboard Escape » (Étape 1).

## c) Autres maintenances

- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-30. Aucun datetime ponctuel passé à retirer ; aucun horaire officiel nouvellement confirmé à promouvoir (règle d'honnêteté respectée — pas d'heure inventée). Bascule heure standard US (Steal a Brainrot) : rappel pour le 2 nov 2026.
- Jeux ajoutés : aucun (pas de nouveau hit non couvert).
- Guides / tier lists créés : aucun (brique du jour = hub éditorial).
- UGC : non modifié.
- Jeu de la semaine : non (jeudi).

## d) Fichiers touchés (aujourd'hui) + QC

- **Créé** : `nouveaux-jeux-roblox.html`
- **Codes** : `codes/anime-last-stand.html` (codes + dates) ; +11 pages « Vérifié le » → 30/07 (blox-fruits, grow-a-garden, grow-a-garden-2, steal-a-brainrot, blue-lock-rivals, volleyball-legends, anime-vanguards, fisch, anime-rangers-x, blade-ball, dig)
- **Maillage** : `index.html`, `meilleurs-jeux-roblox.html`, `codes/index.html`, `guides/index.html`, `tier-list/index.html`
- **Sitemaps** : `sitemap-pages.xml`, `sitemap.xml`
- **Données** : `tools/code-watch.json`, `data/events.json`
- **Roadmap** : `SEO-directeur-audit-roadmap-2026-07-24.md`

**QC (Étape 8)** — scan intégrité sur TOUS les fichiers modifiés : 0 null byte, tous les HTML finissent par `</html>`, `<div>` équilibrés (0), GA4 présent, `main.js?v=36` uniforme (325 pages), `node --check js/main.js` + `js/events.js` OK, JSON `code-watch.json` + `events.json` valides, sitemaps `</urlset>` + XML valide. **0 problème.** Nouvelle page ≥1 200 mots (~1 810) + descriptif développé.

⚠️ **À noter pour Peter** : le dépôt contient encore les changements **non commités des runs des 28 et 29/07** (les rapports `rapport-zoneblox-2026-07-28.md` et `-07-29.md` sont non suivis). Le commit ci-dessous les inclura tous.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
