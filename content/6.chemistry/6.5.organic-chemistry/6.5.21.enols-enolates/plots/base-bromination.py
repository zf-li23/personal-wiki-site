"""Bromination of acetone under basic conditions. Top: the enolate oxygen lone pair pushes the C=C
electrons onto one bromine of Br2, and bromide leaves, giving bromoacetone. Bottom: the bromine
withdraws electrons, so the remaining protons on the CH2Br carbon are more acidic than those of
acetone; hydroxide removes one faster than the first, and the sequence runs on to the CBr3 ketone."""

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
e = s.molecule("C=C([O-])C", at=(0, y), lone_pairs=[2])
br = s.molecule("BrBr", at=(0.2, y + 2.0), lone_pairs=True)
s.curly(e.atom(2), e.bond(1, 2), bend=0.6)
s.curly(e.bond(0, 1), br.atom(0), bend=0.5)
s.curly(br.bond(0, 1), br.atom(1), bend=-0.6)
s.arrow((2.0, y), (3.4, y))
s.molecule("BrCC(C)=O", at=(5.0, y))
s.plus((6.4, y))
s.molecule("[Br-]", at=(7.2, y), lone_pairs=True)

y = -4.4
k = s.molecule("BrCC(C)=O", at=(0.4, y), show_h=[1], lone_pairs=[4])
oh = s.molecule("[OH-]", at=(2.6, y - 1.0), lone_pairs=True)
h = nearest_h(k, 1, oh.xy(0))
s.curly(oh.atom(0), h, bend=0.4)
s.curly((k.xy(1) + h.xy) / 2, k.bond(1, 2), bend=0.6)
s.curly(k.bond(2, 4), k.atom(4), bend=0.6)
s.text((1.2, y - 2.4), "more acidic: faster second deprotonation")
s.arrow((3.6, y), (5.0, y), above=r"$-$H$_2$O")
s.molecule("BrC=C([O-])C", at=(6.4, y))
s.arrow((7.8, y), (9.2, y), above=r"Br$_2$, then again")
s.molecule("CC(=O)C(Br)(Br)Br", at=(10.8, y))
s.draw()
