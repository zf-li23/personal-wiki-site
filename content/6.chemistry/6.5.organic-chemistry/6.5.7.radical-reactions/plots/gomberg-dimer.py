"""Gomberg's dimer. Two triphenylmethyl radicals cannot join at their central carbons (the six
phenyl groups would clash); instead the central carbon of one radical pairs with the para carbon of
another, where the unpaired electron also resides (resonance form on the right). The product is the
quinoid dimer, which in solution dissociates partly back into the radicals."""

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


s = Scheme(scale=0.36)
a = s.molecule("[C](c1ccccc1)(c1ccccc1)c1ccccc1", at=(0, 0))
q = "[CH:1]1=[CH:2][C:3](=[C:4](c2ccccc2)c2ccccc2)[CH:5]=[CH:6][CH:7]1"
b = s.molecule(q, at=(7.0, 0), rotate=0)
pa, pb = a.xy(0), b.xy(7)
m = (pa + pb) / 2 + (0, 0.9)
s.curly(a.atom(0), m - (0.1, 0), bend=0.4, single=True)
s.curly(b.atom(7), m + (0.1, 0), bend=-0.4, single=True)
s.text((0, -2.8), "trityl radical", size=10)
s.text((7.0, -2.8), "trityl radical (para resonance form)", size=10)
s.arrow((10.6, 0), (12.0, 0))
s.molecule("C1=CC(C=CC1=C(c2ccccc2)c3ccccc3)C(c4ccccc4)(c5ccccc5)c6ccccc6", at=(16.5, 0))
s.text((16.5, -4.6), "quinoid dimer (Gomberg's hydrocarbon)", size=10)
finish(s)
