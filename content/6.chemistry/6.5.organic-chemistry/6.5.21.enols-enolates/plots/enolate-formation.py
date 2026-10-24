"""Deprotonation of acetone at the alpha carbon. Ethoxide takes the alpha proton whose C-H bond
lies parallel to the carbonyl pi system; the C-H electrons become the C=C pi bond and the C=O pi
electrons move onto oxygen. The enolate is drawn as its two resonance structures: the carbanion
form and the oxyanion form, which carries most of the negative charge."""

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
ket = s.molecule("CC(=O)C", at=(0, 0), show_h=[0], lone_pairs=[2])
base = s.molecule("CC[O-]", at=(-2.6, -1.8), lone_pairs=[2])
h = nearest_h(ket, 0, base.xy(2))
s.curly(base.atom(2), h, bend=-0.4)
s.curly((ket.xy(0) + h.xy) / 2, ket.bond(0, 1), bend=-0.7)
s.curly(ket.bond(1, 2), ket.atom(2), bend=-0.7)
s.text((-0.6, -2.9), "acetone + ethoxide")
s.arrow((1.8, 0), (3.2, 0), kind="equilibrium", below=r"$-$EtOH")
a = s.molecule("[CH2-:1][C:2](=[O:3])[CH3:4]", at=(4.8, 0), lone_pairs=[3])
s.curly(a.atom(1), a.bond(1, 2), bend=0.6)
s.curly(a.bond(2, 3), a.atom(3), bend=0.6)
s.arrow((6.2, 0), (7.6, 0), kind="resonance")
s.molecule("[CH2:1]=[C:2]([O-:3])[CH3:4]", at=(9.0, 0), like=a, lone_pairs=[3])
s.text((6.9, -2.0), "enolate: carbanion form and oxyanion form")
s.draw()
