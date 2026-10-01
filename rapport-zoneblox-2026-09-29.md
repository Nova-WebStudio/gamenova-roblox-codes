# Rapport ZoneBlox — 2026-09-29 (run 05h, mardi)

> Full maintenance + editorial. **Run interrompu ~05h15 par une déconnexion du PC** (bridge coupé), puis **repris et terminé** après reconnexion. Toutes les modifs ci-dessous sont sur disque, régénérées et QC-validées. **Rien n'est poussé sur Git (push manuel).**

## 🔎 Découverte majeure du jour — bug systémique « chips vs tableau mort »

Sur les pages `codes-*.html`, les codes réellement **affichés** aux joueurs (et lus par `build_codes_json.py` pour le widget partenaire) sont les **chips HTML statiques** dans `<div id="activeList">`. Le tableau JavaScript `const ACTIVE=[...]` présent plus bas est du **code mort** : les blocs `// render active codes` / `// render expired` sont **vides**, donc ce tableau n'est jamais rendu.

Conséquence : des runs précédents ont parfois mis à jour la **prose**, le **compteur du hero** et ce **tableau mort**, mais **pas les chips** → certaines pages affichaient de vieux codes périmés tout en prétendant (prose/compteur) être à jour. **Règle actée (code-watch.json) : toujours se fier aux chips `data-code`, jamais au tableau JS.** Un audit chips-vs-compteur sur les 184 pages donne **0 incohérence** après corrections.

## CODES

### Corrections réelles (chips périmés → codes confirmés)
- **volleyball-legends** : Update 88 (UPDATE_88/GET_SLIMED/XP_BOOST, périmés) → **Update 89 : UPDATE_89, WE_CURSED, SKELETON**. Sources : **Twinfinite + Destructoid (28 sept)**. Prose, compteur (3), verifDate MAJ.
- **sols-rng** : 8 chips périmés (GargantuaBiome, RaidCH2, AnotherRealmCH2, word9999aura, word999aura, 2026ValentineDay, transform, AmalgamationHELL) → **3 confirmés : SRY4DEALY, UPD20260905, UPD20260919**. Sources : **Pocket Gamer (26 sept) + Dexerto (21 sept)**. Compteur 8→3, verifDate 29.
- **blue-lock-rivals** : chips déjà corrects (**SNUFFYUPD, NEWMASTER, UBERSVOTE, WSNUFFY**, confirmés PGG 26 + Beebom 26 + Twinfinite 28). Tableau JS mort resynchronisé + verifDate 29.

### Revérifiées, aucun changement de codes (verifDate → 29)
- **anime-vanguards** (22) = Pocket Tactics 27 (match exact).
- **blade-ball** (15) = Pocket Tactics 22 (14) + DUNGEONSRELEASE conservé (Beebom, pas de preuve d'expiration).
- **fruit-battlegrounds** (4 : EVENHIGHER!, OMGUPDATE22, HIGHER1M120K, YOO1M110K!) = Pocket Tactics 22 (match exact).
- **grow-a-garden** (2 : RDCAward, BEANORLEAVE10) = Pocket Gamer 5 + Beebom 1 (FREESEED/STORY/STARBUD = source unique PGG → non ajoutés).
- **steal-a-brainrot** (1 : BESTBRAINROTEVER) = GamesRadar.
- **anime-last-stand** (3 : MagicKnights!, ElfReincarnation!, IsItReallyWeekly?!) — **tiebreak résolu** : PGG + Beebom listent exactement ces 3 en « recently added » ; les 38 extras de Beebom sont des codes expirés non nettoyés.

### Rotation catalogue
- **ro-ghoul** : verifDate 29. Sous-listé (5 chips vs ~68 chez Pocket Gamer) mais 4/5 confirmés actifs, **aucun faux-actif** → conservé (jeu à codes permanents `!code`).
- `catalogVerify` MAJ (2026-09-29) pour : sols-rng, ro-ghoul, volleyball-legends, blue-lock-rivals, anime-vanguards, blade-ball, grow-a-garden, steal-a-brainrot, fruit-battlegrounds, anime-last-stand.

### Candidats / conflits laissés en attente
- **grow-a-garden** : FREESEED / STORY / STARBUD / torigate (PGG 17 seul, absents de PG 5 + Beebom 1) → à trancher avec 2e source.
- **fruit-battlegrounds** : EVENHIGHER! (PT seul), MILLI90SWAG (PG seul) = 1-source.

## SEO
- Aucune nouvelle URL créée (kill switch). Priorité à la **fiabilité des pages codes existantes** (correction de codes périmés affichés = gain de confiance/fraîcheur SEO direct).
- `sitemap.xml` régénéré : 383 URLs, lastmod issus de verifDate (184), Mis à jour (11), mtime (188).

## NOUVEAUX JEUX
- Aucun ajout. RELL Seas / Roblox Fall Games Preview = MONITOR (pas de traction+codes+page manquante réunis).

## CONTENU
- Aucun guide / tier list / article créé (kill switch, « 2 excellents > 20 faibles »).

## ANIIMO (data-driven)
- 11 codes reconfirmés (**GamesRadar 23 + Pocket Tactics 25**). `aniimoparty` **EXCLU** (conflit : PT actif / GamesRadar expiré). `data/aniimo/codes.json` lastChecked → 2026-09-29. `build_site.py` relancé.

## GTA 6
- Reveal **Game Informer** (dossier 14 pages, 12 screenshots, système météo + Leonida) programmé le 29 sept **mais NON publié à l'heure du run** (embargo). Seuls déjà publics : Jason/Lucia, Miami/Floride, météo/faune. **Page evergreen inchangée** (kill switch). **URGENT maintenu** pour les runs 15h/22h : dès parution → UPDATE evergreen (screenshots + détails), pas de nouvelle URL. Sortie confirmée **19 nov 2026**.

## FC 27
- Monitor. Post-lancement, promos Saison 1 connues, rien de concret (SBC/promo) justifiant une page aujourd'hui.

## EDITORIAL INTELLIGENCE
- **Top action du jour** : correction de 2 pages hot affichant des codes périmés (volleyball-legends, sols-rng) — impact joueur direct.
- Tendances : Grow a Garden / Steal a Brainrot dominent (couverts). RELL Seas à venir (monitor).
- Articles créés : 0. Pages mises à jour : 3 corrections codes + 7 revérifications. Sujets ignorés : Fall Games Preview, marketing GTA 6 (faible valeur joueur). À surveiller : reveal GTA 6, aniimoparty, grow-a-garden extras.
- `tools/editorial-intelligence.json` : meta MAJ 2026-09-29, topic GTA6 → MONITOR + note reveal.

## EDITORIAL QUEUE
- `EDITORIAL-QUEUE.md` régénéré (voir fichier). URGENT : GTA 6. À publier : rien. À mettre à jour : poursuite rotation. À préparer : FC27, Aniimo, RELL Seas. Demain : GTA 6 reveal, hotGames, grow-a-garden tiebreak, rotation des plus anciens.

## QC
- `node --check js/main.js` : OK.
- `data/codes.json` (184 jeux, 1269 codes) + `data/aniimo/codes.json` : JSON valides.
- `sitemap.xml` (383 URLs) + `sitemap-games.xml` : XML valides, `sitemap.xml` finit par `</urlset>`.
- Pages codes modifiées : toutes finissent par `</html>`, 0 null byte, GA4 `G-FEL71QVHNL` présent, div équilibrés (0 fichier déséquilibré).
- Cache JS : site en `main.js?v=47` (165 fichiers). Les 3 fichiers en `v=43` sont sous `/avatar/` = **section protégée, non modifiée** (règle CLAUDE.md).
- Observation (hors périmètre) : `codes-sols-rng.html` et `codes-ro-ghoul.html` ne chargent pas `main.js` et n'ont pas de bandeau `data-cta="guidelink"` (structure ancienne) — fonctionnelles (chips + copie inline OK), à harmoniser un jour.

## Incident technique
- Le PC (bridge Cowork) s'est déconnecté ~05h15 en plein run. Reprise auto planifiée ×3 ; le PC est revenu et le run a été **terminé intégralement**. Peter a été notifié pendant l'interruption.

---

**Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.**
