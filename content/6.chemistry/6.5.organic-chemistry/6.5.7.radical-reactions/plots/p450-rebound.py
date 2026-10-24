"""Oxygen rebound mechanism of cytochrome P450 (Groves), simplified. Top: compound I, an oxo-iron(IV)
porphyrin radical cation whose oxygen behaves like an oxyl radical, abstracts a hydrogen atom from
cyclohexane, giving Fe(IV)-OH and a cyclohexyl radical. Bottom: the radical pairs with one electron of
the Fe-O bond and takes the hydroxyl group (rebound); the other electron returns to iron, Fe(III).
Por = porphyrin."""

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


hexa = [(1.0 + np.cos(np.radians(a)), np.sin(np.radians(a))) for a in (180, 240, 300, 0, 60, 120)]


def iron(s, xy, ox):
    """An iron atom with its oxidation state as a superscript."""
    s.text((xy[0] + 0.42, xy[1] + 0.28), ox, size=8)


s = Scheme()
fe = s.molecule("*[O]", coords=[(-4.4, 0), (-3.1, 0)], labels={0: "Fe", 1: "O"})
iron(s, fe.xy(0), "IV")
o = fe.xy(1)
dot(s, o + (0.37, 0))
cy = s.molecule("[H]C1CCCCC1", coords=[(-1.1, 0)] + hexa, labels={0: "H"})
h, c = cy.xy(0), cy.xy(1)
mid = (o + h) / 2
s.curly(o + (0.38, 0.08), mid + (-0.08, 0.4), bend=0.6, single=True)
s.curly((h + c) / 2 + (0, 0.1), mid + (0.08, 0.4), bend=-0.6, single=True)
s.curly((h + c) / 2 + (0, -0.1), c + (-0.05, -0.33), bend=0.6, single=True)
s.text((-3.7, -1.0), "compound I", size=10)
s.text((-3.7, -1.5), r"(Por$^{+\bullet}$)Fe$^{\mathrm{IV}}$=O", size=9)
s.arrow((2.6, 0), (3.8, 0), above="HAT")
fe2 = s.molecule("*O", coords=[(4.6, 0), (5.9, 0)], labels={0: "Fe", 1: "OH"})
iron(s, fe2.xy(0), "IV")
s.plus((7.0, 0))
s.molecule("[CH]1CCCCC1", at=(8.6, 0))
finish(s)

s = Scheme()
fe = s.molecule("*O", coords=[(-1.3, 0), (0, 0)], labels={0: "Fe", 1: "HO"})
iron(s, fe.xy(0), "IV")
rad = s.molecule("[CH:1]1[CH2:2][CH2:3][CH2:4][CH2:5][CH2:6]1", coords=[(x + 1.9, y) for x, y in hexa])
c = rad.xy(1)
m = (fe.xy(1) + c) / 2
s.curly(rad.atom(1), m + (0.08, 0.4), bend=-0.6, single=True)
s.curly(fe.bond(0, 1).xy + (0.1, 0.1), m + (-0.08, 0.4), bend=0.6, single=True)
s.curly(fe.bond(0, 1).xy + (0, -0.1), fe.xy(0) + (0.1, -0.35), bend=-0.6, single=True)
s.arrow((4.9, 0), (6.1, 0), above="rebound")
s.text((7.1, 0), "Fe")
iron(s, (7.1, 0), "III")
s.plus((8.1, 0))
s.molecule("OC1CCCCC1", at=(9.8, 0))
s.text((9.8, -1.4), "cyclohexanol", size=10)
finish(s)
