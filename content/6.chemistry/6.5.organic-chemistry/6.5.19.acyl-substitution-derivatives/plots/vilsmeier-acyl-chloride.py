"""Acyl chloride formation with oxalyl chloride and catalytic DMF. Top: DMF and oxalyl chloride give
the chloroiminium (Vilsmeier) reagent with loss of CO, CO2 (and chloride). Middle: the carboxylic
acid displaces chloride from the reagent, giving an acyloxyiminium ion (an activated ester), and
chloride adds to its carbonyl carbon. Bottom: the tetrahedral intermediate collapses; the C-O bond
pair forms the C=O bond of DMF while the C=N+ pi pair moves onto nitrogen, so DMF is released and
returns to the cycle, and the acyl chloride is formed."""

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
row(s, ["CN(C)C=O", "+", "O=C(Cl)C(=O)Cl", ("arrow", r"$-$CO, $-$CO$_2$"), "C[N+](C)=CCl", "+", "[Cl-]"], x=0.0, y=0.0)
y = -3.2
_, x = row(s, ["CC(=O)O", ("arrow", r"Me$_2$N$^+$=CHCl", r"$-$HCl")], x=0.0, y=y)
ai = s.molecule("CC(=O)OC=[N+](C)C", coords=[(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5), (1.74, 0.0), (2.61, -0.5), (3.48, 0.0), (2.61, -1.5)],
                at=(x + 1.4, y + 0.1), lone_pairs=[2])
cl = s.molecule("[Cl-]", at=(x + 0.4, y + 1.7), lone_pairs=True)
s.curly(cl.atom(0), ai.atom(1), bend=0.3)
s.curly(ai.bond(1, 2), ai.atom(2), bend=-0.8)
row(s, [("arrow", None)], x=x + 5.4, y=y)
y = -6.6
ti = s.molecule("CC([O-])(Cl)OC=[N+](C)C",
                coords=[(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (-0.3, -0.95), (0.87, 0.5), (1.74, 0.0), (2.61, 0.5), (3.48, 0.0), (2.61, 1.5)],
                at=(1.4, y), lone_pairs=[2])
s.curly(ti.atom(2), ti.bond(1, 2), bend=-0.8)
s.curly(ti.bond(1, 4), ti.bond(4, 5), bend=-0.6)
s.curly(ti.bond(5, 6), ti.atom(6), bend=0.7)
row(s, [("arrow", None), "CC(=O)Cl", "+", "CN(C)C=O"], x=5.6, y=y)
s.draw()
