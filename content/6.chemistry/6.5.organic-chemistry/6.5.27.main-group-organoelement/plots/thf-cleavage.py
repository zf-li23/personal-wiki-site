"""Decomposition of THF by butyllithium. Top: the C-Li electrons of n-BuLi remove a proton from a
carbon next to the ring oxygen; the C-H electrons stay on that carbon, giving 2-lithiotetrahydrofuran
and butane. Bottom: the lithiated THF falls apart by a reverse [3+2] cycloaddition: the C-Li
electrons form a C=C bond, the opposite C-C bond becomes the C=C bond of ethylene and the C-O
bond breaks toward oxygen, giving ethylene and the lithium enolate of acetaldehyde."""

from wikichem import Scheme

PENT = [(0, 0.85), (0.81, 0.26), (0.5, -0.69), (-0.5, -0.69), (-0.81, 0.26)]
s = Scheme()
thf = s.molecule("[H]C1CCCO1", coords=[(1.6, 0.9)] + PENT[1:] + [PENT[0]], lone_pairs=[5])
bu = s.molecule("CCCC[Li]", coords=[(3.8, 1.7), (3.3, 0.83), (3.8, -0.03), (3.3, -0.9), (2.3, -0.9)])
s.curly(bu.bond(3, 4), thf.atom(0), bend=0.6)
s.curly(thf.bond(0, 1), thf.atom(1), bend=0.6)
s.arrow((4.6, 0), (6.0, 0), below="$-$C$_4$H$_{10}$")
s.molecule("[Li]C1CCCO1", coords=[(1.8, 0.8)] + PENT[1:] + [PENT[0]], at=(7.6, 0))

y = -3.8
li = s.molecule("[Li]C1CCCO1", coords=[(1.8, 0.8)] + PENT[1:] + [PENT[0]], at=(0, y), lone_pairs=[5])
s.curly(li.bond(0, 1), li.bond(1, 2), bend=-0.6)
s.curly(li.bond(2, 3), li.bond(3, 4), bend=-0.6)
s.curly(li.bond(4, 5), li.atom(5), bend=0.6)
s.text((0, y - 1.5), "reverse [3+2]", size=11)
s.arrow((2.6, y), (4.0, y))
s.molecule("C=C", at=(5.2, y))
s.plus((6.5, y))
s.molecule("C=CO[Li]", at=(8.6, y))
s.draw()
