"""Baeyer-Villiger oxidation of cyclohexanone by a peroxy acid (peroxyacetic acid shown). Top: the
peroxy acid adds to the carbonyl group (proton transfers not shown), giving the tetrahedral Criegee
intermediate. Bottom, the slow step: the ring C-C bond antiperiplanar to the O-O bond migrates to the
proximal oxygen while the O-O bond breaks and carboxylate leaves, and the OH lone pair re-forms the
C=O bond; loss of a proton gives epsilon-caprolactone. The migrating carbon keeps its configuration."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ket = s.molecule("O=C1CCCCC1", at=(0, y), lone_pairs=[0])
pa = s.molecule("CC(=O)OO", at=(3.0, y + 1.0), lone_pairs=[4])
s.curly(pa.atom(4), ket.atom(1), bend=0.4)
s.curly(ket.bond(0, 1), ket.atom(0), bend=-0.8)
s.arrow((5.4, y), (6.8, y), above="H$^+$ shifts", kind="equilibrium")
s.molecule("OC1(OOC(C)=O)CCCCC1", at=(9.6, y))
s.text((9.6, y - 2.2), "Criegee intermediate", size=13)

y = -5.4
cr = s.molecule("OC1(OOC(C)=O)CCCCC1", at=(0, y), lone_pairs=[0, 2, 3])
s.curly(cr.atom(0), cr.bond(0, 1), bend=0.8)
s.curly(cr.bond(1, 7), cr.atom(2), bend=0.6)
s.curly(cr.bond(2, 3), cr.atom(3), bend=0.8)
s.arrow((2.8, y), (4.4, y), below="slow")
s.molecule("[OH+]=C1CCCCCO1", at=(6.2, y))
s.plus((7.8, y))
s.molecule("CC(=O)[O-]", at=(8.8, y))
s.arrow((10.2, y), (11.6, y), above=r"$-$H$^+$")
s.molecule("O=C1CCCCCO1", at=(13.2, y))
s.draw()
