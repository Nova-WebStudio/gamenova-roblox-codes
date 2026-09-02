# Rapport Zoneblox — 2 septembre 2026 (mercredi)

Run quotidien automatique. Priorité tenue : vérification des **codes** d'abord, puis Directeur SEO, puis QC.

> **Correctif ajouté après le run (signalé par Peter) — Anime Astral Simulator :** la page était **fausse** — 54 codes affichés « actifs » dont la **majorité étaient expirés**, et la liste « expirés » était **vide**. Elle a été **entièrement reconstruite** depuis Pro Game Guides (màj 2 sept.), recoupée Beebom + Pocket Tactics : **100 codes actifs** (dont les nouveaux 12.5FIXES, SORRYRELICS, MINI12.5, QUINQUE, 2GACHAS, UPDATE12, KAGUNES…) et **68 codes expirés** correctement déplacés. Compteur 54→100, note « Mis à jour le 2 septembre » ajoutée, `data/codes.json` régénéré (1270 codes au total). ⚠️ **À surveiller** : d'autres pages de la longue traîne (hors « hot games ») peuvent souffrir du même défaut (codes jamais élagués). Un audit ciblé des pieces « suspectes » (>40 codes actifs sans liste d'expirés) est recommandé au prochain run.

---

> **Audit « faux actifs » (demandé par Peter après le signalement Anime Astral).** J'ai scanné les 178 pages pour la signature « beaucoup de codes actifs + liste d'expirés vide » (= liste jamais élaguée). 9 pages ressortaient ; vérifiées une par une contre des sources datées du 1ᵉʳ-2 sept.
>
> **Corrigées (faux actifs supprimés) :**
> - **Anime Astral Simulator** : 54 « actifs » (majorité expirés) → **100 actifs réels** + 68 expirés.
> - **DOORS** : 31 → **8 actifs** (PGG 1ᵉʳ sept.) ; entrées non-redevables/streamers déplacées en expirés.
> - **Clover Retribution** : 28 (tous expirés en réalité) → **14 actifs réels** (Beebom 1ᵉʳ sept.).
> - **Dress to Impress** : 39 → **32 actifs** (retiré 8 codes expirés : FACECARD, BADDIE4LIFE, CUPIDSCLOUD, 2YEARS, 2026BADDIES, 2GETHER, RDC2025, B3APL4YS_D0L1E ; ajout LANADOLLDRESS).
> - **Anime Last Stand** : nos 38 étaient tous encore valides → **+3 nouveaux** (MagicKnights!, ElfReincarnation!, IsItReallyWeekly?!) = 41.
>
> **Sans correction — sous-listage (non trompeur, honnête) :** Dragon Blox (82 chez nous, ~116 réels) et Brainrot Evolution (24 vs ~86) : ces jeux gardent leurs codes très longtemps ; nos listes sont incomplètes mais pas fausses (à enrichir plus tard).
>
> **À vérifier au prochain run (sources trop minces/périmées pour élaguer sans risque) :** Scroll a Brainrot (seule source datée = mai 2026), World Fighters (sources anciennes), Heroes Battlegrounds (codes de maîtrise souvent persistants).
>
> Après ces corrections : `data/codes.json` régénéré (1229 codes actifs au total). QC OK sur toutes les pages touchées.

---

## (a) Codes vérifiés (priorité)

**Sources croisées** : Beebom (pages datées 1ᵉʳ sept.), PCGamesN, Pro Game Guides, GamesRadar, PC Gamer, Dexerto, Pocket Tactics.

**1 changement de liste appliqué :**

- **Fruit Battlegrounds** — nouveau code actif **`HIGHER1M120K`** (800 Gems), confirmé **NOUVEAU** par Beebom (màj 1ᵉʳ sept.) et recoupé Pocket Tactics + Pro Game Guides (≥3 sources). **`OMGUPDATE22`** basculé en **expiré** (Beebom 1ᵉʳ sept. le liste expiré ; le snapshot PGG du 6 août était périmé). Total actifs **inchangé (5)**, compteur expirés **6→7**, note « Mis à jour le 2 septembre » ajoutée sur la fiche.

**Jeux chauds confirmés stables (aucun changement) :**

- Blox Fruits (24 actifs — aucun nouveau code depuis l'Update PvP d'été)
- Steal a Brainrot (1 actif `BESTBRAINROTEVER` — Dexerto/Beebom « un seul code »)
- Anime Vanguards (3 : Retribution / Wrath / MiniUpd2)
- Blue Lock Rivals (3 : UBERSTAKEOVER / KINGNEXTWEEK / EGODEFENSE — les 6 anciens gardés **hors liste par prudence**, sources en conflit actif/expiré)
- Volleyball Legends (3 : UPDATE_85 / SHIRO / BLOCKED)
- King Legacy (7, aucun conflit)
- Grow a Garden (2 : RDCAward / BEANORLEAVE10)
- Pet Simulator 99 (0 — le jeu n'a pas de système de codes)

**Résolu :** Fisch `SkycrestNextWeek` **confirmé expiré** (Beebom / Pocket Gamer 1ᵉʳ sept.) — n'avait jamais été publié → candidat clos.

**Candidats « en attente » (prudence, à traiter au prochain run) :**

- **Anime Last Stand** : `MagicKnights!` et `ElfReincarnation!` (nouveaux, vus Beebom + PGG + Destructoid le 1-2/09). Reportés pour vérif fine des récompenses avant d'éditer une liste de 38 codes (éviter toute régression).
- **Grow a Garden** : `torigate` — PCGamesN (29/08) + PGG le listent actif, Beebom expiré → **conflit**, gardé hors liste.

**Fraîcheur :** « 🔄 Vérifié le » rafraîchi au **2 septembre 2026** sur les **178 pages** codes. Widget `data/codes.json` régénéré (178 jeux, 1224 codes actifs).

**Jeux non re-vérifiés en profondeur ce run (à prioriser demain) :** longue traîne hors « hot games » (RNG, tower defense, tycoons divers) — stables, non contredits par les agrégateurs.

## (b) Directeur SEO

- **Trending re-scanné :** leaders vérifiés (Steal An Egg #1 ~1,4M CCU, Blox Fruits, Grow a Garden, Steal a Brainrot, Brookhaven, GAG2, Adopt Me). **Aucun nouveau hit ≥4000 joueurs non couvert.** Dungeon Quest Reborn toujours sans système de codes (état « aucun code » de la fiche confirmé). → evergreen.
- **Brique réalisée (maillage / autorité des hubs éditoriaux) :** ajout de **liens de découverte réciproques** depuis les 3 hubs **réellement servis** (`tous-les-codes.html`, `tier-lists.html`, `guides.html`) vers les 2 hubs éditoriaux (`meilleurs-jeux-roblox.html`, `nouveaux-jeux-roblox.html`). Correction d'un vrai trou de maillage : seuls les anciens hubs `codes/index.html`, `tier-list/index.html`, `guides/index.html` (legacy, 301-redirigés) pointaient vers l'éditorial. **Intention distincte** (découverte/navigation) → **aucune cannibalisation**, aucune nouvelle URL. Réciprocité complète (les hubs éditoriaux pointent déjà vers les 3 hubs servis).
- **Prochaine brique (J24) inscrite dans la roadmap :** ajouter proprement les codes Anime Last Stand `MagicKnights!` / `ElfReincarnation!` après vérif ≥3 sources datées ; sinon enrichir/surveiller le cluster Dungeon Quest Reborn.

## (c) Jeux ajoutés / guides / tier lists / UGC / évènements / jeu de la semaine

- **Aucun jeu ajouté** (aucun nouveau hit non couvert).
- **Guides / tier lists :** aucun nouveau (tier list Dungeon Quest Reborn déjà fraîche et couvrant les Terres du Nord / Northern Lands).
- **UGC :** inchangé (pas de nouveau code confirmé).
- **Encart évènements :** non modifié — encart **retiré** de l'accueil (demande de Peter, cf. CLAUDE.md), `data/events.json` non touché.
- **Jeu de la semaine :** non modifié (mercredi ; MAJ réservée au lundi).

## (d) Fichiers touchés + QC

**Fichiers modifiés :**

- `codes-fruit-battlegrounds.html` (changement de codes + note datée)
- Les **178** pages `codes-*.html` (rafraîchissement « Vérifié le » → 2 septembre 2026)
- `tous-les-codes.html`, `tier-lists.html`, `guides.html` (liens vers hubs éditoriaux)
- `SEO-directeur-audit-roadmap-2026-07-24.md` (brique J23 + reco J24)
- `tools/code-watch.json` (lastRun, snapshots, candidats en attente)
- `data/codes.json` (régénéré)

**QC (tous verts) :** chaque HTML se termine par `</html>` ; `<div>` équilibrés (0) ; **0 null byte** partout ; `data/codes.json` + `tools/code-watch.json` JSON valides ; `node --check js/main.js` + `js/events.js` OK ; GA4 présent ; `verifDate` = « 2 septembre 2026 » sur les 178 pages (aucune date résiduelle) ; cache JS uniforme `main.js?v=41` (main.js non modifié → pas de bump) ; fiche Fruit Battlegrounds = 1 471 mots (≥1200).

---

**Pour publier :** dans le dossier GameNova, lance

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
