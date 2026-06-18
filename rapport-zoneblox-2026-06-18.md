# Rapport Zoneblox — 18 juin 2026 (jeudi)

## Résumé

Run de maintenance ciblé : surveillance des sources de codes, remédiation du « thin content » (indexation), et QC d'intégrité du site. Jeudi → pas de mise à jour « Jeu de la semaine » (réservée au lundi).

## Étape 0 — Surveillance des sources de codes

16 jeux chauds vérifiés via l'API Roblox (descriptions in-game) + shouts/descriptions des groupes créateurs des jeux les plus « code-actifs » (Blox Fruits, Fruit Battlegrounds, World Fighters, Defend ur Base).

- **Aucun nouveau code candidat détecté.** Les descriptions in-game et les shouts de groupe sont inchangés depuis le snapshot de la veille. Pour Blox Fruits, Fruit Battlegrounds et World Fighters, les codes mentionnés en description (ex. `YOO1M110K`) sont déjà connus et publiés.
- Shouts de groupe : tous `null` au moment du check.
- `tools/code-watch.json` : `lastChecked` mis à jour pour les 16 jeux (2026-06-18). JSON revérifié valide.
- Note de catalogue : **Anime Last Stand** affiche seulement ~200 joueurs simultanés (en forte baisse) — à surveiller pour l'éligibilité future, mais reste un classique.

## Étapes 2-3 — Codes & contenu minimum (anti thin-content)

Scan de toutes les pages `codes/*.html` (143 pages) pour le volume rédactionnel. 26 pages étaient sous le seuil de 1200 mots. Les **6 plus courtes** ont été étoffées avec du contenu français honnête et utile (genre, éditeur, monnaies du jeu, rôle réel des codes, rythme de mises à jour, « pourquoi un code peut ne plus marcher ») :

| Page | Avant | Après |
|------|-------|-------|
| `codes/fish-it.html` | 1130 | 1319 |
| `codes/slap-battles.html` | 1152 | 1353 |
| `codes/project-slayers.html` | 1156 | 1348 |
| `codes/bloxstrike.html` | 1157 | 1262 |
| `codes/volleyball-legends.html` | 1159 | 1321 |
| `codes/be-a-brainrot.html` | 1165 | 1358 |

Aucun code inventé ; aucune date « Mis à jour le… » modifiée (pas de changement de codes). Ajout d'un bloc « Jeux similaires » manquant sur `be-a-brainrot` (liens vérifiés existants).

### Pages codes encore < 1200 mots (à étoffer aux prochains runs, max 6/run)
brookhaven (1166), anime-vanguards (1167), blade-ball (1168), tower-of-hell (1170), toilet-tower-defense (1173), slime-rng (1175), twenty-one (1179), liminalite-invisible (1180), my-gaming-cafe (1180), adopt-me (1181), fire-force-online (1184), fisch (1185), grow-a-garden-2 (1188), spin-a-brainrot (1192), cliqueur-phonk (1194), grand-piece-online (1194), peroxide (1197), anime-reversal (1198), pressure (1198), anime-rangers-x (1199).

## Étape 8 — QC intégrité

- `GAMES_INDEX` (143) ↔ `ALL_GAMES` (143) : **synchronisés**, aucun écart.
- `node --check js/main.js` : **OK**.
- Version cache JS : **uniforme `main.js?v=24`** sur les 253 pages (la note v=19 dans CLAUDE.md est obsolète ; la cohérence est respectée).
- Équilibre des `<div>` : propre sur l'ensemble du site avant édition ; les 6 pages modifiées revérifiées (un `</div>` manquant introduit puis corrigé sur `be-a-brainrot`).
- Octets nuls : **aucun**.
- Toutes les pages se terminent par `</html>` (vérifié via lecture des fichiers).
- GA4 `G-FEL71QVHNL` : présent partout.
- Nav 7 entrées + lien `/avatar/` : présent partout.
- Bandeau CTA `data-cta="guidelink"` : présent sur toutes les pages codes (seul `codes/_TEMPLATE.html` en est dépourvu, ce qui est normal).

### Note technique (run uniquement)
Le mount bash du bac à sable a servi un cache de lecture périmé pour les fichiers réécrits via les outils fichiers (tailles figées, fin de fichier tronquée à la lecture **bash**). Vérification recoupée via l'outil de lecture fichier (état faisant autorité, identique à ce que voit la machine de Peter) : **les 6 fichiers sont complets et bien fermés**. Les écritures bash (ex. `code-watch.json`) se sont, elles, bien propagées (timestamps 06-18 confirmés côté fichier). Aucune troncature réelle.

## Non traité ce run
Ajout de 6 jeux (Étape 1), nouvelles tier lists (Étape 4), guides complets (Étape 5), UGC (Étape 6) : non abordés ce run, centré sur surveillance + indexation + QC.

## Ajout de 10 nouveaux jeux (« la totale »)

10 jeux Roblox tendance de juin 2026, **tous ≥4000 joueurs simultanés** et **tous avec codes actifs vérifiés par 2+ sources**, absents du catalogue, ajoutés avec page complète (≥1200 mots), vraie miniature `tr.rbxcdn.com`, 2 vidéos YouTube vérifiées via oEmbed, astuces, FAQ, À propos + 3 jeux similaires, bandeau CTA, et intégration dans toutes les sources de données.

| Jeu | Joueurs | Genre | Mots | Codes |
|-----|--------:|-------|-----:|------:|
| Spin a Soccer Card | ~32 700 | Sport/RNG | 1454 | 6 |
| Merge a Nuke | ~30 400 | Simulation | 1372 | 3 |
| VV: ULTIMATUM | ~31 100 | RPG anime (Bleach) | 1338 | 1 |
| FIFA Super Soccer | ~27 400 | Sport | 1287 | 4 |
| Hypershot | ~26 200 | FPS | 1289 | 4 |
| BlockSpin | ~22 000 | Combat/armes | 1322 | 3 |
| Run a Restaurant | ~21 300 | Tycoon | 1284 | 1 |
| Squid Game X | ~18 400 | Survie | 1312 | 6 |
| Catch a Monster | ~18 300 | Simulation | 1348 | 6 |
| Brainrot Evolution | ~4 800 | Brainrot/sim | 1305 | 6 |

Sélection : jeux écartés car **sans système de codes** (Animal Hospital 69k, Violence District 40k, Fling Things and People 34k, Flee the Facility, Ink Game) ou **retombés sous 4000 joueurs** (YBA, Gym League, Heaven Stand, Anime Paradox en maintenance).

Intégrations réalisées pour chaque jeu : carte sur `index.html` (section « Nouveaux jeux »), `ALL_GAMES` + `THUMBS` (codes/index.html), `GAMES_INDEX` + `ROBLOX_THUMBS` + `ROBLOX_UNIVERSE_IDS` (js/main.js), SVG de fallback, `<url>` au sitemap, `hotGames` + `snapshots` (code-watch.json). Synchro vérifiée : **GAMES_INDEX 153 = ALL_GAMES 153**, aucun écart. `node --check js/main.js` OK. Sitemap : 254 URLs, bien formé. Toutes les pages finissent par `</html>`, divs équilibrés, GA4 + nav 7 entrées + cache `v=24` présents, miniatures `tr.rbxcdn.com` (SVG en fallback `onerror` uniquement), aucun octet nul, aucune vidéo invalide.

## Sitemap — mise à jour des `lastmod`
Réalignement de tous les `lastmod` du `sitemap.xml` sur la **vraie date de dernière modification** de chaque page (date du dernier commit git), et **2026-06-18** pour les 6 pages éditées ce jour. 237 entrées ajustées, XML revérifié bien formé (244 URLs, se termine par `</urlset>`). Choix volontaire de **ne pas** tout dater à aujourd'hui (un `lastmod` massivement faux peut être perçu comme du spam par Google). Distribution : 226 pages au 06-16, 1 au 06-17, 17 au 06-18.

### Indexation Google (rappel)
64/244 pages indexées sur un domaine de ~16 jours = normal. Re-soumettre le sitemap ne force pas l'indexation. Leviers réels : étoffer le thin content (en cours), demander l'indexation des pages prioritaires via l'inspection d'URL dans Search Console (~10/jour), obtenir des backlinks, et patienter. Une seule soumission du sitemap suffit (Google le relit seul).

## Fichiers touchés
- `tools/code-watch.json`
- `sitemap.xml` (lastmod réalignés)
- `codes/fish-it.html`, `codes/slap-battles.html`, `codes/project-slayers.html`, `codes/bloxstrike.html`, `codes/volleyball-legends.html`, `codes/be-a-brainrot.html`
- `rapport-zoneblox-2026-06-18.md` (ce rapport)

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
