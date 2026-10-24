"""Michaelis-Arbuzov reaction of triethyl phosphite with ethyl bromoacetate (two of the ethoxy
groups on phosphorus are written EtO). Top: the phosphorus lone pair displaces bromide in an SN2
reaction, giving an alkoxyphosphonium salt. Bottom: bromide attacks the ethyl carbon of one P-O-Et
group, again by SN2; the C-O electrons become the P=O bond, giving the phosphonate (the reagent
of the Horner-Wadsworth-Emmons reaction) and bromoethane."""

from wikichem import Scheme

s = Scheme()
EO = {1: "EtO", 2: "EtO"}
p = s.molecule("P(*)(*)OCC", coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -1.5), (0.87, -2.5)],
               lone_pairs=[0], labels=EO)
bro = s.molecule("BrCC(=O)OCC", coords=[(3.6, 0), (2.6, 0), (2.1, 0.87), (1.1, 0.87), (2.6, 1.73), (2.1, 2.6), (2.6, 3.46)],
                 lone_pairs=[])
s.curly(p.atom(0), bro.atom(1), bend=-0.4)
s.curly(bro.bond(0, 1), bro.atom(0), bend=-0.6)
s.arrow((4.6, 0), (6.0, 0), above="SN2")
x = 8.4
ph = s.molecule("[P+](*)(*)(OCC)CC(=O)OCC",
                coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -1.5), (0.87, -2.5),
                        (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87), (3.0, 1.73), (4.0, 1.73)],
                at=(x, 0), labels=EO)
br = s.molecule("[Br-]", at=(x + 2.4, -1.6), lone_pairs=True)

y = -5.0
ph2 = s.molecule("[P+](*)(*)(OCC)CC(=O)OCC",
                 coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -1.5), (0.87, -2.5),
                         (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87), (3.0, 1.73), (4.0, 1.73)],
                 at=(0, y), labels=EO)
br2 = s.molecule("[Br-]", at=(2.6, y - 1.5), lone_pairs=True)
s.curly(br2.atom(0), ph2.atom(4), bend=-0.4)
s.curly(ph2.bond(3, 4), ph2.atom(3), bend=-0.6)
s.arrow((4.8, y), (6.2, y), above="SN2")
s.molecule("O=P(*)(*)CC(=O)OCC",
           coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87), (3.0, 1.73), (4.0, 1.73)],
           at=(8.6, y), labels={2: "EtO", 3: "EtO"})
s.plus((12.6, y))
s.molecule("CCBr", at=(14.4, y))
s.draw()
