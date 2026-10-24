"""Aspartimide formation, the typical side reaction of Asp-Gly sequences in Fmoc synthesis. In
piperidine the backbone amide nitrogen of the residue after Asp (Gly here, R' the rest of the chain)
is deprotonated and attacks the side-chain tert-butyl ester; tert-butoxide leaves and a
five-membered succinimide (aspartimide) closes. The alpha-H of the imide is acidic, so the Asp
centre epimerizes, and ring opening by piperidine or water gives alpha- and beta-linked peptides."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("CC(=O)N[C@@H](CC(=O)OC(C)(C)C)C(=O)[N-]C*", at=(0.0, y), labels={17: "R$'$"}, lone_pairs=[15])
s.curly(a.atom(15), a.atom(6), bend=0.5)
s.curly(a.bond(6, 7), a.atom(7), bend=0.6)
s.text((0.0, y - 4.3), "Asp(OtBu)-Gly, amide N deprotonated")
s.arrow((3.4, y), (5.0, y), above=r"$-$$t$BuO$^-$")
s.molecule("CC(=O)N[C@@H]1CC(=O)N(C*)C1=O", at=(7.6, y), labels={10: "R$'$"})
s.text((7.6, y - 4.3), "aspartimide")
s.arrow((10.8, y), (12.4, y), above="piperidine", below=r"or H$_2$O")
s.text((14.8, y + 0.4), r"$\alpha$- and $\beta$-peptides,", size=11)
s.text((14.8, y - 0.4), "epimerized Asp", size=11)
s.draw()
