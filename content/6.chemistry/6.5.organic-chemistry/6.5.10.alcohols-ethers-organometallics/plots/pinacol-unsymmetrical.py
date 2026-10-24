"""Pinacol rearrangement of an unsymmetrical diol, 2-methyl-1,1-diphenylpropane-1,2-diol. The hydroxy
group that leaves is the one on the carbon that gives the more stable cation (diphenylmethyl type);
a methyl group on the neighbouring carbon then migrates, helped by the lone pair of the remaining
hydroxy oxygen, and loss of the proton from the oxocarbenium ion gives 3,3-diphenylbutan-2-one."""

from wikichem import Scheme

s = Scheme()
PH = {5: "Ph", 6: "Ph"}
pr = s.molecule("CC(C)(O)C(*)(*)[OH2+]", at=(0, 0), labels=PH)
s.curly(pr.bond(4, 7), pr.atom(7), bend=0.7)
s.arrow((1.8, 0), (3.2, 0), below=r"$-$H$_2$O")
# atoms: 0 migrating CH3, 1 C2, 2 CH3, 3 O, 4 C1 (cation), 5, 6 Ph
cat = s.molecule("CC(C)(O)[C+](*)*", coords=[(1.6, 1.0), (1.1, 0), (1.6, -1.0), (2.2, 0), (0, 0), (-0.87, 0.5), (-0.87, -0.5)],
                 at=(4.6, 0), lone_pairs=[3], labels=PH)
s.curly(cat.bond(1, 0), cat.atom(4), bend=-0.9)
s.curly(cat.atom(3), cat.bond(1, 3), bend=-0.7)
s.arrow((7.8, 0), (9.2, 0), above="1,2-CH$_3$ shift")
s.molecule("CC(=[OH+])C(C)(*)*", at=(10.8, 0), labels=PH)
s.arrow((12.4, 0), (13.8, 0), below=r"$-$H$^+$")
s.molecule("CC(=O)C(C)(*)*", at=(15.4, 0), labels=PH)
s.draw()
