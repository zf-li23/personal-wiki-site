"""Dieckmann condensation of diethyl adipate. Top: the ester enolate attacks the carbonyl carbon of
the other ester group of the same molecule, closing a five-membered ring and giving a cyclic
tetrahedral intermediate. Bottom: the alkoxide lone pair re-forms C=O and ethoxide leaves, giving
ethyl 2-oxocyclopentane-1-carboxylate; as in the Claisen condensation, ethoxide then removes the
acidic proton between the two carbonyl groups, which drives the equilibrium, and acid work-up
returns the neutral beta-keto ester."""

from wikichem import Scheme

s = Scheme()
y = 0.0
t = s.molecule("CCOC1([O-])CCCC1C(=O)OCC", at=(6.6, y), lone_pairs=[4])
s.text((6.6, y - 2.2), "tetrahedral intermediate")
# same atom order as the ring: ethoxy C, C, O, attacked C, O, ring CH2 x3, alpha C, ester C, O, O, ethyl
en = s.molecule("CCOC(=O)CCCC=C([O-])OCC", at=(0, y), like=t, lone_pairs=[10])
s.curly(en.atom(10), en.bond(9, 10), bend=0.7)
s.curly(en.bond(8, 9), en.atom(3), bend=0.5)
s.curly(en.bond(3, 4), en.atom(4), bend=0.7)
s.text((0, y - 2.2), "ester enolate")
s.arrow((2.6, y), (4.0, y), kind="equilibrium")

y = -5.0
t2 = s.molecule("CCOC1([O-])CCCC1C(=O)OCC", at=(0, y), lone_pairs=[4])
s.curly(t2.atom(4), t2.bond(3, 4), bend=0.7)
s.curly(t2.bond(2, 3), t2.atom(2), bend=0.7)
s.arrow((2.6, y), (4.0, y), kind="equilibrium", below=r"$-$EtO$^-$")
s.molecule("CCOC(=O)C1CCCC1=O", at=(7.0, y))
s.text((7.0, y - 2.0), "cyclic beta-keto ester")
s.draw()
