"""Why thalidomide racemizes in the body. Its stereocentre (C3 of the glutarimide ring) carries an
acidic C-H between the imide carbonyl group and the phthalimide nitrogen (NPhth = phthalimido). A base
(in vivo: water, phosphate, the side chains of proteins) removes this proton; the electrons move onto
the carbonyl oxygen and the stereocentre becomes the planar sp2 carbon of an enolate. Reprotonation on
either face gives back (R) or (S) with equal probability, so either pure enantiomer turns into the
racemate within hours under physiological conditions."""

from wikichem import Scheme

s = Scheme()
PH = {5: "NPhth"}
# atoms: 0 O, 1 C, 2 C, 3 C, 4 C3 (stereocentre), 5 NPhth, 6 C(=O), 7 O, 8 NH, 9 H on C3
r = s.molecule("O=C1CC[C@@H](*)C(=O)N1", at=(0, 0), show_h=[4], lone_pairs=[7], labels=PH)
base = s.molecule("[OH-]", at=(-2.2, -2.4), lone_pairs=True)
s.curly(base.atom(0), r.h(4), bend=-0.4)
s.curly(r.bond(4, 9), r.bond(4, 6), bend=0.6)
s.curly(r.bond(6, 7), r.atom(7), bend=0.6)
s.text((0.6, -3.2), "(R)-thalidomide")
s.arrow((2.4, 0), (3.8, 0), kind="equilibrium", below=r"$-$H$_2$O")
s.molecule("[O-]C1=C(*)CCC(=O)N1", at=(5.8, 0), labels={3: "NPhth"})
s.text((5.8, -3.2), "planar enolate")
s.arrow((7.8, 0), (9.2, 0), kind="equilibrium", above=r"H$_2$O")
s.molecule("O=C1CC[C@@H](*)C(=O)N1", at=(11.2, 1.6), labels=PH)
s.molecule("O=C1CC[C@H](*)C(=O)N1", at=(11.2, -2.0), labels=PH)
s.text((13.3, 1.6), "(R)")
s.text((13.3, -2.0), "(S)")
s.text((11.2, -4.0), "racemate (1 : 1)")
s.draw()
