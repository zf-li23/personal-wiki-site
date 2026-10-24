"""Carbon-carbon bond cleavage in the haloform reaction. Hydroxide adds to the carbonyl carbon of
1,1,1-tribromoacetone; the tetrahedral alkoxide collapses, re-forming C=O and expelling CBr3-, which
is stabilised by the three bromine atoms. Proton transfer from the acid to CBr3- gives bromoform
and acetate."""

from wikichem import Scheme

s = Scheme()
oh = s.molecule("[OH-]", at=(-2.0, 1.4), lone_pairs=True)
k = s.molecule("CC(=O)C(Br)(Br)Br", at=(0, 0), lone_pairs=[2])
s.curly(oh.atom(0), k.atom(1), bend=-0.4)
s.curly(k.bond(1, 2), k.atom(2), bend=-0.7)
s.arrow((1.8, 0), (3.2, 0), kind="equilibrium")
t = s.molecule("CC([O-])(O)C(Br)(Br)Br", at=(5.0, 0), lone_pairs=[2])
s.curly(t.atom(2), t.bond(1, 2), bend=0.7)
s.curly(t.bond(1, 4), t.atom(4), bend=0.7)
s.text((5.0, -2.3), "tetrahedral intermediate")
s.arrow((6.9, 0), (8.3, 0))
s.molecule("CC(=O)O", at=(9.6, 0.2))
s.plus((10.9, 0))
s.molecule("Br[C-](Br)Br", at=(12.2, 0))

y = -4.0
ac = s.molecule("CC(=O)O[H]", coords=[(0, 0), (0.87, 0.5), (0.87, 1.5), (1.73, 0), (2.6, 0.5)], at=(1.0, y))
cb = s.molecule("Br[C-](Br)Br", at=(5.0, y), lone_pairs=[1])
s.curly(cb.atom(1), ac.atom(4), bend=0.4)
s.curly(ac.bond(3, 4), ac.atom(3), bend=0.8)
s.arrow((7.0, y), (8.4, y), above="proton transfer")
s.molecule("CC(=O)[O-]", at=(9.6, y + 0.2))
s.plus((11.1, y))
s.molecule("BrC(Br)Br", at=(12.2, y))
s.text((12.2, y - 1.5), "bromoform")
s.draw()
