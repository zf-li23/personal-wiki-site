"""Stereospecific E2 of the 1,2-dibromo-1,2-diphenylethanes, drawn as Newman projections along C1-C2
in the conformation where the front H and the back Br are antiperiplanar. Top: in the meso isomer
the front Br and the back phenyl are then anti, so after elimination they are trans and the two
phenyl groups are cis: (E)-1-bromo-1,2-diphenylethene. Bottom: in the racemic isomer (one
enantiomer shown) the front Br and the back phenyl are gauche, giving the (Z)-alkene."""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

from wikichem import Scheme

s = Scheme()
R0, R1, RL = 0.55, 1.25, 1.62  # circle radius, bond end, label distance
LINES = []  # (centre, front?, angle)


def u(deg):
    t = math.radians(deg)
    return np.array([math.cos(t), math.sin(t)])


def newman(c, front, back):
    """front/back: lists of (angle in degrees, label)."""
    c = np.asarray(c, float)
    for group, is_front in ((front, True), (back, False)):
        for a, text in group:
            LINES.append((c, is_front, a))
            s.text(c + RL * u(a), text)
    s.text(c + np.array([0, -R1 - 0.6]), "")
    s.text(c + np.array([0, R1 + 0.4]), "")
    return c


rows = ((0.0, [(30, "Ph"), (150, "H")], "Br/C(c1ccccc1)=C/c1ccccc1", "meso", "(E)", 6.2),
        (-5.6, [(150, "Ph"), (30, "H")], r"Br/C(c1ccccc1)=C\c1ccccc1", "racemic", "(Z)", 7.4))
for y, back, product, name, label, px in rows:
    c = newman((0, y), [(90, "H"), (210, "Br"), (330, "Ph")], back + [(270, "Br")])
    s.text((-2.6, y + 2.3), r"EtO$^-$")
    s.curly(np.array([-2.0, y + 2.15]), c + 1.45 * u(90) + np.array([-0.25, 0.05]), bend=-0.3)
    s.curly(c + 0.75 * u(90) + np.array([0.08, 0]), c + np.array([0.12, 0.05]), bend=-0.9)
    s.curly(c + 0.95 * u(270) + np.array([0.08, 0]), c + 1.45 * u(270) + np.array([0.35, 0.0]), bend=-0.9)
    s.text((0, y - 2.4), name)
    s.arrow((2.4, y), (3.8, y), below=r"$-$HBr")
    s.molecule(product, at=(px, y))
    s.text((px, y - 2.4), label)

fig, ax = s.draw()
ink = plt.rcParams["text.color"]
for c, is_front, a in LINES:
    start = c if is_front else c + R0 * u(a)
    end = c + R1 * u(a)
    ax.plot(*zip(start, end), color=ink, lw=1.4, solid_capstyle="round")
for y, *_ in rows:
    ax.add_patch(Circle((0, y), R0, fill=False, color=ink, lw=1.4))
