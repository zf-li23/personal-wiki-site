"""[2+2] photocycloaddition of cyclohex-2-en-1-one with ethene. The pi,pi* triplet of the enone
(drawn as a 1,2-biradical on C-alpha and C-beta) adds one carbon to the alkene; the resulting triplet
1,4-biradical must undergo intersystem crossing before the second bond forms and closes the
cyclobutane of bicyclo[4.2.0]octan-2-one."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    """A point moved by the vector d (to start or end a fishhook beside a bond)."""
    return np.asarray(p.xy, float) + np.asarray(d, float)


s = Scheme()
y = -2.3  # caption line
s.molecule("O=C1C=CCCC1", at=(0, 0))
s.text((0, y), "cyclohexenone")
s.arrow((1.6, 0), (3.1, 0), above=r"$h\nu$", below="ISC")
# atoms: 0 O, 1 C=O, 2 C-alpha, 3 C-beta, 4-6 ring CH2
e = s.molecule("O=C1[CH][CH]CCC1", at=(4.8, 0), rotate=90)
cb = e.xy(3)
alk = s.molecule("C=C", coords=[(cb[0] + 2.6, cb[1] - 1.3), (cb[0] + 2.6, cb[1])])
new = (cb + alk.xy(1)) / 2  # where the new C-C bond forms
s.curly(e.atom(3), new + (0.1, 0.1), bend=-0.45, single=True)
s.curly(shift(alk.bond(0, 1), (-0.12, 0.0)), new + (0.25, -0.05), bend=-0.5, single=True)
s.curly(shift(alk.bond(0, 1), (0.15, 0.0)), shift(alk.atom(0), (0.22, -0.05)), bend=0.7, single=True)
s.text((6.1, y), r"T$_1$ ($\pi,\pi^*$) + ethene")
s.arrow((9.0, 0), (10.3, 0))
b = s.molecule("O=C1[CH]C(C[CH2])CCC1", at=(12.1, 0))
s.text((12.1, y), "triplet 1,4-biradical")
s.arrow((14.0, 0), (15.5, 0), above="ISC", below="ring closure")
s.molecule("O=C1CCCC2CCC12", at=(17.2, 0))
s.text((17.2, y), "bicyclo[4.2.0]octan-2-one", size=10)
s.draw()
