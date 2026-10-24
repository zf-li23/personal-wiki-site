"""Imine formation from acetone and methylamine. The amine nitrogen adds to the carbonyl carbon;
proton transfers give the neutral hemiaminal (carbinolamine). Acid then protonates the OH, and the
nitrogen lone pair pushes out water to give an iminium ion, which loses its N-H proton to give the
imine. Every step is reversible; the reverse sequence is imine hydrolysis."""

from wikichem import Scheme

s = Scheme()
y = 0.0
am = s.molecule("CN", at=(-2.4, 1.2), lone_pairs=[1])
ket = s.molecule("CC(=O)C", at=(0.0, 0), lone_pairs=[2])
s.curly(am.atom(1), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 2), ket.atom(2), bend=-1.2)
s.arrow((1.6, y), (3.0, y), kind="equilibrium")
s.molecule("C[NH2+]C(C)(C)[O-]", at=(4.6, y))
s.arrow((6.2, y), (7.8, y), above="H$^+$ shift", kind="equilibrium")
s.molecule("CNC(C)(C)O", at=(9.4, y))
s.text((9.4, y - 1.7), "hemiaminal")

y = -4.2
pr = s.molecule("CNC(C)(C)[OH2+]", at=(0.0, y), lone_pairs=[1])
s.curly(pr.atom(1), pr.bond(1, 2), bend=-0.8)
s.curly(pr.bond(2, 5), pr.atom(5), bend=0.8)
s.arrow((1.8, y), (3.2, y), above=r"$-$H$_2$O", kind="equilibrium")
s.molecule("C[NH+]=C(C)C", at=(4.8, y))
s.text((4.8, y - 1.6), "iminium ion")
s.arrow((6.4, y), (7.8, y), above=r"$-$H$^+$", kind="equilibrium")
s.molecule("CN=C(C)C", at=(9.4, y))
s.text((9.4, y - 1.6), "imine")
s.draw()
