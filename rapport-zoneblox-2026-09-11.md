# Rapport Zoneblox — run du 2026-09-11 (vendredi)

## ⛔ BLOCAGE INFRASTRUCTURE — run partiel (vérification codes en lecture seule uniquement)

**Le bac à sable Linux (shell bash) n'a pas démarré de tout le run.** Erreur identique sur 4 tentatives :

```
failed to mount ... /outputs as outputs: source path ... is under Plan9 share "c" which is not mounted
```

Conséquence : **aucun outil Python / git / Node n'était disponible**. Or l'ensemble des étapes d'écriture de la tâche dépendent d'eux et sont **des garde-fous bloquants** :

- `python3 tools/build_codes_json.py` — **régénération obligatoire de `data/codes.json`** dès qu'un code change (sinon le widget partenaire sert des codes périmés) → **impossible**.
- `node --check js/main.js`, validation JSON, scan null-bytes, contrôle d'équilibre des `<div>`, scan d'intégrité `git diff` avant commit → **impossibles**.
- Restauration de secours `git show HEAD:<fichier>` en cas de troncature → **impossible**.

Le `CLAUDE.md` du projet documente en détail que ces pages HTML (~50 Ko, 178 pages codes) sont **fragiles à l'écriture** (troncatures, null bytes, `</div>` déséquilibrés déjà survenus et ayant cassé le site en production). **Éditer ces fichiers sans pouvoir exécuter la QC ni régénérer `data/codes.json` reviendrait à prendre exactement le risque que tout le workflow cherche à éviter.**

**Décision (run autonome, utilisateur absent) :** je n'ai fait **AUCUNE écriture sur le site** (ni pages codes, ni `js/main.js`, ni `codes.json`, ni dates « Vérifié le »). J'ai réalisé la partie **sans risque et à plus forte valeur** — la vérification des codes en lecture seule via le web — et je livre ce rapport. **Aucun commit à faire pour ce run.**

> ➡️ **Action recommandée : relancer la tâche quotidienne une fois le bac à sable Linux rétabli.** Les findings ci-dessous donneront une longueur d'avance (candidats déjà identifiés et sourcés).

---

## ✅ Ce qui a été fait (lecture seule) : vérification des hotGames volatils

Vérification web des jeux hotGames dont les codes tournent vite (cibles des faux-actifs), comparée aux snapshots de `code-watch.json` (datés 02–03/09). **Rien n'a été publié** — les changements ci-dessous sont à appliquer au prochain run, après recoupement ≥3 sources conformément à la règle de sourcing.

### Stables — aucun changement détecté (nos pages restent correctes)

| Jeu | Set servi | Vérification 11/09 |
|-----|-----------|---------------------|
| **blade-ball** | ~13–14 codes (wheel spins) | 14 actifs, « aucun nouveau code depuis un moment » — **cohérent, inchangé**. |
| **anime-vanguards** | Retribution, Wrath, MiniUpd2 | 3 actifs identiques (expirent le 14/09) — **cohérent, inchangé**. |
| **grow-a-garden** | RDCAward, BEANORLEAVE10 | Exactement ces 2 codes ; *torigate* et LUNARGLOW10 confirmés **expirés** (bien exclus chez nous) — **cohérent**. |
| **blox-fruits** | 24 actifs (EASTEREXP, SUB2GAMERROBOT_EXP1, BIGNEWS…) | Set servi confirmé actif — **inchangé** (voir candidats ci-dessous). |
| **fruit-battlegrounds** | HIGHER1M120K, YOO1M110K!, BIGMILLIHUNNID!, ITSTHEBILLION!, CODEFIX | Set servi confirmé actif — **inchangé** (voir candidat ci-dessous). |

### ⚠️ Rotations probables à trancher — PRIORITÉ MAX du prochain run

- **blue-lock-rivals** — PC Gamer (10/09) ne liste plus que **4 codes actifs : NELKING, NIKOSOON, UBERSMONTH, SORRYLOADING** — un set **entièrement différent** de notre page (UBERSTAKEOVER / KINGNEXTWEEK / EGODEFENSE + 6 anciens, snapshot 03/09). Forte présomption que **notre page affiche des codes désormais expirés**. ⚠️ **1 seule source consultée** → recouper ≥3 sources (PGG, Beebom, RoCodes) avant de basculer les anciens en expirés et publier le nouveau set. **À traiter en premier.**

- **volleyball-legends** — GamesRadar (09/2026) liste **UPDATE_86, HAKKA_RETURN, SPIKER, UPDATE_85, SHIRO, BLOCKED**. Notre set (UPDATE_84 / SEASON_18 / PIRATE_SZN, snapshot 02/09) semble avoir **rotationné** (Update 85→86). Présomption que nos 3 codes sont périmés. ⚠️ **1 source** → recouper ≥3 (Beebom, PGG, RoCodes, Twinfinite) avant édition. **Priorité haute.**

### 🟡 Candidats confirmés / à confirmer (ajouts potentiels, non publiés)

- **anime-last-stand** — **3 nouveaux codes confirmés par ≥3 sources** (PGG, Beebom, Roblox Den, The Click, allthings.how ; ajoutés le 01/09) : **MagicKnights!** (35 Rerolls, 25 Perfect Stat Cubes, 50 Stat Cubes), **ElfReincarnation!** (25 Rerolls, 10 Mythic Shards, 100 Essence Selectors), **IsItReallyWeekly?!** (50 Rerolls, 5 000 Jewels). Étaient déjà « pending » dans notre snapshot → **publiables dès que l'écriture est possible** (édition d'une longue liste : prudence, remplacement littéral du compteur du hero).

- **fruit-battlegrounds** — nouveau candidat **MILLI90SWAG** (600 Gems) vu chez Twinfinite/Beebom. À confirmer ≥3 sources. Jeu à grande liste longue durée : pas d'urgence d'expiration.

- **blox-fruits** — candidats **LIGHTNINGABUSE**, **1LOSTADMIN**, **KITT_RESET** cités comme récents (Beebom/PCGamesN). *1LOSTADMIN* traînait déjà en attente (note 22/07). À confirmer ≥3 sources avant ajout ; set actuel inchangé entre-temps.

---

## ❌ Étapes NON exécutées (bloquées par l'absence de sandbox)

- **ÉTAPE 0** — mise à jour des snapshots `code-watch.json` (écriture + validation JSON impossibles).
- **ÉTAPE 2 / 2ter** — aucune édition de page codes, aucune date « 🔄 Vérifié le » rafraîchie, **aucun lot de rotation de 15–20 jeux traité** (édition + QC bloquées). Le tracking `catalogVerify` n'a donc pas avancé.
- **ÉTAPE 2bis (Directeur SEO)** — aucune brique de cluster (nécessite écriture + QC + éventuel bump cache).
- **ÉTAPES 1, 3, 4, 5, 6** — ajout de jeux, guides, tier lists, UGC : non exécutés.
- **ÉTAPE 7** — sans objet (vendredi, pas lundi).
- **ÉTAPE 8/9 (QC + cache JS)** — non exécutables.
- **`data/codes.json`** — **non régénéré** (aucun code n'ayant été modifié, il n'est de toute façon pas devenu plus périmé qu'avant ce run).

---

## Fichiers touchés

- **Aucun fichier du site modifié.** Seul ce rapport a été créé : `rapport-zoneblox-2026-09-11.md`.

## QC

- Sans objet : aucune écriture sur le site. Aucun risque de troncature/null-byte introduit ce run.

---

## Pour publier

**Rien à publier pour ce run** (aucune modification du site). Dès que le bac à sable Linux est rétabli, **relancer la tâche** : elle appliquera les vérifications ci-dessus (rotations blue-lock-rivals & volleyball-legends à trancher en priorité, ajouts anime-last-stand confirmés) avec la QC et la régénération de `data/codes.json` habituelles.

*Rappel : ne jamais lancer `git push` automatiquement — Peter pousse manuellement.*
