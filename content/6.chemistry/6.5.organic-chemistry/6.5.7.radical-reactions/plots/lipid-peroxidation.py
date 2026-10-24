"""Lipid peroxidation. Top: a peroxyl radical LOO abstracts a hydrogen atom from the bis-allylic
CH2 group of a linoleate chain (C-H only about 320 kJ/mol); the resulting pentadienyl radical is
delocalised over C1, C3 and C5. Bottom: O2 adds at a terminal carbon, giving a peroxyl radical with a
conjugated diene, which abstracts the next bis-allylic hydrogen and carries the chain."""

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
# R-CH=CH-CH2-CH=CH-R'; the bis-allylic C-H (atom 3, H drawn) points down at the peroxyl radical
pts = [(-2.6, -0.75), (-1.95, 0.0), (-0.65, 0.0), (0.0, -0.75), (0.0, -1.85), (0.65, 0.0), (1.95, 0.0), (2.6, -0.75)]  # both C=C cis (Z)
lh = s.molecule("*C=CC([H])C=C*", coords=pts, labels={0: "R", 4: "H", 7: "R'"})
c, h = lh.xy(3), lh.xy(4)
roo = s.molecule("*O[O]", coords=[(0.0, -5.6), (0.0, -4.6), (0.0, -3.6)], labels={0: "L", 2: "O"})
op = roo.xy(2)
dot(s, op + (0.36, 0.05))
mid = (h + op) / 2
s.curly(op + (0.38, 0.12), mid + (0.32, 0.0), bend=0.6, single=True)
s.curly((c + h) / 2 + (0.1, 0.0), mid + (0.36, 0.1), bend=-0.6, single=True)
s.curly((c + h) / 2 + (-0.1, 0.0), c + (-0.32, -0.05), bend=-0.6, single=True)
s.text((0, 1.0), "linoleate unit (9Z,12Z)", size=10)
s.arrow((3.4, -0.4), (4.8, -0.4), above="$-$LOOH")
A = "*[CH:1]=[CH:2][CH:3][CH:4]=[CH:5]*"
p1 = s.molecule(A, coords=[(x + 8.0, y) for x, y in [pts[0], pts[1], pts[2], pts[3], pts[5], pts[6], pts[7]]], labels={0: "R", 6: "R'"})
s.arrow((11.2, -0.4), (12.4, -0.4), kind="resonance")
s.molecule("*[CH:1]=[CH:2][CH:3]=[CH:4][CH:5]*", coords=p1.coords - p1.coords.mean(axis=0) + (15.6, 0), labels={0: "R", 6: "R'"})
s.text((11.8, -2.0), "pentadienyl radical (C1, C3, C5)", size=10)
finish(s)

s = Scheme()
# radical centre C5 at the end of the diene; C1=C2 stays Z, the new C3=C4 bond forms E
rc = [(-2.6, -0.75), (-1.95, 0.0), (-0.65, 0.0), (0.0, -0.75), (1.3, -0.75), (1.95, -1.5), (3.25, -1.5)]
r = s.molecule("*[CH:1]=[CH:2][CH:3]=[CH:4][CH:5]*", coords=rc, labels={0: "R", 6: "R'"})
c5 = r.xy(5)
o2 = s.molecule("[O][O]", coords=[c5 + (0.0, -2.0), c5 + (0.0, -3.2)], labels={0: "O", 1: "O"})
dot(s, o2.xy(0) + (0.36, 0.0))
dot(s, o2.xy(1) + (0.36, 0.0))
m = (c5 + o2.xy(0)) / 2
s.curly(r.atom(5), m + (0.3, 0.05), bend=-0.6, single=True)
s.curly(o2.xy(0) + (0.38, 0.08), m + (0.34, -0.05), bend=0.6, single=True)
s.arrow((3.6, -0.4), (5.0, -0.4))
pc = rc[:6] + [(1.95, -2.6), (2.9, -3.15), (3.25, -1.5)]
s.molecule("*C=CC=CC(O[O])*", coords=[(x + 8.6, y) for x, y in pc], labels={0: "R", 7: "O", 8: "R'"})
dot(s, (2.9 + 8.6 + 0.37, -3.15))
s.text((8.6, -3.9), "conjugated diene peroxyl LOO", size=10)
finish(s)
