"""Hydrolysis of an isocyanide in dilute acid (alpha-addition). The terminal carbon, with its lone
pair, takes a proton and becomes the carbon of a nitrilium ion; water adds to the same carbon and the
C-N pi pair moves onto nitrogen. Loss of a proton and tautomerization give the N-alkylformamide, so
the isocyanide carbon ends up as a formyl group rather than a carboxyl group."""

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
iso = s.molecule("*[N+]#[C-]", coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)], labels={0: "R"}, lone_pairs=[2])
h3o = s.molecule("[H][OH2+]", coords=[(2.0, 0.6), (2.8, 1.1)])
s.curly(iso.atom(2), h3o.atom(0), bend=0.5)
s.curly(h3o.bond(0, 1), h3o.atom(1), bend=0.8)
_, x = row(s, [("arrow", r"$-$H$_2$O")], x=3.4, y=0.0)
w = s.molecule("O", at=(x + 2.2, 1.4), lone_pairs=True)
ni = s.molecule("*[N+]#C", coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)], labels={0: "R"}, at=(x + 1.4, 0.0))
s.curly(w.atom(0), ni.atom(2), bend=-0.4)
s.curly(ni.bond(1, 2), ni.atom(1), bend=0.8)
row(s, [("arrow", r"$-$H$^+$")], x=x + 3.2, y=0.0)
row(s, [("arrow", None), ("*N=CO", {"labels": {0: "R"}}), ("arrow", "tautomerism"), ("*NC=O", {"labels": {0: "R"}})], x=0.0, y=-2.6, arrow=2.2)
s.draw()
