# Rapport Zoneblox — 1 juillet 2026 (run quotidien 05h00)

Jour : **mercredi** (`date +%u` = 3) → pas de « Jeu de la semaine » (lundi uniquement).
État de départ : working tree intègre côté contenu (cache `main.js?v=32` uniforme sur 306 références, `node --check js/main.js` OK, 0 null byte). Modifications non commitées héritées des runs précédents toujours en attente du push de Peter.

## ÉTAPE 0 / 2 — Vérification des codes (PRIORITÉ)

Règle appliquée : un code n'est publié ACTIF que confirmé par **≥3 sources fiables OU une source officielle** ; en cas de conflit → **prudence** (non-publication + « en attente »). Sources utilisées ce run : Beebom (curée, datée), The Click, allthings.how, RoCodes, PCGamer, PCGamesN, Pocket Tactics, GamesRadar.

### ✅ Anime Vanguards — MISE À JOUR RÉELLE (ajout de LagGone)

**LagGone** avait été mis « en attente » le 30 juin par prudence (crainte d'une expiration le 30/06). Le code a **survécu** et est désormais listé **ACTIF au 1er juillet 2026 par ≥3 sources datées de juillet** (The Click, allthings.how, RoCodes) + PCGamer → consensus de **8 codes actifs** : LagGone, 13.5, EternalAdversaries, Gambler, DMCAFree, Liberation, 223, Cog5th. Publié.

Modifs sur `codes/anime-vanguards.html` :
- Nouvelle ligne active **LagGone** — 🎲 1 000 Trait Rerolls + 200 000 Iced Teas + 100 Summer Capsules (niveau 30).
- Compteur **7 → 8 codes actifs** (hero + bannière live).
- Dates : « Mis à jour le » 23 juin → **1 juillet 2026** ; « Vérifié le » 30 juin → **1 juillet 2026** ; status-bar + bannière live → 1 juillet ; « fonctionnent en juin » → juillet.
- SEO : titre / og:title / JSON-LD name / H1 / meta description « juin 2026 » → **juillet 2026** ; JSON-LD `dateModified` `2026-06-23` → **`2026-07-01`**.
- Paragraphe « Dernière mise à jour » enrichi (mention LagGone) ; « Page vérifiée le » → 1 juillet.
- `kat` conservé « en attente » (code meme, non publié).

### Jeux vérifiés — AUCUN changement (honnêteté : « Mis à jour le » inchangé, seul « Vérifié le » rajeuni)

| Jeu | Vérification | Décision |
|---|---|---|
| **Blue Lock Rivals** | Beebom (maj 30/06, « checked July 1, 2026 ») : actifs = GAGAREWORK, ADDRESSME, BEARCLAW → **identiques** à la page. | Inchangé. Jeu à expiration rapide (≤ 1 j) : confirmé stable aujourd'hui. |
| **Grow a Garden** | Beebom : actifs = RDCAward, BEANORLEAVE10 ; expirés = torigate, LUNARGLOW10 → **identiques**. | Inchangé. |
| **Grow a Garden 2** | The Click (juillet), Beebom, Game8, u7buy, nerdschalk : **seul TEAMGREENBEAN** confirmé actif ; STARBUD non vérifié. Page = « 1 code actif » (TEAMGREENBEAN), le reste bien en table **expirés**. | Correct, inchangé. |
| **Volleyball Legends** | Page = UPDATE_75…JUNE_2026 (9 codes). Beebom **en retard** (UPDATE_72). Rumeurs UPDATE_76 / ENCHO_RETURNS / BALANCE_76 = 1 source. | Inchangé ; candidats maintenus « en attente ». |
| **Steal a Brainrot** | Beebom + PCGamesN + Pocket Tactics : **aucun code** (système de codes vidé depuis UPD 11). | Page « aucun code actif » = correcte, inchangée. |
| **Blade Ball** | Beebom **périmé (avril)** — non probant. Aucune source ≥3 montrant un changement depuis le 30/06. | Inchangé (revérifié, pas de signal de changement). |
| **Blox Fruits** | Dexerto/The Click (juillet) : « updated June 29, no new codes ». Set curé stable. | Inchangé. |

« 🔄 Vérifié le » rafraîchi à **1 juillet 2026** sur les 7 pages ci-dessus + anime-vanguards (8 pages au total réellement re-vérifiées ce run).

## Candidats « en attente » (à reconfirmer au prochain run)

| Jeu | Candidats | Raison |
|---|---|---|
| Volleyball Legends | UPDATE_76, ENCHO_RETURNS, BALANCE_76 | 1 source seulement |
| Anime Vanguards | kat | code meme |
| Fruit Battlegrounds | CRASHL4NDING, TIMEISVALUABLE | < 3 sources nommées |
| Fisch | TheDeepAwaitsForYou | Beebom seul |

## Jeux non revus ce run (à prioriser au prochain)

- Longue traîne des ~150 autres pages codes non re-vérifiée aujourd'hui (priorité donnée aux hot games les plus volatils : jeux à expiration rapide + gros trafic).
- Hot games restants non re-checkés aujourd'hui (stables au 30/06, à couvrir demain) : fisch, king-legacy, fruit-battlegrounds, anime-last-stand, pet-simulator-99, tower-defense-simulator (recheck structurel), world-fighters, noob-incremental, defend-ur-base-with-anime, spin-a-soccer-card, merge-a-nuke, vv-ultimatum, fifa-super-soccer, hypershot, blockspin, run-a-restaurant, squid-game-x, catch-a-monster, brainrot-evolution, 100-days-at-sea.

## Autres étapes (1–7)

- **Ajout de jeux / miniatures `tr.rbxcdn.com`** (ÉTAPE 1) : non fait ce run (priorité codes ; nécessite navigateur Chrome pour l'API thumbnails, non requis ici).
- **Tier lists / guides / UGC** : pas de changement ce run.
- **Jeu de la semaine** : non concerné (mercredi).

## ÉTAPE 8/9 — QC (vert)

- 8 pages modifiées (`anime-vanguards`, `blue-lock-rivals`, `grow-a-garden`, `grow-a-garden-2`, `volleyball-legends`, `steal-a-brainrot`, `blade-ball`, `blox-fruits`) : finissent par `</html>`, **0 null byte**, `<div>` équilibrés (0), GA4 `G-FEL71QVHNL` présent, cache `main.js?v=32`, **1 seul** `data-cta="guidelink"`, **1 seule** ligne « 🔄 Vérifié le » chacune.
- `codes/anime-vanguards.html` : table active = **8 codes** (LagGone unique), « 8 codes actifs » cohérent (hero + bannière), 0 reliquat « 7 codes actif », **~1419 mots** (> 1200), JSON-LD `dateModified` = 2026-07-01.
- `tools/code-watch.json` : **JSON valide**, 0 null byte, finit par `}` ; snapshots `lastChecked` = 2026-07-01T05:00:00Z pour les 7 hot games vérifiés + LagGone promu dans `anime-vanguards.knownCodes`.
- `js/main.js` **non modifié** → `node --check` OK, cache reste `v=32` (aucun bump nécessaire), **306 références uniformes** en v=32.
- Aucun rédactionnel anglais introduit.

## ⚠️ À signaler à Peter (git — hérité, non créé ce run)

`git status` affiche une entrée parasite `UA "\310\267"` (octet 0xC8 0xB7 = « ȷ ») **sans fichier sur disque** et **absente de `git ls-files -u`** (aucun contenu non-mergé réel). Vestige d'index d'une session antérieure ; un `git add -A` la résout normalement. À surveiller après le prochain commit. Les suppressions/ajouts stagés de `tier-list/*` et `ugc-gratuit/` restent hérités des runs précédents (incohérence d'index qui se résout au `git add -A`).

## Fichiers touchés ce run

- `codes/anime-vanguards.html` (ajout LagGone + dates + SEO juillet)
- `codes/blue-lock-rivals.html`, `codes/grow-a-garden.html`, `codes/grow-a-garden-2.html`, `codes/volleyball-legends.html`, `codes/steal-a-brainrot.html`, `codes/blade-ball.html`, `codes/blox-fruits.html` (« Vérifié le » → 1 juillet 2026)
- `tools/code-watch.json` (snapshots + LagGone promu)
- `rapport-zoneblox-2026-07-01.md` (ce rapport)

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
