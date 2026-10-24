"""Thiol-disulfide exchange: a thiolate attacks one sulfur atom of a disulfide along the S-S axis
(an SN2 reaction at sulfur) and the other sulfur leaves as a thiolate. In cells the attacking
thiolate is often glutathione or a cysteine of a protein; R and R' stand for these groups."""

from wikichem import Scheme

s = Scheme()
rs = s.molecule("*[S-]", coords=[(-1.0, 0), (0, 0)], lone_pairs=[1], labels={0: "R"})
dis = s.molecule("*SS*", coords=[(1.5, 0.5), (2.2, -0.2), (3.2, -0.2), (3.9, -0.9)], lone_pairs=[], labels={0: "R'", 3: "R'"})
s.curly(rs.atom(1), dis.atom(1), bend=-0.5)
s.curly(dis.bond(1, 2), dis.atom(2), bend=-0.6)
s.arrow((4.8, 0), (6.2, 0), kind="equilibrium")
s.molecule("*SS*", coords=[(-1.0, 0.5), (-0.3, -0.2), (0.7, -0.2), (1.4, -0.9)], at=(7.6, 0), labels={0: "R", 3: "R'"})
s.plus((10.2, 0))
s.molecule("*[S-]", coords=[(-0.5, 0), (0.5, 0)], at=(11.4, 0), lone_pairs=[1], labels={0: "R'"})
s.draw()
