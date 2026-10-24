"""Diazotization of aniline. (1) Protonated nitrous acid loses water to give the nitrosonium ion.
(2) The amine lone pair attacks the nitrogen of NO+; loss of a proton gives N-nitrosoaniline.
(3) After tautomerization to the diazohydroxide and protonation of OH, the lone pair on the
aryl-bearing nitrogen pushes out water, giving the benzenediazonium ion."""

import math

from wikichem import Scheme

# benzenediazonium with a linear C-N-N unit: ring atoms 0-5 (atom 3 bears N), then the two nitrogens
ARYL_N2 = [(math.cos(math.radians(a)) - 1.5, math.sin(math.radians(a))) for a in (180, 120, 60, 0, 300, 240)]
ARYL_N2 += [(0.5, 0.0), (1.5, 0.0)]

# (1) nitrosonium ion
s = Scheme()
a = s.molecule("[O:1]=[N:2][OH2+:3]", at=(0, 0), lone_pairs=[1, 2])
s.curly(a.bond(2, 3), a.atom(3), bend=-0.6)
s.curly(a.atom(1), a.bond(1, 2), bend=-1.0)
s.arrow((1.6, 0), (3.0, 0))
s.molecule("N#[O+]", at=(4.3, 0))
s.plus((5.6, 0))
s.molecule("O", at=(6.4, 0))
s.draw()

# (2) N-nitrosation
s = Scheme()
an = s.molecule("c1ccc(cc1)[NH2:1]", at=(0, 0), lone_pairs=[1], flip=True)
no = s.molecule("[N:2]#[O+:3]", at=(an.xy(1)[0] + 2.2, an.xy(1)[1] + 0.9))
s.curly(an.atom(1), no.atom(2), bend=-0.4)
s.curly(no.bond(2, 3), no.atom(3), bend=-0.7)
x = no.xy(3)[0] + 0.8
s.arrow((x, 0), (x + 1.4, 0), above=r"$-\mathrm{H^+}$")
s.molecule("c1ccc(cc1)NN=O", at=(x + 3.4, 0), flip=True)
s.draw()

# (3) tautomerization and loss of water
s = Scheme()
s.molecule("c1ccc(cc1)NN=O", at=(-0.6, 0), flip=True)
s.arrow((2.6, 0), (4.2, 0), kind="equilibrium", above="tautomerize", below=r"$+\mathrm{H^+}$")
d = s.molecule("c1ccc(cc1)[N:1]=[N:2][OH2+:3]", at=(6.8, 0), lone_pairs=[1], flip=True)
s.curly(d.atom(1), d.bond(1, 2), bend=0.9)
s.curly(d.bond(2, 3), d.atom(3), bend=0.6)
s.arrow((9.5, 0), (10.9, 0), above=r"$-\mathrm{H_2O}$")
s.molecule("c1ccc(cc1)[N+]#N", at=(13.6, 0), coords=ARYL_N2)
s.draw()
