# Rapport Zoneblox — 13 juin 2026 (samedi)

## Résumé

Run centré sur la **règle CONTENU MINIMUM (indexation)** : 6 pages codes parmi les jeux les plus populaires ont été étoffées au-delà de **1200 mots** de rédactionnel français unique, avec descriptif de jeu développé, 6 astuces spécifiques, FAQ enrichie et section « À propos » approfondie. Aucun code inventé. Samedi → pas de mise à jour « Jeu de la semaine » (lundi uniquement).

## Étape 0 — Surveillance des sources de codes

L'API Roblox reste **inaccessible** depuis cet environnement (le shell n'a aucun accès réseau sortant : `curl` renvoie HTTP 000 sur tous les domaines ; `web_fetch` est restreint au provenance set). La détection automatique via `code-watch.json` (résolution universeId, description in-game, shout de groupe) n'a donc pas pu s'exécuter.

Vérification de repli **par recherche web (2 sources)** sur les jeux chauds prioritaires :

| Jeu | Statut |
|-----|--------|
| Grow a Garden (original) | Inchangé — RDCAward, BEANORLEAVE10, torigate toujours listés (Game8, Beebom). |
| Blue Lock Rivals | Inchangé — NELHIORI / SNOWFLAKE / HIORIREWORK déjà en page (ProGameGuides, PCGamer). |

⚠️ **À surveiller** : les agrégateurs mentionnent un nouveau jeu **« Grow a Garden 2 »** lancé le 12 juin 2026 (code de lancement **TEAMGREENBEAN** → 3 Green Bean Seeds). C'est un **jeu distinct** de notre page `grow-a-garden` : je n'ai donc **pas** contaminé la page existante avec ce code. À évaluer comme **nouveau jeu à ajouter** (ÉTAPE 1) dès que l'API permettra de vérifier l'éligibilité ≥ 4000 joueurs, l'universe ID et la miniature.

`tools/code-watch.json` **non modifié** : sans véritable fetch des descriptions (API down), bumper `lastChecked`/`descExcerpt` serait malhonnête. Snapshots laissés intacts.

## Étape 3 — Étoffement « thin content » (6 pages, priorité indexation)

Toutes réécrites en un seul passage Python (restauration/lecture → édition → écriture unique), vérifiées par parser HTML (équilibre des `<div>`), fin `</html>` et comptage de mots :

| Page | Avant | Après |
|------|------:|------:|
| codes/steal-a-brainrot.html | 821 | **1583** |
| codes/blue-lock-rivals.html | 1040 | **1534** |
| codes/blade-ball.html | 950 | **1325** |
| codes/pet-simulator-99.html | 787 | **1243** |
| codes/volleyball-legends.html | 845 | **1209** |
| codes/grow-a-garden.html | 825 | **1208** |

Pour chaque page : remplacement des **3 astuces génériques identiques** (présentes à l'identique sur tout le site → mauvais pour le SEO) par **6 astuces spécifiques au jeu** ; ajout de **3 questions FAQ** propres au jeu (gameplay, codes, méta) ; ajout de **2 à 3 paragraphes « À propos »** couvrant gameplay, progression, monnaies/ressources et ce que donnent les codes ; pour Steal a Brainrot, ajout d'une section « Comment jouer » dans l'intro. Contenu honnête et utile, liens internes vers tier lists/guides.

📋 **Backlog indexation** : avec le compteur strict utilisé ici, **~110 pages codes restent < 1200 mots**. Les plus prioritaires à étoffer aux prochains runs (max 6/run) : blox-fruits, fisch, fish-it, anime-vanguards, anime-last-stand, world-fighters, dress-to-impress, adopt-me, king-legacy, doors.

## Étapes 1, 2, 4, 5, 6 — non réalisées ce run

- **Ajout de jeux / tier lists / guides / UGC** : nécessitent l'API Roblox (éligibilité, universe IDs, miniatures `tr.rbxcdn.com`, vidéos vérifiées via oEmbed). Données non inventables → reportées dès rétablissement de l'accès réseau. Candidat noté : *Grow a Garden 2*.
- **Codes existants** : aucun nouveau code confirmé pour les pages vérifiées ; aucune page codes modifiée côté tableau de codes.

## Étape 8 — QC (tout vert sur les 6 pages modifiées)

| Check | Résultat |
|-------|----------|
| Se termine par `</html>` | ✅ 6/6 |
| Octets nuls | ✅ 0 |
| Équilibre des `<div>` (parser HTML) | ✅ 0 ouvert / 0 orphelin |
| Nav 6 entrées | ✅ |
| GA4 `G-FEL71QVHNL` | ✅ |
| Cache JS `main.js?v=23` | ✅ (js/main.js non modifié → pas de bump) |
| Bandeau CTA `data-cta="guidelink"` unique | ✅ |
| ≥ 1200 mots FR + descriptif développé | ✅ 6/6 |
| `node --check js/main.js` | ✅ |

## ⚠️ État du dépôt git (à connaître avant de committer)

Le working tree contenait **déjà**, avant ce run, des modifications non liées à mes éditions : `CLAUDE.md` et `rapport-zoneblox-2026-06-12.md` marqués modifiés, plus des suppressions/renommages indexés dans `tier-list/`, `tools/` et `ugc-gratuit/` (vraisemblablement un run précédent interrompu, possible souci de casse de noms de fichiers). Je n'y ai **pas touché**. `git add -A` les ré-ajoutera ; vérifie d'un coup d'œil `git status` avant de pousser si tu veux écarter ces changements.

## Fichiers touchés par ce run

- `codes/steal-a-brainrot.html`, `codes/grow-a-garden.html`, `codes/blade-ball.html`, `codes/volleyball-legends.html`, `codes/pet-simulator-99.html`, `codes/blue-lock-rivals.html`
- `rapport-zoneblox-2026-06-13.md` (ce rapport)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
