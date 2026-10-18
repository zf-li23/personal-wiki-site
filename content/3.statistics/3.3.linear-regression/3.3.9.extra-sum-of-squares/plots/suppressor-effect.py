"""Suppression: R^2_{Y2|1} = r_Y2^2 / (1 - r_12^2) when X1 is uncorrelated with Y."""

import numpy as np
import matplotlib.pyplot as plt

r12 = np.linspace(0, 0.95, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
for ry2, col in [(0.2, "C0"), (0.3, "C1"), (0.5, "C2")]:
    # the correlation matrix must stay positive definite: r_Y2^2 + r_12^2 < 1
    ok = ry2 ** 2 + r12 ** 2 < 1
    partial = ry2 ** 2 / (1 - r12[ok] ** 2)
    ax.plot(r12[ok], partial, color=col, lw=2, label=f"r_Y2 = {ry2}: partial R^2_Y2|1")
    ax.axhline(ry2 ** 2, color=col, ls=":", lw=1.2)
ax.set_xlabel("correlation r_12 between X1 and X2")
ax.set_ylabel("proportion of variation")
ax.set_ylim(0, 1)
ax.set_title("With r_Y1 = 0, controlling for X1 makes X2 more useful (dotted: r_Y2^2)")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
