# Rapport Zoneblox — 28 juillet 2026 (mardi)

## a) Codes vérifiés (priorité absolue)

**6 jeux vérifiés** ce run (2 hot + 4 jeux flaggés au run précédent), sources : Pro Game Guides, Pocket Gamer, GamesRadar, Fossbytes, Roblox Den, Beebom, game.guide, Destructoid, PCGamesN + descriptions/officiels.

### Changement réel appliqué
- **Sakura Stand** — **CHANGEMENT RÉEL : 8 → 2 codes actifs.** La page traînait des codes périmés (dernière vraie MAJ : 15 juin). Retiré **6 codes** :
  - *Touhou, Flandre, Scarlet* → **conflit de sources** : Pro Game Guides (maj 01/07) les donne actifs, mais **Pocket Gamer (maj 18/07, plus récent)** les classe **expirés**. Codes de « The Flandre Update » (16/02), soit ~5 mois. Règle de prudence → **retirés** (ne pas publier un code douteux).
  - *NoSleep40HoursGG, Christmas2025!, NewYear2026!* → saisonniers, **confirmés expirés** par Pocket Gamer (18/07). Retirés.
  - **Conservés** : *RTZREWORK, JOJOMONTH* (listés **actifs** par Pocket Gamer, non marqués expirés ailleurs).
  - Synchro complète : compteur 8→2 (game-meta + live-banner + prose), « Mis à jour le » **et** « Vérifié le » → 28/07, JSON-LD `dateModified` → 2026-07-28, FAQ réécrite, `GAMES_INDEX` + `ALL_GAMES` + objet data de `main.js` (codes:2, dates 28/07). Page toujours **1 393 mots** (≥ 1200 ✓).
  - **Candidats en attente** (Pocket Gamer seul = 1 source, non publiés) : boohoomyfrierenbeamgotpatched, ChosoBubu, NaoyaDoopie, ThisCodeGiveRokakaka, BesureToWearVansCheckerboard, GrandOrder, TypingMoon, deathduriyay67, SireisSupervision, 50ktoken, EVILRESTV5 → à confirmer par ≥3 sources OU officiel.

### Vérifiés sans changement (« Vérifié le » rafraîchi au 28/07)
- **Grimoires Era** : 11 actifs (SorryShutdown, GGgames, SorryBugs2/3/4, Guizera, WEAPOLOGIZE, Release, FunzyLabs, GrimoiresEra2, GameOpen) — **identiques** sur Pocket Gamer + Fossbytes + Roblox Den + Beebom. Aucun changement.
- **Re:Rangers X** (`anime-rangers-x`) : nos **15 codes tous confirmés ACTIFS** par PGG (maj 13/07). Aucun expiré → aucun retrait. PGG liste **15 codes actifs supplémentaires** (AdminAbuseNeedsABuff, Capsules?!?, SummerTime, delaRXy, SHADOWAA, ShadowPatched, LEVELING, ABYSSALDELAY, CATCHINGUP, ECLIPSESORRYFORDELAYS, SACRIFICE, THESAGEKING, SINGULARITY, HOLYGRAIL, BOSSEVENT) → **en attente** (1 source propre, à confirmer ≥3 sources OU Trello/Discord officiel avant publication).
- **Blue Lock Rivals** : 9 actifs (SEMIFINALS/WORLDTOURNAMENTPART3/NEWMAP + QOLUPD/QUARTERFINALSOON/REBALANCES/NELSHIDOU/NEWCHEMSOON/DEMON). Cohérent PGG/GamesRadar/Fossbytes/PCGamer. Aucun nouveau code depuis la MAJ du 25/07.
- **Grow a Garden** : aligné (les sources confondent souvent GAG et GAG2 ; TEAMGREENBEAN est un code GAG2). Aucun changement.
- **DIG** : **conflit persistant** — game.guide affiche « 8 actifs » (liste client-rendue, non extractible en HTML statique), Pocket Gamer historiquement prudent. Page maintenue sur **plsdevshovel** seul (prudence). À trancher via Discord officiel DIG.

### Jeux non revus ce run (à prioriser au prochain)
Catalogue = **176 pages codes**. Couvert ce run : Sakura Stand, Grimoires Era, Re:Rangers X, DIG, Blue Lock Rivals, Grow a Garden (+ re-scan trending des autres hot, inchangés depuis le 27/07). Reste à traiter : anime-* (hors ceux ci-dessus), tower defense, simulateurs, UGC (ugc-limited), RNG. `code-watch.json` : `lastRun` = 2026-07-28.

## b) Directeur SEO (autorité topicale)

- **Trending re-scanné (web)** : leaders — Grow a Garden 2 (#1), Steal a Brainrot, Brookhaven (~639K), Blox Fruits (~203K pic), Animal Hospital, Evomon — **tous déjà couverts** (Evomon et Animal Hospital vérifiés présents au catalogue). Aucun nouveau hit ≥4000 joueurs manquant → approfondissement autorité (conforme roadmap J6).
- **Brique du jour (J6)** : nouveau **hub éditorial `meilleurs-jeux-roblox.html`** (« Meilleurs jeux Roblox à jouer maintenant — été 2026 », **~1 890 mots**).
  - **Intention ciblée** : head terms « meilleurs jeux roblox », « jeux roblox populaires / tendance », « top jeux roblox 2026 » — intention **découverte/navigation**.
  - **Anti-cannibalisation** : distincte des pages codes (transaction), guides (how-to) et tier lists (classement d'items). **Aucune page existante** ne visait ces head terms (vérifié : aucun hub `meilleur/best/tendance/top` préexistant).
  - **Effet SEO principal** : maillage transversal — le hub distribue de l'equity vers **18 pages jeu** du catalogue, avec pour chacune les liens codes + guide + tier list (quand ils existent).
  - **Roster sourcé** (palmarès « most played / top games » juillet 2026) : Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Blade Ball, Blue Lock Rivals, Volleyball Legends, Anime Vanguards, Fisch, Fruit Battlegrounds, Grow a Garden, Animal Hospital, Adopt Me, 99 Nights in the Forest, DIG, Pet Simulator 99, Anime Last Stand, Evomon.
  - **EEAT / honnêteté** : encart méthodologie + date (28/07) + byline « L'équipe Zoneblox » + mention explicite que le classement évolue ; **aucun compteur inventé** (chiffres uniquement quand sourcés — Brookhaven ~639K, Blox Fruits ~203K).
  - **Schema** : BreadcrumbList + ItemList (18) + FAQPage (3/3 valides).
  - **Maillage (anti-orphelin)** : **vraies miniatures tr.rbxcdn.com**, lien depuis l'accueil (section « Jeux & codes »), `sitemap-pages.xml` + `sitemap.xml`.
- **Prochaine brique inscrite (J7 — 29/07)** : renforcer le maillage du hub (liens réciproques depuis les hubs codes/guides/tier-lists) **ou** second hub « Nouveaux jeux Roblox (2026) » (intention *nouveauté* distincte de *popularité*) ; à défaut, guide GAG « weather / météo ».

## c) Autres maintenances
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-28. Aucune `datetime` ponctuelle passée (tous récurrents ou `no-fixed-time`). Entrée **Blue Lock Rivals** actualisée : « MAJ Quarts de finale (teasée) » → « Prochaine MAJ (Tournoi mondial) », watch mis à jour (demi-finales déployées le 25/07, suite non datée). JSON validé, `js/events.js` `node --check` OK (non modifié → pas de bump propre).
- **Jeu de la semaine** : mardi → **non touché** (mise à jour le lundi uniquement).
- **Jeux ajoutés / guides / tier lists / UGC** : aucun ce run (priorité codes + brique hub SEO).

## d) Fichiers touchés + QC

**Créé :** `meilleurs-jeux-roblox.html` (hub éditorial).
**Modifiés (codes, changement réel) :** `codes/sakura-stand.html` (8→2), `js/main.js` (2 entrées Sakura), `codes/index.html` (ALL_GAMES Sakura).
**Modifiés (codes, « Vérifié le » → 28/07, sans changement) :** `codes/grimoires-era.html`, `codes/anime-rangers-x.html`, `codes/dig.html`, `codes/blue-lock-rivals.html`, `codes/grow-a-garden.html`.
**Modifiés (SEO/maintenance) :** `index.html` (lien vers le hub), `sitemap-pages.xml`, `sitemap.xml`, `data/events.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`.
**Modifiés (cache) :** **323 fichiers .html** bumpés `main.js?v=35` → **`v=36`** (car `js/main.js` modifié).

**QC — tous verts (331 fichiers scannés) :**
- 0 null byte ; toutes les pages HTML finissent par `</html>` ; sitemaps par `</urlset>` ; `<div>` équilibrés partout (diff 0).
- `node --check` OK (`main.js`, `events.js`) ; JSON valides (`events.json`, `code-watch.json`).
- Cache **uniforme** : 0 fichier resté en `v=35`, 323 en `v=36`.
- `GAMES_INDEX` ↔ `ALL_GAMES` **parfaitement synchronisés** (0 manquant des deux côtés) ; compteur Sakura (2) cohérent dans les 3 sources de données.
- Hub : nav 7 entrées (dont Avatars) + GA4 + canonical propre + 3 JSON-LD valides + 18 cartes à **vraie miniature tr.rbxcdn.com** + `main.js?v=36`.
- Sakura Stand : **1 393 mots** visibles (≥ 1200 ✓).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
