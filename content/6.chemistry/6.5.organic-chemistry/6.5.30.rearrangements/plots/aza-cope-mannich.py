"""Aza-Cope-Mannich reaction (Overman), on the simplest acyclic substrate: the iminium ion formed
from formaldehyde and 2-hydroxy-2-methylbut-3-enyl(methyl)amine. Top: a cationic 2-aza-Cope
([3,3]-sigmatropic) rearrangement through a six-membered transition state (dashed: the forming
C-C bond) gives an enol and a new iminium ion. Bottom: the enol attacks the iminium carbon
intramolecularly (Mannich reaction), closing a pyrrolidine ring; loss of the proton gives
1-(1-methylpyrrolidin-3-yl)ethan-1-one, a 3-acylpyrrolidine."""

import math

from wikichem import Scheme


def ring_xy(cx, cy, angle, r=1.0):
    return (cx + r * math.cos(math.radians(angle)), cy + r * math.sin(math.radians(angle)))


s = Scheme()
y = 0.0
cx = 0.0
# C1(H2)=N2(+)(Me)-C3H2-C4(OH)(Me)-C5H=C6H2
p = {a: ring_xy(cx, y, a) for a in (30, 90, 150, 210, 270, 330)}
c4 = p[210]
coords = [p[30], p[90], ring_xy(cx, y, 90, 2.0), p[150], c4, (c4[0] - 0.98, c4[1] + 0.2),
          (c4[0] - 0.35, c4[1] - 0.94), p[270], p[330]]
k = s.molecule("C=[N+](C)CC(O)(C)C=C", coords=coords)
s.partial(k.atom(0), k.atom(8))
s.curly(k.bond(7, 8), k.bond(0, 8), bend=0.6)
s.curly(k.bond(0, 1), k.bond(1, 3), bend=0.6)
s.curly(k.bond(3, 4), k.bond(4, 7), bend=0.6)
s.text((cx, y - 2.4), "iminium ion")
s.arrow((2.2, y), (3.6, y), above="2-aza-Cope", below="[3,3]")
# enol and iminium: C3=N2(+)(Me)-C1-C6-C5=C4(OH)Me on a pentagon N2, C1, C6, C5, C3
cx2 = 6.0
q = {a: ring_xy(cx2, y, a, 0.85) for a in (90, 162, 234, 306, 18)}
c5 = q[306]
c4b = ring_xy(c5[0], c5[1], 306, 1.0)
coords2 = [q[18], q[90], ring_xy(cx2, y, 90, 1.85), q[162], q[234], c5, c4b,
           ring_xy(c4b[0], c4b[1], 0, 1.0), ring_xy(c4b[0], c4b[1], 250, 1.0)]
e = s.molecule("C=[N+](C)CCC=C(O)C", coords=coords2, lone_pairs=[7])
s.partial(e.atom(5), e.atom(0))
s.curly(e.atom(7), e.bond(6, 7), bend=0.6)
s.curly(e.bond(5, 6), e.bond(5, 0), bend=0.6)
s.curly(e.bond(0, 1), e.atom(1), bend=-0.6)
s.text((cx2, y - 3.4), "enol + iminium ion")
s.arrow((8.6, y), (10.0, y), above="Mannich", below=r"$-$H$^+$")
s.molecule("CN1CCC(C(C)=O)C1", at=(12.4, y))
s.text((12.4, y - 2.4), "3-acetyl-1-methylpyrrolidine")
s.draw()
