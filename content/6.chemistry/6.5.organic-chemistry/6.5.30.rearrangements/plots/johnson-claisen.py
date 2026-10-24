"""Johnson-Claisen rearrangement of but-3-en-2-ol with triethyl orthoacetate. Acid-catalysed
exchange gives the mixed orthoester, which loses ethanol to form a ketene acetal
CH2=C(OEt)-O-allyl, an allyl vinyl ether generated in situ. Its [3,3]-sigmatropic shift through
a six-membered (chair) transition state, drawn flat with the forming C-C bond dashed, transposes
the allylic double bond and gives ethyl (E)-hex-4-enoate, a gamma,delta-unsaturated ester."""

import math

from wikichem import Scheme


def ring_xy(cx, cy, angle, r=1.0):
    return (cx + r * math.cos(math.radians(angle)), cy + r * math.sin(math.radians(angle)))


s = Scheme()
y = 0.0
s.molecule("CC(O)C=C", at=(0.0, y))
s.text((0.0, y - 1.8), "but-3-en-2-ol")
s.arrow((1.6, y), (4.4, y), above=r"MeC(OEt)$_3$, H$^+$", below=r"$-$2 EtOH, 140 °C")
cx = 6.6
# CH2=, C(OEt), OEt O, Et C, Et C, O(ring), CH, Me, CH=, =CH2
p = {a: ring_xy(cx, y, a) for a in (330, 30, 90, 150, 210, 270)}
oe = ring_xy(cx, y, 30, 2.0)
coords = [p[330], p[30], oe, ring_xy(oe[0], oe[1], 90), ring_xy(oe[0], oe[1], 30, 2.0) if False else (oe[0] + 0.87, oe[1] + 1.5),
          p[90], p[150], ring_xy(cx, y, 150, 2.0), p[210], p[270]]
k = s.molecule("C=C(OCC)OC(C)C=C", coords=coords)
s.partial(k.atom(0), k.atom(9))
s.curly(k.bond(8, 9), k.bond(0, 9), bend=-0.6)
s.curly(k.bond(5, 6), k.bond(6, 8), bend=-0.6)
s.curly(k.bond(0, 1), k.bond(1, 5), bend=-0.6)
s.text((cx, y - 2.2), "ketene acetal (chair TS)")
s.arrow((8.8, y), (10.2, y), above="[3,3]")
s.molecule("CCOC(=O)CC/C=C/C", at=(13.4, y))
s.text((13.4, y - 1.8), "ethyl (E)-hex-4-enoate")
s.draw()
