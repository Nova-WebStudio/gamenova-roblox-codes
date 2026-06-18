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
