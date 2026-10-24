"""Reduction of ethyl propanoate by LiAlH4. A hydride adds to the carbonyl carbon; the tetrahedral
intermediate collapses, the alkoxide pushing back and ethoxide leaving, so an aldehyde is formed. The
aldehyde is more reactive than the ester and takes the second hydride at once; workup gives
propan-1-ol (and ethanol). Al is omitted from the alkoxides."""

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
al = s.molecule("[H][Al-]([H])([H])[H]", coords=[(0.0, 1.0), (0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (1.0, 0.0)], at=(-2.3, 1.2))
est = s.molecule("CCC(=O)OCC", coords=[(-1.74, -1.0), (-0.87, -0.5), (0.0, -1.0), (0.0, -2.0), (0.87, -0.5), (1.74, -1.0), (2.61, -0.5)], lone_pairs=[3])
s.curly(al.bond(1, 4), est.atom(2), bend=-0.5)
s.curly(est.bond(2, 3), est.atom(3), bend=-0.8)
(ti,), x = row(s, [("arrow", None), ("CCC([H])([O-])OCC", {"coords": [(-1.74, 0.0), (-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (-0.3, -1.0), (0.87, 0.5),
                                                                       (1.74, 0.0), (2.61, 0.5)], "lone_pairs": [4]})], x=3.0, y=-1.0)
s.curly(ti.atom(4), ti.bond(2, 4), bend=0.8)
s.curly(ti.bond(2, 5), ti.atom(5), bend=-0.7)
row(s, [("arrow", r"$-$EtO$^-$"), "CCC=O", ("arrow", r"AlH$_4^-$", r"then H$_3$O$^+$"), "CCCO"], x=x, y=-1.0)
s.draw()
