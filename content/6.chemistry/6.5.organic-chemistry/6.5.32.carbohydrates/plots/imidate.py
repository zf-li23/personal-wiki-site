"""Schmidt trichloroacetimidate glycosylation, on a tetrahydropyranyl model of the glycosyl donor.
Top: with a base (DBU or K2CO3) the anomeric alkoxide adds to the nitrile carbon of
trichloroacetonitrile, and protonation of nitrogen gives the O-glycosyl trichloroacetimidate.
Bottom: a catalytic Lewis or Bronsted acid (TMSOTf, drawn as H+) activates the imidate nitrogen;
the ring oxygen lone pair expels trichloroacetamide (a weak base, because the C=N becomes a
C=O after tautomerization) and the oxocarbenium ion is captured by the acceptor alcohol."""

from wikichem import Scheme

s = Scheme()
y = 0.0
al = s.molecule("[O-]C1CCCCO1", at=(0.0, y), lone_pairs=[0])
nit = s.molecule("ClC(Cl)(Cl)C#N", at=(2.6, y + 1.4))
s.curly(al.atom(0), nit.atom(4), bend=-0.4)
s.curly(nit.bond(4, 5), nit.atom(5), bend=-0.6)
s.text((1.2, y - 2.0), r"anomeric alkoxide + Cl$_3$CCN")
s.arrow((4.4, y), (5.8, y), above=r"then H$^+$")
s.molecule("ClC(Cl)(Cl)C(=N)OC1CCCCO1", at=(8.6, y))
s.text((8.6, y - 2.0), "glycosyl trichloroacetimidate")
y2 = -5.0
im = s.molecule("ClC(Cl)(Cl)C(=[NH2+])OC1CCCCO1", at=(0.0, y2), lone_pairs=[12])
s.curly(im.atom(12), im.bond(7, 12), bend=0.6)
s.curly(im.bond(6, 7), im.atom(6), bend=-0.6)
s.text((0.0, y2 - 2.0), "activated imidate")
s.arrow((3.2, y2), (4.6, y2))
oc = s.molecule("C1CC[O+]=CC1", at=(6.0, y2))
s.plus((7.3, y2))
s.molecule("NC(=O)C(Cl)(Cl)Cl", at=(9.9, y2))
s.text((8.0, y2 - 2.0), "oxocarbenium ion + trichloroacetamide")
s.arrow((11.6, y2), (13.0, y2), above="ROH", below=r"$-$H$^+$")
s.molecule("*OC1CCCCO1", at=(14.6, y2), labels={0: "R"})
s.text((14.6, y2 - 2.0), "glycoside")
s.draw()
