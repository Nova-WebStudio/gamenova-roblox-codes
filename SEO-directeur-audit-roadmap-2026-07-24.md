# ZoneBlox — Audit SEO & Roadmap (Directeur SEO)

**Date :** 24 juillet 2026 · **Langue primaire retenue :** Français (moat existant ; EN plus tard) · **KPI unique :** faire croître chaque jour l'autorité topicale de ZoneBlox.

---

## 1. Décision stratégique validée

Le mandat déclarait l'anglais en langue primaire, mais le site réel est **100 % français** (`html lang="fr"`, ~300 pages indexées, dossier `en/` réduit à 3 fichiers). Décision prise avec Peter : **rester français-first**. Raison SEO : la SERP Roblox anglophone est saturée d'acteurs très établis (Pro Game Guides, Beebom, Pocket Tactics, GamesRadar, Dexerto). Le français est un marché où ZoneBlox a déjà de l'autorité et bien moins de concurrence — c'est là que le ROI marginal est le plus élevé. L'anglais reste une phase ultérieure (via `/en/` + hreflang propre), pas une priorité 2026.

---

## 2. État des lieux (audit de couverture)

| Cluster | Pages | Lecture SEO |
|---|---|---|
| Codes | 173 | Colonne vertébrale du site, rafraîchie quotidiennement. Solide. |
| Tier lists | 65 → **66** | Bon maillage, vraies miniatures. Peu de sous-tier-lists par jeu (opportunité). |
| Guides complets | 56 | Piliers longs (ex. Blox Fruits 2 556 mots). Qualité correcte. |
| Encart évènements | 1 (accueil) | Nouveau : comptes à rebours restocks/admin abuses (GAG, Steal a Brainrot). |

**Forces** : fraîcheur (run quotidien), maillage codes↔tier↔guide, honnêteté éditoriale (règles anti-invention), vraies miniatures Roblox, JSON-LD présent.

**Faiblesses / dettes** :
1. **Profondeur de cluster faible.** Chaque jeu = ~3 pages (codes/tier/guide). Les jeux phares méritent des sous-entités (races, awakening, value list, boss, builds) — c'est là que se gagne l'autorité topicale.
2. **Risque de cannibalisation** si on fragmente mal : les guides piliers couvrent déjà beaucoup de sous-sujets en H2. Toute sous-page doit cibler une **intention distincte** (ex. « tier list des races » ≠ « guide »), et s'interlier au pilier.
3. **Intentions éditoriales/hub non couvertes** : « meilleurs jeux Roblox », « nouveaux jeux Roblox », « jeux Roblox tendance », value lists / trading — fort volume, peu ou pas présents.
4. **Anglais** : `en/` orphelin (3 pages) — soit l'assumer plus tard proprement, soit le retirer de l'index pour éviter du thin content.

---

## 3. Analyse « trending » (avant tout evergreen)

Vérifié ce jour : les leaders actuels sont **déjà couverts** (Grow a Garden 2 #1, Steal a Brainrot, 99 Nights in the Forest, Animal Hospital, Brookhaven, Blox Fruits). **Pas de gros jeu neuf non couvert** à ce run. Conséquence : la priorité du jour bascule légitimement de « nouveau jeu » vers **approfondissement des clusters phares** (conforme à la règle « si rien de neuf, améliore l'existant »). À re-vérifier chaque jour — un nouveau hit Roblox peut surgir en 48 h.

---

## 4. Scoring des opportunités (framework ROI)

Score = Potentiel trafic (1-5) × Valeur topicale (1-5) − Difficulté (1-5), pondéré par Fraîcheur. Top opportunités :

| # | Opportunité | Trafic | Autorité | Difficulté | Priorité | Statut |
|---|---|:--:|:--:|:--:|:--:|---|
| 1 | **Blox Fruits — sous-cluster** (races ✓, value list, awakening en page dédiée, best build) | 5 | 5 | 2 | **★★★★★** | Races **FAIT aujourd'hui** |
| 2 | Hub éditorial « Meilleurs jeux Roblox (mois) » + « Nouveaux jeux Roblox » | 5 | 4 | 3 | ★★★★☆ | À faire |
| 3 | Value / Trading lists (Blox Fruits, Adopt Me, Murder Mystery 2, Grow a Garden) | 5 | 4 | 3 | ★★★★☆ | À faire (maintenance requise) |
| 4 | Sous-tier-lists par jeu phare (Blox Fruits swords, GAG pets/seeds, AV units) | 4 | 4 | 2 | ★★★★☆ | Swords **FAIT le 25/07** ; GAG pets/seeds + AV units à faire |
| 5 | Cluster « comment awaken / débloquer » (verbes d'intention) sur top jeux | 4 | 4 | 2 | ★★★☆☆ | À faire |
| 6 | Nettoyage `en/` orphelin (noindex ou plan hreflang) | 2 | 3 | 1 | ★★★☆☆ | À arbitrer |
| 7 | Grow a Garden — cluster (mutations, weather, calculator, value) | 5 | 5 | 3 | ★★★★☆ | Tier list **pets GAG2 FAITE le 26/07** ; mutations + value à faire |

---

## 5. Travail exécuté aujourd'hui

**Nouvelle page : `tier-list/blox-fruits-races.html`** (Blox Fruits Race Tier List, juillet 2026).
- **Intention distincte** ciblée : « meilleure race blox fruits », « blox fruits race tier list », « blox fruits v4 » — sans cannibaliser le guide (qui garde l'intention how-to) ni la tier list des fruits.
- Classement sourcé (multi-sources : ssegold, bloxfruitsai, gamingpromax, poxelio) : S = Draco, Ghoul · A = Cyborg, Angel, Rabbit · B = Human, Shark · C = Mink. Nuances honnêtes (Shark = S pour le farm en mer).
- 2 009 mots, sections « meilleure race par objectif », « débloquer le V4 » (prérequis marqués comme évolutifs → renvoi wiki, aucune invention), FAQ 6 questions.
- **EEAT** : byline équipe, politique éditoriale liée, ton d'expérience réelle.
- **Schema** : ItemList + BreadcrumbList + FAQPage (tous validés).
- **Maillage** : carte ajoutée au hub `tier-lists.html` ; boutons + « articles liés » croisés depuis `tier-list/blox-fruits.html` ; liens sortants vers codes + guide Blox Fruits ; entrées ajoutées à `sitemap-tier-list.xml` et `sitemap.xml`.
- **QC** : 0 null byte, `</html>` OK, `<div>`/`<section>` équilibrés, GA4, nav 7 entrées, `main.js?v=35`.

Effet топ­ique : renforce le **hub Blox Fruits** (codes ↔ tier fruits ↔ **tier races** ↔ guide) et distribue de l'equity interne — la page sert tout le cluster, pas seulement elle-même.

---

## 6. Roadmap 30 jours (français-first)

**Semaine 1 — Approfondir Blox Fruits (jeu-modèle du sous-cluster)**
- J1 : Tier list des races ✓ (fait).
- J2/J3 : Blox Fruits **Sword Tier List** ✓ (fait le 25/07). Choix de la brique la plus **stable** (classement de puissance, pas de valeurs fluctuantes à maintenir), conforme au repli recommandé en section 7. Intention « best sword blox fruits » / « meilleure épée blox fruits », distincte de la tier list des fruits (fruits) et des races (races) → aucune cannibalisation. Interliée aux 3 autres pages du cluster (fruits, races, guide, codes).
- J4 : Blox Fruits **Value List** (valeurs de trading) — reportée : n'entreprendre que si l'engagement de maintenance quotidienne (redate + resource des valeurs, ≥2 sources) est tenable. Sinon enchaîner sur GAG (semaine 2).
- J4 : Page « comment awaken » dédiée si le volume le justifie, sinon renforcer la section du pilier + interliens.
- J5 : Audit interne du cluster Blox Fruits (anti-orphelin, anti-cannibalisation, ancres descriptives).

**Semaine 2 — Répliquer le modèle sur Grow a Garden (jeu #1)**
- Mutations (liste + valeurs), pets/seeds tier list, calculateur/valeur, guide events (relié à l'encart). GAG est le plus gros trafic actuel : priorité maximale en volume.

**Semaine 3 — Hubs éditoriaux à fort volume**
- « Meilleurs jeux Roblox (mois) », « Nouveaux jeux Roblox », « Jeux Roblox tendance » : pages hub qui **redistribuent l'equity** vers 30-50 pages jeu et captent des head terms. Fort effet crawl + maillage.

**Semaine 4 — Steal a Brainrot + hygiène technique**
- Sous-cluster Steal a Brainrot (brainrots value/tier, admin abuse guide relié à l'encart). Puis hygiène : arbitrage `en/` (noindex ou plan hreflang), audit liens internes global, pages fines < 1200 mots à étoffer.

**Principe permanent** : chaque jour, (1) re-scan trending → si nouveau hit, il passe devant l'evergreen ; (2) sinon, avancer d'une brique le cluster prioritaire ; (3) jamais d'orphelin, toujours interlier au hub.

---

## 7. Suggestion pour demain (J5 — 27/07)

**Travail fait le 26/07 :** nouvelle page **`tier-list/grow-a-garden-2-pets.html`** (Tier List Pets Grow a Garden 2, ~1 930 mots). Intention distincte ciblée : « grow a garden 2 pets tier list », « meilleurs pets grow a garden 2 » — sans cannibaliser la tier list des **graines** GAG2 (intention rendement) ni la tier list des **pets du 1er opus** GAG (jeu différent). Classement sourcé (Beebom, Pro Game Guides, FRVR, u7buy, Skycoach) : S = Unicorn, Ice Serpent, Black Dragon, Raccoon · A = Golden Dragonfly, Queen Bee, Deer · B/C détaillés. Effets honnêtes (mutation Rainbow/Gold, défense nocturne, croissance), note d'évolutivité des prix, schema ItemList + FAQPage + Breadcrumb. Maillage complet : carte hub (vraie miniature), cross-links seeds ↔ pets ↔ codes ↔ guide, sitemap-tier-list.xml + sitemap.xml. Aucun orphelin.

Le cluster Grow a Garden compte désormais : GAG pets ✓ · GAG2 graines ✓ · **GAG2 pets ✓**. Prochaine brique recommandée, par ordre de priorité :

1. **Grow a Garden — page « mutations »** (`guides/` ou `tier-list/`) : intention « grow a garden mutations », « comment obtenir mutation Rainbow / Gold / Wet / Chilled ». Fort volume, intention distincte (how-to, pas un classement) → complète le cluster sans cannibaliser. Sourcer ≥2 (valeurs/multiplicateurs communautaires datés).
2. Alternative : **hub éditorial « Meilleurs jeux Roblox (juillet 2026) »** — forte demande, maillage transversal vers tout le catalogue (opportunité #2 du scoring, encore À faire).
3. Poursuivre le cluster GAG2 : **value list des graines/pets** uniquement si la maintenance des valeurs (≥2 sources datées) est tenable.

⚠️ Règle permanente : re-scan trending d'abord ; si un nouveau hit Roblox ≥4000 joueurs apparaît, il passe devant l'evergreen.

---

*Rappel opérationnel : je ne fais jamais `git push` moi-même. Pour publier le travail du jour, dans le dossier GameNova :*

```
git add -A && git commit -m "SEO: tier list races Blox Fruits + encart evenements + audit roadmap" && git push origin main
```
