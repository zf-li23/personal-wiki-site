"""Norrish type I reaction (alpha cleavage) of pentan-3-one. After excitation and intersystem
crossing the n,pi* triplet behaves like an alkoxyl radical on oxygen and a radical on the carbonyl
carbon. Beta scission relative to the oxygen radical: the oxygen electron and one electron of the
C(O)-C(alpha) bond form the new C=O pi bond, the other electron leaves with the ethyl group.
The products are a propanoyl (acyl) radical and an ethyl radical."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    """A point moved by the vector d (to start or end a fishhook beside a bond)."""
    return np.asarray(p.xy, float) + np.asarray(d, float)


s = Scheme()
y = -2.0  # caption line
s.molecule("CCC(=O)CC", at=(0, 0))
s.text((0, y), "pentan-3-one")
s.arrow((1.9, 0), (3.5, 0), above=r"$h\nu$", below="ISC")
x0 = 6.0
t = s.molecule("CC[C](CC)[O]", at=(x0, 0),
               coords=[(-2.25, 0), (-1.13, -0.65), (0, 0), (1.13, -0.65), (2.25, 0), (0, 1.3)])
s.curly(t.atom(5), shift(t.bond(2, 5), (0.15, 0)), bend=-0.8, single=True)
s.curly(shift(t.bond(2, 3), (0.1, 0.17)), shift(t.bond(2, 5), (0.18, -0.1)), bend=0.5, single=True)
s.curly(shift(t.bond(2, 3), (-0.08, -0.15)), shift(t.atom(3), (0.0, -0.3)), bend=0.6, single=True)
s.text((x0, y), r"T$_1$ (n,$\pi^*$)")
s.arrow((8.8, 0), (10.4, 0), above=r"$\alpha$ cleavage")
s.molecule("CC[C]=O", at=(11.9, 0))
s.text((11.9, y), "propanoyl radical")
s.plus((13.5, 0))
s.molecule("[CH2]C", at=(14.8, 0))
s.text((15.4, y), "ethyl radical")
s.draw()
