"""Addition of HBr to 1,3-butadiene. Protonation at C1 gives an allylic cation whose charge is shared
by C2 and C4 (two resonance structures). Bromide attacks C2 (1,2-adduct) or C4 (1,4-adduct)."""

from wikichem import Scheme

s = Scheme()
diene = s.molecule("C=CC=C", at=(0, 0))
hbr = s.molecule("[H]Br", at=(1.8, 1.0), coords=[(-0.5, 0.0), (0.5, 0.0)])
s.curly(diene.bond(0, 1), hbr.atom(0), bend=-0.4)
s.curly(hbr.bond(0, 1), hbr.atom(1), bend=-0.8)
s.text((0, -1.4), "1,3-butadiene")
s.arrow((2.6, 0), (3.8, 0))
c1 = s.molecule("CCC=C", at=(5.4, 0))
s.text(c1.xy(1) + (0, -0.45), "+")
s.curly(c1.bond(2, 3), c1.bond(1, 2), bend=-0.7)
s.arrow((7.0, 0), (8.2, 0), kind="resonance")
c2 = s.molecule("CC=CC", at=(9.8, 0))
s.text(c2.xy(3) + (0.0, 0.45), "+")
s.text((7.6, -1.4), "allylic cation")
s.arrow((11.2, 0.4), (12.6, 1.2), above="C2")
s.arrow((11.2, -0.4), (12.6, -1.2), below="C4")
s.molecule("CC(Br)C=C", at=(14.0, 1.6))
s.molecule("CC=CCBr", at=(14.2, -1.7))
s.text((14.0, 0.1), "1,2-adduct")
s.text((14.2, -2.9), "1,4-adduct")
s.draw()
