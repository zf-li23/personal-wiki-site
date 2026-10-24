"""Chain breaking by vitamin E. The lipid peroxyl radical LOO abstracts the hydrogen atom of the
phenolic O-H group of alpha-tocopherol (hydrogen atom transfer: the unpaired electron and one O-H
electron form the new O-H bond, the other O-H electron stays on the phenolic oxygen). The lipid
hydroperoxide LOOH and the tocopheroxyl radical are formed; the latter is delocalised over the ring and
hindered by the ortho methyl groups and does not continue the chain."""

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


def unit(v):
    return v / np.linalg.norm(v)


SM = "Oc1c(C)c(C)c2OC(C)(*)CCc2c1C"
probe = Scheme().molecule(SM, show_h=[0], labels={10: "R"})
d = probe.h(0).xy - probe.xy(0)
turn = -np.degrees(np.arctan2(d[1], d[0]))  # turn the molecule so that the O-H bond points to the right

s = Scheme()
toc = s.molecule(SM, at=(0, 0), rotate=turn, show_h=[0], labels={10: "R"})
o, h = toc.xy(0), toc.h(0).xy
u = unit(h - o)
n = np.array([-u[1], u[0]])
roo = s.molecule("*O[O]", coords=[h + 3.9 * u, h + 2.8 * u, h + 1.8 * u], labels={0: "L", 2: "O"})
op = roo.xy(2)
dot(s, op - 0.36 * u)
mid = (h + op) / 2
side = n if n[1] > 0 else -n
s.curly(op - 0.38 * u + 0.08 * side, mid + 0.3 * side, bend=-0.6 if u[0] > 0 else 0.6, single=True)
s.curly((o + h) / 2 + 0.1 * side, mid + 0.34 * side - 0.1 * u, bend=0.6 if u[0] > 0 else -0.6, single=True)
s.curly((o + h) / 2 - 0.1 * side, o - 0.3 * side, bend=0.7 if u[0] > 0 else -0.7, single=True)
s.text((toc.coords[:, 0].mean(), toc.coords[:, 1].min() - 0.8), r"$\alpha$-tocopherol (R = C$_{16}$H$_{33}$)", size=10)
x0 = max(h[0], op[0], roo.xy(0)[0]) + 1.4
s.arrow((x0, 0), (x0 + 1.4, 0))
w = toc.coords[:, 0].max() - toc.coords[:, 0].min()
pr = s.molecule("[O]c1c(C)c(C)c2OC(C)(*)CCc2c1C", at=(x0 + 1.0 + w / 2, toc.coords[:, 1].mean()), rotate=turn, labels={10: "R"})
s.text((x0 + 1.0 + w / 2, toc.coords[:, 1].min() - 1.1), "tocopheroxyl radical", size=10)
s.plus((pr.coords[:, 0].max() + 0.8, 0))
s.text((pr.coords[:, 0].max() + 1.9, 0), "LOOH")
finish(s)
