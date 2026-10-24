"""Beta-scission of the tert-butoxyl radical. The unpaired electron on oxygen and one electron of a
C-CH3 bond form the C=O pi bond of acetone; the other electron of that bond leaves with the methyl
radical."""

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
t = s.molecule("[O]C(C)(C)C", coords=[(-1.3, 0), (0, 0), (-0.65, -1.1), (0.65, -1.1), (1.4, 0)], show_carbons=[4], labels={0: "O"})
o, c, me = t.xy(0), t.xy(1), t.xy(4)
dot(s, o + (0, 0.36))
s.curly(o + (0.08, 0.38), (o + c) / 2 + (0.05, 0.16), bend=-0.7, single=True)
s.curly((c + me) / 2 + (0.1, 0.12), (o + c) / 2 + (0.2, 0.18), bend=-0.6, single=True)
s.curly((c + me) / 2 + (0.1, -0.12), me + (-0.05, -0.32), bend=-0.6, single=True)
s.text((0, -1.9), "tert-butoxyl radical", size=10)
s.arrow((2.5, 0), (3.9, 0), above=r"$\beta$-scission")
s.molecule("CC(C)=O", at=(5.1, 0))
s.plus((6.4, 0))
s.molecule("[CH3]", at=(7.4, 0), labels={0: "CH$_3$"})
dot(s, (6.95, 0))
s.text((5.1, -1.3), "acetone", size=10)
finish(s)
