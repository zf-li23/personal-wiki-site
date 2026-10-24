"""Addition of methanol to ketene. The alcohol oxygen attacks the central sp carbon in the plane of
the molecule (where the C=O pi* orbital lies); the C=O pi electrons move onto oxygen. Proton
transfer gives the enol of the ester, which tautomerises to methyl acetate."""

from wikichem import Scheme

s = Scheme()
me = s.molecule("CO", at=(0.6, 1.6), lone_pairs=[1])
ke = s.molecule("C=C=O", at=(0.6, -0.2), lone_pairs=[2])
s.curly(me.atom(1), ke.atom(1), bend=-0.4)
s.curly(ke.bond(1, 2), ke.atom(2), bend=-0.8)
s.arrow((2.4, 0), (3.8, 0))
s.molecule("C=C([O-])[OH+]C", at=(5.2, 0))
s.arrow((6.6, 0), (8.0, 0), above="H$^+$ shift")
s.molecule("C=C(O)OC", at=(9.4, 0))
s.text((9.4, -1.5), "enol", size=13)
s.arrow((10.8, 0), (12.2, 0))
s.molecule("CC(=O)OC", at=(13.6, 0))
s.draw()
