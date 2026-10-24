"""Sigma complexes of naphthalene bromination. Attack at C1 (top) gives two resonance structures in
which the second ring stays a complete benzene ring (positive charge on C2 or C4); attack at C2
(bottom) gives only one (positive charge on C1). The other resonance structures put the charge into
the second ring and destroy both sextets; they contribute less and are not drawn."""

exec(open("helpers.txt").read())

LEFT = [1, 2, 3, 4, 9, 10]
A2 = "[CH:1]1(Br)[CH2:2][CH:3]=[CH:4][C:9]2=[C:10]1[CH:8]=[CH:7][CH:6]=[CH:5]2"
A4 = "[C:1]%101(Br)[CH:2]=[CH:3][CH2:4][C:9]2=[C:10]1[CH:8]=[CH:7][CH:6]=[CH:5]2.[H]%10"
B1 = "[CH2:1]1[CH:2](Br)[CH:3]=[CH:4][C:9]2=[C:10]1[CH:8]=[CH:7][CH:6]=[CH:5]2"

s = Scheme()
a = s.molecule(A2, at=(0, 0), show_h=[1])
charge(s, a, 2, LEFT)
s.arrow((2.0, 0), (2.8, 0), kind="resonance")
b = s.molecule(A4, at=(4.8, 0), like=a)
charge(s, b, 4, LEFT)
s.text((-3.5, 0), "attack at C1", size=10)
s.text((2.4, -2.0), "two structures keep a benzene ring", size=9)
c = s.molecule(B1, at=(0, -4.6), show_h=[2])
charge(s, c, 1, LEFT)
s.text((-3.5, -4.6), "attack at C2", size=10)
s.text((0, -6.6), "only one such structure", size=9)
s.draw()
