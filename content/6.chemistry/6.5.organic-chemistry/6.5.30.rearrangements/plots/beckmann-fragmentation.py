"""Beckmann fragmentation of the oxime of 3,3-dimethylbutan-2-one (methyl tert-butyl ketone). In the
protonated (E)-oxime the tert-butyl group is anti to the leaving group. Because it can leave as a
stable tertiary carbocation, the C-C bond breaks instead of migrating: its electron pair forms the
third bond between C and N as water leaves from nitrogen, giving acetonitrile and the tert-butyl
cation, which loses a proton to give 2-methylpropene (or is captured by a nucleophile)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
m = s.molecule("CC(C)(C)/C(C)=N/[OH2+]", at=(0.0, y))
s.curly(m.bond(1, 4), m.bond(4, 6), bend=-0.6)
s.curly(m.bond(6, 7), m.atom(7), bend=-0.6)
s.text((0.0, y - 2.2), "protonated (E)-oxime")
s.arrow((2.4, y), (3.9, y), above=r"$-$H$_2$O")
s.molecule("CC#N", at=(5.2, y))
s.plus((6.6, y))
s.molecule("[C+](C)(C)C", at=(7.8, y))
s.text((6.6, y - 2.2), r"acetonitrile + $t$-Bu$^+$")
s.arrow((9.2, y), (10.6, y), above=r"$-$H$^+$")
s.molecule("C=C(C)C", at=(11.8, y))
s.text((11.8, y - 2.2), "2-methylpropene")
s.draw()
