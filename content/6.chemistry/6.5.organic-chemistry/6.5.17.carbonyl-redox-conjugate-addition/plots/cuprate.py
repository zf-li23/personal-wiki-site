"""Conjugate addition of lithium dimethylcuprate to 3-methylcyclohex-2-en-1-one. The d10 Cu(I)
first forms a pi complex with the C=C bond while Li+ activates the carbonyl oxygen; oxidative
addition then gives a beta-cuprio(III) lithium enolate, in which copper is sigma-bonded to the beta
carbon. Reductive elimination joins one methyl group to the beta carbon (the Cu-C bond pair forms
the new C-C bond, and the Cu-C(beta) pair returns to copper) and releases MeCu; workup protonates the
lithium enolate to 3,3-dimethylcyclohexanone."""

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
_, x = row(s, ["CC1=CC(=O)CCC1", ("arrow", r"Me$_2$CuLi", "ox. addition")], x=-6.0, y=0.0)
h = ring((0.0, 0.0), 150)  # C-beta at 150 degrees, then counterclockwise: C2, C3, C4, C5 (enolate C), C-alpha
cu = s.molecule("CC1(CCCC(O[Li])=C1)[Cu](C)C",
                coords=[(-1.8, -0.2), h[0], h[1], h[2], h[3], h[4], (1.73, 1.0), (2.6, 0.5), h[5], (-1.2, 1.9), (-2.5, 2.3), (-0.6, 3.1)],
                at=(x + 2.6, 0.0), labels={9: "Cu"})
s.curly(cu.bond(9, 10), (cu.xy(10) + cu.xy(1)) / 2, bend=0.6)
s.curly(cu.bond(1, 9), cu.atom(9), bend=-0.6)
row(s, [("arrow", "reductive", "elimination"), "CC1(C)CCCC(O[Li])=C1", "+", "C[Cu]", ("arrow", r"H$_3$O$^+$"), "CC1(C)CCCC(=O)C1"],
    x=x + 6.0, y=0.0)
s.draw()
