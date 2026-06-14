# Générateur d'avatar Roblox par budget — Zoneblox

Section **statique** de zoneblox.com. Outil 100 % informatif : il compose une idée
d'avatar Roblox selon un budget en Robux et un style, puis renvoie vers le catalogue
officiel Roblox. **Aucun achat, aucune connexion Roblox, rien à vendre.**

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | Page outil (formulaire budget/style + rendu de l'avatar). |
| `avatar.js` | Générateur côté client (algorithme de budget, partage URL, localStorage). |
| `data/items.json` | Catalogue mis en cache (nom, prix, slot, vignette). **Source de données.** |
| `build-items.mjs` | Script d'ingestion : régénère `data/items.json` depuis l'API Roblox. |
| `anime-500-robux.html`, `ninja-800-robux.html` | Pages SEO programmatiques (budget × style). |

## Rafraîchir / compléter le catalogue

Le fichier `data/items.json` livré est un **seed** (Anime + Ninja, données réelles).
Pour remplir les 4 styles (Anime, Ninja, Cyberpunk, Démon), tous les slots, et
rafraîchir prix + vignettes, lance depuis ce dossier :

```bash
node build-items.mjs
```

Requiert **Node 18+** (aucune dépendance npm). Le script interroge le catalogue
public Roblox, classe chaque objet par slot (cheveux, haut, bas, visage, chapeau,
dos…), récupère les vignettes rbxcdn et réécrit `data/items.json`.

> ⚠️ À lancer depuis ta machine (pas depuis un hébergement bridé) : l'API Roblox
> limite fortement les IP partagées. Relance-le ~1×/semaine pour garder les prix à jour.

## Ajouter un style

1. Ajoute une entrée dans `STYLES` de `build-items.mjs` (mots-clés de recherche).
2. Relance `node build-items.mjs`.
3. Le `<select>` de style se remplit automatiquement depuis `items.json`.

## Déploiement

Rien de spécial : ce sont des fichiers statiques. Copie le dossier `avatar/` à la
racine du site (même Hostinger que le reste de Zoneblox). Aucun serveur ni base de
données nécessaire.

## Pages SEO supplémentaires

Duplique `anime-500-robux.html`, change le titre/meta/H1 et le lien CTA
(`/avatar/#b=BUDGET&s=STYLE`). Ajoute l'URL au `sitemap.xml`.
