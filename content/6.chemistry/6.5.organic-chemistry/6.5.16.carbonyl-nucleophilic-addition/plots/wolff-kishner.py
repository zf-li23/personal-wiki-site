"""Mechanism of the Wolff-Kishner reduction (acetone hydrazone, hydroxide, ethylene glycol, about
200 C). Top: hydroxide removes an N-H proton; the anion, delocalised onto carbon, takes a proton
from the solvent at carbon (the slow step), giving a diazene. Bottom: removal of the second N-H
proton gives a diazenide anion, which loses nitrogen gas; the carbanion left behind is protonated
by the solvent. The loss of N2 makes the reaction irreversible."""

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
hz = s.molecule("CC(C)=NN", at=(0, y), show_h=[4])
oh = s.molecule("[OH-]", at=(2.4, y + 1.6), lone_pairs=True)
h = nearest_h(hz, 4, oh.xy(0))
s.curly(oh.atom(0), h, bend=0.4)
s.curly((hz.xy(4) + h.xy) / 2, hz.atom(4), bend=0.9)
s.arrow((2.6, y), (4.0, y), kind="equilibrium")
an = s.molecule("CC(C)=N[NH-]", at=(5.8, y), lone_pairs=[4])
w = s.molecule("O", at=(5.6, y - 2.4), lone_pairs=True, show_h=[0])
hw = nearest_h(w, 0, an.xy(1))
s.curly(an.atom(4), an.bond(3, 4), bend=-0.8)
s.curly(an.bond(1, 3), hw, bend=0.5)
s.curly((w.xy(0) + hw.xy) / 2, w.atom(0), bend=0.9)
s.arrow((7.8, y), (9.4, y), below="slow")
s.molecule("CC(C)N=N", at=(11.0, y))
s.text((11.0, y - 1.5), "diazene")

y = -4.8
dz = s.molecule("CC(C)N=N", at=(0, y), show_h=[4])
oh2 = s.molecule("[OH-]", at=(2.4, y + 1.6), lone_pairs=True)
h2 = nearest_h(dz, 4, oh2.xy(0))
s.curly(oh2.atom(0), h2, bend=0.4)
s.curly((dz.xy(4) + h2.xy) / 2, dz.atom(4), bend=0.9)
s.arrow((2.6, y), (4.0, y), kind="equilibrium")
dn = s.molecule("CC(C)N=[N-]", at=(5.8, y), lone_pairs=[4])
s.curly(dn.atom(4), dn.bond(3, 4), bend=0.8)
s.curly(dn.bond(1, 3), dn.atom(1), bend=0.8)
s.arrow((7.6, y), (9.0, y), above=r"$-$N$_2$")
s.molecule("C[CH-]C", at=(10.2, y), lone_pairs=[1])
s.arrow((11.4, y), (12.8, y), above=r"H$_2$O")
s.molecule("CCC", at=(14.0, y))
s.draw()
