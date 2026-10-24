"""Mislow-Evans rearrangement. An allylic sulfoxide is in equilibrium with the allylic sulfenate ester
through a [2,3]-sigmatropic shift: the sulfoxide oxygen bonds to the far end of the allyl group while
the C=C bond moves and the C-S bond breaks (five-membered cyclic transition state). The equilibrium
lies on the sulfoxide side, but a thiophile such as trimethyl phosphite cleaves the O-S bond of the
sulfenate and pulls the reaction over to the allylic alcohol, with transposition of the double bond."""

import math

from wikichem import Scheme

ring = [(-1.95 + math.cos(math.radians(a)), -0.3 + math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]
# atom order: O, S, phenyl (6), CH2, CH, CH, CH3; the allyl group bends back towards oxygen
SULFOXIDE = [(0.25, 1.25), (0.0, 0.0)] + ring + [(0.95, -0.35), (1.6, 0.45), (1.3, 1.4), (1.95, 2.2)]

s = Scheme(scale=0.42)
y = 0.0
a = s.molecule("[O-][S+](c1ccccc1)CC=CC", coords=[(x + 1.0, q + y) for x, q in SULFOXIDE], lone_pairs=[0])
s.curly(a.atom(0), a.atom(10), bend=-0.5)
s.curly(a.bond(9, 10), a.bond(8, 9), bend=-0.7)
s.curly(a.bond(1, 8), a.atom(1), bend=0.7)
s.text((0.3, y - 2.0), "allylic sulfoxide")
s.arrow((3.4, y + 0.3), (4.8, y + 0.3), kind="equilibrium", above="[2,3]")
s.molecule("CC(OSc1ccccc1)C=C", at=(9.0, y))
s.text((9.0, y - 2.0), "allylic sulfenate")
s.arrow((11.8, y + 0.3), (13.4, y + 0.3), above=r"P(OMe)$_3$", below="MeOH")
s.molecule("CC(O)C=C", at=(15.0, y))
s.text((15.0, y - 2.0), "allylic alcohol")
s.draw()
