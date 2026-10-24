"""Wittig reaction of propanal with the non-stabilised ylide Ph3P=CHCH3 (the three phenyl groups
on phosphorus are written Ph). Top: the nucleophilic ylide carbon bonds to the carbonyl carbon
while the carbonyl oxygen bonds to phosphorus: a concerted, asynchronous [2+2] cycloaddition that
gives the oxaphosphetane directly and irreversibly (lithium-free conditions). Bottom: the
four-membered ring falls apart in a syn cycloreversion to the alkene and triphenylphosphine oxide;
the cis oxaphosphetane gives the Z alkene."""

import math

import numpy as np

from wikichem import Scheme

s = Scheme()


def phenyls(mol, centre, subs):
    """Write Ph at the ends of the stand-in bonds from phosphorus."""
    for k in subs:
        u = mol.xy(k) - mol.xy(centre)
        u = u / np.linalg.norm(u)
        s.text(mol.xy(k) + 0.32 * u, "Ph", size=13)


def ring(n, r=1.0, start=90):
    return [(r * math.cos(math.radians(start + i * 360 / n)), r * math.sin(math.radians(start + i * 360 / n))) for i in range(n)]


# ylide: P at the origin, carbanion to the right, phenyls to the left and below
yl = s.molecule("C[CH-][P+](C)(C)C",
                coords=[(1.5, -0.87), (1.0, 0.0), (0.0, 0.0), (-0.87, 0.5), (-1.0, 0.0), (-0.5, -0.87)],
                at=(0, 0), lone_pairs=[1])
phenyls(yl, 2, [3, 4, 5])
ald = s.molecule("O=CCC", coords=[(0.0, 1.6), (1.0, 1.6), (1.5, 2.47), (2.5, 2.47)], at=(0, 0), lone_pairs=[0])
s.curly(yl.atom(1), ald.atom(1), bend=0.5)
s.curly(ald.bond(0, 1), yl.atom(2), bend=0.5)  # the C=O pi pair forms the O-P bond
s.arrow((3.0, 0.8), (4.6, 0.8), above="[2+2]")

x = 7.0
ox = s.molecule("CCC1OP(C)(C)(C)C1C",
                coords=[(2.5, 2.47), (1.5, 2.47), (1.0, 1.6), (0.0, 1.6), (0.0, 0.6), (-0.87, 1.1), (-1.0, 0.6),
                        (-0.5, -0.27), (1.0, 0.6), (1.5, -0.27)],
                at=(x, 0))
phenyls(ox, 4, [5, 6, 7])
s.text((x + 0.5, -1.2), "cis-oxaphosphetane", size=13)

y = -4.6
ox2 = s.molecule("CCC1OP(C)(C)(C)C1C",
                 coords=[(2.5, 2.47), (1.5, 2.47), (1.0, 1.6), (0.0, 1.6), (0.0, 0.6), (-0.87, 1.1), (-1.0, 0.6),
                         (-0.5, -0.27), (1.0, 0.6), (1.5, -0.27)],
                 at=(0, y))
phenyls(ox2, 4, [5, 6, 7])
s.curly(ox2.bond(4, 8), ox2.bond(2, 8), bend=-0.6)
s.curly(ox2.bond(2, 3), ox2.bond(3, 4), bend=-0.6)
s.arrow((3.0, y + 0.8), (4.6, y + 0.8))
s.molecule("CC/C=C\\C", at=(6.4, y + 0.8))
s.plus((8.0, y + 0.8))
po = s.molecule("O=P(C)(C)C", coords=[(1.0, 0.0), (0.0, 0.0), (-0.5, 0.87), (-1.0, 0.0), (-0.5, -0.87)], at=(10.2, y + 0.8))
phenyls(po, 1, [2, 3, 4])
s.draw()
