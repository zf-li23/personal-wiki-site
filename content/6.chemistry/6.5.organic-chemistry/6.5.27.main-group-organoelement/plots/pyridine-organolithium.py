"""Addition of phenyllithium to pyridine (Ziegler). Top: the C-Li electrons add to C2, next to the
nitrogen, and the C=N electrons go to nitrogen, giving the lithium salt of a 1,2-dihydropyridine
(lithium coordinated to the amide nitrogen). Bottom: on heating, the nitrogen lone pair re-forms
the C=N bond and the C2-H bond breaks with the hydrogen leaving as hydride (as LiH), restoring
the aromatic ring: 2-phenylpyridine. The second step is the same as in the Chichibabin reaction."""

from wikichem import Scheme

s = Scheme()
HEX = [(0, 1.0), (0.87, 0.5), (0.87, -0.5), (0, -1.0), (-0.87, -0.5), (-0.87, 0.5)]
py = s.molecule("n1ccccc1", coords=HEX, lone_pairs=[0])
pl = s.molecule("[Li]c1ccccc1", at=(3.2, 1.6), rotate=0)
s.curly(pl.bond(0, 1), py.atom(1), bend=0.5)
s.curly(py.bond(0, 1), py.atom(0), bend=-0.6)
s.arrow((5.0, 0), (6.4, 0))
x = 8.4
s.molecule("[Li]N1C([H])(c2ccccc2)C=CC=C1", coords=[(0, 2.0), HEX[0], HEX[1], (1.6, 1.2)] + [(1.87, 0.0), (2.87, 0.0), (3.37, -0.87), (2.87, -1.73), (1.87, -1.73), (1.37, -0.87)] + HEX[2:],
           at=(x, 0))

y = -5.0
d = s.molecule("[Li]N1C([H])(c2ccccc2)C=CC=C1", coords=[(0, 2.0), HEX[0], HEX[1], (1.6, 1.2)] + [(1.87, 0.0), (2.87, 0.0), (3.37, -0.87), (2.87, -1.73), (1.87, -1.73), (1.37, -0.87)] + HEX[2:],
               at=(0, y), lone_pairs=[1])
s.curly(d.atom(1), d.bond(1, 2), bend=-0.6)
s.curly(d.bond(2, 3), d.atom(3), bend=0.6)
s.arrow((4.0, y), (5.4, y), above="heat", below="$-$LiH")
s.molecule("c1ccc(nc1)-c1ccccc1", at=(7.6, y))
s.draw()
