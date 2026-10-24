"""Acid cleavage of a beta-keto ester (retro-Claisen). Concentrated hydroxide adds to the ketone
carbonyl of ethyl acetoacetate; the tetrahedral alkoxide collapses, re-forming C=O and expelling
the ester enolate, a stabilised carbanion leaving group. Proton transfer gives acetate and ethyl
acetate, which is itself hydrolysed in the concentrated base."""

from wikichem import Scheme

s = Scheme()
oh = s.molecule("[OH-]", at=(-1.4, 1.8), lone_pairs=True)
k = s.molecule("CCOC(=O)CC(C)=O", at=(0, 0), lone_pairs=[8])
s.curly(oh.atom(0), k.atom(6), bend=0.4)
s.curly(k.bond(6, 8), k.atom(8), bend=0.8)
s.text((0, -1.9), "ethyl acetoacetate")
s.arrow((2.2, 0), (3.6, 0), kind="equilibrium")
t = s.molecule("CCOC(=O)CC(C)(O)[O-]", at=(5.8, 0), lone_pairs=[9])
s.curly(t.atom(9), t.bond(6, 9), bend=0.8)
s.curly(t.bond(5, 6), t.bond(3, 5), bend=0.8)
s.curly(t.bond(3, 4), t.atom(4), bend=0.8)
s.text((5.8, -2.2), "tetrahedral intermediate")
y = -4.4
s.arrow((-1.6, y), (-0.2, y))
s.molecule("CC(=O)O", at=(1.4, y + 0.3))
s.plus((3.1, y))
s.molecule("CCOC(=C)[O-]", at=(5.0, y))
s.text((5.0, y - 1.5), "ester enolate")
s.arrow((7.0, y), (8.4, y), above="H$^+$ transfer")
s.molecule("CC(=O)[O-]", at=(9.8, y + 0.3))
s.plus((11.5, y))
s.molecule("CCOC(C)=O", at=(13.3, y))
s.draw()
