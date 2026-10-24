"""Norrish type I cleavage of the photoinitiator 2,2-dimethoxy-2-phenylacetophenone (DMPA).
At 365 nm the n,pi* state breaks the C(O)-C(alpha) bond homolytically (fishhook arrows), giving a
benzoyl radical and an alpha,alpha-dimethoxybenzyl radical. The benzoyl radical adds to the CH2
end of an acrylate (here methyl acrylate), starting the radical chain polymerization used in
photocuring."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    return np.asarray(p.xy, float) + np.asarray(d, float)


s = Scheme()
y = 0.0
d = s.molecule("COC(OC)(C(=O)c1ccccc1)c1ccccc1", at=(0.0, y))
mid = d.bond(2, 5)
s.curly(shift(mid, (0.15, 0.15)), shift(d.atom(5), (0.15, 0.35)), bend=-0.8, single=True)
s.curly(shift(mid, (-0.15, -0.15)), shift(d.atom(2), (-0.3, -0.2)), bend=0.8, single=True)
s.text((0.0, y - 3.0), "DMPA")
s.arrow((2.8, y), (4.4, y), above=r"$h\nu$ (365 nm)")
s.molecule("O=[C]c1ccccc1", at=(6.2, y))
s.plus((8.4, y))
s.molecule("CO[C](OC)c1ccccc1", at=(11.0, y))
y2 = -5.6
b2 = s.molecule("O=[C]c1ccccc1", at=(0.0, y2))
ac = s.molecule("C=CC(=O)OC", at=(3.6, y2))
m = (b2.xy(1) + ac.xy(0)) / 2
s.curly(b2.atom(1), m, bend=-0.5, single=True)
s.curly(shift(ac.bond(0, 1), (0.0, 0.15)), m, bend=0.6, single=True)
s.curly(shift(ac.bond(0, 1), (0.0, -0.15)), shift(ac.atom(1), (0.0, -0.35)), bend=-0.6, single=True)
s.text((1.8, y2 - 2.4), "benzoyl radical + methyl acrylate")
s.arrow((6.0, y2), (7.4, y2))
s.molecule("O=C(C[CH]C(=O)OC)c1ccccc1", at=(10.6, y2))
s.text((10.6, y2 - 2.4), "chain-carrying radical")
s.draw()
