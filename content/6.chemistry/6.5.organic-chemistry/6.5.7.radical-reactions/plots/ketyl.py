"""Formation of the benzophenone ketyl. Sodium gives one electron (fishhook) to the carbonyl
group: it pairs on oxygen with one electron of the C=O pi bond, which becomes a lone pair, and the
other pi electron stays on carbon. The product is a radical anion: negative charge on oxygen,
unpaired electron on carbon (delocalised into both rings)."""

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
k = s.molecule("O=C(c1ccccc1)c1ccccc1", at=(0, 0), rotate=0, lone_pairs=[0])
o, c = k.xy(0), k.xy(1)
na = o + (1.5, 1.1)
s.molecule("[Na]", at=tuple(na), labels={0: "Na"})
dot(s, na + (-0.42, 0))
s.curly(na + (-0.44, 0.05), o + (0.25, 0.3), bend=0.6, single=True)
s.curly((o + c) / 2 + (0.1, -0.08), o + (0.32, -0.1), bend=0.9, single=True)
s.text((0, -2.9), "benzophenone", size=10)
s.arrow((2.8, 0), (4.2, 0))
s.molecule("[O-][C](c1ccccc1)c1ccccc1", at=(7.0, 0), lone_pairs=[0], like=k)
s.text((7.0, -2.9), "ketyl (deep blue)", size=10)
s.text((9.9, 0.0), r"Na$^+$")
finish(s)
