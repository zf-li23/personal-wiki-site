"""Chain propagation in the autoxidation of diethyl ether. Top: the alpha-ethoxyethyl radical
pairs its unpaired electron with one of the two unpaired electrons of triplet O2, giving a peroxyl
radical. Bottom: the peroxyl radical abstracts the weak alpha C-H hydrogen of another ether molecule
(hydrogen atom transfer), giving the hydroperoxide and a new alpha-ethoxyethyl radical that carries
the chain."""

import matplotlib.pyplot as plt
import numpy as np
from wikichem import Scheme

DOTS = []  # radical dots placed by hand (the radical atoms carry a label, which suppresses the automatic dot)


def dot(s, p):
    p = np.asarray(p, float)
    DOTS.append(p)
    s.text(p, "")


def pair(s, p, q, lift=0.3, bend=0.7):
    """Two fishhooks from the electrons at p and q meeting above the middle (a new bond)."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    m = (p + q) / 2 + (0, lift)
    s.curly(p + (0, 0.08), m - (0.06, 0), bend=bend, single=True)
    s.curly(q + (0, 0.08), m + (0.06, 0), bend=-bend, single=True)


def finish(s):
    fig, ax = s.draw()
    ink = plt.rcParams["text.color"]
    for p in DOTS:
        ax.plot(*p, marker="o", ms=2.4, color=ink, mec=ink, mfc=ink)
    DOTS.clear()


s = Scheme()
r = s.molecule("C[CH]OCC", coords=[(0.65, -1.1), (0, 0), (-1.3, 0), (-1.95, -1.1), (-3.25, -1.1)], lone_pairs=[2])
c = r.xy(1)
o2 = s.molecule("[O][O]", coords=[c + (1.9, 0.0), c + (3.1, 0.0)], labels={0: "O", 1: "O"})
p, q = c + (0.0, 0.0), o2.xy(0) - (0.38, 0)
dot(s, q)
dot(s, o2.xy(1) + (0.38, 0))
s.curly(r.atom(1), (c + o2.xy(0)) / 2 + (-0.1, 0.35), bend=0.6, single=True)
s.curly(q + (0, 0.08), (c + o2.xy(0)) / 2 + (0.05, 0.35), bend=-0.7, single=True)
s.text((-1.3, -2.0), r"$\alpha$-ethoxyethyl radical", size=10)
s.text((o2.xy(0)[0] + 0.6, -0.9), r"O$_2$ (triplet)", size=10)
s.arrow((c[0] + 4.0, 0), (c[0] + 5.4, 0))
pr = s.molecule("CC(OCC)O[O]", at=(c[0] + 7.3, 0), lone_pairs=[2], labels={6: "O"})
dot(s, pr.xy(6) + (0.33, 0.12))
s.text((c[0] + 7.3, -1.5), "peroxyl radical", size=10)
finish(s)

s = Scheme()
# R-O-O(dot) ... H-C(alpha) of diethyl ether, all on one line
roo = s.molecule("*O[O]", coords=[(-2.6, 0), (-1.4, 0), (-0.2, 0)], labels={0: "R", 2: "O"})
eth = s.molecule("[H]C(C)OCC", coords=[(1.6, 0), (2.7, 0), (3.3, 1.05), (3.3, -1.05), (4.6, -1.05), (5.2, 0)], labels={0: "H"})
o, h, cα = roo.xy(2), eth.xy(0), eth.xy(1)
dot(s, o + (0.36, 0.0))
mid = (o + h) / 2
s.curly(o + (0.36, 0.08), mid + (0, 0.35), bend=0.6, single=True)
s.curly((h + cα) / 2 + (0, 0.1), mid + (0.1, 0.35), bend=-0.7, single=True)
s.curly((h + cα) / 2 + (0, -0.1), cα + (0.05, -0.3), bend=-0.6, single=True)
s.text((-1.4, -1.0), r"R = CH(CH$_3$)OEt", size=10)
s.arrow((6.0, 0), (7.4, 0))
s.molecule("CC(OCC)OO", at=(9.3, 0))
s.text((9.3, -1.5), "hydroperoxide", size=10)
s.plus((12.5, 0))
s.molecule("C[CH]OCC", at=(14.5, 0))
finish(s)
