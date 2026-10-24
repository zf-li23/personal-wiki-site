"""Periodate cleavage of a 1,2-diol (butane-2,3-diol as the model). The diol and periodate form a
five-membered cyclic periodate diester (water is lost). In the cyclic ester three electron pairs
move together: the C-C bond becomes the pi bond of one C=O, one O-I bond pair stays on iodine,
and the other O-I bond pair becomes the pi bond of the second C=O. Iodine is reduced from I(VII)
to I(V) (iodate), and the two carbons become carbonyl groups (two molecules of acetaldehyde). A
cis-diol forms the cyclic ester easily, which is why it reacts faster than a trans-diol."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("CC(O)C(C)O", at=(0.0, y))
s.plus((1.8, y))
s.text((2.9, y), r"IO$_4^-$")
s.arrow((3.8, y), (5.2, y), below=r"$-$H$_2$O")
k = s.molecule("CC1O*OC1C", at=(7.4, y - 0.3), labels={3: "I"},
               coords=[(-1.5, -1.2), (-0.65, -0.6), (-1.0, 0.55), (0.0, 1.25), (1.0, 0.55), (0.65, -0.6), (1.5, -1.2)])
s.text((7.4, y + 1.75), r"(=O)$_2$O$^-$", size=10)
s.curly(k.bond(1, 5), k.bond(5, 4), bend=0.8)
s.curly(k.bond(4, 3), k.atom(3), bend=0.8)
s.curly(k.bond(3, 2), k.bond(2, 1), bend=0.8)
s.text((7.4, y - 2.4), "cyclic periodate ester")
s.arrow((10.2, y), (11.6, y))
s.molecule("CC=O", at=(12.6, y + 0.8))
s.molecule("CC=O", at=(12.6, y - 0.8))
s.plus((14.0, y))
s.text((15.0, y), r"IO$_3^-$")
s.text((15.0, y - 2.2), "iodate, I(V)")
s.draw()
