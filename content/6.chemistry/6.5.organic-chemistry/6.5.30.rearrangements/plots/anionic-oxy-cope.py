"""Anionic oxy-Cope rearrangement of 3-methylhexa-1,5-dien-3-ol. The potassium alkoxide (KH,
18-crown-6, THF) undergoes the [3,3]-sigmatropic shift at room temperature, through a chair-like
six-membered transition state drawn flat here (the dashed line is the forming C1-C6 bond): the
C3-C4 bond, weakened by the alkoxide, breaks and the two pi bonds move. The product is a potassium
enolate, which is protonated on work-up and tautomerises to hept-6-en-2-one."""

import math

from wikichem import Scheme


def ring_xy(cx, cy, angle, r=1.0):
    return (cx + r * math.cos(math.radians(angle)), cy + r * math.sin(math.radians(angle)))


s = Scheme()
y = 0.0
cx = 0.0
# C1, C2, C3, O-, Me, C4, C5, C6
c1, c2, c3, c4, c5, c6 = (ring_xy(cx, y, a) for a in (30, 90, 150, 210, 270, 330))
coords = [c1, c2, c3, ring_xy(cx, y, 150, 2.0), (c3[0] - 0.2, c3[1] + 0.98), c4, c5, c6]
k = s.molecule("C=CC([O-])(C)CC=C", coords=coords, lone_pairs=[3])
s.partial(k.atom(0), k.atom(7))
s.curly(k.bond(6, 7), k.bond(0, 7), bend=0.6)
s.curly(k.bond(0, 1), k.bond(1, 2), bend=0.6)
s.curly(k.bond(2, 5), k.bond(5, 6), bend=0.6)
s.text((cx, y - 2.3), r"K$^+$ alkoxide (chair TS)")
s.arrow((2.2, y), (3.6, y), above="[3,3]", below="rt")
s.molecule("CC([O-])=CCCC=C", at=(6.4, y), lone_pairs=[2])
s.text((6.4, y - 2.3), "enolate")
s.arrow((9.2, y), (10.6, y), above=r"H$_3$O$^+$")
s.molecule("CC(=O)CCCC=C", at=(13.4, y))
s.text((13.4, y - 2.3), "hept-6-en-2-one")
s.draw()
