"""Decarboxylation of a beta-keto acid (acetoacetic acid) through a six-membered cyclic transition
state. The carboxyl O-H is hydrogen-bonded to the ketone oxygen; the ketone oxygen takes the
proton, the O-H electrons become the second C=O of carbon dioxide, the C-C bond to the carboxyl
carbon becomes the C=C of an enol, and the ketone pi bond moves onto oxygen. The enol then
tautomerizes to the ketone (acetone)."""

from wikichem import Scheme

s = Scheme()
# Atoms: 0 CH3, 1 C(ketone), 2 O(ketone), 3 CH2, 4 C(carboxyl), 5 =O, 6 O(H), 7 H
R = 1.3  # a slightly enlarged ring leaves room for the arrows
ring = [(R * x, R * y) for x, y in [(-0.866, 0.5), (0.0, 1.0), (0.866, 0.5), (0.866, -0.5), (0.0, -1.0), (-0.866, -0.5)]]
c1, c3, c4, o6, h7, o2 = ring
coords = [(c1[0] - 0.866, c1[1] + 0.5), c1, o2, c3, c4, (c4[0] + 0.866, c4[1] + 0.5), o6, h7]
acid = s.molecule("CC(=O)CC(=O)O[H]", coords=coords, at=(0, 0), lone_pairs=[2, 6])
s.partial(acid.atom(7), acid.atom(2))
s.curly(acid.atom(2), acid.atom(7), bend=-0.9)
s.curly(acid.bond(6, 7), acid.bond(4, 6), bend=-0.6)
s.curly(acid.bond(3, 4), acid.bond(1, 3), bend=0.8)
s.curly(acid.bond(1, 2), acid.atom(2), bend=0.6)
s.text((0, -2.2), "acetoacetic acid (H-bonded)")
s.arrow((2.4, 0), (3.8, 0), above="heat")
enol = s.molecule("CC(O)=C", at=(5.0, 0))
s.plus((6.5, 0))
s.molecule("O=C=O", at=(7.9, 0), show_carbons=[1])
s.text((5.0, -2.0), "enol")
s.arrow((9.4, 0), (10.8, 0), above="tautomerism")
s.molecule("CC(C)=O", at=(12.0, 0))
s.text((12.0, -2.0), "acetone")
s.draw()
