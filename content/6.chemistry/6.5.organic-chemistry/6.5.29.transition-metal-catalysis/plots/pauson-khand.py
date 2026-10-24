"""Pauson-Khand reaction of a terminal alkyne (R-C#C-H) with ethylene and CO (Magnus mechanism,
simplified). The alkyne and Co2(CO)8 form the stable Co2(CO)6(mu-alkyne) complex, a tetrahedral
C2Co2 core; one cobalt loses CO and binds the alkene, which inserts into the Co-C bond of the less
hindered alkyne carbon, giving a cobaltacyclopentene ([Co] = the Co2(CO)n unit); CO inserts into
the Co-CH2 bond and reductive elimination closes the cyclopentenone. The larger alkyne
substituent R ends up next to the carbonyl group."""

exec(open("cycle.txt").read())

s = Scheme()
s.molecule("*C12[Co]3[Co]1C23[H]", coords=[(-1.5, 0.5), (-0.5, 0), (0, 1.0), (0, -1.0), (0.5, 0), (1.4, 0.5)],
           labels={0: "R", 2: "Co(CO)$_3$", 3: "Co(CO)$_3$"})
s.text((0, -2.0), "Co$_2$(CO)$_6$($\\mu$-alkyne)", size=11)
s.arrow((2.2, 0), (3.8, 0), above="C$_2$H$_4$", below="$-$CO")
x = 6.0
s.molecule("[Co]1CCC=C1*", at=(x, 0), labels={0: "[Co]", 5: "R"})
s.text((x, -1.8), "alkene insertion", size=11)
s.arrow((x + 1.8, 0), (x + 3.2, 0), above="CO")
x2 = x + 5.2
s.molecule("[Co]1C(=O)CCC=C1*", at=(x2, 0), labels={0: "[Co]", 7: "R"})
s.text((x2, -2.0), "CO insertion", size=11)
s.arrow((x2 + 2.0, 0), (x2 + 3.6, 0), above="reductive", below="elimination")
s.molecule("O=C1CCC=C1*", at=(x2 + 5.4, 0), labels={6: "R"})
s.draw()
