"""Conversion of (R)-butan-2-ol into (S)-2-bromobutane with PBr3. The hydroxy oxygen attacks
phosphorus and displaces bromide, giving a protonated dibromophosphite; after loss of the proton
the OPBr2 group is a good leaving group, and bromide attacks the carbon from the back side (SN2):
no carbocation, no rearrangement, inversion of configuration."""

from wikichem import Scheme

s = Scheme()
UP = [(-0.87, -0.5), (0, 0)]  # methyl and stereocentre; the oxygen points up
y = 0.0
alc = s.molecule("C[C@@H](O)CC", coords=UP + [(0, 1), (0.87, -0.5), (1.73, 0)], at=(0, y), lone_pairs=[2])
pb = s.molecule("BrP(Br)Br", at=(2.7, y + 1.2), lone_pairs=[1])
s.curly(alc.atom(2), pb.atom(1), bend=-0.5)
s.curly(pb.bond(1, 2), pb.atom(2), bend=0.7)
s.text((0.4, y - 1.4), "(R)-butan-2-ol")
s.arrow((4.0, y + 0.5), (5.4, y + 0.5))
s.molecule("C[C@@H]([OH+]P(Br)Br)CC", coords=UP + [(0, 1), (0, 2), (-0.87, 2.5), (0.87, 2.5), (0.87, -0.5), (1.73, 0)],
           at=(6.8, y))
s.plus((9.4, y + 0.5))
s.molecule("[Br-]", at=(10.3, y + 0.5), lone_pairs=True)
s.arrow((11.1, y + 0.5), (12.5, y + 0.5), below=r"$-$H$^+$")

y = -4.6
est = s.molecule("C[C@@H](OP(Br)Br)CC", coords=UP + [(0, 1), (0, 2), (-0.87, 2.5), (0.87, 2.5), (0.87, -0.5), (1.73, 0)],
                 at=(1.5, y), lone_pairs=[2])
br = s.molecule("[Br-]", at=(1.5, y - 1.9), lone_pairs=True)
s.curly(br.atom(0), est.atom(1), bend=0.4)
s.curly(est.bond(1, 2), est.atom(2), bend=-0.8)
s.arrow((4.2, y), (5.6, y), above=r"S$_{\mathrm{N}}$2")
s.molecule("C[C@H](Br)CC", coords=[(-0.87, 0.5), (0, 0), (0, -1), (0.87, 0.5), (1.73, 0)], at=(7.0, y))
s.text((7.4, y - 2.2), "(S)-2-bromobutane")
s.plus((9.6, y))
s.molecule("[O-]P(Br)Br", at=(10.9, y))
s.draw()
