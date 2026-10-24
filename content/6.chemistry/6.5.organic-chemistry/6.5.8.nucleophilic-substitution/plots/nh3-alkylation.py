"""SN2 with a neutral nucleophile. The lone pair of ammonia attacks bromoethane; the product is the
ethylammonium ion, which gives up a proton to a second ammonia molecule (the free amine can react
again, which is why alkylation of ammonia gives mixtures)."""

from wikichem import Scheme

s = Scheme()
n = s.molecule("N", at=(-2.0, 0), lone_pairs=True)
eb = s.molecule("C(C)Br", coords=[(0, 0), (-0.5, 1.2), (1.4, 0)], lone_pairs=[2])
s.curly(n.atom(0), eb.atom(0), bend=0.3)
s.curly(eb.bond(0, 2), eb.atom(2), bend=-0.8)
s.arrow((2.5, 0.3), (3.9, 0.3), below=r"$-$Br$^-$")
am = s.molecule("CC[NH3+]", at=(5.4, 0.3), show_h=[2])
nh3 = s.molecule("N", at=(7.6, -1.0), lone_pairs=True)
s.curly(nh3.atom(0), am.h(2, 1), bend=-0.4)
s.curly(am.bond(2, 4), am.atom(2), bend=0.8)
s.arrow((8.6, 0.3), (10.0, 0.3), below=r"$-$NH$_4^+$")
s.molecule("CCN", at=(11.6, 0.3), lone_pairs=True)
s.text((11.6, -0.8), "ethylamine", size=10)
s.draw()
