"""A Grignard reagent adds twice to an ester. Methylmagnesium bromide adds to the carbonyl carbon of
methyl acetate; the tetrahedral alkoxide collapses, re-forming C=O and expelling methoxide, which
gives acetone. The ketone is more reactive than the ester, so it immediately takes up a second
equivalent of the reagent; acid work-up gives the tertiary alcohol 2-methylpropan-2-ol."""

from wikichem import Scheme

s = Scheme()
y = 0.0
g = s.molecule("C[Mg]Br", at=(-0.6, y + 0.4))
es = s.molecule("CC(=O)OC", at=(2.2, y), rotate=-90, lone_pairs=[2])
s.curly(g.bond(0, 1), es.atom(1), bend=0.5)
s.curly(es.bond(1, 2), es.atom(2), bend=0.9)
s.arrow((3.8, y), (5.2, y))
t = s.molecule("CC(C)([O-])OC", at=(6.6, y), lone_pairs=[3])
s.curly(t.atom(3), t.bond(1, 3), bend=0.8)
s.curly(t.bond(1, 4), t.atom(4), bend=0.8)
s.text((6.6, y - 1.8), "tetrahedral intermediate")
s.arrow((8.2, y), (9.6, y), below=r"$-$CH$_3$OMgBr")
s.molecule("CC(=O)C", at=(10.8, y))

y = -3.8
g2 = s.molecule("C[Mg]Br", at=(-0.6, y + 0.4))
k = s.molecule("CC(=O)C", at=(2.2, y), rotate=-90, lone_pairs=[2])
s.curly(g2.bond(0, 1), k.atom(1), bend=0.5)
s.curly(k.bond(1, 2), k.atom(2), bend=0.9)
s.arrow((3.8, y), (5.2, y))
s.molecule("CC(C)(C)[O-]", at=(6.6, y))
s.arrow((8.2, y), (9.6, y), above=r"H$_3$O$^+$")
s.molecule("CC(C)(C)O", at=(10.8, y))
s.draw()
