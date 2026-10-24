"""Hydrolysis of acetamide in concentrated base. Hydroxide adds to the carbonyl carbon, but the
tetrahedral intermediate prefers to lose hydroxide again, because the amide ion is a very poor leaving
group. Only after a second deprotonation does the doubly charged intermediate push hard enough: an
oxide forms the C=O bond and the C-N bond pair leaves with nitrogen. The amide ion is protonated by
water at once, and the carboxylate does not react with ammonia, so the reaction is irreversible."""

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
oh = s.molecule("[OH-]", at=(-1.3, 1.5), lone_pairs=True)
am = s.molecule("CC(N)=O", coords=[(-0.87, -0.5), (0.0, 0.0), (0.87, -0.5), (0.0, 1.0)], lone_pairs=[3])
s.curly(oh.atom(0), am.atom(1), bend=0.4)
s.curly(am.bond(1, 3), am.atom(3), bend=0.8)
_, x = row(s, [("arrow", None, "reversible"), "CC(N)(O)[O-]", ("arrow", r"HO$^-$", r"$-$H$_2$O")], x=2.0, y=0.0)
di = s.molecule("CC(N)([O-])[O-]", coords=[(-0.87, -0.5), (0.0, 0.0), (0.87, -0.5), (0.0, 1.0), (-0.3, -1.0)], at=(x + 1.2, 0.0), lone_pairs=[3])
s.curly(di.atom(3), di.bond(1, 3), bend=-0.8)
s.curly(di.bond(1, 2), di.atom(2), bend=0.7)
row(s, [("arrow", None), "CC(=O)[O-]", "+", "[NH2-]", ("arrow", r"H$_2$O"), "N", "+", "[OH-]"], x=x + 2.6, y=0.0)
s.draw()
