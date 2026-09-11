# Analyse Search Console + plan d'action SEO — Zoneblox (11/09/2026)

Basé sur tes exports GSC (Performance + Couverture d'indexation, ~13 juin → 4 sept 2026).

## Chiffres clés

- **~140 clics / ~5 000 impressions** sur la période. Position moyenne ~23 (donc rarement en page 1).
- **France = 90 % des clics** (125 clics / 2 249 impr). Belgique, Suisse, Maghreb (Maroc 456 impr / 0 clic, Algérie 299 / 0) derrière.
- **Mobile : position ~7,9** (6,8 % CTR) vs **Ordinateur : position ~41** (2 % CTR). Tu ranks bien mieux sur mobile.
- **Indexation en train de décrocher : 237 pages NON indexées contre 233 indexées** — et l'écart se creuse à chaque ajout de page. C'est LE problème n°1.
- Page la plus performante, de loin : **`guides/vendre-des-citrons.html` (69 clics, position 4,25)** — contenu 100 % français.

---

## 🔴 PROBLÈME N°1 — Fragmentation des URL (jusqu'à 4 versions par page)

C'est ce qui plombe l'indexation. Google voit **plusieurs variantes de la même page** et se disperse :

1. **`www.zoneblox.com` ET `zoneblox.com`** apparaissent tous deux dans les résultats.
   *Preuve :* `www.zoneblox.com/guides/vendre-des-citrons.html` = 69 clics, mais `zoneblox.com/guides/vendre-des-citrons.html` = 2 clics séparément. Même page, deux hôtes, signaux divisés.
2. **Ancien schéma `/codes/<slug>.html` ET nouveau `codes-<slug>.html`** cohabitent dans l'index.
   *Preuve :* `/codes/mini-guerre.html` (78 impr, pos 8,7) capte le trafic pendant que `codes-mini-guerre.html` (11 impr, pos 3,9) — pourtant mieux classé — reçoit 0 clic. Les deux se cannibalisent.
3. **Des pages `/en/` existent et sont indexées** (`/en/codes/paint-and-seek.html`, `/en/guides/…`, `/en/tier-list/…`) alors qu'il ne devrait pas y avoir de pages EN.

**Confirmé par le rapport Couverture :** 152 « page avec redirection », 16 « Google a choisi une autre URL canonique », 4 « doublon sans canonique », 40 « explorée, actuellement non indexée ».

### Ce que tu dois faire (par ordre d'impact)

1. **Vérifier que la redirection www→non-www fonctionne réellement en production** (le `.htaccess` la contient, mais Google indexe encore des URL www → soit la conso tarde, soit une `<link rel="canonical">` de page pointe encore vers `www`). → Ouvre 2-3 pages en `www.zoneblox.com/...` et confirme le 301 vers `zoneblox.com/...`. Puis vérifie que **chaque `canonical` pointe vers la version non-www + nouveau schéma**.
2. **Supprimer / neutraliser les pages `/en/`** : soit les retirer (404/410), soit `noindex`, et **enlever `sitemap-en.xml`** (ne pas le déclarer). Elles sont thin et gaspillent ton budget de crawl.
3. **Nettoyer l'ancien répertoire `codes/`** : les fichiers `codes/<slug>.html` existent encore physiquement dans le dossier. Ils sont censés être de simples 301, mais leur présence crée des doublons potentiels — surtout des pages non couvertes par une règle de redirection (ex. `codes/anime/index.html`, une page catégorie pleine de liens à l'ancien schéma). → S'assurer que **tout `/codes/...` est bien 301 vers la racine** (règle générique `RedirectMatch 301 ^/codes/(.+)\.html$ /codes-$1.html` plutôt qu'une ligne par jeu), et qu'aucun lien interne ne pointe encore vers `/codes/`. (Bonne nouvelle : `js/main.js` utilise déjà le bon schéma.)

> Une fois ces doublons résolus, Google reconcentre l'autorité sur UNE URL par page → meilleures positions **sans écrire une ligne de contenu**.

---

## 🟠 PROBLÈME N°2 — Indexation qui stagne / fraîcheur non signalée

- La moitié du site n'est pas indexée, et les 40 pages « explorées, non indexées » = Google les juge trop pauvres ou trop semblables.
- **Ton `sitemap.xml` a des `lastmod` figés au 22/07/2026** sur presque toutes les pages, alors que tu revérifies les codes quasi chaque jour (« 🔄 Vérifié le »). Google ne voit donc aucune raison de recrawler → tes pages paraissent « gelées en juillet ».

### À faire
1. **Générer le `lastmod` du sitemap depuis la vraie date « Vérifié le » de chaque page** (à automatiser dans la tâche quotidienne). C'est un signal de fraîcheur gratuit, crucial pour des pages « codes ».
2. **Passer à un sitemap index** qui déclare `sitemap-codes.xml`, `-guides.xml`, `-tier-list.xml`, `-pages.xml` (aujourd'hui `robots.txt` ne pointe que vers un seul gros `sitemap.xml`).
3. Pour les 40 pages non indexées : soit les **étoffer** en contenu unique ≥1200 mots (règle déjà dans ton process), soit **fusionner** les jeux morts/à ~0 impression. Ne pas multiplier les pages faibles : la couverture montre que **produire plus de pages sans les faire indexer aggrave le ratio**.

---

## 🟡 PROBLÈME N°3 — CTR ≈ 0 même en page 1

Plusieurs requêtes FR sont en page 1 mais ne rapportent aucun clic :
- « code mini guerre » : position 10 / **52 impressions / 0 clic**.
- Page d'accueil : position 66 / **586 impressions / 3 clics** (0,5 %).
- Onglet « Apparence dans les résultats » **vide** → tu n'obtiens **aucun résultat enrichi** (FAQ, fil d'Ariane) malgré ton JSON-LD.

### À faire
1. **Réécrire les title/meta** des pages FR qui touchent la page 1 (mini-guerre, defend-ur-base-with-anime, ferme-d-anneaux, evasion-clavier, tier lists Blue Lock Rivals) : requête exacte + accroche + « (septembre 2026) ». C'est le levier de clic le plus rapide.
2. **Vérifier que le JSON-LD FAQPage/BreadcrumbList valide** (test de résultats enrichis Google) — tu n'en gagnes aucun actuellement, c'est du CTR laissé sur la table.
3. Retravailler le title/description de l'accueil : il capte 586 impressions sur des requêtes génériques (« roblox code », « code roblox ») mais en position 66. Cible plutôt une requête FR réaliste.

---

## 🎯 STRATÉGIE DE FOND — ton avantage, c'est le FRANÇAIS

Les données sont sans ambiguïté :
- **Tes seules vraies victoires sont du contenu français / franco-original** : vendre des citrons, mini guerre, défends ta base avec des anime, construire une ferme d'anneaux, évasion clavier, liminalité invisible, cliqueur phonk, « tier list blue lock rivals 2026 ».
- **Les requêtes génériques anglaises/mondiales** (roblox codes, blox fruits codes, pet simulator 99, arsenal, brookhaven, king legacy) te classent **entre 40 et 90** = invisibles. Tu ne peux pas battre Pro Game Guides / Beebom dessus à court terme (autorité de domaine trop faible).

**Donc : arrête de courir après les gros mots-clés anglais saturés. Concentre-toi sur l'intention française :**
1. **Noms/traductions FR** de jeux et de quêtes (« vendre des citrons », « défends ta base », « construire une ferme d'anneaux », « évasion clavier ») — peu de concurrence, tu y es déjà 1re.
2. **Modificateurs FR** : « tier list <jeu> 2026 », « code <jeu> roblox français », « meilleur <élément> <jeu> ».
3. **Jeux de niche à faible concurrence** plutôt qu'un 180ᵉ « codes <gros jeu> » où tu finis 60ᵉ.
4. **Priorité mobile** (ton audience = ados FR sur téléphone, où tu ranks déjà ~8ᵉ) : vitesse et lisibilité mobile avant tout.

---

## Plan d'action priorisé (résumé)

| Priorité | Action | Effort | Impact |
|----------|--------|--------|--------|
| **P1** | Confirmer 301 www→non-www + canonicals non-www partout | Faible | 🔥 Élevé |
| **P1** | Supprimer/`noindex` les pages `/en/` + retirer `sitemap-en.xml` | Faible | 🔥 Élevé |
| **P1** | Redirection générique `/codes/*` → `codes-*` + purge liens internes anciens | Moyen | 🔥 Élevé |
| **P2** | `lastmod` du sitemap = vraie date « Vérifié le » (auto) | Moyen | Élevé |
| **P2** | Sitemap index déclarant tous les sous-sitemaps dans robots.txt | Faible | Moyen |
| **P2** | Étoffer ou fusionner les 40 pages « explorées non indexées » | Élevé | Élevé |
| **P3** | Réécrire title/meta des pages FR en page 1 + mois/année | Moyen | Moyen |
| **P3** | Valider JSON-LD FAQ/Breadcrumb (résultats enrichis) | Faible | Moyen |
| **Fond** | Doubler le contenu franco-original ciblé, lâcher les gros mots-clés EN | — | 🔥 Élevé (durable) |

**Le plus rentable maintenant :** les 3 actions P1 (canonicalisation). Elles ne demandent aucun nouveau contenu et devraient débloquer l'indexation de dizaines de pages déjà écrites.
