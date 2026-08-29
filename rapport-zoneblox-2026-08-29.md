# Rapport Zoneblox — 29 août 2026 (samedi)

## (a) Codes vérifiés (PRIORITÉ)

**Méthode :** re-scan multi-sources sur les jeux chauds (`tools/code-watch.json > hotGames`) via pcgamesn, gamesradar, progameguides, beebom, pcgamer + recoupement avec l'état vérifié du 28/08.

**Résultat : tout est STABLE — aucun changement de code appliqué aujourd'hui.** L'état est identique à celui vérifié hier (28/08), ce qui est cohérent pour un dimanche/week-end à faible churn.

| Jeu | Codes servis | Vérification 29/08 |
|-----|--------------|--------------------|
| Blox Fruits | 24 actifs (dont Lightningabuse, EASTEREXP) | ✅ Sync avec pcgamesn (MAJ 28/08). « Chandler » (=rien) volontairement non ajouté. |
| Blue Lock Rivals | 6 (INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!!) | ✅ Match exact PC Gamer (28/08). |
| Volleyball Legends | 3 (UPDATE_84, SEASON_18, PIRATE_SZN) | ✅ Match gamesradar/progameguides. |
| Grow a Garden | 2 (RDCAward, BEANORLEAVE10) | ✅ Confirmés actifs. |
| Fruit BG, King Legacy, Fisch, Blade Ball, Anime Vanguards | inchangés | ✅ Aucune info contradictoire ≥3 sources. |

**Candidat « en attente » (conflit, prudence) :**
- **Grow a Garden — `torigate`** (Whispering Torii) : la fiche zoneblox le classe **expiré**, mais 4 sites (pcgamesn, gamesradar, progameguides, beebom) le listent encore « actif ». Ces sites gardent souvent des codes cosmétiques d'event périmés → **gardé expiré par prudence** (ne pas afficher un code potentiellement mort comme actif). Consigné dans `code-watch.json > _pending2026-08-29`. À retester si GAG relance l'event.

**« 🔄 Vérifié le »** rafraîchi au **29 août 2026** sur les **177 pages codes servies** (idempotent, 1 par page, via `id="verifDate"`).

**Jeux non re-vérifiés en profondeur ce run (à prioriser) :** le gros du catalogue « non-hot » (RNG, tycoons, obby…) n'a pas fait l'objet d'un re-scan web individuel ; couvert par le rafraîchissement de date. Prioriser au prochain run les jeux hot restants (Steal a Brainrot — très volatil, Anime Last Stand, Pet Sim 99).

## (b) DIRECTEUR SEO (ÉTAPE 2bis)

- **Trending re-scanné :** aucun nouveau hit Roblox ≥4000 joueurs non couvert → poursuite de l'evergreen.
- **Brique réalisée (cluster Anime Origins) :** nouvelle **`tier-list/anime-origins.html`** (~1 910 mots FR).
  - **Intention ciblée :** « anime origins tier list / meilleures unités » (classement) — **distincte** de la fiche codes (transactionnelle). Le report récurrent « ficher Anime Origins » (J17→J19) était **obsolète** : `codes-anime-origins.html` existe déjà.
  - **Anti-cannibalisation :** aucune page existante ne visait cette intention ; liens croisés codes↔tier list posés dans les deux sens.
  - **Information gain :** classement complet **SS→C (51 unités)** d'après Pocket Tactics (20/08/2026), write-ups FR des 13 unités SS+S, section **meilleurs traits**, meilleure équipe, conseils débutants, FAQ 5 Q. Schema **ItemList + BreadcrumbList + FAQPage** (3 blocs valides).
  - **EEAT/honnêteté :** byline « L'équipe Zoneblox », source datée recoupée (Pocket Tactics + Sportskeeda + Pro Game Guides), caveat « noms d'unités variables selon les sites », rien d'inventé.
  - **Maillage (anti-orphelin) :** carte hub `tier-lists.html` (vraie miniature tr.rbxcdn.com), `sitemap-tier-list.xml` + `sitemap.xml`, bouton hero croisé sur `codes-anime-origins.html`.
- **Cluster Anime Origins :** fiche codes ✓ · tier list ✓ · guide ✗.
- **Prochaine brique inscrite (J20) :** `guides/anime-origins.html` (guide complet, clôt le cluster). Roadmap `SEO-directeur-audit-roadmap-2026-07-24.md` mise à jour (J19 = dernière brique, J18 archivé).

## (c) Autres maintenances

- **Jeux ajoutés :** aucun (aucun nouveau hit ≥4000 non couvert).
- **Tier lists :** 1 nouvelle (`tier-list/anime-origins.html`). **Guides :** aucun. **UGC :** non modifié.
- **Encart évènements (`data/events.json`) :** non touché (encart retiré de l'accueil le 24/08 ; JSON laissé valide).
- **Jeu de la semaine :** N/A (mise à jour le lundi ; aujourd'hui = samedi).

## (d) Fichiers touchés & QC

**Nouveaux / modifiés à publier :**
- **`tier-list/anime-origins.html`** (nouveau, ~1 910 mots, 3 JSON-LD valides)
- `tier-lists.html` (carte Anime Origins, vraie miniature)
- `codes-anime-origins.html` (bouton hero « 📊 Tier list »)
- `sitemap.xml`, `sitemap-tier-list.xml` (URL tier list)
- **177 × `codes-*.html`** (« Vérifié le » → 29/08)
- `data/codes.json` (régénéré : 177 jeux, 1228 codes actifs)
- `tools/code-watch.json` (lastRun + candidat en attente `torigate`)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (roadmap J19→J20)

**QC (tout OK) :**
- ✅ Toutes les pages HTML modifiées finissent par `</html>`, `<div>` équilibrés (0), **0 null byte**, GA4 (G-FEL71QVHNL) présent.
- ✅ `sitemap.xml` / `sitemap-tier-list.xml` = XML bien formé, finissent par `</urlset>`.
- ✅ `data/codes.json` + `tools/code-watch.json` + `data/events.json` = JSON valides.
- ✅ Tier list Anime Origins : 3 blocs JSON-LD valides, ~1 910 mots, nav 7 entrées (dont Avatars), `main.js?v=39`.
- ✅ **Cache JS :** `js/main.js` **non modifié** → reste `v=39`, aucun bump nécessaire (les pages `codes-*.html` plates utilisent un JS inline, sans main.js).
- ℹ️ Note : les fichiers dépréciés `codes/<slug>.html` (sous-dossier redirigé 301) n'ont **pas** été touchés ce run — seul l'arbre servi (`codes-<slug>.html`) l'a été.

⚠️ **`.git/index.lock` résiduel présent** (comme au run précédent) — il **bloquera le commit**. Le supprimer d'abord.

---

Pour publier : dans le dossier GameNova, **supprime d'abord `.git/index.lock`** (`del .git\index.lock` sous Windows), puis lance  `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main` . Hostinger déploie automatiquement après le push.
