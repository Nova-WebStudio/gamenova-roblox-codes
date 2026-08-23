# Rapport Zoneblox — 23 août 2026 (dimanche)

## (a) Codes vérifiés (priorité absolue)

**Portée :** arbre **servi** `codes-<slug>.html` (les `codes/<slug>.html` sont 301-redirigés → laissés gelés). Jeux chauds (hotGames) revérifiés via web ≥3 sources et/ou sources officielles.

| Jeu | Source(s) | Verdict |
|---|---|---|
| Anime Vanguards | PGG + Beebom (17/08) + GamesRadar (22/08) | Page servie déjà à jour (6 actifs) depuis le 22/08 — cohérente, **inchangée** |
| Volleyball Legends | allthings.how, Beebom, RoCodes, GamesRadar, Fossbytes, Twinfinite, Destructoid | `UPDATE_83 / MIKAGE_REVIVED / SCHOOL_SOON` = set servi → **inchangé** |
| Blue Lock Rivals | PGG, Beebom, GamesRadar, RoCodes, Pocket Tactics | `SAEREWORK / HALFBAKED / RINSOON / SAERRY4DELAY` = **match exact** → inchangé |
| Fisch | GamesRadar, PGG, PCGamer | SCARLET/TemporarySubmarine/CARBON confirmés long-lived ; set servi (6) cohérent → inchangé |
| Blade Ball | Beebom, Pocket Tactics, GamesRadar | 4BVISITS/GIVEMELUCK/SERPENT actifs ; set servi (13) stable → inchangé par prudence |
| Steal a Brainrot | u7buy, Beebom, Dexerto, RoCodes | Sources **en conflit fort** (1 à 23 codes) → **aucun code publié** (prudence) |
| Fruit Battlegrounds, King Legacy | agrégateurs | stables → inchangés |

**Aucun changement de liste de codes ce run** : les jeux chauds avaient déjà été réconciliés au run du 22/08 (Anime Vanguards 16→6 notamment). La règle d'honnêteté est respectée — les dates « Mis à jour le… » et compteurs n'ont **pas** bougé.

**« 🔄 Vérifié le » rafraîchi au 23 août 2026 sur les 176 pages servies** (idempotent, 1 par page).

**Candidats/à prioriser prochain run :** Anime Origins (à ficher avec Chrome), Fruit Battlegrounds & Anime Last Stand (listes actives exactes à reconfirmer). Steal a Brainrot à re-surveiller (conflit persistant).

## (b) Directeur SEO (ÉTAPE 2bis)

**Trending re-scanné (web ≥3 sources) :** leaders (Murder Mystery 2 — pic all-time du mois, couvert ; Grow a Garden/2, Steal a Brainrot, Brookhaven, Anime Expeditions, Animal Hospital) **tous couverts**. Aucun nouveau hit ≥4000 joueurs non couvert (Fusion Piece ~6 joueurs, négligeable).

**Brique de cluster réalisée (nouveau contenu, ÉTAPE 5) :** guide how-to **`guides/grow-a-garden-pets.html`** — « Pets Grow a Garden : œufs, éclosion & meilleurs pets » (~1 656 mots).

- **Intention ciblée :** « grow a garden pets », « meilleurs pets grow a garden », « comment faire éclore œuf grow a garden », « grow a garden eggs guide » (intention *how-to obtention/éclosion*).
- **Anti-cannibalisation :** distincte de la tier list pets GAG2 (classement) et du guide mutations (multiplicateurs) ; aucune page existante ne visait ces head terms. Liens réciproques pets ↔ mutations ↔ tier list pets GAG2.
- **Contenu :** rôle des pets, mécanique d'éclosion (Chicken/Blood Kiwi), types d'œufs, meilleurs pets par objectif (Blood Kiwi/Dragonfly/Golden Bee/Butterfly/Raccoon), stratégie, FAQ 6 Q. Schema Article + BreadcrumbList + FAQPage (validés).
- **EEAT/honnêteté :** byline équipe, encart « communautaire évolutif » (wiki/Beebom/gagdata, daté), aucun taux/valeur inventé.
- **Maillage (anti-orphelin) :** carte au hub `guides/index.html` (vraie miniature tr.rbxcdn.com) + ItemList position 47, lien réciproque depuis `guides/grow-a-garden-mutations.html`, entrées `sitemap-guides.xml` + `sitemap.xml`.
- **Effet :** cluster Grow a Garden = 7ᵉ brique (codes · guide · tier graines · tier pets GAG2 · mutations · météo · **pets how-to**).

**Prochaine brique inscrite dans la roadmap (J15) :** (1) ficher **Anime Origins** avec Chrome ; (2) arbitrage Peter sur l'arbre codes + brique technique ; (3) value/calculateur GAG si maintenance tenable.

## (c) Autres maintenances

- **Encart évènements :** `data/events.json` → `meta.updated` au 23/08/2026. Aucune date ponctuelle passée à purger, aucune heure d'admin abuse confirmée à promouvoir (règle d'honnêteté). `node --check js/events.js` OK (js inchangé → pas de bump cache).
- **Jeu de la semaine :** non concerné (dimanche ; mise à jour le lundi uniquement).
- **UGC, tier lists :** pas de changement requis ce run.

## (d) Fichiers touchés & QC

**Modifiés (183 fichiers suivis) :** 176 pages servies `codes-*.html` (date « Vérifié le »), `guides/index.html` (carte + ItemList), `guides/grow-a-garden-mutations.html` (lien réciproque), `sitemap-guides.xml`, `sitemap.xml`, `data/events.json`, `tools/code-watch.json`, `SEO-directeur-audit-roadmap-2026-07-24.md`.
**Nouveau (non suivi) :** `guides/grow-a-garden-pets.html`.

**QC (tout vert) :**
- Scan intégrité sur les 183 fichiers modifiés + le nouveau guide : **0 null byte**, toutes les pages finissent par `</html>`, sitemaps par `</urlset>`, **équilibre `<div>` intact** (0 déséquilibre).
- `node --check js/main.js` et `node --check js/events.js` OK ; `data/events.json` et `tools/code-watch.json` = JSON valide.
- Nouveau guide : 1 656 mots FR, GA4 présent, nav 7 entrées (incl. Avatars + À propos), 3 blocs JSON-LD valides, vraie miniature tr.rbxcdn.com.
- `js/main.js` **non modifié** → pas de bump de version cache nécessaire.

**⚠️ Bloquant à traiter côté Peter :** un fichier résiduel **`.git/index.lock`** est présent et **impossible à supprimer depuis l'environnement** (permission refusée sur le mount). Il **bloquera `git add`/`commit`**. Le supprimer d'abord :

```
del .git\index.lock
```

## Pour publier

Dans le dossier GameNova, lance :

```
del .git\index.lock
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
