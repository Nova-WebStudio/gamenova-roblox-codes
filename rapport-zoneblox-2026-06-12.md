# Rapport Zoneblox — 12 juin 2026

## Étape 0 — Surveillance des sources de codes

L'API Roblox reste **inaccessible** depuis cet environnement (connexion bloquée sur tous les domaines roblox.com depuis le shell, `web_fetch` restreint). Vérification effectuée **par recherche web (2 sources croisées par jeu)** pour les 15 jeux de `hotGames` :

| Jeu | Statut |
|-----|--------|
| Blox Fruits | Inchangé (EASTEREXP toujours le + récent) |
| Grow a Garden | Inchangé (RDCAward, BEANORLEAVE10, torigate) |
| Blue Lock Rivals | Inchangé (NELHIORI/SNOWFLAKE/HIORIREWORK déjà en page) |
| Volleyball Legends | Inchangé (UPDATE_73, JUNGLE_MAP, JUNE_2026) |
| Anime Vanguards | Inchangé (Cog5th, 223, Liberation, DMCAFree déjà en page) |
| Anime Last Stand | Inchangé (DemonicCyborg etc. déjà en page) |
| Blade Ball, King Legacy, TDS, PS99, Steal a Brainrot, Noob Incremental | Aucun nouveau code |
| **Fisch** | 🔴 **19 codes expirés détectés** → page mise à jour |
| **World Fighters** | 🟢 **9 nouveaux codes confirmés** → page mise à jour |
| **Fruit Battlegrounds** | 🟠 2 codes invalides retirés, 1 ajouté, récompenses corrigées |

`tools/code-watch.json` réécrit : `lastChecked` + `knownCodes` à jour pour les 15 jeux, JSON validé.

## Étape 2 — Codes mis à jour (avec 2 sources chacun)

- **codes/fisch.html** : actifs réduits à 4 (**Crews, scarlet, TemporarySubmarine, CARBON** — sources : Pocket Tactics 9/06 + Pro Game Guides 7/06). Les 19 autres déplacés dans une nouvelle section « codes expirés ». Récompense exacte de Crews ajoutée.
- **codes/world-fighters.html** : ajout de **WOOGARPP (nouveau), UPDATE7PT2, DRAGONDEFENSEHARD, SORRYYADELAY, UPDATE7, SRRY5SHUTDOWSERVANT, UPDATE6PT2, BATTLEPASS_SEASON2, 25KLIKESAMAZING!!!** (sources : Try Hard Guides 11/06 + Beebom/PGG). 11 codes actifs au total, FAQ mise à jour.
- **codes/fruit-battlegrounds.html** : retrait de YOO1M110K! (introuvable dans les sources) et BIG1M170K!! (expiré selon Pocket Tactics + GameRant) ; ajout d'**OMGUPDATE22** ; récompense d'ITSTHEBILLION! corrigée (8 500 Gems + titre). 5 actifs.
- Compteurs et dates synchronisés dans `ALL_GAMES` (codes/index.html) et `GAMES_INDEX` (js/main.js) — vérification croisée 0 écart.

## Étape 5 — NOUVEAU GUIDE COMPLET : Anime Vanguards 📚

Création de **guides/anime-vanguards.html** (gabarit blox-fruits, 100 % français, 2 sources : animevanguardsguide.com 11/06 + endsights.com) : sommaire ancré, guide débutant, progression Actes 1-5 et 6-10, farm de gemmes & pity, tableau des meilleures unités (méta juin 2026), priorité des traits (Monarch/Vampire), 4 règles de placement, mode Infini/raids/boss, FAQ. JSON-LD Article + Breadcrumb + FAQPage valides.

Intégrations : carte dans guides/index.html (+ ItemList), `<url>` sitemap, bouton « 📚 Guide complet » dans le hero de codes/anime-vanguards.html et tier-list/anime-vanguards.html, bandeau CTA de la page codes mis à niveau (Guide en dégradé + Tier list en contour).

## Étape 3 — Présentations « À propos » (6 pages populaires)

Sections « À propos de <Jeu> » (2 paragraphes FR) + bloc « 🎮 Jeux similaires » (3 jeux de la même catégorie) ajoutées entre `<!-- ABOUT-START/END -->` sur : **the-strongest-battlegrounds, volleyball-legends, fruit-battlegrounds, world-fighters, tower-defense-simulator, all-star-tower-defense**.

📋 Backlog documenté : il reste ~71 pages codes sans section À propos et ~93 avec moins de 2 vidéos — à traiter par lots de 6 sur les prochains runs.

## Étapes 1, 4, 6, 7

- **Ajout de 6 jeux : non réalisé** — l'API Roblox (éligibilité ≥ 4000 joueurs, universe IDs, miniatures tr.rbxcdn.com) est inaccessible et ces données ne s'inventent pas. À refaire dès que l'accès réseau le permet.
- **Tier lists** : pas de changement de méta détecté sur les jeux vérifiés ce run.
- **UGC** : codes/ugc-limited.html comparé à Roblox Den (8/06) — liste identique (32 actifs), aucun changement. ugc-gratuit : RAS.
- **Jeu de la semaine** : vendredi → non concerné (lundi uniquement).

## Étape 9 — Cache JS

`js/main.js` modifié (compteurs de codes) → version bumpée **v=21 → v=22 sur les 193 fichiers HTML** (+ le nouveau guide créé directement en v=22... corrigé au bump : 100 % des pages en v=22, 0 résidu).

## Étape 8 — QC (tout vert)

| Check | Résultat |
|-------|----------|
| 196 fichiers modifiés finissent par leur balise de fermeture | ✅ |
| Octets nuls | ✅ aucun |
| `node --check js/main.js` | ✅ |
| `tools/code-watch.json` JSON valide, finit par `}` | ✅ |
| JSON-LD valide sur tous les fichiers modifiés | ✅ |
| GAMES_INDEX ↔ ALL_GAMES | ✅ 0 écart |
| GA4 + nav 6 entrées sur le nouveau guide | ✅ |
| CTA `data-cta="guidelink"` unique par page codes | ✅ |
| Cache JS uniforme v=22 | ✅ 193 fichiers |
| Aucun iframe dQw4w9WgXcQ | ✅ |

## Fichiers touchés

- `codes/fisch.html`, `codes/world-fighters.html`, `codes/fruit-battlegrounds.html` (codes + dates)
- `guides/anime-vanguards.html` (**nouveau**), `guides/index.html`, `sitemap.xml`
- `codes/anime-vanguards.html`, `tier-list/anime-vanguards.html` (liens guide)
- 6 pages codes (sections À propos)
- `codes/index.html`, `js/main.js` (compteurs), `tools/code-watch.json`
- 193 HTML (bump v=22)
- `rapport-zoneblox-2026-06-12.md` (ce rapport)

---

**Pour publier :** dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.
