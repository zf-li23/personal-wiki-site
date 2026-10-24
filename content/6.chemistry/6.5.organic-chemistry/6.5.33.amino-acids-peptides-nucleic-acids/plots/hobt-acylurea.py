"""What happens to the O-acylisourea from a carbodiimide (drawn for DIC; R = the activated amino
acid). Top: HOBt (as its anion) intercepts it at the acyl carbon; the tetrahedral intermediate
expels diisopropylurea, giving the OBt active ester, reactive enough to acylate the amine but much
less prone to oxazolone formation. Bottom: without an additive, the imine nitrogen of the isourea
attacks the same acyl carbon intramolecularly (O to N acyl migration through a four-membered cyclic
intermediate), giving the unreactive N-acylurea, a dead end that lowers the yield."""

from wikichem import Scheme

s = Scheme()
y = 0.0
obt = s.molecule("[O-]n1nnc2ccccc21", at=(0.0, y), lone_pairs=[0])
iu = s.molecule("*C(=O)OC(=NC(C)C)NC(C)C", at=(6.2, y), labels={0: "R"})
s.curly(obt.atom(0), iu.atom(1), bend=-0.4)
s.curly(iu.bond(1, 2), iu.atom(2), bend=0.6)
s.text((3.0, y - 3.0), "HOBt anion + O-acylisourea")
s.arrow((9.0, y), (10.4, y), below=r"$-$iPrNHC(O)NHiPr")
s.molecule("*C(=O)On1nnc2ccccc21", at=(13.0, y), labels={0: "R"})
s.text((13.0, y - 3.0), "OBt active ester")
y2 = -6.4
a = s.molecule("*C(=O)OC(=NC(C)C)NC(C)C", at=(0.0, y2), labels={0: "R"}, lone_pairs=[5])
s.curly(a.atom(5), a.atom(1), bend=0.7)
s.curly(a.bond(1, 2), a.atom(2), bend=0.6)
s.text((0.0, y2 - 3.0), "O-acylisourea")
s.arrow((2.8, y2), (4.4, y2), above=r"O$\to$N acyl shift")
s.molecule("*C(=O)N(C(C)C)C(=O)NC(C)C", at=(7.2, y2), labels={0: "R"})
s.text((7.2, y2 - 2.6), "N-acylurea (unreactive)")
s.draw()
