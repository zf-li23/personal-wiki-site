"""Charge-separated resonance structures that contain aromatic ions. Top: in tropone the polarized
C=O bond gives a structure whose seven-membered ring is a tropylium ion (6 pi electrons): large dipole
moment, basic carbonyl. Middle: the same structure for cyclopentadienone puts a 4-pi cyclopentadienyl
cation in the ring (antiaromatic), so it contributes little and the ketone dimerizes. Bottom: azulene;
the charge-separated structure combines a cyclopentadienyl anion (five-membered ring) with a tropylium
ion (seven-membered ring), which explains its dipole moment (negative end on the five-membered ring)."""

exec(open("helpers.txt").read())

s = Scheme()
a = s.molecule("[O:8]=[C:1]1[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(0, 0), rotate=0)
s.curly(a.bond(8, 1), a.atom(8), bend=0.6)
s.arrow((2.0, 0), (2.8, 0), kind="resonance")
s.molecule("[O-:8][C+:1]1[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(4.8, 0), like=a)
s.text((10.6, 0), "tropone: 6-pi tropylium ring (favorable)", size=10)

y = -3.4
b = s.molecule("[O:6]=[C:1]1[CH:2]=[CH:3][CH:4]=[CH:5]1", at=(0, y), rotate=0)
s.curly(b.bond(6, 1), b.atom(6), bend=0.6)
s.arrow((2.0, y), (2.8, y), kind="resonance")
s.molecule("[O-:6][C+:1]1[CH:2]=[CH:3][CH:4]=[CH:5]1", at=(4.8, y), like=b)
s.text((10.6, y), "cyclopentadienone: 4-pi cation (antiaromatic)", size=10)

y = -7.0
c = s.molecule("[CH:1]1=[CH:2][CH:3]=[C:4]2[C:10]1=[CH:9][CH:8]=[CH:7][CH:6]=[CH:5]2", at=(0, y), rotate=0)
s.arrow((2.0, y), (2.8, y), kind="resonance")
s.molecule("[CH-:1]1[CH:2]=[CH:3][C:4]2=[C:10]1[CH+:9][CH:8]=[CH:7][CH:6]=[CH:5]2", at=(4.8, y), like=c)
s.text((10.6, y), "azulene: 6-pi anion + 6-pi cation", size=10)
s.draw()
