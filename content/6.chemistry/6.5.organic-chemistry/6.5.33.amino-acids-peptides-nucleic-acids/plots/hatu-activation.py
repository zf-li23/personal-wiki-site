"""Activation by HATU, drawn in its O-uronium form for clarity (the reagent is mainly the
guanidinium N-oxide isomer; it reacts the same way). Top: the carboxylate (formed with DIPEA) adds
to the electrophilic central carbon of the uronium salt and the HOAt anion is expelled, giving an
O-acyl isouronium ion. Middle: the HOAt anion attacks its acyl carbon; the tetrahedral
intermediate expels tetramethylurea, giving the OAt active ester. Bottom: the amine attacks the
active ester while one N-H hydrogen bonds to the pyridine nitrogen of the leaving group (dashed),
which positions and activates the amine; this neighbouring-group assistance is why HOAt-based
reagents couple faster and with less epimerization than HOBt-based ones."""

import numpy as np
from wikichem import Scheme

s = Scheme()
y = 0.0
rc = s.molecule("*C(=O)[O-]", at=(0.0, y), labels={0: "R"}, lone_pairs=[3])
h = s.molecule("CN(C)C(=[N+](C)C)On1nnc2cccnc21", at=(4.4, y))
s.curly(rc.atom(3), h.atom(3), bend=-0.4)
s.curly(h.bond(3, 4), h.atom(4), bend=0.6)
s.text((2.4, y - 2.8), "carboxylate + HATU (O-form)")
s.arrow((7.6, y), (9.0, y), above=r"$-$OAt$^-$")
s.molecule("*C(=O)OC(N(C)C)=[N+](C)C", at=(11.0, y), labels={0: "R"})
s.text((11.0, y - 2.8), "O-acyl isouronium ion")
y2 = -5.6
oat = s.molecule("[O-]n1nnc2cccnc21", at=(0.0, y2), lone_pairs=[0])
iu = s.molecule("*C(=O)OC(N(C)C)=[N+](C)C", at=(4.6, y2), labels={0: "R"})
s.curly(oat.atom(0), iu.atom(1), bend=-0.4)
s.curly(iu.bond(1, 2), iu.atom(2), bend=0.6)
s.arrow((6.8, y2), (8.6, y2), below=r"$-$Me$_2$NC(O)NMe$_2$")
s.molecule("*C(=O)On1nnc2cccnc21", at=(11.0, y2), labels={0: "R"})
s.text((11.0, y2 - 2.9), "OAt active ester")
y3 = -11.6
e = s.molecule("*C(=O)On1nnc2cccnc21", at=(0.0, y3), labels={0: "R"})
c0 = e.xy(1)
pn = e.xy(11)
npos = c0 + np.array([-1.4, 0.1])
u = (pn - npos) / np.linalg.norm(pn - npos)
am = s.molecule("*N[H]", coords=[tuple(npos + np.array([-0.7, -0.75])), tuple(npos), tuple(npos + 0.95 * u)], labels={0: "R$'$"}, lone_pairs=[1])
s.curly(am.atom(1), e.atom(1), bend=-0.5)
s.curly(e.bond(1, 2), e.atom(2), bend=0.6)
s.partial(am.atom(2), e.atom(11))
s.text((0.0, y3 - 3.2), "aminolysis, N-H hydrogen-bonded to the pyridine N")
s.arrow((3.4, y3), (4.8, y3), below=r"$-$HOAt")
s.molecule("*C(=O)N*", at=(6.6, y3), labels={0: "R", 4: "R$'$"})
s.text((6.6, y3 - 1.8), "amide (peptide bond)")
s.draw()
