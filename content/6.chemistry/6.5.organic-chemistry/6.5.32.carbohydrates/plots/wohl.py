"""Wohl degradation, drawn on the top carbons of an aldose (R = the rest of the chain). The oxime
is dehydrated and all hydroxyl groups are acetylated by acetic anhydride and sodium acetate,
giving the acetylated nitrile. Sodium methoxide removes the acetyl groups; the C2 alkoxide of the
resulting cyanohydrin pushes its electron pair back into a C=O bond and cyanide leaves (the reverse
of cyanohydrin formation). The new aldehyde carbon is the old C2, so the aldose has lost C1."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("*[C@@H](O)[C@H](O)C=NO", at=(0.0, y), labels={0: "R"})
s.text((0.0, y - 1.9), "oxime")
s.arrow((2.2, y), (4.0, y), above=r"Ac$_2$O", below="NaOAc")
s.molecule("*[C@@H](OC(C)=O)[C@H](OC(C)=O)C#N", at=(7.2, y), labels={0: "R"})
s.text((7.2, y - 2.4), "acetylated nitrile")
s.arrow((9.8, y), (11.4, y), above="NaOMe", below="MeOH")
c = s.molecule("*[C@@H](O)[C@H]([O-])C#N", at=(13.6, y), labels={0: "R"}, lone_pairs=[4])
s.curly(c.atom(4), c.bond(3, 4), bend=0.6)
s.curly(c.bond(3, 5), c.atom(5), bend=0.6)
s.text((13.6, y - 1.9), "cyanohydrin alkoxide")
s.arrow((15.8, y), (17.2, y), above=r"$-$CN$^-$")
s.molecule("*[C@@H](O)C=O", at=(18.8, y), labels={0: "R"})
s.text((18.8, y - 1.9), "aldose $-$ 1 C")
s.draw()
