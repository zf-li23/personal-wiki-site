"""Why direct alkylation of ammonia gives mixtures. Top: ammonia attacks bromoethane from the back
side of the C-Br bond (SN2), giving the ethylammonium ion; proton exchange with ammonia releases
ethylamine. Bottom: ethylamine is at least as good a nucleophile as ammonia (the alkyl group donates
electrons), so it competes for the remaining bromoethane, and the sequence continues to the tertiary
amine and the quaternary ammonium salt."""

from wikichem import Scheme

EB = [(0.0, 0.0), (0.0, -1.0), (1.0, -1.0)]  # CH3 above, CH2, Br to the right

s = Scheme()
y = 0.0
nh3 = s.molecule("[H]N([H])[H]", coords=[(-0.6, 0.8), (0, 0), (-0.95, -0.1), (-0.4, -0.85)], at=(-1.2, y), lone_pairs=[1])
eb = s.molecule("CCBr", coords=EB, at=(0.4, y + 1.0), lone_pairs=[2])
s.curly(nh3.atom(1), eb.atom(1), bend=-0.3)
s.curly(eb.bond(1, 2), eb.atom(2), bend=-0.6)
s.arrow((2.4, y), (3.8, y), below=r"$-$Br$^-$")
s.molecule("CC[NH3+]", at=(5.5, y))
s.arrow((6.6, y), (8.0, y), kind="equilibrium", above=r"NH$_3$", below=r"$-$NH$_4^+$")
s.molecule("CCN", at=(9.9, y))
s.text((9.9, y - 1.2), "ethylamine")

y = -3.4
ea = s.molecule("[H]N([H])CC", coords=[(-0.35, 0.95), (0, 0), (-0.35, -0.95), (-1.0, 0), (-1.87, 0.5)], at=(-1.2, y), lone_pairs=[1])
eb2 = s.molecule("CCBr", coords=EB, at=(0.4, y + 1.0), lone_pairs=[2])
s.curly(ea.atom(1), eb2.atom(1), bend=-0.3)
s.curly(eb2.bond(1, 2), eb2.atom(2), bend=-0.6)
s.arrow((2.4, y), (3.8, y), below=r"$-$Br$^-$")
s.molecule("CC[NH2+]CC", at=(5.8, y))
s.arrow((7.4, y), (9.0, y), above="EtBr", below="repeat")
s.text((10.8, y), r"Et$_3$N, Et$_4$N$^+$")
s.draw()
