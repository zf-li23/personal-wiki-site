"""Acid-catalysed lactonization of 4-hydroxybutanoic acid. The carbonyl oxygen is protonated and the
hydroxy group at the other end of the chain, held close by the chain, adds to the activated carbonyl
carbon (an intramolecular Fischer esterification); the five-membered tetrahedral intermediate loses
water and a proton to give gamma-butyrolactone. The equilibrium lies far on the side of the lactone."""

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
p = ring((0.0, 0.0), 162, n=5)  # O(H) at 162 deg, then C-gamma, C-beta, C-alpha, C1
ha = s.molecule("OCCCC(O)=[OH+]", coords=[p[0], p[1], p[2], p[3], p[4], (p[4][0] + 0.95, p[4][1] + 0.3), (p[4][0] - 0.25, p[4][1] + 0.95)],
                lone_pairs=[0])
s.curly(ha.atom(0), ha.atom(4), bend=-0.4)
s.curly(ha.bond(4, 6), ha.atom(6), bend=0.8)
row(s, [("arrow", None), "OC1(O)CCC[OH+]1", ("arrow", r"$-$H$_2$O", r"$-$H$^+$"), "O=C1CCCO1"], x=1.8, y=0.0)
s.draw()
