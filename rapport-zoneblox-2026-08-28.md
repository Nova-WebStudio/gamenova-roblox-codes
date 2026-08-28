# Rapport Zoneblox — 28 août 2026 (run quotidien 05h00)

## ⚠️ Découverte importante (à retenir)

L'**arbre SERVI** du site est constitué des **fichiers plats `codes-<slug>.html`** (racine), **pas** du sous-dossier `codes/<slug>.html`.
- Preuve : `sitemap.xml` référence 178 URLs `https://zoneblox.com/codes-<slug>.html` (0 en `/codes/`), et `.htaccess` fait un **301 de `/codes/<slug>.html` → `/codes-<slug>.html`**.
- Le sous-dossier `codes/<slug>.html` est **déprécié** (redirigé, absent des sitemaps). Les tier lists (`tier-list/<slug>.html`) et guides (`guides/<slug>.html`) restent, eux, en **sous-dossier servi**.
- Le build du widget (`tools/build_codes_json.py`) lit bien les fichiers plats `codes-*.html`.
- **Conséquence sur ce run :** toutes les MAJ de codes et de dates « Vérifié le » ont été appliquées sur les **fichiers plats servis**. (Des éditions initiales avaient touché par erreur le sous-dossier déprécié — voir §Fichiers ; sans impact car non servi.)

## 🔴 Blocage commit — `.git/index.lock`

Un fichier résiduel `.git/index.lock` (0 octet) est présent et **impossible à supprimer** depuis l'environnement (permission refusée sur le montage). **Il bloquera `git commit`.** Peter doit le supprimer manuellement avant de publier :
```
del .git\index.lock   (Windows)   ou   rm .git/index.lock
```

---

## (a) Vérification des CODES (priorité absolue)

**Jeux chauds vérifiés ce run (≥1 source fiable + croisement / source officielle) :** 11.

| Jeu | Résultat | Source(s) |
|-----|----------|-----------|
| **Fisch** | **MODIFIÉ** : `ShootingStars` **expiré** (consensus 24/08 PCGamer/GamesRadar) → retiré des actifs (déplacé en expirés). Actifs = **scarlet, TemporarySubmarine, CARBON** (3). Date « Mis à jour » + « Vérifié » → 28/08. | Pro Game Guides (23/08) + PCGamer/GamesRadar/PocketGamer (24/08) |
| Grow a Garden | Inchangé — **RDCAward, BEANORLEAVE10** confirmés **actifs**. | Beebom + owlzo + growagardengame (≥3) |
| Blue Lock Rivals | Inchangé — 6 codes confirmés (INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!!). | Twinfinite/GamesRadar/PocketGamer/PGG |
| Volleyball Legends | Inchangé — UPDATE_84, SEASON_18, PIRATE_SZN. | GamesRadar/PGG/Beebom/Destructoid |
| Anime Vanguards | Inchangé (4 servis) — 1DayDelay, 25thHour, LetTheLarpingBegin confirmés + Prepare (conservé, conflit). | Pocket Tactics (24/08) |
| Blade Ball | Inchangé (13) — « ~14 actifs » cohérent. | Pocket Tactics/GamesRadar/TheSpike |
| Blox Fruits | Inchangé (24, dont EASTEREXP). | BlueStacks/Twinfinite/TheClick |
| Steal a Brainrot | Inchangé (1, BESTBRAINROTEVER) — **sources en conflit** (0/1/23) → prudence. | Dexerto/PCGamesN/Beebom |
| Fruit Battlegrounds | Inchangé (5) — 4/5 confirmés actifs. | Pocket Tactics/PGG/GameRant |
| King Legacy | Inchangé (7) — 3 confirmés actifs (WELCOMETOKINGLEGACY, DragonColorRefund, SKGames). | Insider Gaming/Pocket Tactics/PGG |

**Dates « 🔄 Vérifié le » rafraîchies au 28/08** sur ces 11 pages servies (idempotent, 1 par page).

**MAJ post-run (demande de Peter) :** l'encart « Vérifié aujourd'hui · <date> » du hero de `index.html` a été **retiré** (span `eyebrow`/`#todayDate` + `const TODAY` + ligne JS `$("#todayDate").textContent=TODAY`). Il n'y a donc plus de date d'accueil à maintenir. `CLAUDE.md` mis à jour en conséquence. (La ligne « 🔄 Vérifié le » des pages codes reste inchangée.)

**Candidats « en attente » (loggés dans `tools/code-watch.json` → snapshots.pending, à confirmer 2ᵉ source avant publication) :**
- Anime Vanguards : 12 codes actifs supplémentaires listés par Pocket Tactics (WhoopsieDaisy, LateBP, PowerOfLove, EEPart1, BPSoon, LagGone, 13.5, EternalAdversaries, Gambler, DMCAFree, Liberation, 223, Cog5th) — **source unique**.
- Fruit Battlegrounds : `HIGHER1M120K` (NOUVEAU, 800 Gems) — à confirmer ; `OMGUPDATE22` non reconfirmé.
- King Legacy : `RainbowDragon` (100 Gems), `2MFAV` (Stats Reset) — à confirmer.

**Widget :** `data/codes.json` régénéré (`build_codes_json.py`) → 177 jeux, **1228 codes** (−1 Fisch). Snapshots + `lastRun` mis à jour dans `code-watch.json`.

**Jeux NON revus ce run (à prioriser au prochain) :** le catalogue compte ~173 fiches ; seuls les ~11 jeux « hot » ont été re-vérifiés en profondeur. Priorités prochaines : jeux hot restants de `hotGames` (anime-last-stand, pet-simulator-99, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital, steal-an-egg), puis la longue traîne.

## (b) Directeur SEO (ÉTAPE 2bis)

**Trending re-scanné (multi-sources)** — leaders vérifiés contre le catalogue (Murder Mystery 2, Grow a Garden, Steal a Brainrot, Brookhaven, Animal Hospital ~350K, Anime Expeditions, Steal An Egg, GAG2) : **aucun nouveau hit ≥4000 non couvert** → approfondissement du cluster porteur (règle evergreen).

**Brique réalisée (J18) — Guide complet Steal An Egg :** nouveau `guides/steal-an-egg.html` (**~2 140 mots FR**, gabarit `guides/blox-fruits.html`).
- **Intention distincte (anti-cannibalisation) :** how-to (« guide steal an egg », « comment jouer », « comment augmenter vitesse », « rebirth ») — distincte de la fiche codes (transactionnelle) et de la tier list (classement). Aucune page existante ne visait cette intention.
- **Information gain :** table des **9 biomes + seuils de vitesse** (Forest→Cosmic), treadmill vs base, 10 trails, reset œufs 5 min/13 s, gardiens, pets (78, taille+mutations), outils de vol PvP, **Rebirth** (+5 %/palier, vitesse 150 = ×2 mutation Legendary), ordre de progression + erreurs, FAQ 6 Q. Schema **Article + BreadcrumbList + FAQPage**.
- **EEAT/honnêteté :** byline « L'équipe Zoneblox » + politique éditoriale ; **2 sources datées** (All Things How / Sehaj Padda 16/08 + Sportskeeda) ; encarts « valeurs communautaires susceptibles d'évoluer » ; rien d'inventé.
- **Maillage :** carte hub `guides.html` (vraie miniature tr.rbxcdn.com) + `sitemap-guides.xml` + `sitemap.xml` ; **liens croisés bidirectionnels** fiche `codes-steal-an-egg.html` (CTA `data-cta="guidelink"` → guide) ↔ guide ↔ tier list (bouton hero « Guide complet » ajouté).
- **Cluster Steal An Egg désormais COMPLET :** fiche codes ✓ · tier list pets ✓ · guide complet ✓.

**Prochaine brique inscrite (J19) :** 1) Ficher **Anime Origins** (report récurrent) ; 2) Value list (Steal An Egg/GAG2) si maintenance tenable ; 3) Hub « Nouveaux jeux Roblox (2026) ». Roadmap `SEO-directeur-audit-roadmap-2026-07-24.md` mise à jour (J18 = dernière brique, J17 archivé).

## (c) Autres maintenances

- **Jeux ajoutés :** aucun (aucun nouveau hit ≥4000 non couvert).
- **Guides créés :** `guides/steal-an-egg.html` (voir §b). **Tier lists :** aucune nouvelle.
- **UGC :** non modifié ce run.
- **Encart évènements (`data/events.json`) :** **non touché** — l'encart a été retiré de l'accueil (demande de Peter, 24/08) ; `events.json` reste valide mais n'est plus chargé.
- **Jeu de la semaine :** N/A (mise à jour le lundi ; aujourd'hui = vendredi).

## (d) Fichiers touchés & QC

**Fichiers servis modifiés (à publier) :**
- `codes-fisch.html` (codes : −ShootingStars ; dates 28/08)
- `codes-{grow-a-garden,blue-lock-rivals,volleyball-legends,anime-vanguards,blade-ball,blox-fruits,steal-a-brainrot,fruit-battlegrounds,king-legacy}.html` (« Vérifié le » 28/08)
- `codes-steal-an-egg.html` (bouton CTA `guidelink` → guide)
- `tier-list/steal-an-egg.html` (bouton hero « Guide complet »)
- `guides/steal-an-egg.html` (**nouveau**), `guides.html` (carte)
- `sitemap.xml`, `sitemap-guides.xml` (URL guide)
- `index.html` (date accueil), `data/codes.json` (régénéré), `tools/code-watch.json` (snapshots)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (roadmap)

**Fichiers dépréciés modifiés (sous-dossier redirigé, sans impact — éditions initiales avant découverte de l'arbre servi) :** `codes/fisch.html` + `codes/{grow-a-garden,blue-lock-rivals,volleyball-legends,anime-vanguards,blade-ball,blox-fruits,steal-a-brainrot,fruit-battlegrounds,king-legacy}.html`. Internesment cohérents (Fisch : 3 codes, 28/08). Peter peut les inclure ou les ignorer (`git checkout -- codes/`).

**QC (tout OK) :**
- ✅ Toutes les pages HTML modifiées finissent par `</html>`, `<div>` équilibrés (0), **0 null byte**, GA4 présent, nav 7 entrées (dont Avatars).
- ✅ `sitemap.xml` / `sitemap-guides.xml` finissent par `</urlset>`.
- ✅ `data/codes.json` + `tools/code-watch.json` + `data/events.json` = JSON valides.
- ✅ `node --check js/main.js` et `node --check js/events.js` OK.
- ✅ Guide `steal-an-egg` : 2 140 mots (≥1200), 3 blocs JSON-LD valides.
- ✅ Cache JS : `js/main.js` non modifié → reste `v=39`, uniforme (0 page hors v39). Pas de bump nécessaire.

---

Pour publier : dans le dossier GameNova, **supprime d'abord `.git/index.lock`** (`del .git\index.lock`), puis lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
