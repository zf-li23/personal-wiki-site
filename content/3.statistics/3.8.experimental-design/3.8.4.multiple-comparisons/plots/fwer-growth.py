"""Probability of at least one false positive among m independent tests, without and with Bonferroni."""

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.05
m = np.arange(1, 101)
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.plot(m, 1 - (1 - alpha) ** m, color="C3", lw=2, label="each test at level 0.05")
ax.plot(m, 1 - (1 - alpha / m) ** m, color="C0", lw=2, label="each test at level 0.05/m (Bonferroni)")
ax.axhline(alpha, color="gray", ls="--", lw=1)
for k in (6, 20):
    v = 1 - (1 - alpha) ** k
    ax.plot(k, v, "o", color="C3")
    ax.annotate(f"m = {k}: {v:.2f}", (k, v), xytext=(k + 4, v - 0.08))
ax.set_xlabel("number of tests m")
ax.set_ylabel("P(at least one false positive)")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, loc="center right")
ax.grid(alpha=0.3)
fig.tight_layout()
