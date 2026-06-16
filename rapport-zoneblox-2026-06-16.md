# Rapport Zoneblox — 16 juin 2026

Run de maintenance autonome. **Mardi** → pas de mise à jour « Jeu de la semaine » (ÉTAPE 7 ignorée, normal).

## Contraintes d'environnement (reconfirmées)
- **Shell sans réseau sortant** : `curl` vers l'API Roblox renvoie une réponse vide. Vérification des codes faite uniquement via **WebSearch + web_fetch** (sources éditoriales).
- **Le mount bash sert une copie obsolète/tronquée** des fichiers édités via les outils de fichiers : la QC `cat`/`tail`/`python` sur ces fichiers a donné de faux positifs de troncature. **Toute la QC réelle a été refaite via les outils fiables Read/Grep** (qui lisent les vrais fichiers Windows). Les fichiers réels sont intacts.

## ÉTAPE 0/2 — Vérification des codes

### Blade Ball — grand nettoyage (action principale du run)
La page listait **~26 codes « actifs »**, dont une majorité **expirés depuis des mois**. Vérification croisée sur **2 sources fiables** (Pocket Tactics, maj 10 mai ; GamesRadar, maj 1er juin) :
- **Retirés (expirés, confirmés par les 2 sources)** : 5BVISITS, DRAGONS, SERPENT_HYPE, VISITS_TY, XMAS, MERRYXMAS, DELAYBALL, BPTEAMS, REBIRTHLTM, ROBLOXCLASSIC, GOODVSEVILMODE, EASTERHYPE, ZEROGRAVITY, GALAXYSEASON, FALLINGLTM, TOURNAMENTSW, LAVAFLOOR, LUNARNEWYEAR, LIVEEVENTS, 1.5BTHANKS, UPDATE.DAY, UPD250COINS.
- **Retirés (non confirmés par aucune source fiable)** : SUMMER2026, ABILITYDROP, JUNEUPDATE.
- **Conservés / ajoutés (13 codes actifs confirmés par les 2 sources)** : SERPENT, RAMADAN, 4BVISITS, 2BTHANKS, SPOOKYSEASON, FROGS, ENERGYSWORDS, SHARKATTACK, SUMMERWHEEL, SUMMERSTARTSHERE, RNGEMOTES, GIVEMELUCK, FREESPINS.
- Mises à jour cohérentes : compteurs (13 codes actifs), date (16 juin 2026), bandeau live, encadré « Dernière mise à jour » réécrit honnêtement, et `tools/code-watch.json` (snapshot blade-ball : knownCodes + lastChecked).

### Autres jeux populaires vérifiés (aucun changement nécessaire)
- **Grow a Garden / Grow a Garden 2** : TEAMGREENBEAN est déjà présent sur la page GaG2 ; la page GaG originale reste alignée (RDCAward, BEANORLEAVE10, torigate). Les résultats de recherche mélangent les deux jeux → pas de modification hasardeuse. Dates inchangées.
- **Steal a Brainrot** : toujours aucun code public fiable confirmé sur 2 sources (un seul « BESTBRAINROTEVER » non corroboré). Page inchangée.

## ÉTAPE 3 — Contenu minimum (indexation) : 6 pages étoffées (limite 6/run)
Pages du backlog mesurées sous/à la limite des 1200 mots rédactionnels. Chacune reçoit **une nouvelle entrée FAQ substantielle (~100 mots)**, exacte, utile et **non redondante** avec l'existant. Aucun code/chiffre/classement inventé ; date « Mis à jour le… » **non modifiée** (seul le rédactionnel a été enrichi).

| Page | Nouvelle FAQ | Angle |
|------|--------------|-------|
| codes/sailor-piece.html | « Sur quoi dépenser ses Beli en priorité ? » | Priorité style/arme puis fruit, garder des Beli pour reset |
| codes/wizard-alchemy.html | « Comment bien débuter dans Wizard Alchemy ? » | Quêtes d'intro, mana, race rerolls, matériaux rares |
| codes/project-mugetsu.html | « Comment devenir Shinigami ou Hollow ? » | Voies Soul Reaper / Hollow → Arrancar, rerolls |
| codes/combat-warriors.html | « Jouable sur mobile et à la manette ? » | Cross-platform, précision parry souris vs tactile |
| codes/bedwars.html | « Comment bien défendre son lit ? » | Couches de blocs, générateurs, surveiller la mini-carte |
| codes/jailbreak.html | « Quel véhicule acheter en priorité ? » | Vitesse/maniabilité > prix, améliorations garage |

Word count rédactionnel après édition (vrais fichiers) : toutes **> 1200 mots** avec marge.

## Correctif technique
- **codes/blade-ball.html** : l'édition (raccourcissement du tableau 26→13 lignes) avait laissé **2974 octets nuls** en fin de fichier (le fichier n'avait pas été tronqué à la bonne longueur). Nettoyé : fichier coupé proprement à `</html>`, **0 octet nul**, 29240 octets. Vérifié via Read (ligne 221 = `</html>`).

## ÉTAPE 8 — QC (outils fiables Read/Grep)
Sur les **7 pages codes éditées** :
- **`</html>`** : ✅ exactement 1 par fichier (aucune troncature réelle).
- **Nouvelles FAQ** : ✅ présentes sur les 6 pages (1 occurrence chacune).
- **Octets nuls** : ✅ 0 (blade-ball nettoyé ; les 6 autres = ajout de contenu, aucun nul).
- **Équilibre `<div>`** : préservé — les insertions sont des `<details>…</details>` autonomes (aucun `<div>` ajouté).
- **GA4 `G-FEL71QVHNL`** : ✅ présent.
- **Cache JS** : `js/main.js` non modifié → reste **`main.js?v=24`** (pas de bump).
- **JSON** `tools/code-watch.json` : valide et complet (vérifié via Read, se termine par `}`).
- **Honnêteté** : aucun code inventé ; codes retirés/ajoutés sur **2 sources fiables** ; rédactionnel 100 % FR.

## Étapes non réalisées ce run (justifié)
- **ÉTAPE 1 (ajouter 6 jeux)** : nécessite l'API Roblox (éligibilité ≥4000) + `thumbnails.roblox.com` (miniature tr.rbxcdn.com), injoignables depuis le shell. Non réalisable honnêtement.
- **ÉTAPES 4/5/6 (tier lists / guides complets / UGC)** : pas de nouvelle donnée à 2 sources justifiant une création/maj prioritaire ce run sans risque de duplication.
- **ÉTAPE 7 (Jeu de la semaine)** : mardi, non applicable.

## Backlog indexation pour prochains runs
À surveiller / étoffer si encore sous 1200 mots rédactionnels : fish-it, slime-rng, anime-vanguards (proches du seuil), ainsi que les pages signalées par les runs précédents non encore traitées.

## Fichiers touchés ce run
`codes/blade-ball.html`, `codes/sailor-piece.html`, `codes/wizard-alchemy.html`, `codes/project-mugetsu.html`, `codes/combat-warriors.html`, `codes/bedwars.html`, `codes/jailbreak.html`, `tools/code-watch.json`, `rapport-zoneblox-2026-06-16.md`.

> ⚠️ `git status` peut aussi contenir `guides/index.html` (modifié par un run précédent, non touché ce run) — il sera inclus dans le `git add -A`.

---

Pour publier : dans le dossier GameNova, lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
