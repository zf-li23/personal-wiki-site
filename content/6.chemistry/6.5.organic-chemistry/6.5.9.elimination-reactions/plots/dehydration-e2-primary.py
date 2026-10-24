"""Dehydration of ethanol in hot concentrated sulfuric acid. A primary carbocation is too unstable to
be an intermediate, so after protonation of the hydroxy group the hydrogensulfate ion (or another
alcohol molecule) removes a beta hydrogen while water leaves: an E2 elimination from the
protonated alcohol."""

from wikichem import Scheme

s = Scheme()
ox = s.molecule("C([H])C[OH2+]", coords=[(0, 0), (0, 1), (0.87, -0.5), (1.73, 0)], at=(0, 0))
b = s.molecule("OS(=O)(=O)[O-]", at=(-1.8, 2.2), lone_pairs=[4])
s.curly(b.atom(4), ox.atom(1), bend=-0.4)
s.curly(ox.bond(0, 1), ox.bond(0, 2), bend=0.8)
s.curly(ox.bond(2, 3), ox.atom(3), bend=0.8)
s.arrow((3.0, 0), (4.4, 0), above=r"170 $^\circ$C")
s.molecule("C=C", at=(5.4, 0))
s.text((7.9, 0), r"+  H$_2$SO$_4$  +  H$_2$O")
s.draw()
