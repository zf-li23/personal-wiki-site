"""Barton reaction (nitrite photolysis), on pentyl nitrite. Light cleaves the weak O-NO bond
homolytically (fishhook arrows), giving an alkoxyl radical and nitric oxide. The alkoxyl radical
abstracts a hydrogen atom from the delta carbon through a six-membered cyclic transition state
(1,5-hydrogen atom transfer), moving the radical centre to an unactivated secondary carbon. This
carbon radical combines with NO to give a delta-nitroso alcohol, which tautomerises to the oxime."""

import math

import numpy as np
from wikichem import Scheme


def shift(p, d):
    return np.asarray(p.xy, float) + np.asarray(d, float)


def ring(cx, r, angles):
    return [(cx + r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in angles]


s = Scheme()
cap = -2.3
n = s.molecule("CCCCCON=O", at=(0.0, 0.0))
mid = n.bond(5, 6)
s.curly(shift(mid, (-0.1, 0.25)), shift(n.atom(5), (0.0, 0.45)), bend=0.8, single=True)
s.curly(shift(mid, (0.1, -0.25)), shift(n.atom(6), (0.1, -0.45)), bend=0.8, single=True)
s.text((0.0, cap), "pentyl nitrite")
s.arrow((3.0, 0), (4.4, 0), above=r"$h\nu$", below=r"$-$NO$^\bullet$")
cx = 6.4
o, c1, c2, c3, c4, h = ring(cx, 1.3, [90, 150, 210, 270, 330, 30])
c5 = (c4[0] + 1.1, c4[1] - 0.6)
t = s.molecule("[O]CCCC([H])C", coords=[o, c1, c2, c3, c4, h, c5])
s.curly(t.atom(0), t.bond(0, 5), bend=-1.2, single=True)
s.curly(shift(t.bond(4, 5), (0.18, 0.0)), shift(t.bond(0, 5), (0.12, -0.1)), bend=0.9, single=True)
s.curly(shift(t.bond(4, 5), (-0.15, 0.0)), shift(t.atom(4), (-0.25, 0.15)), bend=-0.9, single=True)
s.text((cx, cap), "alkoxyl radical, 1,5-HAT")
s.arrow((8.6, 0), (10.0, 0))
s.molecule("OCCC[CH]C", at=(12.6, 0))
s.text((12.6, cap), "delta-carbon radical")
y2 = -5.0
s.arrow((0.4, y2), (1.9, y2), above=r"NO$^\bullet$")
s.molecule("OCCCC(C)N=O", at=(5.6, y2))
s.text((5.6, y2 + cap), "delta-nitroso alcohol")
s.arrow((8.6, y2), (10.0, y2), above="tautomerism")
s.molecule("OCCCC(C)=NO", at=(12.6, y2))
s.text((12.6, y2 + cap), "oxime")
s.draw()
