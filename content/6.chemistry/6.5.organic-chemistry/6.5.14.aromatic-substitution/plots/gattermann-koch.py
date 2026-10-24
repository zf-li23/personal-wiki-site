"""Gattermann-Koch formylation. The carbon lone pair of CO takes the proton of HCl (activated by AlCl3,
which takes the chloride as AlCl4-): the formyl cation H-C#O+ forms, the equivalent of the unstable
formyl chloride. It attacks toluene mainly para to the methyl group (SEAr), and loss of the proton
gives 4-methylbenzaldehyde."""

exec(open("helpers.txt").read())

s = Scheme()
co = s.molecule("[C-]#[O+]", at=(0, 0), lone_pairs=[0], flip=True, show_carbons=[0])
hcl = s.molecule("Cl", at=(2.3, 0), show_h=[0], lone_pairs=True, flip=True)
s.curly(co.atom(0), hcl.h(0), bend=-0.6)
s.curly(bond_to(hcl, 0, hcl.h(0)), hcl.atom(0), bend=-0.9)
s.arrow((3.6, 0), (4.8, 0), above=r"AlCl$_3$", below=r"$-$AlCl$_4^-$")
s.molecule("[CH]#[O+]", at=(6.0, 0), show_carbons=[0])
s.text((6.0, -0.9), "formylium ion", size=10)
s.arrow((7.3, 0), (8.5, 0), above="toluene", below=r"$-$H$^+$")
s.molecule("Cc1ccc(C=O)cc1", at=(11.4, 0), rotate=-30)
s.draw()
