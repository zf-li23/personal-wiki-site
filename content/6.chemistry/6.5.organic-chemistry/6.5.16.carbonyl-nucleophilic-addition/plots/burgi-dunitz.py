"""Burgi-Dunitz trajectory. The carbonyl group is seen edge-on: the C=O bond lies in the page and
the plane of the molecule (the two R groups, one wedged and one hashed) is perpendicular to it. The
pi* orbital (LUMO) has a large lobe on carbon and a smaller lobe of opposite phase on oxygen, so a
nucleophile approaching from above overlaps best when it leans away from oxygen, at about 107
degrees to the C=O bond."""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon

from wikichem import Scheme

s = Scheme(scale=0.6)
C, O = np.array([0.0, 0.0]), np.array([1.25, 0.0])
s.orbital(C, angle=90, phase=1, size=1.5)
s.orbital(O, angle=90, phase=-1, size=0.8)
s.text(C, "C")
s.text(O, "O")

t = math.radians(107)
nu = np.array([2.6 * math.cos(t), 2.6 * math.sin(t)])
s.text(nu + np.array([-0.15, 0.25]), r"Nu$^-$")
s.partial(nu, (0.0, 0.25))
s.text((0.75, 0.75), r"107$^\circ$", size=11)
s.text((-1.45, -0.55), "R")
s.text((-1.3, 0.35), "R")
s.text((0.6, -1.3), r"$\pi^*$ (LUMO)", size=11)
s.text((-1.6, 1.8), "")
fig, ax = s.draw()
ink = plt.rcParams["text.color"]
for o in (-0.07, 0.07):  # the C=O double bond, drawn between the two labels
    ax.plot([0.25, 1.0], [o, o], color=ink, lw=1.4)
# the two R groups: one wedge (towards the viewer) and one hashed bond (away)
a, b = np.array([-0.2, -0.1]), np.array([-1.2, -0.45])
u = (b - a) / np.linalg.norm(b - a)
n = np.array([-u[1], u[0]])
ax.add_patch(Polygon([a, b + 0.09 * n, b - 0.09 * n], closed=True, color=ink, lw=0))
a2, b2 = np.array([-0.2, 0.1]), np.array([-1.1, 0.3])
u2 = (b2 - a2) / np.linalg.norm(b2 - a2)
n2 = np.array([-u2[1], u2[0]])
for k in np.linspace(0.15, 1, 7):
    p = a2 + k * (b2 - a2)
    ax.plot([p[0] - 0.09 * k * n2[0], p[0] + 0.09 * k * n2[0]], [p[1] - 0.09 * k * n2[1], p[1] + 0.09 * k * n2[1]], color=ink, lw=1.1)
ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=0, theta2=107, color=ink, lw=1.0))
