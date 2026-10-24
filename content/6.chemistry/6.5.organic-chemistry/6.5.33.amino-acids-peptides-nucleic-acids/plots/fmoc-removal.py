"""Removal of the Fmoc group with piperidine (20% in DMF): an E1cb elimination. Piperidine
removes the proton on C9 of the fluorene, which is acidic because the resulting anion is an
aromatic cyclopentadienyl-type anion (fluorene pKa 22.6 in DMSO). The anion expels the
carbamate (the C-O bond to the CH2 is beta to the carbanion), giving dibenzofulvene; the
carbamate loses CO2 to release the free amine. Excess piperidine adds to the electrophilic
dibenzofulvene (conjugate addition), so the fulvene cannot react with the liberated amine."""

from wikichem import Scheme

s = Scheme()
y = 0.0
f = s.molecule("O=C(NC)OCC1c2ccccc2-c2ccccc21", at=(0.0, y), show_h=[6])
pip = s.molecule("C1CCNCC1", at=(2.6, y + 2.4), lone_pairs=[3])
s.curly(pip.atom(3), f.h(6), bend=0.4)
s.curly(f.bond(6, f.mol.GetNumAtoms() - 1), f.bond(5, 6), bend=-0.5)
s.curly(f.bond(4, 5), f.atom(4), bend=-0.6)
s.text((0.0, y - 2.6), "Fmoc carbamate")
s.arrow((3.2, y - 0.6), (4.6, y - 0.6), above="E1cb")
s.molecule("C=C1c2ccccc2-c2ccccc21", at=(7.2, y))
s.text((7.2, y - 2.0), "dibenzofulvene")
s.plus((9.9, y - 0.6))
s.molecule("[O-]C(=O)NC", at=(11.4, y - 0.6))
s.arrow((12.8, y - 0.6), (14.2, y - 0.6), above=r"$-$CO$_2$", below=r"H$^+$")
s.molecule("CN", at=(15.2, y - 0.6))
s.draw()
