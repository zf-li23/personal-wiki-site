"""Umpolung with 1,3-dithiane. Butyllithium removes the C2 proton of 2-phenyl-1,3-dithiane (the
anion is stabilised by the two polarisable sulfur atoms); the lithiated dithiane, an acyl anion
equivalent, alkylates 1-bromobutane by SN2; mercury(II)-assisted hydrolysis releases the ketone.
The former aldehyde carbon has reacted as a nucleophile."""

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
dt = s.molecule("C1(c2ccccc2)SCCCS1", at=(0, y), show_h=[0])
bu = s.molecule("CCCC[Li]", at=(1.0, y + 3.0))
h = nearest_h(dt, 0, bu.xy(3))
s.curly(bu.bond(3, 4), h, bend=0.5)
s.curly((dt.xy(0) + h.xy) / 2, dt.atom(0), bend=0.9)
s.arrow((3.0, y), (4.4, y), above="THF", below=r"$-$BuH")
an = s.molecule("[C-]1(c2ccccc2)SCCCS1", at=(7.0, y), lone_pairs=[0])
br = s.molecule("CCCCBr", at=(8.6, y + 3.0), lone_pairs=[4])
s.curly(an.atom(0), br.atom(3), bend=-0.4)
s.curly(br.bond(3, 4), br.atom(4), bend=-0.8)
s.text((9.4, y - 1.2), r"Li$^+$", size=13)

y = -6.0
s.arrow((-3.0, y), (-1.6, y), above=r"$-$LiBr")
s.molecule("CCCCC1(c2ccccc2)SCCCS1", at=(1.2, y))
s.arrow((4.0, y), (6.0, y), above=r"HgCl$_2$", below=r"H$_2$O")
s.molecule("CCCCC(=O)c1ccccc1", at=(10.0, y))
s.draw()
