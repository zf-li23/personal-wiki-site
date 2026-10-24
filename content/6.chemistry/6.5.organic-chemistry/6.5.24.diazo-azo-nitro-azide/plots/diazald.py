"""Preparation of diazomethane from Diazald (N-methyl-N-nitroso-p-toluenesulfonamide). Top: alkoxide
attacks the sulfonyl sulfur and the S-N bond breaks, releasing the methyldiazotate anion
CH3-N=N-O(-) (shown after protonation by the alcohol). Bottom: the N=N-OH group loses hydroxide as
the nitrogen lone pair forms a triple bond, giving the methyldiazonium ion; base removes a proton
from its methyl group, the C-H electrons form the C=N bond and one N-N pi bond moves onto the
terminal nitrogen, giving diazomethane."""

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
dz = s.molecule("Cc1ccc(cc1)S(=O)(=O)N(C)N=O", at=(0, y))
ro = s.molecule("C[O-]", at=(dz.xy(7)[0] - 0.4, dz.xy(7)[1] + 2.2), lone_pairs=[1])
s.curly(ro.atom(1), dz.atom(7), bend=0.4)
s.curly(dz.bond(7, 10), dz.atom(10), bend=0.6)
s.arrow((3.6, y), (5.0, y), below=r"$-$TsOMe")
s.molecule("CN=N[O-]", at=(7.0, y))
s.arrow((8.6, y), (10.0, y), above="MeOH", below=r"$-$MeO$^-$")
s.molecule("CN=NO", at=(11.6, y))

y = -4.0
a = s.molecule("CN=NO", at=(0, y), lone_pairs=[1])
s.curly(a.atom(1), a.bond(1, 2), bend=0.6)
s.curly(a.bond(2, 3), a.atom(3), bend=0.6)
s.arrow((1.6, y), (3.0, y), below=r"$-$HO$^-$")
m = s.molecule("C[N+]#N", at=(4.6, y), show_h=[0])
b = s.molecule("C[O-]", at=(m.xy(0)[0] - 1.6, m.xy(0)[1] - 1.4), lone_pairs=[1])
h = nearest_h(m, 0, b.xy(1))
s.curly(b.atom(1), h, bend=-0.4)
s.curly((m.xy(0) + h.xy) / 2, m.bond(0, 1), bend=-0.6)
s.curly(m.bond(1, 2), m.atom(2), bend=-0.6)
s.text((4.6, y + 1.5), "methyldiazonium")
s.arrow((6.4, y), (7.8, y), below=r"$-$MeOH")
s.molecule("C=[N+]=[N-]", at=(9.2, y))
s.text((9.2, y - 1.3), "diazomethane")
s.draw()
