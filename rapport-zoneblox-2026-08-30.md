# Rapport Zoneblox — 30 août 2026 (dimanche)

## (a) Codes vérifiés (PRIORITÉ)

**Méthode :** re-scan multi-sources sur les jeux chauds (`tools/code-watch.json > hotGames`) via gamesradar, progameguides, beebom, pcgamer, pcgamesn, twinfinite, roonby, dexerto + recoupement avec l'état vérifié du 29/08.

**1 changement de codes appliqué aujourd'hui : Volleyball Legends → Update 85.**

| Jeu | Codes servis | Vérification 30/08 |
|-----|--------------|--------------------|
| **Volleyball Legends** | **UPDATE_85, SHIRO, BLOCKED** (3 actifs) | ✅ **Changement** : Update 85 fait tourner la liste. Confirmé ≥4 sources (gamesradar, progameguides, twinfinite, roonby « UPDATE 85 »). Anciens **UPDATE_84 / SEASON_18 / PIRATE_SZN** passés en **expirés** (compteur 15→18, prose MAJ au 30/08). |
| Blue Lock Rivals | 6 (INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!!) | ✅ Match exact sources (gamesradar/PC Gamer/progameguides). Inchangé. |
| Steal a Brainrot | 1 (BESTBRAINROTEVER) | ✅ Confirmé actif « throughout August » (gamesradar, dexerto, beebom). Inchangé. |
| Grow a Garden | 2 (RDCAward, BEANORLEAVE10) | ✅ Toujours actifs (pcgamesn/progameguides/beebom). Inchangé. |
| Blox Fruits | 24 servis (incl. Lightningabuse, KITT_RESET, Bignews) | ✅ Aucune expiration confirmée ≥3 sources. Inchangé. |
| Fisch, Blade Ball, Anime Vanguards, King Legacy, Fruit BG, Anime Last Stand | inchangés | ✅ Aucune info contradictoire ≥3 sources. |

**Candidats « en attente » (conflit / prudence, consignés dans `code-watch.json > _pending2026-08-30`) :**
- **Grow a Garden — `FREESEED`** : ajouté le 23/08 mais **rapporté glitché** (invites qui ne s'enregistrent pas) → non publié par prudence, à retester.
- **Blox Fruits — `1LOSTADMIN`** : mentionné par **1 seule source** (recap web) → besoin ≥3 sources ou officiel avant publication.
- **Grow a Garden — `torigate`** : report du 29/08 (zoneblox=expiré vs sites=actif), gardé expiré.

**« 🔄 Vérifié le »** rafraîchi au **30 août 2026** sur les **177 pages codes servies** (idempotent, 1 par page, via `id="verifDate"`). `data/codes.json` régénéré (`tools/build_codes_json.py`) : **177 jeux, 1228 codes actifs**.

**Jeux non re-vérifiés en profondeur ce run (à prioriser) :** le catalogue « non-hot » (RNG, tycoons, obby…) n'a pas fait l'objet d'un re-scan web individuel — couvert par le rafraîchissement de date. Prioriser au prochain run : Anime Last Stand (volatil), Pet Sim 99, Fisch.

## (b) DIRECTEUR SEO (ÉTAPE 2bis)

- **Trending re-scanné :** leaders vérifiés contre le catalogue (Steal An Egg #1 ~1,4M CCU, Murder Mystery 2, Brookhaven, Grow a Garden, +1 Speed Keyboard Escape [couvert = `evasion-clavier`], Anime Expeditions) → **aucun nouveau hit ≥4000 non couvert**. On clôt le cluster evergreen.
- **Brique réalisée (cluster Anime Origins — guide complet, 3ᵉ pièce) :** nouveau **`guides/anime-origins.html`** (~2 250 mots FR, gabarit `guides/anime-last-stand.html`).
  - **Intention ciblée :** *how-to* (« guide / comment évoluer / meilleure équipe / comment farmer Anime Origins ») — **distincte** de la fiche codes (transactionnelle) et de la tier list (classement). Anti-cannibalisation : aucune page existante ne visait cette intention.
  - **Information gain :** TOC 8 sections ; ordre de progression optimal (Story→Hard→Legend Stages→Challenges→évolution→modes avancés) ; route d'évolution Vegita ; **3 tableaux** (équipe débutant 6 rôles, priorités ressources, modes avancés Raids/Rifts/Infinite Mansion/World Bosses) ; 8 erreurs à éviter ; FAQ 5 Q. Schema **Article + BreadcrumbList + FAQPage** (valides).
  - **EEAT/honnêteté :** byline « L'équipe Zoneblox », sources datées recoupées (Pocket Tactics 20/08 + Pro Game Guides + Sportskeeda + guide débutant LDPlayer 26/08), caveat d'évolutivité, rien d'inventé.
  - **Maillage (anti-orphelin) :** carte hub `guides.html` + `guides/index.html` (ItemList pos. 45, map CATS, vraie miniature tr.rbxcdn.com) ; `sitemap-guides.xml` + `sitemap.xml` ; **liens croisés bidirectionnels** codes ↔ tier list ↔ guide (boutons hero ajoutés sur `codes-anime-origins.html` et `tier-list/anime-origins.html`).
- **Cluster Anime Origins : COMPLET** — fiche codes ✓ · tier list ✓ · guide complet ✓.
- **Prochaine brique inscrite (J21) :** cluster **Volleyball Legends** (tier list ou guide dédié — fiche codes très active mais pas de tier/guide). Roadmap `SEO-directeur-audit-roadmap-2026-07-24.md` mise à jour (J20 = dernière brique, J19 archivé).

## (c) Autres maintenances

- **Jeux ajoutés :** aucun (aucun nouveau hit ≥4000 non couvert).
- **Tier lists :** aucune nouvelle (bouton guide ajouté sur `tier-list/anime-origins.html`). **Guides :** 1 nouveau (`guides/anime-origins.html`). **UGC :** non modifié.
- **Encart évènements (`data/events.json`) :** non touché (encart retiré de l'accueil ; JSON laissé valide).
- **Jeu de la semaine :** N/A (mise à jour le lundi ; aujourd'hui = dimanche).

## (d) Fichiers touchés & QC

**Nouveaux / modifiés à publier :**
- **`guides/anime-origins.html`** (nouveau, ~2 250 mots, 3 JSON-LD valides, nav 7 entrées, `main.js?v=39`)
- `guides.html` + `guides/index.html` (carte Anime Origins, vraie miniature ; ItemList + CATS)
- `codes-anime-origins.html` + `tier-list/anime-origins.html` (bouton hero « 📖 Guide complet »)
- `codes-volleyball-legends.html` (codes actifs UPDATE_85/SHIRO/BLOCKED, 3 expirés ajoutés, prose MAJ 30/08)
- `sitemap.xml`, `sitemap-guides.xml` (URL guide)
- **177 × `codes-*.html`** (« Vérifié le » → 30/08)
- `data/codes.json` (régénéré : 177 jeux, 1228 codes actifs)
- `tools/code-watch.json` (lastRun + candidats en attente)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (roadmap J20→J21)

**QC (tout OK) :**
- ✅ Scan d'intégrité sur les **185 fichiers modifiés + le nouveau guide** : tous finissent par `</html>` / `</urlset>`, `<div>` équilibrés (0), **0 null byte**, GA4 (G-FEL71QVHNL) présent sur chaque page.
- ✅ `node --check js/main.js` et `node --check js/events.js` réussissent.
- ✅ `data/codes.json`, `tools/code-watch.json`, `data/events.json` = JSON valides ; `sitemap.xml` / `sitemap-guides.xml` = XML bien formé.
- ✅ **Cache JS :** `js/main.js` **non modifié** → reste `v=39`, aucun bump nécessaire.
- ℹ️ Les fichiers dépréciés `codes/<slug>.html` (sous-arbre 301) n'ont pas été touchés — seul l'arbre servi (`codes-<slug>.html`) l'a été.

⚠️ **`.git/index.lock` résiduel présent** (comme aux runs précédents) — il **bloquera le commit**. Le supprimer d'abord (`del .git\index.lock` sous Windows) — je ne peux pas le supprimer moi-même.

---

Pour publier : dans le dossier GameNova, **supprime d'abord `.git/index.lock`** (`del .git\index.lock`), puis lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
