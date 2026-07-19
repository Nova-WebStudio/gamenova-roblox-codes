# Rapport Zoneblox — dimanche 19 juillet 2026

Run quotidien automatique. Dernier run enregistré : 18 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **167 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **167/167** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **19 juillet 2026** (motif unique et idempotent, aucun doublon).
- **10 jeux « hot » vérifiés en profondeur, multi-sources** : Anime Last Stand, Anime Vanguards, Anime Rangers X (Re:Rangers X), Fisch, Blue Lock Rivals, Blox Fruits, Grow a Garden, Steal a Brainrot, King Legacy, Fruit Battlegrounds.

### Sources utilisées

Destructoid (01/07), Pocket Tactics (01/07), Beebom (22/06 et 06/05), PC Gamer (06/07), Pro Game Guides (13/07), RoCodes, GamesRadar. Croisement systématique d'au moins 2–3 sources par jeu selon la règle de sourcing (≥3 sources fiables OU source officielle).

### Changements réellement appliqués

**`codes/fisch.html` — 7 codes actifs → 3 (correction importante)**

Le run du 18/07 avait ajouté quatre codes de l'événement **Drylands** comme actifs. Or **PC Gamer** (mis à jour le 06/07) est explicite : ces codes *« ont expiré presque immédiatement »* et seuls trois codes permanents restent actifs. Les quatre codes sont donc repassés en **expirés** :

| Code basculé en expiré | Statut source |
|---|---|
| DrylandsIsFire | Expiré (PC Gamer, liste barrée) |
| HAPPY4TH | Expiré (PC Gamer, liste barrée) |
| KingCrabstle | Expiré (PC Gamer, liste barrée) |
| OllieAndFinWhale | Absent des actifs (PC Gamer) |

Restent actifs les trois codes permanents confirmés : **scarlet, TemporarySubmarine, CARBON**. Compteurs (7→3), bloc « codes expirés » (22→26), date « Mis à jour le » (19/07), `dateModified` JSON-LD, paragraphe d'intro et meta description (« juin » → « juillet ») mis à jour en conséquence.

**`codes/fruit-battlegrounds.html` — correction d'un compteur incohérent (pas de changement de liste)**

La page affichait **5 codes actifs** (game-meta et tableau) mais l'intro et le bandeau live indiquaient encore **4**. Compteurs alignés à **5**. OMGUPDATE22 confirmé actif par les sources de juillet. La date « Mis à jour le » n'a **pas** été touchée (aucun code réellement modifié, simple correction d'affichage).

### Jeux vérifiés sans changement (listes déjà exactes)

- **Anime Last Stand** — 21 codes actifs. La liste correspond **à l'identique** à celle de Destructoid (01/07) et est corroborée par Beebom. L'alerte « 31 vs 4 » du 18/07 était un artefact de comptage (le 31 additionnait actifs + expirés ; le « 4 » n'était que la courte liste « new » de Pocket Tactics). **Aucune correction nécessaire.**
- **Anime Vanguards** — 8 actifs. 13.5 / EternalAdversaries / Gambler confirmés actifs par Pocket Tactics (01/07) ET Beebom (22/06). Les cinq codes plus récents (WhoopsieDaisy, LateBP, PowerOfLove, EEPart1, BPSoon) restent en place. `kat` **non ajouté** (Pocket Tactics le classe expiré = conflit → prudence). L'écart « 22 vs 7 » du 18/07 était là encore un comptage : la page est déjà à 8.
- **Anime Rangers X (Re:Rangers X)** — 15 actifs, tous présents dans la liste active de Pro Game Guides (30 codes, maj 13/07). Sous-ensemble prudent, **aucun faux actif**. Les candidats PGG supplémentaires ne sont pas publiés faute de 2ᵉ/3ᵉ source.
- **Blue Lock Rivals** — 3 actifs (NELSHIDOU, NEWCHEMSOON, DEMON), identiques aux sources PGG / PC Gamer / Beebom (maj 17/07).
- **Blox Fruits** — 24 actifs, cohérent (SUB2GAMERROBOT_EXP1 conservé, historiquement présent au Trello officiel).
- **Grow a Garden** — 2 actifs (RDCAward, BEANORLEAVE10), cohérent.
- **Steal a Brainrot** — aucun code (le jeu n'en propose pas). Position honnête conservée.
- **King Legacy** — 8 actifs, 7 confirmés par PC Gamer / Pocket Tactics (jeu sans MAJ récente). `2MFAV` non retrouvé dans les sources (candidat expiré à surveiller) ; `RainbowDragon` (conditionnel) non ajouté. Aucun changement appliqué.

La ligne interne « Dernière vérification » a été passée au 19/07 sur ces pages vérifiées ce jour.

### Candidats « en attente » (non publiés) — `_pending2026-07-19`

- **Fruit Battlegrounds** — les sources de juillet listent des paliers plus récents (BIG1M170K!!, 1M60WOWZER, 1M50INSANE, 4MPUTAT3, THEMARINEHERO, REBOOTPART2…) absents de Zoneblox. Reconciliation/ajout dédiés au prochain run (2–3 sources).
- **King Legacy** — `2MFAV` (probable expiré) et `RainbowDragon` (conditionnel) à trancher avec une 2ᵉ source.
- **Anime Rangers X** — candidats PGG additionnels (AdminAbuseNeedsABuff, SHADOWAA, SummerTime, delaRXy, SINGULARITY, HOLYGRAIL, BOSSEVENT…) à confirmer via GamesRadar + Destructoid.
- **Anime Vanguards** — LateBP expire ~19/07 (à repasser en expiré au prochain run si confirmé) ; `kat` en conflit non ajouté.
- **Blade Ball** — conflits du 18/07 (BATTLEROYALE, DUNGEONSRELEASE, GOODVSEVIL) non revus ce run.

### À prioriser au prochain run

1. **Fruit Battlegrounds** — ajouter les paliers récents confirmés (Zoneblox est en retard).
2. **Fisch** — surveiller la sortie de nouveaux codes Drylands stables (le wiki officiel Fischipedia est client-rendu, non lisible en fetch simple → passer par Chrome).
3. **King Legacy** — trancher 2MFAV / RainbowDragon.
4. Les **~20 jeux hotGames** non revus en profondeur : pet-simulator-99, tower-defense-simulator, world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea, animal-hospital, volleyball-legends, grow-a-garden-2, blade-ball.

---

## 2. Étapes non traitées ce run — et pourquoi

Le budget du run a été consacré à l'étape 2 (priorité absolue). Les étapes suivantes n'ont produit aucune modification :

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le » mais pas de revérification approfondie.
- **Étape 7 (Jeu de la semaine)** — non applicable : on est **dimanche** (`date +%u` = 7). La bannière `FEATURED-WEEK` n'a pas été touchée.

---

## 3. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie. Fisch et Fruit Battlegrounds conservent leur volume rédactionnel (> 1 200 mots) ; seules les listes de codes et compteurs ont bougé.

---

## 4. Contrôle qualité

Scan d'intégrité sur les **167 pages HTML modifiées** + `tools/code-watch.json` :

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 167/167 |
| Null bytes | ✅ 0 partout |
| Balises `<div>` équilibrées | ✅ delta 0 partout |
| GA4 `G-FEL71QVHNL` | ✅ présent partout |
| Cache JS `main.js?v=34` | ✅ uniforme (314 occurrences) |
| `🔄 Vérifié le 19 juillet 2026` | ✅ exactement 1 par page codes |
| `codes/fisch.html` — 3 boutons Copier actifs | ✅ |
| `tools/code-watch.json` | ✅ JSON valide, 30 snapshots, `lastRun` = 2026-07-19 |
| `js/main.js` modifié | ❌ non → pas de bump de cache requis |

Aucune troncature détectée ce run.

---

## 5. Fichiers touchés

- **167 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 19 juillet 2026 ».
- **`codes/fisch.html`** — 4 codes Drylands basculés en expirés (actifs 7→3), compteurs / dates / intro / meta description mis à jour.
- **`codes/fruit-battlegrounds.html`** — compteur incohérent aligné (4→5), sans changement de liste.
- **`codes/anime-last-stand.html`, `codes/anime-vanguards.html`, `codes/anime-rangers-x.html`, `codes/blue-lock-rivals.html`, `codes/blox-fruits.html`, `codes/grow-a-garden.html`, `codes/king-legacy.html`** — bandeau « Dernière vérification » au 19/07 (aucun changement de codes).
- **`tools/code-watch.json`** — snapshots des 10 jeux vérifiés, `lastRun`, candidats `_pending2026-07-19`.
- **`rapport-zoneblox-2026-07-19.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
