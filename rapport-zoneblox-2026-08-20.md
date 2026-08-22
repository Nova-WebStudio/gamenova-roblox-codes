# Rapport Zoneblox — 20 août 2026

Run de maintenance quotidienne (exécution autonome). Contexte : **écart d'environ 19 jours** depuis le dernier run enregistré (snapshots au 01/08). La priorité absolue — vérification des codes des jeux chauds — a donc mobilisé l'essentiel du budget d'édition.

---

## a) Codes vérifiés

**Découverte majeure en cours de run (confirme l'anomalie du 01/08) :** le site sert les pages **`codes-<slug>.html`** (URLs plates, racine) ; les pages **`codes/<slug>.html`** sont **301-redirigées** (`.htaccess`). Les deux arbres avaient **divergé** — templates ET données différentes. Exemple : Blue Lock Rivals *servi* affichait encore **9 codes** « Semi-Finals », tandis que la copie `codes/` en affichait 6 « Quarter-Finals ». **Toutes les mises à jour de ce run ont été appliquées sur l'arbre SERVI** (et répliquées sur `codes/` pour cohérence).

### Jeux mis à jour (codes réellement modifiés)

Sourcing : ≥3 sources fiables (Pocket Tactics, Beebom, Pro Game Guides, GamesRadar, Twinfinite, Fossbytes…) croisées, et source officielle quand disponible (Trello / groupe Roblox).

| Jeu | Avant | Après | Détail |
|-----|------:|------:|--------|
| **Blue Lock Rivals** | 9 (servi) / 6 | **4 actifs** | MàJ *Sae Rework* : SAEREWORK, HALFBAKED, RINSOON, SAERRY4DELAY. Tous les anciens (Semi-Finals + Quarter-Finals) passés en expirés. Sources : Beebom (15/08), GamesRadar, Pro Game Guides. |
| **Volleyball Legends** | 6 (servi) / 3 | **3 actifs** | *Update 83* : UPDATE_83, MIKAGE_REVIVED, SCHOOL_SOON. Anciens (UPDATE_80, HIDARI_FINALLY, ENCHO_NERF, UPDATE_79, SEASON_17, FESTIVAL_UPD) expirés. Sources : Pocket Tactics (17/08), Beebom, Fossbytes, GamesRadar. |
| **Anime Vanguards** | 7 (servi) / 9 | **16 actifs** | Version 9.0 : ajout de 1DayDelay, 25thHour, LetTheLarpingBegin, LagGone, DMCAFree, Liberation, 223, Cog5th, LateBP (+ les 7 déjà valides). Source : Pocket Tactics (16/08) confirmée par Beebom/PGG. |
| **Anime Last Stand** | 26 (servi) / 26 | **38 actifs** | MàJ *Shibuya Pt.1* : +12 codes (ALSISBACK!, NEWLEVELS??, WeeklyReturn!, FORMYBROTHER!!!, Shibuya!, RRSFORDAYS!, WelcomeBack!, ALSREVERT, ALSWORLD2, ThankYouForBelieving!, ShhhThisIsASecret!, MORECOMINGSOON?). Source : Pro Game Guides (19/08, 38 actifs). Additif (aucun ancien expiré). |

Cartes du hub **`tous-les-codes.html`** resynchronisées (compteurs + date « Vérifié le ») pour ces 4 jeux.

### Jeux vérifiés — inchangés (date « Vérifié le » rafraîchie au 20/08, servi + `codes/`)

- **Blox Fruits** — 24 codes actifs, aucun nouveau code (EASTEREXP reste le plus récent). Confirmé PC Gamer / Beebom / Dexerto.
- **Blade Ball** — 14 codes actifs, inchangé. Confirmé Pocket Tactics / Beebom.
- **Grow a Garden** & **Grow a Garden 2** — « quiet », aucun code frais. Confirmé Beebom / PC Gamer.
- **Fisch** — jeu à forte rotation ; ensemble curatif de la page cohérent avec le pool actif suivi (33 codes valides suivis au 15/08). Date de vérification rafraîchie.

### Candidats « en attente » (prudence — non publiés)

- **Anime Vanguards** : Miniupdate1, 2BVisits, Prepare — cités par une seule source agrégée (postérieurs au snapshot Pocket Tactics), non corroborés → enregistrés en `pending` dans `code-watch.json`, **non publiés**.

### Jeux non revus ce run (à prioriser au prochain)

King Legacy, Fruit Battlegrounds, Steal a Brainrot, Sakura Stand, Grimoires Era, Dig, Anime Rangers X, Tower Defense Simulator, World Fighters, et le reste du catalogue (~160 pages). À traiter avec la réconciliation des deux arbres (voir plus bas).

---

## b) Directeur SEO

- **Trending re-scanné** (web, ≥3 sources) : leaders actuels — Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Anime Expeditions (~300K CCU), Murder Mystery 2 (~1M), +1 Speed Keyboard Escape (~500K CCU). **Tous couverts** au catalogue (Anime Expeditions et Murder Mystery 2 ont bien leurs pages `codes-…`, tier-list et guide). Aucun nouveau hit non couvert.
- **Aucune nouvelle brique de cluster créée ce run** — décision légitime : le rattrapage codes (19 j d'écart + 4 refontes complètes sur deux arbres divergents + découverte d'architecture) a consommé le budget, et la règle interdit d'empiéter sur la vérif codes.
- **Roadmap mise à jour** (`SEO-directeur-audit-roadmap-2026-07-24.md`) : entrée du 20/08 ajoutée. **Prochaine brique n°1 = brique technique : réconcilier les deux arbres `codes-<slug>.html` (servis) vs `codes/<slug>.html` (redirigés)** — enjeu d'honnêteté/SEO élevé (des pages servies non chaudes affichent encore des codes périmés). Puis : génériquiser le `FAQPage` JSON-LD ; guide GAG pets/œufs.

---

## c) Autres tâches

- **Jeux ajoutés** : aucun (aucun hit ≥4000 joueurs non couvert détecté).
- **Guides / tier lists** : aucune création (budget codes prioritaire).
- **UGC** : non revu ce run.
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-08-20 ; titre de l'événement Blue Lock Rivals « Prochaine MAJ (Tournoi mondial) » dé-périmé en « Prochaine mise à jour » (le Tournoi mondial est passé — codes WORLDTOURNAMENT expirés). Aucun compte à rebours ponctuel passé à retirer. JSON revalidé.
- **Jeu de la semaine** : non touché (jeudi ; réservé au lundi).
- **Fuseau US Eastern** : rappel — repasser les `hourUTC` de Steal a Brainrot à l'heure standard le **2 nov 2026** (pas encore).

---

## d) Fichiers touchés & QC

**Fichiers modifiés ce run (~22) :** pages servies `codes-{blue-lock-rivals, volleyball-legends, anime-vanguards, anime-last-stand, blox-fruits, blade-ball, grow-a-garden, grow-a-garden-2, fisch}.html` ; copies `codes/…` correspondantes ; `tous-les-codes.html` ; `data/events.json` ; `tools/code-watch.json` (snapshots + lastRun) ; `SEO-directeur-audit-roadmap-2026-07-24.md`.

**QC (Étape 8) — tout vert :**

- Scan d'intégrité sur **tous** les fichiers modifiés du working tree (348 au total, incluant le run J10 du 01/08 non encore commité) : **0 null byte**, tous finissent par `</html>`, **balises `<div>` équilibrées partout** (BAD: none).
- `node --check js/main.js` ✅ · `node --check js/events.js` ✅ · `data/events.json` JSON valide ✅ · `tools/code-watch.json` JSON valide ✅.
- **Cache JS** : `js/main.js` non modifié → pas de bump de version nécessaire.

**⚠️ À savoir pour le commit :** le dernier commit date du **31/07**. Le working tree contient donc **aussi les changements non commités du run du 01/08** (correctif JSON-LD breadcrumb/FAQ sur les 171 pages servies). Un `git add -A` les inclura, avec les modifications d'aujourd'hui — comportement normal du workflow, mais à noter (≈348 fichiers dans le commit).

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
