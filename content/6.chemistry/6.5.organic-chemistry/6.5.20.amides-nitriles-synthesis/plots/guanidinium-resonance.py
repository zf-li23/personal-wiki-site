"""The three equivalent resonance structures of the guanidinium ion. In each, one nitrogen carries the
double bond and the positive charge; the curved arrows show how the first structure turns into the
second. The charge is spread evenly over three nitrogens and the ion is planar, which is why guanidine is
one of the strongest neutral organic bases."""

from wikichem import Scheme

s = Scheme()
g1 = s.molecule("[NH2:1][C:2]([NH2:3])=[NH2+:4]", at=(0.0, 0.0), lone_pairs=[3])
s.curly(g1.atom(3), g1.bond(2, 3), bend=0.8)
s.curly(g1.bond(2, 4), g1.atom(4), bend=0.8)
s.arrow((1.6, 0.0), (2.9, 0.0), kind="resonance")
s.molecule("[NH2:1][C:2](=[NH2+:3])[NH2:4]", at=(4.4, 0.0), like=g1)
s.arrow((5.9, 0.0), (7.2, 0.0), kind="resonance")
s.molecule("[NH2+:1]=[C:2]([NH2:3])[NH2:4]", at=(8.7, 0.0), like=g1)
s.draw()
