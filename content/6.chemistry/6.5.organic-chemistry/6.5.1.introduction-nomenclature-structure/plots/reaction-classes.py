"""Two polar reactions written with the basic steps. (a) Addition of HBr to ethene in two steps: the
C=C pi electrons take the proton (the H-Br bonding pair stays on bromine), then bromide attacks the
carbocation. (b) Elimination (E2) from bromoethane: in one step ethoxide removes a beta hydrogen,
the C-H bonding pair becomes the C=C pi bond and bromide leaves."""

from wikichem import Scheme

s = Scheme()
# (a) addition
y = 0.0
s.text((-2.6, y), "(a)")
ene = s.molecule("C=C", at=(-1.2, y))
hbr = s.molecule("Br", at=(0.9, y + 0.0), explicit_h=True, lone_pairs=True, rotate=180)
s.curly(ene.bond(0, 1), hbr.atom(1), bend=-0.6)
s.curly(hbr.bond(0, 1), hbr.atom(0), bend=-0.7)
s.arrow((2.3, y), (3.5, y))
cat = s.molecule("C[CH2+]", at=(4.6, y))
br = s.molecule("[Br-]", at=(6.6, y), lone_pairs=True)
s.curly(br.atom(0), cat.atom(1), bend=0.5)
s.arrow((7.6, y), (8.8, y))
s.molecule("CCBr", at=(10.2, y))
s.text((1.0, y - 1.5), "addition")

# (b) elimination
y = -3.6
s.text((-2.6, y), "(b)")
eto = s.molecule("CC[O-]", at=(-1.4, y + 1.2), lone_pairs=[2])
# H-C-C-Br drawn antiperiplanar: H up-left, Br down-right
sub = s.molecule("[H]CCBr", coords=[(-0.5, 0.87), (0, 0), (1, 0), (1.5, -0.87)], at=(0.9, y), lone_pairs=[3])
s.curly(eto.atom(2), sub.atom(0), bend=-0.4)
s.curly(sub.bond(0, 1), sub.bond(1, 2), bend=0.7)
s.curly(sub.bond(2, 3), sub.atom(3), bend=0.6)
s.arrow((3.4, y), (4.6, y))
s.molecule("C=C", at=(5.6, y))
s.plus((6.6, y))
s.text((7.6, y), "EtOH")
s.plus((8.6, y))
s.molecule("[Br-]", at=(9.4, y), lone_pairs=True)
s.text((1.0, y - 1.9), "elimination")
s.draw()
