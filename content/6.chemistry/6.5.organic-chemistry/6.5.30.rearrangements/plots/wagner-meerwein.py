"""Wagner-Meerwein rearrangement: isoborneol to camphene in acid. The protonated alcohol loses water
to give the secondary 2-bornyl cation. The C1-C6 bond, antiperiplanar to the departing exo group,
migrates with its electron pair to C2 (a 1,2-alkyl shift that changes the ring skeleton); the positive
charge moves to C1, which is tertiary. Loss of a proton from the methyl group on C1 gives camphene.
The bicyclic skeletons are drawn at hand-chosen coordinates in the usual perspective."""

from wikichem import Scheme

# norbornane template: left/right bridgeheads, front pair, back pair, top bridge
L, R = (0.0, 0.0), (2.1, 0.0)
FL, FR = (0.55, -0.8), (1.55, -0.8)
BL, BR = (0.5, 0.3), (1.6, 0.3)
T = (1.05, 1.0)

# bornane numbering in SMILES order: Me, C7, Me, C4, C5, C6, C1, Me(C1), C2, O, C3
BORNANE = [(0.6, 1.85), T, (1.5, 1.85), R, BR, BL, L, (-0.95, 0.05), FL, (0.25, -1.7), FR]
BORNYL = BORNANE[:9] + [FR]
# after the shift: Me(C1), C1, C7, Me, Me, C4, C5, C6, C2, C3; C2 and C4 are now the bridgeheads
CAMPHENYL = [(0.25, -1.65), FL, FR, (1.25, -1.7), (2.45, -1.35), R, BR, BL, L, T]


def place(smiles, coords, at):
    return s.molecule(smiles, coords=[(x + at[0], y + at[1]) for x, y in coords])


s = Scheme()
y = 0.0
p = place("CC1(C)C2CCC1(C)C([OH2+])C2", BORNANE, (0.0, y))
s.curly(p.bond(8, 9), p.atom(9), bend=-0.6)
s.text((1.0, y - 2.6), "protonated isoborneol")
s.arrow((3.0, y), (4.4, y), below=r"$-\,\mathrm{H_2O}$")
c = place("CC1(C)C2CCC1(C)[CH+]C2", BORNYL, (5.6, y))
s.curly(c.bond(6, 5), c.atom(8), bend=0.9)
s.text((6.6, y - 2.6), "2-bornyl cation (2°)")
s.arrow((8.4, y), (9.8, y), above="1,2-alkyl shift")
place("C[C+]1C(C)(C)C2CCC1C2", CAMPHENYL, (10.9, y))
s.text((11.9, y - 2.6), "tertiary cation")
s.arrow((13.6, y), (15.0, y), below=r"$-\,\mathrm{H^+}$")
place("C=C1C(C)(C)C2CCC1C2", CAMPHENYL, (16.1, y))
s.text((17.1, y - 2.6), "camphene")
s.draw()
