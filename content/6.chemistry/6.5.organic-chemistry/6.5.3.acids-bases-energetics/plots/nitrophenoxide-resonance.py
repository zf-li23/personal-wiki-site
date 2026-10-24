"""Why 4-nitrophenol is a stronger acid than phenol. In 4-nitrophenoxide the lone pair on the
phenoxide oxygen can be pushed through the ring all the way onto an oxygen of the nitro group
(four arrows): the C-O bond gains double-bond character, the ring becomes quinoid and the negative
charge ends up on the electronegative nitro oxygen. 3-Nitrophenoxide has no such structure; its
nitro group acts by induction only."""

from wikichem import Scheme

s = Scheme()
# atoms: 0 O-, 1-6 ring carbons (1 bears O, 4 bears N), 7 N, 8 O, 9 O-
a = s.molecule("[O-]C1=CC=C(C=C1)[N+](=O)[O-]", at=(0, 0), rotate=90, lone_pairs=[0, 8, 9])
s.curly(a.atom(0), a.bond(0, 1), bend=0.6)
s.curly(a.bond(1, 2), a.bond(2, 3), bend=0.6)
s.curly(a.bond(3, 4), a.bond(4, 7), bend=0.6)
s.curly(a.bond(7, 8), a.atom(8), bend=0.6)
s.arrow((2.0, 0), (3.2, 0), kind="resonance")
s.molecule("O=C1C=CC(C=C1)=[N+]([O-])[O-]", at=(5.2, 0), like=a, lone_pairs=[0, 8, 9])
s.text((0, -3.6), "4-nitrophenoxide")
s.text((5.2, -3.6), "charge on a nitro oxygen")
s.draw()
