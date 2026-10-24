"""Fries rearrangement of phenyl acetate (AlCl3, heat). Top: AlCl3 binds the ester (aryl) oxygen;
the acyl-oxygen bond breaks heterolytically to give the acylium ion and an aryloxy-aluminium
species. Bottom: the acylium ion attacks the ring para (or ortho) to the strongly activating
O-Al group; the sigma complex loses a proton, and aqueous work-up gives 4-hydroxyacetophenone."""

exec(open("helpers.txt").read())

s = Scheme()
est = s.molecule("C[C:1](=O)[O:2][c:3]1ccccc1", at=(0, 0), lone_pairs=[2])
al = s.molecule("Cl[Al](Cl)Cl", at=est.xy(2) + (0.2, -2.1))
s.curly(est.atom(2), al.atom(1), bend=0.4)
s.arrow((2.7, 0), (3.9, 0))
cx = s.molecule("C[C:1](=O)[O+:2]([Al-](Cl)(Cl)Cl)[c:3]1ccccc1", at=(6.4, 0))
s.curly(cx.bond(1, 2), cx.atom(2), bend=0.6)
s.arrow((8.9, 0), (10.1, 0))
s.molecule("CC#[O+]", at=(11.2, 0.6))
s.plus((11.2, -0.3))
s.molecule("Cl[Al-](Cl)(Cl)Oc1ccccc1", at=(12.2, -1.9))
s.draw()

s = Scheme()
ar = s.molecule("Cl[Al-](Cl)(Cl)[O:1][C:2]1=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(0, 0), rotate=0)
acyl = s.molecule("C[C+:8]=O", at=ar.xy(5) + (0.9, 1.8))
s.curly(ar.bond(4, 5), acyl.atom(8), bend=-0.4)
s.arrow((3.6, -0.6), (5.4, -0.6), above=r"$-$H$^+$", below=r"then H$_2$O")
s.molecule("CC(=O)c1ccc(O)cc1", at=(8.2, 0))
s.text((8.2, -2.5), "4-hydroxyacetophenone", size=10)
s.draw()
