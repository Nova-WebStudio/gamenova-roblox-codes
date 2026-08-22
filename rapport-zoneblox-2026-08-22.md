# Rapport Zoneblox — 22 août 2026 (samedi)

## (a) Vérification des codes (ÉTAPE 2 — priorité absolue)

### Réconciliation majeure : Anime Vanguards (16 → 6 codes actifs)

Candidat en attente depuis plusieurs runs (sources en conflit sur l'ensemble actif exact). Tranché ce run grâce à **deux sources récentes et concordantes** : **GamesRadar** (MAJ 17/08) et **Beebom** (MAJ 17/08), croisées avec Pro Game Guides / PC Gamer / PCGamesN.

| Action | Codes |
|--------|-------|
| **Ajoutés (actifs)** — confirmés par ≥3 agrégateurs | `Miniupdate1`, `2BVisits` (⚠️ expirent le 23/08), `Prepare` |
| **Conservés actifs** — toujours listés actifs par Beebom/PGG (conflit avec GamesRadar → prudence, conservés) | `1DayDelay`, `25thHour`, `LetTheLarpingBegin` |
| **Déplacés en « expirés »** — GamesRadar+Beebom concordants | `WhoopsieDaisy`, `LateBP`, `PowerOfLove`, `EEPart1`, `BPSoon`, `LagGone`, `13.5`, `EternalAdversaries`, `Gambler`, `DMCAFree`, `Liberation`, `223`, `Cog5th` |

**Bug corrigé** : 6 codes (`LateBP`, `LagGone`, `DMCAFree`, `Liberation`, `223`, `Cog5th`) figuraient simultanément dans la liste active ET la liste expirée. Les deux listes ont été reconstruites proprement (6 actifs, 22 expirés, dédupliquées). Compteur `16 → 6 codes actifs`, H1 « juillet → août 2026 », carte du hub `tous-les-codes.html` resynchronisée (compteur + date + mois).

> ⚠️ `Miniupdate1` et `2BVisits` expirent le **23/08** : à repasser en « expirés » au prochain run.

### Autres jeux chauds re-vérifiés (web ≥3 sources) — inchangés par prudence

| Jeu | Constat | Décision |
|-----|---------|----------|
| Fisch | ~5 actifs cités (SCARLET, TemporarySubmarine, CARBON, TheDeepIsVeryDeep, HALIBUT) mais codes expirant en ~24 h | Inchangé (reconciliation same-day non fiable) |
| Blade Ball | 14–24 actifs selon sources, strings précis absents des snippets | Inchangé, à revoir via Discord/X officiel |
| Grow a Garden | Sources confondent GAG et GAG2 (liste retournée = codes GAG2) | Inchangé (prudence) |
| Fruit Battlegrounds | `OPE V2` (800 gems, 20/08) cité par 1 source ; paliers `BIG1M170K!!`… sans distinction actif/expiré nette | Non publié (< 3 sources concordantes) |
| Anime Last Stand | Newest (DelaySorryals, ALSUPD2, BleachSS, HuntersMark, SaveRukia) déjà sur la page | Inchangé (aucun nouveau code confirmé) |

**Stables confirmés les 20–21/08** (non re-vérifiés source-à-source ce run) : Blox Fruits, Blue Lock Rivals (4), Volleyball Legends (3), Steal a Brainrot (1 : BESTBRAINROTEVER).

**« 🔄 Vérifié le »** rafraîchi au **22 août 2026** sur les **171 pages codes servies** (`codes-*.html`), idempotent (1 ligne `#verifDate` / page). 170 étaient au 21 août, 1 (AV) déjà au 22.

**Aucun code inventé.** Règle de sourcing respectée (≥3 sources fiables ou officielle ; conflit → prudence + « en attente »).

**Candidats « en attente » (prochain run)** : Fruit Battlegrounds (paliers + OPE V2), Anime Last Stand (liste active exacte), Fisch (fluide), + tout le long tail.

## (b) Directeur SEO (ÉTAPE 2bis)

**Trending re-scanné (web)** : leaders (Murder Mystery 2, Grow a Garden/2, Steal a Brainrot, Brookhaven, Anime Expeditions) tous couverts. Deux hits éligibles **non couverts** : **Anime Origins** (anime TD en croissance, codes déjà suivis par Beebom/GamesRadar/PGG) et **+1 Speed Keyboard Escape** (~500K CCU, 3,8 Md visites). **Fiche impossible ce run** : Chrome non connecté + shell sans réseau → API miniatures Roblox inaccessible, et règle absolue « jamais de SVG comme miniature affichée ». À ficher lors d'un run avec Chrome.

**Brique de cluster réalisée (maillage / anti-orphelin)** : sur `codes-grow-a-garden.html` (page GAG la plus trafiquée), **correction d'un lien mort** (« Guide débutant » → `href="#"`) vers `guides/grow-a-garden.html`, et **ajout de 2 liens profonds** vers `guides/grow-a-garden-mutations.html` et `guides/grow-a-garden-weather.html`. Effet : la page codes redistribue désormais de l'equity vers 3 pages how-to profondes du cluster GAG. **Anti-cannibalisation** : aucune nouvelle page, ancres distinctes → nulle. **Intention** : renforcer le cluster GAG depuis son point d'entrée le plus fort.

**Constat structurel remonté à Peter (non tranché en autonome)** : les 171 pages **servies** `codes-<slug>.html` n'ont **aucun** bandeau `data-cta="guidelink"` et lient un hub générique `guides.html` (jamais le guide spécifique) ; la nav servie compte **6 entrées** (sans « À propos »). Ces écarts découlent de la divergence des deux arbres codes (`codes-<slug>.html` servis vs `codes/<slug>.html` legacy 301-redirigés). Un mass-edit des 171 pages serait risqué **avant** l'arbitrage : à traiter comme brique technique **après** décision de Peter.

**Prochaine brique inscrite dans la roadmap (J14)** : (1) arbitrage Peter + brique technique (ne garder que l'arbre servi, y ré-injecter CTA guidelink + guide spécifique + nav 7 entrées, geler l'arbre `codes/`) ; (2) ficher Anime Origins avec Chrome ; (3) réconcilier Fruit Battlegrounds & Anime Last Stand.

## (c) Autres maintenances

- **Jeux ajoutés** : aucun (API miniatures Roblox inaccessible ce run).
- **Guides / tier lists** : aucune création (les guides GAG météo + mutations existent déjà et sont reliés au hub servi `guides/index.html`).
- **UGC** : non modifié.
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-08-22. Aucun horaire ponctuel passé à retirer (17 évènements, tous récurrents/restocks). Pas de changement DST US avant le 2 nov 2026. `node --check js/events.js` OK.
- **Jeu de la semaine** : non touché (samedi ; MAJ réservée au lundi).

## (d) Fichiers touchés + QC

**Modifiés par ce run** :
- 171 × `codes-*.html` — `#verifDate` → 22 août 2026.
- `codes-anime-vanguards.html` — réconciliation 16→6 actifs (listes reconstruites, doublon corrigé, compteur, H1 août).
- `codes-grow-a-garden.html` — lien mort corrigé + 2 liens guides profonds.
- `tous-les-codes.html` — carte Anime Vanguards resynchronisée (6 codes, 22 août, mois).
- `data/events.json` — `meta.updated`.
- `tools/code-watch.json` — snapshot Anime Vanguards + `_pending2026-08-22` + `lastRun`.
- `SEO-directeur-audit-roadmap-2026-07-24.md` — brique J13 + archive J12 + brique J14.

**QC (tout vert)** :
- Scan intégrité sur les 348 fichiers modifiés (inclut les runs non committés des 20–21/08, dernier commit = 31/07) : **0 null byte**, toutes les pages finissent par `</html>`, sitemaps par `</urlset>`, **équilibre `<div>` intact** (0 déséquilibre).
- `node --check js/main.js` et `node --check js/events.js` OK.
- `data/events.json` et `tools/code-watch.json` valides (JSON).
- Blocs `ld+json` de `codes-anime-vanguards.html` re-parsés OK.
- Version cache uniforme `main.js?v=36` (js/main.js non modifié → pas de bump).

> ℹ️ Le dépôt n'a pas été committé depuis le **31 juillet** : le répertoire de travail contient donc aussi les modifications des runs des **20 et 21 août**. Le commit ci-dessous les regroupe toutes (sans risque).

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.
