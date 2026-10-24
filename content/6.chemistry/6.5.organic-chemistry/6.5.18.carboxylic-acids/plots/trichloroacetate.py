"""Decarboxylation of trichloroacetate. The oxide lone pair forms the second C=O bond of carbon
dioxide while the C-C bond pair stays on the CCl3 carbon; the trichloromethyl anion, stabilized by
the inductive effect of three chlorines, takes a proton from water to give chloroform."""

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
t = s.molecule("[O-]C(=O)C(Cl)(Cl)Cl", coords=[(-0.87, -0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5), (1.74, 0.0), (0.87, -1.5), (1.6, -1.2)],
               lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=-0.8)
s.curly(t.bond(1, 3), t.atom(3), bend=0.7)
row(s, [("arrow", r"heat"), "O=C=O", "+", "[C-](Cl)(Cl)Cl", ("arrow", r"H$_2$O", r"$-$HO$^-$"), "ClC(Cl)Cl"], x=2.4, y=-0.2)
s.draw()
