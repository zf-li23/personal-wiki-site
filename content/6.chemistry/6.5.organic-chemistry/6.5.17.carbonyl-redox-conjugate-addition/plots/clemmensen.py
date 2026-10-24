"""One commonly proposed course of the Clemmensen reduction (the mechanism is not settled; the
alcohol is not an intermediate). The protonated ketone takes two electrons from the zinc surface,
giving an alpha-hydroxyalkylzinc species; protonation of the OH and loss of water, pushed by the
C-Zn bond pair, give a zinc carbenoid, which is protonated twice (with further electron transfer
from zinc) to the CH2 group."""

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
ZN = ("CC([OH2+])([Zn]Cl)*", {"coords": [(1.0, 0.0), (0.0, 0.0), (0.0, -1.0), (0.0, 1.0), (0.9, 1.45), (-1.0, 0.0)], "labels": {5: "Ph"}})
(_, zn), x = row(s, [("CC(=O)*", {"labels": {3: "Ph"}}), ("arrow", r"Zn(Hg), HCl", r"2e$^-$, H$^+$"), ZN], x=0.0, y=0.0)
s.curly(zn.bond(1, 3), zn.bond(1, 2), bend=0.8)
s.curly(zn.bond(1, 2), zn.atom(2), bend=0.8)
CARB = ("C[C](=[Zn+]Cl)*", {"coords": [(1.0, 0.0), (0.0, 0.0), (0.0, 1.0), (0.9, 1.45), (-1.0, 0.0)], "labels": {4: "Ph"}})
(carb, _), x2 = row(s, [("arrow", r"$-$H$_2$O"), CARB, ("arrow", r"2H$^+$, 2e$^-$"), ("CC*", {"labels": {2: "Ph"}})], x=x, y=0.0)
s.text((carb.xy(1)[0], -1.3), "zinc carbenoid", size=11)
s.text((carb.xy(1)[0], -1.8), "(proposed)", size=11)
s.draw()
