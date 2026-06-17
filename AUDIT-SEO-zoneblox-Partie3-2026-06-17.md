# Audit SEO Zoneblox — Partie 3 : Plan de contenu ultra-agressif 0 → 100k

**Site :** https://zoneblox.com
**Objet :** transformer la stratégie (Partie 2) en **machine de production** : cadence, modèles, calendrier 12 semaines, contrôle qualité.
**Date :** 17 juin 2026

---

## Principe : tu as déjà une usine, il faut la rediriger

Zoneblox possède un atout que 99 % des sites concurrents n'ont pas : **une tâche quotidienne automatisée** qui surveille les sources de codes, vérifie, met à jour et contrôle la qualité. Le plan de contenu ne consiste donc pas à « écrire plus à la main », mais à **réorienter cette capacité de production** vers les chantiers à plus fort PWE (Partie 2) tout en gardant la maintenance des codes.

Règle d'or : **chaque page publiée doit être soit evergreen (se maintient seule), soit branchée sur l'automatisation (se met à jour seule).** On évite de créer de la dette de maintenance manuelle.

---

## 1. Les 7 modèles de pages (templates de production)

Standardiser = produire vite **et** garder la cohérence E-E-A-T/SEO. Chaque modèle a une cible, une longueur, un schema et un quota de maillage.

| Modèle | Cible requête | Long. cible | Schema obligatoire | Maillage min. | Fréquence MAJ |
|---|---|---|---|---|---|
| **A. Page codes** (existe) | `codes <jeu>` | 1500-2500 mots | Article + FAQPage + Breadcrumb | 12 liens | Quotidienne (auto) |
| **B. Page catégorie** (NOUVEAU) | `codes <genre> roblox` | 600-1000 mots | CollectionPage + ItemList | 15+ liens | Mensuelle |
| **C. Hub/satellite Musique** (NOUVEAU) | `code musique roblox <thème>` | 1200-2500 mots | Article + ItemList | 10 liens | Trimestrielle |
| **D. Pilier Robux/confiance** (NOUVEAU) | `robux gratuit`, `<sujet> roblox` | 1500-2500 mots | Article + FAQPage + HowTo | 10 liens | Semestrielle |
| **E. Guide de progression** (existe) | `comment avoir <X>`, `meilleur <X>` | 1200-2500 mots | Article + HowTo + FAQPage | 10 liens | Sur MAJ jeu |
| **F. Tier list** (existe) | `tier list <jeu>` | 1000-1800 mots | Article + ItemList | 8 liens | Sur MAJ jeu |
| **G. Actualité datée** (NOUVEAU) | `nouveau code <jeu>`, `MAJ <jeu>` | 300-700 mots | NewsArticle | 6 liens | Ponctuelle (auto) |

**Note schema :** ajoute `VideoObject` partout où une vidéo YouTube est intégrée, et `Person` (auteur) sur les modèles A, C, D, E, F (cf. Partie 5).

---

## 2. Le moteur de fraîcheur : `/actualites/` branché sur l'automatisation

C'est le plus gros gain « gratuit » du plan. Ta surveillance `code-watch` détecte déjà chaque nouveau code. Au lieu de seulement l'injecter dans la page-jeu, **génère aussi une actualité datée** :

- Déclencheur : nouveau code confirmé (2 sources) → page `/actualites/<jeu>-nouveau-code-<date>.html` (modèle G).
- Contenu : le code, sa récompense, comment l'utiliser, lien vers la page-jeu (modèle A), date/heure.
- Effet : Google reçoit un signal de fraîcheur **daté et structuré** (`NewsArticle`), capte les requêtes « nouveau code <jeu> aujourd'hui », et alimente le hub `/actualites/` qui devient une page-magnet mise à jour en continu.
- Coût marginal : quasi nul (l'info est déjà collectée). **C'est le levier au meilleur rapport effort/impact du site.**

Garde-fou honnêteté (déjà dans tes règles) : ne crée une actu que sur un **vrai** changement vérifié. Pas de fausse fraîcheur.

---

## 3. Calendrier éditorial 12 semaines (Vague 1)

Cadence réaliste pour une production automatisée + supervision. Objectif fin de période : **15-30k visites/mois** et les fondations d'architecture posées.

**Semaines 1-2 — Architecture indexable**
- Publier les **8 pages de catégories** (modèle B). Réutilise `ALL_GAMES` + `cat` → 80 % du contenu est déjà en base.
- Mettre en place `/actualites/` (hub + modèle G + branchement `code-watch`).
- QC : sitemap, maillage accueil → catégories → pages-jeu.

**Semaines 3-5 — Gisement Musique (★ priorité)**
- Pilier `/musique/` (modèle C) : grande liste d'IDs vérifiés (2 sources).
- 4 satellites : `rap`, `phonk`, `troll/meme`, `par-jeu`.
- Objectif : premier contenu evergreen capable d'attirer des backlinks.

**Semaines 6-8 — Cluster guides « comment avoir »**
- 10-15 guides de progression (modèle E) sur les plus gros jeux : `meilleur fruit Blox Fruits`, `comment avoir le Leopard`, `meilleures graines Grow a Garden`, `reroll Anime Vanguards`, etc.
- Relier chaque guide à sa page codes + tier list (triangulation).

**Semaines 9-10 — Pilier confiance Robux**
- `/robux-gratuit/` (modèle D) + 3 satellites (`microsoft-rewards`, `creer-des-ugc`, `arnaques-a-eviter`).
- Double objectif : trafic massif + Trust E-E-A-T + appât à backlinks éditoriaux.

**Semaines 11-12 — Densification & nouveaux jeux**
- Ajouter les jeux tendance manquants (vérif. hebdo du top trending Roblox).
- Densifier le maillage (« Jeux similaires » 3→6-8, liens in-prose) sur les 30 pages stratégiques.
- Étoffer les 10 pages codes les plus prometteuses vers 2200-2500 mots.

---

## 4. Process de production industrialisé (le « pipeline »)

Pour chaque nouvelle page, un flux unique et répétable :

1. **Recherche** : 2 sources fiables minimum (Pocket Tactics, Beebom, Pro Game Guides, description in-game, Trello officiel). Jamais d'invention.
2. **Rédaction** depuis le modèle adéquat (§1), en français, ton clair, 0 remplissage creux.
3. **SEO on-page** : title normé, meta 150-160, H1 unique, FAQ ≥4 Q/R, alt descriptifs, canonical/OG.
4. **Schema** : le(s) type(s) obligatoire(s) du modèle + `Person` auteur + `VideoObject` si vidéo.
5. **Maillage** : respecter le quota du modèle (pilier↔satellites, in-prose).
6. **QC automatisé** (déjà en place, à étendre) : fin de fichier `</html>`, divs équilibrés, 0 octet nul, ≥ seuil de mots, JSON-LD valide, GA4 + nav 7 entrées, cache JS homogène.
7. **Intégration** : sitemap, hub parent, compteurs synchronisés (`GAMES_INDEX`/`ALL_GAMES`, `ROBLOX_THUMBS`/`THUMBS`).

⚠️ **Contrainte technique connue** : la troncature intermittente des grosses écritures (documentée dans `CLAUDE.md` et constatée encore le 17/06). Pour le scaling, **produire une page à la fois avec vérification de fin de fichier systématique**, jamais en lot massif. Idéalement, fiabiliser la chaîne d'écriture avant d'industrialiser (sinon le scaling amplifiera les pannes).

---

## 5. Politique de qualité « anti-thin / anti-ferme »

Le secteur des codes Roblox est rempli de fermes de contenu que Google cherche activement à déclasser (Helpful Content System). Pour rester du bon côté :

- **Profondeur réelle** : descriptif de jeu développé, mécaniques, ce que débloquent les codes — pas une liste sèche.
- **Unicité** : éléments que les autres n'ont pas (historique des codes, captures de test, tableaux de récompenses datés, vidéos maison).
- **Honnêteté de fraîcheur** : `dateModified` mis à jour **seulement** sur changement réel.
- **Sources visibles** : bloc « Sources vérifiées » sur 100 % des pages codes (aujourd'hui 13/143 — à généraliser).
- **Pas de cannibalisation** : une intention = une URL. Le pilier vise le terme générique, les satellites les variantes (évite que 2 pages se battent sur la même requête).

---

## 6. Mesure de la Vague 1 (ce qu'on regarde)

| KPI | Cible fin S12 | Outil |
|---|---|---|
| Pages indexées | +60-80 (catégories, musique, robux, guides, actus) | Search Console |
| Visites SEO/mois | 15-30k | GA4 |
| Pages catégories en top 20 FR | ≥4/8 | Search Console |
| 1er hub evergreen (musique) en top 10 | « code musique roblox <thème> » | Search Console |
| Pages avec impressions > 0 | 80 %+ du catalogue | Search Console |
| Premiers backlinks référents | ≥10 domaines | Ahrefs/Search Console |

**Connecte Google Search Console dès maintenant** si ce n'est pas fait : sans elle, tu pilotes à l'aveugle. GA4 mesure le trafic, GSC mesure les requêtes/positions/indexation — c'est l'instrument de bord n°1 du plan.

---

→ **Partie 4** : l'autorité et le netlinking — le facteur sans lequel tout ce contenu plafonnera en page 2.
