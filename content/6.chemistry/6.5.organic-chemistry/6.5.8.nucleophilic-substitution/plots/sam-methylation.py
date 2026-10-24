"""Biological methylation by S-adenosylmethionine (SAM), as in catechol O-methyltransferase. The
phenoxide oxygen of catechol (deprotonated in the active site, Mg2+ not shown) attacks the methyl
carbon of the sulfonium ion; the neutral thioether S-adenosylhomocysteine (SAH) leaves (SN2).
Ado = 5'-deoxyadenosyl, R = CH2CH2CH(NH3+)CO2-."""

from wikichem import Scheme

s = Scheme()
import numpy as np

probe = Scheme().molecule("[O-]c1ccccc1O")
d = probe.xy(0) - probe.xy(1)
cat = s.molecule("[O-]c1ccccc1O", at=(-2.6, 0), rotate=-np.degrees(np.arctan2(d[1], d[0])), lone_pairs=[0])
o = cat.xy(0)
sam = s.molecule("[CH3:1][S+:2]([*:3])[*:4]", coords=[(o[0] + 2.2, o[1]), (o[0] + 3.5, o[1]), (o[0] + 4.1, o[1] + 1.1), (o[0] + 4.1, o[1] - 1.1)], labels={3: "Ado", 4: "R"}, show_carbons=[1], lone_pairs=[2])
s.curly(cat.atom(0), sam.atom(1), bend=0.35)
s.curly(sam.bond(1, 2), sam.atom(2), bend=-0.8)
s.text((-2.6, -2.5), "catechol (phenoxide)", size=10)
s.text((o[0] + 3.5, o[1] - 2.0), "SAM", size=10)
x = o[0] + 5.4
s.arrow((x, 0), (x + 1.4, 0), above="COMT")
s.molecule("COc1ccccc1O", at=(x + 3.6, 0))
s.text((x + 3.6, -2.0), "2-methoxyphenol", size=10)
s.plus((x + 5.4, 0))
s.molecule("[*:3][S:2][*:4]", coords=[(x + 6.2, 0.6), (x + 6.9, -0.3), (x + 7.8, 0.6)], labels={3: "Ado", 4: "R"}, lone_pairs=[2])
s.text((x + 7.0, -2.0), "SAH", size=10)
s.draw()
