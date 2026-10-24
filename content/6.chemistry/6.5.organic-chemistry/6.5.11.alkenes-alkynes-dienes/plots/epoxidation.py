"""Epoxidation of an alkene by a peroxy acid (the Bartlett "butterfly" mechanism). In one concerted
step the pi bond attacks the outer (electrophilic) oxygen, the weak O-O bond breaks, the O-H proton
moves to the carbonyl oxygen, and the outer oxygen forms the second C-O bond. Both C-O bonds form
on the same face, so the geometry of the alkene is kept (cis alkene gives cis epoxide)."""

import numpy as np
from wikichem import Scheme


def fixed(s, smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, at=at, coords=coords, lone_pairs=list(lone_pairs))


s = Scheme()
# cis-2-butene, C=C vertical on the left
alkene = fixed(s, "C/C=C\\C", [(-3.1, 1.6), (-2.4, 0.9), (-2.4, -0.3), (-3.1, -1.0)])
# peroxy acid in its internally hydrogen-bonded conformation: O(outer)-O(inner)-C(=O)R with H on O(outer)
acid = fixed(s, "[H]OOC(=O)C", [(-0.35, -0.55), (0.0, 0.3), (1.1, 0.75), (1.95, 0.1), (1.6, -0.85), (3.05, 0.4)],
             lone_pairs=(1, 4))
s.curly(alkene.bond(1, 2), acid.atom(1), bend=-0.3)
s.curly(acid.bond(1, 2), acid.bond(2, 3), bend=-0.6)
s.curly(acid.bond(3, 4), acid.atom(0), bend=-0.5)
s.curly(acid.bond(0, 1), alkene.atom(2), bend=-0.4)
s.arrow((3.6, 0.3), (5.0, 0.3), above="concerted")
s.molecule("C[C@H]1O[C@H]1C", at=(6.4, 0.3), lone_pairs=False)
s.text((6.4, -1.9), "cis epoxide")
s.text((8.4, 0.3), "+")
s.molecule("OC(=O)C", at=(9.6, 0.3))
s.draw()
