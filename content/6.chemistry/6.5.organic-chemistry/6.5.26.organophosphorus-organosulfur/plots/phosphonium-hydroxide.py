"""Decomposition of a quaternary phosphonium hydroxide (benzyltriphenylphosphonium, phenyl groups
written Ph). Top: hydroxide adds to phosphorus, giving a five-coordinate hydroxyphosphorane
(trigonal bipyramid: OH and benzyl in the axial positions). Bottom: a second hydroxide removes the
O-H proton; the O-H electrons become the P=O bond while the P-C bond breaks toward carbon, so the
group that best stabilizes a negative charge (benzyl) leaves as a carbanion, which takes a proton
from water. Products: toluene and triphenylphosphine oxide. A quaternary ammonium hydroxide cannot
do this (nitrogen does not become five-coordinate); it undergoes Hofmann elimination instead."""

from wikichem import Scheme

s = Scheme()
BN = {1: "Ph", 2: "Ph", 3: "Ph", 4: "CH$_2$Ph"}
ph = s.molecule("[P+](*)(*)(*)*", coords=[(0, 0), (0, 1.0), (-0.87, -0.5), (0.87, -0.5), (0, -1.1)], labels=BN)
oh = s.molecule("[OH-]", at=(-2.4, 0.6), lone_pairs=True)
s.curly(oh.atom(0), ph.atom(0), bend=-0.4)
s.arrow((1.8, 0), (3.2, 0))
x = 5.4
TBP = [(0, 0), (0, 1.0), (0.8, 1.6), (-1.1, 0), (0.7, 0.6), (0.7, -0.6), (0, -1.1)]
s.molecule("P(O[H])(*)(*)(*)*", coords=TBP, at=(x, 0), labels={3: "Ph", 4: "Ph", 5: "Ph", 6: "CH$_2$Ph"})
s.text((x, -2.1), "hydroxyphosphorane", size=11)

y = -4.6
hp = s.molecule("P(O[H])(*)(*)(*)*", coords=TBP, at=(0, y), labels={3: "Ph", 4: "Ph", 5: "Ph", 6: "CH$_2$Ph"})
oh2 = s.molecule("[OH-]", at=(2.4, y + 2.0), lone_pairs=True)
s.curly(oh2.atom(0), hp.atom(2), bend=0.4)
s.curly(hp.bond(1, 2), hp.bond(0, 1), bend=0.8)
s.curly(hp.bond(0, 6), hp.atom(6), bend=-0.6)
s.arrow((2.4, y), (3.8, y), below="$-$H$_2$O")
x = 6.2
s.molecule("O=P(*)(*)*", coords=[(0, 1.0), (0, 0), (-0.87, -0.5), (0.87, -0.5), (0, -1.0)], at=(x, y + 0.3),
           labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.plus((x + 1.8, y))
s.molecule("[CH2-]c1ccccc1", at=(x + 3.6, y))
s.arrow((x + 5.4, y), (x + 6.8, y), above="H$_2$O")
s.molecule("Cc1ccccc1", at=(x + 8.6, y))
s.draw()
