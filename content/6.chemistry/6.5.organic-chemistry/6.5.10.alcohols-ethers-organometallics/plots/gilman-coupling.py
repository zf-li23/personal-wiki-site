"""Corey-House coupling of lithium dimethylcuprate with 1-bromobutane. The electron-rich copper(I)
centre attacks the carbon from the back side (an SN2-like oxidative addition), bromide leaves and a
copper(III) intermediate with three alkyl groups forms; reductive elimination joins the methyl
and butyl groups, giving pentane and methylcopper."""

from wikichem import Scheme

s = Scheme()
cu = s.molecule("C[Cu-]C", at=(-0.6, -0.2))
s.text((-0.6, -1.2), r"Li$^+$", size=11)
bb = s.molecule("CCCCBr", coords=[(-0.5, 2.6), (0, 1.73), (-0.5, 0.87), (0, 0), (1.0, 0)], at=(2.2, -0.2), lone_pairs=[4])
s.curly(cu.atom(1), bb.atom(3), bend=-0.4)
s.curly(bb.bond(3, 4), bb.atom(4), bend=0.8)
s.arrow((4.2, 0), (6.2, 0), above="oxidative", below="addition")
s.molecule("C[Cu](C)CCCC", coords=[(-1, 0), (0, 0), (0, 1), (1, 0), (1.87, 0.5), (2.73, 0), (3.6, 0.5)], at=(7.6, -0.2))
s.text((8.6, -1.4), "Cu(III)")
s.arrow((11.8, 0), (13.8, 0), above="reductive", below="elimination")
s.molecule("CCCCC", at=(15.4, 0))
s.text((19.0, 0), r"+  CH$_3$Cu  +  LiBr")
s.draw()
