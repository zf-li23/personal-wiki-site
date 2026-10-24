"""Reduction of cyclohexanone by lithium aluminium hydride in dry ether. The lithium cation
coordinates to the carbonyl oxygen (dashed bond) and activates it; an Al-H bond pair is delivered
to the carbonyl carbon and the C=O pi pair moves onto oxygen, giving an alkoxyaluminate. The
remaining three Al-H bonds reduce three more ketone molecules, and aqueous workup releases
cyclohexanol."""

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
KET = "O=C1CCCCC1"
al = s.molecule("[H][Al-]([H])([H])[H]", coords=[(0.0, 1.0), (0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (1.0, 0.0)], at=(-2.0, 1.0))
ket = s.molecule(KET, at=(0.4, 0.6), rotate=turn(KET, 1, 0, 270), lone_pairs=[0])
li = ket.xy(0) + (0.0, -1.1)
s.text(li, r"Li$^+$")
s.partial(ket.atom(0), li + (0.0, 0.32))
s.curly(al.bond(1, 4), ket.atom(1), bend=-0.5)
s.curly(ket.bond(0, 1), ket.atom(0), bend=-0.9)
_, x = row(s, [("arrow", None), "[AlH3-]OC1CCCCC1"], x=2.6, y=0.0)
s.text((x - 0.2, -1.2), r"Li$^+$")
row(s, [("arrow", r"3 R$_2$C=O", r"then H$_2$O"), "OC1CCCCC1"], x=x, y=0.0)
s.draw()
