"""Hunsdiecker reaction (radical chain). The silver carboxylate and bromine give an acyl hypobromite,
whose weak O-Br bond breaks homolytically (fishhook arrows). The acyloxyl radical loses CO2 at once,
and the alkyl radical abstracts the bromine atom from another acyl hypobromite, giving the alkyl
bromide and a new acyloxyl radical that carries the chain."""

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
hb = s.molecule("CCC(=O)OBr", coords=[(-1.74, 0.0), (-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5), (1.74, 0.0)])
s.curly(hb.bond(4, 5), hb.atom(4), bend=0.7, single=True)
s.curly(hb.bond(4, 5), hb.atom(5), bend=-0.7, single=True)
row(s, [("arrow", r"heat or $h\nu$"), "CCC(=O)[O]", "+", "[Br]"], x=2.4, y=0.0)
y = -2.8
_, x = row(s, ["CCC(=O)[O]", ("arrow", r"$-$CO$_2$")], x=-2.4, y=y)
et = s.molecule("C[CH2]", coords=[(0.0, 0.0), (0.87, -0.5)], at=(x - 0.1, y + 0.2))
hb2 = s.molecule("BrOC(=O)CC", coords=[(0.0, 0.0), (0.9, 0.3), (1.77, -0.2), (1.77, -1.2), (2.64, 0.3), (3.5, -0.2)], at=(x + 2.7, y + 0.1))
mid = (et.xy(1) + hb2.xy(0)) / 2
s.curly(et.atom(1), mid, bend=-0.6, single=True)
s.curly(hb2.bond(0, 1), mid, bend=0.6, single=True)
s.curly(hb2.bond(0, 1), hb2.atom(1), bend=-0.6, single=True)
row(s, [("arrow", None), "CCBr", "+", "CCC(=O)[O]"], x=x + 6.4, y=y)
s.draw()
