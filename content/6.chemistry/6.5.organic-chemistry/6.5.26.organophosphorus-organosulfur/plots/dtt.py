"""Reduction of a disulfide RS-SR by dithiothreitol (DTT). Top: a thiolate of DTT attacks one
sulfur of the disulfide (thiol-disulfide exchange, SN2 at sulfur) and RS- leaves, giving a mixed
disulfide. Bottom: the second thiolate of DTT attacks the sulfur bonded to its own chain; the ring
closes to the six-membered cyclic disulfide (trans-4,5-dihydroxy-1,2-dithiane) and a second RS-
is released. Because the intramolecular step is so favourable, DTT drives the reduction to
completion."""

from wikichem import Scheme

s = Scheme()
D = [(0, 0), (0.87, 0.5), (1.73, 0), (1.73, -1.0), (2.6, 0.5), (2.6, 1.5), (3.46, 0), (4.33, 0.5)]
dtt = s.molecule("[S-]CC(O)C(O)CS", coords=D, lone_pairs=[0])
rss = s.molecule("*SS*", coords=[(-2.6, 0.9), (-1.9, 0.2), (-1.9, -0.8), (-2.6, -1.5)], lone_pairs=[], labels={0: "R", 3: "R"})
s.curly(dtt.atom(0), rss.atom(1), bend=0.5)
s.curly(rss.bond(1, 2), rss.atom(2), bend=-0.6)
s.arrow((5.2, 0), (6.6, 0))
x = 8.4
s.molecule("*SSCC(O)C(O)CS", coords=[(-1.4, 0.5), (-0.7, -0.2)] + D, at=(x, 0), labels={0: "R"})
s.plus((x + 5.2, 0))
s.molecule("*[S-]", coords=[(0, 0), (1.0, 0)], at=(x + 6.4, 0), labels={0: "R"}, lone_pairs=[1])

y = -5.0
# chain curled into an open hexagon: S(a)-C-C-C-C-S(b)-S-R with S(a) as thiolate
hexa = [(-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -0.5), (0.87, 0.5), (0, 1.0)]
m = s.molecule("[S-]CC(O)C(O)CSS*",
               coords=[(0, 1.0), (-0.87, 0.5), (-0.87, -0.5), (-1.73, -1.0), (0, -1.0), (0, -2.0), (0.87, -0.5), (0.87, 0.5),
                       (1.87, 1.0), (2.6, 0.3)],
               at=(0, y), lone_pairs=[0], labels={9: "R"})
s.curly(m.atom(0), m.atom(7), bend=-0.6)
s.curly(m.bond(7, 8), m.atom(8), bend=0.6)
s.arrow((3.4, y), (4.8, y), above="$-$RS$^-$")
s.molecule("OC1CSSCC1O", at=(7.0, y))
s.text((7.0, y - 1.9), "cyclic disulfide", size=11)
s.draw()
