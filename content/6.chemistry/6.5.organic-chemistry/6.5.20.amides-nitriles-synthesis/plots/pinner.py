"""Pinner reaction. In dry HCl, the nitrile is protonated on nitrogen; ethanol adds to the activated
carbon and the C-N pi pair moves onto nitrogen, and loss of a proton from oxygen gives the imidate
hydrochloride (Pinner salt). Water converts the salt into the ester (with ammonium chloride), ammonia
into the amidine."""

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
et = s.molecule("CCO", coords=[(-2.0, 1.9), (-1.2, 1.4), (-0.6, 2.2)], lone_pairs=[2])
ni = s.molecule("CC#[NH+]", coords=[(-0.87, -0.5), (0.0, 0.0), (1.0, 0.0)])
s.curly(et.atom(2), ni.atom(1), bend=-0.4)
s.curly(ni.bond(1, 2), ni.atom(2), bend=0.8)
(ps,), x = row(s, [("arrow", r"$-$H$^+$"), "CCOC(C)=[NH2+]"], x=1.6, y=0.0)
s.text((ps.xy(3)[0], -1.3), r"Cl$^-$")
s.text((ps.xy(3)[0], -1.9), "Pinner salt", size=11)
s.arrow((x + 0.2, 0.4), (x + 1.5, 1.4), above=r"H$_2$O")
s.arrow((x + 0.2, -0.4), (x + 1.5, -1.4), below=r"NH$_3$")
row(s, ["CCOC(C)=O", "+", "[NH4+]"], x=x + 1.3, y=1.9)
row(s, [("CC(N)=[NH2+]", {}), "+", "CCO"], x=x + 1.3, y=-1.9)
s.draw()
