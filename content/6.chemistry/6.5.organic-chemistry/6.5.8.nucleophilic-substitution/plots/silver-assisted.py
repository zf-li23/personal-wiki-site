"""Silver-assisted ionization in the AgNO3/ethanol test. Ag+ accepts a lone pair of bromine in
2-bromo-2-methylpropane; the C-Br bond then breaks with both electrons going to bromine, AgBr
precipitates and the tert-butyl cation is captured by nitrate or by ethanol."""

from wikichem import Scheme

s = Scheme()
tb = s.molecule("CC(C)(C)Br", coords=[(-1.3, 0), (0, 0), (0, 1.3), (0, -1.3), (1.4, 0)], lone_pairs=[4])
ag = s.molecule("[Ag+]", at=(3.0, 0.9))
s.curly(tb.atom(4), ag.atom(0), bend=-0.4)
s.curly(tb.bond(1, 4), tb.atom(4), bend=0.7)
s.arrow((3.8, 0), (5.2, 0), below=r"$-$AgBr$\downarrow$")
cat = s.molecule("C[C+](C)C", at=(6.4, 0))
no3 = s.molecule("[O-][N+](=O)[O-]", at=(8.6, 1.2), lone_pairs=[0])
s.curly(no3.atom(0), cat.atom(1), bend=0.4)
s.arrow((9.4, 0), (10.8, 0))
s.molecule("CC(C)(C)O[N+](=O)[O-]", at=(12.4, 0))
s.text((12.4, -1.6), "tert-butyl nitrate", size=10)
s.draw()
