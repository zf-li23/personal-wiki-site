"""Resonance structures judged by the contribution rules. (a) The carbonyl group: the charge-separated
structure puts the negative charge on the more electronegative oxygen and is a minor but real
contributor (the C=O bond is polar). (b) Nitromethane: two equivalent structures, so both N-O bonds
are the same length and each oxygen carries half a negative charge. (c) Diazomethane: neither
structure is free of formal charges; in the right one every atom has an octet and carbon carries the
negative charge, which explains why the carbon of diazomethane is nucleophilic."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.text((-2.2, y), "(a)")
c = s.molecule("CC(C)=O", at=(0, y), rotate=-90, lone_pairs=[3])
s.curly(c.bond(1, 3), c.atom(3), bend=-0.7)
s.arrow((1.6, y), (2.6, y), kind="resonance")
s.molecule("C[C+](C)[O-]", at=(4.2, y), rotate=-90, lone_pairs=[3])
s.text((2.1, y - 1.6), "minor contributor on the right", size=10)

y = -3.6
s.text((-2.2, y), "(b)")
n1 = s.molecule("C[N+:2](=[O:3])[O-:4]", at=(0, y), lone_pairs=[3, 4])
s.curly(n1.atom(4), n1.bond(2, 4), bend=0.6)
s.curly(n1.bond(2, 3), n1.atom(3), bend=0.6)
s.arrow((1.6, y), (2.6, y), kind="resonance")
s.molecule("C[N+:2]([O-:3])=[O:4]", at=(4.2, y), like=n1, lone_pairs=[3, 4])
s.text((2.1, y - 1.6), "equivalent structures", size=10)

y = -7.0
s.text((-2.2, y), "(c)")
d1 = s.molecule("C=[N+]=[N-]", at=(0, y), lone_pairs=[2])
s.curly(d1.bond(0, 1), d1.atom(0), bend=0.7)
s.curly(d1.atom(2), d1.bond(1, 2), bend=0.7)
s.arrow((1.8, y), (2.8, y), kind="resonance")
s.molecule("[CH2-][N+]#N", at=(4.6, y), like=d1, lone_pairs=[0, 2])
s.text((2.3, y - 1.4), "both carry formal charges", size=10)
s.draw()
