# Rapport Zoneblox — 26 août 2026 (mercredi)

## (a) Codes vérifiés (priorité absolue)

**Portée :** arbre servi `codes-<slug>.html`. Jeux chauds revérifiés via web (≥3 sources fiables : PCGamesN, PC Gamer, GamesRadar, PGG, Pocket Tactics, Beebom, Dexerto, Twinfinite…) et sources officielles quand disponibles.

| Jeu | Source(s) | Verdict |
|---|---|---|
| **Blue Lock Rivals** | PCGamesN (23/08) + PC Gamer + GamesRadar + PGG | **CHANGEMENT** : rotation U20 Rin Rework — anciens actifs (SAEREWORK, HALFBAKED, RINSOON, SAERRY4DELAY) **expirés**, remplacés par **6 nouveaux** : INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!! (pill 4→6, date + intro maj) |
| **Volleyball Legends** | GamesRadar + Beebom + Twinfinite + RoCodes | **CHANGEMENT** : Update 84 fait tourner la liste — UPDATE_83/MIKAGE_REVIVED/SCHOOL_SOON **expirés** → **UPDATE_84, SEASON_18, PIRATE_SZN** (3 actifs, date + intro maj) |
| **Anime Vanguards** | GamesRadar + Pocket Tactics + PGG | **CHANGEMENT** : `Miniupdate1` **expiré le 23/08** (past sa date annoncée) → retiré (pill 5→4). Restent Prepare, 1DayDelay, 25thHour, LetTheLarpingBegin |
| Blox Fruits | PCGamesN (21/08) | Liste servie (24 codes) = liste PCGamesN (sauf « Chandler » = rien, exclu à raison) → **inchangé** |
| Grow a Garden | Pocket Tactics + Pocket Gamer + Beebom | RDCAward + BEANORLEAVE10 confirmés actifs → **inchangé** |
| Steal a Brainrot | Beebom (1) vs autres (23) | Conflit fort persistant → set servi `BESTBRAINROTEVER` conservé (prudence) → **inchangé** |
| Grow a Garden 2 | — | `FREESEED` toujours **en attente** (non reconfirmé) → non publié |

**« 🔄 Vérifié le » rafraîchi au 26 août 2026 sur les 177 pages servies** (idempotent, 1 par page). Date accueil `index.html` (`const TODAY` + `#todayDate`) passée à **26 août 2026** (aucune trace résiduelle du bug « 23 juillet »).

**Candidats / à prioriser prochain run :** GAG2 `FREESEED` (à reconfirmer) ; Steal a Brainrot (conflit à re-surveiller) ; Anime Origins (fiche déjà présente, RAS). **Non revus ce run** (à couvrir en priorité aux prochains) : le gros du catalogue evergreen non-« hot » (aucune dégradation, dates rafraîchies).

## (b) Directeur SEO (ÉTAPE 2bis)

**Trending re-scanné (web) :** Murder Mystery 2 (~1M CCU, couvert), **Steal An Egg** (#1 trending ~724K CCU, couvert), +1 Speed Keyboard Escape (~500K CCU, **déjà couvert** sous le slug FR `evasion-clavier`), Anime Expeditions (couvert). **Aucun nouveau hit ≥4000 non couvert** → approfondissement du cluster porteur.

**Brique réalisée :** nouvelle **`tier-list/steal-an-egg.html`** (~2 317 mots FR).
- **Intention distincte (anti-cannibalisation) :** « steal an egg tier list » / « meilleur pet steal an egg » — classement, distinct de la fiche codes du même jeu ; aucune tier list existante ne visait ce jeu.
- **Information gain :** classement S/A/B **par revenu/seconde** (Unicorn Divine ~1 Md/s → dragons Eternal → paliers Legendary réalistes), **tableau meilleur pet par biome** (Forest→Cosmic), section début de partie, encart honnêteté mutations (multiplicateurs non publiés), section Rebirth, FAQ 5 Q. Schema ItemList + Breadcrumb + FAQPage.
- **EEAT :** byline « L'équipe Zoneblox », sources datées (index IGN via timesaver.gg 21–24/08 + corroboration bloxspot/stealthygaming/ldplayer/eldorado), distinction officielle / communautaire / non publié.
- **Maillage :** carte + ItemList du hub `tier-list/index.html` (vraie miniature tr.rbxcdn.com), `sitemap-tier-list.xml` + `sitemap.xml`, liens croisés fiche ↔ tier list.

**Bonus :** ajout du bandeau CTA `data-cta="guidelink"` qui **manquait** sur `codes-steal-an-egg.html`.

**Prochaine brique (J18) inscrite dans la roadmap :** guide complet Steal An Egg (`guides/steal-an-egg.html`) — 3ᵉ brique du cluster (fiche ✓ · tier list ✓ · guide à faire).

## (c) Autres maintenances

- **Jeu de la semaine :** mercredi → non touché (mise à jour le lundi uniquement).
- **Encart évènements :** retiré (demande de Peter du 24/08) → ÉTAPE 6bis désactivée, non touchée.
- **UGC, guides, autres tier lists existantes :** pas de changement requis ce run.

## (d) Fichiers touchés & QC

**Modifiés (codes) :** 174 pages `codes-*.html` (« Vérifié le » 24→26 août) + `codes-blue-lock-rivals.html`, `codes-volleyball-legends.html`, `codes-anime-vanguards.html` (listes de codes + pill + intro + date), `codes-steal-an-egg.html` (bandeau CTA + lien tier list).
**Modifiés (SEO/maillage) :** `tier-list/index.html` (carte + ItemList), `sitemap-tier-list.xml`, `sitemap.xml`, `index.html` (TODAY), `tools/code-watch.json` (snapshots), `SEO-directeur-audit-roadmap-2026-07-24.md`.
**Nouveaux :** `tier-list/steal-an-egg.html`, ce rapport.
> À noter : le worktree contenait déjà les modifications non commitées du run du 24/08 (bump cache `main.js?v=38→v=39` sur 326 HTML). Elles seront incluses dans le prochain commit.

**QC (tout vert) :**
- Scan d'intégrité sur les **512 fichiers suivis modifiés** : **0 null byte**, toutes les pages finissent par `</html>`, sitemaps par `</urlset>`, **équilibre `<div>` intact** (0 déséquilibre).
- `node --check js/main.js` OK ; `tools/code-watch.json` = JSON valide.
- Cache JS **uniforme v=39** (327 refs, 0 en v=38). js/main.js non modifié ce run → pas de bump.
- Nouvelle tier list : 2 317 mots FR, GA4 présent, nav 7 entrées (Avatars inclus), 3 JSON-LD valides, miniature réelle tr.rbxcdn.com, canonical/og cohérents, aucun rédactionnel anglais.
- `codes-steal-an-egg.html` : exactement **1** bandeau `data-cta="guidelink"`.

## Pour publier

Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.

Sources : [PCGamesN Blue Lock Rivals](https://www.pcgamesn.com/blue-lock-rivals/codes) · [PCGamesN Volleyball Legends](https://www.gamesradar.com/games/sports/volleyball-legends-codes/) · [PCGamesN Anime Vanguards](https://www.pcgamesn.com/anime-vanguards/codes) · [PCGamesN Blox Fruits](https://www.pcgamesn.com/blox-fruits/codes) · [Pocket Tactics Grow a Garden](https://www.pockettactics.com/grow-a-garden-codes) · [timesaver.gg Steal An Egg best pets](https://timesaver.gg/blog/steal-an-egg-best-pets)
