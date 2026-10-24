"""Base-catalysed retro-aldol cleavage of diacetone alcohol (4-hydroxy-4-methylpentan-2-one). After
hydroxide removes the OH proton, the alkoxide lone pair re-forms a C=O bond and pushes out the
enolate of acetone: the C(alpha)-C(beta) bond electrons become the C=C of the enolate and the C=O
electrons move onto its oxygen. Protonation of the enolate gives a second molecule of acetone."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("CC(=O)CC(C)(C)[O-]", at=(0, 0), lone_pairs=[7])
s.curly(a.atom(7), a.bond(4, 7), bend=0.7)
s.curly(a.bond(3, 4), a.bond(1, 3), bend=0.7)
s.curly(a.bond(1, 2), a.atom(2), bend=0.7)
s.text((0, -1.9), "alkoxide of diacetone alcohol")
s.arrow((2.2, 0), (3.6, 0), kind="equilibrium")
s.molecule("CC(C)=O", at=(4.8, 0))
s.plus((6.0, 0))
s.molecule("C=C([O-])C", at=(7.2, 0))
s.arrow((8.4, 0), (9.8, 0), above=r"H$_2$O", below=r"$-$HO$^-$")
s.molecule("CC(C)=O", at=(11.0, 0))
s.draw()
