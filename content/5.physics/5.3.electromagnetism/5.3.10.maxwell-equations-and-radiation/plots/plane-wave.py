"""Snapshot of a linearly polarized plane electromagnetic wave travelling along +x."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 400)          # in wavelengths
phase = 2 * np.pi * x
E = np.cos(phase)                   # E along y
B = np.cos(phase)                   # B along z, in phase with E (scaled to the same height)

fig = plt.figure(figsize=(9, 4.2))
ax = fig.add_subplot(projection="3d")
ax.plot(x, E, 0 * x, color="C0", lw=2, label="E (along y)")
ax.plot(x, 0 * x, B, color="C3", lw=2, label="B (along z)")
for xi in x[::12]:
    c = np.cos(2 * np.pi * xi)
    ax.plot([xi, xi], [0, c], [0, 0], color="C0", lw=0.6, alpha=0.6)
    ax.plot([xi, xi], [0, 0], [0, c], color="C3", lw=0.6, alpha=0.6)
ax.plot([0, 2.25], [0, 0], [0, 0], color="0.3", lw=1)
ax.set_title("E, B and the propagation direction x form a right-handed set; E and B are in phase", fontsize=9)
ax.set_xlabel("x / wavelength")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_yticks([-1, 0, 1])
ax.set_zticks([-1, 0, 1])
ax.set_box_aspect((2.4, 1.2, 1.2))
ax.view_init(elev=22, azim=-40)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
