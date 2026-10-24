"""[1,2]-Brook rearrangement. The alkoxide of an alpha-silyl alcohol (here phenyl(trimethylsilyl)
methanol) attacks its own silicon atom; through a three-membered pentacoordinate silicate the C-Si
bond breaks and the trimethylsilyl group ends on oxygen, leaving a benzylic carbanion that is
protonated. Silicon can migrate to an electron-rich centre because it accepts the electron pair
into a low-lying sigma* orbital, and the strong Si-O bond drives the reaction."""

from wikichem import Scheme

s = Scheme()
y = 0.0
m = s.molecule("[O-]C(c1ccccc1)[Si](C)(C)C", at=(0.0, y), lone_pairs=[0])
s.curly(m.atom(0), m.atom(8), bend=-0.6)
s.curly(m.bond(1, 8), m.atom(1), bend=-0.6)
s.text((0.0, y - 2.5), "alpha-silyl alkoxide")
s.arrow((2.6, y), (4.0, y), above="O-silylation")
c = s.molecule("[CH-](O[Si](C)(C)C)c1ccccc1", at=(6.6, y), lone_pairs=[0])
s.text((6.6, y - 2.5), "benzylic carbanion")
s.arrow((9.2, y), (10.6, y), above=r"H$^+$")
s.molecule("C(O[Si](C)(C)C)c1ccccc1", at=(13.2, y))
s.text((13.2, y - 2.5), "benzyl silyl ether")
s.draw()
