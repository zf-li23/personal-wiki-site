"""Trifluoromethylation of benzaldehyde with the Ruppert-Prakash reagent (TMS = trimethylsilyl).
Top: a catalytic amount of fluoride adds to silicon, giving a five-coordinate silicate in which the
Si-CF3 bond is weakened; the CF3 group is transferred with its electron pair to the carbonyl carbon
and the C=O electrons go to oxygen. Bottom: the alkoxide attacks silicon of another molecule of
TMS-CF3; the new silicate again transfers CF3 to an aldehyde, so the alkoxide carries the chain
and the product is the TMS ether of the trifluoromethyl carbinol."""

from wikichem import Scheme

s = Scheme()
f = s.molecule("[F-]", at=(-1.6, 0.6), lone_pairs=True)
tm = s.molecule("C[Si](C)(C)C(F)(F)F", coords=[(0, 1.0), (0, 0), (-0.87, -0.5), (0.87, -0.5), (0, -1.1), (-0.8, -1.7), (0.8, -1.7), (0, -2.1)])
s.curly(f.atom(0), tm.atom(1), bend=-0.4)
s.arrow((1.6, 0), (3.0, 0))
x = 5.2
sil = s.molecule("C[Si-](C)(C)(F)C(F)(F)F",
                 coords=[(-0.87, 0.5), (0, 0), (0.87, 0.5), (0, 1.1), (-0.9, -0.4), (0, -1.1), (-0.8, -1.7), (0.8, -1.7), (0, -2.1)], at=(x, 0.4))
ald = s.molecule("O=Cc1ccccc1", at=(x + 2.6, -1.6), lone_pairs=[0])
s.curly(sil.bond(1, 5), ald.atom(1), bend=0.5)
s.curly(ald.bond(0, 1), ald.atom(0), bend=0.6)
s.arrow((x + 5.0, 0), (x + 6.4, 0), below="$-$TMSF")
s.molecule("[O-]C(C(F)(F)F)c1ccccc1", at=(x + 8.6, 0))

y = -5.6
alk = s.molecule("[O-]C(C(F)(F)F)c1ccccc1", at=(0, y), lone_pairs=[0])
tm2 = s.molecule("C[Si](C)(C)C(F)(F)F", coords=[(0, 1.0), (0, 0), (-0.87, -0.5), (0.87, -0.5), (0, -1.1), (-0.8, -1.7), (0.8, -1.7), (0, -2.1)],
                 at=(5.0, y + 0.6))
s.curly(alk.atom(0), tm2.atom(1), bend=-0.4)
s.arrow((6.4, y), (7.8, y))
s.molecule("C[Si-](C)(C)(OC(C(F)(F)F)c1ccccc1)C(F)(F)F", at=(10.8, y))
s.text((10.8, y - 3.0), "transfers CF$_3^-$ to the next aldehyde", size=11)
s.arrow((14.0, y), (15.4, y), below="+ PhCHO")
s.molecule("C[Si](C)(C)OC(C(F)(F)F)c1ccccc1", at=(18.0, y))
s.draw()
