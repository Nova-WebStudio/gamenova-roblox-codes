# Rapport Zoneblox — 12 septembre 2026 (samedi)

## ⚠️ Environnement dégradé : sandbox bash indisponible

Le sandbox Linux ne parvient toujours pas à monter le dossier (échec du partage Plan9, conséquence du bug de la mise à jour Windows du 8 septembre — déjà constaté au run du 10/09). **Conséquences :**

- `build_codes_json.py`, `build_sitemap.py`, `sync_month.py`, `node --check` et toutes les commandes `git` **n'ont pas pu être exécutés**.
- Les outils de fichiers (Read/Write/Edit) fonctionnent normalement. **Toutes les éditions ont été faites avec l'outil Edit** (remplacement de chaîne exact) → pas de `sed`, donc **aucun risque de troncature ni de null byte** (c'est précisément le mode d'édition recommandé par `CLAUDE.md`).
- **Aucun code n'a été modifié ce run** → `data/codes.json` n'est pas impacté par un changement de codes. En revanche, des dates « 🔄 Vérifié le » ont été rafraîchies, donc les `<lastmod>` du `sitemap.xml` devront être régénérés (voir « Pour publier »).

La priorité du run (vérification des codes) a été traitée intégralement. Les étapes annexes (ajout de jeux, Directeur SEO, guides, tier lists, UGC) ont été **volontairement reportées** : sans build scripts ni QC automatisé, créer de nouvelles pages (sitemap / codes.json / miniatures / équilibre des div non vérifiables) serait risqué et incomplet.

---

## (a) Codes vérifiés

### hotGames — tous stables, AUCUN changement de codes
Vérifiés via ≥3 sources web datées septembre 2026 (GamesRadar, Pocket Gamer, PCGamer, Beebom, PGG, Pocket Tactics, Destructoid, PCGamesN) :

| Jeu | Actifs | Statut |
|-----|--------|--------|
| volleyball-legends | 3 (UPDATE_86 / HAKKA_RETURN / SPIKER) | Stable. UPDATE_85/SHIRO/BLOCKED toujours en conflit → non ajoutés. |
| blue-lock-rivals | 4 (NELKING / NIKOSOON / UBERSMONTH / SORRYLOADING) | = PCGamer 11 sept. Stable. |
| anime-vanguards | 3 (Retribution / Wrath / MiniUpd2) | Stable (Retribution expire le 14 sept, encore actif aujourd'hui). |
| fruit-battlegrounds | 2 | Sous-listage OK (agrégats mélangés actifs/anciens). |
| fisch | 3 (scarlet / TemporarySubmarine / CARBON) | SkycrestIsInTheSky toujours expiré ; HarpoonGunsNextWeek / OllieAndFinWhale = source unique → non ajoutés. |
| blade-ball | 13 | Pas de nouveau code depuis semaines ; sous-listage OK. |
| anime-last-stand | 22 | Liste active = sur-ensemble de la liste source ; aucune expiration. |
| blox-fruits | 24 | EASTEREXP/SUB2GAMERROBOT_EXP1 actifs ; KITT_RESET/LIGHTNINGABUSE/1LOSTADMIN non confirmés ≥3 → non ajoutés. |
| grow-a-garden | 2 (RDCAward / BEANORLEAVE10) | FREESEED ambigu GaG/GaG2 + source unique → non ajouté. |
| steal-a-brainrot | 1 | Conflit persistant 1-vs-plusieurs → inchangé par prudence. |

→ **« 🔄 Vérifié le »** rafraîchi au 12 sept sur ces 10 pages.

### Rotation ÉTAPE 2ter — lot du jour (priorité aux pages jamais vérifiées en profondeur)

**8 jeux confirmés OK** (source datée sept. comparée à notre page ; « Vérifié le » → 12 sept + `catalogVerify` MAJ) :

- **project-slayers** — 0 actif : honnête (consensus « no working codes » ; source isolée « 6 working » écartée).
- **ro-ghoul** — 5 : sous-listage de ~18 trackés (codes Ro-Ghoul long-lived, aucune expiration prouvée).
- **dead-rails** — 0 : le jeu n'a **aucun système de codes** (confirmé multi-sources).
- **combat-warriors** — 0 : codes rares/expirent en quelques jours, aucun actif surfacé.
- **forsaken** — 0 : **aucun système de codes** (Alpha).
- **the-strongest-battlegrounds** — 0 : les « codes » sont des **Sound IDs payants**, pas des codes-récompense.
- **sols-rng** — 8 : sous-listage de ~14 (codes tickets/potions long-lived).
- **bedwars** — 0 : **aucun système de rédemption**.

**6 jeux laissés « à revérifier » (pages NON modifiées, prudence) :**

- **sonic-speed-simulator** — conflit 0 (PT/Beebom 2 sept) vs 5 (Roblox Den 5 sept) + confusion version « RE-RAN ».
- **mad-city** — conflit 0 (Pocket Gamer 7 sept) vs 6 (Roblox Den) ; notre page = 6 (codes Mad City historiquement permanents).
- **fire-force-online** — collision de nom Fire Force Online vs Fire Force Reignition + données contradictoires (LONGAWAITEDUPDATE listé actif ET retiré le 2 sept).
- **anime-reborn** — **sous-listé** : notre page à 0 alors que les sources confirment ~10 actifs (domainexpansion! / PATCH / Podcastgang!!…). Jeu à rotation rapide → à compléter proprement (≥3 sources/code + regen codes.json) quand bash revient.
- **jujutsu-infinite** — **sous-listé** : page à 0 ; HELLO_JJI / 400K_SUBS confirmés ≥3 sources mais codes très volatils (durée ~jours) → à compléter avec regen codes.json.
- **dig** — collision de nom : résultats contaminés par « Dig and Clean » (jeu différent). Liste DIG propre non isolée.

Aucun code ajouté/expiré ce run. Aucun candidat « en attente » nouveau (ceux des runs précédents restent consignés dans `tools/code-watch.json`).

## (b) Directeur SEO
Reporté (environnement dégradé, pas de build scripts/QC). Aucune brique de cluster ce run. La roadmap `SEO-directeur-audit-roadmap-2026-07-24.md` n'a pas été modifiée.

## (c) Jeux ajoutés / guides / tier lists / UGC / jeu de la semaine
- Aucun ajout (reporté, cf. ci-dessus).
- Jeu de la semaine : non concerné (mise à jour le lundi uniquement ; aujourd'hui = samedi).

## (d) Fichiers touchés + QC

**Pages codes — date « 🔄 Vérifié le » → 12 septembre 2026 (18 fichiers) :**
codes-blox-fruits, codes-blade-ball, codes-blue-lock-rivals, codes-anime-vanguards, codes-fisch, codes-volleyball-legends, codes-fruit-battlegrounds, codes-grow-a-garden, codes-steal-a-brainrot, codes-anime-last-stand, codes-project-slayers, codes-ro-ghoul, codes-dead-rails, codes-combat-warriors, codes-forsaken, codes-the-strongest-battlegrounds, codes-sols-rng, codes-bedwars.

**Suivi :** `tools/code-watch.json` — ajout de 8 entrées `catalogVerify` (12 sept) + bloc `_pending2026-09-12` (hotGames stables, rotation OK, 6 « à revérifier »).

**QC réalisable (sans bash) :**
- Éditions via l'outil Edit uniquement → remplacement exact, **pas de null byte, pas de troncature** possibles.
- `code-watch.json` : structure JSON revérifiée manuellement (accolades/virgules/guillemets internes en apostrophes) — valide, se termine par `}`.
- Chaque édition de page n'a touché que la valeur de `id="verifDate"` (chaîne unique par page) — aucune autre partie du HTML modifiée.

**QC NON réalisable ce run (bash requis) :** `python3 -c json.load(codes.json)`, `node --check js/main.js`, scan équilibre des `<div>`, scan null bytes global, `git diff`. À relancer au prochain run avec bash.

---

## Pour publier
Dans le dossier GameNova, lance (quand le sandbox/bash sera rétabli, ou directement sur ta machine) :

```
python3 tools/build_sitemap.py
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

`build_sitemap.py` rafraîchira les `<lastmod>` à partir des dates « 🔄 Vérifié le » mises à jour aujourd'hui. (`build_codes_json.py` n'est pas nécessaire ce run : aucun code n'a changé.) Hostinger déploie automatiquement après le push.
