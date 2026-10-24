"""The two stereochemical courses of the Peterson elimination from one diastereomer,
(2S,3R)-3-(trimethylsilyl)butan-2-ol. Top, acid: the protonated hydroxy group leaves anti-periplanar
to the C-Si bond; water (or another nucleophile) takes the trimethylsilyl group while the C-Si
electrons form the C=C bond (an E2-like anti elimination assisted by the beta-silicon effect),
giving (E)-but-2-ene. Bottom, base (KH): the alkoxide attacks silicon and the syn elimination
through the four-membered ring (figure above) gives (Z)-but-2-ene."""

from wikichem import Scheme

s = Scheme()
# anti-periplanar: Si up on C3, OH2+ down on C2, drawn in the plane of the paper
A = [(-0.87, 0.5), (0, 0), (0, -1.0), (1.0, 0), (1.87, -0.5), (1.0, 1.0)]
m = s.molecule("C[C@H]([OH2+])[C@@H](C)[Si](C)(C)C", coords=A + [(1.0, 2.0), (0.13, 1.5), (1.87, 1.5)], at=(0, 0))
w = s.molecule("O", coords=[(2.6, 2.2)], lone_pairs=[0])
s.curly(w.atom(0), m.atom(5), bend=0.5)
s.curly(m.bond(3, 5), m.bond(1, 3), bend=-0.6)
s.curly(m.bond(1, 2), m.atom(2), bend=0.6)
s.text((0.5, -2.0), "anti-periplanar Si and OH$_2^+$", size=11)
s.arrow((3.2, 0), (4.6, 0), above="acid, anti")
s.molecule("C/C=C/C", at=(6.2, 0))
s.text((6.2, -1.0), "(E)", size=12)
s.plus((7.6, 0))
s.molecule("C[Si](C)(C)[OH2+]", at=(9.0, 0))

y = -4.6
s.molecule("C[C@H](O)[C@@H](C)[Si](C)(C)C", coords=A + [(1.0, 2.0), (0.13, 1.5), (1.87, 1.5)], at=(0, y))
s.arrow((3.2, y), (4.6, y), above="KH, syn")
s.molecule("C/C=C\\C", at=(6.2, y))
s.text((6.2, y - 1.0), "(Z)", size=12)
s.plus((7.6, y))
s.molecule("C[Si](C)(C)[O-]", at=(9.0, y))
s.draw()
