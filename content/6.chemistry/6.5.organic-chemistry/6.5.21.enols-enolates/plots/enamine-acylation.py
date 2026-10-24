"""Acylation of the pyrrolidine enamine of cyclohexanone (Stork). The nitrogen lone pair pushes the
C=C electrons onto the carbonyl carbon of acetyl chloride and the C=O electrons move onto oxygen.
The tetrahedral intermediate collapses, re-forming C=O and expelling chloride, giving an acyl
iminium ion; aqueous acid hydrolyses the iminium ion to 2-acetylcyclohexanone and pyrrolidine."""

from wikichem import Scheme

s = Scheme()
y = 0.0
en = s.molecule("N1(CCCC1)C1=CCCCC1", at=(0, y), lone_pairs=[0])
ac = s.molecule("CC(=O)Cl", at=(2.4, y + 1.6), lone_pairs=[2])
s.curly(en.atom(0), en.bond(0, 5), bend=0.6)
s.curly(en.bond(5, 6), ac.atom(1), bend=-0.4)
s.curly(ac.bond(1, 2), ac.atom(2), bend=-0.6)
s.text((0, y - 2.6), "enamine")
s.arrow((3.8, y), (5.2, y))
t = s.molecule("[N+]1(CCCC1)=C1CCCCC1C(C)([O-])Cl", at=(7.6, y), lone_pairs=[13])
s.curly(t.atom(13, pair=2), t.bond(11, 13), bend=0.8)
s.curly(t.bond(11, 14), t.atom(14), bend=1.0)
s.text((7.6, y - 2.8), "tetrahedral intermediate")

y = -5.6
s.arrow((-2.2, y), (-0.8, y), below=r"$-$Cl$^-$")
s.molecule("[N+]1(CCCC1)=C1CCCCC1C(C)=O", at=(1.6, y))
s.text((1.6, y - 2.6), "acyl iminium ion")
s.arrow((4.0, y), (5.4, y), above=r"H$_3$O$^+$", below=r"$-$pyrrolidine")
s.molecule("CC(=O)C1CCCCC1=O", at=(7.4, y))
s.text((7.4, y - 2.0), "2-acetylcyclohexanone")
s.draw()
