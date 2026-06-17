# Audit SEO Zoneblox — Partie 2 : Stratégie de mots-clés & architecture de contenu

**Site :** https://zoneblox.com — référence **francophone** des codes & guides Roblox.
**Cap :** 100 000 → 500 000 visites SEO/mois.
**Date :** 17 juin 2026
**Suite de la Partie 1** (audit). Trois angles : stratège mots-clés type Ahrefs, architecte de contenu type HubSpot, expert E-E-A-T.

---

## Le principe directeur : gagner par vagues, pas par volume brut

Tu ne peux pas battre Pocket Tactics et Pro Game Guides frontalement aujourd'hui (Partie 1, autorité 2,5/10). La stratégie gagnante n'est pas « plus de pages », c'est **prendre le terrain dans l'ordre où tu peux le tenir** :

1. **Vague 1 — Longue traîne FR** : requêtes précises, faible concurrence, que les géants EN couvrent mal en français. C'est là que tu rankes *vite*, même avec un domaine jeune.
2. **Vague 2 — Hubs evergreen à fort volume** : 2-3 sujets stables et massifs (musique Roblox, Robux, catégories) qui font effet de levier et apportent des backlinks naturels.
3. **Vague 3 — Moyenne traîne & head FR** : « codes roblox », « codes <gros jeu> » — accessibles seulement une fois l'autorité installée.

Chaque vague finance la suivante (trafic → signaux → autorité → requêtes plus dures).

> **Note d'honnêteté méthodo :** je n'ai pas d'accès Ahrefs/Semrush en direct ici. Les volumes ci-dessous sont des **estimations de priorité relatives** fondées sur les patterns de recherche, la SERP réelle et la saisonnalité du secteur. Avant d'industrialiser, fais valider les MSV exacts dans Ahrefs/Semrush (base FR) — je donne le cadre de priorisation, l'outil donne les chiffres définitifs.

---

## 1. L'univers de mots-clés : 6 clusters d'intention

Tout le trafic Roblox FR se range dans 6 intentions. Zoneblox n'en exploite aujourd'hui que 3 (codes, guides, tier list) et **rate les 3 plus gros gisements evergreen**.

| # | Cluster d'intention | Exemples de requêtes | Volume relatif | Volatilité | Statut Zoneblox |
|---|---|---|---|---|---|
| 1 | **Codes par jeu** | `codes blox fruits`, `code grow a garden juin 2026`, `nouveau code <jeu>` | Élevé | Très haute | ✅ Couvert (143 pages) |
| 2 | **Guides / progression** | `comment avoir <X>`, `meilleur fruit blox fruits`, `<jeu> wiki fr` | Élevé | Basse | 🟡 Partiel (38 guides) |
| 3 | **Tier lists** | `tier list <jeu>`, `meilleur perso <jeu>` | Moyen | Moyenne | ✅ Couvert (50) |
| 4 | **Musique / IDs** | `code musique roblox`, `id musique roblox`, `code boombox <chanson>` | **Très élevé, stable** | Très basse | ❌ **Absent** |
| 5 | **Plateforme / confiance** | `robux gratuit`, `comment échanger roblox`, `roblox premium ça vaut le coup`, `meilleurs jeux roblox` | **Très élevé** | Basse | ❌ **Absent** |
| 6 | **Découverte / catégories** | `meilleurs jeux anime roblox`, `jeux simulator roblox`, `jeux roblox comme <X>` | Moyen | Basse | ❌ **Absent** (filtre JS only) |

**Lecture stratégique :** tes 3 clusters actuels (1, 2, 3) sont **volatils** (les codes expirent, il faut maintenir en permanence) et **hyper-concurrentiels**. Les clusters 4, 5, 6 sont **stables, evergreen, à fort volume** et **largement ouverts en français**. Ce sont eux qui vont faire décoller le trafic *et* l'autorité — un article « codes musique Roblox » bien fait attire des backlinks et se maintient des années, contrairement à une page de codes qui se périme chaque semaine.

---

## 2. Les 3 gisements evergreen à ouvrir d'urgence

### 2.1 — Hub « Codes musique Roblox » (cluster 4) — *le plus gros levier court terme*
Dexerto.fr ranke déjà sur « codes musique roblox » et « meilleurs codes musique » : preuve que le volume FR est là et que ce n'est **pas** un sujet réservé aux géants EN.
- **Pilier :** `/musique/` — « Codes musique Roblox (2026) : +500 IDs pour Boombox ».
- **Satellites :** `/musique/rap/`, `/musique/phonk/`, `/musique/troll/`, `/musique/par-jeu/`, `/musique/<artiste-tendance>/`.
- Pourquoi ça marche : intention stable, faible volatilité (les IDs changent peu), format « grande liste » qui attire des liens, et **0 maintenance quotidienne** contrairement aux codes de jeu.
- Bonus : crée une raison de revenir + temps sur site élevé (les joueurs copient plusieurs IDs).

### 2.2 — Pilier confiance « Robux gratuit : la vérité » (cluster 5) — *le plus gros levier d'autorité*
« robux gratuit » est l'une des requêtes Roblox les plus cherchées au monde — et un nid à arnaques. Un contenu **honnête** (« non, aucun code ne donne de Robux gratuits, voici les seules méthodes légitimes : Microsoft Rewards, créer des items UGC, Premium… ») :
- capte un volume énorme,
- **renforce massivement le Trust E-E-A-T** (tu protèges l'utilisateur — exactement ce que Google veut mettre en avant),
- attire des backlinks éditoriaux (les médias citent les pages anti-arnaque).
- **Pilier :** `/robux-gratuit/` + satellites `/robux/microsoft-rewards/`, `/robux/creer-des-ugc/`, `/robux/cartes-cadeaux/`, `/robux/arnaques-a-eviter/`.

### 2.3 — Pages de catégories indexables (cluster 6) — *le chaînon manquant d'architecture*
Identifié en Partie 1 : tes 9 catégories ne sont qu'un filtre JS. Crée 6-8 **pages rédigées et indexables** ciblant « codes <genre> roblox » + « meilleurs jeux <genre> roblox » :
`/codes/simulator/`, `/codes/anime/`, `/codes/battle/`, `/codes/tower-defense/`, `/codes/rpg/`, `/codes/tycoon/`, `/codes/horror/`, `/codes/obby/`.
- Chaque page = intro 400-600 mots (qu'est-ce que le genre, jeux phares, pourquoi des codes), grille de jeux, FAQ, `ItemList` + `CollectionPage` JSON-LD.
- Fusionne `sport` (1 jeu) dans une catégorie plus large pour éviter une page maigre.
- Rôle SEO double : capter la moyenne traîne **et** servir de plaque tournante de maillage entre l'accueil et tes 143 pages-jeu.

---

## 3. Architecture de contenu cible : le modèle « pilier → cluster »

Aujourd'hui ton maillage est « par gabarit » (Partie 1, 7/10). Passe à une architecture **en clusters thématiques**, où chaque pilier capte l'autorité et la redistribue à ses satellites.

```
ACCUEIL (zoneblox.com)
│
├─ HUB CODES  (/codes/)
│   ├─ Pages CATÉGORIES indexables  ← NOUVEAU (cluster 6)
│   │     ├─ /codes/anime/  → 35 jeux
│   │     ├─ /codes/simulator/  → 37 jeux
│   │     └─ … (6-8 catégories)
│   └─ 143 pages-jeu  →  chacune triangulée :
│            codes ↔ /guides/<jeu> ↔ /tier-list/<jeu>   (déjà en place, à densifier)
│
├─ HUB GUIDES  (/guides/)
│   └─ Clusters par grosse licence :
│        Pilier "Guide Blox Fruits" → satellites "meilleur fruit",
│        "comment avoir le Leopard", "races", "raids", "reroll"…
│
├─ HUB TIER LISTS  (/tier-list/)
│
├─ HUB MUSIQUE  (/musique/)   ← NOUVEAU (cluster 4)  ★ priorité haute
│
├─ PILIER ROBUX/CONFIANCE  (/robux-gratuit/)  ← NOUVEAU (cluster 5)  ★ autorité
│
├─ HUB ACTUALITÉS  (/actualites/)  ← NOUVEAU — fraîcheur datée
│        "Nouveau code <jeu> aujourd'hui", "MAJ <jeu> : tout savoir"
│
└─ AVATARS  (/avatar/) — déjà en place (pipeline séparé)
```

**Règles de maillage du modèle cluster (à appliquer) :**
- Chaque satellite lie vers **son pilier** (ancre exacte) + 3-4 satellites frères.
- Chaque pilier liste **tous** ses satellites (silo fort).
- Plancher : **≥12 liens internes utiles** par page, dont **6-8 contextuels in-prose** (pas seulement dans des modules/cartes).
- Densifier « Jeux similaires » de 3 → 6-8, basé sur la proximité de requêtes réelle (un joueur Blox Fruits → King Legacy, Grand Piece, Haze Piece, A One Piece Game…), pas seulement « même catégorie ».

---

## 4. Analyse de l'écart concurrentiel (où tu peux gagner)

| Acteur | Force | Faille exploitable par Zoneblox |
|---|---|---|
| **Pocket Tactics / Pro Game Guides / Roblox Den (EN)** | Autorité énorme, fraîcheur, exhaustivité | **En anglais.** Pages FR inexistantes ou traduites médiocrement. La longue traîne FR leur échappe. |
| **Dexerto.fr** | Autorité média, marque, couvre codes + musique | **Généraliste** (pas que Roblox) → couverture **peu profonde** par jeu, pas de tier lists, pas de guides de progression détaillés, catalogue limité. |
| **Sites FR amateurs / fermes traduites** | Volume | Qualité faible, codes périmés, pas d'E-E-A-T. |

**Ton angle gagnant :** *le site FR 100 % Roblox, le plus exhaustif et le plus à jour, qui couvre toute la chaîne (codes → guide → tier list → musique → confiance) là où Dexerto reste en surface et où les géants restent en anglais.* La profondeur par jeu (143 jeux × 3 formats) est déjà un différenciateur que Dexerto n'a pas.

---

## 5. Cadre de priorisation : le score PWE (Potentiel × Winnabilité × Effort inverse)

Pour décider **quoi écrire d'abord**, note chaque page sur 3 axes (1-5) :

- **P — Potentiel de trafic** (volume estimé de la requête)
- **W — Winnabilité** (probabilité de ranker vu l'autorité actuelle — favorise la longue traîne FR)
- **E — Effort inverse** (5 = rapide à produire/maintenir)

**Score = P × W × E.** On attaque par score décroissant.

Application directe (top priorités) :

| Chantier | P | W | E | Score | Vague |
|---|---|---|---|---|---|
| Hub Musique + 5 satellites | 5 | 4 | 4 | **80** | 1-2 |
| Pages catégories (×8) | 4 | 4 | 4 | **64** | 1 |
| Pilier Robux/confiance + 4 satellites | 5 | 3 | 4 | **60** | 2 |
| Guides « comment avoir <X> » (top 10 jeux) | 4 | 5 | 3 | **60** | 1 |
| Hub Actualités (fraîcheur) | 3 | 5 | 4 | **60** | 1 |
| Nouvelles pages-jeu (jeux tendance manquants) | 4 | 4 | 3 | **48** | 1-2 |
| Étoffer top 30 pages codes (1500→2500 mots) | 4 | 3 | 3 | **36** | 2 |
| Moyenne traîne « codes roblox » (head FR) | 5 | 2 | 2 | **20** | 3 |

---

## 6. Le backlog de production, en vagues, jusqu'à 100k

**Vague 1 — Fondations & longue traîne (mois 1-3) — viser 15-30k/mois**
- 8 pages de catégories indexables.
- Hub Musique + 5 satellites (★ démarre les backlinks).
- Hub Actualités opérationnel : 1 actu datée par jour (recycle déjà ta surveillance `code-watch` quotidienne → contenu frais automatique).
- Cluster guides « comment avoir <X> » sur tes 10 plus gros jeux (Blox Fruits, Grow a Garden, Adopt Me, Blade Ball, Anime Vanguards…).
- Combler les jeux tendance manquants au catalogue (vérifier vs top trending Roblox : Steal a Brainrot, Grow a Garden, Brookhaven, Murder Mystery 2 — déjà présents ; ajouter les nouveaux entrants chaque semaine).

**Vague 2 — Effet de levier & profondeur (mois 3-6) — viser 30-60k/mois**
- Pilier Robux/confiance + satellites.
- Étoffer le top 30 des pages codes à 2200-2800 mots (éléments uniques : historique des codes, tableaux de récompenses, captures de test).
- Développer 2-3 clusters guides complets par grosse licence (modèle `/guides/blox-fruits`).
- Schema enrichi : `VideoObject` (vidéos intégrées), `HowTo` (guides), `Person` (auteurs — cf. Partie 5).

**Vague 3 — Moyenne traîne & marque (mois 6-12) — viser 60-100k+/mois**
- Attaquer « codes <gros jeu> » et catégories à plus forte concurrence (une fois l'autorité installée).
- Page pilier « Tous les codes Roblox » optimisée pour le head FR.
- Internationaliser le maillage musique/Robux (evergreen) qui aura accumulé des liens.

---

## 7. Le modèle de trafic : d'où viennent les 100k (et les 500k)

Pour que l'objectif soit crédible et pas incantatoire, voici la décomposition cible à maturité :

**Palier 100k/mois :**
| Source | Pages | Trafic moyen/page | Sous-total |
|---|---|---|---|
| Pages codes (longue traîne FR) | ~160 | ~250 | ~40 000 |
| Hub + satellites Musique | ~6 | ~3 500 | ~21 000 |
| Pilier Robux + satellites | ~5 | ~2 500 | ~12 500 |
| Pages catégories | ~8 | ~1 200 | ~10 000 |
| Guides progression | ~80 | ~180 | ~14 000 |
| Actualités (fraîcheur, cumulé) | flux | — | ~8 000 |
| **Total** | | | **~105 000** |

**Lecture :** 100k n'exige PAS de battre les géants sur le head. Il s'atteint avec **~260 pages bien rankées en longue/moyenne traîne FR + 2 hubs evergreen qui percent**. C'est réaliste sur 9-12 mois *si* l'autorité suit (Partie 4).

**Palier 500k/mois :** changement de nature, pas d'échelle seule. Il faut (a) ranker sur le **head FR** (« codes roblox », « robux gratuit », « codes musique roblox » en top 3), (b) **800-1200 pages**, (c) une **marque** avec recherches directes et présence sociale, (d) élargir le périmètre (items/UGC, IDs déco, guides plateforme, voire FR→autres marchés francophones). Le head ne se prend qu'avec l'autorité de la Partie 4 — c'est le vrai goulot vers 500k.

---

## 8. Ce qui change concrètement cette semaine

Sans attendre les Parties suivantes, 5 actions à fort PWE déclenchables tout de suite :

1. **Créer les 8 pages de catégories indexables** (réutilise tes données `ALL_GAMES` + `cat`, le gros du travail est déjà en base).
2. **Lancer le hub `/musique/`** avec une première grande liste d'IDs vérifiés (2 sources) — ton plus gros levier evergreen.
3. **Activer `/actualites/`** branché sur ta surveillance `code-watch` quotidienne : chaque nouveau code détecté = 1 actu datée = fraîcheur gratuite.
4. **Densifier le maillage** : porter « Jeux similaires » à 6-8 et ajouter 6-8 liens contextuels in-prose sur les 30 pages les plus stratégiques.
5. **Préparer l'E-E-A-T** (transition Partie 5) : créer 1 auteur identifié et basculer le `author` JSON-LD de `Organization` vers `Person` sur les pages éditoriales.

---

## Suite du rapport

- **Partie 3 — Plan de contenu ultra-agressif 0 → 100k** : cadence exacte, modèles de pages, calendrier éditorial 12 semaines, process de production industrialisé (en s'appuyant sur ta tâche quotidienne automatisée).
- **Partie 4 — Autorité, netlinking & marque** : le vrai goulot. Acquisition de backlinks FR, stratégie sociale (TikTok/Shorts Roblox), partenariats créateurs, RP gaming.
- **Partie 5 — E-E-A-T & confiance** : auteurs, preuves d'expérience, schema, signaux Trust.
- **Partie 6 — Scaling 100k → 500k** : industrialisation, périmètre élargi, roadmap 12 mois & KPIs.

Dis-moi : j'enchaîne sur la **Partie 3 (plan de contenu + calendrier)** ou tu préfères que je saute directement à la **Partie 4 (autorité/netlinking)**, qui est ton facteur limitant n°1 ?
