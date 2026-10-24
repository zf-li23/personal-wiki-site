"""Decarboxylative Claisen condensation, the C-C bond-forming step of fatty-acid and polyketide
synthesis, with methyl thioesters standing in for the enzyme-bound thioesters. Top: the
carboxylate of a malonyl thioester pushes electrons to form CO2, and the C-C bond electrons become
the C=C of a thioester enolate. Bottom: the enolate carbon attacks the carbonyl carbon of an acetyl
thioester; the tetrahedral intermediate expels the thiolate, giving the acetoacetyl thioester."""

from wikichem import Scheme

s = Scheme()
y = 0.0
mal = s.molecule("CSC(=O)CC(=O)[O-]", at=(0, y), rotate=90, lone_pairs=[7, 3])
s.curly(mal.atom(7), mal.bond(5, 7), bend=0.7)
s.curly(mal.bond(4, 5), mal.bond(2, 4), bend=0.8)
s.curly(mal.bond(2, 3), mal.atom(3), bend=0.8)
s.text((0, y - 2.4), "malonyl thioester")
s.arrow((2.0, y), (3.4, y))
s.molecule("CSC([O-])=C", at=(4.8, y))
s.plus((6.3, y))
s.molecule("O=C=O", at=(7.8, y), show_carbons=[1])
s.text((4.8, y - 1.6), "thioester enolate")

y = -5.0
en = s.molecule("C=C([O-])SC", at=(0, y + 0.8), rotate=180, lone_pairs=[2])
ac = s.molecule("CC(=O)SC", at=(0.6, y - 1.6), lone_pairs=[2])
s.curly(en.atom(2), en.bond(1, 2), bend=0.7)
s.curly(en.bond(0, 1), ac.atom(1), bend=-0.6)
s.curly(ac.bond(1, 2), ac.atom(2), bend=0.7)
s.text((2.6, y - 2.6), "acetyl thioester")
s.arrow((2.8, y), (4.2, y))
t = s.molecule("CSC(=O)CC(C)([O-])SC", at=(6.4, y), lone_pairs=[7])
s.curly(t.atom(7), t.bond(5, 7), bend=0.8)
s.curly(t.bond(5, 8), t.atom(8), bend=-0.8)
s.arrow((8.6, y), (10.0, y), below=r"$-$MeS$^-$")
s.molecule("CSC(=O)CC(C)=O", at=(11.8, y))
s.text((11.8, y - 1.6), "acetoacetyl thioester")
s.draw()
