"""Why Jones oxidation of a primary alcohol does not stop at the aldehyde. In water the aldehyde
(propanal) adds water to give its hydrate, a gem-diol; the hydrate forms a chromate ester like any
alcohol, and the same E2-like step as before (water removes the C-H proton, the O-Cr bond pair
moves onto chromium) gives propanoic acid. In anhydrous CH2Cl2 (PCC) no hydrate forms and the
oxidation stops at the aldehyde."""

from wikichem import Scheme

s = Scheme()
y = 0.0
al = s.molecule("CCC=O", at=(0, y), lone_pairs=[3])
w = s.molecule("O", at=(1.9, y + 1.3), explicit_h=True, lone_pairs=[0])
s.curly(w.atom(0), al.atom(2), bend=0.4)
s.curly(al.bond(2, 3), al.atom(3), bend=-0.8)
s.arrow((2.4, y), (3.8, y), kind="equilibrium", below="proton transfer")
s.molecule("CCC(O)O", at=(5.7, y))
s.text((5.7, y - 1.4), "hydrate")
s.arrow((7.1, y), (8.5, y), above=r"H$_2$CrO$_4$", below=r"$-$H$_2$O")
y = -4.4
est = s.molecule("CCC([H])(O)O[Cr](=O)(=O)O",
                 coords=[(-1.73, -0.5), (-0.87, 0), (0, -0.5), (0, -1.5), (-0.5, 0.37), (0.87, 0), (1.73, -0.5), (1.73, -1.5), (2.6, 0), (2.6, -1.0)],
                 at=(1.0, y + 0.6), lone_pairs=[5])
w2 = s.molecule("O", at=(0.6, y - 2.3), explicit_h=True, lone_pairs=[0])
s.curly(w2.atom(0), est.atom(3), bend=-0.3)
s.curly(est.bond(2, 3), est.bond(2, 5), bend=-0.8)
s.curly(est.bond(5, 6), est.atom(6), bend=0.8)
s.text((1.4, y - 3.4), "chromate ester of the hydrate")
s.arrow((5.2, y), (6.8, y), below=r"$-$H$_3$O$^+$, $-$Cr(IV)")
s.molecule("CCC(=O)O", at=(8.4, y))
s.text((8.4, y - 2.0), "propanoic acid")
s.draw()
