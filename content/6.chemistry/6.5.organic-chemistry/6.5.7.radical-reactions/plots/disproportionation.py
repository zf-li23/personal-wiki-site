"""Two ways in which two ethyl radicals destroy each other. Top: coupling, the two unpaired electrons
pair to form the new C-C bond of butane. Bottom: disproportionation, one radical abstracts a beta
hydrogen from the other: the unpaired electron of the left radical and one electron of the C-H bond
form the new C-H bond, and the other C-H electron pairs with the unpaired electron of the right
radical as the new pi bond, giving ethane and ethene."""

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
s.molecule("C[CH2]", coords=[(-1.3, 0), (0, 0)], show_carbons=[0], labels={1: "CH$_2$"})
s.molecule("C[CH2]", coords=[(3.8, 0), (2.5, 0)], show_carbons=[0], labels={1: "H$_2$C"})
dot(s, (0.5, 0.0))
dot(s, (2.0, 0.0))
pair(s, (0.5, 0.0), (2.0, 0.0), lift=0.45)
s.arrow((4.7, 0), (6.1, 0), above="coupling")
s.molecule("CCCC", at=(7.9, 0))
s.text((7.9, -1.1), "butane", size=10)
finish(s)

s = Scheme()
s.molecule("C[CH2]", coords=[(-1.3, 0), (0, 0)], show_carbons=[0], labels={1: "CH$_2$"})
b = s.molecule("[H][CH2][CH2]", coords=[(2.1, 0), (3.4, 0), (4.05, -1.15)], labels={1: "CH$_2$", 2: "CH$_2$"})
dot(s, (0.5, 0.0))
dot(s, b.xy(2) + (0.05, 0.33))
h, c2, c3 = b.xy(0), b.xy(1), b.xy(2)
s.curly((0.5, 0.08), (1.2, 0.42), bend=0.7, single=True)  # radical electron to the new C-H bond
s.curly((h + c2) / 2 + (0, 0.12), (1.35, 0.42), bend=-0.6, single=True)  # one C-H electron to the new C-H bond
s.curly((h + c2) / 2 + (0, -0.12), (c2 + c3) / 2 + (-0.2, -0.1), bend=0.7, single=True)  # the other to the new pi bond
s.curly(b.xy(2) + (0.12, 0.38), (c2 + c3) / 2 + (0.2, 0.1), bend=0.9, single=True)  # second radical electron to the pi bond
s.arrow((5.2, 0), (7.0, 0), above="disproportionation")
s.molecule("CC", at=(8.2, 0), show_carbons=[0, 1])
s.plus((9.6, 0))
s.molecule("C=C", at=(11.0, 0), show_carbons=[0, 1])
s.text((8.2, -1.0), "ethane", size=10)
s.text((11.0, -1.0), "ethene", size=10)
finish(s)
