"""Base-catalysed cyanohydrin formation (Lapworth). Cyanide, not HCN, is the nucleophile: it adds
to the carbonyl carbon of acetone, and the alkoxide takes a proton from HCN, which regenerates
cyanide. Each step is reversible."""

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
cn = s.molecule("[C-]#N", at=(-1.8, 0.6), lone_pairs=[0])
ket = s.molecule("CC(=O)C", at=(0.5, 0), lone_pairs=[2])
s.curly(cn.atom(0), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 2), ket.atom(2), bend=-1.2)
s.arrow((2.0, 0), (3.4, 0), kind="equilibrium")
ad = s.molecule("CC(C)([O-])C#N", at=(5.0, 0), lone_pairs=[3])
hcn = s.molecule("N#C", at=(7.8, 1.0), show_h=[1])
h = nearest_h(hcn, 1, ad.xy(3))
s.curly(ad.atom(3), h, bend=-0.4)
s.curly((hcn.xy(1) + h.xy) / 2, hcn.atom(1), bend=-1.4)
s.arrow((8.6, 0), (10.0, 0), kind="equilibrium")
s.molecule("CC(C)(O)C#N", at=(11.6, 0))
s.plus((13.3, 0))
s.molecule("[C-]#N", at=(14.8, 0), lone_pairs=[0])
s.draw()
