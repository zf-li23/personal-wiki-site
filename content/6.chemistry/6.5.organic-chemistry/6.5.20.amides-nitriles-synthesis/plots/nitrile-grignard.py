"""Ketone synthesis from a nitrile and a Grignard reagent (benzonitrile and ethylmagnesium bromide).
The C-Mg bond pair adds to the nitrile carbon and the C-N pi pair moves onto nitrogen, which is bound to
magnesium. The negatively charged imine salt is not attacked by a second equivalent; aqueous acid
hydrolyses it, through the imine, to propiophenone."""

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
ni = s.molecule("*C#N", coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)], labels={0: "Ph"}, lone_pairs=[2])
eg = s.molecule("CC[Mg]Br", coords=[(-0.5, -2.3), (0.1, -1.5), (1.4, -1.2), (2.4, -1.6)])
s.partial(ni.atom(2), eg.atom(2))
s.curly(eg.bond(1, 2), ni.atom(1), bend=-0.4)
s.curly(ni.bond(1, 2), ni.atom(2), bend=0.8)
row(s, [("arrow", None), "CCC(=N[Mg]Br)c1ccccc1", ("arrow", r"H$_3$O$^+$"), "CCC(=N)c1ccccc1", ("arrow", r"H$_3$O$^+$", r"$-$NH$_4^+$"),
        "CCC(=O)c1ccccc1"], x=2.8, y=-0.4)
s.draw()
