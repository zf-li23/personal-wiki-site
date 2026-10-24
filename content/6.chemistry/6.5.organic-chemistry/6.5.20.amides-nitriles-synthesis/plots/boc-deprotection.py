"""Removal of the Boc protecting group with trifluoroacetic acid. The carbamate is protonated on the
carbonyl oxygen; the bond between oxygen and the tert-butyl group breaks heterolytically (as in the
AAl1 cleavage of tert-butyl esters), its electrons forming a C=O bond, and the tert-butyl cation leaves.
The carbamic acid loses CO2 and releases the amine (as its ammonium salt); the tert-butyl cation loses a
proton to give isobutene."""

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
bo = s.molecule("CC(C)(C)OC(=[OH+])N*",
                coords=[(-1.7, 0.6), (-0.87, 0.0), (-1.4, -0.85), (-0.5, 0.95), (0.0, -0.5), (0.87, 0.0), (0.87, 1.0), (1.74, -0.5), (2.61, 0.0)],
                labels={8: "R"})
s.curly(bo.bond(1, 4), bo.bond(4, 5), bend=0.7)
s.curly(bo.bond(5, 6), bo.atom(6), bend=-0.8)
row(s, [("arrow", None), "C[C+](C)C", "+", ("OC(=O)N*", {"labels": {4: "R"}}), ("arrow", r"$-$CO$_2$"), ("[NH3+]*", {"labels": {1: "R"}})],
    x=3.2, y=0.0)
row(s, [("C[C+](C)C", {}), ("arrow", r"$-$H$^+$"), "C=C(C)C"], x=3.2, y=-2.6)
s.draw()
