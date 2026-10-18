"""BLUE is not the end of the story: a biased estimator can have smaller mean squared error."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

beta = 0.0
g = np.linspace(-6, 6, 600)
rivals = [
    ("rival 1: biased, small variance", -1.2, 0.5, "C2", ":"),
    ("OLS: unbiased, the smallest variance among linear unbiased", 0.0, 1.0, "C0", "-"),
    ("rival 2: unbiased, larger variance", 0.0, 2.0, "C3", "--"),
]
fig, ax = plt.subplots(figsize=(8, 4.2))
for name, bias, sd, c, ls in rivals:
    mse = bias**2 + sd**2
    ax.plot(g, stats.norm.pdf(g, beta + bias, sd), color=c, ls=ls, lw=1.8, label=f"{name} (MSE = {mse:.2f})")
ax.axvline(beta, color="0.5", lw=1)
ax.text(beta + 0.1, 0.78, "true beta", color="0.4", fontsize=9)
ax.set_xlabel("estimate")
ax.set_ylabel("density")
ax.set_ylim(0, 0.85)
ax.legend(fontsize=9, loc="upper right")
ax.grid(alpha=0.3)
fig.tight_layout()
