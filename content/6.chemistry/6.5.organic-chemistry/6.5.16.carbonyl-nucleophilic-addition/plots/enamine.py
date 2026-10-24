"""Enamine formation: the iminium ion from cyclohexanone and pyrrolidine has no N-H proton to lose,
so a base (another molecule of the amine) removes a proton from the alpha carbon; the C-H electrons
form the C=C bond and the C=N pi electrons move onto nitrogen, giving the neutral enamine."""

import numpy as np

from wikichem import Scheme


def nearest_h(mol, k, target):
    """The hydrogen drawn on atom k that lies closest to a target point."""
    best, d = None, 1e9
    for i in range(4):
        try:
            p = mol.h(k, i)
        except IndexError:
            break
        e = np.linalg.norm(p.xy - np.asarray(target, float))
        if e < d:
            best, d = p, e
    return best


s = Scheme()
im = s.molecule("[N+]1(CCCC1)=C1CCCCC1", at=(0, 0), show_h=[6])
base = s.molecule("C1CCNC1", at=(3.2, 2.6), lone_pairs=[3])
h = nearest_h(im, 6, base.xy(3))
s.curly(base.atom(3), h, bend=0.4)
s.curly((im.xy(6) + h.xy) / 2, im.bond(5, 6), bend=0.8)
s.curly(im.bond(0, 5), im.atom(0), bend=-0.8)
s.text((0, -2.2), "iminium ion")
s.arrow((4.6, 0), (6.0, 0), kind="equilibrium")
s.molecule("N1(CCCC1)C1=CCCCC1", at=(8.4, 0))
s.text((8.4, -2.2), "enamine")
s.draw()
