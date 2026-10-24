"""Reduction of an alkyl halide by a metal hydride (SN2). A deuteride of AlD4- attacks the carbon of
(R)-2-bromobutane from the back side as bromide leaves, giving 2-deuteriobutane with inversion of
configuration; the hydride (deuteride) ion is the nucleophile."""

from wikichem import Scheme

s = Scheme()
sub = s.molecule("C[C@@H](Br)CC", coords=[(-0.87, -0.5), (0, 0), (0, 1), (0.87, -0.5), (1.73, 0)], at=(0, 0), lone_pairs=[2])
al = s.molecule("[2H][Al-]([2H])([2H])[2H]", at=(0, -2.5))
s.curly(al.bond(0, 1), sub.atom(1), bend=0.4)
s.curly(sub.bond(1, 2), sub.atom(2), bend=-0.8)
s.text((0.4, 1.9), "(R)-2-bromobutane")
s.arrow((2.6, -0.4), (4.0, -0.4), above=r"S$_{\mathrm{N}}$2")
s.molecule("C[C@H]([2H])CC", coords=[(-0.87, 0.5), (0, 0), (0, -1), (0.87, 0.5), (1.73, 0)], at=(5.4, -0.4))
s.text((5.8, -2.2), "inversion")
s.text((8.6, -0.4), r"+  Br$^-$  +  AlD$_3$")
s.draw()
