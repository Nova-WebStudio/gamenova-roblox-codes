# Audit performance mobile — ZoneBlox

**Date :** 9 juin 2026 · **Score mobile actuel :** ~65/100 · **Objectif :** LCP < 2,5 s, Lighthouse > 85

Cet audit est basé sur l'analyse du code réel de `index.html` (la page d'accueil, qui est la page testée), et sur des mesures concrètes faites sur les fichiers du site.

---

## Résumé exécutif

Le score est plombé par **une seule cause dominante** : l'image hero `images/hero-bg.png` pèse **1,9 Mo** et c'est l'élément LCP. À elle seule, elle explique le LCP de 15 s sur mobile. Un second facteur aggrave tout : **73 des 74 images de la page se chargent immédiatement (eager)**, ce qui sature la bande passante et retarde encore le hero.

La bonne nouvelle : les deux corrections les plus impactantes sont aussi les plus simples, et devraient suffire à passer le LCP sous 2,5 s et le score au-dessus de 85.

| Problème | Mesure réelle | Correction | Gain attendu |
|---|---|---|---|
| Hero PNG énorme (élément LCP) | 1,9 Mo / 1717×916 | → WebP ~80–120 Ko | **LCP 15 s → < 2 s** |
| 73 images en eager | 72 cartes sans `loading="lazy"` | lazy-load sous la ligne de flottaison | **Payload initial −70 à −80 %** |
| Pas de preconnect CDN images | 0 vers tr.rbxcdn.com | `<link rel=preconnect>` | −100 à −300 ms |
| Miniatures Roblox en PNG/trop grandes | 40 PNG, demandées en 768×432 | URL → WebP + 480×270 | Payload −40 à −60 % |
| Aucun cache configuré | pas de `.htaccess` | Cache-Control + gzip/Brotli | Visites répétées + payload |

---

## Réponses à tes 9 questions

### 1. Quel élément exact provoque le LCP de 15 s ?

**`<img class="hero-bg-img" src="images/hero-bg.png" fetchpriority="high">`** (section `.hero`, en haut de `index.html`).

C'est une image de fond plein écran, **PNG de 1,9 Mo (1888 Ko exactement, 1717×916 px)**, servie depuis l'origine Hostinger. Lighthouse mobile simule un réseau ~1,6 Mbit/s : 1,9 Mo ≈ **10 à 15 s** de téléchargement. C'est mathématiquement ton LCP.

`fetchpriority="high"` est bien présent (bon réflexe), mais ça ne sert à rien tant que le fichier fait 1,9 Mo. **Facteur aggravant** : 73 autres images partent en même temps et se disputent les ~6 connexions simultanées du navigateur, ce qui retarde encore la livraison du hero.

### 2. Quelles images doivent être optimisées ?

Par ordre de priorité :

1. **`images/hero-bg.png` (1,9 Mo)** — de loin la priorité absolue.
2. **Les 40 miniatures Roblox en PNG** sur la page d'accueil (format le plus lourd ; voir Q5).
3. `images/og-cover.png` (67 Ko) et `images/logo.png` (20 Ko) — mineur, mais à passer en WebP par cohérence.

Les SVG locaux (`images/games/*.svg`, 124 Ko au total pour ~85 fichiers) sont légers et servent de secours : rien à changer.

### 3. WebP ou AVIF ?

**WebP partout, par défaut.** Test concret sur le hero :

- PNG original : **1888 Ko**
- WebP même taille (q80) : **119 Ko** (−94 %)
- WebP redimensionné 1600 px (q72) : **83 Ko**
- WebP 800 px mobile (q70) : **29 Ko**
- AVIF 1600 px : **71 Ko**

AVIF est marginalement plus petit (71 vs 83 Ko) mais encode plus lentement et reste moins universel sur les vieux appareils. **Recommandation : WebP** (gain déjà énorme, support universel). Si tu veux gratter les derniers Ko, sert l'AVIF en plus via `<picture>` avec repli WebP — mais c'est optionnel et à faible enjeu.

Pour les miniatures Roblox, pas besoin de convertir des fichiers : il suffit de changer le format dans l'URL du CDN (voir Q5).

### 4. Le lazy loading est-il correctement utilisé ?

**Non.** Sur 74 `<img>`, **une seule** porte `loading="lazy"`. Les **72 cartes de jeux** (réparties sur 5 sections : « Nouveaux jeux », « Jeux populaires », « Récemment mis à jour », « Récemment ajoutés », « Tous les jeux Roblox ») se chargent **toutes immédiatement**, alors que la grande majorité est sous la ligne de flottaison.

Règle à appliquer :
- **Hero** : rester en eager + `fetchpriority="high"` (c'est le LCP, il NE doit PAS être lazy). ✅ déjà le cas.
- **Première rangée de cartes visible** (3–6 cartes) : eager.
- **Toutes les autres cartes** : `loading="lazy"` + `decoding="async"`.

### 5. Les miniatures Roblox sont-elles servies à une taille excessive ?

**Oui, deux fois.** Répartition réelle des URL tr.rbxcdn.com dans `index.html` :
- 51 demandées en **768×432**, 5 en 512×512, 14 en 500×280 ;
- formats : **40 PNG**, 16 WebP, 14 JPEG.

Or dans les cartes, l'image est affichée à environ **150–260 px de large**. On télécharge donc du 768 px pour l'afficher en ~240 px, et 40 d'entre elles en PNG (le format le plus lourd).

Correction (simple, juste l'URL) : demander **`/480/270/Image/Webp/noFilter`** au lieu de `/768/432/Image/Png/noFilter`. Le CDN de Roblox génère le WebP et la taille réduite à la volée. Gain typique : **−40 à −60 %** sur chaque miniature, sans rien réencoder.

### 6. Quels CSS/JS peuvent être réduits ?

- `css/style.css` : **28 Ko, 759 lignes, non minifié**.
- `js/main.js` : **28 Ko, 435 lignes, non minifié**.

La minification ferait gagner ~30–40 % (≈ 10 Ko chacun). **Impact réel faible** : les fichiers sont déjà petits et, d'après ton diagnostic, le render-blocking et le TBT ne sont pas des problèmes (TBT 60 ms). À faire en finition, pas en priorité. Le vrai gain « texte » viendra de la **compression gzip/Brotli** côté serveur (voir Q8), pas de la minification.

### 7. Faut-il activer un CDN ?

**Pas indispensable pour atteindre l'objectif, mais recommandé en second temps.**

- Les miniatures Roblox sont **déjà** sur un CDN (`tr.rbxcdn.com`).
- Tes assets locaux (hero, CSS, JS, SVG, og-cover) sont servis depuis l'origine Hostinger.

Mettre **Cloudflare (offre gratuite)** devant le domaine apporterait : cache en périphérie, **Brotli automatique**, HTTP/2-3, et TLS optimisé. C'est un bon « plus », mais le hero à 1,9 Mo reste 1,9 Mo même derrière un CDN tant qu'il n'est pas converti. **Priorité : d'abord les images (Q1-Q5), ensuite Cloudflare.**

### 8. Quels headers de cache configurer ?

Il n'y a **aucun `.htaccess`** → d'où le « Use efficient cache lifetimes ». Hostinger tourne sous Apache, donc un `.htaccess` à la racine suffit. Modèle prêt à l'emploi :

```apache
# --- Compression ---
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/xml
</IfModule>
<IfModule mod_brotli.c>
  AddOutputFilterByType BROTLI_COMPRESS text/html text/css application/javascript image/svg+xml
</IfModule>

# --- Cache ---
<IfModule mod_expires.c>
  ExpiresActive On
  # Images & polices : 1 an (immuables)
  ExpiresByType image/webp              "access plus 1 year"
  ExpiresByType image/png               "access plus 1 year"
  ExpiresByType image/jpeg              "access plus 1 year"
  ExpiresByType image/svg+xml           "access plus 1 year"
  ExpiresByType image/x-icon            "access plus 1 year"
  # CSS / JS : versionnés via ?v=15 → 1 an
  ExpiresByType text/css                "access plus 1 year"
  ExpiresByType application/javascript  "access plus 1 year"
  # HTML : court, car les codes changent chaque jour
  ExpiresByType text/html               "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
  <FilesMatch "\.(webp|png|jpg|jpeg|svg|ico|css|js)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\.html$">
    Header set Cache-Control "public, max-age=3600, must-revalidate"
  </FilesMatch>
</IfModule>
```

Note : le cache long sur CSS/JS est sûr **parce que tu utilises déjà le cache-busting `main.js?v=15`** — il suffit d'incrémenter le numéro à chaque modif (ce qui est déjà ta procédure).

### 9. Quelles optimisations = plus grand gain pour le moins d'effort ?

Classé par rapport impact/effort réel sur le score Lighthouse :

| Prio | Action | Effort | Impact Lighthouse |
|---|---|---|---|
| **P1** | Convertir `hero-bg.png` → WebP (1600 px) + `<picture>` repli | 15 min | ⭐⭐⭐⭐⭐ LCP 15 s → < 2 s |
| **P1** | `loading="lazy"` + `decoding="async"` sur les 72 cartes hors écran | 20 min | ⭐⭐⭐⭐ payload initial −70 % |
| **P2** | `preconnect` vers `tr.rbxcdn.com` (+ `fonts.gstatic.com`) | 5 min | ⭐⭐ −100 à −300 ms |
| **P2** | Miniatures Roblox : URL PNG 768×432 → WebP 480×270 | 20 min | ⭐⭐⭐ payload −40 à −60 % |
| **P3** | `.htaccess` (cache + gzip/Brotli) | 10 min | ⭐⭐ visites répétées + texte |
| **P4** | `width`/`height` sur chaque `<img>` (verrouille CLS=0) | 20 min | ⭐ robustesse |
| **P4** | Minifier CSS/JS | 10 min | ⭐ marginal |
| **P5** | Mettre Cloudflare devant le domaine | 30 min | ⭐⭐ latence/cache global |

**P1 + P1 suffisent très probablement à atteindre l'objectif** (LCP < 2,5 s, score > 85). Le reste consolide et améliore les visites répétées.

---

## Plan d'exécution recommandé

**Étape 1 — Le hero (le seul vrai problème de LCP)**
1. Générer `images/hero-bg.webp` (1600 px, q72 ≈ 83 Ko) + une version mobile 800 px (≈ 29 Ko).
2. Remplacer l'`<img>` par un `<picture>` : source WebP + repli PNG, en gardant `fetchpriority="high"` et **sans** `loading="lazy"`.
3. Ajouter un `<link rel="preload" as="image">` du WebP hero dans le `<head>`.

**Étape 2 — Lazy loading des cartes**
- Ajouter `loading="lazy" decoding="async"` à toutes les `img.thumb-svg` **sauf** les 3–6 premières de la première section.

**Étape 3 — Quick wins**
- `<link rel="preconnect" href="https://tr.rbxcdn.com">` et `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` dans le `<head>`.
- Remplacer dans les URL de miniatures `/768/432/Image/Png/` (et `/512/512/`) par `/480/270/Image/Webp/`.

**Étape 4 — Serveur**
- Déposer le `.htaccess` ci-dessus à la racine.

**Étape 5 — Finition (optionnel)**
- `width`/`height` sur les images, minification CSS/JS, Cloudflare.

---

## Note importante

Ces optimisations touchent `index.html` (et idéalement le gabarit des pages codes, qui chargent aussi des miniatures Roblox). Une fois faites, **re-tester sur PageSpeed Insights** en mobile : le LCP devrait s'effondrer dès l'étape 1.
