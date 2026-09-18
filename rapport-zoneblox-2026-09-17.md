# Rapport Zoneblox — 17 septembre 2026 (jeudi)

Sandbox bash de nouveau opérationnelle → toutes les régénérations (`build_codes_json.py`, `build_sitemap.py`, `node --check`) exécutées ce run.

## (a) Codes — PRIORITÉ

### hotGames — 3 corrections réelles + confirmations

| Jeu | Action | Sources |
|-----|--------|---------|
| **Blue Lock Rivals** | Rotation Niko : nos 4 codes (NELKING, NIKOSOON, UBERSMONTH, SORRYLOADING) désormais tous inactifs → remplacés par **NIKOHERE, GATEKEEPOVER, QOLNEXTWEEK!** ; 4 déplacés en expirés ; compteur 4→3 ; changelog corrigé | Pro Game Guides (15 sept.) + GamesRadar (14 sept.) |
| **Blox Fruits** | `Lightningabuse` déplacé en expiré | Beebom (13 sept.) |
| **Anime Vanguards** | Ajout de 5 actifs confirmés : MiniUpd2, Wrath, Retribution, 1DayDelay, 25thHour ; 3→8 | Pocket Tactics (16 sept.) + GamesRadar |

**Confirmés stables (« Vérifié le » rafraîchi au 17 sept., aucun changement de codes) :** Grow a Garden (2), Steal a Brainrot (1), Blade Ball (13), Volleyball Legends (3 — ⚠️ UPDATE_86/HAKKA_RETURN/SPIKER/UPDATE_85/SHIRO/BLOCKED sont **expirés** d'après GamesRadar, ne pas les rajouter malgré les snippets de recherche), Fisch (3 — LittleBudlingUpdate confirmé expiré).

### Rotation quotidienne (ÉTAPE 2ter) — 18 jeux non-hot vérifiés en profondeur

**3 corrections réelles :**
- **Fire Force Online** : nos 3 codes (REIGNITION, REIGNITION2, 55KLIKES) tous listés expirés (Roblox Den, vérif du jour) → remplacés par **MOREFRAMES** (page Roblox officielle) + **LEAKPATCHED** (≥2 sources) ; ENDGATEKEEP tenu en attente (source unique). 3→2.
- **Jujutsu Infinite** : page à 0 code alors que **HELLO_JJI** (50 Spins) est actif (PGG « Active (1) »). ⚠️ 400K_SUBS/JUDGEMAN_REWORK/JUDGE_SOON vus en snippet sont en fait *inactifs* (conflit évité). 0→1.
- **Evade** : page à 0 code alors que **HAPPY4THBIRTHDAYEVADE** (40 Points) est actif (GamesRadar/PGG/PocketTactics). 0→1.

**Confirmés OK (sous-listage acceptable, `catalogVerify` + « Vérifié le » au 17 sept.) :** mad-city (6), car-crushers-2 (6), anime-story-2 (17), restaurant-tycoon-3 (11), war-tycoon (4), untitled-attack-on-titan (6), pressure (4), sonic-speed-simulator (8), strongman-simulator (8), anime-souls-simulator-x (3), anime-warriors-iii (0 = pas de système de codes), adopt-me / brookhaven / tower-of-hell / work-at-a-pizza-place (0 = jamais eu de codes).

**⚠️ À revérifier au prochain run :** **grimoires-era** (collision de nom Era / Era 2 / Legacy / Clover ; les sources datées de sept. portent sur d'autres jeux — désambiguïser via placeId avant tout retrait).

## (b) Directeur SEO — brique ÉTAPE 2bis (trending d'abord)

Re-scan trending → 1 gros hit **non couvert** confirmé : **Search For The Needle** (~38 000 joueurs en simultané, pic 85K ; Garage Games ; universeId 10756011174 ; sorti le 23/08/2026).

**Brique = nouvelle page ÉTAPE 1 : `codes-search-for-the-needle.html`** — 1857 mots FR, vraie miniature `tr.rbxcdn.com`, codes **WEATHER** (120 Gems) + **PETS** (200 Gems + boost x2 Luck) actifs, **ALIEN** expiré (GamesRadar 17 sept.), description/mécaniques développées, 7 astuces, FAQ 4 questions, section « À propos », schémas BreadcrumbList + FAQPage.
- **Intention distincte** (transaction « codes <jeu> »), **aucune cannibalisation** (aucune page existante).
- **Intégrations** : carte `index.html` (const GAMES), carte `tous-les-codes.html`, `GAMES_INDEX` + `ROBLOX_THUMBS` + `ROBLOX_UNIVERSE_IDS` (js/main.js), `<url>` `sitemap.xml`.
- **Limite honnête** : pas de vidéos oEmbed (accès YouTube refusé dans ce run non-interactif) ; pas encore de guide/tier-list dédiés — inscrits comme prochaine brique (J31) dans la roadmap.

## (c) Autres

Jeux ajoutés : 1 (Search For The Needle). Guides/tier lists créés : 0. UGC : non touché. **Jeu de la semaine :** non modifié (nous sommes jeudi, pas lundi).

## (d) Fichiers touchés + QC

- **Pages codes modifiées** (codes) : blox-fruits, blue-lock-rivals, anime-vanguards, fire-force-online, jujutsu-infinite, evade.
- **Pages codes** (« Vérifié le » seul) : grow-a-garden, steal-a-brainrot, blade-ball, volleyball-legends, fisch, mad-city, car-crushers-2, anime-story-2, restaurant-tycoon-3, war-tycoon, untitled-attack-on-titan, pressure, sonic-speed-simulator, strongman-simulator, anime-souls-simulator-x, anime-warriors-iii, adopt-me, brookhaven, tower-of-hell, work-at-a-pizza-place.
- **Nouvelle page** : codes-search-for-the-needle.html.
- **Données/intégration** : js/main.js (+3 entrées, `node --check` OK), tous-les-codes.html (+1 carte), index.html (+1 entrée GAMES, JSON valide), sitemap.xml (+1 URL, régénéré → 334 URLs, XML valide), data/codes.json (régénéré → 179 jeux, 1181 codes actifs), tools/code-watch.json (catalogVerify +18, JSON valide), SEO-directeur-audit-roadmap (brique J30 + prochaine brique J31).
- **Cache JS** : bump uniforme **main.js?v=41 → v=42** sur 341 fichiers HTML (0 fichier resté en v=41).

**QC :** 0 null byte sur tout le site ; toutes les pages finissent par `</html>` (sitemap `</urlset>`) ; `<div>` équilibrés sur toutes les pages codes ; GA4 + nav présents sur la nouvelle page ; `node --check js/main.js` OK ; `data/codes.json` et `sitemap.xml` valides ; ≥1200 mots sur la nouvelle page (1857).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
