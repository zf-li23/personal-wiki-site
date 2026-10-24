"""Base-catalysed cleavage of RNA. The 2'-hydroxyl, deprotonated in base, attacks the neighbouring
3'-phosphodiester phosphorus intramolecularly (through a trigonal-bipyramidal, pentacoordinate
phosphorane); the 5'-oxygen of the next nucleotide leaves in line, giving a 2',3'-cyclic phosphate
and breaking the chain (B = base, R and R' the rest of the chain). DNA, without a 2'-OH, cannot
react this way. Ribonuclease A uses the same mechanism with two histidines as acid and base."""

from wikichem import Scheme

s = Scheme()
y = 0.0
r = s.molecule("*[C@@H]1O[C@H](CO*)[C@@H](OP(=O)([O-])O*)[C@H]1[O-]", at=(0.0, y),
               labels={0: "B", 6: "R", 13: "R$'$"}, lone_pairs=[15])
s.curly(r.atom(15), r.atom(9), bend=0.6)
s.curly(r.bond(9, 12), r.atom(12), bend=-0.6)
s.text((0.0, y - 3.0), "2'-alkoxide of RNA")
s.arrow((3.2, y), (4.8, y), above="via P(V)", below="pentacoordinate")
s.molecule("*[C@@H]1O[C@H](CO*)[C@H]2OP(=O)([O-])O[C@@H]12", at=(7.4, y), labels={0: "B", 6: "R"})
s.text((7.4, y - 3.0), "2',3'-cyclic phosphate")
s.plus((9.8, y))
s.molecule("[O-]*", at=(10.8, y), labels={1: "R$'$"})
s.text((10.8, y - 3.0), "5'-alkoxide")
s.draw()
