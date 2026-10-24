"""Bisulfite conversion of cytosine to uracil (R = the deoxyribose of DNA). In acid, bisulfite adds
to C6 of N3-protonated cytosine (conjugate addition; curved arrows), saturating the C5=C6 bond.
In the 5,6-dihydro adduct the C4 amidine is easily hydrolysed (water adds, ammonium leaves), giving
the uracil sulfonate; in base bisulfite is eliminated and the C5=C6 double bond returns, leaving
uracil. 5-Methylcytosine reacts far more slowly and is read as C after PCR."""

from wikichem import Scheme

s = Scheme()
y = 0.0
c = s.molecule("*N1C=CC(N)=[NH+]C1=O", at=(0.0, y), labels={0: "R"})
hs = s.molecule("OS(=O)[O-]", at=(c.xy(2)[0] - 1.2, c.xy(2)[1] - 2.0), lone_pairs=[1])
s.curly(hs.atom(1), c.atom(2), bend=0.4)
s.curly(c.bond(2, 3), c.bond(3, 4), bend=0.6)
s.curly(c.bond(4, 6), c.atom(6), bend=0.6)
s.text((0.0, y - 4.7), "N3-protonated cytosine")
s.arrow((2.2, y), (3.6, y), above=r"HSO$_3^-$", below=r"H$^+$")
s.molecule("*N1C(S(=O)(=O)[O-])CC(N)=NC1=O", at=(6.0, y), labels={0: "R"})
s.text((6.0, y - 4.7), "5,6-dihydrocytosine sulfonate")
y2 = -7.8
s.arrow((0.0, y2), (1.6, y2), above=r"H$_2$O", below=r"$-$NH$_4^+$")
s.molecule("*N1C(S(=O)(=O)[O-])CC(=O)NC1=O", at=(4.0, y2), labels={0: "R"})
s.text((4.0, y2 - 2.4), "uracil sulfonate")
s.arrow((6.4, y2), (8.0, y2), above=r"OH$^-$", below=r"$-$HSO$_3^-$")
s.molecule("*n1ccc(=O)[nH]c1=O", at=(10.0, y2), labels={0: "R"})
s.text((10.0, y2 - 2.4), "uracil")
s.draw()
