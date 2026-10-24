"""Curved-arrow rule 2 (octet rule). Hydroxide adds to the carbonyl carbon of acetone; the carbon
already has an octet, so the new O-C bond forms only if the C=O pi bond moves onto oxygen at the same
time (second arrow). The arrows run head to tail: lone pair -> carbon, pi bond -> oxygen."""

from wikichem import Scheme

s = Scheme()
oh = s.molecule("[OH-]", at=(-2.2, 0.0), lone_pairs=True)
ket = s.molecule("CC(C)=O", at=(0.6, 0.0), rotate=-90, lone_pairs=[3])
s.curly(oh.atom(0), ket.atom(1), bend=-0.4)
s.curly(ket.bond(1, 3), ket.atom(3), bend=-0.8)
s.arrow((2.4, 0), (3.8, 0))
s.molecule("CC(C)(O)[O-]", at=(5.4, 0.0), rotate=180)
s.text((0.0, -1.9), "nucleophile + carbonyl")
s.text((5.4, -1.9), "tetrahedral alkoxide")
s.draw()
