"""18O labelling in the acid-catalysed esterification of acetic acid with methanol. The labelled
oxygen of methanol attacks the carbonyl carbon of the protonated acid; after proton transfer the
water that leaves contains an oxygen of the acid, so the label ends up in the ester (as
CH3C(=O)-18OCH3) and not in the water: the acyl C-O bond breaks, not the alkyl C-O bond of methanol."""

from wikichem import Scheme

L = r"$^{18}$O"
s = Scheme()
# atoms: 0 CH3, 1 C, 2 O+ (protonated carbonyl), 3 OH
acid = s.molecule("CC(=[OH+])O", at=(0, 0), rotate=90)
meoh = s.molecule("C[OH]", at=(-2.0, -1.3), labels={1: L + "H"}, lone_pairs=[1])
s.curly(meoh.atom(1), acid.atom(1), bend=-0.4)
s.curly(acid.bond(1, 2), acid.atom(2), bend=0.8)
s.arrow((1.6, 0), (2.8, 0), below="proton transfer")
# tetrahedral intermediate: 0 CH3, 1 C, 2 OH, 3 OH2+, 4 18O, 5 CH3
ti = s.molecule("CC(O)([OH2+])OC", at=(4.6, 0), labels={4: L})
s.curly(ti.bond(1, 3), ti.atom(3), bend=0.7)
s.arrow((6.6, 0), (7.8, 0), below=r"$-$H$_2$O, $-$H$^+$")
s.molecule("CC(=O)OC", at=(9.6, 0), labels={3: L})
s.text((4.6, -2.0), "the leaving water carries an acid oxygen")
s.draw()
