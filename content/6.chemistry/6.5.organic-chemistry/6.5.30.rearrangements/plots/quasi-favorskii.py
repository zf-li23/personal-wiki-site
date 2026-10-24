"""Quasi-Favorskii (semibenzilic) rearrangement of 1-chlorocyclohexyl phenyl ketone, which has no
alpha'-hydrogen and cannot form a cyclopropanone. Hydroxide adds to the carbonyl group; in the
tetrahedral alkoxide the oxygen lone pair re-forms C=O while the phenyl group migrates with its
electron pair to the carbon bearing chlorine and chloride leaves from the back side (a 1,2-shift
like that of a semipinacol rearrangement, with inversion at the migration terminus). Proton transfer
gives 1-phenylcyclohexane-1-carboxylate."""

from wikichem import Scheme

s = Scheme()
y = 0.0
k = s.molecule("O=C(c1ccccc1)C1(Cl)CCCCC1", at=(0.0, y), lone_pairs=[0])
oh = s.molecule("[OH-]", at=(-1.0, y + 2.4), lone_pairs=True)
s.curly(oh.atom(0), k.atom(1), bend=0.4)
s.curly(k.bond(0, 1), k.atom(0), bend=-0.6)
s.arrow((2.6, y), (4.0, y))
t = s.molecule("[O-]C(O)(c1ccccc1)C1(Cl)CCCCC1", at=(6.6, y), lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=0.6)
s.curly(t.bond(1, 3), t.atom(9), bend=-0.6)
s.curly(t.bond(9, 10), t.atom(10), bend=0.6)
s.text((6.6, y - 2.8), "tetrahedral alkoxide")
s.arrow((9.2, y), (10.6, y), above=r"$-$Cl$^-$", below="proton transfer")
s.molecule("[O-]C(=O)C1(c2ccccc2)CCCCC1", at=(13.2, y))
s.text((13.2, y - 2.8), "1-phenylcyclohexanecarboxylate")
s.draw()
