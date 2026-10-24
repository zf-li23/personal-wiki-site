"""Directed ortho metalation of N,N-diethylbenzamide. The amide oxygen coordinates the lithium of
the alkyllithium (dashed line), which holds the basic carbon next to the ortho C-H bond
(complex-induced proximity effect); the C-Li electrons take the ortho proton, and the aryllithium
stays chelated by the amide oxygen. Quenching with an electrophile (here iodomethane) puts the new
group ortho to the directing group."""

from wikichem import Scheme

s = Scheme()
RING = [(0, 1.0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -0.5), (0.87, 0.5)]
AMIDE = [(-1.74, 4.0), (-0.87, 3.5), (-0.87, 2.5), (-1.74, 2.0), (-2.61, 2.5), (0, 2.0), (0.87, 2.5)]
am = s.molecule("CCN(CC)C(=O)c1ccccc1[H]", coords=AMIDE + RING + [(1.74, 1.0)], lone_pairs=[6])
bu = s.molecule("[Li]CCCC", coords=[(2.3, 2.7), (2.8, 1.8), (3.8, 1.8), (4.3, 0.93), (5.3, 0.93)])
s.partial(am.atom(6), bu.atom(0))
s.curly(bu.bond(0, 1), am.atom(13), bend=-0.5)
s.curly(am.bond(12, 13), am.atom(12), bend=-0.6)
s.arrow((6.0, 1.4), (7.4, 1.4), above="$-$BuH")
x = 10.0
li = s.molecule("CCN(CC)C(=O)c1ccccc1[Li]", coords=AMIDE + RING + [(1.74, 1.0)], at=(x, 0))
s.partial(li.atom(6), li.atom(13))
s.arrow((12.6, 1.4), (14.0, 1.4), above="CH$_3$I")
s.molecule("CCN(CC)C(=O)c1ccccc1C", coords=AMIDE + RING + [(1.74, 1.0)], at=(17.0, 0))
s.draw()
