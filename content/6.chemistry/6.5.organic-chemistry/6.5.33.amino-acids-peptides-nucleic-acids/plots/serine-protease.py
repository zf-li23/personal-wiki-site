"""The first step of peptide-bond hydrolysis by a serine protease (chymotrypsin, trypsin,
subtilisin), with the catalytic triad Asp-His-Ser drawn as fragments. His57 acts as a general
base: its ring nitrogen takes the proton of the Ser195 hydroxyl while the serine oxygen adds to
the carbonyl carbon of the scissile peptide bond; Asp102 holds the His in the right tautomer and
orientation through a hydrogen bond (dashed). The tetrahedral intermediate carries an oxyanion,
stabilized by two backbone N-H groups (the oxyanion hole). It then collapses, His (now acting as
a general acid) protonates the leaving amine, and the acyl-enzyme ester is hydrolysed by water
in the reverse sequence of steps: two nucleophilic acyl substitutions in a row."""

from wikichem import Scheme

s = Scheme()
asp = s.molecule("*C(=O)[O-]", at=(-4.6, 0.0), labels={0: "Asp"}, rotate=0)
his = s.molecule("*c1cnc[nH]1", at=(-1.8, 0.0), labels={0: "His"}, lone_pairs=[3], rotate=-90)
ser = s.molecule("*C[OH]", at=(1.2, 1.4), labels={0: "Ser"}, explicit_h=False, show_h=[2], lone_pairs=[2])
sub = s.molecule("*C(=O)N*", at=(3.4, -0.6), labels={0: "R", 4: "R$'$"}, lone_pairs=[2])
s.partial(asp.atom(3), his.atom(5))
s.curly(his.atom(3), ser.h(2), bend=-0.4)
s.curly(ser.bond(2, ser.mol.GetNumAtoms() - 1), ser.atom(2), bend=-0.5)
s.curly(ser.atom(2), sub.atom(1), bend=-0.4)
s.curly(sub.bond(1, 2), sub.atom(2), bend=0.6)
s.text((3.4, -2.4), "peptide bond (substrate)")
s.text((-3.2, -2.4), "catalytic triad")
s.arrow((5.6, -0.4), (7.0, -0.4))
s.molecule("*C([O-])(N*)OC*", at=(8.8, -0.4), labels={0: "R", 4: "R$'$", 7: "Ser"})
s.text((8.8, -2.4), "tetrahedral intermediate\n(oxyanion hole)")
s.draw()
