"""Hydride transfer in alcohol dehydrogenase. Ethanol is bound to the active-site zinc ion as an
alkoxide. Its electron pair re-forms a C=O bond while one hydrogen of C1 leaves as a hydride to C4 of
the nicotinamide ring of NAD+; the ring electrons move onto the positively charged nitrogen, giving
acetaldehyde and NADH. The enzyme always transfers the pro-R hydrogen of ethanol (shown with
1-deuterioethanol of known configuration) and delivers it to one specific face of C4.
R = ribose-ADP."""

from wikichem import Scheme

s = Scheme()
# ethoxide: 0 CH3, 1 C1, 2 O, then the two H on C1
et = s.molecule("CC[O-]", at=(0, 0.3), show_h=[1], lone_pairs=[2], rotate=-90)
s.text(et.xy(2) + (-1.3, 0.0), "Zn$^{2+}$")
# NAD+: 0 N, 1 C, 2 O, 3 C3, 4 C2, 5 N1, 6 R, 7 C6, 8 C5, 9 C4
nad = s.molecule("NC(=O)C1=C[N+](*)=CC=C1", at=(3.8, -0.6), labels={6: "R"}, rotate=-90)
s.curly(et.atom(2), et.bond(1, 2), bend=0.8)
s.curly(et.bond(1, 4), nad.atom(9), bend=0.3)
s.curly(nad.bond(8, 9), nad.bond(7, 8), bend=0.6)
s.curly(nad.bond(5, 7), nad.atom(5), bend=0.6)
s.text((0.0, -2.9), "ethoxide on Zn$^{2+}$")
s.text((4.0, -2.9), "NAD$^+$")
s.arrow((6.6, -0.4), (8.0, -0.4))
s.molecule("CC=O", at=(9.2, 0.0))
s.text((9.2, -2.9), "acetaldehyde")
s.plus((10.6, -0.4))
s.molecule("NC(=O)C1=CN(*)C=CC1", at=(12.8, -0.6), labels={6: "R"}, like=nad)
s.text((12.8, -2.9), "NADH")
s.draw()
