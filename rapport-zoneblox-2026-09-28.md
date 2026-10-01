# Rapport ZoneBlox — run 05h00 du 2026-09-28 (lundi)

**Mode :** FULL MAINTENANCE + EDITORIAL. Fenêtre de recherche : 12–24 h (nuit).
**Résultat net :** +24 codes actifs (data/codes.json : **1274** codes / 184 jeux). 10 pages codes modifiées, 3 fichiers de mémoire éditoriale à jour, QC intégral OK.

---

## CODES

### hotGames (priorité absolue)
- **anime-vanguards — FIX MAJEUR.** La page n'affichait que **4 codes actifs** alors que **19 codes réellement actifs** étaient à tort classés « expirés » (incohérence héritée + arrays JS désynchronisés). Rebuild complet → **22 codes actifs**, double-source concordante **Pocket Tactics (27 sept) + Pocket Gamer (26 sept)**, orthographe vérifiée sur les deux. `100thTournament` déplacé en expiré (code d'event, absent des 3 sources fraîches complètes). Arrays JS `ACTIVE`/`EXPIRED` resynchronisés, badge et `verifDate` corrigés.
- **blade-ball** — ajout `BATTLEROYALE` (Pocket Tactics 22 + Beebom 1). Page 14 → **15**.
- **blue-lock-rivals** — aucun changement (SNUFFYUPD / NEWMASTER / UBERSVOTE / WSNUFFY = Beebom 26 + Pro Game Guides 26). Rotation quasi quotidienne, date rafraîchie.
- **grow-a-garden** — aucun changement (RDCAward / BEANORLEAVE10 ; Pocket Gamer 5 + Beebom 1).
- **steal-a-brainrot** — aucun changement (BESTBRAINROTEVER ; Dexerto 1 + GamesRadar 3).
- **volleyball-legends** — aucun changement (UPDATE_88 / GET_SLIMED / XP_BOOST ; GamesRadar 21).
- **fruit-battlegrounds** — aucun changement (4 codes ; Pocket Tactics 22).
- **anime-last-stand** — 3 codes maintenus (MagicKnights! / ElfReincarnation! / IsItReallyWeekly?!), confirmés actifs par PGG 1 + Beebom 1.

### Lot de rotation (non-hot)
- **driving-empire** — ajout `UWU` / `2MLIKES` / `200KMEMBERS` (Pocket Tactics 23 + Beebom 19). Page 2 → **5**.
- **dress-to-impress** (prioritaire, non fait le 27) — les 27 codes tous reconfirmés (PC Gamer 21 + GamesRadar 18 + Beebom 12) ; ajout `CH00P1E_B4CK_AGA1N` (PCG 21 + GR 18) + `10BILLION` (GR 18 + Beebom 12). Page 27 → **29**.
- **forsaken** / **dead-rails** — 0 code confirmé (aucun système de codes ; Beebom 1 / PGG 1).
- **the-strongest-battlegrounds** — 0 code récompense (uniquement des sound-IDs).
- `catalogVerify` rafraîchi pour 13 jeux au total.

### Codes ajoutés (net)
anime-vanguards +18 · dress-to-impress +2 · blade-ball +1 · driving-empire +3 → **+24**.

### Codes expirés / rétrogradés
`100thTournament` (anime-vanguards) → expiré.

### Candidats en attente (non publiés — sourcing insuffisant)
- `AIRDROP` (driving-empire) : PT 23 actif / Beebom 19 inactif → conflit.
- `GOODVSEVIL` (blade-ball) : Beebom seul.
- `HOTFIXESARECUTE`, extras anime-last-stand : source unique ou conflit.
- Aniimo : `aniimonow` / `anywhereaniimo` / `anythinganiimo` / `aniimazingfroyo` (Beebom seul ; PC Gamer les omet).

### Sources officielles
Trello Blue Lock Rivals / Blade Ball privés ou sans codes (état inchangé). Vérifs de ce run basées sur croisement médias fiables (Pocket Tactics, Pocket Gamer, Beebom, PC Gamer, GamesRadar, Pro Game Guides, Dexerto).

---

## SEO
- **Tendance travaillée :** correction de sous-listage sur 2 hotGames à forte intention (« anime vanguards codes », « dress to impress codes »). Impact SEO direct : pages passées de listes quasi vides à des listes complètes et fraîches (fraîcheur + complétude = signaux de qualité).
- **Intention :** « codes actifs [jeu] » (intention transactionnelle claire, existante).
- **Anti-cannibalisation :** aucune nouvelle URL créée — UPDATE des pages fortes existantes (règle Update-before-Create respectée).
- **Prochaine brique :** UPDATE evergreen GTA 6 dès le reveal (~29 sept), sans nouvelle URL.

---

## NOUVEAUX JEUX
Aucun ajout. Kill switch appliqué : aucun nouveau jeu ne réunit traction réelle + codes réels + absence de page. Grow a Garden / Steal a Brainrot dominent (déjà couverts).

---

## CONTENU
- Guides / tier lists / articles : aucune modification (aucune évolution réelle le justifiant — règle « 2 excellents > 20 faibles »).
- Mises à jour : 10 pages codes (voir section CODES) + homepage (date Aniimo codée en dur dans `tools/build_home.py` synchronisée 18 → 28 sept).

---

## ANIIMO
Data-driven (`data/aniimo/codes.json`). **11 codes actifs tous reconfirmés** (PC Gamer 24 + Beebom 25). `lastChecked` → 28 sept, aucun changement de contenu. Les 4 codes Beebom-seul restent en attente d'une 2e source. `Aniimo2026` (récompense en conflit) inchangé. Pages régénérées via build_site.py (pas d'édition directe de /games/).

---

## GTA 6
**URGENT — reveal Game Informer imminent (~29 sept)** : 14 pages, 12 nouveaux screenshots, détails Rockstar (Push Square, GamingBible, RockstarINTEL). Aujourd'hui = pré-reveal → **rien publié** (kill switch). Dès la parution : **UPDATE de la page evergreen GTA 6** (screenshots + détails concrets), **pas de nouvelle URL**, en séparant CONFIRMÉ / RAPPORTÉ / RUMEUR. Sortie du jeu confirmée le 19 nov. 2026.

---

## FC 27
Post-lancement. Promo de lancement **Destined for Glory** (DFG) et calendrier promos Saison 1 connus. Aucune SBC / promo concrète nouvelle justifiant une page ou une MAJ aujourd'hui → **monitor**.

---

## EDITORIAL INTELLIGENCE
- **Top opportunité du run :** correction anime-vanguards (fort volume de recherche, page qui trompait les joueurs).
- **Tendances :** GTA 6 reveal (imminent), Roblox Fall Games Preview (monitor, pas de page).
- **Articles créés :** 0 (kill switch).
- **Pages mises à jour :** 10 pages codes + homepage.
- **Sujets ignorés :** Roblox Fall Games / Everywhere / RELL Seas (kill switch).
- **À surveiller :** conflit anime-last-stand (Beebom 20+ vs PGG 3) ; sols-rng (sources stale) ; Prepare/Miniupdate1 (anime-vanguards, PT27 les omet).
- `tools/editorial-intelligence.json` : topic `code-maintenance-2026-09-28` ajouté ; GTA6 + Aniimo mis à jour (15 topics).

---

## EDITORIAL QUEUE
`EDITORIAL-QUEUE.md` régénéré. En résumé :
- **🔥 Urgent :** GTA 6 (UPDATE evergreen dès reveal ~29).
- **🟢 À publier :** rien (kill switch).
- **🛠️ À mettre à jour :** anime-last-stand (tiebreak), sols-rng, grosses listes (anime-astral 100 / dragon-blox 82 / anime-battle-rng 35 / clover-retribution 14).
- **📅 Demain (29 sept, mardi) :** GTA 6 (si reveal paru) → codes hotGames → anime-last-stand tiebreak → sols-rng → rotation (ro-ghoul, bedwars, project-slayers, combat-warriors, anime-champions/dimensions/eternal/origins).

---

## QC
- `node --check` : main.js **OK**, events.js **OK**.
- JSON valides : codes.json, code-watch.json, editorial-intelligence.json, aniimo/codes.json, games-index.json — **tous OK**.
- Sitemaps XML valides : sitemap.xml (**383 URLs**), sitemap-games.xml (**40 URLs**) — **OK**.
- 10 pages éditées : fin `</html>`, **0 null byte**, `<div>`/`</div>` équilibrés, CTA `guidelink` unique, nb `<code>` = nb boutons Copier — **toutes OK**.
- Extraction build_codes_json cohérente avec les pages (anime-vanguards 22, dress-to-impress 29, blade-ball 15, driving-empire 5).
- Régénération dans l'ordre : build_site → build_home → build_codes_json → build_sitemap — **OK**.
- **Correctif technique :** suppression d'un `.git/index.lock` périmé (vide, artefact du sandbox) qui aurait bloqué le `git add`/`commit` manuel. `git add -A` re-testé → OK.

### Points signalés (non bloquants, à traiter par toi si souhaité)
- **Jeu de la semaine (spec §30) = N/A** : le bloc `<!-- FEATURED-WEEK-START/END -->` **n'existe plus** dans le site (homepage refondue le 18 sept, sections auto-générées « Jeux du moment » via build_home.py). Aucun bloc à mettre à jour ; à réimplémenter si tu veux conserver cette feature.
- **driving-empire** : page codes sans bandeau CTA `guidelink` (préexistant, pas de guide/tier list associés).

---

**Pour publier :** dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
