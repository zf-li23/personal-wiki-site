"""Why RNA hydrolyses much faster than DNA: in base the 2'-oxygen of ribose attacks the
neighbouring 3'-phosphodiester phosphorus in line with the P-O5' bond (through a trigonal
bipyramidal, pentacoordinate transition state), the 5'-oxygen of the next nucleotide leaves, and a
2',3'-cyclic phosphate forms. DNA lacks the 2'-OH. B is the nucleobase; R stands for the 5'-end of
the strand and R' for the next nucleoside."""

from wikichem import Scheme

s = Scheme()
rna = s.molecule("*OC[C@H]1O[C@@H](*)[C@H]([O-])[C@@H]1OP(=O)([O-])O*", at=(0, 0), lone_pairs=[8],
                 labels={0: "R", 6: "B", 15: "R'"})
s.curly(rna.atom(8), rna.atom(11), bend=-0.5)
s.curly(rna.bond(11, 14), rna.atom(14), bend=-0.6)
s.arrow((3.4, 0), (4.8, 0))
s.molecule("*OC[C@H]1O[C@@H](*)[C@@H]2OP(=O)([O-])O[C@H]12", at=(7.6, 0), labels={0: "R", 6: "B"})
s.plus((10.4, 0))
s.molecule("[O-]*", at=(11.6, 0), labels={1: "R'"})
s.draw()
