#!/usr/bin/env python3
"""Synchronise le libelle de mois SEO ((<mois> <annee>) et 'de/d'<mois> <annee>')
dans le <head> des pages codes-<slug>.html vers le MOIS COURANT.

But : eviter le decalage "title = septembre / description = aout" reste sur une page
(constate le 11/09/2026). Ne touche QUE le <head> (title, og:title, meta description) :
jamais le corps, jamais les codes, jamais les dates "Verifie le" / "Mis a jour".

Idempotent (relancer = no-op si deja a jour). A lancer a chaque debut de mois, et sans
risque a chaque run quotidien. Verifier apres : aucune page ne doit finir sans </html>.
Usage : python3 tools/sync_month.py
"""
import glob, re, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
        'août', 'septembre', 'octobre', 'novembre', 'décembre']

now = datetime.date.today()
CUR_MOIS = MOIS[now.month - 1]
CUR_AN = str(now.year)
# élision : "d'avril / d'août / d'octobre" sinon "de <mois>"
_prem = CUR_MOIS[0].lower()
DE_PHRASE = (f"d'{CUR_MOIS}" if _prem in 'aâàeéèêiîoôuûh' else f"de {CUR_MOIS}")

# tous les mois FR (avec/sans accent) pour la detection
_MOISPAT = ('(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|'
            'août|aout|septembre|octobre|novembre|décembre|decembre)')

PAT_PAREN = re.compile(r'\(' + _MOISPAT + r'\s+20\d{2}\)')
PAT_DESC = re.compile(r"(?:d['’]|de )" + _MOISPAT + r"\s+20\d{2}")


def sync_head(head):
    head = PAT_PAREN.sub(f'({CUR_MOIS} {CUR_AN})', head)
    head = PAT_DESC.sub(f'{DE_PHRASE} {CUR_AN}', head)
    return head


def main():
    changed = 0
    for f in sorted(glob.glob('codes-*.html')):
        h = open(f, encoding='utf-8').read()
        i = h.find('</head>')
        if i == -1:
            print(f'  ! {f} : pas de </head>, ignore')
            continue
        head, rest = h[:i], h[i:]
        new_head = sync_head(head)
        if new_head == head:
            continue
        out = new_head + rest
        # garde-fous anti-troncature
        if not out.rstrip().endswith('</html>') or '\x00' in out:
            print(f'  ! {f} : sortie suspecte, NON ecrit')
            continue
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(out)
        changed += 1

    print(f'sync_month : mois courant = {CUR_MOIS} {CUR_AN} ("{DE_PHRASE} {CUR_AN}")')
    print(f'  pages mises a jour : {changed}')


if __name__ == '__main__':
    main()
