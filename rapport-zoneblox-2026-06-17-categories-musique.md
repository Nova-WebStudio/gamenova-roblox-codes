# Rapport — Mise en œuvre : pages de catégories + hub Musique (17 juin 2026)

Application concrète des Parties 2-3 de l'audit SEO. Deux chantiers livrés et intégrés au site.

## 1. 8 pages de catégories indexables (NOUVEAU)

Créées sous `/codes/<genre>/index.html` — désormais Google peut indexer des regroupements ciblant « codes <genre> roblox » (auparavant simple filtre JavaScript, invisible).

| Page | Jeux listés | Mots | Cible SEO |
|---|---|---|---|
| `/codes/simulator/` | 36 | ~1340 | codes simulateur roblox |
| `/codes/anime/` | 35 | ~1295 | codes anime roblox |
| `/codes/battle/` | 36 | ~1245 | codes combat / battlegrounds roblox |
| `/codes/rpg/` | 14 | ~890 | codes rpg roblox |
| `/codes/tower-defense/` | 11 | ~850 | codes tower defense roblox |
| `/codes/tycoon/` | 10 | ~785 | codes tycoon roblox |
| `/codes/obby/` | 5 | ~690 | codes obby roblox |
| `/codes/horror/` | 11 | ~780 | codes horreur roblox |

Chaque page contient : intro éditoriale FR unique (genre, mécaniques, rôle des codes), grille de cartes vers les jeux (vraies miniatures `tr.rbxcdn.com` via THUMBS), section « Comment utiliser un code », section « Codes qui ne marchent pas », FAQ (4 Q/R), chips de navigation inter-catégories. Les catégories minces (horror, tower-defense) ont été **enrichies** par curation : on y inclut les jeux du genre classés ailleurs (ex. tous les Tower Defense, les jeux d'horreur type Doors/Pressure/Forsaken). Le jeu « sport » unique (Muscle Legends) reste sur `/codes/` (non orphelin pour l'utilisateur).

**Schema par page :** `CollectionPage` + `ItemList` (jeux) + `BreadcrumbList` + `FAQPage` — tous validés.

## 2. Hub `/musique/` — Codes musique Roblox (NOUVEAU, gisement evergreen)

`/musique/index.html` : pilier ciblant « code musique roblox » / « id musique roblox » — l'un des plus gros gisements evergreen identifiés en Partie 2 (Dexerto y ranke ; volume stable, faible maintenance).

- **43 codes** répartis en 2 tableaux : chansons populaires & tendances (25) + sons mèmes & dialogues drôles (18), avec boutons « Copier ».
- Sélection **adaptée au jeune public** (sons explicites écartés).
- Sections : intro, mode d'emploi Boombox, « pourquoi mon code ne marche pas », FAQ (5 Q/R), bloc sources.
- **Honnêteté (règles Zoneblox) :** sources vérifiées **Beebom + PCGamesN** (corroborées par recherche multi-sources), date du 17/06, et **disclaimer visible** rappelant que Roblox peut retirer un audio à tout moment (politique de licence) — les codes musique ne sont pas garantis éternels.
- ~1080 mots, schema `Article` + `ItemList` + `BreadcrumbList` + `FAQPage` validés.

## 3. Intégration

- **Maillage :** bloc « Parcourir les codes par catégorie » ajouté sur `/codes/` avec liens crawlables vers les 8 catégories + un bouton mis en avant vers `/musique/`. Les pages catégories se maillent entre elles (chips).
- **Sitemap :** +9 URL (`sitemap.xml` passe de 235 à 244 entrées), XML valide.
- **Nav :** inchangée (7 entrées, règle respectée — pas d'ajout « Musique » dans la nav globale pour ne pas toucher les 244 fichiers).

## 4. ⚠️ Incident de troncature (rencontré et réparé)

Lors de l'insertion du bloc catégories, `codes/index.html` a été **tronqué** (perte du `<div class="container">` d'ouverture et du `</html>` final). Conforme au bug récurrent documenté.

**Réparation :** reconstruction atomique depuis `git show HEAD:codes/index.html` (version complète, contenant déjà `fruit-battlegrounds codes:5`), ré-application du bloc en **une seule écriture Python**, vérifiée (61 244 octets, `</html>` présent, divs équilibrés, 0 octet nul). Les 8 pages catégories et le hub musique ont été générés par script Python (écriture atomique unique par fichier) — méthode la plus fiable contre la troncature.

## 5. ⚠️ Verrou git à lever avant commit

Un fichier `.git/index.lock` **résiduel** est présent et n'a pas pu être supprimé automatiquement (« Operation not permitted »). Il risque de bloquer `git add`/`commit`. **Avant de committer, supprime-le** :

```
del .git\index.lock
```
(ou sous PowerShell : `Remove-Item .git\index.lock`)

## 6. Contrôle qualité final (tout vert)

- `node --check js/main.js` : OK
- 9 nouvelles pages : se terminent par `</html>`, 0 octet nul, GA4 présent, `main.js?v=24`, nav 7 entrées, balises `<div>` équilibrées
- JSON-LD : tous les blocs valides (CollectionPage/ItemList/FAQPage/BreadcrumbList/Article)
- Aucun lien interne cassé depuis les pages catégories (tous les `/codes/X.html` ciblés existent)
- `sitemap.xml` : XML valide, 244 URL, se termine par `</urlset>`
- `codes/index.html` reconstruit : complet et équilibré

## 7. Fichiers touchés

**Nouveaux :** `codes/{simulator,anime,battle,rpg,tower-defense,tycoon,obby,horror}/index.html`, `musique/index.html`.
**Modifiés :** `codes/index.html` (bloc catégories + lien musique), `sitemap.xml` (+9 URL).

## 8. Suite recommandée (prochaines itérations)

- Satellites musique (`/musique/rap/`, `/phonk/`, `/troll/`) pour élargir la couverture.
- Ajouter `author` `Person` (Partie 5) sur ces pages quand l'auteur identifié sera créé.
- Re-tester quelques ID musique en jeu pour la preuve d'Experience (E-E-A-T).
- Étoffer `obby` (5 jeux) si de nouveaux jeux du genre entrent au catalogue.

## Pour publier

Dans le dossier GameNova : **(1)** supprime `.git\index.lock` si présent, puis **(2)** lance
`git add -A && git commit -m "Pages catégories indexables + hub musique" && git push origin main`.
Hostinger déploie automatiquement après le push.
