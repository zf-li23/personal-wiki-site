"""Release of the amine in the Gabriel synthesis by hydrazinolysis (Ing-Manske). Top: one nitrogen
of hydrazine adds to an imide carbonyl carbon; the tetrahedral intermediate collapses and expels the
amide nitrogen, opening the ring (proton transfers not shown). Bottom: the free NH2 group of the
hydrazide attacks the second carbonyl carbon in the same molecule, and collapse of this cyclic
tetrahedral intermediate expels ethylamine, leaving the stable six-membered phthalhydrazide."""

from wikichem import Scheme

s = Scheme()
y = 0.0
im = s.molecule("CCN1C(=O)c2ccccc2C1=O", at=(0, y), lone_pairs=[4])
hz = s.molecule("NN", at=(-0.2, y + 2.4), lone_pairs=True)
s.curly(hz.atom(1), im.atom(3), bend=0.4)
s.curly(im.bond(3, 4), im.atom(4), bend=0.7)
s.text((0, y - 2.2), "N-ethylphthalimide")
s.arrow((2.8, y), (4.2, y), kind="equilibrium")
t = s.molecule("CCN1C([O-])([NH2+]N)c2ccccc2C1=O", at=(6.6, y), lone_pairs=[4])
s.curly(t.atom(4), t.bond(3, 4), bend=0.7)
s.curly(t.bond(2, 3), t.atom(2), bend=0.7)
s.text((6.6, y - 2.6), "tetrahedral intermediate")

y = -6.0
c2 = s.molecule("CCNC1([O-])c2ccccc2C(=O)N[NH2+]1", at=(6.0, y), lone_pairs=[4])
op = s.molecule("CCNC(=O)c1ccccc1C(=O)NN", at=(0, y), like=c2, lone_pairs=[4, 14])
s.curly(op.atom(14), op.atom(3), bend=-0.4)
s.curly(op.bond(3, 4), op.atom(4), bend=-0.7)
s.text((0, y - 2.4), "ring-opened hydrazide")
s.arrow((2.2, y), (3.6, y), kind="equilibrium")
s.curly(c2.atom(4), c2.bond(3, 4), bend=0.7)
s.curly(c2.bond(2, 3), c2.atom(2), bend=0.7)
s.arrow((8.4, y), (9.8, y))
s.molecule("O=C1NNC(=O)c2ccccc12", at=(11.6, y))
s.text((11.6, y - 2.2), "phthalhydrazide")
s.plus((13.8, y))
s.molecule("CCN", at=(15.0, y))
s.draw()
