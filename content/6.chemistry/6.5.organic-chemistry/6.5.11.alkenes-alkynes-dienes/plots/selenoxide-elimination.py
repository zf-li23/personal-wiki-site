"""Selenoxide syn elimination. After the PhSe group has been added and oxidized (H2O2 or mCPBA), the
selenoxide oxygen takes a hydrogen on the neighbouring carbon through a five-membered cyclic
transition state: the C-H bond becomes the new pi bond and the C-Se bond breaks toward selenium.
The H and the Se group leave from the same side (syn), at room temperature; PhSeOH is released (in the diastereomer drawn, the two methyl groups end up cis)."""

import numpy as np
from wikichem import Scheme

ang = np.radians([234, 306, 18, 90, 162])
r = 0.85
C2, C1, H, O, SE = [(r * np.cos(t), r * np.sin(t)) for t in ang]

s = Scheme(scale=0.6)
# SMILES order: CH3(6), C1, H(5), C2, CH3(7), Se, O, Ph
m = s.molecule("[CH3:6][CH:1]([H:5])[CH:2]([CH3:7])[Se+:3]([O-:4])[*:8]",
               coords=[(1.25, -1.35), C1, H, C2, (-1.25, -1.35), SE, O, (-1.85, 0.6)],
               labels={8: "Ph"}, lone_pairs=[4])
s.partial(m.atom(4), m.atom(5))
s.curly(m.atom(4), m.atom(5), bend=-0.6)
s.curly(m.bond(1, 5), m.bond(1, 2), bend=-0.9)
s.curly(m.bond(2, 3), m.atom(3), bend=0.9)
s.arrow((2.0, 0), (3.2, 0), above="r.t.", below="syn")
s.molecule("C/C=C\\C", at=(4.6, 0))
s.plus((6.2, 0))
s.text((7.3, 0), "PhSeOH")
s.text((-0.1, -2.2), "selenoxide (cyclic TS)")
s.draw()
