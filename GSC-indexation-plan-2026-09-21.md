# Plan d'action — Indexation Zoneblox (Search Console, 21 sept. 2026)

**Constat GSC** : 427 pages *non indexées* vs 227 *dans l'index*. L'indexé stagne (~220-248 depuis juin) alors que le catalogue grandit → il faut débloquer l'indexation, pas produire plus de pages.

---

## 1. Décomposition honnête des 427 (ce qui est grave vs bénin)

| Raison | Pages | Verdict |
|---|---|---|
| Page avec redirection | 162 | **Bénin** — résultat attendu de la migration `codes/`→`codes-` + www→non-www. Google indexe la cible. Rien à « corriger ». |
| Autre page avec canonique correcte | 24 | **Bénin** — dédoublonnage volontaire (canonical assumé). |
| Erreur liée à des redirections | 1 | **Corrigé le 21/09** (301→404 sur `clean-the-supermarket` / `drain-the-lake`). |
| Doublon : Google n'a pas choisi la même canonique | 12 | **À corriger** — nécessite la liste d'URL exacte. |
| Doublon sans URL canonique choisie | 5 | **À corriger** — nécessite la liste d'URL exacte. |
| **Explorée, actuellement non indexée** | **49** | **Vrai sujet** — crawlé mais jugé pas assez prioritaire/distinctif. |
| **Détectée, actuellement non indexée** | **174** | **Vrai sujet #1** — découvert (sitemap) mais pas encore crawlé = budget de crawl + autorité. |

**Ce qui est réellement à traiter ≈ 223 pages** (174 + 49). Les 186 « redirection/canonique » sont normales.

### Ce qui n'est PAS la cause (vérifié dans le code le 21/09)
- **Pas de thin content** : les 179 pages `codes-*.html` font toutes ≥1200 mots (médiane 1564).
- **Pas de blocage technique** : `robots.txt` = `Allow: /` + 2 sitemaps déclarés ; **aucun `noindex`** sur les pages servies ; canoniques auto-référentes correctes ; `sitemap.xml` propre (368 URLs, aucun vieux `/codes/`, aucun `?cat=`, aucun `www`).

### Diagnostic
Profil classique d'un **site jeune (lancé ~juin 2026), à autorité encore faible, avec beaucoup de pages « codes » très gabarisées**. Google **découvre** les URL via le sitemap mais **repousse le crawl/indexation** : budget de crawl limité + signaux d'autorité faibles + pages perçues comme peu différenciées. Le pic du 5 sept. (+161 non indexées) = churn post-migration ; il se résorbe si les signaux s'améliorent.

---

## 2. Plan priorisé

### P0 — Obtenir les URL exactes (pré-requis pour les corrections chirurgicales)
Dans Search Console → *Indexation des pages* → cliquer chaque motif → bouton **Exporter** → me transmettre le ZIP, pour :
- **Détectée, actuellement non indexée** (174)
- **Explorée, actuellement non indexée** (49)
- **Doublon : Google n'a pas choisi la même canonique** (12)
- **Doublon sans URL canonique** (5)

→ Je pourrai alors : repérer les pages faibles/à fusionner, corriger les canoniques au cas par cas, et renforcer le maillage vers les pages « détectées ».

### P1 — Autorité (le vrai levier de « Détectée non indexée »)
- Exécuter le **`P3-plan-backlinks-notoriete-2026-08-26.md`** déjà présent : quelques backlinks de qualité (annuaires jeux, partenariats, le widget « Codes du jour » avec backlink retour) augmentent le crawl budget alloué au domaine.
- Le **widget embeddable** (`embed/` + `data/codes.json`) est justement un vecteur de backlinks retour : le déployer sur 2-3 sites partenaires.

### P2 — Concentrer le crawl sur les pages fortes
- **Demande d'indexation manuelle** (GSC → Inspection d'URL → *Demander une indexation*) pour 10-15 pages prioritaires/semaine (top jeux : blox-fruits, grow-a-garden, steal-a-brainrot, plants-vs-brainrots, anime-vanguards, fisch, blade-ball…).
- **Maillage interne renforcé** vers les pages « détectées » : depuis l'accueil, les hubs (`tous-les-codes`, `guides`, `tier-lists`) et les blocs « jeux similaires ». (Le 21/09, les sauts de redirection internes ont déjà été retirés et un bandeau CTA ajouté sur Plants vs Brainrots.)
- **Différenciation** : pour les pages jugées « explorées non indexées », enrichir l'intro/à-propos avec des specificités réelles du jeu (mécaniques, éditeur, particularités) plutôt qu'un gabarit interchangeable. Prioriser d'abord les pages codes **vides** (fish-it, type-soul, anime-reborn) qui doivent être remplies (cf. roadmap J35).

### P3 — Hygiène (impact SEO faible, mais propre)
- **Supprimer le vieux dossier `codes/`** (176 fichiers + sous-dossiers catégories). Ils redirigent déjà via `.htaccess` (les règles agissent sur l'URL, pas sur le fichier), donc les supprimer ne casse rien et **réduit les doublons `index,follow` + canonical vers l'ancienne URL**. ⚠️ *Je n'ai pas pu le faire : le montage de l'agent interdit la suppression de fichiers.* **Commande à lancer par Peter** dans le dossier GameNova :
  ```
  git rm -r codes/
  ```
  (ou supprimer le dossier `codes\` dans l'explorateur, puis `git add -A`). Vérifier ensuite qu'une vieille URL redirige toujours (ex. `https://zoneblox.com/codes/blox-fruits.html` → `…/codes-blox-fruits.html`).
- Supprimer les 3 fichiers résiduels `en/` (déjà redirigés en 301) : `git rm -r en/`.
- Envisager de **ne garder au sitemap que les pages à indexer en priorité** si le volume dilue le crawl (à réévaluer avec les exports P0).

### P4 — Patience & suivi
- L'après-migration + montée en autorité se mesure sur **4 à 8 semaines**. Suivre chaque semaine la courbe *Dans l'index* (doit remonter) et le bucket *Détectée non indexée* (doit baisser).

---

## 3. Fait le 21/09 (déjà en place)
- Corrigé 2 redirections 301→404 (`.htaccess` : `clean-the-supermarket`, `drain-the-lake` → guides).
- Repointé 20 liens internes servis vers des pages codes fantômes.
- Vérifié : sitemap propre, robots OK, aucun noindex servi, contenu ≥1200 mots.
- Ajouté un bandeau CTA de maillage sur `codes-plants-vs-brainrots.html`.

## 4. À faire côté Peter (récap)
1. **Exporter** les 4 drilldowns GSC (P0) et me les envoyer.
2. Lancer la suppression du dossier `codes/` (et `en/`) : `git rm -r codes/ en/` — *bloqué côté agent (montage en lecture pour la suppression)*.
3. Lancer quelques **demandes d'indexation** manuelles sur les top pages.
4. Avancer le **plan backlinks** (autorité).
