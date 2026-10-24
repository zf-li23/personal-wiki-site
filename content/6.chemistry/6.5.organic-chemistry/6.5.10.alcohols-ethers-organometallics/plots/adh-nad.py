"""Alcohol dehydrogenase: ethanol is oxidized by NAD+. In the active site ethanol is bound to zinc as
the alkoxide; its oxygen lone pair forms the C=O bond while the C-H bonding pair moves as a hydride
to C4 of the nicotinamide ring of NAD+ (on one face, stereospecifically); the ring pi electrons move
onto the positive nitrogen, giving acetaldehyde and NADH (a 1,4-dihydropyridine). R = the
ADP-ribose part of the coenzyme."""

from wikichem import Scheme

s = Scheme()
eo = s.molecule("C[CH]([H])[O-]", coords=[(-0.87, -0.5), (0, 0), (0.87, -0.5), (0, 1)], at=(0, 0), lone_pairs=[3])
s.text((0.0, 2.1), r"Zn$^{2+}$", size=11)
# atoms: 0 N, 1 C(=O), 2 O, 3 C3, 4 C2, 5 N+, 6 R, 7 C6, 8 C5, 9 C4
nad = s.molecule("NC(=O)C1=C[N+](*)=CC=C1", at=(3.0, -1.6), labels={6: "R"}, rotate=0)
s.curly(eo.atom(3), eo.bond(1, 3), bend=0.8)
s.curly(eo.bond(1, 2), nad.atom(9), bend=-0.3)
s.curly(nad.bond(9, 8), nad.bond(8, 7), bend=-0.7)
s.curly(nad.bond(7, 5), nad.atom(5), bend=-0.7)
s.text((3.6, -4.4), r"NAD$^+$")
s.arrow((5.4, -0.6), (6.8, -0.6))
s.molecule("CC=O", at=(7.8, 0.6))
s.plus((7.8, -0.6))
s.molecule("NC(=O)C1=CN(*)C=CC1", at=(9.4, -1.6), labels={6: "R"})
s.text((10.0, -4.4), "NADH")
s.draw()
