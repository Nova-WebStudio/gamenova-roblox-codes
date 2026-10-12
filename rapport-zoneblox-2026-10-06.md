# 🗞️ Rapport ZoneBlox — 2026-10-06 (05h, full maintenance, mardi)

**Philosophie appliquée : EXACTITUDE > FRAÎCHEUR > UTILITÉ JOUEUR > AUTORITÉ > SEO > QUANTITÉ.**
Résultat global : run de **maintenance et vérification**. Aucun code inventé, aucune nouvelle URL, aucune suppression sans preuve. 5 hot games confirmés inchangés, 1 incohérence d'affichage corrigée (Aniimo), conflits documentés.

> ⚠️ **À noter** : le working tree contenait déjà les modifications non commitées du run du 05/10 (Peter n'a pas encore poussé). Ce run s'ajoute à ce lot — tout part dans le même commit.

---

## CODES

### hotGames (priorité absolue) — revérifiés, AUCUN changement
| Jeu | Actifs | Sources (date) | verifDate |
|-----|--------|----------------|-----------|
| volleyball-legends | 4 — UPDATE_90, SKELETON_BUNDLE, JINX, SLOT_REWORK | Dexerto 04/10 (match exact) | → 6 oct |
| blue-lock-rivals | 3 — DONREVAMP, SENDOUNEXT, ACEEATER | Pocket Tactics 04/10 (match exact) | → 6 oct |
| steal-a-brainrot | 1 — BESTBRAINROTEVER | Pocket Tactics 05/10 + Dexerto | → 6 oct |
| grow-a-garden | 2 — RDCAward, BEANORLEAVE10 | Gfinity 30/09 | → 6 oct |
| anime-vanguards | 3 — Assault, SummerLeaving, AnniNextHopefully | Pocket Tactics + Dexerto | → 6 oct |

### Rotation / conflits
- **anime-vanguards `2ndAnniDay1`** : **RÉSOLU → non ajouté** (introuvable sur PT + Dexerto). Codes AV disputés (Wrath/Retribution/MiniUpd2 : actifs PT vs expirés Dexerto, même date) → **kill switch**.
- **clover-retribution** : `!wspainplusdelay` = **expiré confirmé** (PGG 28/09) → reste hors page. Écart 13 (nous) vs 5 (PGG) non tranché (1 source) → pas de bump.
- **restaurant-tycoon-3 (11)** / **untitled-aot (6)** : sources trop anciennes (PGG restaurant = mai) → **maintenus**, conflit non tranchable.

### Codes ajoutés / expirés ce run
- **0 ajouté, 0 expiré** sur les pages Roblox (toutes confirmations = statu quo).

### Candidats en attente
- Grosses listes +26 j (astral-simulator 100, dragon-blox 82, anime-battle-rng 35) : **sources fraîches introuvables** → aucune suppression (preuve requise). Reportées.

---

## SEO
- **Tendance détectée** : aucune nouvelle à fort potentiel. Pas de breakout Roblox (nouveaux jeux octobre sans traction).
- **Cluster travaillé** : aucun (update-before-create respecté, kill switch éditorial).
- **Anti-cannibalisation** : OK — aucune nouvelle page créée.
- **Prochaine brique** : trim des grosses listes de codes (autorité + confiance) dès sources fraîches.

## NOUVEAUX JEUX
- Aucun ajouté. Prime Heroes / Octane / Starforged / Scrapbook Saga toujours sans preuve de traction → surveillance.

## CONTENU
- Guides / tier lists / articles : **0 créé** (pas de justification).
- Mises à jour : 5 verifDate hot games + correction prose Aniimo (11→15 codes).

## ANIIMO
- `data/aniimo/codes.json` lastChecked → **6 oct**. 14/15 codes reconfirmés (mein-mmo 05/10) ; `aniimazingfroyo` (US-only) conservé (région-locked ≠ expiré).
- **Fix** : note + FAQ affichaient encore « 11 codes / 27 sept » (liste incomplète) → corrigées en « 15 codes / 6 oct » + rebuild.
- **À vérifier** : mein-mmo rapporte un nouveau monstre/patch → NE PAS éditer creatures.json sans confirmation (nom + stats).

## GTA 6
- **CONFIRMÉ** : sortie 19 nov 2026 (seule date officielle).
- **RUMEUR** : Trailer 3 (aucune date officielle Rockstar). Aucune annonce overnight. → veille evergreen, 0 URL.

## FC 27
- Live octobre 2026 = **EA Sports FC 26** (ambiguïté spec FC27 vs réalité). Kill switch, aucune page. À clarifier avec Peter.

## EDITORIAL INTELLIGENCE
- **Top opportunités** : aucune MUST_PUBLISH. Marché calme overnight.
- **Tendances** : rien de neuf à fort trendScore.
- **Articles créés** : 0. **Pages mises à jour** : 5 hot + Aniimo.
- **Sujets ignorés** : AV codes disputés, 2ndAnniDay1 (non confirmé), nouveaux jeux oct (pas de traction).
- **Sujets à surveiller** : GTA6 Trailer 3, Aniimo nouveau monstre, grosses listes à trimmer.
- `editorial-intelligence.json` : +1 topic (`maint-2026-10-06`), GTA6 & Aniimo revérifiés. 22 topics.

## EDITORIAL QUEUE
- **Urgents** : GTA 6 (annonce officielle).
- **À publier** : rien.
- **À mettre à jour** : grosses listes (preuve d'expiration), clover 13→5, Aniimo creatures (à vérifier).
- **À préparer** : nouveaux jeux oct, FC périmètre, pass CTA.
- **Demain / prochain run** : hot games (volleyball Update week-end), grosses listes (sources alternatives), rotation en retard (jailbreak/arsenal/a-dusty-trip hors PGG).

## QC
- **36 HTML modifiés** : 0 null byte, tous `</html>`, div équilibrés, GA4 présent, CTA unique. ✅
- **3 JSON** (code-watch, editorial-intelligence, aniimo/codes) valides. ✅
- `node --check js/main.js` ✅ | sitemap.xml (383 URLs) + sitemap-games.xml well-formed ✅
- /avatar/ non touché ✅ | build_codes_json non lancé (aucun code modifié).
- **Erreurs corrigées** : incohérence d'affichage Aniimo (11 vs 15 codes).

---

_Pour publier : dans le dossier GameNova, lance `git add -A && git commit -m "MAJ Zoneblox du jour" && git push origin main`. Hostinger déploie automatiquement après le push._
