"""First step of the reaction of an alcohol with thionyl chloride. The hydroxy oxygen attacks sulfur
and displaces chloride; loss of the proton (as HCl) gives the alkyl chlorosulfite R-O-S(=O)Cl. The
C-O bond is not touched, so the configuration of the carbon is unchanged at this stage."""

from wikichem import Scheme

s = Scheme()
alc = s.molecule("C[C@@H](O)*", at=(0, 0), lone_pairs=[2], labels={3: r"C$_6$H$_{13}$"})
so = s.molecule("ClS(=O)Cl", at=(2.6, 0.3), lone_pairs=[1])
s.curly(alc.atom(2), so.atom(1), bend=-0.5)
s.curly(so.bond(1, 3), so.atom(3), bend=0.7)
s.arrow((4.1, 0), (5.7, 0), below=r"$-$HCl")
s.molecule("C[C@@H](OS(=O)Cl)*", at=(7.6, 0), labels={6: r"C$_6$H$_{13}$"})
s.text((7.6, -1.6), "alkyl chlorosulfite")
s.draw()
