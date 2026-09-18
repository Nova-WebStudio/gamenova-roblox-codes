# Rapport Zoneblox — 18 septembre 2026 (vendredi)

## (a) Codes vérifiés — PRIORITÉ

### hotGames (confirmés, « Vérifié le » → 18 sept.)
Aucun changement de code nécessaire — pages exactes/conservatrices, aucune expiration prouvée.

| Jeu | Statut | Sources |
|-----|--------|---------|
| Grow a Garden | 2 exacts (RDCAward, BEANORLEAVE10) | PGG 17/09 + Beebom + PCGamesN (3 sources concordantes) |
| Steal a Brainrot | 1 exact (BESTBRAINROTEVER) | GamesRadar 03/09 + Dexerto (confirmé unique actif) |
| Blue Lock Rivals | 3 exacts (NIKOHERE, GATEKEEPOVER, QOLNEXTWEEK!) | PGG 15/09 (table active = 3) |
| Volleyball Legends | 3 exacts (UPDATE_87, RONIN_RETURN, KATANA) | GamesRadar 17/09 |
| Fisch | 3 exacts (scarlet, TemporarySubmarine, CARBON) | game8/PCGamer 17/09 |
| Anime Vanguards | 8 (Assault, SummerLeaving, AnniNextHopefully, MiniUpd2, Wrath…) | Pocket Tactics/GamesRadar 16/09 |

**Candidats en attente (`_pending`)** : Grow a Garden — **FREESEED / STORY / STARBUD** (PGG seul le 17/09, source unique → non publiés) ; **torigate** laissé expiré (PGG actif MAIS Beebom + PCGamesN concordants sur expiré → prudence).

### Lot de rotation du jour (ÉTAPE 2ter) — 11 slugs traités

**Corrections réelles (2) :**
- **be-a-fish-bait** — correction majeure de faux-actifs : nos **8 « actifs » tous périmés** (BAITAURA, 4000/2500CCU/2000/1500/1000/500LIKES, OFFICIAL) → déplacés en expirés, remplacés par les 2 vrais actifs **HOOLALALA + SHARDS**. Compteur 8→2. Sources : PGG 01/09 + PC Gamer + Beebom.
- **anime-card-farm** — page vide (0) alors que 4 actifs → ajout **BRUTALCOMEBACK!, PRODUCTION!, TRAITS!, POTIONS** (0→4). Sources : Dexerto 10/09 + PGG 01/09 concordants. *(TRADING! écarté = source unique.)*

**Confirmés OK, sous-listage acceptable (9), « Vérifié le » → 18 sept. :** wizard-alchemy (10/10 actifs), anime-stars (6/6 actifs), dig (1 exact), search-for-the-needle (2 exacts), evomon (4/4 actifs), encounters (IKES=515 cristaux confirmé), steal-a-fish (ADMINFISH confirmé), dungeon-quest-reborn (0 = pas de système de codes), kick-a-lucky-block (0 = pas de système de codes).

**⚠️ À revérifier au prochain run (laissés intacts, non tamponnés) :**
- **grimoires-era** — aucune source datée 2026 fiable (PCGamesN = 2024 périmé) ; 4ᵉ report.
- **bloxstrike** — codes à usages limités (MICHAELSRETURN/HAPPYBDAYYUUTO) non confirmables sans risque ; SUPERSOAKED probablement expiré.
- **be-a-brainrot** — conflit : sources indiquent « aucun code actif » vs BRAINROT/RELEASE affichés.
- **catch-and-tame** — page vide mais ~36 codes actifs existent (PC Gamer/PGG 08/09) → **à ENRICHIR** (MOUNTAINUPDATE, WEATHERMACHINE…).
- **button-rng-2** — page vide ; aucune liste datée sept. 2026 fiable trouvée.

## (b) Directeur SEO — brique du jour

**Trending re-scanné** (rblxdb/roblox charts 16/09) : #1 Steal An Egg (~1,7M, couvert), leaders evergreen tous couverts, **aucun nouveau hit ≥4000 non couvert**.

**Brique = approfondissement du cluster « Search For The Needle »** (hit ~38K CCU, page codes créée au J30 mais orpheline de cluster).
→ Création de **`guides/search-for-the-needle.html`** (~1 690 mots FR). **Intention how-to distincte** (comment jouer / meilleures classes / gemmes / pets) ≠ intention transactionnelle de la page codes → **aucune cannibalisation**. Sourcé ≥2 (Pocket Tactics 17/09 + PGG/games.gg). Schema Article + BreadcrumbList + FAQPage. Maillage : carte hub `guides.html`, `<url>` sitemap, **liens croisés codes ↔ guide** + ajout du bandeau **CTA `data-cta="guidelink"` manquant** sur la page codes.

**Prochaine brique (J32)** inscrite dans la roadmap : tier-list SFTN (classes) → compléter le cluster ; puis catch-and-tame ; puis grimoires-era.

## (c) Jeux ajoutés / guides / tier lists / UGC / jeu de la semaine
- Nouveau **guide** : `guides/search-for-the-needle.html` (voir ci-dessus).
- Aucun nouveau jeu, tier list, ni UGC ce run.
- **Jeu de la semaine** : non touché (nous sommes vendredi ; MAJ le lundi uniquement).

## (d) Fichiers touchés + QC
**Édités :** codes-{grow-a-garden, steal-a-brainrot, blue-lock-rivals, volleyball-legends, fisch, anime-vanguards, wizard-alchemy, anime-stars, dig, search-for-the-needle, evomon, encounters, steal-a-fish, dungeon-quest-reborn, kick-a-lucky-block, anime-card-farm, be-a-fish-bait}.html ; guides.html ; **nouveau** guides/search-for-the-needle.html ; tools/code-watch.json ; sitemap.xml ; data/codes.json (régénéré : 179 jeux, 1179 codes) ; SEO-directeur-audit-roadmap-2026-07-24.md.

**QC — tout au vert :**
- ✅ Tous les HTML finissent par `</html>`, **0 null byte**, balises `<div>` équilibrées (be-a-fish-bait : imbalance +1 détectée puis corrigée).
- ✅ `data/codes.json` JSON valide · `tools/code-watch.json` JSON valide · `sitemap.xml` XML valide (finit par `</urlset>`, 335 URLs).
- ✅ `node --check js/main.js` OK. Cache JS uniforme **v=42** sur 342 fichiers (js/main.js non modifié → pas de bump).
- ✅ Guide SFTN : nav 7 entrées (Avatars incl.), GA4, 3 JSON-LD valides. Page codes SFTN : `data-cta="guidelink"` présent (1 seul).
- ✅ `catalogVerify` mis à jour (11 slugs) ; `verifDate` unique par page.

⚠️ *Note : le dépôt contient aussi le travail non poussé du J30 (17/09) — le commit ci-dessous inclura les deux runs.*

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
