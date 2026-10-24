"""Dakin oxidation of 4-hydroxybenzaldehyde with alkaline hydrogen peroxide. The hydroperoxide
anion adds to the carbonyl carbon; in the tetrahedral adduct the oxide pushes, the electron-rich
aryl group migrates from carbon to the proximal oxygen with its bonding pair, and hydroxide leaves
from the distal oxygen as the O-O bond breaks (a Baeyer-Villiger type step). The aryl formate is
hydrolysed in the base to the phenol (hydroquinone) and formate."""

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
ar = ring((2.0, 0.0), 180)  # ipso, then counterclockwise
ARYL = [ar[0], ar[5], ar[4], ar[3], (4.0, 0.0), ar[2], ar[1]]
hoo = s.molecule("[O-]O", coords=[(-1.5, 0.3), (-2.4, 0.8)], lone_pairs=[0])
ald = s.molecule("O=Cc1ccc(O)cc1", coords=[(0.0, 1.0), (0.0, 0.0)] + ARYL, lone_pairs=[0])
s.curly(hoo.atom(0), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), ald.atom(0), bend=0.8)
s.arrow((4.7, 0), (6.1, 0))
x = 8.2
ad = s.molecule("[O-]C([H])(OO)c1ccc(O)cc1", coords=[(0.0, 1.0), (0.0, 0.0), (-0.9, 0.45), (-0.5, -0.87), (-1.5, -0.87)] + ARYL,
                at=(x, 0.0), lone_pairs=[0])
s.curly(ad.atom(0), ad.bond(0, 1), bend=-0.7)
s.curly(ad.bond(1, 5), ad.atom(3), bend=0.6)
s.curly(ad.bond(3, 4), ad.atom(4), bend=0.7)
row(s, [("arrow", r"$-$HO$^-$")], x=x + 4.6, y=0.0)
row(s, [("arrow", None), "O=COc1ccc(O)cc1", ("arrow", r"HO$^-$, H$_2$O"), "Oc1ccc(O)cc1", "+", "O=C[O-]"], x=-1.0, y=-3.2)
s.draw()
