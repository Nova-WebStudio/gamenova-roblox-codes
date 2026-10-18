# Rapport ZoneBlox — 2026-10-15 (run 05h, jeudi)

**Type de run :** 05h — Full Maintenance + Editorial Intelligence (fire décalé ~08:30 UTC)
**Fenêtre :** nuit (12-24 h précédentes) · **Mode :** autonome
**Résultat en une ligne :** **fix systémique haute-valeur** — resync du bouton « Tout copier » (`const ACTIVE`) sur **68 pages codes** désynchronisées (elles copiaient des codes périmés/absents), **0 édition de code risquée** (kill-switch maintenu sur tous les drops mono-source/conflits), 4 verifDate rafraîchies. Fidèle à « EXACTITUDE > FRAÎCHEUR > UTILITÉ ».

---

## CODES

- **hotGames vérifiés** :
  - **volleyball-legends** : UPDATE_91 / REPLAYS / MVP — **stable**, pas d'Update 92 (roonby 10/10 + samlover 10/13). verifDate → 15/10.
  - **steal-a-brainrot** : BESTBRAINROTEVER — **stable** (Dexerto 12/10). verifDate → 15/10.
  - **grow-a-garden** : RDCAward / BEANORLEAVE10 — inchangé (seule source datée disponible = juin ; aucune preuve d'expiration). verifDate → 15/10.
  - **steal-an-egg** : **0 code confirmé** — corroboré par Destructoid (12/10, placeId 107778070777162). Page honnête conservée. verifDate → 15/10.
  - anime-vanguards : 8 codes (vérif antérieure 12/10, inchangé).
- **Rotation / catalogVerify** : volleyball-legends, steal-a-brainrot, grow-a-garden, steal-an-egg, blue-lock-rivals, iron-soul-dungeon, anime-expeditions, anime-defenders, anime-vanguards → **2026-10-15**.
- **Codes ajoutés / expirés :** **aucun** (aucun changement de la liste visible — règle d'honnêteté « Mis à jour le » non touchée).
- **Candidats en attente (kill-switch) :** blue-lock-rivals (drop EPICSENDOU/ONEMOREWEEK/NELAIKUNEXT mono-source Dexerto 11/10 ; PCGamer 09/10 + Pocket Tactics 04/10 montrent l'ancien set), iron-soul-dungeon (conflit 3 voies), anime-expeditions, anime-defenders, dig-and-clean (UPDATE3).
- **Sources officielles :** Rockstar Newswire (GTA, rien), EA/FC (FC26).

## SEO

- **Problème détecté / traité :** **bug de confiance systémique** — le bouton « Tout copier » distribuait des codes **périmés** (ou copiait des codes alors que la page affiche « aucun code actif »), sur **68/185 pages**. Mauvais signal qualité + mauvaise expérience joueur. **Correction prioritaire**, sans invention (resync sur la liste visible déjà vérifiée).
- **Cluster travaillé :** intégrité des pages codes (transversal).
- **Intention :** transactionnelle (« codes <jeu> »). **Anti-cannibalisation :** 0 nouvelle URL (UPDATE BEFORE CREATE respecté).
- **Prochaine brique :** éliminer la dette (synchroniser `const ACTIVE` à chaque édition, ou supprimer la duplication).

## NOUVEAUX JEUX

- **Aucun ajouté.** Veille tendances (Steal a Brainrot, Steal an Egg, Dress to Impress, 99 Nights, Fish It) : dominants **déjà couverts**. Aucun net-new ne justifie un cluster sans preuve de traction supplémentaire. Conforme à « pas de contenu pour remplir ».

## CONTENU

- **Guides / tier lists / articles :** aucun (pas de déclencheur confirmé à forte valeur).
- **Mises à jour :** 68 pages codes (resync `const ACTIVE`) + 4 verifDate.

## ANIIMO

- Listes de codes octobre existantes (mein-mmo, primagames, khelnow). Data-driven → maj via `data/aniimo/` + `build_site.py`. **Différé** (hors budget d'édition sûr) ; en queue avec exigence ≥2 sources.

## GTA 6

- **Trailer 3 : TOUJOURS NON SORTI** au 15/10. Uniquement rumeurs d'insiders, **0 confirmation Rockstar**. Sortie nov. 2026 = **RAPPORTÉE**, non reconfirmée. **Aucune édition.** Veille Newswire.

## FC 27 / FC 26

- Titre EA **live = FC 26**. **Divergence de naming** des verticales « FC 27 » → **décision Peter** (rien édité en autonome).

## EDITORIAL INTELLIGENCE

- **Top opportunité traitée :** fix copyAll 68 pages (intégrité/confiance). Trend score interne ~70/100 (impact transversal, risque nul, 0 nouveauté).
- **Tendances :** Steal an Egg / Steal a Brainrot virales (déjà couvertes), aucune émergence net-new exploitable.
- **Articles créés :** 0. **Pages mises à jour :** 68 (+4 verifDate).
- **Sujets ignorés :** rumeurs GTA (non confirmées), drops mono-source (BLR, anime-defenders, anime-expeditions), listes gonflées (décision Peter).
- **À surveiller :** blue-lock drop, iron-soul conflit, 8 pages à liste vide, Aniimo codes, GTA Newswire.

## EDITORIAL QUEUE

- **Urgents :** blue-lock-rivals (2ᵉ source), GTA 6 (veille Newswire).
- **À publier :** rien.
- **À mettre à jour :** iron-soul-dungeon, anime-expeditions, anime-defenders, dig-and-clean, 8 pages vides, Aniimo codes.
- **À préparer / Peter :** naming FC26, jeu de la semaine (§30, marqueurs absents), listes gonflées, dette copyAll.
- **Demain / prochain run :** cf. EDITORIAL-QUEUE.md § PRIORITÉS.

## QC

- **Portée :** 68 pages codes-*.html (resync `const ACTIVE` ← `#activeList`) + 4 verifDate (volleyball-legends, steal-a-brainrot, grow-a-garden, steal-an-egg). Édition surgicale (1 ligne/page), aucune invention de code.
- **Tests :** 185 pages codes → 0 null byte · toutes finissent par `</html>` · déséquilibre `<div>` = 0 sur tout le site · `node --check js/main.js` OK · `data/codes.json` valide (185 jeux / 1279 codes) · `tools/code-watch.json` + `tools/editorial-intelligence.json` JSON valides · `sitemap.xml` + `sitemap-games.xml` XML valides, finissent par `</urlset>`.
- **Builds :** build_site.py (40 URLs games) · build_home.py (5 sections) · build_codes_json.py (inchangé — lit la liste visible, non modifiée) · build_sitemap.py (385 URLs ; lastmod verifDate=185).
- **Note cache JS :** version réelle du site = **v=47** (166 fichiers ; 3 fichiers /avatar/ en v=43, pré-existant, zone à ne pas toucher). CLAUDE.md mentionne encore « v=19 » = doc obsolète. Aucun `<script>` touché ce run.
- **/avatar/ intact · GA4 intact · structure préservée · aucune nouvelle URL.**

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push._
