"""Removal of the Fmoc protecting group with piperidine (E1cb). Piperidine removes the acidic C9 proton
of the fluorene (its conjugate base is an aromatic cyclopentadienyl-type anion); the carbanion pushes
out the carbamate, forming dibenzofulvene. The carbamate loses CO2 to release the free amine, and excess
piperidine adds to dibenzofulvene, which would otherwise react with the amine."""

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
FM = "O=C(N*)OCC1c2ccccc2-c2ccccc21"
fm = s.molecule(FM, at=(0.0, 0.0), rotate=turn(FM, 6, 5, 90), labels={3: "R"}, show_h=[6], lone_pairs=[])
h = fm.h(6)
pip = s.molecule("C1CCNCC1", at=(h.xy[0] + 2.2, h.xy[1] - 0.6), lone_pairs=[3])
s.curly(pip.atom(3), h, bend=-0.4)
s.curly((fm.xy(6) + h.xy) / 2, fm.bond(5, 6), bend=0.7)
s.curly(fm.bond(4, 5), fm.atom(4), bend=-0.7)
row(s, [("arrow", None), "C=C1c2ccccc2-c2ccccc21", "+", ("[O-]C(=O)N*", {"labels": {4: "R"}}), ("arrow", r"$-$CO$_2$"),
        ("N*", {"labels": {1: "R"}})], x=pip.coords[:, 0].max() + 0.6, y=0.0)
s.draw()
