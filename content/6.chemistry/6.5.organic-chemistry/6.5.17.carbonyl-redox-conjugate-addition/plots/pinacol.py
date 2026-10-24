"""Pinacol coupling of acetone. Sodium (or magnesium) transfers one electron to the carbonyl pi*
orbital (fishhook arrow), giving a ketyl radical anion. Two ketyls join through their carbon
radicals, each supplying one electron to the new C-C bond (fishhook arrows), giving the dianion of
the 1,2-diol; aqueous work-up gives pinacol (2,3-dimethylbutane-2,3-diol)."""

from wikichem import Scheme

s = Scheme()
na = s.molecule("[Na]", at=(-1.6, 1.0))
ket = s.molecule("CC(=O)C", at=(0.4, 0), lone_pairs=[2])
s.curly(na.atom(0), ket.bond(1, 2), bend=-0.4, single=True)
s.arrow((1.9, 0), (3.3, 0), below=r"$-$Na$^+$")
s.text((5.0, 1.6), "ketyl", size=13)

k1 = s.molecule("C[C](C)[O-]", at=(5.0, 0), lone_pairs=[3])
k2 = s.molecule("C[C](C)[O-]", at=(8.2, 0), lone_pairs=[3], flip=True)
mid = (k1.xy(1) + k2.xy(1)) / 2
s.curly(k1.atom(1), mid, bend=-0.5, single=True)
s.curly(k2.atom(1), mid, bend=0.5, single=True)
s.arrow((9.8, 0), (11.2, 0))
s.molecule("CC(C)([O-])C(C)(C)[O-]", at=(12.8, 0))
s.arrow((14.4, 0), (15.8, 0), above=r"H$_2$O")
s.molecule("CC(C)(O)C(C)(C)O", at=(17.4, 0))
s.draw()
