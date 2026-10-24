"""Cyanide as an ambident nucleophile. Top: with NaCN in a polar aprotic solvent the carbon lone pair
attacks bromoethane (SN2), giving propanenitrile. Bottom: in silver cyanide the carbon is bonded to
silver, Ag+ also pulls bromide away (AgBr precipitates) and the nitrogen lone pair attacks, giving
ethyl isocyanide."""

from wikichem import Scheme

s = Scheme()
cn = s.molecule("[C-]#N", coords=[(-2.6, 0), (-3.7, 0)], lone_pairs=[0, 1], show_carbons=[0])
eb = s.molecule("C(C)Br", coords=[(0, 0), (-0.5, 1.2), (1.4, 0)], lone_pairs=[2])
s.curly(cn.atom(0), eb.atom(0), bend=0.3)
s.curly(eb.bond(0, 2), eb.atom(2), bend=-0.8)
s.arrow((2.6, 0.3), (4.0, 0.3), above="DMSO", below=r"$-$Br$^-$")
s.molecule("CCC#N", at=(5.6, 0.3))
s.text((5.6, -0.8), "propanenitrile", size=10)
s.draw()

s = Scheme()
ag = s.molecule("[Ag]C#N", coords=[(-5.0, 0), (-3.8, 0), (-2.6, 0)], lone_pairs=[2], show_carbons=[1])
eb = s.molecule("C(C)Br", coords=[(0, 0), (-0.5, 1.2), (1.4, 0)], lone_pairs=[2])
s.curly(ag.atom(2), eb.atom(0), bend=0.3)
s.curly(eb.bond(0, 2), eb.atom(2), bend=-0.8)
s.arrow((2.6, 0.3), (4.0, 0.3), below=r"$-$AgBr$\downarrow$")
s.molecule("CC[N+]#[C-]", at=(6.4, 0.3), lone_pairs=[3], show_carbons=[3])
s.text((6.4, -0.8), "ethyl isocyanide", size=10)
s.draw()
