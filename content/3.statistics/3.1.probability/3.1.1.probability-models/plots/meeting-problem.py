"""Geometric probability: the meeting problem on the unit square, |x - y| <= 1/4."""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))
t = 0.25
poly_x = [0, t, 1, 1, 1 - t, 0]
poly_y = [0, 0, 1 - t, 1, 1, t]
ax.fill(poly_x, poly_y, color="C0", alpha=0.35, label="M: |x - y| <= 1/4")
ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color="black", lw=1.2)
ax.plot([t, 1], [0, 1 - t], color="C0", lw=1.5)
ax.plot([0, 1 - t], [t, 1], color="C0", lw=1.5)

rng = np.random.default_rng(0)
pts = rng.uniform(size=(400, 2))
inside = np.abs(pts[:, 0] - pts[:, 1]) <= t
ax.scatter(pts[inside, 0], pts[inside, 1], s=6, color="C0", label="simulated: meet")
ax.scatter(pts[~inside, 0], pts[~inside, 1], s=6, color="C3", label="simulated: miss")
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.set_aspect("equal")
ax.set_xlabel("delay of first person x (hours)")
ax.set_ylabel("delay of second person y (hours)")
ax.set_title(f"area(M) = 7/16 = 0.4375, simulated: {inside.mean():.3f}")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
