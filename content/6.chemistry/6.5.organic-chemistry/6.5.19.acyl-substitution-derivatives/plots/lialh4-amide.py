"""Reduction of a tertiary amide (N,N-dimethylacetamide) to an amine by LiAlH4. Hydride adds to the
carbonyl carbon. In the tetrahedral intermediate the nitrogen lone pair, a better donor than the
oxygen bound to aluminium, pushes out the O-Al group, so an iminium ion forms rather than an
aldehyde. A second hydride adds to the iminium ion and gives the amine: the C=O has become CH2."""

from wikichem import Scheme

s = Scheme()
y = -1.9  # caption line
al = s.molecule("[AlH4-]", at=(-1.8, 1.4), show_h=[0])
am = s.molecule("CC(=O)N(C)C", at=(0, 0), lone_pairs=[2])
s.curly(al.bond(0, 4), am.atom(1), bend=0.4)
s.curly(am.bond(1, 2), am.atom(2), bend=-0.8)
s.text((-0.3, y), "N,N-dimethylacetamide")
s.arrow((1.7, 0), (3.1, 0))
ti = s.molecule("CC(O[AlH3-])N(C)C", at=(5.3, 0), lone_pairs=[4])
s.curly(ti.atom(4), ti.bond(1, 4), bend=0.7)
s.curly(ti.bond(1, 2), ti.atom(2), bend=-0.7)
s.text((5.3, y), "tetrahedral intermediate")
s.arrow((7.2, 0), (8.8, 0), below=r"$-\,[\mathrm{OAlH_3}]^{2-}$")
s.molecule("CC=[N+](C)C", at=(10.2, 0))
s.text((10.2, y), "iminium ion")
s.arrow((11.5, 0), (12.9, 0), above=r"H$^-$")
s.molecule("CCN(C)C", at=(14.4, 0))
s.text((14.4, y), "N,N-dimethylethylamine")
s.draw()
