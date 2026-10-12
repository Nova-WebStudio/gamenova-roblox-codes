# RAPPORT ZONEBLOX — 2026-10-12 (session Peter : 3 jeux « la totale » + audit Halloween)

> Complément au rapport du run 05h. Travail demandé par Peter en session interactive.
> **Rien n'est en ligne tant que tu n'as pas poussé** (voir fin).

---

## 1. ANIME ZERO — NOUVEAU CLUSTER ✅ (net-new)

Place Roblox 114574503491412 — RPG anime / dungeon crawler, **en développement actif** (édité par LY). N'existait pas sur le site.

**Pages créées :**
- `codes-anime-zero.html` — **25 codes actifs** (~1 900 mots FR, miniature réelle, FAQ, guide d'échange, anti-troncature OK).
- `guides/anime-zero.html` — guide débutant honnête (codes, Lucky Spins / Trait Rerolls, donjons, niveaux 25/50, raids), fort maillage vers la page codes.
- `images/games/anime-zero.svg` — fallback SVG (jamais utilisé comme miniature principale).

**Codes — sourcing :** 25 codes retenus car confirmés par **≥ 2 sources fraîches** parmi Pocket Tactics (9 oct.), Dexerto (8 oct.) et igeeksblog. Les 4 plus récents (50KCCU, SORRYFORZEDELAY, UPDATETWO, ARISE67) marqués « Nouveau ». Codes à niveau requis signalés (25 / 50). 4 codes igeeksblog-only (SORRY4DELAY, UPDATE3LEGACY, 3TIMESACHARM, TRIALSPATCH) **écartés** (mono-source, kill switch).

**Miniature :** vraie `tr.rbxcdn.com` (hash 4929be…, 768×432 Webp) + fallback SVG en `onerror`. ⚠️ L'API Roblox (universe/thumbnail) est **bloquée par le proxy** des deux côtés → universeId non récupérable ; `ROBLOX_UNIVERSE_IDS` non renseigné pour ce jeu (miniature codée en dur, correcte). À compléter si l'API redevient joignable.

**Intégration complète (anti-orphelin) :** `index.html` (tableau `GAMES`), `js/main.js` (`GAMES_INDEX` + `ROBLOX_THUMBS`), carte `tous-les-codes.html`, carte `guides.html`, 2 `<url>` au sitemap, liens croisés codes ↔ guide. Propagé à l'accueil (sections auto `build_home`). **Pas de tier list** : aucune donnée d'unités sourcée → rien inventé (à créer plus tard).

---

## 2. DANDY'S WORLD — refresh ✅ (cluster déjà complet)

- **ICHOR** confirmé actif (samlover 2 oct., 50 Ichor). verifDate → **12 oct.**
- **SPOOKYSEASON** = **expiré** (samlover) → non ajouté (ce n'est pas un code Halloween actif).
- **RESEARCHMOBILE** (skin Rodger) = candidat **mono-source** (samlover) → non ajouté, à confirmer (2ᵉ source).
- Cluster (codes + guide + tier list) déjà présent et complet → pas de refonte.

---

## 3. SLAYERS 2 — ⚠️ CONFLIT non tranché (aucun changement)

- **roonby (7 oct.)** liste 12 codes actifs (dont nos SkillTreeReset / Release26 + Roguelike, RoguelikeRaceReset, M1LL1ON, ANIM4L, SPINS50, BREATHRESET, ARTRESET, EVILARTSPINS, POINTSRESET, SORRYFORSHUTDOWN).
- **Pocket Tactics (12 oct., plus récent)** dit **AUCUN code actif** — tout expiré (indice de shutdown/wipe via « SORRYFORSHUTDOWN »).
- games.gg (1ᵉʳ oct.) : ~4 actifs, non détaillés.
- **Décision : kill switch.** Aucun code ajouté ni retiré, verifDate **non bumpé**. Conflit à trancher au prochain run avec une 3ᵉ source fraîche (possible wipe à confirmer). Cluster (codes + guide + tier list) déjà complet.

---

## 4. AUDIT HALLOWEEN DU CATALOGUE

Passe ciblée sur les ~13 jeux les plus susceptibles d'avoir du contenu Halloween + un agrégateur multi-jeux :

- **blade-ball** : possède **déjà SPOOKYSEASON actif** (parmi 15 codes). ✓ À jour.
- **steal-a-brainrot** : événement Halloween **Haunted Fuse / secret Phoenix** en cours — **ce n'est pas un code** (angle guide possible). Candidats **FREEOCTOBLOCK777** et **saturn** = mono-source → **rejetés** (timesaver 8/10 marque le cousin OCTOBLOCK555 expiré). Page correcte (BESTBRAINROTEVER).
- **bee-swarm-simulator / tower-defense-simulator / pet-simulator-99** : **aucun nouveau code Halloween** (TDS = 1MILCOMMUNITY/2MILLION inchangés ; PS99 & Adopt Me & Brookhaven = jeux sans codes).
- **blox-fruits / grow-a-garden / steal-a-brainrot / arsenal** : vérifiés il y a < 4 jours, pas de code Halloween neuf.

**Conclusion :** plusieurs jeux ont un **événement** Halloween en cours, mais **très peu de codes Halloween neufs** à ajouter — et ceux qui existent (blade-ball) sont déjà en ligne. Aucun code Halloween manquant confirmé (≥ 2 sources) détecté. La rotation quotidienne maintient déjà la fraîcheur (~tous les 10 j). Audit exhaustif des 184 jeux non réalisable en une passe ; priorisé sur les candidats Halloween les plus probables.

---

## QC

- `node --check js/main.js` ✓ ; JSON valides (codes.json → **185 jeux / 1 276 codes**, code-watch.json, editorial-intelligence.json → 33 topics) ✓ ; XML valides (sitemap.xml **385 URLs**, sitemap-games.xml) ✓.
- Pages neuves/éditées : `</html>` final, **0 null byte**, `<div>` équilibrés, `#activeList` = 25 codes, miniature rbxcdn, maillage codes↔guide présents.
- `index.html` `GAMES` = 179 entrées, anime-zero présent (count 25) ; carte accueil propagée ; carte hub codes (1) ; carte hub guides (1).
- Régénération ordre §29 : build_site → build_codes_json → build_home → build_sitemap ✓.

## ÉTAT MÉMOIRE
- `tools/code-watch.json` : catalogVerify anime-zero + dandys-world = 12/10 ; `_session2026-10-12_interactive` (Anime Zero, Dandy's World, Slayers 2 conflit, audit Halloween).
- `tools/editorial-intelligence.json` : +`anime-zero-launch-2026-10` (PUBLISHED), +`halloween-audit-2026-10` (MONITOR).
- `EDITORIAL-QUEUE.md` mis à jour.

---

**Pour publier** : dans le dossier GameNova, lance `git add -A && git commit -m "Anime Zero (cluster) + refresh Dandy's World/Slayers 2 + audit Halloween" && git push origin main`. Hostinger déploie automatiquement après le push.
_(Rappel : si un `.git/index.lock` bloque, supprime-le avec `del ".git\index.lock"` puis relance.)_
