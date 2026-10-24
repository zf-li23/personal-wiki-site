"""Drawing all resonance structures one arrow at a time: the pentadienyl cation. Each step moves one
pi bond toward the positive carbon, so the charge walks from C5 to C3 to C1; it never sits on C2 or C4."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("[CH2:1]=[CH:2][CH:3]=[CH:4][CH2+:5]", at=(0, 0))
s.curly(a.bond(3, 4), a.bond(4, 5), bend=0.6)
s.arrow((2.6, 0), (3.6, 0), kind="resonance")
b = s.molecule("[CH2:1]=[CH:2][CH+:3][CH:4]=[CH2:5]", at=(6.2, 0), like=a)
s.curly(b.bond(1, 2), b.bond(2, 3), bend=0.6)
s.arrow((8.8, 0), (9.8, 0), kind="resonance")
s.molecule("[CH2+:1][CH:2]=[CH:3][CH:4]=[CH2:5]", at=(12.4, 0), like=a)
for x, k in ((0, 5), (6.2, 3), (12.4, 1)):
    s.text((x, -1.4), f"+ on C{k}", size=10)
s.draw()
