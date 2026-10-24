"""Kolbe electrolysis. At the anode acetate gives up one electron (single electron transfer)
to form the acetoxyl radical. In a beta-scission the unpaired electron on oxygen and one electron of
the C-CH3 bond form the second C=O pi bond of CO2, and the other electron leaves with the methyl
radical; two methyl radicals then couple to ethane."""

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
ac = s.molecule("CC(=O)[O-]", at=(0, 0), lone_pairs=[3])
s.arrow((1.6, 0), (3.0, 0), above=r"$-e^-$", below="anode")
r = s.molecule("CC(=O)[O]", coords=[(3.9, 0.0), (5.2, 0.0), (5.85, 1.08), (5.85, -1.08)], labels={3: "O"}, show_carbons=[0])
me, c, o = r.xy(0), r.xy(1), r.xy(3)
dot(s, o + (0.37, 0.0))
s.curly(o + (0.38, -0.08), (c + o) / 2 + (0.22, -0.1), bend=-0.9, single=True)
s.curly((me + c) / 2 + (0, -0.1), (c + o) / 2 + (-0.18, -0.1), bend=-0.6, single=True)
s.curly((me + c) / 2 + (0, 0.1), me + (0.1, 0.35), bend=-0.9, single=True)
s.text((5.0, -1.9), "acetoxyl radical", size=10)
s.arrow((6.8, 0), (8.0, 0), above=r"$\beta$-scission")
s.molecule("O=C=O", at=(9.3, 0), show_carbons=[1])
s.plus((10.7, 0))
s.molecule("[CH3]", at=(11.8, 0), labels={0: "CH$_3$"})
dot(s, (11.35, 0))
s.arrow((12.7, 0), (14.3, 0), above=r"$\times 2$, coupling")
s.molecule("CC", at=(15.5, 0), show_carbons=[0, 1])
finish(s)
