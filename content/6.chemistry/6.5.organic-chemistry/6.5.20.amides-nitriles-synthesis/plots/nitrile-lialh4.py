"""Reduction of a nitrile (butanenitrile) to a primary amine by LiAlH4. A hydride adds to the nitrile
carbon and the C-N pi pair moves onto nitrogen, which binds aluminium; the imine salt takes a second
hydride, and aqueous workup protonates the nitrogen dianion to butan-1-amine. With DIBAL-H at low
temperature only one hydride adds, and hydrolysis of the imine gives the aldehyde instead."""

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
al = s.molecule("[H][Al-]([H])([H])[H]", coords=[(0.0, 1.0), (0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (1.0, 0.0)], at=(-1.8, 1.4))
ni = s.molecule("CCCC#N", coords=[(-1.74, -1.0), (-0.87, -0.5), (0.0, -1.0), (0.87, -0.5), (1.74, 0.0)], lone_pairs=[4])
s.curly(al.bond(1, 4), ni.atom(3), bend=-0.5)
s.curly(ni.bond(3, 4), ni.atom(4), bend=-0.8)
row(s, [("arrow", None), "CCCC=N[AlH3-]", ("arrow", r"H$^-$", r"then H$_2$O"), "CCCCN"], x=2.4, y=-0.5, gap=1.0)
s.draw()
