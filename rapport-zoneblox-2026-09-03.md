# Rapport Zoneblox — 3 septembre 2026 (jeudi)

Run quotidien automatique. Priorité tenue : vérification des **codes** d'abord, puis Directeur SEO, puis QC. Journée « propre » : après le gros audit du 2 septembre, tous les jeux chauds re-vérifiés sont **stables** (aucun changement de liste à appliquer).

---

## (a) Codes vérifiés (priorité)

**Sources croisées ce run :** Beebom (pages datées 1ᵉʳ sept.), Pocket Tactics (30/08), PCGamesN, Dexerto (1ᵉʳ sept.).

**Aucun changement de liste — tout confirmé stable :**

- **Blue Lock Rivals** — **3 actifs** : `UBERSTAKEOVER`, `KINGNEXTWEEK`, `EGODEFENSE`. **Pocket Tactics (30/08) ET Beebom (1ᵉʳ sept.) concordent exactement**, et listent bien INSANETRAILERSOON / DESTROYERMODE / RINTODAY / FIXESLATERTODAY / SORRY4DELAY!! en **expirés** → notre fiche est correcte (le conflit apparent d'hier est clos).
- **Grow a Garden** — **2 actifs** : `RDCAward`, `BEANORLEAVE10`. Beebom + PCGamesN concordent ; **`torigate` est désormais listé expiré par les deux** (conflit clos) → correctement hors liste.
- **Steal a Brainrot** — **1 actif** : `BESTBRAINROTEVER` (Dexerto, màj 1ᵉʳ sept., « one active code »). Le conflit PCGamesN d'hier est résolu → fiche correcte.
- **Fruit Battlegrounds** — **5 actifs** = liste Beebom (HIGHER1M120K, YOO1M110K!, BIGMILLIHUNNID!, ITSTHEBILLION!, CODEFIX). Aucun nouveau.
- **Stables sans re-conflit** : Blox Fruits, Volleyball Legends (3), King Legacy (7), Anime Vanguards (3), Anime Last Stand (41 — inchangé depuis la mise à niveau du 2/09), Pet Simulator 99 (0, pas de système de codes).

**Candidats en attente :** aucun nouveau. `torigate` (GAG) définitivement clos (expiré des deux sources).

**Fraîcheur :** « 🔄 Vérifié le » rafraîchi au **3 septembre 2026** sur les **178 pages** codes (idempotent, 1 par page). `tools/code-watch.json` : `lastRun` + snapshots mis à jour (blox-fruits, fruit-battlegrounds, blue-lock-rivals, grow-a-garden, steal-a-brainrot). Widget `data/codes.json` régénéré (**178 jeux, 1272 codes actifs**).

**Jeux non re-vérifiés en profondeur ce run (à prioriser demain) :** longue traîne hors « hot games » (RNG, tower defense, tycoons divers) — stables, non contredits par les agrégateurs ; et les jeux chauds secondaires (Fisch, Anime Last Stand liste longue) à re-croiser ≥3 sources au prochain passage.

## (b) Directeur SEO

- **Trending re-scanné (≥2 sources)** : leaders vérifiés — **Steal An Egg #1 (~1,77M joueurs)**, Brookhaven, Blox Fruits, Murder Mystery 2, Grow a Garden, Adopt Me — **tous couverts**. Seul top-item non couvert : **« +1 Speed Keyboard Escape | Candy & Chocolate »** (~329K joueurs), obby **sans système de codes**, déjà fiché en guide `evasion-clavier`. **Aucun nouveau hit ≥4000 avec codes non couvert** → evergreen.
- **Brique réalisée (approfondissement du cluster n°1 + correction d'orphelin) :** nouvelle page **`guides/steal-an-egg-mutations.html`** (~1 600 mots) — « Mutations Steal an Egg : liste, multiplicateurs & comment les obtenir ». Table des **5 mutations** (Silver ×1,25, Bloom ×1,5, Golden ×2, Rainbow ×2,5, Spirit Bloom ×3), Sakura Incubator (Cherry Blossom, Sakura Crystals, taux 97,5 % / 2,5 %), stratégies, FAQ.
  - **Intention distincte (anti-cannibalisation)** : *référence mécanique* (mutations/multiplicateurs), ≠ guide complet (how-to) ≠ tier list (classement pets). Aucune page existante ne visait ces head terms.
  - **Sources ≥2 croisées** : Beebom (màj 24/08) **et** games.gg / Sportskeeda / Stealthy Gaming — tous concordants sur les 5 multiplicateurs. Aucune valeur inventée ; encart « info communautaire » daté ; byline « L'équipe Zoneblox ».
  - **Schema** : Article + BreadcrumbList + FAQPage (5 Q).
  - **Maillage (anti-orphelin)** : carte hub `guides/index.html` (vraie miniature tr.rbxcdn.com 768/432) + ItemList position 54 ; entrées `sitemap-guides.xml` + `sitemap.xml` ; liens depuis `codes-steal-an-egg.html` (« Va plus loin ») et `guides/steal-an-egg.html` (articles liés). **Bonus** : la page **`guides/steal-an-egg.html` (guide de base) était orpheline du hub** (présente aux sitemaps mais sans carte) → carte ajoutée (position 53), trou de maillage corrigé.
- **Prochaine brique (J25) inscrite dans la roadmap :** enrichir la tier list Steal an Egg (meilleurs pets par biome / revenu par seconde) ou une value list pets (≥2 sources datées) ; sinon un how-to « Sakura Incubator / Great Bloom ».

## (c) Jeux ajoutés / guides / tier lists / UGC / évènements / jeu de la semaine

- **Jeux ajoutés** : aucun (aucun nouveau hit non couvert).
- **Guides** : 1 nouveau (`guides/steal-an-egg-mutations.html`) + réparation orphelin du guide de base Steal an Egg dans le hub.
- **Tier lists** : aucune nouvelle.
- **UGC** : inchangé (pas de nouveau code confirmé).
- **Encart évènements** : non modifié (encart retiré de l'accueil, cf. CLAUDE.md ; `data/events.json` non touché).
- **Jeu de la semaine** : non modifié (jeudi ; MAJ réservée au lundi).

## (d) Fichiers touchés + QC

**Fichiers modifiés / créés :**

- **178** pages `codes-*.html` (rafraîchissement « Vérifié le » → 3 septembre 2026).
- `codes-steal-an-egg.html` (lien vers le nouveau guide mutations).
- **`guides/steal-an-egg-mutations.html`** (nouvelle page, ~1 600 mots).
- `guides/index.html` (2 cartes ajoutées : guide de base + mutations ; ItemList positions 53-54).
- `guides/steal-an-egg.html` (lien réciproque vers mutations).
- `sitemap-guides.xml`, `sitemap.xml` (entrée mutations).
- `SEO-directeur-audit-roadmap-2026-07-24.md` (brique J24 + reco J25).
- `tools/code-watch.json` (lastRun + snapshots), `data/codes.json` (régénéré).

**QC (tous verts) :** chaque HTML modifié se termine par `</html>`, sitemaps par `</urlset>` ; **0 null byte** sur les 185 fichiers modifiés ; `<div>` équilibrés (0) sur la page créée et les fichiers édités ; nouvelle page = **GA4 présent + nav 7 entrées (incl. Avatars) + 3 blocs JSON-LD valides + miniature tr.rbxcdn.com réelle** ; cache JS uniforme **`main.js?v=41`** (341 réf., main.js non modifié → pas de bump) ; `tools/code-watch.json` + `data/codes.json` JSON valides ; `node --check js/main.js` + `js/events.js` OK ; nouvelle page reliée au hub + sitemaps (aucun orphelin, orphelin existant corrigé en bonus).

---

**Pour publier :** dans le dossier GameNova, lance

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
