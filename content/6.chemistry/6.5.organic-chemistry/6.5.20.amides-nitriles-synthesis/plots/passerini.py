"""Passerini reaction, drawn in the ionic stepwise form (in nonpolar solvents the steps are thought to
be concerted, held together by hydrogen bonds). Top: the isocyanide carbon, with its lone pair, adds to
the carbonyl carbon of the aldehyde activated by the carboxylic acid, giving a nitrilium ion; the
carboxylate adds to the nitrilium carbon (alpha-addition: electrophile and nucleophile end up on the
same isocyanide carbon). Bottom: in the imidate the acyl group moves to the neighbouring hydroxy
oxygen through a five-membered ring, and tautomerization gives the alpha-acyloxy amide."""

import numpy as np

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
ald = s.molecule("*C=[OH+]", coords=[(-0.87, 0.5), (0.0, 0.0), (0.87, 0.5)], labels={0: "R$^1$"})
iso = s.molecule("*[N+]#[C-]", coords=[(1.2, -3.0), (0.6, -2.2), (0.0, -1.4)], labels={0: "R$^3$"}, lone_pairs=[2])
s.curly(iso.atom(2), ald.atom(1), bend=-0.5)
s.curly(ald.bond(1, 2), ald.atom(2), bend=-0.8)
_, x = row(s, [("arrow", None)], x=1.6, y=-0.8)
nit = s.molecule("*C(O)C#[N+]*", coords=[(-0.87, 0.5), (0.0, 0.0), (0.0, 1.0), (0.87, -0.5), (1.74, -1.0), (2.61, -1.5)],
                 labels={0: "R$^1$", 5: "R$^3$"}, at=(x + 1.2, 0.0))
car = s.molecule("*C(=O)[O-]", coords=[(-1.6, -2.6), (-0.7, -2.1), (-0.7, -1.1), (0.15, -2.6)], labels={0: "R$^2$"}, lone_pairs=[3],
                 at=(x + 1.2, 0.0))
s.curly(car.atom(3), nit.atom(3), bend=0.5)
s.curly(nit.bond(3, 4), nit.atom(4), bend=-0.7)
row(s, [("arrow", None)], x=x + 4.4, y=-0.8)
y = -6.0
c = np.array([1.5, y])
p = ring(c, 162, n=5)  # O(H), C-acyl, O(imidate), C(imidate) ... assigned below
out = lambda q, d=1.0: tuple(np.array(q) + d * (np.array(q) - c) / np.linalg.norm(np.array(q) - c))
im = s.molecule("*C(O)C(=N*)OC(*)=O",
                coords=[out(p[4]), p[4], p[0], p[3], out(p[3]), out(p[3], 2.0), p[2], p[1], out(p[1]), (p[1][0] + 0.4, p[1][1] - 0.95)],
                labels={0: "R$^1$", 5: "R$^3$", 8: "R$^2$"}, lone_pairs=[2])
s.curly(im.atom(2), im.atom(7), bend=0.4)
s.curly(im.bond(7, 9), im.atom(9), bend=-0.8)
row(s, [("arrow", "acyl transfer,", "tautomerism"), ("*C(OC(*)=O)C(=O)N*", {"labels": {0: "R$^1$", 4: "R$^2$", 9: "R$^3$"}})], x=4.6, y=y)
s.draw()
