"""Chain extension by two carbons: allylmagnesium chloride (from 3-chloropropene) opens ethylene
oxide. The C-Mg bonding pair attacks a ring CH2 carbon (SN2) and the C-O bond breaks, releasing
the ring strain; the magnesium alkoxide is protonated on work-up to give pent-4-en-1-ol."""

from wikichem import Scheme

s = Scheme()
g = s.molecule("C=CC[Mg]Cl", at=(0, 0))
ep = s.molecule("C1CO1", at=(2.8, -0.4), lone_pairs=[2])
s.curly(g.bond(2, 3), ep.atom(0), bend=0.5)
s.curly(ep.bond(0, 2), ep.atom(2), bend=-0.7)
s.arrow((4.0, 0), (5.4, 0))
s.molecule("C=CCCC[O-]", at=(7.9, 0))
s.text((9.3, -0.9), r"$^+$MgCl", size=11)
s.arrow((10.1, 0), (11.5, 0), above=r"H$_3$O$^+$")
s.molecule("C=CCCCO", at=(13.5, 0))
s.draw()
