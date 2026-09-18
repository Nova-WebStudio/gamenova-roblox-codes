# Plan d'indexation Search Console — 14 septembre 2026

Objectif : débloquer l'indexation après la migration (schéma plat `codes-<jeu>.html` + consolidation www/`/codes/`). Diagnostic : Google est resté sur l'ancien jeu d'URL parce que le sitemap n'a pas été relu depuis le 1er juillet. On force la reprise.

---

## 1. À faire en premier dans Search Console (5 min)

1. **Propriété** : vérifie que tu utilises la propriété **Domaine** `zoneblox.com` (couvre www + non-www + http/https). Sinon, crée-la (vérification DNS) — c'est ce qui fait disparaître les doublons `www.` de tes rapports.
2. **Sitemaps** → supprime l'ancienne entrée si besoin, puis (re)soumets :
   `https://zoneblox.com/sitemap.xml`
3. **Rapport « Indexation des pages »** → sur les motifs **« Page avec redirection »** et **« Introuvable (404) »** → bouton **« Valider la correction »** (Google recrawle les vieilles URL, voit les 301/le contenu, et met à jour).
4. **Inspection d'URL** → « Demander l'indexation » sur les URL des lots ci-dessous (quota ~10-15/jour, d'où le découpage).

> ⚠️ Les correctifs `.htaccess` (paint-and-seek, voir §4) ne seront actifs qu'**après un `git push`** et le déploiement Hostinger. Fais le push AVANT de lancer « Valider la correction ».

---

## 2. URL à soumettre (Inspection d'URL → Demander l'indexation)

Toutes ces URL renvoient un **200** (ce sont les bonnes adresses actuelles). Soumets-les dans cet ordre.

### Lot 1 — Hubs + gros jeux (jour 1)
```
https://zoneblox.com/
https://zoneblox.com/tous-les-codes.html
https://zoneblox.com/tier-lists.html
https://zoneblox.com/guides.html
https://zoneblox.com/codes-blox-fruits.html
https://zoneblox.com/codes-grow-a-garden.html
https://zoneblox.com/codes-steal-a-brainrot.html
https://zoneblox.com/codes-blade-ball.html
https://zoneblox.com/codes-anime-last-stand.html
https://zoneblox.com/codes-fisch.html
```

### Lot 2 — Autres jeux prioritaires (jour 2)
```
https://zoneblox.com/codes-blue-lock-rivals.html
https://zoneblox.com/codes-volleyball-legends.html
https://zoneblox.com/codes-anime-vanguards.html
https://zoneblox.com/codes-fruit-battlegrounds.html
https://zoneblox.com/codes-king-legacy.html
https://zoneblox.com/codes-pet-simulator-99.html
https://zoneblox.com/codes-grand-piece-online.html
https://zoneblox.com/codes-adopt-me.html
https://zoneblox.com/codes-dig.html
https://zoneblox.com/codes-pet-simulator-x.html
```

### Lot 3 — Reste de ta liste GSC, nouvelles adresses (jour 3)
```
https://zoneblox.com/codes-wizard-alchemy.html
https://zoneblox.com/codes-evomon.html
https://zoneblox.com/codes-hypershot.html
https://zoneblox.com/codes-dead-rails.html
https://zoneblox.com/codes-war-tycoon.html
https://zoneblox.com/codes-blox-monsters.html
https://zoneblox.com/codes-tower-defense-simulator.html
https://zoneblox.com/codes-anime-apocalypse.html
https://zoneblox.com/codes-anime-eternal.html
https://zoneblox.com/codes-ro-ghoul.html
```

### Lot 4 — Fin de ta liste GSC (jour 4)
```
https://zoneblox.com/codes-survive-zombie-arena.html
https://zoneblox.com/codes-grimoires-era.html
https://zoneblox.com/codes-be-a-brainrot.html
https://zoneblox.com/codes-spin-a-brainrot.html
https://zoneblox.com/codes-scroll-a-brainrot.html
https://zoneblox.com/codes-muscle-legends.html
https://zoneblox.com/codes-steal-a-fish.html
https://zoneblox.com/codes-car-dealership-tycoon.html
https://zoneblox.com/codes-type-soul.html
https://zoneblox.com/codes-sonic-speed-simulator.html
```

### Lot 5 — Guides & tier lists (URL actuelles, NON redirigées — prioritaires car « explorées, non indexées ») (jour 5)
```
https://zoneblox.com/guides/blox-fruits.html
https://zoneblox.com/guides/king-legacy.html
https://zoneblox.com/guides/anime-warriors-iii.html
https://zoneblox.com/guides/build-a-ring-farm.html
https://zoneblox.com/guides/paint-and-seek.html
https://zoneblox.com/tier-list/anime-warriors-iii.html
https://zoneblox.com/tier-list/broken-blade.html
https://zoneblox.com/tier-list/fish-it.html
https://zoneblox.com/tier-list/blox-fruits.html
https://zoneblox.com/tier-list/king-legacy.html
```

---

## 3. Correspondance ancienne URL (ce que tu voyais) → nouvelle URL

Les `/codes/<jeu>.html` de ta liste sont d'**anciennes adresses** qui redirigent (301). Ne les soumets pas : soumets/vérifie leur destination.

| Ancienne (redirige, ne s'indexe pas) | Nouvelle (à soumettre) |
|---|---|
| `/codes/dig.html` | `/codes-dig.html` |
| `/codes/wizard-alchemy.html` | `/codes-wizard-alchemy.html` |
| `/codes/evomon.html` | `/codes-evomon.html` |
| `/codes/blade-ball.html` | `/codes-blade-ball.html` |
| `/codes/blox-fruits.html` | `/codes-blox-fruits.html` |
| `/codes/paint-and-seek.html` | **→ `/guides/paint-and-seek.html`** (voir §4) |
| `/tier-list/anime-warriors-iii.html` | inchangée (déjà la bonne) |
| `/guides/blox-fruits.html` | inchangée (déjà la bonne) |

(Même logique pour toutes les autres `/codes/<jeu>.html` de ta liste : ajoute simplement le tiret → `codes-<jeu>.html`.)

---

## 4. Bug corrigé ce jour : `/codes/paint-and-seek.html`

Ce jeu a un **guide** et une **tier list** mais **pas de page codes** (`codes-paint-and-seek.html` n'existe pas). L'ancienne URL redirigeait donc en 301 vers une page **404**.

**Correctif appliqué** dans `.htaccess` : `/codes/paint-and-seek.html` → `301` → `/guides/paint-and-seek.html` (règle placée avant la règle générique). Actif après `git push`.

---

## 5. À relancer dès que le sandbox/bash refonctionne

- `python3 tools/build_sitemap.py` — rafraîchit les `<lastmod>` (ceux des guides/tier-list sont encore figés au 01/09).
- **Audit des cibles de redirection** (détecter d'autres cas « paint-and-seek », c.-à-d. un ancien `/codes/<jeu>.html` qui redirige vers un `codes-<jeu>.html` inexistant) :
  ```bash
  # liste les cibles de redirection .htaccess sans fichier correspondant
  grep -oE '/codes-[a-z0-9-]+\.html' .htaccess | sort -u | while read u; do
    f=".${u}"; [ -f "$f" ] || echo "CIBLE MANQUANTE: $u";
  done
  ```

---

## 6. Pour publier
```
git add -A && git commit -m "Fix redirect paint-and-seek + plan indexation" && git push origin main
```
Puis, dans Search Console : resoumettre le sitemap et lancer « Valider la correction ». Compter 2 à 6 semaines pour que l'index bascule (domaine jeune).
