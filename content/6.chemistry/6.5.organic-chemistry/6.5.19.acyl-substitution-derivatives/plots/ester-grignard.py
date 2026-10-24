"""Reaction of an ester with two equivalents of a Grignard reagent (methyl acetate and
methylmagnesium bromide). The C-Mg bond adds to the carbonyl carbon; the magnesium alkoxide
(tetrahedral intermediate) expels methoxide and gives a ketone, which is more electrophilic than the
ester and is attacked by the second equivalent at once. Acidic work-up gives the tertiary alcohol."""

from wikichem import Scheme

s = Scheme()
y = -1.9  # caption line
g = s.molecule("C[Mg]Br", at=(-1.4, 1.5))
ester = s.molecule("CC(=O)OC", at=(0, 0), lone_pairs=[2])
s.curly(g.bond(0, 1), ester.atom(1), bend=0.4)
s.curly(ester.bond(1, 2), ester.atom(2), bend=-0.8)
s.text((0, y), "methyl acetate")
s.arrow((1.8, 0), (3.4, 0))
ti = s.molecule("CC(C)([O-])OC", at=(5.4, 0), lone_pairs=[3])
s.curly(ti.atom(3), ti.bond(1, 3), bend=0.7)
s.curly(ti.bond(1, 4), ti.atom(4), bend=-0.6)
s.text((5.4, y), "tetrahedral intermediate")
s.arrow((7.3, 0), (8.9, 0), below=r"$-\mathrm{MeOMgBr}$")
s.molecule("CC(C)=O", at=(10.0, 0))
s.text((10.0, y), "acetone")
s.arrow((11.1, 0), (12.7, 0), above="1. MeMgBr", below=r"2. H$_3$O$^+$")
s.molecule("CC(C)(C)O", at=(13.9, 0))
s.text((13.9, y), "tert-butanol")
s.draw()
