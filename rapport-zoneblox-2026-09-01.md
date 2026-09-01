# Rapport Zoneblox — 1ᵉʳ septembre 2026

## a) Codes (priorité absolue)

Re-scan multi-sources des jeux chauds (Beebom, PCGamesN, Pro Game Guides, PC Gamer, GamesRadar), tous vérifiés le 1ᵉʳ septembre 2026 :

- **Blue Lock Rivals — 1 changement appliqué.** Les 6 codes du patch précédent (INSANETRAILERSOON, DESTROYERMODE, BIGTRAILERSOON, RINTODAY, FIXESLATERTODAY, SORRY4DELAY!!) ont **expiré** (Beebom, màj 1ᵉʳ sept.). Codes actifs désormais : **UBERSTAKEOVER, KINGNEXTWEEK, EGODEFENSE** (3 actifs). Tables, compteurs, prose d'intro, note « Mis à jour le » et JSON-LD corrigés sur `codes-blue-lock-rivals.html`.
- **Volleyball Legends — confirmé stable** : UPDATE_85 / SHIRO / BLOCKED (Beebom 1ᵉʳ sept.). Déjà à jour.
- **Anime Vanguards — confirmé stable** : Retribution / Wrath / MiniUpd2 (PGG 30/08 + PC Gamer). Déjà à jour.
- **Stables confirmés** : Blox Fruits (24 codes, PCGamesN), Grow a Garden (RDCAward, BEANORLEAVE10).
- **Candidat en attente (prudence)** : Steal a Brainrot `BESTBRAINROTEVER` — PCGamesN (31/08) affirme « aucun code n'existe », mais 3 sources l'ont confirmé actif le 30/08. **Gardé actif** (règle des 3 sources récentes) et **à re-vérifier au prochain run**.

**Fraîcheur catalogue** : « Vérifié le » rafraîchi au **1ᵉʳ septembre 2026** et titres/H1/og basculés en **(septembre 2026)** sur les **177 pages codes servies**. Widget `data/codes.json` régénéré (**178 jeux** avec l'ajout de Dungeon Quest Reborn, 1224 codes actifs).

Jeux chauds non re-vérifiés en profondeur ce run (stables, à re-prioriser) : King Legacy, Fisch, Fruit Battlegrounds, Anime Last Stand, Pet Simulator 99, World Fighters.

## b) Directeur SEO

- **Trending re-scanné** : leaders (Blox Fruits, Grow a Garden, Steal a Brainrot, Brookhaven, GAG2, Adopt Me, 99 Nights, Steal An Egg, Anime Expeditions) tous couverts. **Nouveau hit détecté** : **Dungeon Quest Reborn** (~43,8K joueurs, Action RPG) → non couvert, donc fiché en priorité (voir c).
- **Brique cluster (information gain)** : ajout d'une section **« Spins & système de pity »** au guide Volleyball Legends (`guides/volleyball-legends.html`) — mécaniques de pity (paliers 50/200/400), coûts de spins, stratégie 2× Luck, meilleurs styles par priorité. Intention *how-to* distincte de la tier list, sourcée (Sportskeeda + Dot Esports + wiki Volleyball Legends). ~1 900 → ~2 200 mots.
- Roadmap `SEO-directeur-audit-roadmap-2026-07-24.md` mise à jour (J22 + prochaine brique J23).

## c) Nouveau jeu — « la totale » sur Dungeon Quest Reborn

À la demande de Peter. Jeu : `roblox.com/games/77649408247578` — universe **9931749389**, groupe **496909722** (Delta Quarters OG), ~**43 821 joueurs**, 62,7M visites, Action RPG / dungeon crawler licencié Voldex.

Vraie miniature : `tr.rbxcdn.com/180DAY-70c1d4c8beaf4aa7f463b9556abfe4c9/…` (768/432 hero, 480/270 cartes).

3 pages créées et reliées (codes ↔ tier list ↔ guide) :

1. **`codes-dungeon-quest-reborn.html`** (~1 690 mots) — état **« aucun code » honnête et sourcé** : le jeu n'a pas de système de codes (comme le Dungeon Quest original), confirmé par Pro Game Guides, PCGamesN, Destructoid et All Things How. Section « Que faire à la place », 6 astuces, À propos développé, FAQ, **2 vidéos oEmbed vérifiées** (ItsChalls, Cocajola), **bandeau CTA `data-cta="guidelink"`**.
2. **`tier-list/dungeon-quest-reborn.html`** — armes & capacités classées S+/S/A : Eden's Vengeance (Guerrier), Eden's Reaper (Mage), EIR/IEF, Voidspire/Effigy/Hofund. Sources PGG + BloxRant.
3. **`guides/dungeon-quest-reborn.html`** (~1 680 mots, 8 sections) — classes Mage→Guerrier, donjons + niveaux requis (table), leveling/leech (+ boosts XP), ordre des game pass, meilleures armes/« pot »/gemmes, trading. Sources All Things How + PGG.

**Intégration complète** : carte accueil (`GAMES`) ; `GAMES_INDEX` + `ROBLOX_THUMBS` + `ROBLOX_UNIVERSE_IDS` (js/main.js) ; carte `tous-les-codes.html` ; cartes hubs `tier-lists.html` et `guides.html` (vraies miniatures) ; 4 sitemaps (codes, tier-list, guides, principal) ; SVG fallback `images/games/dungeon-quest-reborn.svg` ; liens croisés bidirectionnels.

## d) Fichiers touchés & QC

- **Nouveaux** : `codes-dungeon-quest-reborn.html`, `tier-list/dungeon-quest-reborn.html`, `guides/dungeon-quest-reborn.html`, `images/games/dungeon-quest-reborn.svg`, ce rapport.
- **Modifiés** : `codes-blue-lock-rivals.html` (+ dates/titres sur les 177 pages codes), `guides/volleyball-legends.html`, `index.html`, `js/main.js`, `tous-les-codes.html`, `tier-lists.html`, `guides.html`, `data/codes.json`, 4 sitemaps, roadmap SEO. **Cache JS bumpé v=40 → v=41** sur les 340 fichiers HTML (main.js modifié).
- **QC** : scan intégrité sur les **529 fichiers** modifiés/nouveaux → **tout propre** (0 null byte, tous les `.html` finissent par `</html>`, `<div>` équilibrés, GA4 présent ; sitemaps valides `</urlset>`). `node --check js/main.js` et `js/events.js` OK. `data/codes.json` JSON valide. Pages DQR : ≥1 680 mots chacune, nav 7 entrées (tier/guide) / nav codes, JSON-LD valide, miniatures tr.rbxcdn, aucune vidéo interdite.

---

Pour publier : dans le dossier GameNova, lance

```
git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main
```

Hostinger déploie automatiquement après le push.
