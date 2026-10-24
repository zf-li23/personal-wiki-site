"""Neophyl rearrangement: a 1,2-aryl shift in a radical. The primary 2-methyl-2-phenylpropyl
(neophyl) radical adds to the ipso carbon of its own ring (fishhook arrows, one electron each),
giving a spiro cyclohexadienyl radical (a cyclopropane fused at one carbon). The other cyclopropane
bond then breaks so that the ring becomes aromatic again and the unpaired electron moves to the
tertiary carbon: the phenyl group has migrated from C2 to C1. Hydrogen and alkyl groups do not make
such 1,2-shifts in radicals, because they cannot form the bridged intermediate."""

import math

from wikichem import Scheme


def hexagon(cx, cy, start=180):
    return [(cx + math.cos(math.radians(start + 60 * k)), cy + math.sin(math.radians(start + 60 * k))) for k in range(6)]


def shift(coords, dx, dy):
    return [(x + dx, q + dy) for x, q in coords]


# neophyl: CH2, C(Me2), Me, Me, then the ring starting at ipso (Kekule, ipso=ortho double bond below)
NEOPHYL = [(-1.0, -0.75), (-1.0, 0.3), (-1.9, 0.8), (-0.6, 1.2)] + hexagon(1.0, 0.0)
# spiro radical: Me, C(Me2), Me, CH2, spiro C, then the ring (radical carbon below the spiro carbon)
SPIRO = [(-1.65, 1.15), (-0.85, 0.5), (-0.55, 1.45), (-0.85, -0.5)] + hexagon(1.0, 0.0)

s = Scheme(scale=0.42)
y = 0.0
r = s.molecule("[CH2]C(C)(C)C1=CC=CC=C1", coords=shift(NEOPHYL, -0.5, y))
m = (r.xy(0) + r.xy(4)) / 2
s.curly(r.atom(0), m, bend=-0.5, single=True)
s.curly(r.bond(4, 5), m, bend=0.5, single=True)
s.curly(r.bond(4, 5), r.atom(5), bend=-0.6, single=True)
s.text((0.0, y - 2.4), "neophyl radical (1°)")
s.arrow((2.2, y), (3.6, y))
sp = s.molecule("CC1(C)CC12[CH]C=CC=C2", coords=shift(SPIRO, 5.3, y))
m2 = (sp.xy(4) + sp.xy(5)) / 2
s.curly(sp.atom(5), m2, bend=0.6, single=True)
s.curly(sp.bond(1, 4), m2, bend=-0.6, single=True)
s.curly(sp.bond(1, 4), sp.atom(1), bend=0.6, single=True)
s.text((5.8, y - 2.4), "spiro cyclohexadienyl radical")
s.arrow((8.2, y), (9.6, y))
s.molecule("C[C](C)Cc1ccccc1", at=(12.0, y))
s.text((12.0, y - 2.4), "tertiary radical (3°)")
s.draw()
