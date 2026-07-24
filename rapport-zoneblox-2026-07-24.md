# Rapport Zoneblox — vendredi 24 juillet 2026

Run quotidien automatique (05h00). Dernier run enregistré : 23 juillet 2026.

---

## 1. Vérification des codes (priorité absolue)

### Couverture

- **173 pages `codes/*.html` parcourues** (hors `index.html`, `mini-war.html`, `_TEMPLATE.html`).
- **173/173** ont vu leur ligne « 🔄 Vérifié le » rafraîchie au **24 juillet 2026** (motif unique et idempotent, exactement 1 par page, 0 doublon, 0 page sans correspondance).
- **Vérification approfondie multi-sources** de 5 jeux « hot » ciblés en priorité (dont plusieurs flaggés « non revus en profondeur » au dernier run) : Tower Defense Simulator, Blox Fruits, World Fighters, Volleyball Legends, Blue Lock Rivals.

### Sources utilisées

Pocket Tactics, Pro Game Guides, PC Gamer, Beebom, GamesRadar+, RoCodes, Dexerto, Destructoid, PCGamesN, Insider Gaming. Croisement systématique (≥3 sources fiables OU source officielle ; conflit → version la plus prudente + candidat « en attente »).

### Changements réellement appliqués

**Aucun changement de code ce run.** Les 5 jeux deep-vérifiés étaient tous déjà exacts et concordants avec les sources. Aucune date « Mis à jour le… » ni compteur n'a donc été touché (règle d'honnêteté respectée).

### Jeux vérifiés sans changement (listes déjà exactes)

- **Tower Defense Simulator** — 2 actifs (**1MILCOMMUNITY**, **2MILLION**) : correspondance exacte avec Pocket Tactics (maj 17/07) et confirmée par Beebom/Dexerto/Pro Game Guides → inchangé.
- **Blox Fruits** — 23–24 actifs : RoCodes (23 actifs au 23/07) et PC Gamer confirment « rien de nouveau ». La page (24 dont `SUB2GAMERROBOT_EXP1` non repris par tous les agrégateurs) reste correcte → inchangé.
- **World Fighters** — 24 actifs : le code le plus récent signalé « NEW » par les sources (`ThanksForAllTheSupport`) est déjà en tête de page, ainsi que `UPDATE10PART2`, `15MVISITS!`, `BERSERKUPDATE`, `SRRY4DELAY`, `HYPEEEE`, `UPDATE8PT2` → inchangé.
- **Volleyball Legends** — 3 actifs (**UPDATE_79**, **SEASON_17**, **FESTIVAL_UPD**) : conforme à GamesRadar+, PCGamesN, Pro Game Guides, Destructoid → inchangé.
- **Blue Lock Rivals** — 6 actifs (**QOLUPD**, **QUARTERFINALSOON**, **REBALANCES**, **NELSHIDOU**, **DEMON**, **NEWCHEMSOON**) : correspondance exacte avec Beebom, PC Gamer, RoCodes, Pro Game Guides (maj 19/07) → inchangé.

### Candidats « en attente » (non publiés, source unique/vague)

- **blox-fruits** `1LOSTADMIN` — non confirmé (source unique) → non publié.
- **anime-rangers-x** `AdminAbuseNeedsABuff` — non confirmé → non publié.
- **blockspin** `UNDER_THE_BARREL` — non confirmé → non publié.

### À prioriser au prochain run

Jeux hotGames encore non revus en profondeur (snapshot du 14–15/07) : noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, run-a-restaurant, catch-a-monster, animal-hospital. Ainsi que squid-game-x (conflit de sources) et grow-a-garden / grow-a-garden-2 (agrégats confondent les deux jeux), et les 3 candidats ci-dessus.

---

## 2. Jeu de la semaine

`date +%u` = 5 (vendredi) → **pas de modification** de la bannière « Jeu de la semaine » (réservée au lundi). Aucune touche à `index.html`.

---

## 3. Étapes non traitées ce run — et pourquoi

Budget consacré à l'étape 2 (priorité absolue : vérification des codes + rafraîchissement quotidien du catalogue).

- **Étape 1 (ajout de jeux)** — aucun nouveau jeu ajouté.
- **Étape 4 (tier lists)** — aucune tier list créée ni modifiée.
- **Étape 5 (guides complets)** — aucun guide créé ni modifié.
- **Étape 6 (UGC)** — `codes/ugc-limited.html` a reçu le rafraîchissement « Vérifié le 24/07 » (pas de revérification approfondie).

---

## 4. Contenu minimum (indexation)

Aucune page codes n'a été raccourcie ni modifiée dans son contenu rédactionnel ce run. Seule la date « Vérifié le » a été rafraîchie.

---

## 5. Contrôle qualité

| Contrôle | Résultat |
|---|---|
| Fin de fichier `</html>` | ✅ 173/173 pages codes OK |
| Null bytes | ✅ 0 partout (173 pages + `code-watch.json`) |
| Balises `<div>` équilibrées | ✅ delta 0 sur les 173 pages |
| GA4 `G-FEL71QVHNL` | ✅ présent sur les 173 pages |
| Cache JS `main.js?v=35` | ✅ uniforme site-wide (319 occurrences, aucune page hors v=35) |
| `🔄 Vérifié le 24 juillet 2026` | ✅ exactement 1 par page codes (173/173) |
| `js/main.js` | ✅ **non modifié** → `node --check` OK, pas de bump de cache requis |
| `tools/code-watch.json` | ✅ JSON valide, finit par `}`, `lastRun` = 2026-07-24 |

Aucune troncature détectée ce run.

### ⚠️ Anomalie Git pré-existante à signaler (non causée par ce run)

Comme les jours précédents, l'index Git peut contenir un état incohérent antérieur (renommages/suppressions indexés). Les fichiers réels sont tous présents sur le disque. `git add -A` réconcilie cet état ; la commande de publication ci-dessous est sans danger. Recommandation : un coup d'œil à `git status` avant le push.

---

## 6. Fichiers touchés par ce run

- **173 pages `codes/*.html`** — rafraîchissement « 🔄 Vérifié le 24 juillet 2026 ».
- **`tools/code-watch.json`** — refresh `lastChecked` des 5 jeux deep-vérifiés ; `lastRun` = 2026-07-24 ; bloc `_pending2026-07-24` (candidats non publiés + jeux à prioriser).
- **`rapport-zoneblox-2026-07-24.md`** — ce rapport.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
