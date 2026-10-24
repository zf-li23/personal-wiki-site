"""Neighbouring-group participation in sulfur mustard. The sulfur lone pair displaces chloride
intramolecularly (an intramolecular SN2) to form a strained three-membered episulfonium (thiiranium)
ion; water, or N7 of guanine in DNA, then opens the ring at carbon. The second arm reacts in the same
way, so the mustard can cross-link two DNA strands."""

from wikichem import Scheme

s = Scheme()
# Cl-CH2-CH2-S-CH2-CH2-Cl with the S lone pair facing the back of the C-Cl bond
m = s.molecule("[Cl:1][CH2:2][CH2:3][S:4][CH2:5][CH2:6]Cl",
               coords=[(1.3, -0.6), (0.0, 0.0), (-0.65, 1.15), (-1.95, 0.6), (-3.1, 1.3), (-4.3, 0.7), (-5.5, 1.3)], lone_pairs=[1, 4])
s.curly(m.atom(4), m.atom(2), bend=0.6)
s.curly(m.bond(1, 2), m.atom(1), bend=-0.8)
s.arrow((2.2, 0.4), (3.6, 0.4), below=r"$-$Cl$^-$")
ep = s.molecule("C1C[S+]1CCCl", at=(5.6, 0.4))
w = s.molecule("O", at=(4.6, -1.6), lone_pairs=True)
s.curly(w.atom(0), ep.atom(0), bend=0.3)
s.curly(ep.bond(0, 2), ep.atom(2), bend=0.8)
s.text((5.6, 1.9), "episulfonium ion", size=10)
s.arrow((7.9, 0.4), (9.3, 0.4), below=r"$-$H$^+$")
s.molecule("OCCSCCCl", at=(12.5, 0.4))
s.draw()
