"""Pinnick oxidation of an aldehyde with sodium chlorite in a weakly acidic buffer. Chlorous acid
adds to the carbonyl group; the adduct fragments in a pericyclic step through a five-membered ring:
the oxygen of the chlorite ester takes the aldehydic hydrogen, the C-H bond pair forms the new C=O
bond, and the O-Cl bond pair leaves with chlorine as hypochlorous acid. 2-Methylbut-2-ene removes
the HOCl, which would otherwise consume chlorite and attack C=C bonds."""

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
row(s, [("O=C*", {"labels": {2: "R"}}), ("arrow", r"HClO$_2$")], x=-5.6, y=0.0)
ad = s.molecule("OC([H])(*)OCl=O", coords=[(-1.0, 0.3), (0.0, 0.0), (0.3, 1.0), (-0.5, -0.9), (1.0, -0.6), (2.0, -0.3), (2.2, 0.75)],
                labels={3: "R"}, lone_pairs=[6])
s.curly(ad.atom(6), ad.atom(2), bend=0.4)
s.curly(ad.bond(1, 2), ad.bond(1, 4), bend=0.6)
s.curly(ad.bond(4, 5), ad.atom(5), bend=-0.7)
row(s, [("arrow", None), ("OC(=O)*", {"labels": {3: "R"}}), "+", "OCl"], x=3.0, y=0.0)
s.text((7.6, -1.7), r"HOCl + Me$_2$C=CHMe $\to$ chlorohydrin (scavenger)", size=11)
s.draw()
