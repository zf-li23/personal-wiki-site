"""Activation of DMSO in the Swern oxidation (the steps before those drawn in 26.9.2). Top: the
oxygen of DMSO adds to a carbonyl carbon of oxalyl chloride; the tetrahedral intermediate (not
drawn) expels chloride, giving an acyloxysulfonium ion. Middle: chloride attacks sulfur and the
S-O bond breaks, releasing the chlorooxalate anion and the chlorodimethylsulfonium ion, the
species that reacts with the alcohol. Bottom: the chlorooxalate anion fragments: the oxygen anion
forms carbon dioxide, the C-C electrons stay on the other carbon, its oxygen lone pair completes
the triple bond of carbon monoxide and chloride leaves. Two gases form, which is why the
activation is strongly exothermic and is done at -78 C."""

from wikichem import Scheme

s = Scheme()
dmso = s.molecule("C[S+](C)[O-]", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0)], lone_pairs=[3])
ox = s.molecule("O=C(Cl)C(=O)Cl", coords=[(2.6, 1.2), (2.6, 0.2), (3.5, -0.3), (2.1, -0.67), (1.1, -0.67), (2.6, -1.53)],
                lone_pairs=[0])
s.curly(dmso.atom(3), ox.atom(1), bend=-0.5)
s.curly(ox.bond(0, 1), ox.atom(0), bend=-0.6)
s.arrow((4.4, 0), (6.0, 0), above="$-$Cl$^-$")
x = 7.6
s.molecule("C[S+](C)OC(=O)C(=O)Cl", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87),
                                            (3.0, 0.0), (3.0, 1.73)], at=(x, 0))

y = -4.4
ac = s.molecule("C[S+](C)OC(=O)C(=O)Cl", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87),
                                                 (3.0, 0.0), (3.0, 1.73)], at=(1.4, y))
cl = s.molecule("[Cl-]", at=(-0.4, y - 1.6), lone_pairs=True)
s.curly(cl.atom(0), ac.atom(1), bend=-0.4)
s.curly(ac.bond(1, 3), ac.atom(3), bend=0.6)
s.arrow((5.4, y), (6.8, y))
x = 8.4
s.molecule("C[S+](C)Cl", coords=[(-0.5, 0.87), (0, 0), (-0.5, -0.87), (1.0, 0)], at=(x, y))
s.plus((x + 2.0, y))
s.molecule("[O-]C(=O)C(=O)Cl", coords=[(0, 0), (0.5, 0.87), (0, 1.73), (1.5, 0.87), (2.0, 0.0), (2.0, 1.73)], at=(x + 3.0, y - 0.4))

y2 = -9.0
fr = s.molecule("[O-]C(=O)C(=O)Cl", coords=[(0, 0), (0.5, 0.87), (0, 1.73), (1.7, 0.87), (2.2, 0.0), (2.2, 1.73)],
                at=(0.2, y2 - 0.4), lone_pairs=[0, 4])
s.curly(fr.atom(0), fr.bond(0, 1), bend=0.7)
s.curly(fr.bond(1, 3), fr.atom(3), bend=0.6)
s.curly(fr.atom(4), fr.bond(3, 4), bend=-0.7)
s.curly(fr.bond(3, 5), fr.atom(5), bend=-0.6)
s.arrow((3.4, y2), (4.8, y2))
s.molecule("O=C=O", at=(6.4, y2), show_carbons=[1])
s.plus((8.2, y2))
s.molecule("[C-]#[O+]", at=(9.3, y2), show_carbons=[0])
s.plus((10.6, y2))
s.molecule("[Cl-]", at=(11.5, y2))
s.draw()
