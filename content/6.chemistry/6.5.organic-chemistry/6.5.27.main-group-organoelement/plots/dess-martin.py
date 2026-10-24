"""Dess-Martin oxidation of propan-2-ol. The alcohol first exchanges with one acetate on the
iodine(V) of the Dess-Martin periodinane (acetic acid is released), giving an alkoxyperiodinane.
An acetate then removes the hydrogen on the carbinol carbon; the C-H electrons form the C=O bond and
the I-O bond breaks with its electrons going to iodine, so acetone is released and iodine is reduced
from I(V) to I(III) (an iodinane)."""

from wikichem import Scheme

s = Scheme()
# iodine at the origin; aryl and ring oxygen to the left, acetates up and down, alkoxy to the right
per = s.molecule("CC(=O)OI1(OC(C)=O)(OC([H])(C)C)OC(=O)c2ccccc21",
                 coords=[(-0.5, 3.6), (0.0, 2.73), (-0.5, 1.87), (0.0, 1.2), (0, 0),
                         (0.0, -1.2), (0.5, -2.07), (0.0, -2.93), (1.5, -2.07),
                         (1.2, 0), (2.2, 0), (2.2, -1.0), (2.7, 0.87), (3.2, -0.3),
                         (-0.95, 0.5), (-1.9, 0.2), (-2.6, 0.9), (-2.2, -0.75), (-3.2, -0.95), (-3.55, -1.9),
                         (-2.9, -2.65), (-1.9, -2.45), (-1.4, -1.0)][:23])
ac = s.molecule("CC(=O)[O-]", coords=[(4.6, -3.3), (3.6, -3.3), (3.1, -4.17), (3.1, -2.43)], lone_pairs=[3])
s.curly(ac.atom(3), per.atom(11), bend=-0.4)
s.curly(per.bond(10, 11), per.bond(9, 10), bend=0.6)
s.curly(per.bond(4, 9), per.atom(4), bend=0.6)
s.arrow((5.2, 0), (6.6, 0))
s.molecule("CC(C)=O", at=(8.0, 0))
s.plus((9.4, 0))
s.molecule("CC(=O)OI1OC(=O)c2ccccc21", at=(11.6, 0))
s.draw()
