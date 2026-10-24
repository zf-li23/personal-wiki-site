"""Thiamine-type catalysis (Breslow). A base removes the acidic C2-H of a 3-methylthiazolium ion,
giving an N-heterocyclic carbene (drawn with its lone pair). The carbene carbon adds to the carbonyl
carbon of benzaldehyde; proton transfer from the former aldehyde carbon to oxygen gives the
Breslow intermediate, an enaminol whose exocyclic carbon is nucleophilic: an acyl anion equivalent."""

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
th = s.molecule("C[N+]1=CSC=C1", at=(0, y), show_h=[2])
b = s.molecule("CN(C)C", at=(2.6, y + 2.0), lone_pairs=[1])
h = nearest_h(th, 2, b.xy(1))
s.curly(b.atom(1), h, bend=0.4)
s.curly((th.xy(2) + h.xy) / 2, th.atom(2), bend=0.9)
s.text((0, y - 1.8), "thiazolium ion")
s.arrow((2.8, y), (4.4, y), kind="equilibrium")
cb = s.molecule("CN1[C]SC=C1", at=(6.2, y), singlet=[2], lone_pairs=[])
ald = s.molecule("O=Cc1ccccc1", at=(10.0, y - 0.8), rotate=180, lone_pairs=[0])
s.curly(cb.atom(2), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), ald.atom(0), bend=0.9)
s.text((6.2, y - 1.8), "carbene (NHC)")

y = -5.4
s.arrow((-2.4, y), (-1.0, y), kind="equilibrium")
s.molecule("C[N+]1=C(SC=C1)C([O-])c1ccccc1", at=(1.8, y))
s.arrow((4.8, y), (6.4, y), above=r"H$^+$ shift", kind="equilibrium")
s.molecule("CN1C=CSC1=C(O)c1ccccc1", at=(9.4, y))
s.text((9.4, y - 2.2), "Breslow intermediate")
s.draw()
