# Rapport Zoneblox — 1 août 2026 (samedi)

## 🚨 Anomalie majeure détectée & corrigée (à arbitrer par Peter)

**Les runs quotidiens éditaient les mauvais fichiers.** Depuis la migration « URLs plates » du 22/07, les pages **servies/canoniques** sont les fichiers plats à la racine `codes-<slug>.html`. Le `.htaccess` **301-redirige** `/codes/<slug>.html` → `/codes-<slug>.html`. Or les runs récents rafraîchissaient les copies **`codes/<slug>.html` (redirigées, non servies)**.

Conséquences sur le **site live** :
- La ligne « 🔄 Vérifié le » était **figée au 22 juillet** (159 pages) / **26 juillet** (12 pages) → effet « pages abandonnées » exactement ce que le système devait éviter.
- Fisch servi était figé à **4 codes / 26 juillet**, alors que la copie redirigée avait été mise à 5 codes le 27/07.

**Correctifs appliqués ce run** (sur les fichiers **servis**) :
- « Vérifié le » → **1 août 2026** sur les **171 pages `codes-*.html` servies** (+ 172 copies nested, pour cohérence).
- Page Fisch servie reconciliée (voir §codes).

**Décision requise (Peter)** — deux options propres :
1. **Repointer la tâche quotidienne** (et `CLAUDE.md`) sur les fichiers plats `codes-<slug>.html` servis, et considérer `codes/<slug>.html` comme obsolètes ; ou
2. **Retirer les redirections 301** du `.htaccess` et re-servir `codes/<slug>.html` (canonical à réaligner).

En l'état, j'ai corrigé **les fichiers servis** ce run pour rétablir la fraîcheur, mais la cause racine (tâche/doc pointant sur les nested) doit être tranchée pour ne pas re-diverger.

---

## (a) Codes vérifiés (priorité absolue)

**Jeux hot re-vérifiés (web ≥3 sources)** : Blox Fruits, Grow a Garden, Grow a Garden 2, Blade Ball, Fisch, Volleyball Legends, Anime Vanguards, Blue Lock Rivals. Sources : Beebom (maj 1er août), Destructoid, Pocket Gamer, Pocket Tactics, PC Gamer, GamesRadar, RoCodes, Roonby, AllThings.How.

**Changement réel — Fisch (page servie `codes-fisch.html`)** :
- **+ `SorryForShopShenanigans`** (150 Shady Scrip + Rainbow Totem, Shady Bazaar) — confirmé par **Beebom (01/08), Destructoid, Pocket Gamer, AllThings.How** (≥3 sources fiables). ✅ publiable.
- Reconciliation : `Sorry4Delay` (Chapel, ≥3 sources 27/07) et `RoamingFishAndWaterPark` réintégrés sur la page servie (elle était restée à 4 codes). **Total servi : 4 → 6 codes actifs.** Titre/H1/og bumpés « août 2026 », « Mis à jour le 1 août 2026 », schéma FAQ/breadcrumb corrigé (voir §b).

**Candidats en attente / conflits (prudence, non publiés)** :
- **Volleyball Legends** : Update 81 / `HIDARI_RETURNS` annoncé (Roonby, Beebom) mais **liste complète non confirmée à ≥3 sources** → page maintenue (`UPDATE_80`/`HIDARI_FINALLY`/`ENCHO_NERF`). Jeu à reset hebdo — reconcilier via Discord officiel.
- **Anime Vanguards** : RoCodes/Beebom listent un set divergent (`Cog5th`, `223`, `Liberation`, `DMCAFree`, `LagGone`) — conflit historique persistant → non appliqué.
- **Blade Ball** : set G2A (`5BVISITS`/`DRAGONS`/`XMAS`…) divergent de notre set (14 codes) → non publié.
- **Blox Fruits** : liste « admin abuse » BlueStacks (`DEVSCOOKING`, `ADMINFIGHT`…) = source unique non fiable → non publiée. Liste 23-24 maintenue.
- Grow a Garden / GAG2 / Blue Lock Rivals : sources cohérentes, **aucun changement**.

**Jeux non revus en profondeur ce run (à prioriser)** : fruit-battlegrounds (paliers récents `BIG1M170K!!`), anime-rangers-x (~15 codes PGG additionnels), catch-a-monster, dig, world-fighters, squid-game-x, + jeux non-hot du catalogue.

`tools/code-watch.json` : `lastRun` → 01/08 ; `lastChecked` bumpé sur les 8 jeux re-vérifiés ; bloc `_pending2026-08-01` ajouté (dont l'anomalie fichiers servis).

## (b) Directeur SEO — brique du jour (J10)

**Correctif de données structurées systémique sur les 170 pages codes SERVIES.** Découverte : depuis la migration du 22/07, **chaque** `codes-<slug>.html` embarquait un JSON-LD `BreadcrumbList` + `FAQPage` **copié depuis Blox Fruits** (fil d'Ariane « Codes Blox Fruits » → `/codes/blox-fruits`, 3 questions FAQ toutes « … Blox Fruits … ») — sur des pages Fisch, Adopt Me, King Legacy, etc.

**Correction (script Python validé)** :
- Breadcrumb position 3 = « Codes &lt;NomDuJeu&gt; » → **canonical réel** (URL plate) de chaque page.
- 3 questions FAQ reprennent le bon nom de jeu ; réponse Q1 **génériquisée** (« ouvre la zone dédiée aux codes… ») pour ne pas laisser d'instructions propres à Blox Fruits ailleurs.
- Bonus : nettoyage d'une corruption de nom `Ferme d\` → « Ferme d'Anneaux » sur `codes-ferme-d-anneaux.html`.

**Anti-cannibalisation** : correctif technique, aucune nouvelle page. **QC** : les blocs `<script type="application/ld+json">` re-parsés (`json.loads`) OK sur les **171** pages, 0 null byte, toutes finissent par `</html>`, **0** breadcrumb « Blox Fruits » résiduel.

**Roadmap** : J10 marquée faite (correctif structuré) ; **prochaine brique J11** inscrite = génériquiser le `FAQPage` JSON-LD pour qu'il **reflète la FAQ visible** de chaque page (conformité Google FAQ), puis value/trading list GAG ou guide pets GAG.

**Trending re-scanné** : leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Fisch, Animal Hospital) tous couverts ; aucun nouveau hit ≥4000 joueurs non couvert.

## (c) Autres chantiers
- **Encart évènements** (`data/events.json`) : `meta.updated` → 01/08. Aucune `datetime` ponctuelle passée à retirer (tout en récurrent/no-fixed-time). JSON valide.
- **Jeu de la semaine** : non touché (samedi ; réservé au lundi).
- Aucun jeu ajouté, aucune tier list / guide / UGC créé ce run (effort concentré sur le correctif fichiers servis + structured data).

## (d) Fichiers touchés + QC

**347 fichiers modifiés** :
- 171 × `codes-*.html` (servies) — « Vérifié le » → 1 août + breadcrumb/FAQ JSON-LD corrigés.
- 172 × `codes/*.html` (nested) — « Vérifié le » → 1 août (cohérence).
- `codes-fisch.html` + `codes/fisch.html` — +SorryForShopShenanigans, 6 codes, dates, titres.
- `data/events.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`.

**QC — tout OK** : 0 fichier tronqué (toutes les HTML finissent par `</html>`), 0 null byte, `events.json` + `code-watch.json` valides, tous les JSON-LD parsés OK, GA4 (`G-FEL71QVHNL`) et nav 7 entrées (incl. Avatars) présents, div équilibrés sur les fichiers Fisch édités, 171/171 pages servies à « 1 août 2026 ».

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
