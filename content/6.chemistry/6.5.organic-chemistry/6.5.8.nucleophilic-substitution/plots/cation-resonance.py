"""Delocalisation that stabilises carbocations. Top: in the methoxymethyl cation a lone pair of
oxygen forms a C=O pi bond, giving an oxocarbenium ion in which every atom has an octet. Bottom: in
the allyl cation the C=C pi electrons move toward the empty p orbital, so that the positive charge
is shared by the two terminal carbons."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("[CH3:1][O:2][CH2+:3]", coords=[(-1.3, 0), (0, 0), (1.3, 0)], show_carbons=[1, 3], lone_pairs=[2])
s.curly(a.atom(2), a.bond(2, 3), bend=-0.8)
s.arrow((2.3, 0), (3.5, 0), kind="resonance")
s.molecule("[CH3:1][O+:2]=[CH2:3]", coords=[(4.5, 0), (5.8, 0), (7.1, 0)], show_carbons=[1, 3], lone_pairs=[2])
s.draw()

s = Scheme()
al = s.molecule("[CH2:1]=[CH:2][CH2+:3]", coords=[(-1.1, -0.4), (0, 0.3), (1.1, -0.4)])
s.curly(al.bond(1, 2), al.bond(2, 3), bend=-0.7)
s.arrow((2.0, 0), (3.2, 0), kind="resonance")
s.molecule("[CH2+:1][CH:2]=[CH2:3]", coords=[(4.1, -0.4), (5.2, 0.3), (6.3, -0.4)])
s.draw()
