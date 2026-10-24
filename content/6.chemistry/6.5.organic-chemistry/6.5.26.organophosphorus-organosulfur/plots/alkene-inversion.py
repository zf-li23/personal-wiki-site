"""Inversion of alkene configuration through phosphorus (Vedejs and Fuchs), starting from the
epoxide of (Z)-but-2-ene (phenyl groups on phosphorus written Ph). Top: diphenylphosphide opens
the cis-epoxide by SN2 at one carbon (inversion there), giving a beta-oxido phosphine; methyl
iodide then quaternizes phosphorus, giving the betaine. Bottom: the alkoxide attacks phosphorus
(oxaphosphetane, as in the Wittig reaction) and the four-membered ring breaks in a syn
elimination. One inversion (anti opening) followed by a syn elimination swaps the two groups on
one carbon: the product is (E)-but-2-ene, together with methyldiphenylphosphine oxide."""

from wikichem import Scheme

s = Scheme()
pp = s.molecule("[P-](*)*", coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5)], lone_pairs=[0], labels={1: "Ph", 2: "Ph"})
ep = s.molecule("C[C@H]1[C@@H](C)O1", coords=[(1.4, -1.0), (1.9, -0.13), (2.9, -0.13), (3.4, -1.0), (2.4, 0.74)], lone_pairs=[])
s.curly(pp.atom(0), ep.atom(1), bend=0.4)
s.curly(ep.bond(1, 4), ep.atom(4), bend=-0.6)
s.text((2.4, -2.0), "cis-epoxide", size=11)
s.arrow((4.0, 0), (5.4, 0), above="SN2")
x = 7.4
BO = [(0, 0), (0.87, 0.5), (0.87, 1.5), (0.0, 2.0), (1.73, 2.0), (1.73, 0.0), (2.6, 0.5), (1.73, -1.0)]
s.molecule("C[C@@H](P(*)*)[C@@H](C)[O-]", coords=BO, at=(x, -0.5), labels={3: "Ph", 4: "Ph"})
s.arrow((x + 3.4, 0), (x + 4.8, 0), above="CH$_3$I")
x2 = x + 6.6
BT = [(0, 0), (0.87, 0.5), (0.87, 1.5), (0.87, 2.5), (-0.1, 1.9), (1.84, 1.9), (1.73, 0.0), (2.6, 0.5), (1.73, -1.0)]
s.molecule("C[C@@H]([P+](C)(*)*)[C@@H](C)[O-]", coords=BT, at=(x2, -0.5), labels={4: "Ph", 5: "Ph"})
s.text((x2 + 1.3, -2.6), "betaine", size=11)

y = -5.6
# the betaine turned so that O- and P+ are syn, then the oxaphosphetane
b = s.molecule("C[C@@H]([P+](C)(*)*)[C@@H](C)[O-]",
               coords=[(-0.9, 0.5), (0, 0), (0, 1.1), (-0.7, 1.9), (0.0, 2.2), (0.9, 1.7), (1.1, 0), (2.0, 0.5), (1.1, 1.1)],
               at=(0, y), labels={4: "Ph", 5: "Ph"}, lone_pairs=[8])
s.curly(b.atom(8), b.atom(2), bend=0.5)
s.arrow((2.4, y + 0.4), (3.8, y + 0.4))
ox = s.molecule("C[C@@H]1[C@@H](C)O[P]1(C)(*)*",
                coords=[(-0.9, 0.5), (0, 0), (1.1, 0), (2.0, 0.5), (1.1, 1.1), (0, 1.1), (-0.7, 1.8), (0.0, 2.2), (0.8, 2.0)],
                at=(5.0, y), labels={7: "Ph", 8: "Ph"})
s.curly(ox.bond(1, 5), ox.bond(1, 2), bend=0.35)
s.curly(ox.bond(2, 4), ox.bond(4, 5), bend=0.35)
s.text((5.6, y - 1.2), "oxaphosphetane", size=11)
s.arrow((7.6, y + 0.4), (9.0, y + 0.4), above="syn")
s.molecule("C/C=C/C", at=(10.6, y + 0.4))
s.plus((12.2, y + 0.4))
s.molecule("O=P(C)(*)*", coords=[(-1.0, 0), (0, 0), (0.5, 0.87), (1.0, 0), (0.5, -0.87)], at=(14.0, y + 0.4),
           labels={3: "Ph", 4: "Ph"})
s.draw()
