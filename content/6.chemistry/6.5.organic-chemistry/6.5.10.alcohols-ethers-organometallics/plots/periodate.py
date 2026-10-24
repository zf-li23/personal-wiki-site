"""Periodate cleavage of a vicinal diol (2,3-dimethylbutane-2,3-diol). The two hydroxy groups form a
five-membered cyclic periodate ester (iodine +7). In one concerted step the C-C bond pair becomes
a C=O pi bond, one O-I bond pair moves onto iodine and the other O-I bond pair becomes the second
C=O pi bond: two molecules of acetone and iodate (iodine +5)."""

from wikichem import Scheme

s = Scheme()
s.molecule("CC(C)(O)C(C)(C)O", at=(0, 0))
s.arrow((1.8, 0), (3.2, 0), above=r"IO$_4^-$", below=r"$-$H$_2$O")
# ring: 0 C1, 3 Oa, 4 I (with its three other oxygens written as a label), 5 Ob, 6 C2
est = s.molecule("C1(C)(C)O*OC1(C)C",
                 coords=[(0, 0.5), (-0.5, 1.37), (-0.95, 0.75), (0.95, 0.85), (1.9, 0), (0.95, -0.85), (0, -0.5), (-0.5, -1.37), (-0.95, -0.75)],
                 at=(5.0, 0), lone_pairs=[3, 5], labels={4: r"IO$_3^-$"})
s.curly(est.bond(0, 6), est.bond(0, 3), bend=-0.6)
s.curly(est.bond(3, 4), est.atom(4), bend=-0.6)
s.curly(est.bond(5, 4), est.bond(5, 6), bend=-0.6)
s.text((6.0, -2.0), "cyclic periodate ester")
s.arrow((8.8, 0), (10.2, 0))
s.molecule("CC(=O)C", at=(11.2, 0.9))
s.molecule("CC(=O)C", at=(11.2, -1.1))
s.plus((12.4, 0))
s.text((13.4, 0), r"IO$_3^-$")
s.draw()
