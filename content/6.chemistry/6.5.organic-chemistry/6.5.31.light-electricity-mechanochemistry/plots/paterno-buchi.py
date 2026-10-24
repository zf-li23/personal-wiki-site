"""Paterno-Buchi reaction of benzophenone with 2-methylpropene. The n,pi* triplet of the ketone
behaves like an alkoxyl radical: its oxygen adds to the CH2 end of the alkene so that the more
stable 1,4-biradical forms (a diphenylmethyl radical and a tertiary alkyl radical). After
intersystem crossing the biradical closes to 2,2-diphenyl-3,3-dimethyloxetane."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    """A point moved by the vector d (to start or end a fishhook beside a bond)."""
    return np.asarray(p.xy, float) + np.asarray(d, float)


s = Scheme()
y = -2.6  # caption line
# atoms: 0 O (radical), 1 C (radical), 2-7 phenyl, 8-13 phenyl
k = s.molecule("[O][C](c1ccccc1)c1ccccc1", at=(0, 0), rotate=90)
ox = k.xy(0)
alk = s.molecule("C=C(C)C", at=(ox[0] + 3.2, ox[1] - 0.1), rotate=90)
new = (ox + alk.xy(0)) / 2  # where the new O-C bond forms
s.curly(k.atom(0), new + (0.1, 0.1), bend=-0.45, single=True)
s.curly(shift(alk.bond(0, 1), (0.0, 0.13)), new + (0.25, 0.08), bend=0.5, single=True)
s.curly(shift(alk.bond(0, 1), (0.0, -0.15)), shift(alk.atom(1), (0.05, -0.22)), bend=-0.7, single=True)
s.text((1.0, y), r"Ph$_2$CO T$_1$ (n,$\pi^*$) + 2-methylpropene", size=10)
s.arrow((5.0, 0), (6.3, 0))
s.molecule("[C](c1ccccc1)(c1ccccc1)OC[C](C)C", at=(8.5, 0))
s.text((8.5, y), "more stable 1,4-biradical", size=10)
s.arrow((10.7, 0), (12.2, 0), above="ISC")
s.molecule("C1(c2ccccc2)(c2ccccc2)OCC1(C)C", at=(14.3, 0))
s.text((14.3, y), "oxetane", size=10)
s.draw()
