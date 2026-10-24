"""Friedel-Crafts acylation. (1) A pi bond of benzene attacks the carbon of the acylium ion; one C-O pi
bond moves onto the oxygen. (2) AlCl4- removes the proton from the sigma complex; acetophenone, HCl
and AlCl3 form. (3) The ketone is a Lewis base: its carbonyl oxygen gives a lone pair to AlCl3, and the
1:1 complex takes the Lewis acid out of the cycle, so at least one equivalent is needed; water at the
work-up frees the ketone. (4) Exception: the pivaloyl cation loses CO to give the more stable
tert-butyl cation, so pivaloyl chloride mainly gives tert-butylbenzene."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
SIG = "[CH:1]1([C:7](C)=O)[CH:2]=[CH:3][CH:4]=[CH:5][CH2:6]1"

s = Scheme()
b = s.molecule("c1ccccc1", at=(0, 0), rotate=30)
ac = s.molecule("C[C:1]#[O+:2]", at=(0.3, 2.4), rotate=90)
s.curly(b.bond(0, 1), ac.atom(1), bend=-0.5)
s.curly(ac.bond(1, 2), ac.atom(2), bend=0.8)
s.arrow((1.8, 0.3), (3.2, 0.3), above="slow")
a = s.molecule(SIG, at=(5.0, 0), show_h=[1], rotate=-60)
charge(s, a, 6, RING)
h = a.h(1)
v = (h.xy - a.xy(1)) / np.linalg.norm(h.xy - a.xy(1))
probe = Scheme().molecule("Cl[Al-](Cl)(Cl)Cl", at=h.xy + 2.2 * v)  # layout only, to find the Cl facing H
cl = min((0, 2, 3, 4), key=lambda k: np.linalg.norm(probe.xy(k) - h.xy))
al = s.molecule("Cl[Al-](Cl)(Cl)Cl", at=h.xy + 2.2 * v, lone_pairs=[cl])
s.curly(al.atom(cl), h, bend=0.4)
s.curly(bond_to(a, 1, h), a.bond(1, 6), bend=-0.9)
s.arrow((10.4, 0), (11.6, 0), above="fast")
s.molecule("CC(=O)c1ccccc1", at=(14.2, 0))
s.text((17.4, 0), r"+ HCl + AlCl$_3$", size=11)
s.draw()

s = Scheme()
k = s.molecule("C[C:1](=[O:2])c1ccccc1", at=(0, 0), lone_pairs=[2])
al = s.molecule("Cl[Al](Cl)Cl", at=k.xy(2) + (2.7, 0.2))
s.curly(k.atom(2), al.atom(1), bend=-0.4)
s.arrow((4.0, 0), (5.2, 0))
s.molecule("C[C:1](=[O+:2][Al-](Cl)(Cl)Cl)c1ccccc1", at=(8.6, 0))
s.text((8.6, -2.0), "1:1 complex (deactivated catalyst)", size=10)
s.arrow((11.3, 0), (12.5, 0), above=r"H$_2$O")
s.molecule("CC(=O)c1ccccc1", at=(14.5, 0))
s.draw()

s = Scheme()
pv = s.molecule("C[C:3](C)(C)[C:1]#[O+:2]", at=(0, 0))
s.curly(pv.bond(3, 1), pv.atom(1), bend=0.7)
s.arrow((1.8, 0), (3.0, 0), above=r"$-$CO")
s.molecule("C[C+](C)C", at=(4.2, 0))
s.arrow((5.4, 0), (6.6, 0), above="benzene")
s.molecule("CC(C)(C)c1ccccc1", at=(8.8, 0))
s.text((0, -1.4), "pivaloyl cation", size=10)
s.draw()
