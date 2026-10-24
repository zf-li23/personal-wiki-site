"""C-C bond cleavage by a class I aldolase (fructose-1,6-bisphosphate aldolase). The C2 ketone of
the substrate is bound as a protonated Schiff base (iminium ion) to the active-site lysine. After the
C4 hydroxy group is deprotonated, the alkoxide re-forms a C=O bond, the C3-C4 bond breaks and its
electrons flow into the iminium ion, giving glyceraldehyde 3-phosphate and a neutral enamine; the
enamine is protonated on C3 and hydrolysed to release dihydroxyacetone phosphate. R = CH(OH)CH2OPO3(2-)."""

from wikichem import Scheme

s = Scheme()
# three-carbon units drawn upright: O, C1, C2, X, X substituent, C3, phosphate
TALL = [(-0.87, 1.0), (0, 0.5), (0, -0.5), (-0.87, -1.0), (-0.87, -2.0), (0.87, -1.0), (0.87, -2.0)]
# atoms: 0 O(C4), 1 C4, 2 R, 3 C3, 4 O(C3), 5 C2, 6 N, 7 Lys, 8 C1, 9 OPO3
sub = s.molecule("[O-]C(*)C(O)C(=[NH+]*)C*", at=(0, 0), labels={2: "R", 7: "Lys", 9: r"OPO$_3^{2-}$"}, lone_pairs=[0])
s.curly(sub.atom(0), sub.bond(0, 1), bend=0.7)
s.curly(sub.bond(1, 3), sub.bond(3, 5), bend=0.7)
s.curly(sub.bond(5, 6), sub.atom(6), bend=0.7)
s.text((0, -2.4), "protonated Schiff base")
s.arrow((2.6, 0), (4.0, 0))
s.molecule("O=C*", at=(5.0, 0.3), labels={2: "R"})
s.text((5.0, -1.3), "G3P")
s.plus((6.3, 0))
s.molecule("OC=C(N*)C*", coords=TALL, at=(8.0, 0.3), labels={4: "Lys", 6: r"OPO$_3^{2-}$"})
s.text((8.0, -2.6), "enamine")
s.arrow((10.0, 0), (11.6, 0), above=r"H$^+$; H$_2$O", below=r"$-$Lys")
s.molecule("OCC(=O)C*", coords=TALL[:4] + TALL[5:], at=(13.2, 0.3), labels={5: r"OPO$_3^{2-}$"})
s.text((13.2, -2.6), "DHAP")
s.draw()
