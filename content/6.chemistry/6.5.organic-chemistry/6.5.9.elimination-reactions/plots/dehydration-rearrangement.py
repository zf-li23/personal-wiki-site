"""Acid-catalysed dehydration of 3,3-dimethylbutan-2-ol (E1 with rearrangement). The protonated alcohol
loses water to give a secondary carbocation; a methyl group on the neighbouring quaternary carbon
migrates with its bonding pair (1,2-methyl shift), giving a more stable tertiary cation; loss of a
proton from the adjacent CH gives 2,3-dimethylbut-2-ene (Zaitsev product, 64%)."""

from wikichem import Scheme

s = Scheme()
ox = s.molecule("CC([OH2+])C(C)(C)C", at=(0, 0))
s.curly(ox.bond(1, 2), ox.atom(2), bend=0.7)
s.text((0, -1.7), "protonated alcohol")
s.arrow((1.8, 0), (3.2, 0), below=r"$-$H$_2$O")
sec = s.molecule("C[CH+]C(C)(C)C", at=(4.8, 0))
s.curly(sec.bond(2, 3), sec.atom(1), bend=0.7)
s.text((4.8, -1.7), r"2$^\circ$ cation")
s.arrow((6.4, 0), (7.8, 0), above="1,2-CH$_3$ shift")
ter = s.molecule("CC(C)([H])[C+](C)C", coords=[(-1, 0), (0, 0), (0, 1), (-0.3, -0.95), (0.87, -0.5), (1.73, 0), (0.87, -1.5)], at=(9.2, 0.3))
w = s.molecule("O", at=(8.0, -2.0), explicit_h=True, lone_pairs=[0])
s.curly(w.atom(0), ter.atom(3), bend=0.4)
s.curly(ter.bond(1, 3), ter.bond(1, 4), bend=1.2)
s.text((9.8, 1.8), r"3$^\circ$ cation")
s.arrow((11.6, 0), (13.0, 0), below=r"$-$H$_3$O$^+$")
s.molecule("CC(C)=C(C)C", at=(14.4, 0))
s.draw()
