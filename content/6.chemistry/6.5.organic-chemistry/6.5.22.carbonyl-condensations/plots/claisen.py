"""Claisen condensation of ethyl acetate. The ester enolate attacks the carbonyl carbon of a second
ester molecule, giving a tetrahedral intermediate; the alkoxide lone pair pushes back to re-form
C=O and ethoxide leaves, giving ethyl acetoacetate. Ethoxide then removes a proton from the CH2
between the two carbonyl groups (pKa 10.7, against 15.9 for ethanol); this irreversible
deprotonation drives the whole sequence. Acid work-up returns the neutral beta-keto ester."""

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
en = s.molecule("C=C([O-])OCC", at=(0, y + 1.0), rotate=180, lone_pairs=[2])
es = s.molecule("CC(=O)OCC", at=(0.6, y - 1.6), lone_pairs=[2])
s.curly(en.atom(2), en.bond(1, 2), bend=0.7)
s.curly(en.bond(0, 1), es.atom(1), bend=-0.6)
s.curly(es.bond(1, 2), es.atom(2), bend=0.7)
s.text((-1.6, y + 2.4), "ester enolate")
s.arrow((2.6, y), (4.0, y), kind="equilibrium")
t = s.molecule("CCOC(=O)CC(C)([O-])OCC", at=(6.4, y), lone_pairs=[8])
s.curly(t.atom(8), t.bond(6, 8), bend=0.8)
s.curly(t.bond(6, 9), t.atom(9), bend=-0.8)
s.text((6.4, y - 2.2), "tetrahedral intermediate")

y = -5.0
s.arrow((-2.6, y), (-1.2, y), kind="equilibrium", above=r"$-$EtO$^-$")
k = s.molecule("CCOC(=O)CC(C)=O", at=(1.2, y), show_h=[5])
eto = s.molecule("CC[O-]", at=(1.6, y - 2.4), lone_pairs=[2])
h = nearest_h(k, 5, eto.xy(2))
s.curly(eto.atom(2), h, bend=0.4)
s.curly((k.xy(5) + h.xy) / 2, k.bond(5, 6), bend=0.8)
s.curly(k.bond(6, 8), k.atom(8), bend=0.8)
s.text((1.2, y + 1.9), "ethyl acetoacetate")
s.arrow((3.6, y), (5.0, y), below=r"$-$EtOH")
s.molecule("CCOC(=O)[CH-]C(C)=O", at=(7.0, y))
s.text((7.0, y - 1.6), "stabilized enolate")
s.arrow((9.0, y), (10.4, y), above=r"H$_3$O$^+$")
s.molecule("CCOC(=O)CC(C)=O", at=(12.4, y))
s.draw()
