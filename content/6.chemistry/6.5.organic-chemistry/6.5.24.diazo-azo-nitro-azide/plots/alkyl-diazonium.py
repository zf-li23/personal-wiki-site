"""Fate of an alkyldiazonium ion (from butan-1-amine and nitrous acid). N2, an excellent leaving
group, departs at once and leaves a highly reactive, poorly solvated carbocation. A 1,2-hydride shift
turns it into the more stable secondary cation, which water captures to give butan-2-ol; capture
before the shift gives butan-1-ol and loss of a proton gives butenes, so a mixture results."""

import numpy as np

from wikichem import Scheme


def nearest_h(mol, k, target):
    """The hydrogen drawn on atom k that lies closest to a target point."""
    best, d = None, 1e9
    for i in range(3):
        try:
            p = mol.h(k, i)
        except IndexError:
            break
        e = np.linalg.norm(p.xy - np.asarray(target, float))
        if e < d:
            best, d = p, e
    return best

s = Scheme()
dz = s.molecule("CCCC[N+]#N", at=(0, 0))
s.curly(dz.bond(3, 4), dz.atom(4), bend=0.6)
s.text((0, -1.4), "butyldiazonium")
s.arrow((2.4, 0), (3.8, 0), below=r"$-$N$_2$")
c1 = s.molecule("CCC[CH2+]", at=(5.4, 0), show_h=[2])
h = nearest_h(c1, 2, c1.xy(3) + (0, 1.0))
s.curly((c1.xy(2) + h.xy) / 2, c1.atom(3), bend=-0.6)
s.text((5.4, -1.4), "1,2-H shift")
s.arrow((7.0, 0), (8.4, 0))
s.molecule("CC[CH+]C", at=(9.6, 0))
s.arrow((10.8, 0), (12.2, 0), above=r"H$_2$O", below=r"$-$H$^+$")
s.molecule("CCC(O)C", at=(13.9, 0))
s.text((13.9, -1.4), "butan-2-ol")
s.draw()
