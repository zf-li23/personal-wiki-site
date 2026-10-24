"""Heterolytic cleavage of H2 by a frustrated Lewis pair. Tri-tert-butylphosphine and
tris(pentafluorophenyl)borane are too crowded to form a P-B adduct; together they polarize an H2
molecule held between them: the phosphorus lone pair bonds to one hydrogen while the H-H electrons
go into the empty p orbital of boron, giving a phosphonium cation and a hydridoborate anion."""

from wikichem import Scheme

s = Scheme()
p = s.molecule("P(*)(*)*", coords=[(0, 0), (-0.87, 0.6), (-0.87, -0.6), (-0.2, -1.1)], lone_pairs=[0],
               labels={1: "$t$-Bu", 2: "$t$-Bu", 3: "$t$-Bu"})
hh = s.molecule("[H][H]", coords=[(1.4, 0.0), (2.2, 0.0)])
b = s.molecule("B(*)(*)*", coords=[(3.6, 0), (4.6, 0.6), (4.6, -0.6), (3.6, -1.2)],
               labels={1: "C$_6$F$_5$", 2: "C$_6$F$_5$", 3: "C$_6$F$_5$"})
s.curly(p.atom(0), hh.atom(0), bend=-0.6)
s.curly(hh.bond(0, 1), b.atom(0), bend=-0.6)
s.arrow((5.8, 0), (7.2, 0))
x = 9.4
s.molecule("[P+](*)(*)(*)[H]", coords=[(0, 0), (-0.87, 0.6), (-0.87, -0.6), (-0.2, -1.1), (1.0, 0)], at=(x, 0),
           labels={1: "$t$-Bu", 2: "$t$-Bu", 3: "$t$-Bu"})
x2 = x + 3.4
s.molecule("[H][B-](*)(*)*", coords=[(-1.0, 0), (0, 0), (1.0, 0.6), (1.0, -0.6), (0, -1.2)], at=(x2, 0),
           labels={2: "C$_6$F$_5$", 3: "C$_6$F$_5$", 4: "C$_6$F$_5$"})
s.draw()
