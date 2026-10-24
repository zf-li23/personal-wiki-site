"""Allylic rearrangement in the NBS bromination of 1-butene. Abstraction of the allylic hydrogen
gives the 1-methylallyl radical, whose unpaired electron is shared by C1 and C3 (fishhook arrows: the
unpaired electron and one pi electron form the new C2=C3 pi bond, the other pi electron moves to C1).
Bromine transfer from Br2 at either end gives 3-bromo-1-butene and 1-bromo-2-butene."""

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


s = Scheme(scale=0.5)
a = s.molecule("[CH2:1]=[CH:2][CH:3][CH3:4]", coords=[(-1.3, -0.4), (-0.65, 0.4), (0.65, 0.4), (1.3, -0.4)])
c1, c2, c3 = a.xy(1), a.xy(2), a.xy(3)
s.curly(a.atom(3), (c2 + c3) / 2 + (0.0, 0.12), bend=0.7, single=True)
s.curly((c1 + c2) / 2 + (0.1, 0.0), (c2 + c3) / 2 + (-0.1, 0.12), bend=-0.7, single=True)
s.curly((c1 + c2) / 2 + (-0.1, -0.05), c1 + (-0.25, 0.1), bend=-0.8, single=True)
s.arrow((2.1, 0), (3.3, 0), kind="resonance")
s.molecule("[CH2:1][CH:2]=[CH:3][CH3:4]", coords=[(x + 4.6, y) for x, y in [(-1.3, -0.4), (-0.65, 0.4), (0.65, 0.4), (1.3, -0.4)]])
s.text((2.7, -1.5), "1-methylallyl radical (from 1-butene + Br)", size=10)
s.arrow((6.3, 0), (7.7, 0), above=r"Br$_2$", below=r"$-$Br$\bullet$")
s.molecule("C=CC(C)Br", at=(9.2, 0))
s.plus((11.0, 0))
s.molecule("BrC/C=C/C", at=(13.4, 0))
s.text((9.2, -1.6), "3-bromo-1-butene", size=10)
s.text((13.4, -1.6), "1-bromo-2-butene (E, Z)", size=10)
finish(s)
