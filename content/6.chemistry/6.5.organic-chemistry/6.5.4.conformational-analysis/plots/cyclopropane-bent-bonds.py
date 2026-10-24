"""Bent ("banana") bonds of cyclopropane. The internuclear angle is 60 degrees, but the two ring-bonding
hybrid orbitals of each carbon make an angle of about 104 degrees, so each pair overlaps outside the
C-C axis (shaded lobes; curved lines show the bond paths). The poorer overlap makes the C-C bonds weak
and gives them some pi-like character."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Arc

ink = plt.rcParams["text.color"]
LOBE = "#2563eb"
fig, ax = plt.subplots(figsize=(5.2, 4.6))
R = 1.0  # circumradius; C-C = sqrt(3)
C = [R * np.array([np.cos(t), np.sin(t)]) for t in np.radians([90, 210, 330])]
half = np.radians(104 / 2)
for i in range(3):
    for j in (i - 1, (i + 1) % 3):
        d = C[j] - C[i]
        base = np.arctan2(d[1], d[0])
        # rotate the orbital axis away from the ring centre by (104 - 60) / 2 = 22 degrees
        out = C[i] - np.zeros(2)
        sign = np.sign(np.cross(d, -out)) or 1
        t = base - sign * (half - np.radians(30))
        u = np.array([np.cos(t), np.sin(t)])
        c = C[i] + 0.42 * u
        ax.add_patch(Ellipse(c, 0.8, 0.34, angle=np.degrees(t), color=LOBE, alpha=0.28, lw=0))
        ax.add_patch(Ellipse(c, 0.8, 0.34, angle=np.degrees(t), fill=False, color=LOBE, lw=1.0))
for i in range(3):
    a, b = C[i], C[(i + 1) % 3]
    m = (a + b) / 2
    bulge = m + 0.28 * m / np.linalg.norm(m)
    s = np.linspace(0, 1, 50)[:, None]
    path = (1 - s) ** 2 * a + 2 * s * (1 - s) * bulge + s**2 * b
    ax.plot(*path.T, color=ink, lw=2.0)
    ax.plot(*zip(a, b), color=ink, lw=0.8, ls=(0, (3, 3)))
for p in C:
    ax.plot(*p, "o", color=ink, ms=9)
# angle marks at the top carbon
top = C[0]
ax.add_patch(Arc(top, 0.7, 0.7, theta1=240, theta2=300, color=ink, lw=1.0))
ax.text(top[0], top[1] - 0.55, "60°", ha="center", va="center", fontsize=10)
ax.add_patch(Arc(top, 1.55, 1.55, theta1=270 - 52, theta2=270 + 52, color=LOBE, lw=1.0))
ax.text(top[0] + 0.72, top[1] - 0.62, "about 104°", ha="left", va="center", fontsize=10, color=LOBE)
ax.set_aspect("equal")
ax.set_xlim(-1.6, 2.3)
ax.set_ylim(-1.5, 1.9)
ax.axis("off")
