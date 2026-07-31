# Rapport Zoneblox — 31 juillet 2026 (vendredi)

## (a) Vérification des codes — PRIORITÉ

**Aucun changement réel de codes ce run.** Le run du 30/07 avait déjà fait une vérification approfondie de tous les jeux hot ; contrôle croisé aujourd'hui (web ≥3 sources) → tout cohérent, rien à modifier.

Jeux hot re-vérifiés via sources fiables (Pocket Tactics, Beebom, PGG, GamesRadar, PC Gamer, RoCodes, Roonby, etc.) :

| Jeu | État confirmé | Changement |
|---|---|---|
| Blox Fruits | 23–24 actifs, aucun nouveau code | Aucun |
| Grow a Garden | 2 actifs (RDCAward, BEANORLEAVE10) | Aucun |
| Grow a Garden 2 | 3 actifs (TEAMGREENBEAN, WATERYOPLANTS, REMEMBERTODRINKWATER) | Aucun |
| Blade Ball | 14 actifs (DUNGEONSRELEASE inclus) | Aucun |
| Fisch | 5 actifs (RoamingFishAndWaterPark, Sorry4Delay, scarlet, TemporarySubmarine, CARBON) | Aucun |
| Volleyball Legends | 3 actifs (UPDATE_80, HIDARI_FINALLY, ENCHO_NERF) | Aucun |
| Blue Lock Rivals | 9 actifs (SEMIFINALS/WORLDTOURNAMENTPART3/NEWMAP + 6 anciens) | Aucun |
| Anime Last Stand | ~21 actifs, liste cohérente | Aucun |
| Anime Vanguards | inchangé (Extermination Event Pt.2 déjà reflété) | Aucun |

- **Ligne « 🔄 Vérifié le »** rafraîchie au **31 juillet 2026** sur les **173 pages codes** (idempotent, exactement 1 ligne/page, 0 doublon, 0 null byte). **Aucune** date « Mis à jour le… » ni compteur touché (règle d'honnêteté : pas de changement de codes = pas de changement de date de mise à jour).
- `tools/code-watch.json` : `lastRun` → 2026-07-31 ; `lastChecked` bumpé au 31/07 sur les 9 jeux re-vérifiés + note du jour ; bloc `_pending2026-07-31` ajouté.

**Candidats en attente / à reprioriser au prochain run** : fruit-battlegrounds (paliers récents BIG1M170K!! à réconcilier), anime-rangers-x (~15 codes PGG additionnels à confirmer ≥3 sources), catch-a-monster, dig (conflit persistant → Discord officiel), king-legacy (dormant), world-fighters (sources désynchronisées), squid-game-x. Jeux non-hot du catalogue non revus en profondeur ce run.

## (b) Directeur SEO

- **Trending re-scanné** (web ≥3 sources) : les leaders (Grow a Garden 2, Steal a Brainrot, Brookhaven, Blox Fruits, Animal Hospital) sont **tous déjà couverts**. Aucun nouveau hit ≥4000 joueurs non couvert → priorité à l'approfondissement de cluster. Candidat toujours en veille : « +1 Speed Keyboard Escape » (~500K CCU, obby, probablement sans codes) — à évaluer pour une fiche (Étape 1).
- **Brique de cluster réalisée (J9) : nouveau guide `guides/grow-a-garden-weather.html`** (« Événements météo Grow a Garden », ~1 800 mots).
  - **Intention ciblée** : « grow a garden météo », « weather events grow a garden », « comment déclencher pluie / orage / blood moon ». Intention *how-to météo*.
  - **Anti-cannibalisation** : distincte du guide des mutations (qui liste les multiplicateurs). La page météo explique le **cycle** et **quelle météo déclenche quelle mutation** ; la table des multiplicateurs reste au guide mutations. **Liens réciproques** météo ↔ mutations posés.
  - **EEAT/honnêteté** : encart « info communautaire » (valeurs wiki/Beebom datées, évolutives → renvoi wiki), byline équipe, aucune heure/valeur inventée, renvoi à l'encart évènements accueil pour les admin abuses.
  - **Schema** Article + BreadcrumbList + FAQPage. **Maillage** : carte + ItemList (pos. 46) au hub `guides/index.html` (vraie miniature tr.rbxcdn.com), `sitemap-guides.xml` + `sitemap.xml`, cross-links codes/tier/guide/mutations.
- **Roadmap mise à jour** : J9 marquée faite ; **prochaine brique (J10)** inscrite = value/trading list GAG (si maintenance tenable) OU guide « pets / œufs » GAG ; sinon évaluer « +1 Speed Keyboard Escape ». J8 archivée.

## (c) Autres chantiers

- **Encart évènements** (`data/events.json`) : `meta.updated` → 2026-07-31. Événements récurrents (restocks GAG/GAG2, Saturday Admin Abuse, MAJ hebdo, Taco Tuesday, admin abuses sans horaire) tous encore valides ; aucune `datetime` ponctuelle passée à retirer, aucun nouvel horaire confirmé à promouvoir. Pas de changement d'heure US avant le 2 nov 2026. `js/events.js` non modifié → pas de bump de cache.
- **Jeu de la semaine** : non touché (vendredi ; mise à jour réservée au lundi).
- Aucun nouveau jeu ajouté, aucune tier list / UGC modifiée ce run.

## (d) Fichiers touchés + QC

**Modifiés/créés ce run :**
- `guides/grow-a-garden-weather.html` (nouveau, 1 799 mots)
- `guides/index.html` (carte + ItemList)
- `guides/grow-a-garden-mutations.html` (lien réciproque « météo »)
- `sitemap-guides.xml`, `sitemap.xml` (entrée weather)
- `data/events.json` (meta.updated)
- `tools/code-watch.json` (lastRun + lastChecked + note)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (J9 → J10)
- 173 × `codes/*.html` (ligne « Vérifié le » → 31 juillet 2026)

**QC — tout OK :**
- HTML modifiés se terminent par `</html>`, `<div>`/`<section>` équilibrés, 0 null byte.
- `python3 -c json.load` OK sur `code-watch.json` (33 snapshots, finit par `}`) et `events.json` (17 events, finit par `}`).
- `node --check js/main.js` et `node --check js/events.js` OK.
- `sitemap.xml` / `sitemap-guides.xml` bien formés (finissent par `</urlset>`).
- Cache JS uniforme : **main.js?v=36** sur les 326 pages HTML (`js/main.js` non modifié → pas de bump).
- Nouvelle page : GA4 présent, nav 7 entrées (Avatars inclus), byline EEAT, ≥1200 mots, reliée au hub + sitemaps (aucun orphelin).

> ⚠️ Note technique : un `.git/index.lock` résiduel bloque les écritures git *depuis le sandbox* (permissions). Sans effet sur ta machine Windows ; si `git` refuse un commit, supprime `.git\index.lock` avant de relancer.

---

**Pour publier :** dans le dossier GameNova, lance
`git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`.
Hostinger déploie automatiquement après le push.
