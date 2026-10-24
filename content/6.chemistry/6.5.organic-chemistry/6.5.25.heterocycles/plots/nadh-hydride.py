"""Hydride transfer from NADH, modelled by 1-methyl-1,4-dihydronicotinamide, to acetaldehyde (as in
alcohol dehydrogenase, where a zinc ion and an acid activate the carbonyl). The nitrogen lone pair
pushes through the ring: one C4-H bond's electrons go with the hydrogen to the carbonyl carbon and
the C=O electrons move onto oxygen, which is protonated. The ring becomes the aromatic pyridinium ion
NAD+, and this aromatisation drives the transfer."""

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
n = s.molecule("CN1C=CCC(=C1)C(N)=O", at=(0, 0), show_h=[4], lone_pairs=[1])
h = nearest_h(n, 4, n.xy(4) + (0.6, -3.0))
al = s.molecule("CC=O", at=(h.xy[0] + 0.6, h.xy[1] - 1.5), lone_pairs=[2])
s.curly(n.atom(1), n.bond(1, 2), bend=0.6)
s.curly(n.bond(2, 3), n.bond(3, 4), bend=0.6)
s.curly((n.xy(4) + h.xy) / 2, al.atom(1), bend=0.5)
s.curly(al.bond(1, 2), al.atom(2), bend=0.6)
s.text((al.xy(2)[0] - 1.1, al.xy(2)[1] - 0.2), r"H$^+$")
s.text((-2.4, 1.6), "NADH model")
s.arrow((3.0, 0), (4.4, 0))
s.molecule("C[n+]1cccc(c1)C(N)=O", at=(6.4, 0))
s.text((6.4, -2.4), r"NAD$^+$ model")
s.plus((8.6, 0))
s.molecule("CCO", at=(10.0, 0))
s.draw()
