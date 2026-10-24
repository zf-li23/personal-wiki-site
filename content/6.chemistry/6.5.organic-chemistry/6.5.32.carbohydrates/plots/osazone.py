"""Osazone formation (the Weygand mechanism), drawn on the top carbons of an aldose (R = the rest
of the chain). Top: the C1 phenylhydrazone tautomerizes through the enol-hydrazine (an Amadori-type
rearrangement) to the 1-(2-phenylhydrazinyl)-2-ketone, so C2 has been oxidized and C1 reduced.
Middle: in the enol form, the O-H lone pair, the C=C bond and the N-N bond move together and aniline
is expelled, leaving an alpha-imino ketone. Bottom: two more molecules of phenylhydrazine condense
with the C2 carbonyl group and exchange with the C1 imine (losing NH3), giving the osazone, held
together by an intramolecular hydrogen bond."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("*[C@@H](O)C=NNc1ccccc1", at=(0.0, y), labels={0: "R"})
s.text((0.0, y - 2.0), "phenylhydrazone")
s.arrow((3.4, y), (5.0, y), above="tautomerism", kind="equilibrium")
s.molecule("*C(O)=CNNc1ccccc1", at=(8.4, y), labels={0: "R"})
s.text((8.4, y - 2.0), "enol-hydrazine")
s.arrow((11.8, y), (13.4, y), kind="equilibrium")
s.molecule("*C(=O)CNNc1ccccc1", at=(16.8, y), labels={0: "R"})
s.text((16.8, y - 2.0), "2-keto hydrazine")
y2 = -5.0
e = s.molecule("*C([OH])=C[NH][NH2+]c1ccccc1", at=(0.0, y2), labels={0: "R"}, lone_pairs=[2])
s.curly(e.atom(2), e.bond(1, 2), bend=0.6)
s.curly(e.bond(1, 3), e.bond(3, 4), bend=0.6)
s.curly(e.bond(4, 5), e.atom(5), bend=-0.6)
s.text((0.0, y2 - 2.0), "enol form, N protonated")
s.arrow((3.4, y2), (5.0, y2), above=r"$-$PhNH$_2$", below=r"$-$H$^+$")
s.molecule("*C(=O)C=N", at=(7.0, y2), labels={0: "R"})
s.text((7.0, y2 - 2.0), "alpha-imino ketone")
s.arrow((8.8, y2), (11.0, y2), above=r"2 PhNHNH$_2$", below=r"$-$NH$_3$, $-$H$_2$O")
s.molecule("*C(=NNc1ccccc1)C=NNc1ccccc1", at=(15.8, y2), labels={0: "R"})
s.text((15.8, y2 - 3.0), "osazone")
s.draw()
