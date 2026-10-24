"""Radical chlorination at a stereocentre. A chlorine atom abstracts the tertiary hydrogen of
(S)-1-chloro-2-methylbutane; the 2-chloromethyl-2-butyl radical is (on average) planar, with the unpaired
electron in a p orbital. Cl2 transfers a chlorine atom to either face with equal probability, so the
two enantiomers of 1,2-dichloro-2-methylbutane form in equal amounts."""

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
sm = s.molecule("ClC[C@@H](C)CC", at=(0, 0))
s.text((0, -1.5), "(S)-1-chloro-2-methylbutane", size=10)
s.arrow((2.2, 0), (3.8, 0), above=r"Cl$\bullet$", below=r"$-$HCl")
rad = s.molecule("ClC[C](C)CC", at=(6.0, 0))
s.orbital(rad.atom(2), angle=90, phase=0, size=1.1)
s.text((6.0, -1.6), "planar radical, p orbital", size=10)
s.arrow((8.0, 0.5), (9.6, 1.4))
s.arrow((8.0, -0.5), (9.6, -1.4))
s.text((9.3, 0.5), r"Cl$_2$, top", size=10)
s.text((9.4, -0.5), r"Cl$_2$, bottom", size=10)
s.molecule("ClC[C@@](Cl)(C)CC", at=(11.8, 1.8))
s.molecule("ClC[C@](Cl)(C)CC", at=(11.8, -1.8))
s.text((14.7, 1.8), "(R)", size=10)
s.text((14.7, -1.8), "(S)", size=10)
s.text((11.8, -3.4), "racemic 1,2-dichloro-2-methylbutane", size=10)
s.draw()
