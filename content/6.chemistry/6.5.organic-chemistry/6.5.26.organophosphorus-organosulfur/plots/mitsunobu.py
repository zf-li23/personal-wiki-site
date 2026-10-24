"""Mitsunobu reaction of (S)-butan-2-ol with benzoic acid (phenyl groups on phosphorus written Ph,
the ester groups of DEAD written CO2Et). Top: triphenylphosphine adds to the N=N bond of diethyl
azodicarboxylate (DEAD), giving a betaine whose nitrogen anion deprotonates the acid.
Middle: the alcohol oxygen attacks the phosphonium phosphorus and the hydrazine is released,
giving an alkoxyphosphonium ion: the poor leaving group OH has become O-PPh3+. Bottom: the
carboxylate attacks the carbinol carbon from the back (SN2), so the ester forms with inversion
of configuration, and triphenylphosphine oxide leaves."""

from wikichem import Scheme

s = Scheme()
PH = {1: "Ph", 2: "Ph", 3: "Ph"}
E = "CO$_2$Et"
p = s.molecule("P(*)(*)*", coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0)], lone_pairs=[0], labels=PH)
dead = s.molecule("*N=N*", coords=[(1.6, 1.0), (1.6, 0.0), (2.6, 0.0), (2.6, -1.0)], lone_pairs=[], labels={0: E, 3: E})
s.curly(p.atom(0), dead.atom(1), bend=-0.5)
s.curly(dead.bond(1, 2), dead.atom(2), bend=-0.8)
s.arrow((3.6, 0), (5.0, 0))
x = 7.2
bet = s.molecule("[P+](*)(*)(*)N(*)[N-]*",
                 coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (1.0, 0), (1.0, 1.0), (2.0, 0), (2.0, -1.0)],
                 at=(x, 0), lone_pairs=[6], labels={1: "Ph", 2: "Ph", 3: "Ph", 5: E, 7: E})
s.text((x + 0.5, -2.0), "betaine", size=12)
acid = s.molecule("O=C(O[H])c1ccccc1", coords=[(4.2, 1.0), (4.2, 0.0), (3.2, 0.0), (3.2, 1.0), (5.07, -0.5), (5.07, -1.5), (5.93, -2.0), (6.8, -1.5), (6.8, -0.5), (5.93, 0.0)],
                  at=(x + 0.6, -0.4), lone_pairs=[])
s.curly(bet.atom(6), acid.atom(3), bend=-0.5)
s.curly(acid.bond(2, 3), acid.atom(2), bend=0.6)

y = -5.2
alc = s.molecule("C[C@@H](CC)O[H]", at=(0, y), lone_pairs=[4])
php = s.molecule("[P+](*)(*)(*)N(*)N([H])*",
                 coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0), (1.0, 0), (1.0, 1.0), (2.0, 0), (2.0, -1.0), (3.0, 0)],
                 at=(3.4, y), labels={1: "Ph", 2: "Ph", 3: "Ph", 5: E, 8: E})
s.curly(alc.atom(4), php.atom(0), bend=-0.5)
s.curly(php.bond(0, 4), php.atom(4), bend=-0.6)
s.arrow((8.4, y), (10.6, y), below="$-$EtO$_2$CNHNHCO$_2$Et")

y2 = -10.2
op = s.molecule("C[C@@H](CC)O[P+](*)(*)*", at=(2.2, y2), labels={6: "Ph", 7: "Ph", 8: "Ph"})
bz = s.molecule("[O-]C(=O)c1ccccc1", at=(-2.6, y2 + 0.2), lone_pairs=[0])
s.curly(bz.atom(0), op.atom(1), bend=-0.4)
s.curly(op.bond(1, 4), op.atom(4), bend=-0.6)
s.arrow((5.2, y2), (6.6, y2), above="SN2")
s.molecule("C[C@H](CC)OC(=O)c1ccccc1", at=(10.4, y2))
s.plus((13.6, y2))
s.molecule("O=P(*)(*)*", coords=[(-1.0, 0), (0, 0), (0.5, 0.87), (1.0, 0), (0.5, -0.87)], at=(15.2, y2),
           labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.draw()
