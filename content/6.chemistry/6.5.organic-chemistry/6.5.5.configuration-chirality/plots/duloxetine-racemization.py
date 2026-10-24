"""Recycling the unwanted enantiomer in the duloxetine resolution. In hydrochloric acid (the amine is
then protonated; R = CH2CH2NH2(+)CH3) the hydroxy group of (R)-3-(methylamino)-1-(thiophen-2-yl)propan-1-ol
is protonated and leaves as water (SN1). The resulting secondary carbocation is planar and strongly
stabilised by the adjacent thiophene ring, like a benzylic cation. Water adds to either face with
equal probability, so the alcohol comes back as the racemate, which is resolved again with
(S)-mandelic acid."""

from wikichem import Scheme

s = Scheme()
R = {2: "R"}
# atoms: 0 O, 1 C (stereocentre), 2 R, 3-7 thiophene (7 = S)
a = s.molecule("O[C@H](*)c1cccs1", at=(0, 0), lone_pairs=[0], labels=R)
h3o = s.molecule("[OH3+]", at=(-3.8, 1.9), show_h=[0])
s.curly(a.atom(0), h3o.h(0, 0), bend=0.4)
s.curly(h3o.bond(0, 1), h3o.atom(0), bend=-0.8)
s.text((0, -2.0), "(R)-alcohol")
s.arrow((2.4, 0), (3.8, 0), kind="equilibrium")
b = s.molecule("[OH2+][C@H](*)c1cccs1", at=(6.2, 0), labels=R)
s.curly(b.bond(0, 1), b.atom(0), bend=1.2)
s.text((6.4, -2.0), "oxonium ion")
s.arrow((8.5, 0), (9.9, 0), kind="equilibrium", below=r"$-$H$_2$O")
s.molecule("[CH+](*)c1cccs1", at=(12.0, 0), labels={1: "R"})
s.text((12.2, -2.0), "planar cation")
s.arrow((14.0, 0), (15.4, 0), kind="equilibrium", above=r"$+$H$_2$O", below=r"$-$H$^+$")
s.molecule("OC(*)c1cccs1", at=(17.8, 0), labels=R)
s.text((18.0, -2.0), "(R) + (S), 1 : 1")
s.text((9.0, -3.0), r"R = CH$_2$CH$_2$NH$_2^+$CH$_3$")
s.draw()
