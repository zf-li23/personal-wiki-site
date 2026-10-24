"""Reduction of acetone by sodium borohydride in methanol. The B-H bond pair is delivered to the
carbonyl carbon (hydride transfer), the C=O pi pair moves onto oxygen, and the oxygen takes a proton from the solvent; the
products are propan-2-ol and a methoxyborohydride, which can deliver its remaining three hydrides."""

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
bh = s.molecule("[H][B-]([H])([H])[H]", coords=[(0.0, 1.0), (0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (1.0, 0.0)], at=(-1.6, 0.6))
ket = s.molecule("CC(=O)C", at=(0.6, -0.4), lone_pairs=[2], rotate=180)
me = s.molecule("CO", at=(3.0, 1.4), lone_pairs=[1], show_h=[1])
h = nearest_h(me, 1, ket.xy(2))
s.curly(bh.bond(1, 4), ket.atom(1), bend=-0.5)
s.curly(ket.bond(1, 2), ket.atom(2), bend=0.8)
s.curly(ket.atom(2), h, bend=-0.4)
s.curly((me.xy(1) + h.xy) / 2, me.atom(1), bend=-1.2)
s.arrow((4.2, 0), (5.6, 0))
s.molecule("CC(C)O", at=(6.8, 0))
s.plus((8.2, 0))
s.molecule("CO[BH3-]", at=(9.4, 0))
s.draw()
