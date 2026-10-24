"""Dehydration of a primary amide to a nitrile with thionyl chloride. The amide oxygen (the more
nucleophilic site of an amide) attacks sulfur and chloride leaves; loss of a proton from nitrogen gives
an imino chlorosulfite, in which the oxygen has become part of a good leaving group. A base removes the
remaining N-H proton: the N-H bond pair forms the third C-N bond while the C-O bond pair leaves, and
the chlorosulfite falls apart into SO2 and chloride."""

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
am = s.molecule("CC(N)=O", coords=[(-0.87, -0.5), (0.0, 0.0), (0.87, -0.5), (0.0, 1.0)], lone_pairs=[3])
so = s.molecule("ClS(=O)Cl", coords=[(0.6, 3.0), (1.3, 2.3), (2.2, 2.75), (1.6, 1.3)], lone_pairs=[3])
s.curly(am.atom(3), so.atom(1), bend=-0.4)
s.curly(so.bond(1, 3), so.atom(3), bend=-0.8)
row(s, [("arrow", r"$-$Cl$^-$", r"$-$H$^+$")], x=2.6, y=0.3)
y = 0.0
ic = s.molecule("CC(=N[H])OS(=O)Cl", coords=[(-0.87, -0.5), (0.0, 0.0), (0.87, -0.5), (1.74, 0.0), (0.0, 1.0), (0.87, 1.5), (0.87, 2.5), (1.74, 1.0)],
                at=(5.6, y))
b = ic.xy(3) + (0.9, -0.9)
s.text(b, "B:")
s.curly(b + (-0.1, 0.25), ic.atom(3), bend=0.5)
s.curly(ic.bond(2, 3), ic.bond(1, 2), bend=-0.8)
s.curly(ic.bond(1, 4), ic.atom(4), bend=0.7)
row(s, [("arrow", r"$-$HB$^+$")], x=8.4, y=0.3)
row(s, ["CC#N", "+", "O=S=O", "+", "[Cl-]"], x=-1.0, y=-3.0)
s.draw()
