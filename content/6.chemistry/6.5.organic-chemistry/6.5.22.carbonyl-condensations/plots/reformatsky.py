"""Reformatsky reaction. Zinc inserts into the C-Br bond of ethyl bromoacetate, giving a zinc
enolate (the Reformatsky reagent, drawn O-bound). The enolate adds to acetone through a
six-membered cyclic transition state: the ketone oxygen binds zinc, the C=C pi bond attacks the
carbonyl carbon and the O-Zn bond electrons re-form the ester C=O. Hydrolysis gives the
beta-hydroxy ester."""

import math

from wikichem import Scheme

s = Scheme()
s.molecule("CCOC(=O)CBr", at=(-7.4, 0))
s.arrow((-5.2, 0), (-3.6, 0), above="Zn", below="ether")

R = 1.25
hexagon = [(R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for a in (150, 210, 270, 330, 30, 90)]
zn, oen, cest, calpha, ccarb, oket = hexagon
# zinc enolate, SMILES order: Br, Zn, O, C(ester), O(ethoxy), CH2, CH3, =CH2
enol = s.molecule(
    "Br[Zn]OC(OCC)=C",
    coords=[(zn[0] - 0.9, zn[1] + 0.6), zn, oen, cest, (cest[0] - 0.9, cest[1] - 0.55), (cest[0] - 1.8, cest[1]), (cest[0] - 2.7, cest[1] - 0.55), calpha],
    at=(0, 0),
)
# acetone, SMILES order: CH3, C=O carbon, CH3, O
ket = s.molecule("CC(C)=O", coords=[(ccarb[0] + 0.9, ccarb[1] + 0.55), ccarb, (ccarb[0] + 0.9, ccarb[1] - 0.6), oket], at=(0, 0), lone_pairs=[3])
s.partial(enol.atom(7), ket.atom(1))
s.partial(ket.atom(3), enol.atom(1))
s.curly(enol.bond(3, 7), ket.atom(1), bend=0.5)
s.curly(ket.bond(1, 3), ket.atom(3), bend=0.6)
s.curly(enol.bond(1, 2), enol.bond(2, 3), bend=0.6)
s.text((0, -2.3), "cyclic transition state")
s.arrow((2.8, 0), (4.2, 0), above=r"H$_3$O$^+$")
s.molecule("CCOC(=O)CC(C)(C)O", at=(6.2, 0))
s.text((6.2, -1.8), "beta-hydroxy ester")
s.draw()
