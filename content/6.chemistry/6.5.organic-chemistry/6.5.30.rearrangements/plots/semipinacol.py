"""Semipinacol ring expansion of 1-[hydroxy(phenyl)methyl]cyclopropan-1-ol. The benzylic hydroxyl,
protonated (or bound to BF3), leaves as water; a ring C-C bond of the cyclopropanol migrates with its
electron pair to the benzylic carbon as the water departs, the three-membered ring becomes a
four-membered ring, and the positive charge ends on the carbinol carbon, where the oxygen lone pair
turns it into a protonated carbonyl. Loss of the proton gives 2-phenylcyclobutan-1-one."""

from wikichem import Scheme

s = Scheme()
y = 0.0
m = s.molecule("OC1(C([OH2+])c2ccccc2)CC1", at=(0.0, y), lone_pairs=[0])
s.curly(m.bond(1, 10), m.atom(2), bend=-0.6)
s.curly(m.bond(2, 3), m.atom(3), bend=0.6)
s.curly(m.atom(0, pair=1), m.bond(0, 1), bend=0.8)
s.text((0.0, y - 3.3), "protonated benzylic alcohol")
s.arrow((2.8, y), (4.4, y), above=r"$-$H$_2$O", below="1,2-shift")
s.molecule("[OH+]=C1CCC1c1ccccc1", at=(7.0, y))
s.text((7.0, y - 3.3), "protonated cyclobutanone")
s.arrow((9.6, y), (11.0, y), above=r"$-$H$^+$")
s.molecule("O=C1CCC1c1ccccc1", at=(13.6, y))
s.text((13.6, y - 3.3), "2-phenylcyclobutanone")
s.draw()
