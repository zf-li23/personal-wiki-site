"""Replacement of a diazonium group by hydrogen with hypophosphorous acid: a radical chain. Top
(propagation 1): the aryl radical abstracts a hydrogen atom from the P-H bond of H3PO2 (one electron
of the P-H bond pairs with the radical, the other stays on phosphorus). Bottom (propagation 2): the
phosphorus radical transfers one electron to the next diazonium ion, which loses N2 and regenerates
the aryl radical."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ar = s.molecule("[c]1ccccc1", at=(0, y))
r = ar.xy(0)
hp = s.molecule("[H]P(=O)(O)*", coords=[(r[0] - 1.5, r[1]), (r[0] - 2.5, r[1]), (r[0] - 2.5, r[1] + 1.0), (r[0] - 3.4, r[1] - 0.5),
                                          (r[0] - 2.5, r[1] - 1.0)], labels={4: "H"})
mid = (r + hp.xy(0)) / 2
s.curly(ar.atom(0), mid, bend=0.5, single=True)
s.curly(hp.bond(0, 1), mid, bend=-0.5, single=True)
s.curly(hp.bond(0, 1), hp.atom(1), bend=0.6, single=True)
s.arrow((2.0, y), (3.4, y))
s.molecule("c1ccccc1", at=(4.8, y))
s.plus((6.2, y))
s.text((7.4, y), r"H$_2$PO$_2^{\bullet}$")

y = -3.2
s.text((-1.4, y), r"H$_2$PO$_2^{\bullet}$  +  ArN$_2^+$")
s.arrow((0.6, y), (2.4, y), above="electron transfer")
s.text((4.4, y), r"H$_2$PO$_2^+$  +  ArN$_2^{\bullet}$")
s.arrow((6.4, y), (7.8, y), above=r"$-$N$_2$")
s.text((8.6, y), r"Ar$^{\bullet}$")
s.draw()
