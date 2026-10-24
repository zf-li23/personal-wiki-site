"""Formation of diethyl ether from ethanol in concentrated sulfuric acid at 140 C (SN2). The oxygen of
one ethanol molecule attacks the CH2 carbon of a protonated ethanol molecule from the back side as
water leaves; the protonated ether then loses a proton."""

from wikichem import Scheme

s = Scheme()
ox = s.molecule("CC[OH2+]", coords=[(-0.5, 0.87), (0, 0), (1.0, 0)], at=(2.4, 0))
nu = s.molecule("CCO", coords=[(-1.73, 0.5), (-0.87, 0), (0, 0.5)], at=(0.0, -0.4), lone_pairs=[2])
s.curly(nu.atom(2), ox.atom(1), bend=0.4)
s.curly(ox.bond(1, 2), ox.atom(2), bend=0.8)
s.arrow((4.4, 0), (5.6, 0), below=r"$-$H$_2$O")
s.molecule("CC[OH+]CC", coords=[(-1.73, -0.25), (-0.87, -0.75), (0, -0.25), (0.87, -0.75), (1.73, -0.25)], at=(7.8, 0.3))
s.arrow((10.0, 0), (11.2, 0), below=r"$-$H$^+$")
s.molecule("CCOCC", at=(13.0, 0))
s.draw()
