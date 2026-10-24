"""Hock rearrangement of cumene hydroperoxide in the cumene process. After protonation of the
terminal OH, the phenyl group migrates with its bonding pair from carbon to the electron-poor
proximal oxygen while water leaves (the same 1,2-shift as in the Baeyer-Villiger oxidation); the
resulting oxocarbenium ion adds water, and the hemiketal falls apart into phenol and acetone."""

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
ar = ring((2.0, 0.0), 180)
hp = s.molecule("CC(C)(O[OH2+])c1ccccc1", coords=[(-0.5, -0.87), (0.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.9, 1.5)] + ar[0:1] + ar[5:0:-1])
s.curly(hp.bond(1, 5), hp.atom(3), bend=0.8)
s.curly(hp.bond(3, 4), hp.atom(4), bend=-0.8)
row(s, [("arrow", r"$-$H$_2$O"), "CC(C)=[O+]c1ccccc1", ("arrow", r"H$_2$O", r"$-$H$^+$")], x=3.4, y=0.0)
row(s, [("arrow", None), "CC(C)(O)Oc1ccccc1", ("arrow", None), "Oc1ccccc1", "+", "CC(C)=O"], x=-1.0, y=-3.0)
s.draw()
