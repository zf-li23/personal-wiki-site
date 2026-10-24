"""Hydration of a carbonyl group. Top: base catalysis: hydroxide adds to the carbonyl carbon (the
pi electrons move onto oxygen) and the alkoxide takes a proton from water, regenerating hydroxide.
Bottom: acid catalysis: protonation of the carbonyl oxygen gives an oxocarbenium ion, a much better
electrophile that even neutral water attacks; loss of a proton gives the same gem-diol."""

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
y = 0.0
oh = s.molecule("[OH-]", at=(-1.5, y + 1.0), lone_pairs=True)
ket = s.molecule("CC(=O)C", at=(0.6, y), lone_pairs=[2])
s.curly(oh.atom(0), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 2), ket.atom(2), bend=-1.2)
s.arrow((2.2, y), (3.6, y), kind="equilibrium")
ad = s.molecule("CC([O-])(C)O", at=(5.0, y), lone_pairs=[2])
w = s.molecule("O", at=(7.6, y + 1.3), lone_pairs=True, show_h=[0])
h = nearest_h(w, 0, ad.xy(2))
s.curly(ad.atom(2), h, bend=-0.4)
s.curly((w.xy(0) + h.xy) / 2, w.atom(0), bend=-1.4)
s.arrow((8.4, y), (9.8, y), kind="equilibrium")
s.molecule("CC(O)(C)O", at=(11.2, y))
s.text((12.9, y), r"+ HO$^-$")

y = -4.2
ket2 = s.molecule("CC(=O)C", at=(-0.8, y), lone_pairs=[2])
h3o = s.molecule("[OH3+]", at=(1.6, y + 1.2), show_h=[0])
h2 = nearest_h(h3o, 0, ket2.xy(2))
s.curly(ket2.atom(2), h2, bend=-0.4)
s.curly((h3o.xy(0) + h2.xy) / 2, h3o.atom(0), bend=-1.4)
s.arrow((2.6, y), (4.0, y), kind="equilibrium")
ox = s.molecule("CC(=[OH+])C", at=(5.4, y))
w2 = s.molecule("O", at=(5.4, y - 2.0), lone_pairs=True)
s.curly(w2.atom(0), ox.atom(1), bend=0.3)
s.curly(ox.bond(1, 2), ox.atom(2), bend=-1.2)
s.arrow((7.0, y), (8.4, y), kind="equilibrium")
s.molecule("CC(O)(C)[OH2+]", at=(9.8, y))
s.arrow((11.2, y), (12.6, y), above=r"$-$H$^+$", kind="equilibrium")
s.molecule("CC(O)(C)O", at=(13.8, y))
s.draw()
