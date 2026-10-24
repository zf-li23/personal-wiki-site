"""Hantzsch thiazole synthesis from chloroacetone and thioacetamide. Top: the soft sulfur atom
displaces chloride by SN2. Bottom: after loss of a proton, the nitrogen of the S-alkyl isothioamide
attacks the ketone carbonyl in the same molecule, closing the five-membered ring; the
4-hydroxythiazoline then loses water and aromatises to 2,4-dimethylthiazole."""

from wikichem import Scheme

s = Scheme()
y = 0.0
th = s.molecule("CC(N)=S", at=(-1.6, y), lone_pairs=[3])
ca = s.molecule("CC(=O)CCl", at=(1.6, y - 0.2), lone_pairs=[4])
s.curly(th.atom(3), ca.atom(3), bend=-0.4)
s.curly(ca.bond(3, 4), ca.atom(4), bend=0.6)
s.arrow((3.4, y), (4.8, y), below=r"$-$Cl$^-$")
s.molecule("CC(=O)CSC(C)=[NH2+]", at=(6.8, y))

y = -4.0
cyc = s.molecule("CC1([O-])CSC(C)=[NH+]1", at=(4.2, y))
op = s.molecule("CC(=O)CSC(C)=N", at=(0, y), like=cyc, lone_pairs=[7])
s.curly(op.atom(7), op.atom(1), bend=-0.4)
s.curly(op.bond(1, 2), op.atom(2), bend=-0.6)
s.text((0, y - 1.8), r"after $-$H$^+$")
s.arrow((1.6, y), (2.8, y))
s.arrow((6.0, y), (7.8, y), above="proton transfer", below=r"$-$H$_2$O")
s.molecule("Cc1csc(C)n1", at=(9.4, y))
s.text((9.4, y - 1.8), "2,4-dimethylthiazole")
s.draw()
