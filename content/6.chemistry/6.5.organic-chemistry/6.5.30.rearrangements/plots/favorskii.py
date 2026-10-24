"""Favorskii rearrangement of 2-chlorocyclohexanone with sodium methoxide. Top row: methoxide removes
an alpha' proton (on the side away from chlorine); the enolate carbon displaces chloride
intramolecularly, closing a cyclopropanone (bicyclo[4.1.0]heptan-7-one). Bottom row: methoxide adds to
the strained carbonyl group; the tetrahedral alkoxide re-forms C=O and breaks one three-membered-ring
bond, releasing the more stable carbanion, which takes a proton from methanol. The product is methyl
cyclopentanecarboxylate: the ring has contracted by one carbon."""

from wikichem import Scheme

s = Scheme(scale=0.42)
y1, y2 = 0.0, -4.6
s.molecule("O=C1CCCCC1Cl", at=(0.0, y1))
s.text((0.0, y1 - 2.0), "2-chlorocyclohexanone")
s.arrow((1.9, y1), (3.3, y1), above=r"MeO$^-$", below=r"$-\,\mathrm{MeOH}$")
e = s.molecule("[O-]C1=CCCCC1Cl", at=(5.2, y1), lone_pairs=[0])
s.curly(e.atom(0), e.bond(0, 1), bend=0.6)
s.curly(e.bond(1, 2), e.atom(6), bend=-0.9)
s.curly(e.bond(6, 7), e.atom(7), bend=0.6)
s.text((5.2, y1 - 2.0), "enolate")
s.arrow((7.2, y1), (8.6, y1), below=r"$-\,\mathrm{Cl^-}$")
s.molecule("O=C1C2CCCCC12", at=(10.8, y1), flip=True)
s.text((10.8, y1 - 2.0), "cyclopropanone")

m = s.molecule("C[O-]", at=(-0.4, y2 + 1.6), lone_pairs=[1])
c = s.molecule("O=C1C2CCCCC12", at=(1.6, y2))
s.curly(m.atom(1), c.atom(1), bend=-0.4)
s.curly(c.bond(0, 1), c.atom(0), bend=0.6)
s.arrow((3.4, y2), (4.8, y2))
t = s.molecule("[O-]C1(OC)C2CCCCC12", at=(6.8, y2), lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=0.6)
s.curly(t.bond(1, 4), t.atom(4), bend=-0.6)
s.text((6.8, y2 - 2.1), "tetrahedral alkoxide")
s.arrow((8.8, y2), (10.4, y2), above="ring opening", below="MeOH")
s.molecule("COC(=O)C1CCCC1", at=(13.8, y2))
s.text((13.8, y2 - 2.1), "methyl cyclopentanecarboxylate")
s.draw()
