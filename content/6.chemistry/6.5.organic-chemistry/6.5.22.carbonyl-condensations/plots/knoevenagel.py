"""Knoevenagel condensation by iminium catalysis. Top: piperidine and benzaldehyde form an iminium
ion, a stronger electrophile than the aldehyde; the malonate carbanion attacks the iminium carbon and
the C=N electrons move onto nitrogen. Bottom: piperidine removes the remaining acidic proton between
the two ester groups and the resulting carbanion expels piperidine (E1cB), giving diethyl
benzylidenemalonate and regenerating the amine catalyst."""

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
y = 0.0
im = s.molecule("C(=[N+]1CCCCC1)c1ccccc1", at=(0, y), rotate=180)
mal = s.molecule("CCOC(=O)[CH-]C(=O)OCC", at=(-4.1, y + 1.7), lone_pairs=[5])
s.curly(mal.atom(5), im.atom(0), bend=-0.4)
s.curly(im.bond(0, 1), im.atom(1), bend=0.6)
s.text((-3.4, y - 1.0), "iminium ion")
s.arrow((2.4, y), (3.8, y))
s.molecule("CCOC(=O)C(C(N1CCCCC1)c1ccccc1)C(=O)OCC", at=(6.8, y))

y = -7.4
ad = s.molecule("CCOC(=O)C(C(N1CCCCC1)c1ccccc1)C(=O)OCC", at=(0, y), show_h=[5], lone_pairs=[7])
pip = s.molecule("C1CCNCC1", at=(-3.6, y + 0.4), lone_pairs=[3])
h = nearest_h(ad, 5, pip.xy(3))
s.curly(pip.atom(3), h, bend=0.4)
s.curly((ad.xy(5) + h.xy) / 2, ad.bond(5, 6), bend=0.6)
s.curly(ad.bond(6, 7), ad.atom(7), bend=0.6)
s.arrow((3.0, y), (4.4, y), below=r"$-$piperidine")
s.molecule("CCOC(=O)C(=Cc1ccccc1)C(=O)OCC", at=(6.8, y))
s.text((6.8, y - 3.2), "diethyl benzylidenemalonate")
s.draw()
