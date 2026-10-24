"""SN1 of an allylic halide with allylic rearrangement. 1-Chloro-2-butene ionizes to the
1-methylallyl cation, whose positive charge is shared by C1 and C3 (resonance). Water attacks
either end, giving 2-buten-1-ol and 3-buten-2-ol after loss of a proton."""

from wikichem import Scheme

P = [(-1.95, -0.4), (-0.65, -0.4), (0.0, 0.35), (1.3, 0.35), (1.95, -0.4)]  # Cl, C1, C2, C3, C4
s = Scheme()
cr = s.molecule("[Cl:5][CH2:1][CH:2]=[CH:3][CH3:4]", coords=P, lone_pairs=[5])
s.curly(cr.bond(1, 5), cr.atom(5), bend=0.8)
s.text((0, -1.4), "1-chloro-2-butene", size=10)
s.arrow((2.6, 0), (3.8, 0), below=r"$-$Cl$^-$")
Q = [(x + 6.0, y) for x, y in P[1:]]
c1 = s.molecule("[CH2+:1][CH:2]=[CH:3][CH3:4]", coords=Q)
s.curly(c1.bond(2, 3), c1.bond(1, 2), bend=0.7)
s.arrow((8.4, 0), (9.6, 0), kind="resonance")
s.molecule("[CH2:1]=[CH:2][CH+:3][CH3:4]", coords=[(x + 5.0, y) for x, y in Q])
s.draw()

s = Scheme()
s.text((0, 0.6), r"H$_2$O at C1")
s.arrow((-1.0, 0.1), (1.0, 0.1))
s.molecule("OC/C=C/C", at=(3.3, 0.1))
s.text((3.0, -1.0), "2-buten-1-ol", size=10)
s.text((6.6, 0.6), r"H$_2$O at C3")
s.arrow((5.6, 0.1), (7.6, 0.1))
s.molecule("C=CC(C)O", at=(9.6, 0.1))
s.text((9.2, -1.0), "3-buten-2-ol", size=10)
s.draw()
