"""Cathodic hydrodimerization of acrylonitrile to adiponitrile (Baizer process). Acrylonitrile takes
one electron at the cathode; in the radical anion the unpaired electron is largely on the beta
carbon and the negative charge on the alpha carbon and the nitrile. Two radical anions couple
tail to tail at their beta carbons (fishhook arrows), and the dianion is protonated twice by water."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("C=CC#N", at=(0.0, y))
s.text((0.0, y - 1.5), "acrylonitrile")
s.arrow((1.4, y), (2.8, y), above=r"+e$^-$", below="cathode")
a = s.molecule("[CH2][CH-]C#N", at=(4.8, y + 1.0), lone_pairs=[1], flip=True)
b = s.molecule("[CH2][CH-]C#N", at=(4.8, y - 1.4), lone_pairs=[1], rotate=180)
m = (a.xy(0) + b.xy(0)) / 2
s.curly(a.atom(0), m, bend=0.5, single=True)
s.curly(b.atom(0), m, bend=0.4, single=True)
s.text((4.8, y - 3.0), "2 radical anions")
s.arrow((6.4, y), (7.8, y), above="tail-to-tail")
s.molecule("N#C[CH-]CC[CH-]C#N", at=(10.4, y), lone_pairs=[2, 5])
s.arrow((13.8, y), (15.2, y), above=r"2 H$_2$O", below=r"$-$2 OH$^-$")
s.molecule("N#CCCCCC#N", at=(18.2, y))
s.text((18.2, y - 1.5), "adiponitrile")
s.draw()
