"""Anionic Fries rearrangement (Snieckus). The aryl O-carbamate is lithiated ortho to the carbamate
by sec-butyllithium (directed ortho metalation; lithium omitted). On warming the aryl carbanion adds
to the neighbouring carbamoyl carbonyl group, giving a four-membered cyclic tetrahedral intermediate;
its collapse breaks the C-O(aryl) bond, so the carbamoyl group has moved from oxygen to the ortho
carbon. Work-up protonates the phenoxide to give 2-hydroxy-N,N-diethylbenzamide."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("[c-]1ccccc1OC(=O)N(CC)CC", at=(0.0, y), lone_pairs=[8])
s.curly(a.atom(0), a.atom(7), bend=-0.5)
s.curly(a.bond(7, 8), a.atom(8), bend=0.6)
s.text((0.0, y - 2.6), "ortho-lithiated aryl carbamate")
s.arrow((2.8, y), (4.2, y), above="warm")
t = s.molecule("[O-]C1(N(CC)CC)Oc2ccccc21", at=(6.6, y), lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=0.6)
s.curly(t.bond(1, 7), t.atom(7), bend=-0.6)
s.text((6.6, y - 2.6), "cyclic tetrahedral intermediate")
s.arrow((9.0, y), (10.4, y))
s.molecule("[O-]c1ccccc1C(=O)N(CC)CC", at=(12.8, y))
s.text((12.8, y - 2.6), "2-oxidobenzamide")
s.draw()
