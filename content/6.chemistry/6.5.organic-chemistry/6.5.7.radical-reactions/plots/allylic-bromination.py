"""Allylic bromination of cyclohexene with NBS (Goldfinger mechanism). NBS only keeps the Br2
concentration low by reacting with the HBr formed; the chain carriers are Br atoms.
(1) A bromine atom abstracts an allylic H; the allylic radical is delocalised over C1 and C3.
(2) The allylic radical abstracts Br from Br2 and regenerates the bromine atom."""

import numpy as np
from wikichem import Scheme


def unit(v):
    return v / np.linalg.norm(v)


def pt(p):
    return np.asarray(p.xy if hasattr(p, "xy") else p, float)


# Atom numbers are the map numbers; the two resonance structures list the atoms in the same order.
SM = "[CH2:1]1[CH2:2][CH2:3][CH2:4][CH:5]=[CH:6]1"  # cyclohexene, allylic C1
A = "[CH:1]1[CH2:2][CH2:3][CH2:4][CH:5]=[CH:6]1"  # radical centre at C1, C5=C6
B = "[CH:1]=1[CH2:2][CH2:3][CH2:4][CH:5][CH:6]1"  # radical centre at C5, C1=C6

# (1) Br. + allylic C-H -> HBr + allylic radical (two resonance structures).
s = Scheme()
m = s.molecule(SM, at=(0, 0), show_h=[1])
c1, h = m.xy(1), m.h(1)
u = unit(h.xy - c1)
n = np.array([-u[1], u[0]])
br = s.molecule("[Br]", at=h.xy + 1.9 * u)
new = (br.xy(0) + h.xy) / 2
mid = (c1 + h.xy) / 2
s.curly(br.atom(0), new + 0.28 * n, bend=-0.7, single=True)
s.curly(mid + 0.12 * n, new + 0.34 * n - 0.1 * u, bend=0.7, single=True)
s.curly(mid - 0.12 * n, m.atom(1), bend=-0.8, single=True)
s.arrow((2.0, 0), (3.4, 0), above=r"$-$HBr")
r1 = s.molecule(A, at=(5.0, 0))
s.arrow((6.6, 0), (7.8, 0), kind="resonance")
s.molecule(B, at=(9.4, 0), like=r1)
s.draw()

# (2) allylic radical + Br-Br -> 3-bromocyclohexene + Br.
s = Scheme()
r = s.molecule(A, at=(0, 0))
c1 = r.xy(1)
a = c1 + np.array([-1.7, 0.0])
b = a + np.array([-1.4, 0.0])
bb = s.molecule("BrBr", coords=[b, a])
new = (c1 + a) / 2
bond = (a + b) / 2
s.curly(r.atom(1), new + (0.0, 0.22), bend=-0.7, single=True)
s.curly(bond + (0, 0.14), new + (-0.12, 0.24), bend=0.6, single=True)
s.curly(bond + (0, -0.14), bb.atom(0), bend=0.9, single=True)
s.arrow((2.2, 0), (3.6, 0))
s.molecule("Br[CH:1]1[CH2:2][CH2:3][CH2:4][CH:5]=[CH:6]1", at=(5.2, 0))
s.plus((7.0, 0))
s.molecule("[Br]", at=(7.8, 0))
s.text((5.2, -1.8), "3-bromocyclohexene", size=10)
s.draw()
