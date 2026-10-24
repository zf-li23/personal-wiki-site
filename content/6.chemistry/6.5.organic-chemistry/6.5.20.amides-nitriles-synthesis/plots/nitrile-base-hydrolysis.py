"""Base-promoted hydrolysis of a nitrile (acetonitrile). Hydroxide adds to the electrophilic nitrile
carbon and the C-N pi pair moves onto nitrogen; the nitrogen anion takes a proton from water, giving the
imidic acid, which tautomerizes to acetamide. Under the same hot, basic conditions the amide is
hydrolysed further to the carboxylate and ammonia."""

from wikichem import Scheme

import math


def extent(smiles, **kw):
    """Horizontal extent of a structure as it would be drawn (laid out on a scratch scheme)."""
    c = Scheme().molecule(smiles, **kw).coords
    return c[:, 0].min(), c[:, 0].max()


def row(s, items, x=0.0, y=0.0, gap=0.7, arrow=1.5):
    """Lay out structures, plus signs and reaction arrows from left to right; returns the placed molecules and the end x."""
    placed = []
    for it in items:
        if isinstance(it, tuple) and it[0] == "arrow":
            s.arrow((x + 0.1, y), (x + 0.1 + arrow, y), above=it[1], below=it[2] if len(it) > 2 else None)
            x += arrow + 0.2
        elif it == "+":
            s.plus((x + 0.45, y))
            x += 0.9
        else:
            smi, kw = (it, {}) if isinstance(it, str) else it
            lo, hi = extent(smi, **kw)
            m = s.molecule(smi, at=(x + gap - lo, y), **kw)
            placed.append(m)
            x += gap + (hi - lo) + gap
    return placed, x


def turn(smiles, i, j, target, **kw):
    """The rotate= value that makes the bond from atom i to atom j point at the target angle (degrees)."""
    m = Scheme().molecule(smiles, **kw)
    d = m.xy(j) - m.xy(i)
    return target - math.degrees(math.atan2(d[1], d[0]))


def ring(centre, start, n=6, r=None):
    """Corner coordinates of a regular n-gon with unit edges, starting at angle start (degrees), counterclockwise."""
    r = r or 1 / (2 * math.sin(math.pi / n))
    return [(centre[0] + r * math.cos(math.radians(start + 360 * k / n)), centre[1] + r * math.sin(math.radians(start + 360 * k / n)))
            for k in range(n)]

s = Scheme()
oh = s.molecule("[OH-]", at=(-0.4, 1.6), lone_pairs=True)
ni = s.molecule("CC#N", coords=[(-0.87, -0.5), (0.0, 0.0), (1.0, 0.0)], lone_pairs=[2])
s.curly(oh.atom(0), ni.atom(1), bend=0.4)
s.curly(ni.bond(1, 2), ni.atom(2), bend=0.8)
(im,), x = row(s, [("arrow", None), ("CC(O)=[N-]", {"coords": [(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5)], "lone_pairs": [3]})],
               x=1.6, y=0.0)
w = s.molecule("O[H]", coords=[(0.0, 0.0), (0.9, 0.0)], at=(im.xy(3)[0] - 0.2, im.xy(3)[1] - 1.5), lone_pairs=[0])
s.curly(im.atom(3), w.atom(1), bend=-0.5)
s.curly(w.bond(0, 1), w.atom(0), bend=-0.8)
row(s, [("arrow", r"$-$HO$^-$"), "CC(O)=N"], x=x, y=0.0)
row(s, [("arrow", "tautomerism"), "CC(N)=O", ("arrow", r"HO$^-$, heat"), "CC(=O)[O-]", "+", "N"], x=0.0, y=-4.0, arrow=2.2)
s.draw()
