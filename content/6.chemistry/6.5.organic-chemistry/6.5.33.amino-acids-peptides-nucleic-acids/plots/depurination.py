"""Acid-catalysed depurination of 2'-deoxyguanosine. With N7 of guanine protonated (or alkylated),
the base is a good leaving group: the lone pair of the ring oxygen O4' pushes it out, the
C1'-N9 bond breaks, and a furanosyl oxocarbenium ion and free guanine are formed. Water adds to the
oxocarbenium ion, leaving an abasic site. Without a 2'-OH, which would destabilize the cation by
its inductive effect, DNA depurinates much faster than RNA."""

from wikichem import Scheme

s = Scheme()
y = 0.0
g = s.molecule("OC[C@H]1O[C@@H](n2c[nH+]c3c2nc(N)[nH]c3=O)C[C@@H]1O", at=(0.0, y), lone_pairs=[3])
s.curly(g.atom(3), g.bond(3, 4), bend=-0.6)
s.curly(g.bond(4, 5), g.atom(5), bend=0.6)
s.text((0.0, y - 3.9), "N7-protonated 2'-deoxyguanosine")
s.arrow((3.8, y), (5.0, y))
s.molecule("OC[C@H]1[O+]=CC[C@@H]1O", at=(7.8, y))
s.text((7.8, y - 3.9), "oxocarbenium ion")
s.plus((9.75, y))
s.molecule("Nc1nc2[nH]cnc2c(=O)[nH]1", at=(12.2, y))
s.text((12.2, y - 3.9), "guanine")
s.arrow((14.4, y), (15.8, y), above=r"H$_2$O", below=r"$-$H$^+$")
s.molecule("OC[C@H]1OC(O)C[C@@H]1O", at=(18.6, y))
s.text((18.6, y - 3.9), "abasic site")
s.draw()
