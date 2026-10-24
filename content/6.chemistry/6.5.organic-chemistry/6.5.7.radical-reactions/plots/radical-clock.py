"""Radical clocks. Top: the 5-hexenyl radical cyclizes (5-exo-trig): the unpaired electron on C1 pairs
with one electron of the C5=C6 pi bond to form the C1-C5 bond, and the other pi electron stays on C6,
giving the cyclopentylmethyl radical (k = 2.3e5 s^-1 at 25 C). Bottom: the cyclopropylmethyl radical
opens (beta-scission of a ring bond, k = 9.4e7 s^-1): the unpaired electron and one electron of the
C2-C3 bond form the C1=C2 pi bond, and the other electron goes to C3, giving the 3-butenyl radical."""

import math

import numpy as np
from wikichem import Scheme


def up(p, dy):
    return np.asarray(p.xy if hasattr(p, "xy") else p, float) + (0.0, dy)


s = Scheme()
r = 1 / (2 * math.sin(math.pi / 5))
ang = [162, 234, 306, 18, 90]  # C1..C5 on a pentagon; C1-C5 is the bond being formed
pts = [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in ang]
pts.append((pts[4][0] + 1.25, pts[4][1]))  # C6
hex_ = s.molecule("[CH2:1][CH2:2][CH2:3][CH2:4][CH:5]=[CH2:6]", coords=pts)
new = (hex_.xy(1) + hex_.xy(5)) / 2
s.curly(hex_.atom(1), up(new, 0.18), bend=0.8, single=True)
c5, c6 = hex_.xy(5), hex_.xy(6)
left = np.array([0.0, 1.0])
s.curly(c5 + 0.35 * (c6 - c5) + 0.18 * left, up(new, 0.24), bend=0.5, single=True)
s.curly(c5 + 0.65 * (c6 - c5) - 0.18 * left, c6 - 0.32 * left, bend=0.8, single=True)
s.text((0, -1.7), "5-hexenyl radical", size=10)
s.arrow((2.6, 0), (4.2, 0), above=r"$k = 2.3\times10^5$ s$^{-1}$", below="5-exo")
s.molecule("[CH2]C1CCCC1", at=(5.9, 0))
s.text((5.9, -1.7), "cyclopentylmethyl radical", size=10)
s.draw()

s = Scheme()
cp = s.molecule("[CH2:1][CH:2]1[CH2:3][CH2:4]1", coords=[(-1.3, 0.0), (0.0, 0.0), (0.75, 0.6), (0.75, -0.6)])
new = cp.bond(1, 2)
s.curly(cp.atom(1), up(new, 0.22), bend=0.8, single=True)
s.curly(cp.bond(2, 3).xy + (-0.1, 0.1), up(new, 0.26), bend=0.6, single=True)
s.curly(cp.bond(2, 3).xy + (0.1, -0.08), cp.xy(3) + (0.2, -0.2), bend=-0.9, single=True)
s.text((0, -1.4), "cyclopropylmethyl radical", size=10)
s.arrow((1.9, 0), (3.5, 0), above=r"$k = 9.4\times10^7$ s$^{-1}$", below="ring opening")
s.molecule("C=CC[CH2]", at=(5.0, 0))
s.text((5.0, -1.4), "3-butenyl radical", size=10)
s.draw()
