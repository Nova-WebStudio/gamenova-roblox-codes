# Rapport Zoneblox — 7 septembre 2026 (lundi)

## a) Codes vérifiés (PRIORITÉ)

### hotGames
| Jeu | Résultat | Sources |
|-----|----------|---------|
| **Anime Last Stand** | **41 → 22 actifs** (19 déplacés en expirés) | Roblox Den (checké 7 sept.) + Pro Game Guides (1er sept.) |
| **Blue Lock Rivals** | **3 → 4 actifs** (rotation complète) | PGG (màj 6 sept.) + GamesRadar/Beebom/Pocket Gamer |
| Grow a Garden | Inchangé — 2 actifs (RDCAward/BEANORLEAVE10) | PCGamesN (torigate confirmé expiré) |
| Anime Vanguards | Inchangé — 3 actifs (Retribution/Wrath/MiniUpd2) | GamesRadar + Pocket Tactics |
| Volleyball Legends | Inchangé — 3 actifs (UPDATE_85/SHIRO/BLOCKED) | GamesRadar (3 sept.) |
| Steal a Brainrot | Inchangé — 1 actif (BESTBRAINROTEVER) | Dexerto |
| Fruit Battlegrounds | Inchangé — 2 actifs | (agrégat ambigu, prudence) |
| Blox Fruits / King Legacy / Fisch / Blade Ball | Inchangés (stables Sep 3-5) | — |

**Détail Anime Last Stand :** les 19 codes retirés (ALSISBACK!, World3Patch2, WORLD3REBALANCE, StellarWorld, SorryForDelay1/2/3, HypeWorld3, ReleaseCode!, Update0, ALSUPD1/2, BleachSS, HuntersMark, SaveRukia, DelaySorryals, BalancePatch3/3.1, GACHIAKUTA!?, Update83!) sont listés inactifs/expirés **par les deux sources**. Les 22 conservés sont confirmés **actifs par Roblox Den (7 sept.)**. Les ~24 actifs supplémentaires listés par Roblox Den n'ont **pas** été ajoutés (PGG les marque inactifs → conflit, prudence).

### Lot de rotation approfondie (Étape 2ter)
**Corrections de faux-actifs :**
- **Da Hood : 18 → 2 actifs.** Les 18 (seasonals 2024-2026 : EASTER26, APRIL26, OCTOBER25, BOSS, BUILD…) sont **tous listés expirés par PGG (3 sept.) ET Pocket Tactics (3 sept.)**. Nouveaux actifs confirmés par les deux : **DOG, SHARK** (300k DHC).
- **Shindo Life : 11 → 29 actifs.** Nos 11 codes étaient **tous périmés** (Roblox Den + PGG concordent). Nouvelle liste = intersection **PGG (1er sept.) ∩ Roblox Den** (29 codes : TickDamageBugs!, FixingShindoBuggyTimes!, PatchUpdate249point5!, RELLGIFTbag!, RELLGIFTsc!, ThankYouAllTruly!…).
- **Bubble Gum Simulator Infinity :** typo corrigé **`ogbfs` → `ogbgs`** (Roblox Den + Insider Gaming) — bug signalé dans CLAUDE.md.

**Confirmés OK (sous-listage acceptable, aucune preuve d'expiration) :** Arsenal (5, codes permanents), Dragon Adventures (6/11), Car Dealership Tycoon (14/23), Bee Swarm Simulator (17, aucun nouveau depuis février).

**⚠️ À revérifier au prochain run :**
- **pet-simulator-x** — la liste de 8 actifs (DIAMONDS2026, PSWELCOME, HATCHMASTER…) semble **périmée/suspecte** ; PocketGamer indique **0 code actif**. Non modifié faute de liste expirée explicite → **priorité J27** (vérifier Roblox Den).
- **grimoires-era** — collision de nom (Grimoires **Era** vs **Legacy** vs **Era 2**), sources muddled/périmées (Beebom fév. 2026). Non touché.

**Candidats en attente :** Volleyball Legends UPDATE_86/HAKKA_RETURN/SPIKER (vus dans l'agrégat mais **non confirmés** par GamesRadar 3 sept. qui liste toujours l'ancien set actif) ; Dragon Adventures DA7THBIRTHDAY2 ; Car Dealership Tycoon AUTUMNSOON.

## b) Directeur SEO (Étape 2bis)
- **Trending re-scanné (≥2 sources, rblxdb + blox-merch, 7 sept.) :** #1 **Steal An Egg ~1,4M**, Blox Fruits, Rivals, Jujutsu Shenanigans, Steal a Brainrot, Adopt Me — **tous couverts**. Aucun nouveau hit ≥4000 non couvert → evergreen.
- Le run a été consommé par **4 corrections majeures de codes** (priorité absolue, qui prime sur la brique cluster). Brique EEAT/honnêteté : correction d'une ligne de changelog ALS rendue incohérente par le nettoyage. **Roadmap mise à jour** (J26) ; prochaine brique J27 = **audit pet-simulator-x** puis enrichissement tier list Steal an Egg.

## c) Jeux / guides / tier lists / UGC / Jeu de la semaine
- **Jeu de la semaine (lundi) : inchangé — Steal An Egg** reste #1 des tendances (~1,4M joueurs). Aucun changement fabriqué (honnêteté).
- Aucun nouveau jeu ajouté (aucun hit non couvert détecté). Guides/tier lists/UGC : pas de modification ce run (priorité codes).

## d) Fichiers touchés + QC
- **181 fichiers** : 5 pages codes corrigées (anime-last-stand, blue-lock-rivals, da-hood, shindo-life, bubble-gum-simulator-infinity), 176 pages avec « 🔄 Vérifié le » rafraîchi au 7 sept., + `data/codes.json` (régénéré : 178 jeux, **1239 codes actifs**), `tools/code-watch.json` (snapshots/catalogVerify/pending), roadmap SEO.
- **QC : 0 problème.** div équilibrés partout, 0 null byte, toutes les pages finissent par `</html>`. Cache JS uniforme (`main.js?v=41`, main.js non modifié → pas de bump). GA4 présent sur les pages éditées. `data/codes.json` JSON valide.

---

Pour publier : dans le dossier GameNova, lance  git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main . Hostinger déploie automatiquement après le push.
