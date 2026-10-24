"""Cyclopropanation of cyclohex-2-en-1-one by dimethylsulfoxonium methylide (Corey-Chaykovsky).
Top: the stabilized ylide adds to the beta carbon (conjugate addition; its 1,2-addition to the
carbonyl is reversible), the C=C electrons move toward the carbonyl and the C=O electrons onto
oxygen, giving an enolate. Bottom: the enolate carbon attacks the CH2 group next to sulfur from
the back (intramolecular SN2, a 3-exo-tet ring closure) and DMSO leaves, giving
bicyclo[4.1.0]heptan-2-one."""

from wikichem import Scheme

s = Scheme()
RING = [(-1.73, 1.0), (-0.87, 0.5), (0, 1.0), (0.87, 0.5), (0.87, -0.5), (0, -1.0), (-0.87, -0.5)]
en = s.molecule("O=C1C=CCCC1", coords=RING, lone_pairs=[0])
yl = s.molecule("[CH2-][S+](C)(C)=O", coords=[(2.2, 1.0), (3.2, 1.0), (3.7, 1.87), (3.7, 0.13), (3.2, 2.0)])
s.curly(yl.atom(0), en.atom(3), bend=-0.5)
s.curly(en.bond(2, 3), en.bond(1, 2), bend=0.6)
s.curly(en.bond(0, 1), en.atom(0), bend=0.6)
s.arrow((4.6, 0), (6.0, 0))
x = 8.4
s.molecule("[O-]C1=CC(C*)CCC1", coords=RING[:4] + [(1.6, 1.3), (2.6, 1.3)] + RING[4:], at=(x, 0),
           labels={5: "$^+$S(O)Me$_2$"})
s.text((x - 0.4, -1.8), "enolate", size=11)

y = -4.6
e = s.molecule("[O-]C1=CC(C*)CCC1", coords=RING[:4] + [(0.75, 1.65), (1.5, 2.4)] + RING[4:], at=(0, y),
               labels={5: "$^+$S(O)Me$_2$"}, lone_pairs=[0])
s.curly(e.atom(0), e.bond(0, 1), bend=0.7)
s.curly(e.bond(1, 2), e.bond(2, 4), bend=-0.5)
s.curly(e.bond(4, 5), e.atom(5), bend=-0.6)
s.arrow((2.4, y), (3.8, y), above="$-$DMSO")
s.molecule("O=C1CCCC2CC12", at=(5.6, y))
s.draw()
