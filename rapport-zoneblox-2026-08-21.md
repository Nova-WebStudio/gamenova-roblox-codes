# Rapport Zoneblox — 21 août 2026 (vendredi)

## (a) Vérification des codes

**Jeux chauds re-vérifiés (web, ≥3 sources fiables) :**

| Jeu | Statut | Résultat |
|-----|--------|----------|
| Blox Fruits | Stable | 21+ codes actifs, aucun nouveau code en août (PCGamesN, PC Gamer, Beebom, The Click). Inchangé. |
| Blue Lock Rivals | Stable | 4 actifs : SAEREWORK, HALFBAKED, RINSOON, SAERRY4DELAY (PGG, PC Gamer, Beebom, Pocket Gamer, Twinfinite). Conforme au snapshot 20/08. |
| Volleyball Legends | Stable | 3 actifs : UPDATE_83, MIKAGE_REVIVED, SCHOOL_SOON (GamesRadar, Roonby, PGG, Beebom). Conforme au 20/08. |
| Anime Vanguards | En conflit → prudence | Page à 16 codes ; agrégateurs marquent Miniupdate1/2BVisits/Prepare comme nouveaux (absents de la page) mais listent un ensemble plus court. **Inchangé ce run**, laissé en attente. |
| **Steal a Brainrot** | **Modifié (0 → 1)** | Ajout de **`BESTBRAINROTEVER`** (spawn du brainrot secret La Vacca Saturno Saturnita), confirmé actif par ≥5 sources (GamesRadar, Beebom, PCGamesN, Dexerto, RoCodes, RBLXGUIDE). La page servie affichait à tort 0 code. |

**Code ajouté ce run :** Steal a Brainrot → BESTBRAINROTEVER (page servie `codes-steal-a-brainrot.html` : compteur 0→1, mois du titre/H1/og juillet→août, code ajouté à la liste active ; carte du hub `tous-les-codes.html` : statut « Pas de codes » → « 1 code actif », date → 21 août 2026 ; snapshot `tools/code-watch.json` mis à jour).

**Aucun code retiré.** Aucun code inventé. Règle de sourcing respectée (≥3 sources fiables ou source officielle ; conflit → version la plus prudente + « en attente »).

**« Vérifié le » rafraîchi au 21 août 2026 sur les 171 pages codes SERVIES** (`codes-*.html`), idempotent (1 seule ligne `#verifDate` par page). 162 étaient bloquées au 1er août, 9 au 20 août → toutes au 21 août désormais.

**Candidats « en attente » (à prioriser au prochain run) :**
- **Anime Vanguards** : réconcilier l'ensemble actif (ajouter Miniupdate1 / 2BVisits / Prepare après confirmation des récompenses ; vérifier expiration des anciens codes de la page).
- Jeux chauds non re-vérifiés web ce run (couverts par le rafraîchissement de date mais pas par une re-vérification source-à-source aujourd'hui) : Fisch, Grow a Garden, Grow a Garden 2, Blade Ball, Anime Last Stand, King Legacy, Fruit Battlegrounds, Pet Simulator 99, + tout le long tail du catalogue.

> ⚠️ **Note ÉTAPE 0** : la surveillance des sources officielles a été faite via les agrégateurs web (WebSearch). L'appel direct aux API Roblox (universeId, description in-game, shout de groupe, Trello/X) n'a pas été possible : le shell n'a pas de réseau et le navigateur Chrome n'est pas connecté dans ce run automatisé non-interactif. Les vérifications web ≥3 sources couvrent l'essentiel du besoin sur les jeux chauds.

## (b) Directeur SEO

**Trending re-scanné (web) :** Grow a Garden, Steal a Brainrot, Brookhaven en tête — tous couverts. Anime Expeditions déjà fiché. À surveiller : Anime Origins & Wonderland (sorties août), +1 Speed Keyboard Escape (~500K, obby, probablement sans codes). **Aucun nouveau hit non couvert** → pas de création de fiche prioritaire (et l'API miniatures Roblox n'était de toute façon pas accessible ce run).

**Brique de cluster réalisée : alignement du `FAQPage` JSON-LD sur la FAQ visible (171 pages codes servies).**
- **Problème corrigé** : depuis le J10, le JSON-LD portait le bon nom de jeu mais 3 questions génériques ne correspondaient pas à la FAQ affichée (ex. Blox Fruits : JSON-LD « …codes sont-ils *ajoutés* ? » vs visible « …*vérifiés* ? » ; réponse Q1 « menu Paramètres » vs visible « zone dédiée aux codes ») → non-conformité Google FAQ (le balisage doit refléter le contenu visible).
- **Correction** (script Python validé) : extraction des paires question/réponse visibles, nettoyage des balises + décodage des entités, reconstruction du `mainEntity` du bloc `FAQPage` à l'identique du visible, sur les 171 pages.
- **Intention ciblée** : renforcer la couverture SERP (FAQ rich results) des pages transactionnelles « codes <jeu> ». **Anti-cannibalisation** : aucune nouvelle page, aucun nouveau mot-clé ciblé → nulle.
- **Prochaine brique inscrite dans la roadmap (J13)** : (1) réconcilier les deux arbres codes (ne garder que l'arbre servi) ; (2) réconcilier Anime Vanguards ; (3) surveiller Anime Origins / Wonderland.

## (c) Autres maintenances

- **Jeux ajoutés** : aucun (pas d'accès fiable à l'API miniatures Roblox ; règle absolue « jamais de SVG en miniature affichée »).
- **Guides / tier lists** : aucune création/MAJ ce run (budget concentré sur codes + brique FAQ).
- **UGC** : non modifié.
- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-08-21. Aucun horaire ponctuel passé à retirer (tous les évènements sont récurrents/restocks) ; aucun nouvel horaire confirmé à promouvoir. `node --check js/events.js` OK.
- **Jeu de la semaine** : non touché (on est vendredi, MAJ réservée au lundi).

## (d) Fichiers touchés + QC

**Modifiés par ce run :**
- 171 × `codes-*.html` (servies) — `#verifDate` → 21 août 2026 + `FAQPage` JSON-LD aligné sur la FAQ visible.
- `codes-steal-a-brainrot.html` — ajout du code BESTBRAINROTEVER (+ titre/H1/og/mois + compteur).
- `tous-les-codes.html` — carte Steal a Brainrot resynchronisée (statut + date).
- `data/events.json` — `meta.updated`.
- `tools/code-watch.json` — snapshot Steal a Brainrot + hot games + `_pending2026-08-21` + `lastRun`.
- `SEO-directeur-audit-roadmap-2026-07-24.md` — brique du jour + brique J13.

**QC (tout vert) :**
- Tous les blocs `ld+json` re-parsés (`json.loads`) OK sur les 171 pages (FAQPage + BreadcrumbList).
- 0 null byte ; toutes les pages finissent par `</html>`.
- Équilibre des balises `<div>` intact (0 déséquilibre).
- `node --check js/main.js` et `node --check js/events.js` OK ; `data/events.json` et `tools/code-watch.json` valides.
- Version cache uniforme `main.js?v=36` (js/main.js non modifié → pas de bump).

> ℹ️ **À savoir avant de committer** : le dernier commit du dépôt date du **31 juillet**. Le répertoire de travail contient donc AUSSI les modifications non committées du run du **20 août** (l'arbre redირigé `codes/*.html` + les 4 jeux chauds), en plus des modifications d'aujourd'hui. Le commit ci-dessous les regroupera toutes. C'est sans risque, mais explique le nombre élevé de fichiers dans `git status`.

---

**Pour publier :** dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.
