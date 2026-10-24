"""Cyanide-catalysed benzoin condensation (Lapworth mechanism). Top: cyanide adds to benzaldehyde;
proton transfer from carbon to oxygen gives a carbanion stabilised by the nitrile and the phenyl
ring: the former carbonyl carbon is now nucleophilic (umpolung). Middle: the carbanion adds to a
second benzaldehyde. Bottom: after proton transfer, the alkoxide re-forms the C=O bond and expels
cyanide, which is regenerated as the catalyst."""

from wikichem import Scheme

s = Scheme(scale=0.36)
y = 0.0
cn = s.molecule("[C-]#N", at=(-3.6, y + 1.0), lone_pairs=[0])
ald = s.molecule("O=Cc1ccccc1", at=(-0.6, y), lone_pairs=[0])
s.curly(cn.atom(0), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), ald.atom(0), bend=-0.9)
s.arrow((1.6, y), (3.0, y), kind="equilibrium")
s.molecule("N#CC([O-])c1ccccc1", at=(5.4, y))
s.arrow((7.6, y), (9.2, y), above=r"H$^+$ shift", kind="equilibrium")
s.molecule("N#C[C-](O)c1ccccc1", at=(11.6, y))

y = -6.6
ca = s.molecule("N#C[C-](O)c1ccccc1", at=(0, y), lone_pairs=[2])
ald2 = s.molecule("O=Cc1ccccc1", at=(3.4, y + 1.8), lone_pairs=[0])
s.curly(ca.atom(2), ald2.atom(1), bend=-0.4)
s.curly(ald2.bond(0, 1), ald2.atom(0), bend=0.9)
s.arrow((5.8, y), (7.2, y), kind="equilibrium")
s.molecule("N#CC(O)(c1ccccc1)C([O-])c1ccccc1", at=(10.4, y))

y = -13.2
s.arrow((-3.6, y), (-2.0, y), above=r"H$^+$ shift", kind="equilibrium")
al = s.molecule("N#CC([O-])(c1ccccc1)C(O)c1ccccc1", at=(1.6, y), lone_pairs=[3])
s.curly(al.atom(3), al.bond(2, 3), bend=0.8)
s.curly(al.bond(1, 2), al.atom(1), bend=0.8)
s.arrow((5.0, y), (6.6, y))
s.molecule("O=C(c1ccccc1)C(O)c1ccccc1", at=(9.4, y))
s.plus((12.8, y))
s.molecule("[C-]#N", at=(14.2, y), lone_pairs=[0])
s.draw()
