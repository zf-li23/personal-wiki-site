"""Kiliani-Fischer chain extension, drawn on the top two carbons of an aldose (R = the rest of the
chain). Top: cyanide adds to the planar aldehyde from either face, so the old C1 becomes a new
stereocentre and two C2-epimeric cyanohydrins form (in unequal amounts). Bottom, the modern
variant: hydrogenation over poisoned Pd/BaSO4 stops at the imine, which is hydrolysed to the
aldehyde of the aldose with one more carbon (classically: hydrolysis to the aldonic acid,
lactonization and reduction of the lactone with sodium amalgam)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("*[C@@H](O)C=O", at=(0.0, y), labels={0: "R"}, lone_pairs=[4])
cn = s.molecule("[C-]#N", at=(1.8, y + 1.8))
s.curly(cn.atom(0), a.atom(3), bend=0.4)
s.curly(a.bond(3, 4), a.atom(4), bend=-0.6)
s.text((0.0, y - 1.9), "aldose (top carbons)")
s.arrow((2.6, y), (4.0, y), above=r"HCN / CN$^-$", below=r"then H$^+$")
s.molecule("*[C@@H](O)[C@H](O)C#N", at=(6.2, y + 1.3), labels={0: "R"})
s.molecule("*[C@@H](O)[C@@H](O)C#N", at=(6.2, y - 1.6), labels={0: "R"})
s.text((9.2, y), "two C2 epimers")
y2 = -5.2
s.molecule("*[C@@H](O)[C@H](O)C#N", at=(0.0, y2), labels={0: "R"})
s.arrow((2.0, y2), (3.8, y2), above=r"H$_2$", below=r"Pd/BaSO$_4$")
s.molecule("*[C@@H](O)[C@H](O)C=N", at=(5.8, y2), labels={0: "R"})
s.text((5.8, y2 - 1.9), "imine")
s.arrow((7.8, y2), (9.2, y2), above=r"H$_2$O", below=r"$-$NH$_3$")
s.molecule("*[C@@H](O)[C@H](O)C=O", at=(11.2, y2), labels={0: "R"})
s.text((11.2, y2 - 1.9), "aldose + 1 C")
s.draw()
