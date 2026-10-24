"""Friedel-Crafts alkylation with tert-butyl chloride. (1) A chlorine lone pair of the alkyl chloride
goes to AlCl3; the C-Cl bond ionizes and the tert-butyl cation forms (AlCl4- is the counterion).
(2) A pi bond of benzene attacks the cation (slow); in the sigma complex the charge is on the ring.
(3) AlCl4- delivers a chloride that removes the proton; tert-butylbenzene, HCl and AlCl3 (the catalyst)
form. (4) Reversibility: in strong acid the ring can be protonated at the ipso carbon; the C-C bond
then breaks and the tert-butyl cation leaves, so the alkyl group can move to another ring."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
SIG = "[CH:1]1([C:7](C)(C)C)[CH:2]=[CH:3][CH:4]=[CH:5][CH2:6]1"

s = Scheme()
rcl = s.molecule("CC(C)(C)Cl", at=(0, 0), lone_pairs=[4])
al = s.molecule("Cl[Al](Cl)Cl", at=(2.7, 0))
s.curly(rcl.atom(4), al.atom(1), bend=-0.5)
s.arrow((4.0, 0), (5.1, 0))
cx = s.molecule("CC(C)(C)[Cl+][Al-](Cl)(Cl)Cl", at=(7.2, 0))
s.curly(cx.bond(1, 4), cx.atom(4), bend=0.8)
s.arrow((9.4, 0), (10.5, 0))
tb = s.molecule("C[C+](C)C", at=(11.6, 0))
s.plus((12.8, 0))
s.molecule("Cl[Al-](Cl)(Cl)Cl", at=(14.3, 0))
s.text((11.6, -1.2), "tert-butyl cation", size=10)
s.draw()

s = Scheme()
b = s.molecule("c1ccccc1", at=(0, 0), rotate=30)
tb = s.molecule("C[C+](C)C", at=(0.4, 2.4))
s.curly(b.bond(0, 1), tb.atom(1), bend=-0.5)
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
s.molecule("CC(C)(C)c1ccccc1", at=(14.0, 0))
s.text((17.4, 0), r"+ HCl + AlCl$_3$", size=11)
s.draw()

s = Scheme()
ar = s.molecule("CC(C)(C)[C:1]1=[CH:2][CH:3]=[CH:4][CH:5]=[CH:6]1", at=(0, 0))
out = ar.xy(2) - ring_centre(ar, RING)
h3o = s.molecule("[OH3+]", at=ar.xy(2) + 2.3 * out / np.linalg.norm(out) + (0.9, 0), show_h=[0])
hp = min((h3o.h(0, i) for i in range(3)), key=lambda p: np.linalg.norm(p.xy - ar.bond(1, 2).xy))
s.curly(ar.bond(1, 2), hp, bend=0.4)
s.curly(bond_to(h3o, 0, hp), h3o.atom(0), bend=-0.9)
s.arrow((3.4, 0), (4.6, 0), above=r"H$^+$")
a = s.molecule(SIG, at=(6.8, 0), show_h=[1], rotate=-60)
charge(s, a, 6, RING)
s.curly(a.bond(1, 7), a.bond(1, 6), bend=-0.9)
s.arrow((9.0, 0), (10.2, 0))
s.molecule("c1ccccc1", at=(11.4, 0))
s.plus((12.8, 0))
s.molecule("C[C+](C)C", at=(13.9, 0))
s.text((7.0, -2.6), "protonation at the ipso carbon", size=10)
s.draw()
