"""Decarboxylation in pyruvate decarboxylase. The carbanion (ylide) at C2 of the thiazolium ring of
thiamine diphosphate has added to the ketone carbonyl of pyruvate; in the adduct the carboxylate
leaves as CO2: the oxide lone pair forms the second C=O bond, the C-C bond pair forms a C=C bond to
C2, and the C=N+ pi pair moves onto nitrogen. The positively charged ring is the electron sink, like
the beta carbonyl group of a beta-keto acid. The enamine (Breslow-type) intermediate is protonated
and releases acetaldehyde. R and R' stand for the pyrimidinylmethyl group and the
diphosphoethyl side chain."""

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
pen = ring((0.0, 0.0), 90, n=5)  # C2 at the top, then counterclockwise: S, C5, C4, N
ad = s.molecule("CC(O)(C(=O)[O-])C1=[N+](*)C(C)=C(*)S1",
                coords=[(-1.0, 2.2), (0.0, 1.85), (-0.35, 2.8), (0.95, 2.3), (1.1, 3.3), (1.75, 1.7), pen[0], pen[4], (1.6, -0.45), pen[3],
                        (0.6, -1.85), pen[2], (-1.6, -0.45), pen[1]],
                labels={8: "R", 12: "R$'$"}, lone_pairs=[5])
s.curly(ad.atom(5), ad.bond(3, 5), bend=0.7)
s.curly(ad.bond(1, 3), ad.bond(1, 6), bend=0.8)
s.curly(ad.bond(6, 7), ad.atom(7), bend=0.6)
row(s, [("arrow", r"$-$CO$_2$")], x=2.5, y=0.5)
en = s.molecule("CC(O)=C1N(*)C(C)=C(*)S1",
                coords=[(-1.0, 2.2), (0.0, 1.85), (0.3, 2.85), pen[0], pen[4], (1.6, -0.45), pen[3], (0.6, -1.85), pen[2], (-1.6, -0.45),
                        pen[1]],
                labels={5: "R", 9: "R$'$"}, at=(6.2, 0.0))
row(s, [("arrow", r"H$^+$", r"$-$TPP ylide"), "CC=O"], x=8.3, y=0.5)
s.draw()
