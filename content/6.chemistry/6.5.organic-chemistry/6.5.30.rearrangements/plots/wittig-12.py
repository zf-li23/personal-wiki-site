"""[1,2]-Wittig rearrangement of dibenzyl ether. Butyllithium removes a benzylic proton next to
oxygen. The concerted 1,2-shift of an anion is symmetry-forbidden, so the O-CH2Ph bond breaks
homolytically instead (fishhook arrows): a ketyl radical anion and a benzyl radical form a radical
pair, which recombines at carbon within the solvent cage to give the lithium alkoxide of
1,2-diphenylethanol. The radical stability of the migrating group sets the migratory aptitude."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
s.molecule("C(OCc1ccccc1)c1ccccc1", at=(0.0, y))
s.text((0.0, y - 2.6), "dibenzyl ether")
s.arrow((3.9, y), (5.3, y), above="BuLi", below="THF")
a = s.molecule("[CH-](OCc1ccccc1)c1ccccc1", at=(9.3, y))
s.curly(a.bond(1, 2), a.atom(2), bend=-0.7, single=True)
s.curly(a.bond(1, 2), a.atom(1), bend=0.7, single=True)
s.text((9.3, y - 2.6), r"$\alpha$-lithio ether (Li$^+$)")
s.arrow((13.2, y), (14.6, y))
k = s.molecule("[O-][CH]c1ccccc1", at=(16.4, y - 0.4))
b = s.molecule("[CH2]c1ccccc1", at=(18.8, y + 1.0))
mid = (k.xy(1) + b.xy(0)) / 2
s.curly(k.atom(1), mid, bend=-0.4, single=True)
s.curly(b.atom(0), mid, bend=0.4, single=True)
s.text((17.6, y - 2.6), "radical pair (solvent cage)")
s.arrow((20.8, y), (22.2, y))
s.molecule("[O-]C(Cc1ccccc1)c1ccccc1", at=(25.4, y))
s.text((25.4, y - 2.6), "lithium alkoxide")
s.draw()
