"""Classification of x' = A x in the trace-determinant plane (p, q) = (tr A, det A)."""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
p = np.linspace(-4, 4, 400)
ax.fill_between(p, -3, 0, color="C3", alpha=0.15)
ax.fill_between(p, 0, p**2 / 4, where=p < 0, color="C0", alpha=0.25)
ax.fill_between(p, p**2 / 4, 5, where=p < 0, color="C2", alpha=0.25)
ax.fill_between(p, 0, p**2 / 4, where=p > 0, color="C1", alpha=0.25)
ax.fill_between(p, p**2 / 4, 5, where=p > 0, color="C4", alpha=0.25)
ax.plot(p, p**2 / 4, color="k", lw=1.6, label=r"$p^2 = 4q$: star / degenerate nodes")
ax.plot([0, 0], [0, 5], color="C5", lw=3, label="p = 0, q > 0: centers")
ax.axhline(0, color="k", lw=0.8)
ax.axvline(0, color="k", lw=0.5, ls=":")
ax.text(0, -1.6, "saddles (unstable)", ha="center", fontsize=11)
ax.text(-3.3, 1.2, "stable\nnodes", ha="center", fontsize=11)
ax.text(3.3, 1.2, "unstable\nnodes", ha="center", fontsize=11)
ax.text(-1.4, 3.8, "stable foci", ha="center", fontsize=11)
ax.text(1.4, 3.8, "unstable foci", ha="center", fontsize=11)
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 5)
ax.set_xlabel("p = tr A")
ax.set_ylabel("q = det A")
ax.set_title("Planar linear systems: asymptotically stable iff p < 0 and q > 0")
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
