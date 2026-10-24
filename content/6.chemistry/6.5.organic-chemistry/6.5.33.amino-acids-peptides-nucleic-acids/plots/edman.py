"""Edman degradation. Top: at pH 8-9 the free N-terminal amino group adds to the central
carbon of phenyl isothiocyanate, giving the phenylthiocarbamoyl (PTC) peptide. Bottom: in
anhydrous trifluoroacetic acid the thiocarbonyl sulfur attacks the carbonyl carbon of the first
peptide bond (activated by protonation); the tetrahedral intermediate expels the amine of the
rest of the peptide, giving the anilinothiazolinone (ATZ) of the first residue and the
peptide shortened by one residue, whose new N-terminus enters the next cycle. The ATZ is
extracted and rearranged in aqueous acid to the stable phenylthiohydantoin (PTH), identified by
HPLC. R is the side chain of residue 1 (methyl here); the rest of the peptide is abbreviated."""

from wikichem import Scheme

s = Scheme()
y = 0.0
pep = s.molecule("NC(C)C(=O)N*", at=(0.0, y), lone_pairs=[0], labels={6: "peptide"})
itc = s.molecule("S=C=Nc1ccccc1", at=(4.4, y + 1.2))
s.curly(pep.atom(0), itc.atom(1), bend=-0.4)
s.curly(itc.bond(1, 2), itc.atom(2), bend=-0.8)
s.arrow((7.0, y), (8.4, y), above="pH 8-9")
s.molecule("S=C(Nc1ccccc1)NC(C)C(=O)N*", at=(12.0, y), labels={15: "peptide"})
s.text((12.0, y - 2.0), "PTC peptide")

y = -6.0
ptc = s.molecule("S=C(Nc1ccccc1)NC(C)C(=[OH+])N*", at=(0.0, y), lone_pairs=[0], labels={15: "peptide"})
s.curly(ptc.atom(0), ptc.atom(12), bend=0.6)
s.curly(ptc.bond(12, 13), ptc.atom(13), bend=-0.6)
s.arrow((5.2, y - 0.4), (6.6, y - 0.4), above="TFA")
s.molecule("S1C(Nc2ccccc2)=NC(C)C1=O", at=(8.4, y + 0.5))
s.plus((10.8, y + 0.5))
s.text((12.6, y + 0.5), r"H$_3$N$^+$–peptide")
s.text((10.2, y - 1.6), "ATZ")
s.arrow((8.4, y - 3.0), (8.4, y - 4.4))
s.text((9.8, y - 3.7), r"H$_3$O$^+$, heat")
s.molecule("CC1NC(=S)N(c2ccccc2)C1=O", at=(8.4, y - 6.4))
s.text((11.2, y - 6.4), "PTH-alanine")
s.draw()
