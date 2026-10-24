"""Conjugate addition of HCl to 1,4-benzoquinone. Protonation of one carbonyl oxygen activates the
ring; chloride attacks the beta carbon (C3), the C2=C3 pi pair moves to C1-C2 and the C=O pi pair
moves onto the protonated oxygen, giving an enol. Tautomerization of the remaining ketone (the C3-H
proton moves to the C4 oxygen) restores aromaticity: the product is 2-chlorobenzene-1,4-diol."""

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
Q = "[OH+]=C1C=CC(=O)C=C1"
cl = s.molecule("[Cl-]", at=(1.6, 1.9), lone_pairs=True)
q = s.molecule(Q, at=(0.0, 0.0), rotate=turn(Q, 1, 0, 180))
s.curly(cl.atom(0), q.atom(3), bend=0.3)
s.curly(q.bond(2, 3), q.bond(1, 2), bend=-0.7)
s.curly(q.bond(0, 1), q.atom(0), bend=-1.3)
EN = "OC1=CC(Cl)C(=O)C=C1"
row(s, [("arrow", None), (EN, {"rotate": turn(EN, 1, 0, 180)}), ("arrow", "tautomerism"), "Oc1ccc(O)c(Cl)c1"], x=2.2, y=0.0)
s.draw()
