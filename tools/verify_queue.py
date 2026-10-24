#!/usr/bin/env python3
"""File de priorite de verification des codes (cadence decidee par Peter le 24/10/2026).

Regle : les hotGames sont verifies CHAQUE JOUR (run de 05h) ; toutes les autres pages
codes-<slug>.html au plus tard tous les 3 jours, reparties sur les runs 05h / 15h / 22h.

Source de verite : tools/code-watch.json -> catalogVerify {slug: "AAAA-MM-JJ"} (date de la
derniere verification REELLE contre une source datee). Slug absent = jamais verifie.

Usage :
  python3 tools/verify_queue.py --run 05h      # lot du run (05h inclut les hotGames)
  python3 tools/verify_queue.py --run 15h
  python3 tools/verify_queue.py --status       # etat global + pages en retard (> 3 jours)
  python3 tools/verify_queue.py --done slug1 slug2 ...   # enregistre une verification faite aujourd'hui

--done ne doit etre lance qu'apres une vraie verification (page modifiee OU confirmee
identique aux sources) : jamais pour "rajeunir" une date (regle d'honnetete).
Un jeu sous kill switch (sources contradictoires) compte comme verifie : la verification a eu
lieu, seule la modification a ete refusee ; le noter dans le rapport.
"""
import datetime, glob, json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCH = os.path.join(ROOT, 'tools', 'code-watch.json')
MAX_AGE = 3                      # jours max sans verification (pages non hot)
RUNS = ('05h', '15h', '22h')
EXCLUDE = {'promo-roblox'}       # page generique, pas un jeu
# Pages a fort trafic (GA4, pages de destination 26/09-23/10) : prioritaires a anciennete egale.
TRAFFIC = ['search-for-the-needle', 'anime-rng']


def load():
    with open(WATCH, encoding='utf-8') as f:
        return json.load(f)


def save(d):
    out = json.dumps(d, ensure_ascii=False, indent=2)
    json.loads(out)  # garde-fou : JSON valide avant ecriture
    with open(WATCH, 'w', encoding='utf-8', newline='') as f:
        f.write(out)


def slugs():
    out = []
    for f in glob.glob(os.path.join(ROOT, 'codes-*.html')):
        s = os.path.basename(f)[6:-5]
        if s not in EXCLUDE:
            out.append(s)
    return sorted(out)


def age(cv, s, today):
    d = cv.get(s)
    if not d:
        return None  # jamais verifie
    return (today - datetime.date.fromisoformat(d[:10])).days


def queue(d, today):
    cv = d.get('catalogVerify', {})
    hot = set(d.get('hotGames', {}))
    rest = [s for s in slugs() if s not in hot]
    # jamais verifies d'abord, puis les plus anciens, puis le trafic, puis l'ordre alphabetique
    rest.sort(key=lambda s: (age(cv, s, today) is not None, -(age(cv, s, today) or 0),
                             s not in TRAFFIC, s))
    return sorted(hot & set(slugs())), rest


def main(argv):
    today = datetime.date.today()
    d = load()
    cv = d.setdefault('catalogVerify', {})

    if argv[:1] == ['--done']:
        known = set(slugs())
        bad = [s for s in argv[1:] if s not in known]
        if bad:
            sys.exit('slug(s) inconnu(s) : ' + ', '.join(bad))
        for s in argv[1:]:
            cv[s] = today.isoformat()
        save(d)
        print(f'catalogVerify : {len(argv) - 1} jeu(x) dates du {today.isoformat()}')
        return

    hot, rest = queue(d, today)
    late = [s for s in rest if age(cv, s, today) is None or age(cv, s, today) > MAX_AGE]
    per_run = math.ceil(len(rest) / (MAX_AGE * len(RUNS)))

    if argv[:1] == ['--status'] or not argv:
        never = [s for s in rest if age(cv, s, today) is None]
        print(f'{len(hot)} hotGames (chaque jour) + {len(rest)} autres pages (max {MAX_AGE} jours)')
        print(f'quota par run : {per_run} pages non hot ({len(RUNS)} runs/jour)')
        print(f'en retard (> {MAX_AGE} j ou jamais) : {len(late)} dont {len(never)} jamais verifiees')
        for s in late[:40]:
            a = age(cv, s, today)
            print(f'   {s:40s} {"jamais" if a is None else str(a) + " j"}')
        if len(late) > 40:
            print(f'   ... et {len(late) - 40} autres')
        return

    if argv[:1] == ['--run'] and len(argv) > 1 and argv[1] in RUNS:
        # tant qu'il y a du retard, on prend au moins tout le retard du lot (rattrapage), plafonne a 2x le quota
        size = min(max(per_run, min(len(late), per_run * 2)), len(rest))
        batch = rest[:size]
        if argv[1] == '05h':
            print(f'HOT ({len(hot)}) : ' + ' '.join(hot))
        print(f'LOT {argv[1]} ({len(batch)}) : ' + ' '.join(batch))
        print(f'(en retard restant apres ce lot : {max(0, len(late) - len(batch))})')
        return

    sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
