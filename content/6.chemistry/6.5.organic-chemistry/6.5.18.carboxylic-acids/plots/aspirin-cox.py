"""Acetylation of cyclooxygenase by aspirin. The hydroxy group of a serine residue in the active site
(Enz-CH2OH; a nearby base takes its proton) adds to the acetyl carbonyl group of aspirin. The
tetrahedral intermediate collapses and expels the phenoxide of salicylate, a good leaving group
(pKa of a phenol about 10), leaving the serine acetylated, which blocks the channel to the active
site."""

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
ser = s.molecule("*CO", coords=[(-2.6, 1.6), (-1.7, 1.15), (-0.9, 1.7)], labels={0: "Enz"}, lone_pairs=[2])
asp = s.molecule("CC(=O)Oc1ccccc1C(=O)O", at=(1.6, 0.0), lone_pairs=[2])
s.curly(ser.atom(2), asp.atom(1), bend=-0.4)
s.curly(asp.bond(1, 2), asp.atom(2), bend=0.8)
(ti,), _ = row(s, [("arrow", r"$-$H$^+$"), ("*COC(C)([O-])Oc1ccccc1C(=O)O", {"labels": {0: "Enz"}, "lone_pairs": [5]})], x=4.0, y=0.0)
s.curly(ti.atom(5), ti.bond(3, 5), bend=0.8)
s.curly(ti.bond(3, 6), ti.atom(6), bend=0.7)
row(s, [("arrow", None), ("*COC(C)=O", {"labels": {0: "Enz"}}), "+", "[O-]c1ccccc1C(=O)O"], x=-1.0, y=-3.4)
s.draw()
