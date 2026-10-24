"""Base-catalysed isomerization of an aldose into a ketose through the enediol (the Lobry de
Bruyn-van Ekenstein rearrangement), shown for D-glyceraldehyde and dihydroxyacetone, the
smallest aldose-ketose pair. Top: hydroxide removes the alpha hydrogen of C2, which is acidic
because it lies next to the carbonyl group; the enolate is protonated on oxygen, giving the
1,2-enediol. C2 is planar in the enediol, so reprotonating it on either face leads back to the
aldose with either configuration at C2 (epimerization). Bottom: removing the proton of the C2
hydroxyl and protonating C1 instead turns the enediol into the ketose."""

from wikichem import Scheme

s = Scheme()
y = 0.0
oh = s.molecule("[OH-]", at=(-1.6, y + 1.2), lone_pairs=True)
ald = s.molecule("O=CC(O)CO", at=(0.6, y), show_h=[2], lone_pairs=[0])
s.curly(oh.atom(0), ald.h(2), bend=-0.4)
s.curly(ald.bond(2, 6), ald.bond(1, 2), bend=0.6)
s.curly(ald.bond(0, 1), ald.atom(0), bend=-0.6)
s.text((0.6, y - 1.8), "D-glyceraldehyde")
s.arrow((2.6, y), (4.0, y), above=r"$-$H$_2$O", kind="equilibrium")
s.molecule("[O-]C=C(O)CO", at=(5.8, y))
s.text((5.8, y - 1.8), "enediolate")
s.arrow((7.6, y), (9.0, y), above=r"H$_2$O", kind="equilibrium")
s.molecule("OC=C(O)CO", at=(10.8, y))
s.text((10.8, y - 1.8), "1,2-enediol")

y = -5.2
end = s.molecule("OC=C(O)CO", at=(1.2, y), show_h=[3], lone_pairs=[3])
oh2 = s.molecule("[OH-]", at=(-1.6, y - 1.5), lone_pairs=True)
water = s.molecule("[H]O[H]", at=(-0.3, y + 1.75), coords=[(0.55, -0.3), (0.0, 0.0), (-0.55, -0.3)], lone_pairs=[1])
s.curly(oh2.atom(0), end.h(3), bend=-0.4)
s.curly(end.bond(3, 6), end.bond(2, 3), bend=-0.5)
s.curly(end.bond(1, 2), water.atom(0), bend=-0.5)
s.curly(water.bond(0, 1), water.atom(1), bend=0.6)
s.arrow((3.4, y), (4.8, y), kind="equilibrium")
s.molecule("OCC(=O)CO", at=(7.6, y))
s.text((7.6, y - 1.6), "dihydroxyacetone")
s.draw()
