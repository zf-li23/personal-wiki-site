"""Reduction of a hindered ketone by a Grignard reagent that carries a beta hydrogen (di-tert-butyl
ketone and isopropylmagnesium bromide). Instead of adding its carbon, the reagent delivers the beta
hydrogen as a hydride through a six-membered cyclic transition state, like the
Meerwein-Ponndorf-Verley reduction: the C-H pair moves to the carbonyl carbon, the C-Mg pair forms
the C=C bond of propene, and the C=O pi pair moves onto oxygen, which stays bound to magnesium."""

import math

from wikichem import Scheme


def hexagon(deg):
    t = math.radians(deg)
    return (math.cos(t), math.sin(t))


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

s = Scheme()
ket = s.molecule("*C(*)=O", coords=[(-1.8, -0.1), hexagon(210), (-1.1, -1.45), hexagon(150)],
                 labels={0: "$t$Bu", 2: "$t$Bu"}, lone_pairs=[3])
mg = s.molecule("[H]CC(C)[Mg]Br", coords=[hexagon(270), hexagon(330), hexagon(30), (1.85, 0.75), hexagon(90), (0.0, 2.0)])
s.partial(ket.atom(3), mg.atom(4))
s.curly(mg.bond(0, 1), ket.atom(1), bend=-0.5)
s.curly(mg.bond(2, 4), mg.bond(1, 2), bend=-0.7)
s.curly(ket.bond(1, 3), ket.atom(3), bend=-0.6)
row(s, [("arrow", None), "CC(C)(C)C(O[Mg]Br)C(C)(C)C", "+", "C=CC"], x=2.4)
s.draw()
