"""The key step of the ninhydrin reaction: the imine formed from the amino group of an amino
acid and the central carbonyl of indane-1,2,3-trione (ninhydrin is its hydrate) decarboxylates.
The carboxylate releases CO2 and the C-C bond electrons form a new C=N bond, while the old
C=N pi electrons move onto the central carbon, where the two flanking carbonyl groups stabilize
the negative charge. Hydrolysis of the new imine then releases the aldehyde RCHO (one carbon
shorter than the amino acid) and 2-aminoindane-1,3-dione, which condenses with a second
ninhydrin to give the purple anion (Ruhemann's purple)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
im = s.molecule("O=C1c2ccccc2C(=O)C1=NC(C)C(=O)[O-]", at=(0.0, y), lone_pairs=[15])
# atoms: 0 O, 1 C, 2-7 ring, 8 C, 9 O, 10 C2, 11 N, 12 Calpha, 13 CH3, 14 C(carboxyl), 15 O, 16 O-
s.curly(im.atom(16), im.bond(14, 16), bend=0.5)
s.curly(im.bond(12, 14), im.bond(11, 12), bend=0.5)
s.curly(im.bond(10, 11), im.atom(10), bend=-0.6)
s.text((0.0, y - 2.4), "imine of ninhydrin and alanine")
s.arrow((3.8, y), (5.4, y), above=r"$-$CO$_2$")
s.molecule("O=C1c2ccccc2C(=O)[C-]1N=CC", at=(8.4, y))
s.text((8.4, y - 2.4), "stabilized carbanion")
s.arrow((11.0, y), (12.6, y), above=r"H$^+$, H$_2$O")
s.molecule("O=C1c2ccccc2C(=O)C1N", at=(14.6, y + 0.6))
s.molecule("CC=O", at=(14.6, y - 1.8))
s.draw()
