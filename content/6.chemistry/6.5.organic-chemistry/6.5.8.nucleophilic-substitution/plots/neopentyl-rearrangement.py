"""Solvolysis of neopentyl bromide. A primary cation is too unstable to form; instead the methyl group
anti to the leaving group migrates with its bonding pair to C1 as bromide leaves, giving the tertiary
2-methyl-2-butyl cation directly. Ethanol captures it (2-ethoxy-2-methylbutane after loss of a proton)
or it loses a proton (2-methyl-2-butene)."""

from wikichem import Scheme

s = Scheme()
# C1, Br, C2 (quaternary), migrating CH3 (anti to Br), two other CH3
nb = s.molecule("[CH2:1]([Br:2])[C:3]([CH3:4])([CH3:5])[CH3:6]",
                coords=[(0, 0), (0.65, -1.1), (-1.3, 0), (-1.95, 1.1), (-1.95, -1.1), (-2.6, 0)], lone_pairs=[2])
s.curly(nb.bond(3, 4), nb.atom(1), bend=-0.6)
s.curly(nb.bond(1, 2), nb.atom(2), bend=0.8)
s.text((-1.0, -2.1), "neopentyl bromide", size=10)
s.arrow((1.4, 0), (2.8, 0), above="EtOH", below=r"$-$Br$^-$")
s.molecule("CC[C+](C)C", at=(4.3, 0))
s.text((4.3, -1.9), "tertiary cation", size=10)
s.arrow((5.8, 0.4), (7.2, 1.3))
s.arrow((5.8, -0.4), (7.2, -1.3))
s.text((6.1, 1.4), r"EtOH, $-$H$^+$", size=10)
s.text((6.9, -0.5), r"$-$H$^+$", size=10)
s.molecule("CCC(C)(C)OCC", at=(9.6, 1.6))
s.molecule("CC=C(C)C", at=(9.2, -1.7))
s.draw()
