"""Lactonization of a gamma-halo acid in base. The carboxylate oxygen attacks the carbon that carries
bromine from the back side (an intramolecular SN2 reaction) and bromide leaves, closing the
five-membered ring of gamma-butyrolactone. Ring closure is fast because the reacting ends are held
close together and the five-membered ring is free of strain."""

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
p = ring((0.0, 0.0), 162, n=5)  # O-, C1, C-alpha, C-beta, C-gamma around a pentagon
br = (p[4][0] + 0.95, p[4][1] + 0.55)
sub = s.molecule("[O-]C(=O)CCCBr", coords=[p[0], p[1], (p[1][0] - 0.7, p[1][1] - 0.75), p[2], p[3], p[4], br], lone_pairs=[0])
s.curly(sub.atom(0), sub.atom(5), bend=-0.3)
s.curly(sub.bond(5, 6), sub.atom(6), bend=-0.7)
row(s, [("arrow", None), "O=C1CCCO1", "+", "[Br-]"], x=2.2, y=0.0)
s.draw()
