"""Ring opening of methylcyclopropane by HBr (polar, full arrows). The bent C1-C2 bond of the ring
acts as a nucleophile: its electron pair takes the proton of HBr, bonding H to C2 (the carbon with more
hydrogens) and leaving the positive charge on C1, the carbon that gives the more stable secondary
cation; bromide then adds to C1, giving 2-bromobutane (Markovnikov orientation)."""

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
cp = s.molecule("[CH3:4][CH:1]1[CH2:2][CH2:3]1", coords=[(-1.1, 0.65), (0.0, 0.0), (0.0, -1.3), (1.1, -0.65)])
hbr = s.molecule("[H]Br", coords=[(-1.2, -2.3), (-2.5, -2.3)], lone_pairs=[1])
s.curly(cp.bond(1, 2), hbr.atom(0), bend=0.5)
s.curly(hbr.bond(0, 1), hbr.atom(1), bend=0.9)
s.text((0.0, -3.3), "methylcyclopropane", size=10)
s.arrow((2.0, -0.6), (3.4, -0.6))
cat = s.molecule("C[CH+]CC", at=(5.0, -0.6))
s.plus((6.5, -0.6))
br = s.molecule("[Br-]", at=(7.6, -0.6), lone_pairs=True)
s.curly(br.atom(0), cat.atom(1), bend=0.6)
s.text((5.0, -1.9), "secondary cation", size=10)
s.arrow((8.6, -0.6), (9.9, -0.6))
s.molecule("CC(Br)CC", at=(11.4, -0.6))
s.text((11.4, -1.9), "2-bromobutane", size=10)
finish(s)
