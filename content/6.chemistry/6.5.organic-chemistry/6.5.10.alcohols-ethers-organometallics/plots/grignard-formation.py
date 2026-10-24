"""Grignard reagent formation goes through radicals. Top: an electron from the magnesium surface
enters the C-Br sigma* orbital; the C-Br bond breaks, giving an alkyl radical and BrMg (one
electron), which combine to the Grignard reagent. Bottom: the hex-5-enyl radical from
6-bromohex-1-ene can instead cyclize (5-exo) before it is captured, so part of the reagent is
cyclopentylmethylmagnesium bromide, a sign of the radical intermediate."""

import math

from wikichem import Scheme

s = Scheme()
y = 0.0
s.text((-1.6, y + 0.9), "Mg")
rb = s.molecule("BrCC", at=(0.4, y - 0.2), lone_pairs=[0])
s.curly((-1.3, y + 0.9), rb.bond(0, 1), bend=-0.5, single=True)
s.curly(rb.bond(0, 1), rb.atom(0), bend=0.9, single=True)
s.arrow((2.2, y), (3.6, y), above="SET")
s.molecule("C[CH2]", at=(4.5, y))
s.text((6.1, y), r"+  $\cdot$MgBr")
s.arrow((7.4, y), (8.8, y), above="fast")
s.molecule("CC[Mg]Br", at=(10.2, y))

y = -3.4
# atoms: 0 radical C, 1-3 CH2, 4 =CH, 5 =CH2, on a broken pentagon so the closing bond is visible
pent = [(1.15 * math.cos(math.radians(a)), 1.15 * math.sin(math.radians(a))) for a in (234, 162, 90, 18, -54)]
rad = s.molecule("[CH2]CCCC=C", coords=pent + [(pent[4][0] + 0.9, pent[4][1] - 0.45)], at=(0.6, y))
s.curly(rad.atom(0), rad.bond(0, 4), bend=-0.8, single=True)
s.curly(rad.bond(4, 5), rad.bond(0, 4), bend=-0.9, single=True)
s.curly(rad.bond(4, 5), rad.atom(5), bend=1.0, single=True)
s.text((0.6, y - 2.1), "hex-5-enyl radical")
s.arrow((3.0, y), (4.4, y), above="5-exo")
s.molecule("[CH2]C1CCCC1", at=(6.0, y))
s.arrow((7.6, y), (9.0, y), above=r"$\cdot$MgBr")
s.molecule("Br[Mg]CC1CCCC1", at=(11.0, y))
s.draw()
