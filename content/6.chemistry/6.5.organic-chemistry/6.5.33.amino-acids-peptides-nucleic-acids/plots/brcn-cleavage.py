"""Cyanogen bromide cleavage on the carboxyl side of methionine (a model Ac-Met-NHR' fragment).
Top: the thioether sulfur attacks the carbon of BrCN and bromide leaves, giving a cyanosulfonium
ion. Middle: the carbonyl oxygen of the Met amide attacks the gamma carbon intramolecularly (SN2,
five-membered ring) and methyl thiocyanate leaves. Bottom: water hydrolyses the cyclic iminium
ether (iminolactone), cutting the peptide bond: the left fragment ends in homoserine lactone and
the right fragment is released with a free N-terminal amine."""

from wikichem import Scheme

s = Scheme()
y = 0.0
m = s.molecule("CSCC[C@H](NC(C)=O)C(=O)N*", at=(0.0, y), labels={12: "R$'$"}, lone_pairs=[1])
b = s.molecule("BrC#N", at=(-2.4, y + 1.8))
s.curly(m.atom(1), b.atom(1), bend=0.4)
s.curly(b.bond(0, 1), b.atom(0), bend=0.6)
s.text((0.0, y - 3.0), "Met residue + BrCN")
s.arrow((3.0, y), (4.4, y), above=r"$-$Br$^-$")
c = s.molecule("C[S+](C#N)CC[C@H](NC(C)=O)C(=O)N*", at=(7.6, y), labels={14: "R$'$"}, lone_pairs=[12])
s.curly(c.atom(12), c.atom(4), bend=0.6)
s.curly(c.bond(1, 4), c.atom(1), bend=-0.6)
s.text((7.6, y - 3.0), "cyanosulfonium ion")
y2 = -6.4
s.arrow((0.0, y2), (1.6, y2), above=r"$-$MeSCN")
s.molecule("CC(=O)N[C@@H]1CCOC1=[NH+]*", at=(3.8, y2), labels={10: "R$'$"})
s.text((3.8, y2 - 2.2), "iminolactone")
s.arrow((6.0, y2), (7.6, y2), above=r"H$_2$O")
s.molecule("CC(=O)N[C@@H]1CCOC1=O", at=(9.8, y2))
s.text((9.8, y2 - 2.2), "homoserine lactone")
s.plus((12.1, y2))
s.molecule("[NH3+]*", at=(13.9, y2), labels={1: "R$'$"})
s.draw()
