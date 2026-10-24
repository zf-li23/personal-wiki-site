"""Formation of the Mannich electrophile from dimethylamine and formaldehyde. Top: the nitrogen lone
pair adds to the carbonyl carbon and the C=O electrons move onto oxygen; proton transfer from N to O
gives the hemiaminal. Bottom: in weak acid the OH is protonated; the nitrogen lone pair forms the
C=N double bond and pushes out water, giving the dimethylmethyleneammonium ion (iminium ion)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
am = s.molecule("CNC", at=(-0.4, y), lone_pairs=[1])
f = s.molecule("C=O", at=(1.6, y + 1.2), rotate=-30, lone_pairs=[1])
s.curly(am.atom(1), f.atom(0), bend=-0.5)
s.curly(f.bond(0, 1), f.atom(1), bend=-0.6)
s.arrow((2.8, y), (4.2, y), kind="equilibrium")
s.molecule("C[NH+](C)C[O-]", at=(5.8, y))
s.arrow((7.4, y), (8.8, y), kind="equilibrium", above="proton transfer")
s.molecule("CN(C)CO", at=(10.9, y))
s.text((10.9, y - 1.5), "hemiaminal")

y = -3.8
p = s.molecule("CN(C)C[OH2+]", at=(0.6, y), lone_pairs=[1])
s.curly(p.atom(1), p.bond(1, 3), bend=0.7)
s.curly(p.bond(3, 4), p.atom(4), bend=0.7)
s.text((0.6, y - 1.6), "protonated hemiaminal")
s.arrow((2.8, y), (4.2, y), kind="equilibrium", above=r"$-$H$_2$O")
s.molecule("C=[N+](C)C", at=(5.8, y))
s.text((5.8, y - 1.6), "iminium ion")
s.draw()
