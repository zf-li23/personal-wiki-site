"""Resonance structures of the benzyl radical. In the first structure the unpaired electron and
one electron of a ring pi bond form the exocyclic C=C pi bond, and the other pi electron moves to the
ortho carbon (fishhook arrows). The unpaired electron is shared by the CH2 carbon and the two ortho
and the para carbons."""

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


SM = ["[CH2:1][C:2]1=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1",
      "[CH2:1]=[C:2]1[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1",
      "[CH2:1]=[C:2]1[CH:3]=[CH:4][CH:5][CH:6]=[CH:7]1",
      "[CH2:1]=[C:2]1[CH:3]=[CH:4][CH:5]=[CH:6][CH:7]1"]
s = Scheme(scale=0.5)
first = s.molecule(SM[0], at=(0, 0), rotate=-120)
c1, c2, c3 = first.xy(1), first.xy(2), first.xy(3)
m12, m23 = (c1 + c2) / 2, (c2 + c3) / 2
ring = first.coords[1:].mean(axis=0)
out12 = m12 - ring  # side of the exocyclic bond away from the ring centre
out12 = np.array([-out12[1], out12[0]]) if np.dot(np.array([-out12[1], out12[0]]), c3 - c2) < 0 else -np.array([-out12[1], out12[0]])
out12 = out12 / np.linalg.norm(out12)
in23 = (ring - m23) / np.linalg.norm(ring - m23)
s.curly(first.atom(1), m12 - 0.22 * out12, bend=-0.6, single=True)
s.curly(m23 - 0.1 * (c3 - c2), m12 + 0.12 * in23, bend=0.6, single=True)
s.curly(m23 + 0.15 * (c3 - c2) / 1.0, c3 + 0.3 * in23, bend=-0.6, single=True)
x = 0
for sm in SM[1:]:
    s.arrow((x + 1.6, 0), (x + 2.8, 0), kind="resonance")
    x += 4.4
    s.molecule(sm, at=(x, 0), like=first)
finish(s)
