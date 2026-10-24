"""Robinson annulation of 2-methylcyclohexanone with methyl vinyl ketone. Top: the thermodynamic
(more substituted) enolate adds to the beta carbon of MVK (Michael addition); proton transfer
gives 2-methyl-2-(3-oxobutyl)cyclohexanone. Bottom: the enolate of the side-chain methyl ketone
attacks the ring carbonyl carbon (intramolecular aldol addition, six-membered ring forming, drawn
in its final ring shape), and E1cb dehydration of the aldol gives the conjugated bicyclic enone."""

import numpy as np

from wikichem import Scheme

s = Scheme()
y = 0.0
en = s.molecule("CC1=C([O-])CCCC1", at=(0, y), lone_pairs=[3])
mvk = s.molecule("C=CC(C)=O", at=(2.6, y - 1.0), lone_pairs=[4])
s.curly(en.atom(3), en.bond(2, 3), bend=0.7)
s.curly(en.bond(1, 2), mvk.atom(0), bend=-0.5)
s.curly(mvk.bond(0, 1), mvk.bond(1, 2), bend=0.8)
s.curly(mvk.bond(2, 4), mvk.atom(4), bend=0.8)
s.text((-0.8, y - 2.6), "thermodynamic enolate")
s.text((3.9, y - 2.8), "MVK")
s.arrow((4.4, y), (5.8, y), above="Michael", below=r"H$^+$ transfer")
s.molecule("CC1(CCC(C)=O)CCCCC1=O", at=(8.2, y))

y = -5.2
# fused-ring geometry for the ring-closing step: left ring is the cyclohexanone, right ring forms
L = [(0, 0.5), (-0.866, 1.0), (-1.732, 0.5), (-1.732, -0.5), (-0.866, -1.0), (0, -0.5)]
R = [(1.0, 1.05), (2.0, 0.55), (2.0, -0.6), (1.1, -1.25)]  # Ca, Cb, Cc(O-), Cd(=CH2)
# SMILES order: Cd, Cc, O-, Cb, Ca, Cq, CH3, four ring CH2, Ce, O
coords = [R[3], R[2], (2.9, -1.1), R[1], R[0], L[0], (0, 1.55), L[1], L[2], L[3], L[4], L[5], (-0.1, -1.6)]
ring = s.molecule("C=C([O-])CCC1(C)CCCCC1=O", coords=coords, at=(0, y), lone_pairs=[2, 12])
s.partial(ring.atom(0), ring.atom(11))
s.curly(ring.atom(2), ring.bond(1, 2), bend=-0.7)
s.curly(ring.bond(0, 1), ring.atom(11), bend=-0.5)
s.curly(ring.bond(11, 12), ring.atom(12), bend=-0.8)
s.text((0.2, y - 2.6), "side-chain enolate")
s.arrow((3.6, y), (5.0, y), above="aldol", below=r"H$^+$ transfer")
s.molecule("CC12CCCCC1(O)CC(=O)CC2", at=(7.2, y))
s.arrow((9.4, y), (10.8, y), above=r"HO$^-$, heat", below=r"$-$H$_2$O (E1cb)")
s.molecule("CC12CCCCC1=CC(=O)CC2", at=(13.0, y))
s.draw()
