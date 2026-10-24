"""Aminolysis of acetyl chloride by methylamine. The amine nitrogen adds to the carbonyl carbon and the
C=O pi pair moves onto oxygen; the tetrahedral intermediate collapses, the oxide pushing back and
chloride leaving. A second equivalent of amine (or NaOH under Schotten-Baumann conditions) removes
the proton from nitrogen, giving N-methylacetamide and the ammonium chloride."""

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
am = s.molecule("CN", coords=[(-2.2, 1.4), (-1.3, 0.95)], lone_pairs=[1])
ac = s.molecule("CC(=O)Cl", coords=[(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5)], lone_pairs=[2])
s.curly(am.atom(1), ac.atom(1), bend=0.4)
s.curly(ac.bond(1, 2), ac.atom(2), bend=-0.8)
(ti,), x = row(s, [("arrow", None), ("C[NH2+]C(C)([O-])Cl", {"coords": [(-1.74, 0.0), (-0.87, -0.5), (0.0, 0.0), (-0.3, -1.0), (0.0, 1.0), (0.95, -0.3)],
                                                             "lone_pairs": [4]})], x=1.4, y=0.0)
s.curly(ti.atom(4), ti.bond(2, 4), bend=-0.8)
s.curly(ti.bond(2, 5), ti.atom(5), bend=0.7)
row(s, [("arrow", r"$-$Cl$^-$"), "C[NH2+]C(C)=O", ("arrow", r"MeNH$_2$", r"$-$MeNH$_3^+$"), "CNC(C)=O"], x=x, y=0.0)
s.draw()
