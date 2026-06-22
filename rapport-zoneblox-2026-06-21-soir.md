# Rapport Zoneblox — dimanche 21 juin 2026 (soir)

Second run de maintenance du jour. Dimanche (`date +%u` = 7) → **pas de « Jeu de la semaine »** (réservé au lundi).

## Étape 0 — Surveillance des sources de codes

Re-vérification du soir des jeux à plus forte vélocité via l'API Roblox (Chrome) :

- **Descriptions in-game** (1 appel groupé `games.roblox.com/v1/games`) : Grow a Garden, Steal a Brainrot, Blade Ball, Volleyball Legends, Fruit Battlegrounds, Anime Vanguards, Fisch, Anime Last Stand.
- **Shouts de groupe** : Volleyball Game Group (35330702), The Garden Game (35789249), Kitawari / Anime Vanguards (17219742) → tous `shout: null`.

**Résultat : aucun nouveau code candidat.** Les seuls codes présents dans les descriptions sont déjà connus :
- Fruit Battlegrounds → `YOO1M110K` (déjà dans le snapshot).
- Aucun code dans les descriptions des 7 autres jeux.

Snapshots `lastChecked` rafraîchis (→ `2026-06-21T20:06:00Z`) pour les 8 jeux re-vérifiés. JSON revérifié **valide** (27 snapshots, se termine par `}`).

## Étape 2/3 — Vérification des codes (2 sources)

### Volleyball Legends — suivi du run du matin, toujours pas de mise à jour justifiée

Le matin, un signal « UPDATE_74 / SEASON_16 / SUMMER_UPDATE » n'avait pu être corroboré. Ce soir, vérification approfondie sur **4 trackers** :

| Source | Date de la version servie | Codes « actifs » |
|--------|---------------------------|------------------|
| Pro Game Guides | 21 mars 2026 (cache) | UPDATE_62… |
| Bloxodes | 16 mai 2026 | UPDATE_70, SEASON_15, OCEAN_UPDATE |
| Beebom | 23 mai 2026 | UPDATE_72, NEW_MAP, SUMMER_DELUXE |
| GamesRadar | 2 juin 2026 | UPDATE_72, NEW_MAP, SUMMER_DELUXE |

L'aperçu du moteur de recherche évoque une « **Update 75** » (UPDATE_75, SPECTATING, SHOW_OFF, SUMMER_UPDATE), mais **aucune page réellement consultable ne le confirme** : les 4 trackers directement récupérables servent des versions plus anciennes (max vérifiable = Update 72). Notre page affiche déjà **UPDATE_73 / JUNGLE_MAP / JUNE_2026**, soit déjà en avance sur toutes les sources vérifiables.

**Décision (règles « 2 sources » + honnêteté) : page NON modifiée.** Publier UPDATE_75 sur la seule foi d'un extrait de recherche, sans 2 sources fraîches concordantes consultables, serait du contenu non vérifié. À revérifier au prochain run quand les trackers auront rattrapé la mise à jour du samedi.

### Autres jeux à forte vélocité — pas de changement

Grow a Garden (description sans code, shout null), Steal a Brainrot (jeu sans codes), Blade Ball, Fisch, Anime Vanguards, Anime Last Stand : descriptions inchangées vs snapshots, aucun nouveau code à publier.

> Note : la recherche « Grow a Garden codes » renvoie surtout des résultats pour **Grow a Garden 2** (sorti le 12 juin, code `TEAMGREENBEAN`), un jeu distinct. Le jeu original « Grow a Garden » suivi ici n'expose aucun code dans sa description.

## Étapes 1, 4, 5, 6 — Ajouts / tier lists / guides / UGC

Pas d'ajout ce run. Comme noté au run du matin, le **mount bash du sandbox sert des lectures tronquées** sur les gros fichiers HTML, ce qui rend les grosses écritures difficiles à vérifier de façon fiable ; priorité donnée à la justesse des codes (lecture/écriture via l'outil fichier, fiable) plutôt qu'à des ajouts en masse risqués.

## Étape 7 — Jeu de la semaine

Dimanche → **non touché** (réservé au lundi). Conforme. (Le run de demain lundi devra mettre à jour la bannière `<!-- FEATURED-WEEK-START/END -->` avec le jeu #1 des tendances présent au catalogue.)

## Étape 8 — QC

Fichier réellement modifié ce run : **`tools/code-watch.json`** uniquement.
- Validé via Python : JSON parse OK, **27 snapshots**, se termine par `}`, **8** `lastChecked` mis à `2026-06-21T20:06:00Z`.
- Aucune page HTML modifiée → pas de risque de troncature HTML, pas de bump de cache JS (`js/main.js` intact, Étape 9 sans objet).

### Changements pré-existants dans l'arbre de travail
Comme au run du matin, `git status` liste des fichiers modifiés non committés issus des runs précédents (dont `codes/blue-lock-rivals.html` mis à jour ce matin). Ils seront inclus au prochain commit de Peter.

## Fichiers touchés ce run
- `tools/code-watch.json` — `lastChecked` rafraîchis (8 jeux) après re-vérification du soir.
- `rapport-zoneblox-2026-06-21-soir.md` — ce rapport.

## À suivre au prochain run (lundi)
- **Jeu de la semaine** : mettre à jour la bannière d'accueil (lundi).
- **Volleyball Legends** : confirmer la dernière update (74/75 ?) dès que 2 trackers fraîchement mis à jour concordent, puis actualiser codes + dates.
- Re-vérifier Blade Ball, Grow a Garden, Steal a Brainrot (sources tierces encore en retard ce soir).

## Pour publier
Dans le dossier GameNova, lance :

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
