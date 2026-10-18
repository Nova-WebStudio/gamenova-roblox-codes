# Rapport ZoneBlox — 2026-10-13 (run 05h)

> ⚠️ Déclenchement en retard : tâche programmée pour 05h01 (Belgique), exécutée à 17:10 UTC. Fenêtre de recherche traitée : nuit + journée du 13/10. Mardi → **pas de jeu de la semaine** (§30).
>
> **Bilan : run d'intelligence/vérification. AUCUNE édition HTML, AUCUN build, AUCUN code ajouté/retiré.** Tous les jeux hot sont à jour ou sous kill-switch ; les écarts de rotation détectés exigent une 2ᵉ source fraîche ou un rewrite complet trop risqué en autonome. Priorité respectée : **EXACTITUDE > fraîcheur > quantité.**

## CODES

### hotGames (priorité absolue)
- **volleyball-legends** : UPDATE_91 / REPLAYS / MVP confirmés **actifs** (Dexerto 11/10). Pas d'Update 92. → inchangé.
- **anime-vanguards** : 8 codes du set anniversaire OK (vérif 12/10). Pocket Tactics liste un set plus large → **non repris** (1 source, gros changement). → inchangé.
- **grow-a-garden** : stable, aucun nouveau code (GAG en publie très rarement). → inchangé.
- **steal-a-brainrot** : **BESTBRAINROTEVER** toujours actif (Dexerto 12/10 « no new codes found » + nerdschalk). Halloween = objets d'événement (Phoenix via Haunted Fuse), pas des codes. → inchangé.
- **blox-fruits** : stable. → inchangé.

### Codes ajoutés
- Aucun.

### Codes expirés / retirés
- Aucun (aucune preuve d'expiration suffisante pour les candidats ; voir conflits).

### Candidats en attente (mono-source / conflit → KILL SWITCH)
- **blue-lock-rivals** : drop EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT confirmé par **Dexerto (11/10) seul** (qui marque l'ancien set expiré) ; **Pocket Tactics (04/10)** montre encore DONREVAMP/SENDOUNEXT/ACEEATER actifs. → page inchangée, 2ᵉ source fraîche requise.
- **anime-defenders** : SKILLTRESS/MEGAUPD/RAIDSAREBACK restent mono-source (RobloxDen ; Dexerto périmé).
- **dig-and-clean** : UPDATE3 mono-source (destructoid 01/10).

### Sources officielles
- Rockstar Newswire (GTA 6) et ea.com/Pitch Notes (FC) suivis ; rien de nouveau à publier.

## SEO
- **Tendance détectée** : aucune nouvelle tendance Roblox majeure justifiant un cluster ce run.
- **Update before create** respecté : aucune nouvelle URL créée. Les écarts détectés sont des **mises à jour de pages existantes** (wizard-alchemy, iron-soul, anime-expeditions), différées faute de sourcing/rewrite sûr.
- **Anti-cannibalisation** : n/a (aucune création).

## NOUVEAUX JEUX
- Aucun ajout. Aucun nouveau jeu avec preuve d'intérêt réel détecté ce run.

## CONTENU
- Guides : aucun. Tier lists : aucune (pas d'évolution réelle justifiant une MAJ). Articles : aucun. Mises à jour de pages : aucune (voir « à vérifier »).

## ANIIMO
- MONITOR. Pas de stats combat Irisalis publiées → aucun ajout aux data. `build_site.py` non lancé.

## GTA 6
- **Trailer 3 : toujours NON sorti au 13/10** (RUMEUR persistante d'insiders depuis juin, aucune source fiable ne confirme une sortie ni une date ferme). Sortie du jeu = **19 nov 2026 RAPPORTÉE** (préco live), non reconfirmée officiellement ce run. → pages evergreen inchangées, veille Newswire.

## FC 27
- ⚠️ **Divergence de naming** : le titre EA live en octobre 2026 est **FC 26** (FC 27 attendu ~sept 2027). Les verticales/pages « FC 27 » pourraient devoir cibler FC 26. À trancher par Peter. Promo FC 26 suivie via Dexerto/ea.com. → aucune édition.

## EDITORIAL INTELLIGENCE
- **Top opportunités** : (1) rewrite wizard-alchemy (set actif 2-sources prêt), (2) résolution drop blue-lock-rivals, (3) iron-soul-dungeon (trancher l'ampleur).
- **Tendances** : rien de neuf majeur.
- **Articles créés** : 0. **Pages mises à jour** : 0.
- **Sujets ignorés** : candidats mono-source (kill switch).
- **Sujets à surveiller** : GTA 6 Trailer 3, FC 26 promos, Blue Lock drop, Slayers 2 (conflit 3 voies), Anime Zero (dev actif).
- Mémoire : `tools/editorial-intelligence.json` (39 topics, 7 ajoutés/mis à jour aujourd'hui) + `tools/code-watch.json` (`_notes2026-10-13`, 10 dates `catalogVerify` rafraîchies).

## EDITORIAL QUEUE
- **Urgents** : GTA 6 (Newswire) ; Blue Lock drop (2ᵉ source).
- **À publier** : rien.
- **À mettre à jour** : wizard-alchemy (rewrite), iron-soul-dungeon, anime-expeditions, dig-and-clean (UPDATE3), anime-defenders, FC 26 promo.
- **À préparer** : naming FC 27→26, Anime Zero, guide Phoenix (Steal a Brainrot), §30 marqueurs jeu de la semaine, resync bug `const ACTIVE`.
- **Demain (05h 14/10)** : voir `EDITORIAL-QUEUE.md` §PRIORITÉS.

## QC
- Fichiers modifiés : `tools/editorial-intelligence.json`, `tools/code-watch.json`, `EDITORIAL-QUEUE.md`, ce rapport. Sauvegardes temporaires déplacées dans `_to_delete/` (gitignoré).
- Tests : JSON validés (`json.load` OK sur les deux fichiers). Aucun fichier HTML touché → pas de risque de troncature HTML, aucun build nécessaire.
- Erreurs corrigées : aucune.

## Jeux vérifiés ce run (11)
volleyball-legends, anime-vanguards, grow-a-garden, steal-a-brainrot, blox-fruits, blue-lock-rivals (hot) · wizard-alchemy, iron-soul-dungeon, anime-expeditions, dig-and-clean, slayers-2, anime-defenders (rotation/conflits).

---

**Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.**
