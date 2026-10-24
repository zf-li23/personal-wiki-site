"""The second, intramolecular Mannich reaction of the Robinson tropinone synthesis. After the first
Mannich reaction and cyclisation of the nitrogen onto the second aldehyde, the molecule holds an
N-methylpyrrolinium ion and the enol of a beta-keto acid. The enol oxygen lone pair pushes the C=C
electrons onto the iminium carbon and the C=N electrons move onto nitrogen, closing the six-membered
ring of the tropane skeleton; loss of a proton gives tropinone-2,4-dicarboxylic acid, and
decarboxylation of both beta-keto acid groups on warming gives tropinone."""

from wikichem import Scheme

# shared layout: piperidine ring N, C1, C2(CO2H), C3(=O), C4(CO2H), C5; two-carbon bridge C6-C7 drawn above
N, C1, C7, C6, C5 = (0, 1.2), (0.87, 0.5), (0.6, 2.1), (-0.6, 2.1), (-0.87, 0.5)
C4, C3, C2 = (-0.87, -0.5), (0, -1.0), (0.87, -0.5)
A4, A4a, A4b = (-1.73, -1.0), (-2.6, -0.5), (-1.73, -2.0)
A2, A2a, A2b = (1.73, -1.0), (2.6, -0.5), (1.73, -2.0)
O3 = (0, -2.0)
# atom order of both SMILES: N, C1, C7, C6, C5, C4, CO2H(C, =O, O), C3, O3, C2, CO2H(C, =O, O)
xy = [N, C1, C7, C6, C5, C4, A4, A4a, A4b, C3, O3, C2, A2, A2a, A2b]

s = Scheme()
im = s.molecule("[NH+]1=CCCC1C(C(=O)O)C(O)=CC(=O)O", coords=xy, at=(0, 0), labels={0: "MeN$^+$"}, lone_pairs=[10])
s.curly(im.atom(10), im.bond(9, 10), bend=1.0)
s.curly(im.bond(9, 11), im.atom(1), bend=0.7)
s.curly(im.bond(0, 1), im.atom(0), bend=0.6)
s.text((0, -3.2), "iminium + enol")
s.arrow((3.4, 0), (4.8, 0), above=r"$-$H$^+$")
s.molecule("N1C2CCC1C(C(=O)O)C(=O)C2C(=O)O", coords=xy, at=(7.9, 0), labels={0: "NMe"})
s.arrow((11.0, 0), (12.4, 0), above=r"$-$2 CO$_2$", below="heat")
s.molecule("N1C2CCC1CC(=O)C2", coords=[N, C1, C7, C6, C5, C4, C3, O3, C2], at=(14.0, 0), labels={0: "NMe"})
s.text((14.0, -3.2), "tropinone")
s.draw()
