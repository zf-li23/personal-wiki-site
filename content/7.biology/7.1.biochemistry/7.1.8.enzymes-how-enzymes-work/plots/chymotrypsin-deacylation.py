"""Deacylation of the acyl-enzyme in a serine protease (chymotrypsin), the second half of the
mechanism (the first half, acylation, is drawn in 6.5.33). His57, now unprotonated, acts as a
general base and takes a proton from a water molecule; the hydroxide-like oxygen adds to the ester
carbonyl carbon of the acyl-Ser195 intermediate, and the C=O pi electrons move onto oxygen. The
second tetrahedral intermediate carries an oxyanion held by the oxyanion hole; its collapse (His57
then acting as a general acid) releases the carboxylic acid product and regenerates Ser195."""

from wikichem import Scheme

s = Scheme()
asp = s.molecule("*C(=O)[O-]", at=(-4.6, 0.0), labels={0: "Asp"}, rotate=0)
his = s.molecule("*c1cnc[nH]1", at=(-1.8, 0.0), labels={0: "His"}, lone_pairs=[3], rotate=-90)
wat = s.molecule("O", at=(0.9, 1.1), explicit_h=False, show_h=[0], lone_pairs=[0])
acyl = s.molecule("*C(=O)OC*", at=(3.4, -0.6), labels={0: "R", 5: "Ser"}, lone_pairs=[2])
s.partial(asp.atom(3), his.atom(5))
s.curly(his.atom(3), wat.h(0, 1), bend=-0.3)
s.curly(wat.bond(0, 2), wat.atom(0), bend=0.6)
s.curly(wat.atom(0), acyl.atom(1), bend=-0.4)
s.curly(acyl.bond(1, 2), acyl.atom(2), bend=0.6)
s.text((3.4, -2.4), "acyl-enzyme (ester)")
s.text((-3.2, -2.4), "catalytic triad")
s.arrow((5.6, -0.4), (7.0, -0.4))
s.molecule("*C([O-])(O)OC*", at=(8.8, -0.4), labels={0: "R", 6: "Ser"})
s.text((8.8, -2.4), "second tetrahedral intermediate\n(oxyanion hole)")
s.draw()
