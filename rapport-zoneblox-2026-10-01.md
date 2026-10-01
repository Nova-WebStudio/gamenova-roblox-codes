# Rapport ZoneBlox — 2026-10-01 (run 05h, jeudi)

> Full maintenance + editorial. Run planifié 03h00 UTC (05h Belgique), **exécuté avec retard** (bridge). Toutes les modifs ci-dessous sont sur disque, régénérées et QC-validées. **Rien n'est poussé sur Git (push manuel).**
> ⚠️ Les modifs des runs **09-28 et 09-29** étaient encore **non commitées** au démarrage — ce run s'est **empilé dessus** (rien d'écrasé). Le commit du jour embarquera les trois runs.

## 🗓️ DÉBUT DE MOIS
- **`sync_month.py`** exécuté : **184 pages codes** passées aux libellés **« octobre 2026 »** (title + og:title + meta description, avec élision « d'octobre »). Signal de fraîcheur SEO mensuel majeur. N'a touché que le `<head>` (règle d'honnêteté préservée).

## CODES

### Corrections réelles
- **🔧 universal-tower-defense-x** : les 18 chips affichés (thème Bleach/DBS : ArrancarSupremacy!, DBSUpdPatch!…) étaient **entièrement périmés**. Remplacés par **7 codes frais** : **Football11!, UniversalFootball!, NewBlitzPass!** (confirmés **mmoculture 01/10 + theclick 28/09 + PGG**) + **WeLoveYoruichi2!, UTDZApologyForBugs!, WeLoveUTDZ!, SrryForWhoopsie!** (mmoculture 01/10 + PGG). Compteur 18→7, verifDate 01/10. (TD à rotation rapide = faux-actifs classiques.)
- **➕ combat-warriors** : page affichait **0 code** alors que le jeu en a. Ajout de **CHAOS_AND_RAGE + OK_LATE_AGAIN** (confirmés **robloxden 01/10 + PGG 26/09**). C6NNON écarté (**expiré** selon PGG) ; C4PID/LongSchnoze109 non ajoutés (source unique). Compteur 0→2, verifDate 01/10.

### Hot games revérifiés — aucun changement (verifDate → 01/10)
- **blue-lock-rivals** (4 : SNUFFYUPD, NEWMASTER, UBERSVOTE, WSNUFFY) = Beebom 30/09 + PGG 26/09.
- **volleyball-legends** (3 : UPDATE_89, WE_CURSED, SKELETON) = Fossbytes 01/10 + Beebom 26/09.
- **grow-a-garden** (2 : RDCAward, BEANORLEAVE10) = Beebom 01/10 + PocketGamer 05/09. **torigate confirmé EXPIRÉ** (résout un point de veille).
- **anime-vanguards** (22) = **Pocket Tactics 27/09, match exact** (Beebom 01/10 n'en liste que 13 = liste partielle, pas de preuve d'expiration).
- **blade-ball** (15) = Beebom 01/09 confirme 14/15 (SERPENT gardé, pas de preuve d'expiration).
- **fruit-battlegrounds** (4) = base Pocket Tactics 22/09.

### Rotation catalogue (verifDate → 01/10)
- **brainrot-evolution** (24) : tous actifs chez Beebom 19/09 (sous-listé vs ~88 = OK, aucun faux-actif).
- **anime-dimensions-simulator** : 8/10 confirmés PGG 26/09 ; **ULTRA + HALLOWEEN gardés** (pas de preuve d'expiration ; HALLOWEEN possiblement saisonnier octobre).
- **bedwars** (0) : confirmé **sans système de codes** (playpatch + autres).
- **project-slayers** (0) : Beebom 01/10 + Pocket Tactics 29/09 = aucun code.
- **weapon-rng** (4 : UPD6, WEAREBACK, UPD4, GRAVEYARD) : tous confirmés robloxden 14/09 (sous-listé vs 10).
- `catalogVerify` MAJ (01/10) pour les 16 jeux traités.

### Non revérifié / conflits laissés en attente
- **anime-champions-simulator** : **AUCUNE source fraîche fiable** (Pocket Tactics = mars 2025). 11 chips **non touchés**, **verifDate non rafraîchie**. Priorité du prochain run.
- **anime-eternal** : sous-listé (13, Update 55) vs jeu à **Update 60P4** (PGG 01/09). Nos 13 actifs ; ajouter Update 56→60 avec 2e source.
- **steal-a-brainrot** : CONFLIT GamesRadar 03/09 (BESTBRAINROTEVER actif) vs Pocket Tactics 22/09 (aucun code). Chip gardé, à retrancher.
- **spongebob-tower-defense** : divergence Fossbytes 01/10 vs PGG 05/09 (aucun accord 2-sources) → 2 gardés, rien ajouté.

## SEO
- Aucune nouvelle URL (kill switch). Valeur du jour = **fiabilité + fraîcheur** : correction d'une page entièrement périmée (UTDX), comblement d'une page vide (combat-warriors), libellés mensuels à jour sur 184 pages.
- `sitemap.xml` régénéré : **383 URLs** (lastmod : verifDate 184, Mis à jour 11, mtime 188).

## NOUVEAUX JEUX
- Aucun ajout (kill switch : pas de titre réunissant traction + codes réels + page manquante).

## CONTENU
- Aucun guide / tier list / article créé (« 2 excellents > 20 faibles »).

## ANIIMO (data-driven)
- `lastChecked` → 01/10. **11 codes gardés.** Divergence : PGG 01/10 + Destructoid 28/09 ne listent que ANIIMOGIFT + Aniimo2026 ; nos 11 confirmés GamesRadar+PT il y a 2 jours (29/09). Codes de lancement evergreen, pas de preuve d'expiration → conservés, à surveiller. `build_site.py` relancé.

## GTA 6
- **Reveal Game Informer PUBLIÉ** (numéro sorti le 29/09 : dossier 14 pages, ~12 screenshots, **système météo avancé**, monde Leonida/Miami, interviews Rockstar). **UPDATE evergreen** : entrée ajoutée à `data/gta-6/updates.json` (confiance HIGH, sources pushsquare + techwiser), **aucune nouvelle URL**, aucun screenshot copyrighté intégré. Sortie confirmée **19 nov 2026**.

## FC 27
- Monitor. Rien de concret (SBC/promo daté) justifiant une page aujourd'hui.

## EDITORIAL INTELLIGENCE
- **Top actions du jour** : fix UTDX (page 100 % périmée corrigée), combat-warriors (page vide comblée), sync_month (184 pages).
- Articles créés : 0. Pages codes modifiées : **2 corrections** + **14 revérifications** + 184 libellés mensuels. GTA 6 evergreen enrichi.
- Sujets ignorés : marketing GTA 6 sans valeur joueur, nouveaux jeux sans traction+codes.
- `tools/editorial-intelligence.json` : meta 01/10, GTA6 → UPDATED, +topic `code-maintenance-2026-10-01`.

## EDITORIAL QUEUE
- `EDITORIAL-QUEUE.md` régénéré. URGENT : veille officielle GTA 6. À mettre à jour : anime-champions-simulator (source fraîche), anime-eternal (Update 56-60). À trancher : steal-a-brainrot, spongebob-td, aniimo. Demain : hotGames + rotation des plus anciens restants.

## QC
- `node --check js/main.js` : OK.
- JSON valides : data/codes.json (**184 jeux, 1260 codes**), data/aniimo/codes.json, data/gta-6/updates.json, tools/code-watch.json, tools/editorial-intelligence.json, data/games-index.json.
- XML valides : sitemap.xml (**383 URLs**, finit `</urlset>`) + sitemap-games.xml.
- Pages modifiées : toutes finissent par `</html>`, **0 null byte**, GA4 `G-FEL71QVHNL` présent, **div équilibrés (0 fichier déséquilibré sur tout le site)**.
- Cache JS : `main.js?v=47` cohérent (aucun fichier hors avatar/git en version différente).

---

**Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.**
