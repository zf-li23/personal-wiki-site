"""Vorbrueggen nucleoside synthesis with neighbouring-group participation, on a model furanose
(the C2' benzoyloxy group of 1-O-acetyl-2,3,5-tri-O-benzoylribose closes the acyloxonium ion with
TMSOTf). The persilylated pyrimidine (2,4-bis(trimethylsilyloxy)pyrimidine) attacks C1' with N1 from
the face opposite the acyloxonium ring, so the new N-glycosidic bond is trans to the C2' substituent
(beta for ribose). Loss of the silyl groups gives the protected beta-nucleoside."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ion = s.molecule("c1ccc(cc1)C1=[O+][C@H]2OCC[C@H]2O1", at=(0.0, y))
base = s.molecule("*Oc1ccnc(O*)n1", at=(4.4, y + 0.6), labels={0: r"Me$_3$Si", 8: r"Me$_3$Si"}, lone_pairs=[5])
s.curly(base.atom(5), ion.atom(8), bend=0.4)
s.curly(ion.bond(7, 8), ion.atom(7), bend=-0.6)
s.text((1.6, y - 2.6), "acyloxonium ion + silylated uracil")
s.arrow((7.0, y), (8.6, y), above=r"$-$Me$_3$Si$^+$", below="work-up")
s.molecule("O=c1ccn([C@@H]2OCC[C@H]2OC(=O)c2ccccc2)c(=O)[nH]1", at=(11.6, y))
s.text((11.6, y - 2.6), "beta-nucleoside (1',2'-trans)")
s.draw()
