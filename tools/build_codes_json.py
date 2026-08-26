#!/usr/bin/env python3
"""Genere data/codes.json a partir des pages codes-<slug>.html servies.
A relancer a chaque run quotidien (apres MAJ des codes) pour que le widget
embed/codes.js affiche des donnees fraiches. Sortie : data/codes.json (JSON valide)."""
import glob, re, json, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def extract(path):
    h = open(path, encoding='utf-8').read()
    slug = os.path.basename(path)[6:-5]  # codes-<slug>.html
    tm = re.search(r'<title>\s*Codes\s+(.+?)\s*(?:\(|—|\|)', h)
    name = html.unescape(tm.group(1).strip()) if tm else slug
    vm = re.search(r'id="verifDate"[^>]*>([^<]+)', h)
    verified = vm.group(1).strip() if vm else ''
    thm = re.search(r'src="(https://tr\.rbxcdn\.com/[^"]+)"', h)
    thumb = thm.group(1) if thm else ''
    codes = []
    i = h.find('id="activeList">')
    if i != -1:
        j = h.find('</section>', i)
        seg = h[i:j]
        for m in re.finditer(r'<code>([^<]+)</code>(?:<span[^>]*>[^<]*</span>)?</div><div class="desc"><div class="reward">([^<]*)</div>', seg):
            codes.append({'code': html.unescape(m.group(1).strip()),
                          'reward': html.unescape(m.group(2).strip())})
    return slug, {'name': name, 'slug': slug, 'thumb': thumb,
                  'verified': verified, 'count': len(codes), 'codes': codes}

def main():
    out = {}
    for f in sorted(glob.glob('codes-*.html')):
        slug, data = extract(f)
        out[slug] = data
    payload = {'meta': {'source': 'https://zoneblox.com', 'games': len(out)}, 'games': out}
    os.makedirs('data', exist_ok=True)
    with open('data/codes.json', 'w', encoding='utf-8') as fh:
        json.dump(payload, fh, ensure_ascii=False, separators=(',', ':'))
    total = sum(g['count'] for g in out.values())
    print(f'data/codes.json ecrit : {len(out)} jeux, {total} codes actifs au total')

if __name__ == '__main__':
    main()
