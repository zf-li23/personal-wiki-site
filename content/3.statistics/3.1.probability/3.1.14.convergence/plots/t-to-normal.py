"""Densities of t_n for n = 1, 3, 10, 30 converge to the N(0,1) density."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.linspace(-5, 5, 800)
fig, ax = plt.subplots(figsize=(8, 4.5))
for n in [1, 3, 10, 30]:
    ax.plot(x, stats.t.pdf(x, n), lw=1.5, label=f"t_{n}")
ax.plot(x, stats.norm.pdf(x), color="black", lw=2, ls="--", label="N(0, 1)")
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("t_n -> N(0, 1) in distribution (Slutsky)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
