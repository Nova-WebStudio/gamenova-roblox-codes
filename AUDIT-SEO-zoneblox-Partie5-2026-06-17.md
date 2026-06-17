# Audit SEO Zoneblox — Partie 5 : E-E-A-T & confiance

**Site :** https://zoneblox.com
**Statut :** E-E-A-T **4,5/10** (Partie 1). Trust correct, mais **Experience, Expertise et Authoritativeness faibles**.
**Date :** 17 juin 2026

> E-E-A-T n'est pas un facteur de classement direct, c'est le **cadre** par lequel Google évalue si un domaine mérite d'être remonté. Pour un domaine jeune dans un secteur rempli de fermes de contenu, **c'est ce qui fait la différence entre « toléré » et « recommandé ».** L'autorité (Partie 4) amène les liens ; l'E-E-A-T transforme ces liens en confiance durable.

---

## 1. Diagnostic par pilier (rappel + détail)

| Pilier | Note | Constat |
|---|---|---|
| **Experience** (vécu de première main) | 🔴 Faible | 0 preuve de test réel affichée. La page « À propos » *dit* tester les codes, rien ne le *montre*. |
| **Expertise** (compétence de l'auteur) | 🔴 Faible | **0 auteur nommé** (0 schema `Person`), 172 pages avec `author = Organization`. Les concurrents affichent des rédacteurs identifiés. |
| **Authoritativeness** (réputation) | 🔴 Faible | Découle de l'autorité (Partie 4) : pas de backlinks, pas de mentions. |
| **Trust** (fiabilité) | 🟢 Correct | Mission claire, méthode de vérif expliquée, disclaimer « non affilié », pages légales, dates de vérif, codes expirés conservés. **C'est ton point fort.** |

**Le verrou principal :** l'absence totale d'**auteur humain** et de **preuve d'expérience**. Ce sont les deux « E » que Google a ajoutés précisément pour distinguer le contenu vécu du contenu recopié.

---

## 2. Chantier 1 — Donner des visages au site (Expertise)

**Objectif :** passer de « site anonyme » à « équipe identifiable de joueurs Roblox ».

Actions concrètes :
1. **Créer 1-2 profils d'auteurs réels** avec page bio dédiée (`/auteurs/<nom>.html`) :
   - photo, pseudo, expérience Roblox (« joue à Blox Fruits depuis 2021 », heures de jeu, jeux maîtrisés),
   - lien vers profil Roblox/réseaux, historique des articles signés.
2. **Byline visible** sur chaque page éditoriale : « Rédigé et vérifié par <Nom> — mis à jour le <date> ».
3. **Schema `Person`** : basculer `author` de `Organization` → `Person` (avec `name`, `url` vers la bio, `sameAs`) sur les modèles A, C, D, E, F (Partie 3). Garder `Organization` comme `publisher`.
4. **`Organization` enrichi** : `logo`, `sameAs` (réseaux créés en Partie 4), `foundingDate`, `contactPoint`.

> Honnêteté : l'auteur doit être une **vraie personne** (toi, un collaborateur). Pas de persona fictive — Google et les utilisateurs détectent les faux profils, et ça détruit le Trust que tu as déjà.

---

## 3. Chantier 2 — Prouver l'expérience de première main (Experience)

C'est le « E » le plus discriminant et le plus négligé du secteur. Le prouver te démarque instantanément.

- **Captures d'écran maison** de la redemption du code en jeu (« code testé le <date>, voici le résultat ») sur les pages phares.
- **Mention explicite** « ✅ Code testé en jeu par <Nom> le <date> » à côté des codes, au-dessus de la ligne de flottaison.
- **Vidéos maison courtes** (issues du canal social, Partie 4) montrant l'utilisation réelle, intégrées avec `VideoObject`.
- **Notes d'expérience** dans les guides : « en pratique, le meilleur reroll se fait ainsi… » — du vécu, pas de la paraphrase.
- **Section « Notre méthode de test »** détaillée et liée depuis chaque page.

Impact : transforme un contenu « recopié de 2 sources » en contenu « vérifié de première main » — exactement le signal que le Helpful Content System cherche à récompenser.

---

## 4. Chantier 3 — Systématiser les signaux de Trust (consolider ton point fort)

Trust est déjà ton meilleur pilier — finalise-le à 100 % :

- **Bloc « Sources vérifiées »** sur **toutes** les pages codes (aujourd'hui visible sur 13/143). Liste les 2+ sources + date.
- **Bloc de fraîcheur visible** près des codes : « Dernière vérification : <date> · Prochaine vérif : quotidienne ».
- **Politique éditoriale publique** (`/methodologie.html` ou section À propos) : comment on vérifie, quand on date, pourquoi on garde les expirés, comment signaler un code mort (tu as déjà le formulaire de contact — mets-le en avant).
- **Signaux de sécurité** : le pilier anti-arnaque Robux (Partie 2) est un signal de Trust majeur — il montre que tu protèges l'utilisateur.
- **Cohérence légale** : `privacy`, `terms`, `contact`, mentions « non affilié à Roblox Corporation » (déjà en place ✅).
- **HTTPS, NAP cohérent, e-mail de contact pro** (idéalement @zoneblox.com plutôt qu'une adresse Gmail personnelle, pour la crédibilité).

---

## 5. Chantier 4 — Le balisage qui soutient l'E-E-A-T

| Schema | Où | Bénéfice |
|---|---|---|
| `Person` (auteur) + lien `author` → bio | Pages éditoriales | Expertise lisible par Google |
| `Organization` enrichi (`logo`, `sameAs`, `contactPoint`) | Toutes pages | Entité/marque reconnue |
| `HowTo` | Guides, « comment utiliser un code » | Rich result + expertise |
| `VideoObject` | Pages avec vidéo | Preuve d'expérience + rich result |
| `FAQPage` | Codes, guides (déjà 36 pages) | Couverture SERP + utilité |
| `Review`/`AggregateRating` (avec prudence) | Tier lists | Seulement si vraies évaluations |

---

## 6. Feuille de route E-E-A-T (3 mois)

**Mois 1**
- Créer 1 auteur réel + page bio. Basculer `author` → `Person` sur les nouveaux contenus (catégories, musique, robux).
- Ajouter le bloc « Sources vérifiées » au gabarit des pages codes (déploiement progressif).

**Mois 2**
- Étendre `Person` au catalogue existant (par lots, avec QC anti-troncature).
- Ajouter captures de test + « testé en jeu le… » sur le top 20 des pages.
- Page `/methodologie.html`.

**Mois 3**
- `VideoObject` sur toutes les pages à vidéo + intégrer les vidéos maison.
- `Organization` enrichi avec `sameAs` (réseaux lancés en Partie 4).
- E-mail pro @zoneblox.com.

---

## 7. Mesure E-E-A-T

| Signal | Avant | Cible 3 mois |
|---|---|---|
| Pages avec auteur `Person` | 0 | 100 % éditoriales |
| Pages avec preuve d'Experience (capture/« testé ») | 0 | Top 20+ |
| Pages citant 2+ sources visibles | 13/143 | 143/143 |
| Schema `HowTo` / `VideoObject` | 0 | Tous guides/vidéos |
| Page méthodologie publique | ❌ | ✅ |

---

## Le message clé de la Partie 5

Ton **Trust** est déjà bon — c'est rare et précieux. Mais sans **auteur humain** ni **preuve d'expérience**, Google n'a aucune raison de te préférer à une ferme de codes. Les deux « E » (Experience, Expertise) sont ton chantier le moins coûteux et le plus différenciant : **mets des visages, montre que vous jouez vraiment, citez vos sources partout.** Couplé à l'autorité (Partie 4), c'est ce qui fait passer un domaine jeune de « toléré » à « recommandé ».

→ **Partie 6** : industrialiser tout ça et passer de 100k à 500k.
