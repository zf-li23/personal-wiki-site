"""Decarboxylation of an amino acid bound to pyridoxal phosphate (PLP) as an aldimine (Schiff base).
The carboxylate leaves as CO2, and the C-C bond pair flows through the C=N bond and the pyridine ring
onto the protonated ring nitrogen, the electron sink; the result is a neutral quinonoid intermediate.
Protonation at the former alpha carbon and hydrolysis of the imine release the amine (dopamine,
histamine or GABA from the corresponding amino acids). R is the amino acid side chain; CH2OP is the
phosphorylated hydroxymethyl group of PLP."""

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
AD = "[O-]C(=O)C(*)N=CC1=C(*)C=[NH+]C(C)=C1O"
ad = s.molecule(AD, at=(0.0, 0.0), rotate=turn(AD, 3, 1, 90), labels={4: "R", 9: "CH$_2$OP"}, lone_pairs=[0])
s.curly(ad.atom(0), ad.bond(0, 1), bend=0.8)
s.curly(ad.bond(1, 3), ad.bond(3, 5), bend=0.7)
s.curly(ad.bond(5, 6), ad.bond(6, 7), bend=0.7)
s.curly(ad.bond(7, 8), ad.bond(8, 10), bend=0.7)
s.curly(ad.bond(10, 11), ad.atom(11), bend=0.7)
QU = "*C=NC=C1C(*)=CNC(C)=C1O"
row(s, [("arrow", r"$-$CO$_2$"), (QU, {"rotate": turn(QU, 1, 2, -30), "labels": {0: "R", 6: "CH$_2$OP"}})], x=3.4, y=0.0)
s.text((7.6, -3.2), "quinonoid intermediate", size=11)
s.draw()
