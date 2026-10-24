"""From anisole to cyclohexenones. Birch reduction leaves the donor OCH3 on a double bond:
1-methoxycyclohexa-1,4-diene is an enol ether. In dilute acid the enol ether double bond takes a proton
at C2 (the oxygen lone pair pushes, giving an oxocarbenium ion); water adds to C1, and the hemiacetal
loses methanol to give cyclohex-3-enone. Stronger acid moves the double bond into conjugation
(through the enol), giving cyclohex-2-enone."""

exec(open("helpers.txt").read())

s = Scheme()
s.molecule("COc1ccccc1", at=(0, 0), rotate=90)
s.arrow((1.4, 0), (2.8, 0), above="Li, NH$_3$", below="EtOH")
e = s.molecule("C[O:7][C:1]1=[CH:2][CH2:3][CH:4]=[CH:5][CH2:6]1", at=(4.6, 0), lone_pairs=[7], rotate=90)
h3o = s.molecule("[OH3+]", at=e.xy(2) + (1.9, -0.6), show_h=[0])
hp = min((h3o.h(0, i) for i in range(3)), key=lambda p: np.linalg.norm(p.xy - e.xy(2)))
s.curly(e.atom(7), e.bond(7, 1), bend=0.7)
s.curly(e.bond(1, 2), hp, bend=0.5)
s.curly(bond_to(h3o, 0, hp), h3o.atom(0), bend=-0.8)
s.arrow((7.6, 0), (8.8, 0))
ox = s.molecule("C[O+:7]=[C:1]1[CH2:2][CH2:3][CH:4]=[CH:5][CH2:6]1", at=(10.4, 0), rotate=90)
w = s.molecule("O", at=ox.xy(1) + (1.6, 1.0), lone_pairs=True)
s.curly(w.atom(0), ox.atom(1), bend=0.4)
s.curly(ox.bond(7, 1), ox.atom(7), bend=-0.8)
s.text((10.4, -2.0), "oxocarbenium ion", size=10)

y = -4.6
s.arrow((-1.0, y), (0.2, y), above=r"$-$H$^+$")
s.molecule("COC1(O)CC=CCC1", at=(2.0, y), rotate=90)
s.arrow((3.8, y), (5.2, y), above=r"H$^+$", below=r"$-$MeOH")
s.molecule("O=C1CC=CCC1", at=(6.8, y), rotate=90)
s.text((6.8, y - 1.9), "cyclohex-3-enone", size=10)
s.arrow((8.4, y), (9.8, y), above=r"H$_3$O$^+$")
s.molecule("O=C1C=CCCC1", at=(11.4, y), rotate=90)
s.text((11.4, y - 1.9), "cyclohex-2-enone", size=10)
s.draw()
