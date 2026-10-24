"""Norrish type II reaction of hexan-2-one. The n,pi* triplet abstracts a gamma hydrogen through a
six-membered cyclic transition state (1,5-hydrogen atom transfer), giving a 1,4-biradical.
The biradical either cleaves (beta scission of the C(alpha)-C(beta) bond) to propene and the enol
of acetone, which tautomerises to acetone, or closes to a cyclobutanol (Norrish-Yang cyclization)."""

import math

import numpy as np
from wikichem import Scheme


def shift(p, d):
    """A point moved by the vector d (to start or end a fishhook beside a bond)."""
    return np.asarray(p.xy, float) + np.asarray(d, float)


def ring(r, angles):
    return [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in angles]


s = Scheme()
y = -2.2  # caption line
# T1 of hexan-2-one drawn as a six-membered ring O ... H-C(gamma)
# atoms: 0 CH3, 1 C(carbonyl, radical), 2 O (radical), 3 C-alpha, 4 C-beta, 5 C-gamma, 6 H, 7 CH3 (delta)
r = 1.4
o, c1, ca, cb, cg, h = ring(r, [90, 150, 210, 270, 330, 30])
out = lambda p, a: (p[0] + 1.25 * math.cos(math.radians(a)), p[1] + 1.25 * math.sin(math.radians(a)))
coords = [out(c1, 150), c1, o, ca, cb, cg, h, out(cg, 330)]
t = s.molecule("C[C]([O])CCC([H])C", at=(0, 0), coords=coords)
s.curly(t.atom(2), t.bond(2, 6), bend=-1.2, single=True)
s.curly(shift(t.bond(5, 6), (0.18, 0.0)), shift(t.bond(2, 6), (0.12, -0.1)), bend=0.9, single=True)
s.curly(shift(t.bond(5, 6), (-0.15, 0.0)), shift(t.atom(5), (-0.25, 0.15)), bend=-0.9, single=True)
s.text((0, y), r"T$_1$, 1,5-HAT")
s.arrow((2.4, 0), (3.9, 0))
# 1,4-biradical, same ring-like layout without the O-H bond to C-gamma
b = s.molecule("C[C](O)CC[CH]C", at=(6.0, 0), coords=[out(c1, 150), c1, o, ca, cb, cg, out(cg, 330)])
s.text((6.0, y), "1,4-biradical")
s.arrow((8.3, 0.6), (10.0, 1.8), above="cleavage")
s.molecule("C=C(C)O", at=(11.4, 2.3))
s.plus((12.7, 2.3))
s.molecule("C=CC", at=(13.8, 2.3))
s.text((12.7, 0.9), "enol (to acetone) + propene", size=10)
s.arrow((8.3, -0.6), (10.0, -1.8), above="cyclization")
s.molecule("CC1(O)CCC1C", at=(11.8, -2.4))
s.text((11.8, -4.0), "cyclobutanol (Norrish-Yang)", size=10)
s.draw()
