"""Michael addition of diethyl malonate to methyl vinyl ketone. The malonate anion (formed with a
catalytic amount of ethoxide) attacks the beta carbon of the enone; the C=C pi electrons move
between the alpha carbon and the carbonyl carbon and the C=O pi electrons move onto oxygen,
giving a ketone enolate. The enolate, a stronger base than the malonate anion, takes a proton from
ethanol, giving the 1,5-dicarbonyl product and regenerating ethoxide."""

from wikichem import Scheme

s = Scheme()
mal = s.molecule("CCOC(=O)[CH-]C(=O)OCC", at=(0, 0.6))
mvk = s.molecule("C=CC(C)=O", at=(2.2, -1.6), lone_pairs=[4])
s.curly(mal.atom(5), mvk.atom(0), bend=-0.5)
s.curly(mvk.bond(0, 1), mvk.bond(1, 2), bend=0.8)
s.curly(mvk.bond(2, 4), mvk.atom(4), bend=0.8)
s.text((0, 2.2), "malonate anion")
s.text((3.9, -2.9), "MVK")
s.arrow((3.8, 0), (5.0, 0))
s.molecule("CCOC(=O)C(CC=C(C)[O-])C(=O)OCC", at=(8.8, 0))
s.text((8.8, -2.6), "ketone enolate")
s.arrow((11.6, 0), (13.0, 0), above="EtOH", below=r"$-$EtO$^-$")
s.molecule("CCOC(=O)C(CCC(C)=O)C(=O)OCC", at=(15.4, 0))
s.text((15.4, -2.6), "1,5-dicarbonyl product")
s.draw()
