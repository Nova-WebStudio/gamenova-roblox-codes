# Rapport Zoneblox — 22 septembre 2026 (mardi, run éditorial du soir ~18h45)

> Run **off-cycle** (entre les fenêtres 15h et 22h). Mode **Editorial Intelligence** léger : pas de maintenance technique complète, pas de rotation complète des codes, pas de QC de tout le site. Le run 05h de ce matin a déjà traité les codes en profondeur et publié son rapport (`rapport-zoneblox-2026-09-22.md`).

## 🕒 Nouveautés depuis 05h

Rien de rupture. Le paysage est stable par rapport au run du matin :
- **FC 27** (J-3) : lancement mondial confirmé **25 sept.** ; accès anticipé live depuis le 18. Contenu de lancement précisé côté sources : Season 1 **Ones to Watch** (17 sept.→22 oct.), **Destined for Glory** (démarre 25 sept., **Mbappé** en tête + Rogers, Fernandes, Isak, Mbeumo), TOTW 1-2, SBC d'accès anticipé.
- **GTA 6** : date **19 nov. 2026** stable. Deux nouveautés confirmées **mineures** : annonce officielle de **« GTA VI: The Album »** et stunt marketing **« Welcome to Vice City »** (lettres géantes, Kaseya Center de Miami, ~1M$).
- **Aniimo** : MAJ **17 sept.** (fix bugs quêtes/graphismes) + nouvelle créature **Prismana Glynsera**. 11 codes actifs (déjà couverts et sourcés chez nous).
- **Roblox** : **Steal An Egg** reste #1 (~1,7M). Aucun nouveau hit ≥4000 non couvert. Rappel plateforme : **Roblox Everywhere** (annonce 11 sept.).

## 🔥 Top opportunités (max 5)

1. **Aniimo — fraîcheur codes + créature Prismana Glynsera** (UPDATE, run 05h) : rafraîchir `lastChecked`, passer 9 badges `new` périmés à `false`, ajouter la créature à `creatures.json`, puis `build_site.py`.
2. **FC 27 — enrichir le détail de lancement** (UPDATE post-25 sept.) : promos Season 1 dans `data/fc-27/updates.json`.
3. **GTA 6 — actus marketing** (À PRÉPARER, faible priorité) : The Album + stunt Miami ; ne rien créer, éventuelle ligne actus evergreen seulement.
4. *(veille)* type-soul — trancher PGG 64 vs Beebom 7.
5. *(veille)* Steal a Brainrot — codes de spawn éphémères, ne pas publier.

## 🆕 Nouveaux jeux

Aucun. Trend detector : aucun hit émergent non couvert au 22 sept.

## 📰 News

Aucun article créé. **Décision éditoriale : ne rien publier ce soir.** Aucun sujet ne réunit confirmation solide + valeur joueur nette + absence de page équivalente. Les items nouveaux (GTA 6 The Album/stunt, FC 27 promos futures, Aniimo créature) sont soit mineurs, soit non encore live, soit relèvent d'un UPDATE au run 05h. Kill switch éditorial appliqué ; « update before create » respecté.

## 🛠️ Pages à mettre à jour

Voir la queue. Aucune édition de page HTML ce soir (build_site réservé au run 05h ; risque > bénéfice en off-cycle pour de la fraîcheur de badge).

## 👀 À surveiller

Steal a Brainrot (spawn codes) · type-soul · sailor-piece · grow-a-chicken-fighter · character-rng · broken-blade · candidats `_pending2026-09-22` · Steal An Egg (ajout d'un système de codes ?) · Aniimo (prochains patchs).

## 📋 Editorial Queue — changements depuis le dernier passage

**Nouveauté structurelle** : création des deux fichiers de mémoire éditoriale requis par le spec V2 (ils n'existaient pas encore) :
- `EDITORIAL-QUEUE.md` (racine) — file opérationnelle (URGENT / À PUBLIER / À METTRE À JOUR / À PRÉPARER / À SURVEILLER / PRIORITÉS DEMAIN).
- `tools/editorial-intelligence.json` — 6 sujets suivis (fc27-launch, gta6-release, aniimo-codes, steal-a-brainrot-spawn, roblox-everywhere, steal-an-egg) avec statut, confiance, sources, trendScore, prochaine action.

Aucun sujet obsolète à retirer (première édition).

## ✅ QC

- `editorial-intelligence.json`, `code-watch.json`, `data/aniimo/codes.json` : **JSON valides**.
- `EDITORIAL-QUEUE.md` + `editorial-intelligence.json` : **0 null byte**.
- **Aucun fichier HTML du site modifié** ce run → pas de contrôle `</html>`/div/cache nécessaire.
- 2 fichiers nouveaux non suivis (voir git).

## ⚠️ Note technique

Un fichier `.git/index.lock` résiduel a été détecté en début de run (« unable to unlink … Operation not permitted »). Les commandes `git status`/`git log` fonctionnent ; le lock semble s'être libéré ensuite. Si un `git commit` échoue côté Peter avec « Unable to create index.lock », supprimer manuellement `GameNova/.git/index.lock`.

## 🌅 Priorités du prochain run 05h (mercredi 23 sept.)

1. Codes (priorité absolue) : hotGames + rotation ; trancher les « à revérifier ».
2. Aniimo : appliquer l'UPDATE (badges `new` + créature Prismana Glynsera) + `build_site.py`.
3. FC 27 (J-2) : vérifier la couverture du contenu d'accès anticipé, préparer le post-lancement.
4. Directeur SEO : généralisation du CTA `data-cta="guidelink"` (brique J36).
5. Régénération dans l'ordre : build_site → build_home → build_codes_json (si codes changés) → build_sitemap.

---

**Pour publier :** dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push.
