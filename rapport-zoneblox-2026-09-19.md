# Rapport Zoneblox — 19 septembre 2026 (samedi)

Run quotidien autonome. Priorité absolue tenue : vérification des **codes** d'abord (hotGames + rotation), puis brique Directeur SEO, puis régénération. Aucun `git push` effectué (Peter pousse manuellement).

---

## (a) Codes vérifiés — PRIORITÉ

### hotGames (7 vérifiés, 3 modifiés)

| Jeu | Résultat | Sources |
|-----|----------|---------|
| **Anime Last Stand** | **22 → 3 actifs** (19 déplacés en expirés) | Destructoid 15 sept. + Pro Game Guides 1er sept. concordants : seuls **MagicKnights!, ElfReincarnation!, IsItReallyWeekly?!** actifs. Beebom (liste « working » périmée, ~42) = **outlier écarté**. ALS = TD à expiration rapide → correction de faux-actifs majeure. |
| **King Legacy** | **7 → 9** (+RainbowDragon, +2MFAV) | Pocket Tactics 18 sept. + PC Gamer concordants (mêmes 9 actifs). |
| **Blade Ball** | **13 → 15** (+GOODVSEVIL, +DUNGEONSRELEASE) | GamesRadar 18 sept. + Beebom concordants sur ces 2 ajouts. Conflit SERPENT (GR actif / Beebom expiré) → **gardé** (source la plus récente prioritaire), noté. |
| Blox Fruits | 23 — stable | PCGamesN/Beebom : EASTEREXP, KITT_RESET… tous confirmés, aucun nouveau. |
| Grow a Garden | 2 — stable | PC Gamer/PCGamesN : RDCAward + BEANORLEAVE10, les seuls depuis des mois. |
| Steal a Brainrot | 1 — stable | Sources en conflit (codes très volatils) → version prudente conservée. |
| Fruit Battlegrounds | 2 — stable | Pocket Tactics : HIGHER1M120K + YOO1M110K! confirmés actifs. **EVENHIGHER!** = candidat en attente (source unique, PT du 4 sept.). |

Dates « 🔄 Vérifié le » rafraîchies au 19 sept. sur les 7 pages ; « Mis à jour le » (changelog) touché uniquement là où les codes changent vraiment.

### Rotation quotidienne (ÉTAPE 2ter) — 11 jeux examinés, jamais vérifiés

**Traités & datés (`catalogVerify` = 19 sept.) :**

| Jeu | Résultat | Sources |
|-----|----------|---------|
| **Iron Soul Dungeon** | **11 → 23 actifs** (correction MAJEURE) | Nos 11 « actifs » étaient **TOUS périmés** (Pocket Tactics 12 sept. + Beebom 18 sept. les listent en expirés). Page reconstruite sur les **23 codes actifs confirmés par les 2 sources** (intersection). |
| **Bloxstrike** | **1 → 4** | SUPERSOAKED périmé (Beebom, liste expirés) → remplacé par MICHAELSRETURN, HAPPYBDAYYUUTO, LORE, RIANOMINATED2026 (multi-sources). |
| **Catch and Tame** | **0 → 2** | Page vide enrichie : PLUSHIECODE + FISHINGCLAW (Pocket Tactics 15 sept. — 2 seuls actifs réels ; le « 36 codes » de certains trackers gonflés est faux). |
| **Dig and Clean** | **3 → 4** (+UPDATE3) | GamesRadar/PGG/Beebom concordants. |
| **Fish an Anime RNG** | 5 — confirmé OK | Sous-listage (≈10 actifs) mais aucun de nos 5 codes prouvé expiré → conservés. |

**Flaggés « à revérifier »** (source unique/ambiguë, non touchés par prudence) : **grimoires-era** (PCGamesN=2024 périmé ; ambiguïté Era vs Era 2), **twenty-one** (nos codes ≠ sources ; 19995 vs 1999 ambigu), **survive-zombie-arena** (GALACTIC/Zombies non confirmés), **spin-a-brainrot** (pas de liste datée), **be-a-brainrot** (conflit « aucun code publié » vs BRAINROT/RELEASE affichés), **button-rng-2** (page vide, pas de liste sept.).

---

## (b) Directeur SEO — 1 brique

**Trending re-scanné** : leaders evergreen (Grow a Garden, Steal a Brainrot/Egg, Blox Fruits, Rivals, 99 Nights…) tous couverts ; aucun nouveau hit ≥4000 non couvert détecté.

**Brique réalisée : clôture du cluster « Search For The Needle »** (codes ✓ · guide ✓ · **tier list ✗ → ✓**).
Création de **`tier-list/search-for-the-needle.html`** (~2 320 mots FR) :
- Classement des **10 classes S→D** (Ultimate Farmer, The Chosen One, Demolitionist, Drone Specialist, Forkmaster, Pack Mule, Hay Merchant, Hoover, Prospector, Starter) avec taux de drop, explications détaillées, stratégie Gems, conseils débutants, FAQ 6 Q.
- **Intention distincte** (classement) ≠ guide (how-to) ≠ codes (transactionnel) → **anti-cannibalisation** respecté.
- **Sourcé ≥2 datés** : Beebom (11 sept.) + games.gg (14 sept.). « The Chosen One » & « Hoover » explicitement attribués à games.gg (plus récent) ; aucune valeur inventée.
- **EEAT** : byline « L'équipe Zoneblox » + politique éditoriale ; note d'évolutivité.
- **Schema** : ItemList (10) + BreadcrumbList + FAQPage.
- **Maillage anti-orphelin** : vraie miniature `tr.rbxcdn.com`, carte hub `tier-lists.html`, `<url>` dans `sitemap.xml`, **liens croisés codes ↔ guide ↔ tier** (CTA guidelink de la page codes + bouton hero du guide pointent désormais vers la tier list dédiée).

**Roadmap mise à jour** (`SEO-directeur-audit-roadmap-2026-07-24.md`) : brique J32 inscrite ; **prochaine brique J33** = ajouter 2 vidéos oEmbed vérifiées au cluster SFTN (ou value list GAG/Blox Fruits si maintenance tenable, ou enrichissement Aniimo).

---

## (c) Jeux ajoutés / guides / tier lists / Aniimo / UGC / Jeu de la semaine

- **Jeu de la semaine** : samedi → non modifié (mise à jour le lundi uniquement).
- **Nouvelle page** : 1 tier list (Search For The Needle, ci-dessus). Aucun nouveau jeu ajouté ce run (priorité codes).
- Aniimo / UGC : non modifiés ce run.

---

## (d) Régénération automatique (ÉTAPE 7bis)

- `python3 tools/build_site.py` → pages `/games/` régénérées (sitemap-games.xml : 38 URLs).
- `python3 tools/build_home.py` → 5 sections dynamiques de l'accueil régénérées ; **idempotence confirmée** (2ᵉ passage identique).
- `python3 tools/build_codes_json.py` → `data/codes.json` : 179 jeux, **1182 codes actifs** (codes réellement modifiés ce run).
- `python3 tools/build_sitemap.py` → `sitemap.xml` : **366 URLs** (lastmod : 179 via verifDate, 11 via « Mis à jour », 176 via mtime).

---

## (e) Fichiers touchés + QC

**Pages codes modifiées (14)** : anime-last-stand, king-legacy, blade-ball, blox-fruits, grow-a-garden, steal-a-brainrot, fruit-battlegrounds, iron-soul-dungeon, bloxstrike, catch-and-tame, dig-and-clean, fish-an-anime-rng (+ search-for-the-needle via cross-link CTA).
**Nouvelle page** : `tier-list/search-for-the-needle.html`.
**Intégrations** : `tier-lists.html` (carte hub), `guides/search-for-the-needle.html` (bouton tier), `sitemap.xml`, `tools/code-watch.json` (catalogVerify + lastRun + notes à revérifier), roadmap.
**Régénérés** : `data/codes.json`, `data/games-index.json`, `games/index.html`, `sitemap-games.xml`, `index.html` (sections dynamiques).

**QC — tout vert :**
- Chaque HTML finit par `</html>`, **0 null byte**, `<div>` équilibrés (0 écart).
- Compteurs hero « X codes actifs » = nombre réel de codes actifs sur chaque page modifiée ; aucun chevauchement actif/expiré.
- `node --check js/main.js` OK ; `data/codes.json` JSON valide ; `sitemap.xml` XML valide (finit par `</urlset>`).
- GA4 (G-FEL71QVHNL) présent, nav complète (menus Roblox/Aniimo + Avatars), cache JS `v=42` sur la nouvelle page, miniature `tr.rbxcdn.com` réelle (jamais SVG en src).

---

## Pour publier

Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
