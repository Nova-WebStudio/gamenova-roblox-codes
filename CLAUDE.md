# Zoneblox — Notes pour Claude

Règles et pièges à éviter, documentés à partir des erreurs réelles rencontrées.

---

## « La totale » sur un jeu (demande de Peter)

Quand Peter dit **« fais-moi la totale »** sur un jeu, cela signifie produire **les 3 pages dédiées** pour ce jeu, complètes et reliées entre elles :

1. **Page codes** — `codes/<slug>.html` (≥1200 mots, miniature réelle `tr.rbxcdn.com`, 2 vidéos vérifiées oEmbed, astuces, FAQ, À propos + 3 similaires, bandeau CTA). Si le jeu n'a pas de codes vérifiables (2 sources / description in-game), ne pas en inventer : afficher honnêtement « pas de code confirmé ».
2. **Tier list** — `tier-list/<slug>.html` (classement pertinent : classes, unités, pets, fruits… selon le jeu ; 2 sources ; chips + ItemList + date).
3. **Guide complet** — `guides/<slug>.html` (gabarit `guides/blox-fruits.html` : TOC ancré, sections adaptées, CTA, FAQ ; 2 sources).

**Intégrations obligatoires à chaque fois** : carte accueil + `GAMES_INDEX`/`ALL_GAMES`/`ROBLOX_THUMBS`/`THUMBS`/`ROBLOX_UNIVERSE_IDS` (pour la page codes) ; carte + ItemList du hub tier-list (vraie miniature) et du hub guides ; `<li>` accueil ; `<url>` au sitemap pour les 3 pages ; **liens croisés** codes ↔ tier list ↔ guide (boutons hero + bandeau CTA `data-cta="guidelink"` pointant vers les pages dédiées) ; SVG fallback ; bump cache si `js/main.js` modifié.

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

⚠️ **RÈGLE ABSOLUE (demandée par Peter) : JAMAIS de SVG comme miniature affichée d'un jeu.** Toujours une **vraie miniature `tr.rbxcdn.com`** récupérée via l'API officielle. Le SVG `/images/games/<slug>.svg` ne sert QUE de fallback `onerror`, jamais de `src` principal, et jamais comme valeur dans `ROBLOX_THUMBS` / `THUMBS`.

**Méthode fiable pour obtenir la vraie miniature (le shell bash n'a PAS de réseau ; utiliser le navigateur Chrome) :**
1. placeId → universeId : `https://apis.roblox.com/universes/v1/places/<placeId>/universe`
2. universeId → imageUrl : `https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=<id>&countPerUniverse=1&size=768x432&format=Png&defaults=true` → champ `imageUrl` (format `https://tr.rbxcdn.com/180DAY-<hash>/768/432/Image/Png/noFilter`).
3. **Toujours vérifier que l'universeId correspond au BON jeu** via `https://games.roblox.com/v1/games?universeIds=<id>` (champ `name`). Bug réel du 16 juin : `ROBLOX_UNIVERSE_IDS['king-legacy']` valait `6096648965` = « Kkimusya's Place » (baseplate vide, 0 joueur) au lieu de `1451439645` (King Legacy) → la miniature live était fausse et retombait sur le SVG.

Mettre la vraie URL dans **les 3 endroits** : `ROBLOX_THUMBS` (js/main.js), `THUMBS` (codes/index.html), et le `src` du hero `codes/<slug>.html` (+ carte index.html, carte tier-list/index.html, guide). Renseigner aussi le bon `ROBLOX_UNIVERSE_IDS` pour le rafraîchissement client-side.

- L'URL `og:image` se trouve dans les meta tags de `https://www.roblox.com/games/<placeId>/<name>`
- Certaines pages Roblox sont client-rendues (JS requis) → `web_fetch` ne retourne pas les meta tags → utiliser Chrome (`navigate` + `get_page_text`) qui exécute le JS et peut lire les endpoints JSON de l'API Roblox
- L'API `thumbnails.roblox.com` est bloquée depuis le shell bash (403) → passer par Chrome
- En dernier recours seulement, si la vraie miniature est introuvable, garder le SVG placeholder — mais ne JAMAIS inventer d'URL

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

## Bandeaux CTA & équilibre des div

- **Ne jamais remplacer le bloc `data-cta="guidelink"` par regex `.*?</div></div></div>`** : la fermeture du titre/sous-titre matche en premier → boutons orphelins et `</div>` en trop (erreur réelle du 12 juin, page cassée visuellement). Réécrire toute la zone pub+bandeau, ou localiser la fin du bloc par comptage de div.
- Après toute édition structurelle, vérifier l'équilibre des div sur tout le site :
```bash
python3 -c "
import re,glob
for f in glob.glob('**/*.html',recursive=True):
    h=open(f,encoding='utf-8',errors='replace').read()
    d=len(re.findall(r'<div\b',h))-h.count('</div>')
    if d: print(f,d)"
```
- Bug historique corrigé le 12 juin : `</div>` de fermeture de l'onglet `tab-codes` manquant sur 6 pages (anime-reborn, basketball-zero, haze-piece, jujutsu-infinite, type-soul, untitled-boxing-game). Si une page s'affiche « cassée », vérifier d'abord l'équilibre des div.

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
