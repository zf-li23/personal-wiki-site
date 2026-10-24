"""Criegee mechanism of ozonolysis. (1) 1,3-dipolar cycloaddition of ozone gives the primary ozonide
(a 1,2,3-trioxolane); (2) it falls apart by a retro-[3+2] step into a carbonyl compound and a
carbonyl oxide (Criegee intermediate); (3) these recombine by a second [3+2] cycloaddition with the
opposite orientation to the secondary ozonide (a 1,2,4-trioxolane), which Me2S or Zn reduces to two
carbonyl compounds."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


# a regular pentagon (ring atoms) with its base vertical on the left: C, C, O, O, O
pent = [(0.0, 0.5), (0.0, -0.5), (0.95, -0.81), (1.54, 0.0), (0.95, 0.81)]

s = Scheme(scale=0.4)
# step 1: ozone adds across the C=C of 2-methyl-2-butene
alkene = fixed(s, "CC(C)=CC", [(-0.8, 1.0), (0.0, 0.5), (0.8, 1.0), (0.0, -0.5), (-0.8, -1.0)])
ozone = fixed(s, "[O-][O+]=O", [(1.6, -1.0), (2.3, 0.0), (1.6, 1.0)], lone_pairs=(0, 2))
s.curly(alkene.bond(1, 3), ozone.atom(2), bend=-0.3)
s.curly(ozone.bond(1, 2), ozone.atom(1), bend=-0.6)
s.curly(ozone.atom(0), alkene.atom(3), bend=-0.3)
s.arrow((2.9, 0), (4.1, 0))

# step 2: the primary ozonide cleaves (retro-[3+2])
x = 5.0
po = fixed(s, "CC1(C)C(C)OOO1", [(x - 0.8, 1.0), (x + pent[0][0], pent[0][1]), (x - 0.8, 0.2), (x + pent[1][0], pent[1][1]),
                                   (x - 0.8, -1.0), (x + pent[2][0], pent[2][1]), (x + pent[3][0], pent[3][1]), (x + pent[4][0], pent[4][1])],
           lone_pairs=(7,))
s.curly(po.atom(7), po.bond(1, 7), bend=0.6)
s.curly(po.bond(1, 3), po.bond(3, 5), bend=0.6)
s.curly(po.bond(5, 6), po.atom(6), bend=0.5)
s.text((x + 0.5, -1.9), "primary ozonide")
s.arrow((x + 2.1, 0), (x + 3.3, 0))

# step 3: carbonyl oxide + carbonyl recombine; secondary ozonide; reduction
x = 10.3
s.molecule("CC(C)=[O+][O-]", at=(x, 0.9))
s.molecule("CC=O", at=(x, -1.0))
s.text((x, -2.4), "carbonyl oxide")
s.text((x, -3.0), "+ aldehyde")
s.arrow((x + 1.6, 0), (x + 2.8, 0), above="[3+2]")
s.molecule("CC1(C)OOC(C)O1", at=(x + 4.2, 0))
s.text((x + 4.2, -1.6), "secondary ozonide")
s.arrow((x + 5.6, 0), (x + 6.8, 0), above=r"Me$_2$S")
s.molecule("CC(C)=O", at=(x + 7.8, 0.8))
s.molecule("CC=O", at=(x + 7.8, -0.9))
s.draw()
