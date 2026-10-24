"""E1 with rearrangement: solvolysis of 1-bromo-2,2-dimethylpropane (neopentyl bromide). Departure of
bromide and migration of a methyl group with its bonding pair are concerted, so no primary
carbocation is formed; the tertiary 2-methylbutan-2-yl cation then loses a proton from the CH2
group to ethanol, giving the Zaitsev product 2-methylbut-2-ene."""

from wikichem import Scheme

s = Scheme()
sub = s.molecule("CC(C)(C)CBr", at=(0, 0), lone_pairs=[5])
s.curly(sub.bond(1, 2), sub.atom(4), bend=0.6)
s.curly(sub.bond(4, 5), sub.atom(5), bend=0.7)
s.text((0, -1.6), "neopentyl bromide")
s.arrow((2.0, 0), (3.6, 0), above="EtOH", below=r"$-$Br$^-$")
cat = s.molecule("C[C+](C)C([H])C", coords=[(0, 1), (0, 0), (-0.87, -0.5), (0.87, -0.5), (0.87, -1.5), (1.73, 0)], at=(5.0, 0.2))
eth = s.molecule("CCO", at=(7.6, -1.6), lone_pairs=[2], rotate=180)
s.curly(eth.atom(2), cat.atom(4), bend=-0.4)
s.curly(cat.bond(3, 4), cat.bond(1, 3), bend=-0.8)
s.text((5.0, -2.2), "tertiary cation")
s.arrow((8.8, 0), (10.2, 0), below=r"$-$EtOH$_2^+$")
s.molecule("CC(C)=CC", at=(11.8, 0))
s.text((11.8, -1.6), "2-methylbut-2-ene")
s.draw()
