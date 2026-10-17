"""LLN and CLT together for Exp(1) samples: M_n concentrates at 1 (LLN) with an approximately N(1, 1/n) shape (CLT)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

reps = 20000
fig, ax = plt.subplots(figsize=(8, 4.5))
x = np.linspace(0, 3, 600)
for n, color in [(1, "C0"), (5, "C1"), (25, "C2"), (100, "C3")]:
    m = np.random.exponential(size=(reps, n)).mean(axis=1)
    ax.hist(m, bins=120, range=(0, 3), density=True, histtype="step", color=color, lw=1.2, label=f"M_n, n = {n}")
    if n > 1:
        ax.plot(x, stats.norm.pdf(x, 1, 1 / np.sqrt(n)), color=color, lw=1, ls="--")
ax.axvline(1, color="black", lw=1)
ax.set_xlabel("sample mean")
ax.set_ylabel("density")
ax.set_ylim(0, 4.3)
ax.set_title("Exp(1) sample means (solid) and N(1, 1/n) approximations (dashed)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
