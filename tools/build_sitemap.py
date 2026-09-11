#!/usr/bin/env python3
"""Regenere sitemap.xml en mettant le <lastmod> de chaque page a jour a partir
de son vrai etat de fraicheur, au lieu d'une date figee.

Priorite pour le lastmod de chaque URL :
  1. date "Vérifié le" (id="verifDate") de la page  -> signal quotidien des pages codes
  2. sinon date "Mis à jour le <date>" trouvee dans la page
  3. sinon date de derniere modification du fichier (mtime)

Le JEU d'URL, les <priority> et <changefreq> existants sont PRESERVES a l'identique :
le script ne fait que rafraichir les <lastmod>. A relancer a chaque run quotidien
(apres la MAJ des codes) : python3 tools/build_sitemap.py
Sortie : sitemap.xml (XML valide, se termine par </urlset>)."""
import os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SITEMAP = 'sitemap.xml'
DOMAIN = 'https://zoneblox.com'

MOIS = {
    'janvier': '01', 'fevrier': '02', 'février': '02', 'mars': '03',
    'avril': '04', 'mai': '05', 'juin': '06', 'juillet': '07',
    'aout': '08', 'août': '08', 'septembre': '09', 'octobre': '10',
    'novembre': '11', 'decembre': '12', 'décembre': '12',
}

DATE_RE = re.compile(r'(\d{1,2})\s+([A-Za-zéû:ô]+)\s+(\d{4})')


def fr_to_iso(txt):
    """'10 septembre 2026' -> '2026-09-10' ; None si non parsable."""
    if not txt:
        return None
    m = DATE_RE.search(txt)
    if not m:
        return None
    jour, mois, annee = m.group(1), m.group(2).lower(), m.group(3)
    mm = MOIS.get(mois)
    if not mm:
        return None
    return f'{annee}-{mm}-{int(jour):02d}'


def loc_to_path(loc):
    """URL absolue -> chemin de fichier local, ou None."""
    rel = loc[len(DOMAIN):] if loc.startswith(DOMAIN) else loc
    rel = rel.lstrip('/')
    if rel == '' or rel.endswith('/'):
        rel = rel + 'index.html'
    return rel


def page_lastmod(path, fallback):
    """Determine le lastmod ISO d'une page selon la priorite documentee."""
    if not os.path.isfile(path):
        return fallback, 'absent'
    h = open(path, encoding='utf-8', errors='replace').read()
    # 1. Verifié le (verifDate)
    m = re.search(r'id="verifDate"[^>]*>([^<]+)', h)
    iso = fr_to_iso(m.group(1)) if m else None
    if iso:
        return iso, 'verifDate'
    # 2. Mis à jour le <date>
    m = re.search(r'Mis à jour(?:\s+le)?\s*(?:</?strong>\s*)?([0-9][^<]{3,30})', h)
    iso = fr_to_iso(m.group(1)) if m else None
    if iso:
        return iso, 'maj'
    # 3. mtime du fichier
    ts = datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
    return ts, 'mtime'


def main():
    if not os.path.isfile(SITEMAP):
        sys.exit(f'ERREUR : {SITEMAP} introuvable')
    xml = open(SITEMAP, encoding='utf-8').read()

    stats = {'verifDate': 0, 'maj': 0, 'mtime': 0, 'absent': 0}
    urls = list(re.finditer(r'<url>.*?</url>', xml, re.DOTALL))
    if not urls:
        sys.exit('ERREUR : aucune balise <url> trouvee, sitemap inattendu')

    new_blocks = []
    for m in urls:
        block = m.group(0)
        locm = re.search(r'<loc>(.*?)</loc>', block)
        if not locm:
            new_blocks.append(block)
            continue
        loc = locm.group(1).strip()
        old_lm = re.search(r'<lastmod>(.*?)</lastmod>', block)
        old_lm = old_lm.group(1).strip() if old_lm else datetime.date.today().isoformat()
        path = loc_to_path(loc)
        iso, src = page_lastmod(path, old_lm)
        stats[src] += 1
        # remplace le lastmod existant, sinon l'insere apres </loc>
        if re.search(r'<lastmod>.*?</lastmod>', block):
            block = re.sub(r'<lastmod>.*?</lastmod>', f'<lastmod>{iso}</lastmod>', block)
        else:
            block = block.replace('</loc>', f'</loc><lastmod>{iso}</lastmod>', 1)
        new_blocks.append(block)

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    body = '\n'.join('  ' + b for b in new_blocks)
    out = header + body + '\n</urlset>\n'

    # garde-fou anti-troncature avant ecriture
    assert out.rstrip().endswith('</urlset>'), 'sortie invalide (pas de </urlset>)'
    assert '\x00' not in out, 'null byte detecte'
    with open(SITEMAP, 'w', encoding='utf-8') as fh:
        fh.write(out)

    print(f'{SITEMAP} regenere : {len(urls)} URLs')
    print(f"  lastmod issus de : verifDate={stats['verifDate']}, "
          f"Mis a jour={stats['maj']}, mtime={stats['mtime']}, fichier absent={stats['absent']}")
    if stats['absent']:
        print('  (les URLs sans fichier local ont garde leur ancien lastmod)')


if __name__ == '__main__':
    main()
