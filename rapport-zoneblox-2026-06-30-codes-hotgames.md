# Rapport Zoneblox — 30 juin 2026 (3e passage : vérification codes hot games)

Complément aux deux rapports du matin (`rapport-zoneblox-2026-06-30.md` = réparation corruption + cache v=31 ; `…-complement.md` = rotation Blue Lock Rivals). Ces runs avaient explicitement reporté la vérification des **hot games restants** à un prochain passage. Ce run s'en charge.

État de départ : working tree intègre (0 null byte, cache `v=31` uniforme, `node --check js/main.js` OK). Modifications non commitées héritées des runs précédents toujours en attente du push de Peter.

## Vérification des codes (ÉTAPE 0 / 2) — hot games

Règle appliquée : un code n'est publié ACTIF que confirmé par **≥3 sources fiables OU source officielle** ; en cas de conflit, **prudence** (non-publication + « en attente »).

### ✅ Fisch — MISE À JOUR RÉELLE appliquée

Page datée du 14 juin → obsolète (les codes Fisch tournent vite). Vérifié sur **RoCodes** (30/06), **Beebom** (13/06) et **Pro Game Guides / G2A** :

| Retiré (passé EXPIRÉ) | Ajouté (ACTIF, vérifié 30/06) |
|---|---|
| Crews | **KingCrabstle** — Duck Floatie + 75× Sunshells + objets d'été |
| Sovereign | **Fischfest2026** — Beach Umbrella + 50× Sunshells |
| Companions | **AquariumCustomization** — 1 000 C$ + skin Longurt Dave Rod |

Conflit tranché : Crews / Sovereign / Companions sont marqués **expirés par Beebom** (source curée) alors que RoCodes (sur-inclusif) les garde « actifs » → décision **prudente = expirés**. Conservés actifs (confirmés par les 2 sources) : **scarlet, TemporarySubmarine, CARBON**.

Modifs sur `codes/fisch.html` : table active (6 codes), table expirés (17 → **20**), paragraphe descriptif + sources, bannière live, status-bar, date « Mis à jour le » (14 → **30 juin**), `dateModified` JSON-LD (`2026-06-14` → `2026-06-30`). Compteur « 6 codes actifs » inchangé (toujours 6). Candidat **TheDeepAwaitsForYou** mis « en attente » (Beebom seul).

### Jeux vérifiés — AUCUN changement (honnêteté : date inchangée)

- **Steal a Brainrot** — sources en **conflit** (Beebom/PCGamesN : aucun code ; un agrégateur annonce 9). Prudence → page « aucun code actif » maintenue. Snapshot daté.
- **Volleyball Legends** — PGG (20/06) confirme exactement les **9 codes déjà publiés**. Rumeur UPDATE_76 / ENCHO_RETURNS / BALANCE_76 sur **1 seule source** → **en attente**, non publiés. GamesRadar trop ancien (02/06) pour trancher.
- **Anime Vanguards** — **LagGone** confirmé par ≥3 sources MAIS **expire le 30/06** (aujourd'hui) → non publié (risque page périmée dès demain) ; **kat** = code meme. Les codes stables (13.5, EternalAdversaries, Gambler) restent confirmés actifs et présents. Logés « en attente ».
- **Anime Last Stand** — les codes les plus récents (TheATDSituationIsCrazy, ALSUPD1, DemonicCyborg, World3Patch2, WORLD3REBALANCE) sont **déjà présents**. Aucune expiration confirmée → inchangé.
- **King Legacy** — jeu « quiet », **aucun nouveau code** (PCGamer/Beebom 28/06). Set actuel cohérent → inchangé.
- **Fruit Battlegrounds** — codes actifs existants toujours listés par les sources. Nouveaux candidats **CRASHL4NDING, TIMEISVALUABLE** non confirmés sur ≥3 sources nommées → **en attente**.
- **Pet Simulator 99** — **0 code actif** confirmé (jeu sans MAJ, seuls codes merch one-time). Page sans code = correcte → inchangé.

## Jeux non revus ce run (à prioriser au prochain)

- **tower-defense-simulator** : la section codes n'expose pas de `code-value` au scan → **recheck structurel** recommandé (page peut-être « sans code » ou markup différent).
- Reste de la longue traîne (~150 pages codes) : non revue ce run, à couvrir progressivement.

## Candidats « en attente » (à reconfirmer au prochain run)

| Jeu | Candidats | Raison |
|---|---|---|
| Volleyball Legends | UPDATE_76, ENCHO_RETURNS, BALANCE_76 | 1 source seulement |
| Anime Vanguards | LagGone, kat | LagGone expire 30/06 ; kat = meme |
| Fruit Battlegrounds | CRASHL4NDING, TIMEISVALUABLE | <3 sources nommées |
| Fisch | TheDeepAwaitsForYou | Beebom seul |

## Autres étapes

- **Ajout de jeux / miniatures `tr.rbxcdn.com`** (ÉTAPE 1) : non fait (priorité donnée à la vérif codes ; nécessite navigateur Chrome pour l'API thumbnails).
- **Jeu de la semaine** : non concerné (mardi, `date +%u` = 2).
- **Tier lists / guides / UGC** : pas de changement ce run.

## QC (ÉTAPE 8) — vert

- `node --check js/main.js` : **OK** (main.js non modifié → reste `v=31`).
- `codes/fisch.html` : finit par `</html>`, **0 null byte**, `<div>` équilibrés (0), `<tr>` équilibrés (0), GA4 `G-FEL71QVHNL` présent, cache `main.js?v=31`, **1 seul** `data-cta="guidelink"`, 6 codes actifs, JSON-LD `dateModified` 2026-06-30.
- `tools/code-watch.json` : JSON valide, **0 null byte**, finit par `}` (snapshots fisch / volleyball-legends / anime-vanguards / anime-last-stand / king-legacy / fruit-battlegrounds / pet-simulator-99 / steal-a-brainrot mis à jour).
- Cache JS uniforme : **0 page hors `v=31`**.
- Aucun rédactionnel anglais introduit.

## Fichiers touchés ce run

- `codes/fisch.html` (rotation des codes + dates)
- `tools/code-watch.json` (snapshots + en attente)
- `rapport-zoneblox-2026-06-30-codes-hotgames.md` (ce rapport)

> Rappel : `git status` affiche aussi les modifications héritées des runs du matin (`codes/blue-lock-rivals.html`, et `tools/code-watch.json` / `tools/rapport-2026-06-10.md` / `ugc-gratuit/` en « deleted staged + untracked »). Tous intègres ; l'incohérence d'index se résout au `git add -A`.

---

**Pour publier** : dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` .
Hostinger déploie automatiquement après le push.
