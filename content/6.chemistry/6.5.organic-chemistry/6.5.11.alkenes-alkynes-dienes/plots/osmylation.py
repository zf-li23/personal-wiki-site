"""Syn dihydroxylation with OsO4: a concerted [3+2] cycloaddition of two Os=O oxygens across the
C=C bond gives a cyclic osmate(VI) ester on one face; hydrolysis releases the cis-1,2-diol. With
catalytic OsO4 the co-oxidant NMO reoxidises Os(VI) to Os(VIII)."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


ang = np.radians([150, 210, 270, 330, 30, 90])
hexagon = [(np.cos(t) - 1.0, np.sin(t)) for t in ang]

s = Scheme()
alkene = fixed(s, "C1=CCCCC1", [hexagon[4], hexagon[3], hexagon[2], hexagon[1], hexagon[0], hexagon[5]])
os4 = fixed(s, "O=[Os](=O)(=O)=O", [(1.6, 0.6), (2.5, 0.0), (1.6, -0.6), (3.1, 0.8), (3.1, -0.8)], lone_pairs=(0, 2))
s.curly(alkene.bond(0, 1), os4.atom(2), bend=0.5)
s.curly(os4.bond(1, 2), os4.atom(1), bend=-0.5)
s.curly(os4.atom(0), alkene.atom(0), bend=0.4)
s.arrow((3.8, 0), (5.2, 0), above="[3+2]")
s.molecule("O=[Os]1(=O)OC2CCCCC2O1", at=(7.4, 0))
s.text((7.4, -1.8), "osmate ester")
s.arrow((9.6, 0), (11.0, 0), above=r"H$_2$O", below="NMO")
s.molecule("O[C@@H]1CCCC[C@@H]1O", at=(12.6, 0))
s.text((12.6, -1.8), "cis-diol")
s.draw()
