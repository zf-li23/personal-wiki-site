"""Bromohydrin formation from 1-methylcyclohexene (Br2 in water). The pi bond attacks bromine to give
the bromonium ion; water, present in large excess, opens it from the face opposite to the bridging
bromine at the more substituted carbon (that C-Br bond is longer and carries more positive charge).
Loss of a proton gives the trans bromohydrin, OH on the tertiary carbon (racemic)."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


ang = np.radians([150, 210, 270, 330, 30, 90])
ring = [(np.cos(t), np.sin(t)) for t in ang]
me = (ring[0][0] - 0.5, ring[0][1] + 0.87)

s = Scheme()
alkene = fixed(s, "CC1=CCCCC1", [me] + ring)
br2 = fixed(s, "BrBr", [(-2.2, -0.2), (-3.4, -0.2)], lone_pairs=(0, 1))
s.curly(alkene.bond(1, 2), br2.atom(0), bend=0.5)
s.curly(br2.bond(0, 1), br2.atom(1), bend=-0.9)
s.arrow((1.5, 0), (3.0, 0))

x = 6.2
ion = fixed(s, "CC12CCCCC1[Br+]2", [me, ring[0], ring[5], ring[4], ring[3], ring[2], ring[1], (-2.0, 0)], at=(x, 0))
water = fixed(s, "O", [(x + 0.4, 2.3)], lone_pairs=(0,))
s.curly(water.atom(0), ion.atom(1), bend=0.3)
s.curly(ion.bond(1, 7), ion.atom(7), bend=-0.9)
s.arrow((x + 1.6, 0), (x + 3.1, 0), above=r"$-$H$^+$")
s.molecule("C[C@]1(O)CCCC[C@@H]1Br", at=(x + 5.3, 0))
s.text((x - 0.6, -1.8), "bromonium ion", size=10)
s.text((x + 5.3, -2.0), "trans (racemic)", size=10)
s.draw()
