"""First step of the reduction of a carboxylic acid by LiAlH4: an acid-base reaction. An Al-H bond
pair takes the acidic proton and the O-H bond pair stays on oxygen, releasing H2 and leaving the
lithium carboxylate bound to aluminium. The carboxylate, activated by the Lewis acidic aluminium,
then accepts hydride; the tetrahedral intermediate loses an aluminium oxide to give the aldehyde,
which is reduced at once, so workup gives the primary alcohol."""

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
acid = s.molecule("CC(=O)O[H]", coords=[(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5), (1.74, 0.0)], lone_pairs=[3])
al = s.molecule("[H][Al-]([H])([H])[H]", coords=[(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (2.0, 0.0), (1.0, -1.0)], at=(3.7, 0.4))
s.text((al.xy(1)[0] + 0.1, al.xy(1)[1] - 1.75), r"Li$^+$")
s.curly(al.bond(0, 1), acid.atom(4), bend=0.6)
s.curly(acid.bond(3, 4), acid.atom(3), bend=0.8)
row(s, [("arrow", r"$-$H$_2$"), "CC(=O)O[AlH3-]", ("arrow", r"H$^-$, then", r"$-$O$-$Al"), "CC=O", ("arrow", r"H$^-$; H$_3$O$^+$"), "CCO"],
    x=6.6, y=0.0)
s.draw()
