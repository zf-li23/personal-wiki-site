"""Ferrocene-mediated electrochemical cyclization of an N-aryl carbamate (allyl N-phenylcarbamate).
At the anode ferrocene (Fc) is oxidized to ferrocenium (Fc+), which oxidizes the carbamate anion
(formed with a weak base) to an amidyl radical. The N radical adds to the internal alkene carbon
(5-exo-trig); the primary carbon radical takes a hydrogen atom from cyclohexa-1,4-diene.
At the cathode methanol is reduced to H2 and methoxide, which serves as the base."""

import math

import numpy as np
from wikichem import Scheme


def shift(p, d):
    """A point moved by the vector d (to start or end a fishhook beside a bond)."""
    return np.asarray(p.xy, float) + np.asarray(d, float)




def pent(k, r=1.15):
    """Vertex k of a regular pentagon centred on the origin (k = 0 at the top)."""
    t = math.radians(90 + 72 * k)
    return (r * math.cos(t), r * math.sin(t))


def out(p, k, d=1.0):
    """A point one bond length outward from pentagon vertex p (vertex number k)."""
    t = math.radians(90 + 72 * k)
    return (p[0] + d * math.cos(t), p[1] + d * math.sin(t))


ph = {3: "Ph"}
s = Scheme(scale=0.55)
y = -2.3  # caption line
s.molecule("O=C(N*)OCC=C", at=(-0.5, 0), labels=ph)
s.text((-0.5, y), "allyl N-phenylcarbamate", size=10)
s.arrow((2.4, 0), (4.0, 0), above=r"base, Fc$^+$", below=r"$-\mathrm{H}^+$, $-\mathrm{e}^-$")
# amidyl radical drawn in the cyclization geometry: N, C(=O), O, CH2, CH= on a pentagon (N...C open)
# atoms: 0 O, 1 C, 2 N (radical), 3 Ph, 4 O, 5 CH2, 6 CH=, 7 =CH2
N, C, O, C5, C6 = pent(0, 1.3), pent(1), pent(2), pent(3), pent(4, 1.6)
coords = [out(C, 1), C, N, out(N, 0), O, C5, C6, out(C6, 4)]
a = s.molecule("O=C([N]*)OCC=C", at=(6.2, 0), coords=coords, labels=ph)
new = a.xy(2) + 0.62 * (a.xy(6) - a.xy(2))  # where the new N-C bond forms, nearer the alkene
s.curly(a.atom(2), new + (0.05, 0.12), bend=-0.6, single=True)
s.curly(shift(a.bond(6, 7), (-0.05, 0.12)), new + (0.2, -0.1), bend=0.6, single=True)
s.curly(shift(a.bond(6, 7), (0.05, -0.12)), shift(a.atom(7), (0.2, -0.2)), bend=0.7, single=True)
s.text((6.2, y), "amidyl radical, 5-exo-trig", size=10)
s.arrow((8.3, 0), (9.8, 0))
s.molecule("O=C1OCC([CH2])N1*", at=(11.5, 0), labels={7: "Ph"})
s.text((11.5, y), "primary alkyl radical", size=10)
s.arrow((13.2, 0), (14.9, 0), above="1,4-CHD", below="HAT")
s.molecule("O=C1OCC(C)N1*", at=(16.5, 0), labels={7: "Ph"})
s.text((16.5, y), "oxazolidinone", size=10)
s.text((8.3, -3.4), r"anode: Fc $\to$ Fc$^+$ + e$^-$        cathode: 2 MeOH + 2 e$^-$ $\to$ H$_2$ + 2 MeO$^-$", size=10)
s.draw()
