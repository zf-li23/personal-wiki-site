"""Darzens reaction of cyclohexanone with ethyl chloroacetate. The ester enolate (formed with
potassium tert-butoxide) adds to the ketone carbonyl, as in an aldol addition, giving a
beta-chloro alkoxide. The alkoxide oxygen then attacks the neighbouring carbon from the back side
and chloride leaves (intramolecular SN2), closing the epoxide of the glycidic ester."""

from wikichem import Scheme

s = Scheme()
en = s.molecule("ClC=C([O-])OCC", at=(0, 1.0), rotate=180, lone_pairs=[3])
ket = s.molecule("O=C1CCCCC1", at=(0.6, -1.8), lone_pairs=[0])
s.curly(en.atom(3), en.bond(2, 3), bend=0.7)
s.curly(en.bond(1, 2), ket.atom(1), bend=-0.6)
s.curly(ket.bond(0, 1), ket.atom(0), bend=0.7)
s.text((-2.2, 1.0), "ester enolate")
s.arrow((2.6, 0), (4.0, 0))
alk = s.molecule("CCOC(=O)C(Cl)C1([O-])CCCCC1", at=(6.4, 0), lone_pairs=[8])
s.curly(alk.atom(8), alk.atom(5), bend=-0.6)
s.curly(alk.bond(5, 6), alk.atom(6), bend=0.6)
s.text((6.4, -2.4), "beta-chloro alkoxide")
s.arrow((8.6, 0), (10.0, 0), above="SN2", below=r"$-$Cl$^-$")
s.molecule("CCOC(=O)C1OC12CCCCC2", at=(12.2, 0))
s.text((12.2, -2.5), "glycidic ester")
s.draw()
