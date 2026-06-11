# Zoneblox — Notes pour Claude

Règles et pièges à éviter, documentés à partir des erreurs réelles rencontrées.

---

## Architecture des données (CRITIQUE)

Il y a **3 sources de données indépendantes** qui doivent toujours être synchronisées manuellement :

| Source | Objet | Rôle |
|--------|-------|------|
| `js/main.js` | `GAMES_INDEX` | Liste tous les jeux (slug, name, emoji, codes count) |
| `js/main.js` | `ROBLOX_THUMBS` | URLs des miniatures (slug → URL) |
| `codes/index.html` | `ALL_GAMES` | Liste des jeux pour la page "Tous les codes" |
| `codes/index.html` | `THUMBS` | URLs des miniatures (objet INLINE, séparé de main.js) |

**Erreurs déjà commises :**
- Ajouter un jeu à `GAMES_INDEX` sans l'ajouter à `ALL_GAMES` → jeu invisible sur la page codes
- Mettre à jour `ROBLOX_THUMBS` dans main.js sans mettre à jour `THUMBS` dans index.html → miniatures manquantes
- Ces deux objets sont complètement indépendants. Modifier l'un ne modifie PAS l'autre.

**Vérification à faire après chaque ajout de jeu :**
```bash
python3 -c "
import re
js = open('js/main.js').read()
html = open('codes/index.html').read()
gi = set(re.findall(r\"slug:\\s*'([^']+)'\", re.search(r'GAMES_INDEX.*?\];', js, re.DOTALL).group()))
ag = set(re.findall(r\"slug:'([^']+)'\", html))
print('Manquants dans ALL_GAMES:', gi - ag)
print('Manquants dans GAMES_INDEX:', ag - gi)
"
```

---

## Version cache JS

La version actuelle est **`main.js?v=19`**. Cette version doit être identique dans TOUS les fichiers HTML.

- `main.js?v=20` **n'existe pas** sur le serveur → cause une panne JS complète → zéro miniature
- Avant de bumper la version, vérifier que le fichier correspondant existe réellement
- Commande de vérification : `grep -r "main.js?v=" . --include="*.html" | grep -v "v=19" | grep -v ".git"`

---

## Fichiers HTML corrompus (null bytes)

Des opérations `sed -i` sur de grands fichiers peuvent introduire des null bytes (`\x00`) qui corrompent le HTML silencieusement.

**Symptôme :** fichier tronqué, pas de `</html>`, taille anormalement petite.

**Remède :**
```bash
# Restaurer depuis git
git show <commit>:<fichier> > <fichier>
# Puis vérifier
python3 -c "c=open('<fichier>','rb').read(); print('null bytes:', c.count(b'\x00'))"
```

**Règle :** toujours utiliser Python pour les remplacements de texte sur les grands fichiers, jamais `sed` avec backreferences complexes.

---

## codes/index.html — Règles d'écriture

Ce fichier fait ~50 Ko. Il est fragile à l'écriture.

**Erreurs déjà commises :**
- Écrire le fichier en plusieurs passes avec `str.replace()` sur du contenu partiel → troncature à mi-fichier
- Utiliser une ancre (ex: `survive-the-killer`) qui n'est pas dans le fichier cible → silencieusement échoué

**Règle :** toujours restaurer depuis `git show HEAD:codes/index.html`, appliquer toutes les modifications en **un seul script Python**, écrire une seule fois. Vérifier que le fichier se termine par `</html>` et que sa taille est > 48 Ko.

---

## Miniatures Roblox

- L'URL `og:image` se trouve dans les meta tags de `https://www.roblox.com/games/<placeId>/<name>`
- Certaines pages Roblox sont client-rendues (JS requis) → `web_fetch` ne retourne pas les meta tags → pas d'URL récupérable
- L'API `thumbnails.roblox.com` est bloquée depuis le shell bash (403)
- En cas d'échec, garder le SVG placeholder plutôt que d'inventer une URL

**Jeux dont la page Roblox ne retourne pas og:image (client-rendu) :**
- `dragon-blox` (place ID: 3177438863)
- `spin-a-brainrot` (universe ID: 8497165255)

---

## Règles de contenu (codes)

- **Minimum 2 sources** avant de publier des codes (Pocket Tactics, Beebom, Pro Game Guides, Destructoid…)
- Ne jamais inventer de codes
- Les codes dans la description Roblox du jeu comptent comme source valide
- Toujours indiquer la date de vérification

---

## Git

- **Ne jamais faire `git push` automatiquement** — Peter pousse manuellement
- Sur Windows cmd, les messages de commit multi-lignes avec `-m "..."` ne supportent pas les retours à la ligne directs → utiliser un fichier temporaire ou une ligne unique
- Commandes git valides à fournir à Peter sous forme de blocs copiables

---

## QC obligatoire après chaque modification

Pour chaque fichier HTML modifié, vérifier :

| Check | Commande |
|-------|---------|
| Se termine par `</html>` | `tail -1 <fichier>` |
| GA4 présent | `grep "G-FEL71QVHNL" <fichier>` |
| Cache JS correct | `grep "main.js?v=19" <fichier>` |
| Nav active correcte | `grep 'class="active"' <fichier>` |
| data-cta="guidelink" | `grep 'data-cta="guidelink"' <fichier>` (codes pages seulement) |
| Pas de null bytes | `python3 -c "print(open('<f>','rb').read().count(b'\x00'))"` |
