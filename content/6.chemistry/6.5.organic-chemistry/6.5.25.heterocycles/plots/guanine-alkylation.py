"""Alkylation of guanine at N7 (9-methylguanine as a model of the nucleoside). The lone pair of N7,
the most nucleophilic site of the bases and exposed in the major groove of DNA, attacks the methyl
carbon of methyl methanesulfonate in an SN2 reaction, and methanesulfonate leaves. The
7-methylguaninium ion has a positively charged imidazole ring, which weakens the N-glycosidic bond
and leads to depurination."""

from wikichem import Scheme

s = Scheme()
g = s.molecule("Cn1cnc2c1nc(N)[nH]c2=O", at=(0, 0), lone_pairs=[3])
ms = s.molecule("COS(C)(=O)=O", at=(g.xy(3)[0] + 0.8, g.xy(3)[1] + 2.0), lone_pairs=[1])
s.curly(g.atom(3), ms.atom(0), bend=-0.4)
s.curly(ms.bond(0, 1), ms.atom(1), bend=-0.6)
s.text((0, -2.2), "guanine (N9-methyl)")
s.arrow((3.0, 0), (4.4, 0), below=r"$-$MsO$^-$")
s.molecule("Cn1c[n+](C)c2c1nc(N)[nH]c2=O", at=(6.8, 0))
s.text((6.8, -2.2), "7-methylguaninium")
s.draw()
