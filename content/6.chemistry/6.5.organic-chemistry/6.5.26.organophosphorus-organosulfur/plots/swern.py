"""Swern oxidation of cyclohexanol, after DMSO has been activated by oxalyl chloride at -78 C to
the chlorodimethylsulfonium ion (with loss of CO, CO2 and chloride). Top: the alcohol oxygen
attacks sulfur and chloride leaves, giving an alkoxysulfonium ion. Bottom: triethylamine removes
a proton from a methyl group on sulfur; the resulting sulfonium ylide takes the carbinol hydrogen
through a five-membered cyclic transition state (an intramolecular syn elimination), giving
cyclohexanone and dimethyl sulfide."""

from wikichem import Scheme

s = Scheme()
alc = s.molecule("OC1CCCCC1", at=(-0.4, 0), lone_pairs=[0])
cs = s.molecule("Cl[S+](C)C", coords=[(3.6, 0.0), (2.6, 0.0), (2.1, 0.87), (2.1, -0.87)], lone_pairs=[])
s.curly(alc.atom(0), cs.atom(1), bend=-0.5)
s.curly(cs.bond(0, 1), cs.atom(0), bend=-0.6)
s.arrow((4.6, 0), (6.0, 0), above="$-$Cl$^-$")
s.molecule("C[S+](C)OC1CCCCC1", at=(9.2, 0))
s.arrow((12.4, 0), (13.8, 0), above="Et$_3$N")

y = -5.0
# five-membered transition-state geometry: CH2(-) S O C1 H around a pentagon
pent = [(-0.81, 0.26), (0.0, 0.85), (0.0, 1.85), (0.81, 0.26), (0.5, -0.69), (-0.5, -0.69)]
c = (0.5 + 0.866, -0.69 - 0.5)
import math
ring = [(c[0] + math.cos(math.radians(a)), c[1] + math.sin(math.radians(a))) for a in (90, 30, -30, -90, 210)]
yl = s.molecule("[CH2-][S+](C)OC1([H])CCCCC1", coords=pent + ring, at=(0, y), lone_pairs=[0])
s.curly(yl.atom(0), yl.atom(5), bend=0.5)
s.curly(yl.bond(4, 5), yl.bond(3, 4), bend=0.6)
s.curly(yl.bond(1, 3), yl.atom(1), bend=0.5)
s.text((0.6, y - 2.6), "sulfonium ylide", size=12)
s.arrow((3.6, y), (5.0, y))
s.molecule("O=C1CCCCC1", at=(7.0, y))
s.plus((9.0, y))
s.molecule("CSC", at=(10.2, y))
s.draw()
