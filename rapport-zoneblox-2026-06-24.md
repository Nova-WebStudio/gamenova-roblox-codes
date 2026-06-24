# Rapport Zoneblox — 24 juin 2026

Run automatique quotidien. Mercredi → pas de mise à jour « Jeu de la semaine » (lundi uniquement).

## État du site (audit d'intégrité)
- **155 jeux** au catalogue, **53 tier lists**, **41 guides complets**.
- `GAMES_INDEX` ↔ `ALL_GAMES` : **synchronisés** (155/155, aucun manquant des deux côtés).
- Équilibre des `<div>` : **0 fichier déséquilibré**.
- Troncatures / octets nuls : **aucun** sur l'ensemble du site.
- `node --check js/main.js` : **OK**.
- Contenu minimum (indexation) : **les 155 pages codes dépassent 1200 mots** (minimum constaté : 1293 mots, `grow-a-garden-2`). Aucune page « thin content ».

## Correctif principal — violation de règle « miniature SVG »
`anime-rift-tower-defense` utilisait `/images/games/anime-rift-tower-defense.svg` comme **miniature affichée** (interdit par la règle absolue : jamais de SVG comme miniature d'un jeu).

- Place ID résolu : `115684951340700` → universe ID **`7651084572`** (vérifié via l'API officielle Roblox).
- Vraie miniature récupérée : `https://tr.rbxcdn.com/180DAY-000826b5aefec382cc3367192cdb5c2f/768/432/Image/Png/noFilter`.
- Mise à jour dans **les 6 emplacements** : `ROBLOX_THUMBS` (js/main.js), `THUMBS` (codes/index.html), `src` du hero (codes/anime-rift-tower-defense.html), `src` du guide (guides/anime-rift-tower-defense.html), cartes des hubs `codes/anime/index.html` et `codes/tower-defense/index.html`. Le SVG reste uniquement en `onerror` (fallback).
- `ROBLOX_UNIVERSE_IDS['anime-rift-tower-defense']` passé de `0` → **`7651084572`** (active le rafraîchissement client-side).

## Cache JS
`js/main.js` modifié → version **v=27 → v=28** propagée dans **269 fichiers .html** (racine, codes/, tier-list/, guides/, ugc-gratuit/, avatar/). Vérifié : 269 occurrences `main.js?v=28`, 0 résiduelle en v=27.

## ÉTAPE 0 — Surveillance des codes (jeux hot)
Descriptions in-game récupérées en direct via l'API Roblox pour : `grow-a-garden`, `steal-a-brainrot`, `fisch`, `blade-ball`, `blue-lock-rivals`, `volleyball-legends`. **Aucun nouveau code candidat** dans les descriptions (ces jeux distribuent leurs codes via menu in-game / Discord, pas la description). Snapshots `tools/code-watch.json` rafraîchis (lastChecked, descLen, descExcerpt) — JSON revalidé.

## ÉTAPE 2/3 — Vérification codes (jeux populaires)
- **Steal a Brainrot** : confirmé **aucun code public actif** (Beebom, PCGamesN, RBLXGuide) — cohérent avec la page actuelle. Pas de changement.
- **Grow a Garden** : les sources récentes portent en réalité sur *Grow a Garden 2* (jeu distinct, page dédiée `grow-a-garden-2.html` ; code `TEAMGREENBEAN` lui appartient). Aucun nouveau code confirmé par 2 sources pour le jeu original → **pas d'édition** (on n'invente pas).
- Décision : aucune édition de page codes n'était justifiée par 2 sources fiables aujourd'hui ; pas de modification des dates « Mis à jour le… » pour rester honnête.

## Fichiers touchés
- `js/main.js` (miniature + universe ID + implicite via cache).
- `codes/index.html`, `codes/anime-rift-tower-defense.html`, `guides/anime-rift-tower-defense.html`, `codes/anime/index.html`, `codes/tower-defense/index.html` (miniature réelle).
- `tools/code-watch.json` (snapshots).
- 269 fichiers `.html` (bump cache v=28).

## QC final
Tous les fichiers modifiés vérifiés : HTML terminant par `</html>`, `js/main.js` valide (`node --check`), `code-watch.json` JSON valide, GA4 (`G-FEL71QVHNL`) et nav 7 entrées (dont `/avatar/`) présents sur la page corrigée, aucune troncature, aucun octet nul.

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`
Hostinger déploie automatiquement après le push.
