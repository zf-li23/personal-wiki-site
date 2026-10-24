"""Weinreb ketone synthesis. Methylmagnesium bromide adds to the carbonyl carbon of the
N-methoxy-N-methylbenzamide; in the tetrahedral intermediate magnesium is chelated by the alkoxide
and the methoxy oxygen (dashed), forming a five-membered ring that does not collapse under the
reaction conditions. No ketone is present while Grignard reagent remains, so it cannot add a second
time; aqueous acid breaks up the chelate and gives acetophenone."""

import numpy as np

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
wa = s.molecule("O=C(*)N(C)OC", coords=[(0.0, 1.0), (0.0, 0.0), (-0.87, -0.5), (0.87, -0.5), (0.87, -1.5), (1.74, 0.0), (2.61, -0.5)],
                labels={2: "Ph"}, lone_pairs=[0])
mg = s.molecule("C[Mg]Br", coords=[(-1.8, 1.0), (-1.8, 2.0), (-1.0, 2.6)])
s.curly(mg.bond(0, 1), wa.atom(1), bend=0.4)
s.curly(wa.bond(0, 1), wa.atom(0), bend=-0.8)
_, x = row(s, [("arrow", None)], x=3.0, y=0.0)
c = np.array([x + 2.4, 0.3])
p = ring(c, 234, n=5)  # C, O, Mg, O(Me), N
out = lambda q, d=1.0: tuple(np.array(q) + d * (np.array(q) - c) / np.linalg.norm(np.array(q) - c))
che = s.molecule("CC(*)(O[Mg]Br)N(C)OC",
                 coords=[out(p[0]) , p[0], (p[0][0] + 0.75, p[0][1] - 0.65), p[1], p[2], out(p[2]), p[4], out(p[4]), p[3], out(p[3])],
                 labels={2: "Ph"})
s.partial(che.atom(4), che.atom(8))
row(s, [("arrow", r"H$_3$O$^+$"), "CC(=O)c1ccccc1"], x=x + 4.6, y=0.0)
s.draw()
