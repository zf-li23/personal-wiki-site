"""Acid-catalysed glycoside formation (Fischer glycosidation), drawn on tetrahydropyran-2-ol, the
simplest model of a pyranose hemiacetal. Top: the anomeric OH is protonated and leaves as water,
pushed out by a lone pair of the ring oxygen; the planar oxocarbenium ion is the key intermediate
of glycoside formation and hydrolysis. Bottom: methanol adds to C1 from either face and loses a
proton, giving both anomers of the methyl glycoside. Every step is reversible, so the product
ratio is set by thermodynamics (the anomeric effect favours the axial, alpha anomer)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
h = s.molecule("[OH2+]C1CCCCO1", at=(0.0, y), lone_pairs=[6])
s.curly(h.atom(6), h.bond(1, 6), bend=-0.6)
s.curly(h.bond(0, 1), h.atom(0), bend=0.7)
s.text((0.0, y - 1.9), "protonated hemiacetal")
s.arrow((2.0, y), (3.6, y), above=r"$-$H$_2$O", below="slow", kind="equilibrium")
s.molecule("C1CC[CH]=[O+]C1", at=(5.4, y))
s.text((5.4, y - 1.9), "oxocarbenium ion")

y = -4.4
ox = s.molecule("C1CCC=[O+]C1", at=(0.6, y))
me = s.molecule("CO", at=(-1.8, y + 0.4), lone_pairs=True)
s.curly(me.atom(1), ox.atom(3), bend=-0.4)
s.curly(ox.bond(3, 4), ox.atom(4), bend=0.7)
s.arrow((2.6, y), (4.0, y), above=r"$-$H$^+$", kind="equilibrium")
s.molecule("CO[C@H]1CCCCO1", at=(5.8, y + 0.9))
s.molecule("CO[C@@H]1CCCCO1", at=(5.8, y - 1.5))
s.text((9.4, y + 0.9), "one face")
s.text((9.4, y - 1.5), "other face")
s.draw()
