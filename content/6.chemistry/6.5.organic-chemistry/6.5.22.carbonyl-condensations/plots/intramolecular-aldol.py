"""Intramolecular aldol condensation of hexane-2,5-dione. The enolate formed at the C1 methyl group
attacks the C5 carbonyl carbon, closing a five-membered ring (the enolate oxygen lone pair pushes
the C=C electrons onto C5 and the C5=O electrons move onto oxygen). Protonation gives the aldol,
3-hydroxy-3-methylcyclopentanone, which dehydrates by E1cB to 3-methylcyclopent-2-en-1-one."""

from wikichem import Scheme

s = Scheme()
ring = s.molecule("C1C(=O)CCC1(C)[O-]", at=(4.6, 0))
s.text((4.6, -1.9), "cyclic alkoxide")
# atom order as in the ring: C1, C2, O, C3, C4, C5, C6 (methyl), O
en = s.molecule("C=C([O-])CCC(C)=O", at=(0, 0), like=ring, lone_pairs=[2, 7])
s.curly(en.atom(2), en.bond(1, 2), bend=-0.7)
s.curly(en.bond(0, 1), en.atom(5), bend=-0.5)
s.curly(en.bond(5, 7), en.atom(7), bend=-0.6)
s.text((0, -1.9), "enolate at C1")
s.arrow((1.6, 0), (3.0, 0), kind="equilibrium")
s.arrow((6.6, 0), (8.6, 0), above=r"H$_2$O", below=r"$-$H$_2$O, E1cB")
s.molecule("CC1=CC(=O)CC1", at=(10.6, 0))
s.text((10.6, -1.9), "3-methylcyclopent-2-enone")
s.draw()
