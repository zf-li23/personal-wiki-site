"""Cannizzaro reaction of benzaldehyde. Top: hydroxide adds to the carbonyl group, giving a
tetrahedral alkoxide. Bottom: the alkoxide re-forms its C=O bond and pushes the C-H bond pair, as a
hydride, onto the carbonyl carbon of a second benzaldehyde (the slow step); the benzoic acid and the
benzyl alkoxide formed then exchange a proton, giving benzoate and benzyl alcohol."""

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


s = Scheme(scale=0.38)
y = 0.0
oh = s.molecule("[OH-]", at=(-2.6, y + 1.2), lone_pairs=True)
ald = s.molecule("O=Cc1ccccc1", at=(0.0, y), lone_pairs=[0])
s.curly(oh.atom(0), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), ald.atom(0), bend=-0.9)
s.arrow((2.2, y), (3.6, y), kind="equilibrium")
s.molecule("[O-]C(O)c1ccccc1", at=(5.8, y))

y = -6.0
t = s.molecule("[O-]C(O)c1ccccc1", at=(0.0, y), lone_pairs=[0], show_h=[1])
ald2 = s.molecule("O=Cc1ccccc1", at=(3.6, y - 0.4), lone_pairs=[0], rotate=180)
h = nearest_h(t, 1, ald2.xy(1))
s.curly(t.atom(0), t.bond(0, 1), bend=-0.8)
s.curly((t.xy(1) + h.xy) / 2, ald2.atom(1), bend=-0.4)
s.curly(ald2.bond(0, 1), ald2.atom(0), bend=0.9)
s.arrow((6.6, y), (8.0, y), below="slow")
s.molecule("OC(=O)c1ccccc1", at=(10.2, y))
s.plus((12.2, y))
s.molecule("[O-]Cc1ccccc1", at=(14.4, y))

y = -11.0
s.arrow((5.0, y), (6.6, y), above=r"H$^+$ transfer")
s.molecule("[O-]C(=O)c1ccccc1", at=(8.8, y))
s.plus((10.8, y))
s.molecule("OCc1ccccc1", at=(13.0, y))
s.draw()
