"""Why amides are protonated on oxygen. Left: the nitrogen lone pair of an amide is delocalised onto
the carbonyl oxygen (two resonance structures). Right: protonation on oxygen keeps this
delocalisation, and the positive charge of the O-protonated amide is shared by oxygen and nitrogen;
protonation on nitrogen would use the delocalised lone pair and destroy the conjugation, so it is
much less favourable. The conjugate acid of acetamide has pKa about -0.5."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("CC(=O)N", at=(0, 0), lone_pairs=[2, 3])
s.curly(a.atom(3), a.bond(1, 3), bend=0.6)
s.curly(a.bond(1, 2), a.atom(2), bend=0.6)
s.arrow((1.4, 0), (2.6, 0), kind="resonance")
s.molecule("CC([O-])=[NH2+]", at=(4.0, 0), like=a)
s.text((2.0, -1.8), "amide resonance")
s.arrow((5.4, 0), (6.8, 0), above=r"H$^+$")
p = s.molecule("CC(=[OH+])N", at=(8.2, 0), like=a, lone_pairs=[3])
s.curly(p.atom(3), p.bond(1, 3), bend=0.6)
s.curly(p.bond(1, 2), p.atom(2), bend=0.6)
s.arrow((9.6, 0), (10.8, 0), kind="resonance")
s.molecule("CC(O)=[NH2+]", at=(12.2, 0), like=a)
s.text((10.2, -1.8), "O-protonated amide: charge on O and N")
s.draw()
