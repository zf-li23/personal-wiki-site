"""Perkow reaction of triethyl phosphite with chloroacetone, the alternative to the Arbuzov reaction
for alpha-halo ketones (two of the ethoxy groups on phosphorus written EtO). Top: phosphorus, a
soft nucleophile, adds to the carbonyl carbon instead of displacing chloride; the C=O electrons go
to oxygen. Middle: the alkoxide oxygen bonds to phosphorus while the P-C electrons become the C=C
bond and chloride is expelled, so phosphorus moves from carbon to oxygen and an enol phosphonium
ion forms. Bottom: chloride removes an ethyl group by SN2 (the second step of the Arbuzov reaction),
giving the enol phosphate (diethyl prop-1-en-2-yl phosphate) and chloroethane."""

from wikichem import Scheme

s = Scheme()
EO = {1: "EtO", 2: "EtO"}
P3 = [(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (0.87, -1.5), (0.87, -2.5)]
p = s.molecule("P(*)(*)OCC", coords=P3, lone_pairs=[0], labels=EO)
ket = s.molecule("ClCC(C)=O", coords=[(3.6, -0.6), (3.1, 0.27), (2.1, 0.27), (1.6, 1.13), (1.6, -0.6)], lone_pairs=[4])
s.curly(p.atom(0), ket.atom(2), bend=-0.4)
s.curly(ket.bond(2, 4), ket.atom(4), bend=0.6)
s.arrow((4.4, 0), (5.8, 0))

x = 8.2
z = s.molecule("[P+](*)(*)(OCC)C(C)([O-])CCl",
               coords=P3 + [(1.0, 0), (1.0, 1.0), (0.75, -0.97), (2.0, -0.1), (2.6, -0.9)],
               at=(x, 0.4), labels=EO, lone_pairs=[8])
s.curly(z.atom(8), z.bond(0, 8), bend=-0.5)
s.curly(z.bond(0, 6), z.bond(6, 9), bend=-0.45)
s.curly(z.bond(9, 10), z.atom(10), bend=-0.6)
s.arrow((x + 4.0, 0), (x + 5.4, 0), above="$-$Cl$^-$")

y = -5.0
ep = s.molecule("[P+](*)(*)(OCC)OC(C)=C",
                coords=P3 + [(1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87)], at=(0.6, y), labels=EO)
cl = s.molecule("[Cl-]", at=(2.6, y - 2.2), lone_pairs=True)
s.curly(cl.atom(0), ep.atom(4), bend=-0.4)
s.curly(ep.bond(3, 4), ep.atom(3), bend=-0.6)
s.arrow((4.4, y), (5.8, y), above="SN2")
s.molecule("O=P(*)(*)OC(C)=C", coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (1.0, 0), (1.5, 0.87), (1.0, 1.73), (2.5, 0.87)],
           at=(8.0, y), labels={2: "EtO", 3: "EtO"})
s.plus((11.4, y))
s.molecule("CCCl", at=(12.8, y))
s.draw()
