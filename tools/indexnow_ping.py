#!/usr/bin/env python3
"""Notifie IndexNow (Bing, Yandex, Seznam, Naver...) des URL zoneblox.com creees ou modifiees.

Pourquoi : ~87 % du trafic vient de Bing et des moteurs adosses a son index (GA4, 24/10/2026).
IndexNow fait decouvrir une page en quelques heures au lieu d'attendre le crawl.

Cle : fichier <KEY>.txt a la racine du site (contenu = la cle). Il DOIT etre en ligne avant
le premier envoi (sinon l'API repond 403).

Usage (par defaut = simulation, rien n'est envoye) :
  python3 tools/indexnow_ping.py                      # URL du sitemap dont lastmod = aujourd'hui
  python3 tools/indexnow_ping.py --date 2026-10-24    # URL dont lastmod = cette date
  python3 tools/indexnow_ping.py --all                # tout le sitemap (une fois, a la mise en place)
  python3 tools/indexnow_ping.py URL [URL ...]        # URL explicites
  ... --send                                          # envoie reellement
A lancer APRES le deploiement (git push) et APRES tools/build_sitemap.py, sinon on annonce
des pages pas encore en ligne.
"""
import datetime, json, os, re, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'zoneblox.com'
KEY = '7534b22b542ba85accf9006eeae26f49'
ENDPOINT = 'https://api.indexnow.org/indexnow'
MAX_URLS = 10000  # limite par requete IndexNow


def sitemap_entries():
    out = []
    for name in ('sitemap.xml', 'sitemap-games.xml'):
        p = os.path.join(ROOT, name)
        if not os.path.exists(p):
            continue
        xml = open(p, encoding='utf-8').read()
        for block in re.findall(r'<url>(.*?)</url>', xml, re.S):
            loc = re.search(r'<loc>\s*([^<\s]+)\s*</loc>', block)
            mod = re.search(r'<lastmod>\s*([^<\s]+)\s*</lastmod>', block)
            if loc:
                out.append((loc.group(1), mod.group(1)[:10] if mod else ''))
    return out


def main(argv):
    send = '--send' in argv
    args = [a for a in argv if a != '--send']
    if not os.path.exists(os.path.join(ROOT, KEY + '.txt')):
        sys.exit(f'Fichier cle {KEY}.txt absent a la racine : abandon.')

    if args and args[0] == '--all':
        urls = [u for u, _ in sitemap_entries()]
    elif args and args[0] == '--date':
        urls = [u for u, d in sitemap_entries() if d == args[1]]
    elif args:
        urls = args
    else:
        today = datetime.date.today().isoformat()
        urls = [u for u, d in sitemap_entries() if d == today]

    urls = sorted({u for u in urls if u.startswith(f'https://{HOST}/')})
    if not urls:
        print('indexnow : aucune URL a notifier.')
        return
    print(f'indexnow : {len(urls)} URL' + ('' if send else ' (simulation, ajouter --send pour envoyer)'))
    for u in urls[:10]:
        print('  ', u)
    if len(urls) > 10:
        print(f'   ... et {len(urls) - 10} autres')
    if not send:
        return

    for i in range(0, len(urls), MAX_URLS):
        body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt',
                           'urlList': urls[i:i + MAX_URLS]}).encode('utf-8')
        req = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                     headers={'Content-Type': 'application/json; charset=utf-8'})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f'  envoi OK : HTTP {r.status}')  # 200 ou 202 = recu
        except urllib.error.HTTPError as e:
            # 403 = cle introuvable en ligne, 422 = URL hors du domaine, 429 = trop de requetes
            print(f'  ! envoi refuse : HTTP {e.code} {e.reason}')
            sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
