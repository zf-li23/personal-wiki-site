"""Chloromethylation (Blanc reaction). (1) Protonated formaldehyde (ZnCl2 also helps by binding the
oxygen) is attacked by a pi bond of the ring at carbon; the C=O pi bond moves onto oxygen. Loss of the
proton from the sigma complex gives benzyl alcohol. (2) In HCl the hydroxy group is protonated, water
leaves to give the resonance-stabilized benzyl cation, and chloride adds to give benzyl chloride."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
SIG = "[CH:1]1([CH2:7]O)[CH:2]=[CH:3][CH:4]=[CH:5][CH2:6]1"

s = Scheme()
b = s.molecule("c1ccccc1", at=(0, 0), rotate=30)
f = s.molecule("[CH2:1]=[OH+:2]", at=(0.3, 2.3))
s.curly(b.bond(0, 1), f.atom(1), bend=-0.5)
s.curly(f.bond(1, 2), f.atom(2), bend=0.8)
s.arrow((1.8, 0.3), (3.2, 0.3), above="slow")
a = s.molecule(SIG, at=(5.0, 0), show_h=[1], rotate=-60)
charge(s, a, 6, RING)
h = a.h(1)
v = (h.xy - a.xy(1)) / np.linalg.norm(h.xy - a.xy(1))
w = s.molecule("O", at=h.xy + 1.6 * v, lone_pairs=True)
s.curly(w.atom(0), h, bend=0.4)
s.curly(bond_to(a, 1, h), a.bond(1, 6), bend=-0.9)
s.arrow((7.8, 0), (9.0, 0), above=r"$-$H$^+$")
s.molecule("OCc1ccccc1", at=(10.6, 0))
s.draw()

s = Scheme()
p = s.molecule("[OH2+:1][CH2:2]c1ccccc1", at=(0, 0))
s.curly(p.bond(1, 2), p.atom(1), bend=0.7)
s.arrow((2.0, 0), (3.2, 0), below=r"$-$H$_2$O")
c = s.molecule("[CH2+:2]c1ccccc1", at=(4.9, 0))
cl = s.molecule("[Cl-]", at=c.xy(2) + (-0.2, 1.5), lone_pairs=True)
s.curly(cl.atom(0), c.atom(2), bend=0.4)
s.text((4.9, -1.6), "benzyl cation", size=10)
s.arrow((6.6, 0), (7.8, 0))
s.molecule("ClCc1ccccc1", at=(9.5, 0))
s.draw()
