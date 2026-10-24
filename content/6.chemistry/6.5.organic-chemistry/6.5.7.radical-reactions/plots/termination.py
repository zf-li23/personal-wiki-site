"""Chain termination in methane chlorination: two radicals meet and their unpaired electrons pair
(fishhook arrows, one per electron). Left: chlorine atom and methyl radical give chloromethane.
Right: dioxygen, a triplet diradical, traps a methyl radical as the much less reactive methylperoxyl
radical, which explains the induction period caused by traces of O2."""

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
s.molecule("[Cl]", at=(0, 0), labels={0: "Cl"})
s.molecule("[CH3]", at=(2.4, 0), labels={0: "CH$_3$"})
dot(s, (0.38, 0))
dot(s, (1.85, 0))
pair(s, (0.38, 0), (1.85, 0), lift=0.4)
s.arrow((2.9, 0), (4.1, 0))
s.molecule("ClC", coords=[(4.7, 0), (6.0, 0)], show_carbons=[1])

s.molecule("[CH3]", at=(7.6, 0), labels={0: "H$_3$C"})
s.molecule("[O][O]", coords=[(9.7, 0), (10.9, 0)], labels={0: "O", 1: "O"})
dot(s, (8.15, 0))
dot(s, (9.35, 0))
dot(s, (11.25, 0))
pair(s, (8.15, 0), (9.35, 0), lift=0.4)
s.text((10.3, -0.9), r"O$_2$ (triplet)", size=10)
s.arrow((11.8, 0), (13.0, 0))
s.molecule("CO[O]", coords=[(13.7, 0), (15.0, 0), (16.0, 0.6)], show_carbons=[0], labels={2: "O"})
dot(s, (16.35, 0.75))
s.text((15.0, -0.9), "methylperoxyl", size=10)
finish(s)
