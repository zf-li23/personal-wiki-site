"""Phenyl participation (Cram). In 3-phenyl-2-butyl tosylate the pi electrons of the phenyl ring at C3
attack C2 from the side opposite to the leaving group as tosylate departs; the bridged phenonium ion
(a spiro cyclopropane fused to a cyclohexadienyl cation) is symmetrical, and acetic acid can open it at
either carbon, each time with inversion at the carbon attacked."""

from wikichem import Scheme

s = Scheme()
# atoms: C1, C2 (OTs), O, Ts, C3, C4, ipso, ortho ... ; ring drawn below C3
sub = s.molecule("C[CH:2]([O:9][*:7])[CH:3](C)[c:4]1[cH:5]cccc1",
                 coords=[(-1.3, 1.3), (-0.65, 0.2), (-1.4, -0.85), (-2.7, -0.85), (0.65, 0.2), (1.3, 1.3), (1.3, -0.95), (0.65, -2.1), (1.3, -3.25), (2.6, -3.25), (3.25, -2.1), (2.6, -0.95)],
                 labels={7: "Ts"}, lone_pairs=[9])
s.curly(sub.bond(4, 5), sub.atom(2), bend=-0.5)
s.curly(sub.bond(2, 9), sub.xy(9) + (0.2, -0.38), bend=0.7)
s.text((0.0, -4.3), "3-phenyl-2-butyl tosylate", size=10)
s.arrow((3.8, -0.8), (5.2, -0.8), above="AcOH", below=r"$-$TsO$^-$")
s.molecule("CC1C(C)C12C=C[CH+]C=C2", at=(7.9, -0.8))
s.text((7.9, -3.0), "phenonium ion", size=10)
s.arrow((10.1, -0.8), (11.5, -0.8), above="AcOH", below=r"$-$H$^+$")
s.molecule("CC(OC(C)=O)C(C)c1ccccc1", at=(14.4, -0.8))
s.text((14.4, -3.0), "attack at C2 or C3", size=10)
s.draw()
