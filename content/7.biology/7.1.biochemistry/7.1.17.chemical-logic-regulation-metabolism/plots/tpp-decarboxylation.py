"""Thiamine pyrophosphate (TPP) in the decarboxylation of pyruvate (pyruvate decarboxylase).
1: the C-2 carbanion (ylide) of the thiazolium ring adds to the carbonyl carbon of pyruvate.
2: in the adduct the C-COO- bond breaks; the electrons flow into the C2=N+ bond of the thiazolium
ring (electron sink), giving CO2 and the enamine hydroxyethyl-TPP ("active acetaldehyde").
R = (4-amino-2-methylpyrimidin-5-yl)methyl, R' = 2-pyrophosphoethyl."""

from wikichem import Scheme

s = Scheme()
yl = s.molecule("[C-]1=[N+](*)C(C)=C(*)S1", at=(0, 0), labels={2: "R", 6: "R′"}, lone_pairs=[0])
pyr = s.molecule("O=C(C)C(=O)[O-]", coords=[(-0.87, 0.5), (0, 0), (0, -1.0), (0.87, 0.5), (0.87, 1.5), (1.73, 0)],
                 at=(2.6, 0.2), lone_pairs=[0])
s.curly(yl.atom(0), pyr.atom(1), bend=0.4)
s.curly(pyr.bond(0, 1), pyr.atom(0), bend=-0.6)
s.text((0, -1.9), "TPP ylide")
s.text((2.9, -1.9), "pyruvate")
s.arrow((4.9, 0), (6.1, 0), above=r"H$^+$")
add = s.molecule("CC(O)(C(=O)[O-])C1=[N+](*)C(C)=C(*)S1", at=(8.3, 0), labels={8: "R", 12: "R′"})
s.curly(add.bond(1, 3), add.bond(1, 6), bend=-0.9)
s.curly(add.bond(6, 7), add.atom(7), bend=-0.9)
s.text((8.3, -2.3), "adduct")
s.arrow((10.6, 0), (11.9, 0), below=r"$-$CO$_2$")
s.molecule("CC(O)=C1N(*)C(C)=C(*)S1", at=(14.0, 0), labels={5: "R", 9: "R′"})
s.text((14.0, -2.3), "hydroxyethyl-TPP (enamine)")
s.draw()
