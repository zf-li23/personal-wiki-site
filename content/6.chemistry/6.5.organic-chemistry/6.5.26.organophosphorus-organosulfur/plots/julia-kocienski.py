"""Julia-Kocienski olefination after the addition of the PT sulfone anion to the aldehyde (PT =
1-phenyl-1H-tetrazol-5-yl; R and R' are the groups from the sulfone and the aldehyde). Top: the
beta-alkoxide attacks the ipso carbon of the tetrazole (intramolecular nucleophilic aromatic
substitution through a spirocyclic Meisenheimer-type intermediate, not drawn) and the C-S bond
breaks: the Smiles rearrangement moves the heteroaryl group from sulfur to oxygen and gives a
sulfinate. Bottom: the sulfinate loses SO2 and the tetrazolyloxide in an anti elimination,
giving the (E)-alkene (the anti relationship is set in the addition step)."""

import math

from wikichem import Scheme

s = Scheme()
c8 = (1.9, 1.2)
cen = (c8[0], c8[1] + 0.85)
pent = [(cen[0] + 0.85 * math.cos(math.radians(a)), cen[1] + 0.85 * math.sin(math.radians(a))) for a in (-90, -18, 54, 126, 198)]
ph = (cen[0] + 1.85 * math.cos(math.radians(198)), cen[1] + 1.85 * math.sin(math.radians(198)))
m = s.molecule("[O-]C(*)C(*)S(=O)(=O)C1=NN=NN1*",
               coords=[(0.5, 1.0), (0, 0), (-1.0, 0), (1.0, -0.4), (1.0, -1.4), (1.9, 0.2), (2.9, 0.2), (2.3, -0.7)] + pent + [ph],
               lone_pairs=[0], labels={2: "R'", 4: "R", 13: "Ph"})
s.curly(m.atom(0), m.atom(8), bend=-0.5)
s.curly(m.bond(5, 8), m.atom(5), bend=-0.6)
s.arrow((4.0, 0.6), (5.6, 0.6), above="Smiles")
x = 8.2
SF = [(-1.0, 1.0), (-0.5, 0.13), (-1.4, -0.4), (0.5, 0.13), (0.5, 1.13), (1.0, -0.73), (1.0, -1.73), (2.0, -0.73), (2.8, -0.13)]
s.molecule("[O-]S(=O)C(*)C(*)O*", coords=SF, at=(x, 0.6), labels={4: "R", 6: "R'", 8: "PT"})

y = -4.4
sf = s.molecule("[O-]S(=O)C(*)C(*)O*", coords=SF, at=(0, y), lone_pairs=[0], labels={4: "R", 6: "R'", 8: "PT"})
s.curly(sf.atom(0), sf.bond(0, 1), bend=-0.7)
s.curly(sf.bond(1, 3), sf.bond(3, 5), bend=0.6)
s.curly(sf.bond(5, 7), sf.atom(7), bend=0.6)
s.arrow((3.4, y), (4.8, y), above="anti")
x = 6.4
s.molecule("*/C=C/*", at=(x, y), labels={0: "R", 3: "R'"})
s.plus((x + 2.0, y))
s.molecule("O=S=O", at=(x + 3.6, y))
s.plus((x + 5.2, y))
s.molecule("*[O-]", coords=[(0, 0), (1.0, 0)], at=(x + 6.4, y), labels={0: "PT"})
s.draw()
