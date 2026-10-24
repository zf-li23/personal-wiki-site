"""Ring opening of glutaric anhydride by N-methylpropylamine. The amine adds to one carbonyl carbon;
the tetrahedral intermediate collapses and expels the ring oxygen as a carboxylate, which stays in the
same molecule. Proton transfer from nitrogen gives the amide acid; the carboxylate cannot be attacked
again, so only one end of the diacid is converted."""

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
h = ring((0.0, 0.0), 30)  # C1 (30 deg), C2, C3, C4, C5, O
anh = s.molecule("O=C1CCCC(=O)O1", coords=[(1.73, 1.0), h[0], h[5], h[4], h[3], h[2], (-1.73, 1.0), h[1]], lone_pairs=[0])
amine = s.molecule("CCCNC", coords=[(4.6, 0.0), (3.7, -0.5), (2.8, 0.0), (2.6, -1.1), (3.2, -1.9)], lone_pairs=[3])
s.curly(amine.atom(3), anh.atom(1), bend=-0.4)
s.curly(anh.bond(0, 1), anh.atom(0), bend=0.8)
row(s, [("arrow", r"addition", r"then collapse"), "CCC[NH+](C)C(=O)CCCC(=O)[O-]", ("arrow", "proton", "transfer"), "CCCN(C)C(=O)CCCC(=O)O"],
    x=5.0, y=0.0)
s.draw()
