"""Appel reaction of (S)-4-phenylbutan-2-ol with CBr4 and triphenylphosphine (phenyl groups on
phosphorus written Ph). Top: the phosphorus lone pair attacks a bromine of CBr4 and the C-Br
electrons stay on carbon, giving the bromotriphenylphosphonium ion and the tribromomethanide ion.
Middle: CBr3- removes the O-H proton (bromoform is lost); the alkoxide attacks phosphorus and
bromide leaves, giving an alkoxyphosphonium ion. Bottom: bromide attacks the carbinol carbon from
the back (SN2), so the (R)-bromide forms with inversion and triphenylphosphine oxide leaves, exactly
as in the last step of the Mitsunobu reaction."""

from wikichem import Scheme

s = Scheme()
PH = {1: "Ph", 2: "Ph", 3: "Ph"}
p = s.molecule("P(*)(*)*", coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0)], lone_pairs=[0], labels=PH)
cb = s.molecule("BrC(Br)(Br)Br", coords=[(1.5, 0), (2.5, 0), (2.5, 1.0), (3.5, 0), (2.5, -1.0)], lone_pairs=[])
s.curly(p.atom(0), cb.atom(0), bend=-0.5)
s.curly(cb.bond(0, 1), cb.atom(1), bend=-0.6)
s.arrow((4.3, 0), (5.7, 0))
x = 7.6
s.molecule("Br[P+](*)(*)*", coords=[(1.0, 0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0)], at=(x, 0),
           labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.plus((x + 2.0, 0))
s.molecule("[C-](Br)(Br)Br", at=(x + 3.4, 0), lone_pairs=[])

y = -4.4
# alkoxide C2 at the origin: methyl down (hashed), CH2CH2Ph up-right, O- to the left
AL = [(0, -1.0), (0, 0), (-0.87, 0.5), (0.87, 0.5), (1.73, 0), (2.6, 0.5)]
alk = s.molecule("C[C@H]([O-])CC*", coords=AL, at=(-0.4, y), lone_pairs=[2], labels={5: "Ph"})
pb = s.molecule("Br[P+](*)(*)*", coords=[(1.0, 0), (0, 0), (0, 1.0), (-0.6, -0.8), (0.6, -0.8)], at=(-2.6, y + 2.0),
                lone_pairs=[], labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.curly(alk.atom(2), pb.atom(1), bend=-0.4)
s.curly(pb.bond(0, 1), pb.atom(0), bend=0.6)
s.text((-0.6, y - 1.9), "alkoxide from ROH + CBr$_3^-$ ($-$CHBr$_3$)", size=11)
s.arrow((3.4, y), (4.8, y), above="$-$Br$^-$")
OP = [(0, -1.0), (0, 0), (-0.87, 0.5), (-1.87, 0.5), (-2.37, 1.37), (-2.87, -0.37), (-1.87, -0.5), (0.87, 0.5), (1.73, 0), (2.6, 0.5)]
s.molecule("C[C@H](O[P+](*)(*)*)CC*", coords=OP, at=(8.6, y), labels={4: "Ph", 5: "Ph", 6: "Ph", 9: "Ph"})

y2 = -9.0
op = s.molecule("C[C@H](O[P+](*)(*)*)CC*", coords=OP, at=(2.4, y2), labels={4: "Ph", 5: "Ph", 6: "Ph", 9: "Ph"})
br = s.molecule("[Br-]", at=(4.0, y2 - 0.9), lone_pairs=True)
s.curly(br.atom(0), op.atom(1), bend=-0.5)
s.curly(op.bond(1, 2), op.atom(2), bend=0.6)
s.arrow((6.0, y2), (7.4, y2), above="SN2")
s.molecule("C[C@@H](Br)CC*", coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (0.87, 0.5), (1.73, 0), (2.6, 0.5)], at=(9.0, y2),
           labels={5: "Ph"})
s.plus((11.6, y2))
s.molecule("O=P(*)(*)*", coords=[(-1.0, 0), (0, 0), (0.5, 0.87), (1.0, 0), (0.5, -0.87)], at=(13.2, y2),
           labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.draw()
