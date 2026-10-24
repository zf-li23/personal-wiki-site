"""Acid-catalysed tautomerization of the enol formed by hydration of propyne. The C=C pi bond is
protonated at the CH2 end while the oxygen lone pair forms the C=O pi bond (giving the oxocarbenium ion, stabilised by the oxygen lone pair), then
the O-H proton is removed: the enol becomes the more stable ketone, acetone."""

from wikichem import Scheme

s = Scheme()
enol = s.molecule("C=C(C)O", at=(0, 0), lone_pairs=[3])
h3o = s.molecule("[OH3+]", at=(-2.3, -0.6), explicit_h=True)
s.curly(enol.bond(0, 1), h3o.atom(1), bend=0.5)
s.curly(h3o.bond(0, 1), h3o.atom(0), bend=0.6)
s.curly(enol.atom(3), enol.bond(1, 3), bend=0.8)
s.text((-0.7, -1.7), "enol")
s.arrow((1.5, 0), (3.0, 0))
ion = s.molecule("CC(C)=[OH+]", at=(4.6, 0))
s.text((4.6, -1.7), "oxocarbenium ion")
s.arrow((7.6, 0), (9.1, 0), above=r"$-\mathrm{H}^+$", below=r"(to H$_2$O)")
s.molecule("CC(C)=O", at=(10.5, 0))
s.text((10.5, -1.7), "ketone")
s.draw()
