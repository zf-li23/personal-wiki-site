"""Resonance structures of the allyl radical and the allyl anion. Radical (fishhook arrows, one electron
each): one electron of the pi bond and the unpaired electron on C3 form the new C2-C3 pi bond, the
other pi electron stays on C1. Anion: the lone pair on C3 forms the new pi bond and the old pi pair
moves onto C1. In both, the unpaired electron or the charge sits on the two end carbons only, as the
Hueckel nonbonding orbital predicts (zero coefficient on C2)."""

import numpy as np

from wikichem import Scheme

s = Scheme(scale=0.42)
y = 0.0
s.text((-2.6, y), "radical", size=10)
XY = [(-1.3, 0.38), (0.0, -0.38), (1.3, 0.38)]  # bonds drawn 1.5 times the usual length, to leave room for the arrows
r = s.molecule("[CH2:1]=[CH:2][CH2:3]", coords=XY, at=(0, y))
c1, c2, c3 = r.xy(1), r.xy(2), r.xy(3)
m12, m23 = (c1 + c2) / 2, (c2 + c3) / 2
# one pi electron goes to C1, the other pairs with the electron on C3 to form the C2=C3 pi bond
s.curly(m12 + (0.12, -0.3), c1 + (-0.1, -0.45), bend=0.6, single=True)
s.curly(m12 + (-0.12, 0.3), m23 + (-0.15, 0.35), bend=-0.5, single=True)
s.curly(r.atom(3), m23 + (0.05, 0.38), bend=0.5, single=True)
s.arrow((2.2, y), (3.4, y), kind="resonance")
s.molecule("[CH2:1][CH:2]=[CH2:3]", coords=XY, at=(5.6, y))

y = -2.8
s.text((-2.6, y), "anion", size=10)
a = s.molecule("[CH2:1]=[CH:2][CH2-:3]", coords=XY, at=(0, y), lone_pairs=[3])
s.curly(a.atom(3), a.bond(2, 3), bend=0.6)
s.curly(a.xy(1) / 2 + a.xy(2) / 2 + (0.12, -0.3), a.xy(1) + (-0.1, -0.45), bend=0.6)
s.arrow((2.2, y), (3.4, y), kind="resonance")
s.molecule("[CH2-:1][CH:2]=[CH2:3]", coords=XY, at=(5.6, y), lone_pairs=[1])
s.draw()
