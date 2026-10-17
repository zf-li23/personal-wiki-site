"""Exact density of (S_n - n)/sqrt(n) for i.i.d. Exp(1) summands versus the N(0,1) density."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

z = np.linspace(-4, 4, 800)
fig, ax = plt.subplots(figsize=(8, 4.5))
for n in [1, 2, 5, 30]:
    # S_n ~ Gamma(n, 1); density of Z_n = (S_n - n)/sqrt(n)
    dens = stats.gamma.pdf(n + np.sqrt(n) * z, a=n) * np.sqrt(n)
    ax.plot(z, dens, lw=1.5, label=f"n = {n}")
ax.plot(z, stats.norm.pdf(z), color="black", lw=2, ls="--", label="N(0, 1)")
ax.set_xlabel("z")
ax.set_ylabel("density")
ax.set_ylim(0, 0.75)
ax.set_title("Standardized sums of Exp(1): skewness fades like 1/sqrt(n)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
