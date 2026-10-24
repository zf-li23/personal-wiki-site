"""Grignard reagents and nitriles give ketones. The C-Mg bonding pair adds to the nitrile carbon of
benzonitrile and the C-N pi electrons move onto nitrogen, giving the magnesium salt of an imine;
it does not react further, and aqueous acid hydrolyses the imine (via the iminium ion) to
acetophenone."""

from wikichem import Scheme

s = Scheme()
g = s.molecule("C[Mg]Br", at=(-0.8, 1.0))
n = s.molecule("N#Cc1ccccc1", at=(1.6, 0), lone_pairs=[0])
s.curly(g.bond(0, 1), n.atom(1), bend=-0.5)
s.curly(n.bond(0, 1), n.atom(0), bend=-0.8)
s.arrow((3.2, 0), (4.4, 0), above="ether")
s.molecule("CC(=N[Mg]Br)c1ccccc1", at=(7.9, 0))
s.text((7.9, -2.0), "imine salt")
s.arrow((10.4, 0), (11.8, 0), above=r"H$_3$O$^+$")
s.molecule("CC(=O)c1ccccc1", at=(13.4, 0))
s.draw()
