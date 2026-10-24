"""Beta-scission in thermal cracking (Rice-Herzfeld chain). The unpaired electron of the 1-hexyl
radical and one electron of the C2-C3 bond form the C1=C2 pi bond of ethene; the other electron of the
C2-C3 bond stays on C3, giving the 1-butyl radical, which repeats the process or abstracts a hydrogen
atom from another alkane molecule."""

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
hx = s.molecule("[CH2:1][CH2:2][CH2:3][CH2:4][CH2:5][CH3:6]", at=(0, 0))
c1, c2, c3 = hx.xy(1), hx.xy(2), hx.xy(3)
s.curly(hx.atom(1), (c1 + c2) / 2 + (0.0, 0.0), bend=-0.8, single=True)
s.curly((c2 + c3) / 2, (c1 + c2) / 2, bend=-0.8, single=True)
s.curly((c2 + c3) / 2, c3, bend=0.8, single=True)
s.text((0, -1.3), "1-hexyl radical", size=10)
s.arrow((3.3, 0), (4.7, 0), above=r"$\beta$-scission")
s.molecule("C=C", at=(5.6, 0))
s.plus((6.6, 0))
s.molecule("[CH2]CCC", at=(8.0, 0))
s.text((8.0, -1.3), "1-butyl radical", size=10)
finish(s)
