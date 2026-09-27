# Rapport ZoneBlox — 2026-09-26 (run 05h, samedi · full maintenance + editorial)

Heure de démarrage : 05h02 (Europe/Brussels). Mode : run complet 05h. Git propre au départ, dernier run 25/09. **Aucun `git push`** (règle : publication manuelle).

---

## CODES

Règle appliquée : 2 sources fiables indépendantes minimum par changement ; date de vérification à jour ; aucune modification sans preuve.

### hotGames (vérifiés ce matin)
| Jeu | Résultat | Détail |
|-----|----------|--------|
| **steal-a-brainrot** | ✏️ **+1** | **BESTBRAINROTEVER réactivé** (expiré → actif) — Dexerto + GamesRadar (fait apparaître le brainrot secret La Vacca Saturno Saturnita sur le tapis rouge). Page 0 → 1. Prose « aucun code » corrigée aux 3 endroits. |
| **blade-ball** | ✏️ **−1** | **GOODVSEVIL expiré** — Pocket Tactics (22 sept) + GamesRadar (18 sept) concordants ; Beebom (1er sept) minoritaire/périmé. Page 15 → 14. |
| anime-last-stand | ✅ inchangé | 3 actifs (MagicKnights!, ElfReincarnation!, IsItReallyWeekly?!) — PGG confirme. Beebom sur-liste (périmé), non suivi. |
| grow-a-garden | ✅ inchangé | 2 actifs (RDCAward, BEANORLEAVE10) confirmés Beebom + PGG. |
| blox-fruits | ✅ inchangé | 23 codes (superset stable des sub-codes) ; PT 18 sept ⊂ notre liste. |
| fisch | ✅ inchangé | 4 codes ; MarianaIsGoingCrazy actif (Beebom 19 sept). |
| king-legacy | ✅ inchangé | 9 codes = match exact Pocket Tactics 18 sept. |

### Rotation / queue de la veille
| Jeu | Résultat | Détail |
|-----|----------|--------|
| **all-star-tower-defense** | ✏️ **+3** | ReturnOfTheLobbies, ALateSummerAwaits, AwesomeBeginnerCode (PT 21 sept + Beebom 4 sept). Page 16 → 19. **game11** non ajouté (1 source). |
| anime-apocalypse | ✅ inchangé | PGG (24 sept) liste TRANSCENDENT + INVASION actifs, mais 1 seule source fraîche chargée (PT/insider/Beebom 404 ou conflit) → **non ajoutés** (kill switch). À traiter au prochain run. |

- **Codes ajoutés** : BESTBRAINROTEVER (SAB) ; ReturnOfTheLobbies, ALateSummerAwaits, AwesomeBeginnerCode (ASTD). **+4**
- **Codes expirés** : GOODVSEVIL (Blade Ball). **−1**
- **Net** : `data/codes.json` 1222 → **1225 codes actifs / 183 jeux**.
- **Candidats en attente** (non publiés faute de 2e source / conflit) : TRANSCENDENT, INVASION (anime-apocalypse) ; game11 (ASTD) ; FREESEED/STORY/STARBUD (GAG) ; LIGHTNINGABUSE (blox-fruits) ; BATTLEROYALE (Blade Ball).
- **Sources officielles** : Trello Blox Fruits/Blade Ball/Blue Lock consultés dans hotGames (non déterminants ce run).

---

## SEO

- **Update before create** appliqué : aucun nouveau slug créé ; FC 27 traité par **UPDATE** de `data/fc-27/updates.json` (pas de nouvelle URL), conformément à la règle anti-cannibalisation sur les pages evergreen.
- Anti-orphelin / maillage : builds régénérés (hubs codes/guides/tier-list, accueil, sitemap) ; aucune page isolée introduite.
- Signal de fraîcheur : sitemap `lastmod` régénéré (verifDate=183 pages).

---

## NOUVEAUX JEUX

Aucun ajout. Kill switch : aucun jeu ne réunit traction réelle **+** codes réels **+** absence de page ZoneBlox. Grow a Garden / Steal a Brainrot dominent (déjà couverts).

---

## CONTENU

- **FC 27** : 3 entrées de lancement ajoutées à `updates.json` (voir section FC 27).
- Guides / tier lists : aucune modification (pas d'évolution réelle justifiant un changement — règle « pas de retouche cosmétique »).

---

## ANIIMO

11 codes stables (données in-game). **Aucune modification** : l'event *Aniimo Together* se termine le **27 sept** → revérification codes + nouvelle créature au prochain run après cette date. Fichiers `/games/` non touchés directement (règle data-driven respectée).

---

## GTA 6

Sortie **19 nov. 2026 confirmée** (Zelnick, pas de report). Page evergreen inchangée (MONITOR). **Nouveau signal** : reveal officiel **Game Informer annoncé pour le 29 sept** → à surveiller ; si contenu concret, UPDATE de l'evergreen (pas de nouvelle URL).

---

## FC 27

**Priorité éditoriale du jour (J+1).** `data/fc-27/updates.json` enrichi de **3 entrées** (source : EA pitch notes officiel « Launch Update » + roadmap Athlon), `updated` → 2026-09-26 :

1. **Saison 1 « Ones to Watch » + refonte FUT** : OTW (17 sept → 22 oct, via Season Pass/DCE/objectifs) ; chimie Icônes base 88 OVR, +1 Ligue, Nation +2→+1 ; Héros Ligue +2→+1 ; packs renommés Mini/Small/Large/Jumbo/Giant (Common/Rare supprimé) ; PlayStyles+ max 5→3 ; palier Hall of FUT.
2. **Récompenses revues** : Rivals/Champions « plusieurs fois plus » de pièces ; Season Points 15-100/match (jusqu'à 850/j) ; Division 6 retirée de la qualif Champions ; finales 15 matchs ; **TOTW voté par la communauté** (6 premières semaines).
3. **The Grounds / Destined for Glory / Career** : hub open-world The Grounds (PS5/Xbox Series/Switch 2/PC, 1er Club Tournament 11v11 Classic Stadium) ; Destined for Glory (15 joueurs/sem) ; Career nouvelles Icônes (Kaká, Di Natale, Del Piero, Raúl, van Persie) + Manager Live/Creator Challenges.

*À faire prochain run* : notes des tops joueurs (nécessiterait un modèle de données distinct ; non couvert par ce JSON de news).

---

## EDITORIAL INTELLIGENCE

- **Top opportunités** : aucune nouvelle opportunité de création ; le travail à valeur = maintenance codes + publication du lancement FC 27.
- **Tendances** : GAG/SAB toujours dominants (couverts) ; Roblox Fall Games sans hit (Showdown ~240 CCU) ; GTA 6 reveal 29 sept à surveiller.
- **Articles créés** : 0 (kill switch).
- **Pages mises à jour** : 3 pages codes (SAB, Blade Ball, ASTD) + FC 27 updates.json.
- **Sujets ignorés** : marketing GTA 6 (faible valeur joueur) ; sur-listages Beebom (fiabilité).
- **Sujets à surveiller** : anime-apocalypse (TRANSCENDENT/INVASION), Aniimo (post-27 sept), GTA 6 (29 sept), petites rotations non vérifiées.
- `tools/editorial-intelligence.json` : 13 topics, SAB → PUBLISHED, FC27 → UPDATED, topic maintenance 26/09 ajouté.

---

## EDITORIAL QUEUE

- **Urgents** : rien.
- **À publier** : rien (kill switch).
- **À mettre à jour** : anime-apocalypse (TRANSCENDENT/INVASION si 2e source) ; ASTD (CTA guidelink absent, pré-existant) ; GTA 6 (reveal 29 sept).
- **À préparer / surveiller** : Aniimo (27 sept), FC 27 promos Saison 1, RELL Seas, Roblox Everywhere/Fall Games.
- **Demain** : codes hotGames + **petites rotations laissées non vérifiées** (doors, 99-nights, royale-high, slap-battles) en trouvant d'abord l'URL source à jour ; Aniimo post-event ; anime-apocalypse.

---

## QC

- **Régénération** ordre respecté : `build_site.py` → `build_home.py` → `build_codes_json.py` → `build_sitemap.py`.
- `node --check` : main.js ✅, events.js ✅.
- JSON valides : codes.json, fc-27/updates.json, editorial-intelligence.json, code-watch.json, games-index.json ✅.
- sitemap.xml : XML valide, se termine par `</urlset>`, **381 URLs** ✅.
- Pages éditées (SAB, Blade Ball, ASTD, anime-apocalypse) : fin `</html>` ✅, **0 null byte** ✅, div équilibrés (0) ✅.
- CTA `guidelink` unique : SAB ✅, Blade Ball ✅. **ASTD = 0 (pré-existant, déjà absent dans git HEAD — pas une régression** ; noté en queue).
- Cache : `main.js?v=43` uniforme sur 167 fichiers HTML (main.js non modifié → pas de bump).
- **Erreurs corrigées** : aucune corruption ; toutes les écritures faites en Python avec assertions (pas de `sed`).

---

## Pour publier

Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
