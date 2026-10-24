"""General SEAr mechanism, shown for nitration. (1) A pi bond of benzene attacks the nitronium ion
(slow, rate-determining): the arenium ion (Wheland intermediate, sigma complex) forms; its positive
charge is shared by the carbons ortho and para to the sp3 carbon (three resonance structures).
(2) A base (water or HSO4-) removes the proton from the sp3 carbon (fast) and aromaticity is restored."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
# arenium ion: C1 sp3 (H, NO2); the resonance structures put + on C6, C4 or C2. The H is written
# last (ring closure 9) so that the later structures can reuse the first layout (like=).
S6 = "[CH:1]1([N+](=O)[O-])[CH:2]=[CH:3][CH:4]=[CH:5][CH2:6]1"
S4 = "[C:1]91([N+](=O)[O-])[CH:2]=[CH:3][CH2:4][CH:5]=[CH:6]1.[H]9"
S2 = "[C:1]91([N+](=O)[O-])[CH2:2][CH:3]=[CH:4][CH:5]=[CH:6]1.[H]9"

s = Scheme()
b = s.molecule("c1ccccc1", at=(0, 0), rotate=30)
no2 = s.molecule("O=[N+]=O", at=(0.2, 2.3), lone_pairs=[0])
s.curly(b.bond(0, 1), no2.atom(1), bend=-0.5)
s.curly(no2.bond(0, 1), no2.atom(0), bend=0.8)
s.arrow((1.6, 0.3), (3.0, 0.3), above="slow")
a6 = s.molecule(S6, at=(4.7, 0), show_h=[1], rotate=-60)
charge(s, a6, 6, RING)
s.arrow((6.3, 0), (7.3, 0), kind="resonance")
a4 = s.molecule(S4, at=(8.9, 0), like=a6)
charge(s, a4, 4, RING)
s.arrow((10.5, 0), (11.5, 0), kind="resonance")
a2 = s.molecule(S2, at=(13.1, 0), like=a6)
charge(s, a2, 2, RING)
s.text((8.9, -2.2), "arenium ion (Wheland intermediate, sigma complex)", size=11)
s.draw()

s = Scheme()
a6 = s.molecule(S6, at=(0, 0), show_h=[1], rotate=-60)
charge(s, a6, 6, RING)
h = a6.h(1)
water = s.molecule("O", at=h.xy + (1.0, 1.4), lone_pairs=True)
s.curly(water.atom(0), h, bend=0.4)
s.curly(bond_to(a6, 1, h), a6.bond(1, 6), bend=0.9)
s.arrow((3.0, 0), (4.4, 0), above="fast")
s.molecule("O=[N+]([O-])c1ccccc1", at=(6.2, 0))
s.plus((8.0, 0))
s.text((9.0, 0), r"H$_3$O$^+$")
s.draw()
