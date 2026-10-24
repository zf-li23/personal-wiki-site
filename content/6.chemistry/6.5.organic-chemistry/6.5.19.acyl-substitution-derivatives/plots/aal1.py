"""Acid-catalysed cleavage of a tert-butyl ester (AAl1). After protonation of the carbonyl oxygen,
the bond between the ester oxygen and the tertiary alkyl group breaks heterolytically: the acid
leaves and the tert-butyl cation remains. The cation loses a proton (isobutene) or is captured by
water (tert-butanol). The alkyl-oxygen bond breaks, unlike in AAc2, where the acyl-oxygen bond does."""

from wikichem import Scheme

s = Scheme()
y = -1.9  # caption line
est = s.molecule("CC(=[OH+])OC(C)(C)C", at=(0, 0))
s.curly(est.bond(3, 4), est.bond(1, 3), bend=0.8)
s.curly(est.bond(1, 2), est.atom(2), bend=-0.8)
s.text((0, y), "protonated tert-butyl acetate")
s.arrow((2.4, 0), (3.8, 0), above="slow")
s.molecule("CC(=O)O", at=(5.0, 0))
s.plus((6.4, 0))
s.molecule("C[C+](C)C", at=(7.6, 0))
s.text((7.6, y), "tert-butyl cation")
s.arrow((8.6, 0), (10.0, 0), above=r"$-\mathrm{H}^+$")
s.molecule("C=C(C)C", at=(11.1, 0))
s.text((11.1, y), "isobutene")
s.draw()
