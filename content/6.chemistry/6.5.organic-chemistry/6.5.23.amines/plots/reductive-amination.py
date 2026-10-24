"""Reductive amination of acetone with methylamine. (1) The amine adds to the carbonyl carbon and a
proton transfer gives the carbinolamine. (2) The protonated hydroxyl leaves as water, pushed out by
the nitrogen lone pair, giving the iminium ion. (3) Cyanoborohydride delivers hydride from its B-H
bond to the iminium carbon, giving N-methylpropan-2-amine."""

import numpy as np

from wikichem import Scheme

# (1) addition
s = Scheme()
ketone = s.molecule("C[C:1](C)=[O:2]", at=(0, 0), lone_pairs=[2])
amine = s.molecule("C[NH2:3]", at=(1.9, -1.4), lone_pairs=[3])
s.curly(amine.atom(3), ketone.atom(1), bend=-0.4)
s.curly(ketone.bond(1, 2), ketone.atom(2), bend=-0.5)
s.arrow((3.0, 0), (4.4, 0), kind="equilibrium", above="proton", below="transfer")
s.molecule("C[C:1](C)([OH:2])[NH:3]C", at=(6.2, 0), lone_pairs=[2, 3])
s.arrow((7.9, 0), (9.3, 0), kind="equilibrium", above=r"$\mathrm{H^+}$")
s.molecule("C[C:1](C)([OH2+:2])[NH:3]C", at=(11.1, 0), lone_pairs=[3])
s.draw()

# (2) loss of water and (3) hydride transfer
s = Scheme()
c = s.molecule("C[C:1](C)([OH2+:2])[NH:3]C", at=(0, 0), lone_pairs=[3])
s.curly(c.atom(3), c.bond(1, 3), bend=-1.2)
s.curly(c.bond(1, 2), c.atom(2), bend=-1.0)
s.arrow((1.8, 0), (3.2, 0), kind="equilibrium", above=r"$-\mathrm{H_2O}$")
im = s.molecule("C[C:1](C)=[NH+:2]C", at=(5.0, 0))
b = s.molecule("N#C[BH3-:1]", at=(5.4, 2.4), show_h=[1])
hb = b.h(1, 0).xy
mid = (hb + b.xy(1)) / 2
s.curly(mid, im.atom(1), bend=0.5)
s.curly(im.bond(1, 2), im.atom(2), bend=1.1)
s.arrow((7.0, 0), (8.4, 0))
s.molecule("CC(C)NC", at=(9.8, 0))
s.draw()
