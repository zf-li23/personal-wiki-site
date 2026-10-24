"""Photoenolization of 2-methylbenzophenone and Diels-Alder trapping. The n,pi* triplet abstracts a
hydrogen from the ortho methyl group (1,5-hydrogen atom transfer) to give a 1,4-biradical, which
relaxes to the hydroxy-o-quinodimethane (photoenol). The Z photoenol returns to the ketone within
about 100 ns; the long-lived E photoenol is a reactive s-cis diene and is captured by maleic
anhydride (Diels-Alder reaction, curved arrows) to give a 1-hydroxy-1-phenyltetralin anhydride."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("Cc1ccccc1C(=O)c1ccccc1", at=(0.0, y))
s.text((0.0, y - 3.2), "2-methylbenzophenone")
s.arrow((2.6, y), (4.2, y), above=r"$h\nu$", below="1,5-HAT")
s.molecule("[CH2]c1ccccc1[C](O)c1ccccc1", at=(6.8, y))
s.text((6.8, y - 3.2), "1,4-biradical")
s.arrow((9.4, y), (10.8, y))
e = s.molecule("C=C1C=CC=CC1=C(O)c1ccccc1", at=(13.4, y), rotate=0)
s.text((13.4, y - 3.2), "(E)-photoenol (o-quinodimethane)")

y2 = -7.0
d = s.molecule("C=C1C=CC=CC1=C(O)*", at=(0.0, y2), labels={9: "Ph"}, flip=True)
ma = s.molecule("O=C1C=CC(=O)O1", at=(3.6, y2 + 0.3), rotate=-90)
s.curly(ma.bond(2, 3), d.atom(0), bend=0.4)
s.curly(d.bond(0, 1), d.bond(1, 6), bend=0.6)
s.curly(d.bond(6, 7), ma.atom(2), bend=0.4)
s.text((1.6, y2 - 2.8), "Diels-Alder with maleic anhydride")
s.arrow((5.6, y2), (7.0, y2))
s.molecule("O=C1OC(=O)C2C1Cc1ccccc1C2(O)c1ccccc1", at=(9.8, y2))
s.text((9.8, y2 - 3.0), "cycloadduct")
s.draw()
