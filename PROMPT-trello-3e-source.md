# Ajout au prompt de la tâche quotidienne — Trello comme 3ᵉ source de codes

> À coller **dans l'ÉTAPE 0** du prompt de la tâche planifiée (juste après la vérification du shout de groupe). Le mécanisme s'appuie sur le champ `trello` déjà ajouté à chaque jeu dans `tools/code-watch.json`.

## Texte à insérer dans ÉTAPE 0

```
3-bis. TRELLO DES DEVS (3e source). Pour chaque jeu de hotGames dont le champ `trello` n'est pas null et dont `trello.codes` vaut "list" ou "card" :
   - Ouvre le board JSON via le navigateur Chrome (le shell n'a pas de réseau) : navigate vers `trello.url` (ex. https://trello.com/b/imb75BzG.json). Si la page est trop grosse pour get_page_text, exécute du JavaScript dans l'onglet trello.com (fetch same-origin) :
       const d = await fetch(trelloUrl).then(r=>r.json());
       const lists = Object.fromEntries(d.lists.map(l=>[l.id,l.name]));
   - Si `trello.codes` == "list" : récupère les cartes des listes dont le nom contient « code » → chaque NOM de carte = un code, sa description = la récompense.
       d.cards.filter(c=>!c.closed && /code/i.test(lists[c.idList])).map(c=>({code:c.name, reward:c.desc}))
   - Si `trello.codes` == "card" : trouve la carte nommée « Codes » (ou `trello.listMatch`) et extrais les codes de sa `desc` (souvent une liste markdown) et/ou de sa checklist.
   - VALIDATION OBLIGATOIRE avant toute écriture :
       • Vérifie que `d.name` correspond bien au jeu (anti-bug ID, cf. CLAUDE.md).
       • Le Trello compte pour UNE seule source. Il peut être OBSOLÈTE (constaté sur Anime Last Stand : Trello en retard sur les codes réels du jeu). Donc :
           - Ne PUBLIE un code vu sur le Trello que s'il est corroboré par une 2e source fiable (Pro Game Guides, Beebom, Pocket Tactics…) OU par la description in-game.
           - Ne RETIRE jamais un code de la page au seul motif qu'il manque sur le Trello.
       • Le Trello sert surtout à DÉTECTER vite un nouveau code (carte ajoutée) → on le passe ensuite par la vérification 2-sources de l'ÉTAPE 2.
   - Met à jour `trello.checked` = date du jour. Si le board renvoie 401/erreur, passe `trello.codes` à "private" et signale-le.
   - Si un jeu hot a `trello` == null, tente (max 1-2 par run) de trouver son board officiel (recherche « <jeu> trello »), valide qu'une liste/carte « Codes » existe réellement, puis renseigne `trello` ; sinon laisse null.
```

## État vérifié des boards (26 juin 2026)

| Jeu | Board | Codes sur le Trello ? | Format |
|-----|-------|------------------------|--------|
| **blox-fruits** | `imb75BzG` | ✅ oui | liste « Codes » (1 carte = 1 code) |
| **anime-last-stand** | `m1Mqaqkh` | ✅ oui (mais board en retard) | carte « Codes » (desc markdown) |
| volleyball-legends | `W659ag0P` | ❌ non | carte « In-Game Codes » = tuto de saisie seulement |
| king-legacy | `pb6yySnh` | ❌ non | board réduit (liste « Information ») |
| fisch | `k8WMQFb3` | ❌ non | wiki uniquement |
| fruit-battlegrounds | `NjZf12R5` | ❌ non | listes sans nom, pas de codes |
| blue-lock-rivals | `R9gCGamp` | 🔒 privé (401) | inaccessible |
| blade-ball | `xdplf9oF` | 🔒 privé/non autorisé | codes sur Discord/X |
| grow-a-garden | — | ❌ pas de board officiel | Discord uniquement |
| steal-a-brainrot | — | ❌ pas encore de board | Discord uniquement |
| anime-vanguards | — | ❌ pas de board officiel | Discord/Wiki |

**Conclusion honnête :** parmi les jeux hot, seuls **Blox Fruits** et **Anime Last Stand** publient réellement les valeurs de codes sur leur Trello. Pour la plupart des autres, les codes tombent sur Discord/X — le Trello ne contient que du wiki. Le champ `trello` reflète cette réalité jeu par jeu (`none` / `private` / `absent`), et les jeux récents non vérifiés sont à `null` (à compléter au fil des runs).

## Technique fiable (rappel)
- Le shell bash n'a PAS de réseau et l'API thumbnails est bloquée → tout passe par **Chrome**.
- Le endpoint public `https://trello.com/b/<boardId>.json` renvoie tout le board en JSON. S'il est trop volumineux pour `get_page_text`, rester sur un onglet `trello.com` et faire un `fetch()` same-origin en JavaScript, puis filtrer côté page (ne renvoyer que les listes/cartes « code »).
