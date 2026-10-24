"""Proline-catalysed aldol reaction (Houk-List model, drawn flat). The enamine formed from L-proline
and acetone attacks the aldehyde: the nitrogen lone pair pushes the C=C electrons onto the aldehyde
carbon, and the carboxylic acid, hydrogen-bonded to the aldehyde oxygen, delivers its proton to the
developing alkoxide while fixing the aldehyde on one face of the enamine. Hydrolysis of the
resulting iminium ion releases (R)-4-hydroxy-4-(4-nitrophenyl)butan-2-one and regenerates proline
(Ar = 4-nitrophenyl)."""

from wikichem import Scheme

s = Scheme()
# atoms: 0 CH3, 1 C, 2 CH2, 3 N, 4-7 ring C (7 bears CO2H), 8 C, 9 O, 10 H, 11 O
xy = [(-0.87, 1.5), (0, 1.0), (0.87, 1.5), (0, 0), (-0.95, -0.31), (-0.59, -1.31), (0.59, -1.31), (0.95, -0.31),
      (1.82, 0.18), (1.82, 1.18), (2.5, 1.85), (2.69, -0.32)]
en = s.molecule("CC(=C)N1CCC[C@H]1C(O[H])=O", coords=xy, at=(0, 0), lone_pairs=[3])
ald = s.molecule("O=C*", coords=[(2.7, 2.95), (1.75, 3.25), (1.75, 4.25)], labels={2: "Ar"}, lone_pairs=[0])
s.partial(ald.atom(0), en.atom(10))
s.curly(en.atom(3), en.bond(1, 3), bend=-0.7)
s.curly(en.bond(1, 2), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), (ald.xy(0) + en.xy(10)) / 2, bend=-0.6)
s.curly(en.bond(9, 10), en.atom(9), bend=-0.6)
s.text((0.6, -2.3), "enamine of L-proline + ArCHO")
s.arrow((3.8, 0.8), (5.4, 0.8), above="C$-$C bond formation", below=r"H$_2$O, $-$proline")
s.molecule("CC(=O)C[C@@H](O)c1ccc(cc1)[N+](=O)[O-]", at=(9.2, 0.8))
s.text((9.2, -1.4), "(R)-aldol")
s.draw()
