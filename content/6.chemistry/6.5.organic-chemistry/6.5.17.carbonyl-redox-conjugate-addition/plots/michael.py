"""Michael addition of diethyl malonate to but-3-en-2-one (methyl vinyl ketone) catalysed by sodium
ethoxide. The malonate enolate (the donor) attacks the beta carbon of the acceptor; the C=C pi pair
moves between the alpha carbon and the carbonyl carbon and the C=O pi pair moves onto oxygen, giving
a new enolate. This more basic enolate takes a proton from ethanol, regenerating the ethoxide
catalyst."""

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
don = s.molecule("*C(=O)[CH-]C(=O)*", coords=[(-1.74, 0.0), (-0.87, -0.5), (-0.87, -1.5), (0.0, 0.0), (0.87, -0.5), (0.87, -1.5), (1.74, 0.0)],
                 labels={0: "EtO", 6: "OEt"})
acc = s.molecule("C=CC(C)=O", coords=[(0.0, 1.7), (0.87, 2.2), (1.74, 1.7), (2.61, 2.2), (1.74, 0.7)], lone_pairs=[4])
s.curly(don.atom(3), acc.atom(0), bend=0.3)
s.curly(acc.bond(0, 1), acc.bond(1, 2), bend=-0.7)
s.curly(acc.bond(2, 4), acc.atom(4), bend=-0.7)
row(s, [("arrow", None), "CCOC(=O)C(CC=C(C)[O-])C(=O)OCC", ("arrow", "EtOH", r"$-$EtO$^-$"), "CCOC(=O)C(CCC(C)=O)C(=O)OCC"], x=3.0, y=0.6)
s.draw()
