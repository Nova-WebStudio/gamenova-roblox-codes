# 📋 EDITORIAL QUEUE — ZoneBlox

> Mémoire éditoriale opérationnelle (spec V2, section 7). Mise à jour à chaque run.
> Détail sourcé complet dans `tools/editorial-intelligence.json` et `tools/code-watch.json`.
> **Dernière MAJ : 2026-10-24 (run 05h — 0 édition, kill switch sur tous les conflits)**

## ✅ FAIT — RUN 05h 2026-10-24 (samedi, pas de Jeu de la semaine)

- **Codes : 0 édition.** Vérification prioritaire des hot games + lot de rotation + cibles de la file. **Toutes** les cibles actionnables se sont révélées soit **confirmées inchangées**, soit sous **KILL SWITCH justifié** (conflit / concordance insuffisante). Aucune invention, aucune suppression sans preuve.
  - **Confirmés inchangés** : `steal-a-brainrot` (BESTBRAINROTEVER = Dexerto 12/10, set identique) · `anime-vanguards` (14 codes 2ᵉ anniversaire = Roonby 13/10, **source unique non vérifiée** → aucune addition) · `grow-a-garden` (RDCAward/BEANORLEAVE10 maintenus — ⚠️ la page Dexerto « FREESEED » concerne **grow-a-garden-2**, un AUTRE jeu, donc non applicable à la page originale ; clarification de l'item queue précédent).
  - **KILL SWITCH maintenu** : `grimoires-era` (**conflit 3 voies CONFIRMÉ** — games.gg 03/10 vs pocketgamer+pockettactics vs notre page) · `rivals` (Insider 04/10 = FREE137 **plus ancien** que notre FREE182 ; Roonby 06/10 = FREE201 → version-dependent, pas de set actif concordant frais) · `fisch` (Roonby 17/10 « no codes available », non tranchable) · `anime-battle-rng` (sources syndiquées nerdschalk/allthings.how Aug 6 → pas de 2 sources fraîches indépendantes).
- **Rotation** : `anime-battle-rng`, `attack-on-titan-revolution`, `project-mugetsu`, `grimoires-era`, `rivals`, `haze-piece`, `fisch`, `steal-a-brainrot`, `grow-a-garden`, `anime-vanguards` → dates `catalogVerify` rafraîchies au 24/10. Constat : listes gonflées non-prunables faute de **preuve d'expiration** (§4).
- **News** : GTA 6 (preload 12/11 + sortie 19/11 confirmés, rien de neuf Newswire → evergreen inchangé) · **Aniimo « Season 1 Part II » annoncé pour le 29/10** (à préparer, data-driven) · FC : titre EA live = **FC 26** (promos FoF / Answer the Call) → décision naming toujours en attente de Peter.
- **Régénération** : **aucune** — aucun contenu/data du site modifié ce run (seuls les fichiers mémoire `tools/*.json` + queue + rapport ont changé). Donc pas de `build_site`/`build_home`/`build_codes_json`/`build_sitemap` (éviter toute churn non justifiée, §3/§29).
- **QC** : JSON `code-watch.json` + `editorial-intelligence.json` valides, 0 null byte, 0 fichier site touché. Arbre git propre avant run.

---

## 🔥 URGENT

- **GTA 6** — ~4 semaines avant lancement (**19/11/2026**). Préchargement **12/11** confirmé. Surveiller le **Rockstar Newswire** à chaque run (heure de préchargement, patch day-one). **UPDATE evergreen uniquement**, séparer CONFIRMÉ / RAPPORTÉ / RUMEUR. Rien de neuf au 24/10.

## 🟢 À PUBLIER

_(rien)_ — aucun nouveau jeu Roblox avec preuve d'intérêt multi-source **+ codes réels** cette nuit ; tous les conflits de codes sous kill switch.

## 🛠️ À METTRE À JOUR (candidats near-ready)

- **grimoires-era — PÉRIMÉE (conflit 3 voies CONFIRMÉ 24/10).** games.gg (NEXTCHAPTER!/MINING!/UPDATE0.6!/SYSTEMREWORK!) vs pocketgamer+pockettactics (REVAMPSOON!/25SPINS!/2025BOOSTS!/CLOVER) vs page (codes release). Rebuild via **source officielle** (Trello/Discord) requis. Ne rien éditer tant que non tranché.
- **rivals — décalage de version.** Page FREE182 ; Insider 04/10=FREE137 (stale) ; Roonby 06/10=FREE201. Besoin d'une **source fraîche marquant clairement l'actif** + concordance.
- **anime-battle-rng — gonflée (~35 codes).** Sources trouvées = contenu syndiqué (nerdschalk = allthings.how, Aug 6). Besoin 2 sources **indépendantes + fraîches** pour pruner (avec preuve d'expiration).
- **attack-on-titan-revolution — gonflée (21 codes).** Dexerto 02/10 ne confirme que 2 actifs (WZINS+TERRA70K). Preuve d'expiration requise avant tout prune (§4 : jamais de suppression sans preuve).
- **haze-piece** — PHANTOMSHIP + OKUCHI désormais à **2 sources** (Roonby 13/10 + TheSpike 06/10 stale) → toujours <3 requis OU officiel. Non ajoutés.
- **type-soul — page vide.** ~55 codes (Insider Gaming) mais **sans récompenses** → 2-3 sources propres avec récompenses.
- **noob-incremental — MUST_UPDATE.** Rewrite + resync `const ACTIVE`/compteur.
- **8 pages à liste vide** (`100-days-at-sea`, `basketball-zero`, `be-a-brainrot`, `encounters`, `garden-tower-defense`, `pet-simulator-x`, `royale-high`, `slap-battles`) : republier **seulement** là où ≥2 sources concordent.

## 🟡 À PRÉPARER / DÉCISION PETER

- **🆕 Aniimo « Season 1 Part II » (29/10)** : gros update annoncé (Update 1.019 déjà sorti le 15/10 = 1ᵉʳ nouveau monstre). **PRÉPARER** la mise à jour `data/aniimo/` + `build_site` **après** l'update officiel. Spécifics non confirmés au 24/10 → aucune invention avant confirmation.
- **⚠️ Naming FC 27 vs FC 26** : titre EA live = **FC 26** (promos FoF / Answer the Call, calendrier actif). Bloque la couverture Ultimate Team. **À trancher.**
- **⚠️ Jeu de la semaine (§30)** : marqueurs `<!-- FEATURED-WEEK-START/END -->` **toujours absents du code** → étape du lundi non exécutable. À Peter : ajouter les marqueurs ou confirmer le mécanisme.
- **⚠️ Listes gonflées** (décision maintien vs rebuild) : anime-battle-rng (~35), anime-astral-simulator (~100), dragon-blox (~82), attack-on-titan-revolution (21).
- **CTA manquant** : `codes-da-hood.html`, `codes-rivals.html`, `codes-knockout.html` n'ont **pas** de `data-cta="guidelink"` (pré-existant, pas de guide/tier dédié). À ajouter si des pages dédiées existent.
- **Note cache obsolète dans CLAUDE.md** : dit « main.js?v=19 » mais le site est à **v47** (hors `/avatar/` off-limits). À corriger dans CLAUDE.md.

## 👀 À REVÉRIFIER (conflits non tranchés)

- **Codes** : grimoires-era (conflit 3 voies), rivals (version en retard), anime-battle-rng (gonflée, sources syndiquées), attack-on-titan-revolution (gonflée), haze-piece (PHANTOMSHIP/OKUCHI 2/3), grand-piece-online (tailor vouchers), da-hood (ESKETIT 1 source), garden-tower-defense (conflit), aniimo (aniimazingfroyo = khelnow 04/10 actif vs mein-mmo 09/10 expiré).
- **Rotation en retard** : anime-astral-simulator, dragon-blox (>40 j) ; ~30 jeux jamais entrés dans catalogVerify (beaucoup = stubs sans codes).

## 📅 PRIORITÉS PROCHAIN RUN (15h / 22h / 05h 25/10)

1. **Aniimo** : suivre l'update **29/10** (préparation data-driven ; ne rien publier avant l'officiel).
2. **grimoires-era** : source officielle (Trello/Discord) → rebuild propre (seul moyen de trancher le conflit 3 voies).
3. **rivals** : source fraîche marquant l'actif → combler le décalage FREE182→FREE201.
4. **anime-battle-rng / attack-on-titan-revolution** : 2 sources **indépendantes + fraîches** + preuve d'expiration → élaguer.
5. **haze-piece** : 3ᵉ source → PHANTOMSHIP + OKUCHI.
6. **Hot games** : GPO (tailor vouchers), Da Hood (ESKETIT), Anime Vanguards (fin 2ᵉ anniversaire ?), Fisch (FischFright 3), GAG (FREESEED = GaG2, hors sujet page originale).
7. **GTA 6** Newswire (préchargement/day-one) · **FC 26** (si naming tranché).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push. (Si `.git/index.lock` bloque : `del ".git\index.lock"` puis relance.)_
