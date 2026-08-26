# Plan d'action SEO Zoneblox — d'après GSC (26 août 2026)

## Diagnostic (28 j : 28 juil → 24 août 2026)
- **≈1 238 impressions · 4 clics · CTR 0,3 % · position moyenne ~53**, en dégradation (~40 → ~67 sur le mois).
- Cause n°1 identifiée : **migration d'URL `/codes/` → `/codes-` mal finalisée côté sitemaps** → signaux coupés en deux, chute de position.
- Le site ne rank #1 que sur ses slugs FR maison (volume ~0). Les requêtes à volume sont en position 60–88.
- Cluster **tier lists = meilleur actif** (meilleures positions, plus d'impressions).

---

## ✅ P0 — Nettoyage technique (FAIT dans le repo, à publier)
1. **`sitemap-codes.xml` réécrit** : 180 vieilles URLs `/codes/…` redirigées → **177 URLs servies `codes-…`** (0 redirigée).
2. **URLs de hub redirigées corrigées** dans `sitemap-guides.xml` (`/guides/`→`/guides.html`), `sitemap-tier-list.xml` (`/tier-list/`→`/tier-lists.html`), `sitemap-pages.xml` (`/about.html`→`/a-propos.html`, `/ugc-gratuit/`→`/ugc-gratuits.html`).
3. **Carte Steal An Egg replacée sur le vrai hub** `tier-lists.html` (elle était sur `/tier-list/index.html`, page masquée par une redirection).
4. Tous les sitemaps validés : XML correct, **0 URL redirigée restante**.

### À faire par toi dans Google Search Console (5 min)
1. **Sitemaps** → garde **uniquement `sitemap.xml`** soumis (il contient déjà les 317 URLs propres). Supprime les soumissions des vieux sous-sitemaps s'ils y sont, ou resoumets-les (ils sont maintenant propres).
2. **Inspection d'URL → Demander une indexation** sur ces 15 pages prioritaires (les URLs **servies**, pas les `/codes/…`) :

```
https://zoneblox.com/
https://zoneblox.com/tous-les-codes.html
https://zoneblox.com/tier-lists.html
https://zoneblox.com/tier-list/grand-piece-online.html
https://zoneblox.com/tier-list/peroxide.html
https://zoneblox.com/tier-list/anime-adventures.html
https://zoneblox.com/tier-list/king-legacy.html
https://zoneblox.com/tier-list/blue-lock-rivals.html
https://zoneblox.com/tier-list/anime-last-stand.html
https://zoneblox.com/tier-list/steal-an-egg.html
https://zoneblox.com/codes-royale-high.html
https://zoneblox.com/codes-steal-a-brainrot.html
https://zoneblox.com/codes-mad-city.html
https://zoneblox.com/codes-brookhaven.html
https://zoneblox.com/guides.html
```

3. **Vérifie la couverture** (Pages → « Pourquoi les pages ne sont pas indexées ») : tu devrais voir chuter les « Page avec redirection » dans les semaines qui suivent.

---

## ⏭️ Prochaines phases (à valider avec toi)

**P1 — Concentrer (au lieu de disperser)**
- Choisir 10–15 jeux à vrai volume FR et en faire des pages best-in-class, maillées depuis la home.
- Renforcer le cluster tier lists (le plus performant).
- Nettoyer/fusionner les pages fines qui ne rankent pas.

**P2 — Liens internes & rich results**
- **Corriger la nav** : elle pointe vers `/tier-list/`, `/guides/`, `/ugc-gratuit/`, `/about.html` (toutes **redirigées 301**). Les faire pointer vers `/tier-lists.html`, `/guides.html`, `/ugc-gratuits.html`, `/a-propos.html` sur les ~326 pages → récupère l'equity interne gaspillée.
- Valider le schema FAQ/Breadcrumb dans le test de résultats enrichis Google (rapport « Apparence » vide = aucun rich result servi).
- Optimiser la home pour « zoneblox » + « codes roblox français ».

**P3 — Autorité (levier long terme)**
- Backlinks : descriptions YouTube de créateurs Roblox FR, subreddits, serveurs Discord, forums. Sans liens entrants, la position ne montera pas.

**Option (destructive, ton feu vert requis)** : supprimer les 176 fichiers `codes/<slug>.html` obsolètes du repo (les 301 restent dans `.htaccess`).
