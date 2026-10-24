"""Acid-catalysed acetal formation from acetaldehyde and methanol. Top: methanol adds to the
protonated carbonyl group and loses a proton, giving the hemiacetal. Bottom: the hemiacetal OH is
protonated and leaves as water, pushed out by the lone pair of the OMe oxygen, which gives an
oxocarbenium ion (the slow step); a second methanol adds and loses a proton, giving the acetal.
Every step is reversible: read from right to left, the scheme is the acid hydrolysis of an acetal."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ald = s.molecule("CC=O", at=(-0.6, y))
s.arrow((0.6, y), (1.8, y), above=r"H$^+$", kind="equilibrium")
ox = s.molecule("C[CH]=[OH+]", at=(3.0, y))
me = s.molecule("CO", at=(3.2, y - 2.0), lone_pairs=True)
s.curly(me.atom(1), ox.atom(1), bend=0.4)
s.curly(ox.bond(1, 2), ox.atom(2), bend=-1.2)
s.arrow((4.4, y), (5.6, y), kind="equilibrium")
s.molecule("C[CH](O)[OH+]C", at=(7.0, y))
s.arrow((8.4, y), (9.6, y), above=r"$-$H$^+$", kind="equilibrium")
s.molecule("CC(O)OC", at=(11.0, y))
s.text((11.0, y - 1.6), "hemiacetal")

y = -4.8
h = s.molecule("COC(C)[OH2+]", at=(-0.4, y), lone_pairs=[1])
s.curly(h.bond(2, 4), h.atom(4), bend=-0.9)
s.curly(h.atom(1), h.bond(1, 2), bend=-0.9)
s.arrow((1.4, y), (2.8, y), above=r"$-$H$_2$O", below="slow", kind="equilibrium")
ox2 = s.molecule("C[CH]=[O+]C", at=(4.2, y))
me2 = s.molecule("CO", at=(4.0, y - 2.1), lone_pairs=True)
s.curly(me2.atom(1), ox2.atom(1), bend=0.4)
s.curly(ox2.bond(1, 2), ox2.atom(2), bend=-1.2)
s.text((4.4, y + 1.3), "oxocarbenium ion")
s.arrow((5.8, y), (7.0, y), kind="equilibrium")
s.molecule("CC(OC)[OH+]C", at=(8.4, y))
s.arrow((9.8, y), (11.0, y), above=r"$-$H$^+$", kind="equilibrium")
s.molecule("CC(OC)OC", at=(12.4, y))
s.text((12.4, y - 1.6), "acetal")
s.draw()
