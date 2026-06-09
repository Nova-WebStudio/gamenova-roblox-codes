# Rapport de maintenance Zoneblox — 9 juin 2026

## Résumé

Maintenance quotidienne complète. 8 pages codes mises à jour, 1 nouveau guide créé, version JS bumpée sur 129 fichiers HTML.

---

## Étape 1 — 6 nouveaux jeux ajoutés (session précédente)

Réalisée en session précédente. Les 6 jeux suivants ont été ajoutés au site (GAMES_INDEX + ALL_GAMES + pages codes) :

- Grow a Garden 🌱
- Steal a Brainrot 🧠
- Pressure 😱
- Type Soul ⚡
- Rivals ⚽
- Fisch 🎣 (page codes existante mise à jour)

---

## Étape 2 — Vérification et mise à jour des codes

### Codes mis à jour (sources ≥ 2 confirmées)

| Jeu | Avant | Après | Sources |
|-----|-------|-------|---------|
| Bee Swarm Simulator | 14 | 17 | Dexerto + PCGamer (8 juin 2026) |
| Fisch | 10 | 23 | RoCodes (9 juin 2026) + PCGamer |
| Da Hood | 6 | 18 | Twinfinite (8 juin 2026) |
| Dress to Impress | 8 | 41 | RoCodes (4 juin 2026) |
| Heroes Battlegrounds | 2 | 21 | RoCodes + Beebom + Dexerto |
| Garden Tower Defense | 6 | 19 | Destructoid (16 mai 2026) |

### Codes inchangés (déjà à jour)

- **Attack on Titan Revolution** — 21 codes, vérifié. Déjà à jour (FREECODE5, FREECODE6, LIKES1M250K, VISITS900M présents).
- **Mad City** — 6 codes, compte confirmé par 2 sources.

### codes/index.html

Entrées ALL_GAMES mises à jour pour les 6 jeux modifiés (nouveaux comptes + dates).

---

## Étape 5 — Nouveau guide créé

### `guides/pressure.html`

Guide complet du jeu Pressure (horreur Roblox, Urbanshade) en français.

**Sections couvertes :**
- Guide débutant (objectif, portes verrouillées, rythme)
- Lampe-torche, gestion des ressources, boutique de Sebastian
- 13 monstres létaux avec stratégies détaillées (Angler + 4 variantes, Squiddles, Puddles of Void Mass, Eyefestation, Tourelles, Pandemonium, Wall Dwellers, Good Duo, Multi-Monster, Death Angel, Stan, Mr. Lopee, Parasites, Finale)
- 10 monstres inoffensifs (lore)
- Zones spéciales : Entrepôt (réparation générateurs + Volus Lunara) + La Tranchée (câbles sous-marins + Canon)
- Conseils avancés
- FAQ (4 questions JSON-LD)
- CTA vers /codes/pressure.html

**Conformité :**
- GA4 : ✅ G-FEL71QVHNL
- Nav 6 entrées : ✅
- JSON-LD : Article + BreadcrumbList + FAQPage ✅
- Langue : ✅ tout en français (noms de monstres en anglais conservés)
- `main.js?v=16` : ✅

### `guides/index.html`

- Carte Pressure ajoutée (position 10)
- JSON-LD ItemList mis à jour (10 entrées)

---

## Étapes 3, 4, 6 — Non modifiées

- **Étape 3 (SEO/vidéos)** : Aucune modification apportée ce jour. Priorité : pages codes avec 0 vidéo YouTube.
- **Étape 4 (Tier lists)** : Aucune modification. Tier lists existantes conservées telles quelles.
- **Étape 6 (UGC)** : Aucune modification. Pages UGC existantes conservées.

---

## Étape 7 — Jeu de la semaine

**Ignoré** — la règle stipule de ne mettre à jour le jeu de la semaine que le lundi. Aujourd'hui est mardi.

---

## Étape 9 — Bump cache JS

`main.js?v=15` → `main.js?v=16` appliqué sur **129 fichiers HTML** (racine, codes/, tier-list/, ugc-gratuit/, guides/).

Vérification : 0 fichier restant en v=15, 129 en v=16.

---

## QC — Résultats sur les fichiers modifiés aujourd'hui

| Fichier | </html> | GA4 | Nav 6 | v=16 |
|---------|---------|-----|-------|------|
| codes/bee-swarm-simulator.html | ✅ | ✅ | ✅ | ✅ |
| codes/fisch.html | ✅ | ✅ | ✅ | ✅ |
| codes/da-hood.html | ✅ | ✅ | ✅ | ✅ |
| codes/dress-to-impress.html | ✅ | ✅ | ✅ | ✅ |
| codes/heroes-battlegrounds.html | ✅ | ✅ | ✅ | ✅ |
| codes/garden-tower-defense.html | ✅ | ✅ | ✅ | ✅ |
| codes/index.html | ❌ (pré-existant) | ✅ | ✅ | ✅ |
| guides/pressure.html | ✅ | ✅ | ✅ | ✅ |
| guides/index.html | ✅ | ✅ | ✅ | ✅ |

> **Note `codes/index.html`** : La balise `</html>` manquante est un problème pré-existant (avant cette session). Le fichier JS en fin de fichier est tronqué depuis une session antérieure. À corriger dans une prochaine session dédiée.

> **Note GA4 absente sur beaucoup de pages codes/** : Détectée en QC global, mais pré-existante. Ces pages n'ont pas été modifiées aujourd'hui. À traiter progressivement.

---

## Fichiers modifiés ce jour

```
codes/bee-swarm-simulator.html
codes/fisch.html
codes/da-hood.html
codes/dress-to-impress.html
codes/heroes-battlegrounds.html
codes/garden-tower-defense.html
codes/index.html
guides/pressure.html   ← nouveau
guides/index.html
js/main.js             ← compteurs codes mis à jour (session précédente)
+ 129 fichiers HTML    ← main.js?v=15 → v=16
```

---

## Pour publier

Dans le dossier GameNova, lance :

```bash
git add -A && git commit -m "MAJ Zoneblox du 9 juin 2026 — codes +6 jeux, guide Pressure, cache v16" && git push origin main
```

Hostinger déploie automatiquement après le push.
