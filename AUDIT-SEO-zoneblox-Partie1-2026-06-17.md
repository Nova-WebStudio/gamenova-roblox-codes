# Audit SEO Zoneblox — Partie 1 : Audit complet

**Site analysé :** https://zoneblox.com
**Objectif client :** devenir la référence **francophone** des codes & guides Roblox — paliers 100 000 puis 500 000 visites SEO/mois.
**Date :** 17 juin 2026
**Méthode :** analyse du code source réel (244 pages HTML, sitemap, JSON-LD, maillage), lecture sous trois angles — consultant SEO type Ahrefs, responsable contenu type HubSpot, expert E-E-A-T Google.

> Note préalable : le brief contenait des restes de copier-coller (« thehvacedge.com », « affiliation SaaS B2B »). Je les ai ignorés : l'audit porte bien sur Zoneblox, site de contenu/affiliation **gaming grand public francophone**, pas un SaaS B2B. La grille de lecture est adaptée en conséquence.

---

## Synthèse exécutive (à lire en premier)

Zoneblox est un site **techniquement bien construit** mais **commercialement invisible**. La fondation on-page (structure, schema, vitesse, maillage) est déjà au niveau d'un site mature ; ce n'est pas là qu'est le problème. Le problème est binaire et brutal :

1. **Autorité quasi nulle.** Pour sa requête cœur (« codes roblox » + variantes FR), Zoneblox n'apparaît nulle part. La SERP est verrouillée par des domaines anglais à très forte autorité (Pocket Tactics, Pro Game Guides, Roblox Den, Pocket Gamer) et, côté français, par Dexerto.fr. Un site neuf de quelques semaines ne bat pas ces domaines sur la seule qualité on-page.

2. **E-E-A-T sans « E » de Experience ni d'auteur humain.** 0 auteur nommé, 0 bio, 0 preuve de test de première main, citations de sources visibles sur seulement 13 pages /143. Google récompense l'expérience démontrable ; Zoneblox la revendique (page « À propos ») mais ne la **prouve** pas.

3. **Aucune page de catégorie indexable.** Les 9 catégories existent comme filtre JavaScript sur une seule page — donc invisibles pour Google. C'est le levier de trafic moyen-de-gamme le plus évident, aujourd'hui inexploité.

**Verdict global pondéré : 5,8 / 10.** Le on-page mérite un 7,5 ; il est tiré vers le bas par l'autorité (2,5) qui est, à ce stade, le **facteur limitant unique** vers 100k/500k. Bonne nouvelle : on ne part pas d'une dette technique, on part d'une base saine qu'il faut maintenant **rendre crédible et populaire**.

---

## Notes par critère

| Critère | Note | Tendance |
|---|---|---|
| Architecture du site | **7,5 / 10** | Solide |
| Maillage interne | **7,0 / 10** | Solide, perfectible |
| Catégories | **5,5 / 10** | Sous-exploité |
| Structure SEO (technique & on-page) | **7,5 / 10** | Solide |
| UX | **7,5 / 10** | Solide |
| Autorité perçue | **2,5 / 10** | Point bloquant |
| E-E-A-T | **4,5 / 10** | À reconstruire |
| **Global pondéré** | **5,8 / 10** | Base saine, traction nulle |

---

## 1. Architecture du site — 7,5 / 10

**Ce qui est vu dans le code :**
- Arborescence claire et logique en *hub-and-spoke* : `/codes/<slug>`, `/guides/<slug>`, `/tier-list/<slug>`, plus sections `/ugc-gratuit/` et `/avatar/`. Chaque verticale a sa page-hub (`/codes/`, `/guides/`, `/tier-list/`).
- 244 pages HTML, 235 URL au sitemap (`codes` 144, `tier-list` 47, `guides` 35) ; `robots.txt` propre, `Disallow` ciblé sur le seul template, `Sitemap:` déclaré.
- URLs lisibles, slugs explicites, fil d'Ariane (BreadcrumbList) présent.
- Pages statiques = crawl rapide, pas de dette JS pour l'indexation (les cartes d'accueil sont rendues en HTML statique, pas injectées en JS — vérifié : 165 cartes dans le HTML).

**Ce qui manque pour viser haut :**
- **Pas de hub éditorial de fraîcheur** (`/actualites/` ou `/blog/`). Pour un sujet aussi volatil que les codes, un flux d'actus daté (« nouveau code X aujourd'hui ») capte des requêtes *fresh* et envoie des signaux de fraîcheur que des pages-jeu statiques ne couvrent pas.
- **Profondeur de clic** : 244 pages reliées surtout via le hub `/codes/`. À 500+ pages, il faudra une couche intermédiaire (catégories indexables, voir §3) pour éviter que la longue traîne soit à 3-4 clics de l'accueil.

**Recommandation prioritaire :** créer la couche « catégories indexables » + un hub d'actualités daté. (Détaillé en Partie 2.)

---

## 2. Maillage interne — 7,0 / 10

**Constats chiffrés :**
- ~24 liens internes par page de codes en moyenne (échantillon), dont 8 à 16 liens **contextuels** vers d'autres pages codes/guides/tier-list.
- Triangulation codes ↔ guide ↔ tier-list en place via le bandeau CTA « Aller plus loin » (`data-cta="guidelink"`), plus un bloc « 🎮 Jeux similaires » (3 jeux de même catégorie).
- Fil d'Ariane sur chaque page → bon passage de PageRank vertical.

**Faiblesses :**
- **Variance trop forte** : certaines pages tombent à 8 liens internes pertinents (ex. fruit-battlegrounds) quand d'autres en ont 16. Le maillage dépend du template plus que de la pertinence sémantique.
- **« Jeux similaires » plafonné à 3** et basé sur la catégorie brute, pas sur la proximité réelle de requêtes (un joueur de Blox Fruits cherche aussi King Legacy, Grand Piece, Haze Piece — la logique « même cat » le fait, mais on peut densifier à 6-8 liens).
- **Pas de liens descendants depuis l'accueil vers la longue traîne** autres que les cartes ; pas de « clusters » thématiques explicites (pilier → satellites).
- **Liens contextuels dans la prose** quasi absents : les liens sont surtout dans des modules (cartes, bandeaux), peu dans le texte rédactionnel — or ce sont les liens *in-prose* qui pèsent le plus.

**Recommandation :** passer d'un maillage « par gabarit » à un maillage « par cluster » (piliers Blox Fruits / Anime / Simulator / Tower Defense → satellites), viser 6-8 liens contextuels in-prose par page, homogénéiser le plancher à ≥12 liens internes utiles.

---

## 3. Catégories — 5,5 / 10

**Constat majeur :** les 9 catégories existent **uniquement comme filtre JavaScript** sur `/codes/` (attributs `data-cat`, 21 occurrences de logique `filter`). **Aucune page physique indexable** (`/codes/anime/`, `/codes/simulator/`…). Google ne voit donc pas ces regroupements et ne peut pas les classer.

Répartition actuelle :

| Catégorie | Jeux | Lecture |
|---|---|---|
| simulator | 37 | Pilier — mérite sa page |
| anime | 35 | Pilier — mérite sa page |
| battle | 35 | Pilier — mérite sa page |
| rpg | 14 | Page viable |
| tycoon | 10 | Page viable |
| obby | 5 | Limite |
| horror | 3 | Trop mince |
| tower-defense | 3 | Trop mince (à fusionner/étoffer) |
| sport | 1 | Inexistant en l'état |

**Problèmes :**
- Des requêtes à fort volume comme « **codes simulator roblox** », « **codes tower defense roblox** », « **meilleurs jeux anime roblox codes** » ne sont **ciblées par aucune URL**.
- Catégories déséquilibrées (sport=1, horror=3) : soit on les étoffe, soit on les fusionne pour éviter des pages maigres.
- La taxonomie sert l'UX (filtre) mais pas le SEO.

**Recommandation prioritaire (gros levier 100k) :** créer 6-8 **pages de catégorie indexables** et rédigées (intro 300-500 mots ciblant « codes <genre> roblox », grille des jeux, FAQ, ItemList JSON-LD). C'est le chaînon manquant entre l'accueil et la longue traîne, et un gisement de mots-clés moyenne traîne aujourd'hui à zéro.

---

## 4. Structure SEO (technique & on-page) — 7,5 / 10

**Points forts (déjà au niveau « site mature ») :**
- **Balisage structuré riche et cohérent** : Article (172), BreadcrumbList (214), FAQPage (36) + 157 Q/R, ItemList (34), Organization (344), ImageObject (163). C'est largement au-dessus de la moyenne du secteur.
- **Titres normés** : `Codes <Jeu> (<mois> <année>) – Tous les codes actifs | Zoneblox`. Meta descriptions présentes, canonicals propres, Open Graph complet.
- **Fraîcheur** : `dateModified` présent sur 143/143 pages codes ; date de vérification visible.
- **Contenu suffisant** : 100 % des pages codes sont à **1200-1800 mots** (0 page sous le seuil de thin content — la règle interne a été tenue).
- **Performance** : miniatures WebP, Google Analytics différé (chargé à l'interaction), polices en `media=print/onload`. Bon pour les Core Web Vitals.

**Faiblesses à corriger :**
- **Pas de schema `VideoObject`** alors que les pages intègrent des vidéos YouTube → on rate des *rich results* vidéo.
- **Pas de schema `HowTo`** sur les guides (« comment utiliser un code », « comment obtenir X ») → format idéal pour la SERP.
- **Pas de `Speakable`** (recherche vocale) ni de balisage `Person`/auteur (cf. E-E-A-T).
- **Profondeur sémantique** : 1200-1800 mots c'est le minimum d'indexation, pas le niveau qui *gagne* contre Pocket Tactics. Les pages cibles à fort volume devront viser 2000-3000 mots utiles (FAQ enrichie, tableaux de récompenses, historique des codes).
- **Maillage `dateModified` ≠ vraie fraîcheur** : attention à ne mettre à jour la date que sur changement réel (la consigne interne le dit déjà — à tenir absolument, Google détecte le « fake freshness »).

**Recommandation :** ajouter VideoObject + HowTo, et faire passer le top 30 des pages à fort potentiel de 1500 à 2500 mots avec des éléments uniques (données, captures, historique).

---

## 5. UX — 7,5 / 10

**Points forts :**
- Design sombre moderne, cohérent, responsive (nav burger mobile), identité visuelle propre.
- Interactions utiles : onglets de contenu, **boutons « Copier le code »**, bandeaux « X codes actifs trouvés », codes expirés repliés.
- Vitesse perçue élevée (WebP, GA différé) — facteur UX **et** SEO.
- Parcours clair : page jeu → guide → tier-list via le bandeau CTA.

**Points de vigilance :**
- **Densité publicitaire** : pub leaderboard + bandeau CTA voyant en haut de page. À surveiller pour ne pas dégrader le CLS ni l'« helpful content » (Google pénalise les pages où la pub repousse le contenu utile).
- **Contenu en onglets** : du contenu masqué par défaut est légèrement déprécié vs contenu visible (mineur, mais réel).
- **Preuve de confiance au-dessus de la ligne de flottaison** : aucune mention « vérifié le … par … » visible immédiatement près des codes (la date existe mais l'humain manque — lien direct avec l'E-E-A-T).

**Recommandation :** garder l'UX actuelle, mais ajouter un bloc de confiance visible près des codes (« Vérifié le 17/06 — méthode ») et limiter la pub au-dessus du premier code.

---

## 6. Autorité perçue — 2,5 / 10  *(facteur limitant n°1)*

**Constat sans détour :** pour « codes roblox français » et variantes, **Zoneblox n'apparaît pas** dans les résultats. La première page est occupée par :
- côté EN : Pocket Tactics, Pro Game Guides, Roblox Den, Pocket Gamer, FRVR — domaines à autorité (DR estimé 80+), des années d'historique, des milliers de backlinks ;
- côté FR : Dexerto.fr (média gaming généraliste à forte autorité).

**Lecture Ahrefs :**
- Domaine très jeune (historique de production concentré sur quelques semaines de juin 2026), donc **peu ou pas de backlinks**, **pas de Domain Rating** établi, **pas de trust accumulé**.
- Aucun signal de marque (peu/pas de recherches « zoneblox », pas de présence sociale détectable, pas de mentions).
- Le secteur « codes Roblox » est l'un des plus **agressivement SEO-optimisés** qui soit : on affronte des fermes de contenu industrialisées.

**Pourquoi c'est LE sujet :** à on-page égal (et Zoneblox est déjà bon en on-page), **c'est l'autorité qui départage**. Sans backlinks ni signaux de marque, même des pages parfaites plafonneront en page 2-3. Les 100k visites ne viendront pas d'« encore mieux optimiser » mais de **gagner de l'autorité et occuper l'angle francophone** que les géants EN couvrent mal.

**Opportunité réelle :** le créneau **français spécialisé** est ouvert. Dexerto FR est généraliste ; les géants sont anglais. Un site FR 100 % dédié, frais et exhaustif, peut rafler la longue traîne francophone *avant* d'attaquer la moyenne traîne. C'est le cheval de bataille de la Partie 2.

---

## 7. E-E-A-T — 4,5 / 10

**Experience (E) — faible.** 0 preuve de test de première main mise en avant (captures de redemption, « code testé en jeu le … », vidéos maison). La page « À propos » *dit* « chaque code est testé et daté » mais rien ne le **montre** sur les pages.

**Expertise (E) — moyenne-faible.** **0 auteur nommé** sur tout le site (0 schema `Person`, 0 byline « Par … »). 172 pages déclarent un `author` = **Organization**, jamais une personne. Or les concurrents affichent des rédacteurs identifiés avec photo et historique (Ruby chez Pocket Tactics, Ishan chez Beebom). Google valorise l'auteur identifiable sur ce type de contenu.

**Authoritativeness (A) — faible.** Découle directement du §6 (pas de backlinks, pas de mentions de marque).

**Trust (T) — correct, c'est le point fort E-E-A-T.**
- Page « À propos » claire : mission + **méthode de vérification** explicite + politique « on déplace les codes expirés au lieu de les supprimer ».
- **Disclaimer** « non affilié à Roblox Corporation » présent (important).
- Pages `privacy`, `terms`, `contact`, formulaire de contact fonctionnel, dates de vérification.
- **Mais** : citation de sources visible sur seulement **13 pages /143**. La transparence des sources (« vérifié via Pocket Tactics + description in-game ») devrait être systématique.

**Recommandations prioritaires :**
1. **Créer 1-2 auteurs identifiés** (page bio avec expérience Roblox, photo, liens), passer le `author` JSON-LD en `Person`, ajouter une byline visible « Vérifié par … le … ».
2. **Prouver l'Experience** : capture d'écran de redemption sur les pages phares, mention « code testé en jeu », éventuellement courte vidéo maison.
3. **Systématiser les sources** : bloc « Sources vérifiées » sur 100 % des pages codes (déjà fait sur 13, à généraliser).
4. Schema `Organization` enrichi (logo, sameAs réseaux sociaux une fois créés, contactPoint).

---

## Les 3 chantiers qui débloquent le palier 100k (teaser Partie 2)

1. **Autorité & marque** (le verrou) : netlinking ciblé FR, présence sociale (TikTok/YouTube Shorts Roblox = canal naturel + backlinks + signaux de marque), relations avec créateurs FR.
2. **Pages de catégories indexables + hub d'actualités daté** : capter la moyenne traîne et la fraîcheur aujourd'hui à zéro.
3. **E-E-A-T humanisé** : auteurs nommés, preuve d'expérience, sources systématiques — pour que Google *fasse confiance* à un domaine jeune.

---

## Structure du rapport complet (à valider)

- **Partie 1 — Audit complet** ✅ (ce document)
- **Partie 2 — Stratégie de mots-clés & architecture de contenu** (clusters piliers/satellites, pages catégories, calendrier moyenne/longue traîne FR)
- **Partie 3 — Plan de contenu ultra-agressif 0 → 100k** (cadence de publication, modèles, priorisation par volume × faisabilité)
- **Partie 4 — Autorité, netlinking & marque** (acquisition de backlinks FR, social, créateurs, RP gaming)
- **Partie 5 — E-E-A-T & confiance** (auteurs, preuves, schema, signaux Trust)
- **Partie 6 — Scaling 100k → 500k + roadmap 12 mois & KPIs** (industrialisation, internationalisation FR→autres marchés, mesure)

Dis-moi si tu veux que j'enchaîne sur la **Partie 2** (stratégie mots-clés & architecture), ou que j'ajuste la pondération/priorisation avant.
