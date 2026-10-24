"""SN1 reaction of 2-methylpropan-2-ol with concentrated hydrochloric acid. The hydroxy oxygen takes
a proton from HCl; the protonated alcohol loses water (rate-determining) to give the tert-butyl
cation, which chloride captures to give 2-chloro-2-methylpropane."""

from wikichem import Scheme

s = Scheme()
y = 0.0
alc = s.molecule("CC(C)(C)O", at=(0, y), lone_pairs=[4])
hcl = s.molecule("Cl", at=(2.3, y + 0.9), explicit_h=True, lone_pairs=[0], rotate=180)
s.curly(alc.atom(4), hcl.atom(1), bend=-0.5)
s.curly(hcl.bond(0, 1), hcl.atom(0), bend=-0.8)
s.arrow((3.6, y), (4.8, y))
ox = s.molecule("CC(C)(C)[OH2+]", at=(6.2, y), lone_pairs=[4])
s.curly(ox.bond(1, 4), ox.atom(4), bend=1.0)
s.arrow((8.3, y), (9.7, y), above="slow", below=r"$-$H$_2$O")
cat = s.molecule("C[C+](C)C", at=(11.0, y))
cl = s.molecule("[Cl-]", at=(12.9, y), lone_pairs=True)
s.curly(cl.atom(0), cat.atom(1), bend=0.5)
s.arrow((13.8, y), (15.0, y), above="fast")
s.molecule("CC(C)(C)Cl", at=(16.3, y))
s.draw()
