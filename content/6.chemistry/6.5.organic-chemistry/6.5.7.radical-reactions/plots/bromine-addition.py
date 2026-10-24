"""Why NBS keeps Br2 dilute. A bromine atom adds reversibly to the C=C bond of cyclohexene: its
unpaired electron and one pi electron form the C-Br bond, and the other pi electron stays on the
neighbouring carbon. The beta-bromoalkyl radical easily loses Br again by beta-scission; only if it
meets Br2 before that does it give the addition product (trans-1,2-dibromocyclohexane in the ionic
reaction). At very low Br2 concentration the irreversible abstraction of the allylic hydrogen wins."""

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
ring = [(0.0, 0.65), (0.0, -0.65), (1.13, -1.3), (2.25, -0.65), (2.25, 0.65), (1.13, 1.3)]
cy = s.molecule("C1=CCCCC1", coords=ring)
br = s.molecule("[Br]", at=(-1.9, 0.65), labels={0: "Br"})
b = br.xy(0)
dot(s, b + (0.38, 0))
c1, c2 = cy.xy(0), cy.xy(1)
m = (b + c1) / 2
s.curly(b + (0.4, 0.08), m + (0.0, 0.35), bend=0.6, single=True)
s.curly((c1 + c2) / 2 + (-0.12, 0.05), m + (0.12, 0.33), bend=-0.6, single=True)
s.curly((c1 + c2) / 2 + (-0.12, -0.05), c2 + (-0.3, -0.1), bend=0.6, single=True)
s.arrow((3.2, 0), (4.8, 0), above="addition", below=r"$\beta$-scission", kind="equilibrium")
s.molecule("BrC1[CH]CCCC1", coords=[(5.9, 1.3)] + [(x + 6.7, y) for x, y in ring])
s.text((7.8, -2.1), r"$\beta$-bromoalkyl radical", size=10)
s.arrow((9.9, 0), (11.9, 0), above=r"Br$_2$ (high conc.)", below=r"$-$Br$\bullet$")
s.molecule("Br[C@@H]1CCCC[C@H]1Br", at=(13.7, 0))
s.text((13.7, -2.1), "1,2-dibromide", size=10)
finish(s)
