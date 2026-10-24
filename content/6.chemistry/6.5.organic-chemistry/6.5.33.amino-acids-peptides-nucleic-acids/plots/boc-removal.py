"""Removal of the Boc group with trifluoroacetic acid. The carbamate carbonyl oxygen is
protonated; the tert-butyl cation leaves (an SN1-type ionization assisted by the stable tertiary
cation, as in the AAl1 ester cleavage); the carbamic acid loses CO2, releasing the amine as its
ammonium salt. The tert-butyl cation loses a proton to give isobutene or is captured by a
scavenger (water, triisopropylsilane, thiols) so that it does not alkylate Trp, Met, Tyr or Cys."""

from wikichem import Scheme

s = Scheme()
y = 0.0
b = s.molecule("CC(C)(C)OC(=[OH+])NC", at=(0.0, y))
# atoms: 0 C,1 C,2 C,3 C,4 O,5 C,6 O+,7 N,8 C
s.curly(b.bond(1, 4), b.atom(4), bend=0.6)
s.text((0.0, y - 1.8), "protonated Boc carbamate")
s.arrow((2.2, y), (3.6, y), above="slow")
s.molecule("C[C+](C)C", at=(4.6, y + 0.8))
s.plus((6.0, y + 0.6))
ca = s.molecule("OC(=O)NC", at=(7.6, y + 0.4))
s.text((7.6, y - 1.1), "carbamic acid")
s.arrow((9.2, y), (10.6, y), above=r"$-$CO$_2$")
s.molecule("C[NH3+]", at=(11.6, y))
s.text((4.6, y - 1.3), "to isobutene\nor scavenger", size=9)
s.draw()
