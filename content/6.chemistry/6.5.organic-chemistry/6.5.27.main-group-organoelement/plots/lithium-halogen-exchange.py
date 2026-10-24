"""Lithium-halogen exchange of iodobenzene with butyllithium, and why tert-butyllithium is used in
two equivalents. Top: the C-Li electrons of butyllithium attack iodine, giving an iodine 'ate'
complex [Ph-I-Bu]- Li+ (observed by Reich at low temperature); the Ph-I bond then breaks toward the
phenyl carbon, giving phenyllithium and 1-iodobutane. The equilibrium lies on the side of the more
stable (sp2) carbanion. Bottom: with tert-butyllithium the tert-butyl bromide formed would be
attacked by the aryllithium; a second molecule of t-BuLi removes it at once by E2 (its C-Li
electrons take a beta-hydrogen), giving isobutene, isobutane and LiBr and making the exchange
irreversible."""

import math

from wikichem import Scheme


def facing(smiles, k, angle):
    m = Scheme().molecule(smiles)
    v = m.xy(k) - m.coords.mean(axis=0)
    return angle - math.degrees(math.atan2(v[1], v[0]))


s = Scheme()
ar = s.molecule("Ic1ccccc1", at=(0, 0), rotate=facing("Ic1ccccc1", 0, 0), lone_pairs=[0])
bu = s.molecule("CCCC[Li]", coords=[(4.4, 1.6), (3.9, 0.73), (4.4, -0.13), (3.9, -1.0), (3.0, -1.5)])
s.curly(bu.bond(3, 4), ar.atom(0), bend=-0.6)
s.arrow((5.0, 0), (6.4, 0))
x = 9.0
ate = s.molecule("CCCC[I-]c1ccccc1", at=(x + 0.6, 0))
s.molecule("[Li+]", at=(x - 2.4, 1.0))
s.text((x + 0.6, -1.6), "iodine ate complex", size=11)
s.arrow((x + 4.4, 0), (x + 5.8, 0), kind="equilibrium")
x2 = x + 8.0
s.molecule("[Li]c1ccccc1", at=(x2, 0))
s.plus((x2 + 2.0, 0))
s.molecule("CCCCI", at=(x2 + 4.2, 0))

y = -4.4
tb = s.molecule("CC(C)(C)[Li]", coords=[(-0.87, 0.5), (0, 0), (0, 1.0), (0.87, 0.5), (0, -1.0)], at=(0, y))
br = s.molecule("[H]CC(C)(C)Br", coords=[(1.0, -1.2), (2.0, -1.2), (2.5, -0.33), (1.8, 0.4), (3.0, 0.5), (3.5, -0.33)],
                at=(0, y), lone_pairs=[])
s.curly(tb.bond(1, 4), br.atom(0), bend=0.5)
s.curly(br.bond(0, 1), br.bond(1, 2), bend=0.7)
s.curly(br.bond(2, 5), br.atom(5), bend=-0.5)
s.arrow((4.4, y), (5.8, y), above="E2")
x = 7.0
s.molecule("CC(C)C", at=(x, y))
s.plus((x + 1.4, y))
s.molecule("C=C(C)C", at=(x + 2.8, y))
s.plus((x + 4.2, y))
s.text((x + 5.2, y), "LiBr", size=12)
s.draw()
