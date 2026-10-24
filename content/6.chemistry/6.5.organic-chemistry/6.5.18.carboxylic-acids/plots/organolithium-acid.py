"""Ketone synthesis from a carboxylic acid and two equivalents of methyllithium. The first
equivalent removes the acidic proton; the second adds its C-Li bond pair to the carbonyl carbon of
the lithium carboxylate while the C=O pi pair moves onto oxygen. The tetrahedral dilithium
dialkoxide cannot expel O2-, so no ketone forms in the flask; on aqueous workup it becomes the
hydrate, which loses water to give the methyl ketone."""

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
cy = ring((-0.87, -1.5), 90)
carb = s.molecule("[Li]OC(=O)C1CCCCC1", coords=[(1.74, 0.0), (0.87, -0.5), (0.0, 0.0), (0.0, 1.0)] + cy,
                  lone_pairs=[3])
ml = s.molecule("C[Li]", coords=[(1.2, 2.0), (2.1, 1.6)])
s.curly(ml.bond(0, 1), carb.atom(2), bend=0.4)
s.curly(carb.bond(2, 3), carb.atom(3), bend=-0.8)
row(s, [("arrow", None), "[Li]OC(C)(O[Li])C1CCCCC1", ("arrow", r"H$_3$O$^+$"), "OC(C)(O)C1CCCCC1", ("arrow", r"$-$H$_2$O"), "CC(=O)C1CCCCC1"],
    x=2.6, y=-0.6)
s.draw()
