"""Legendre polynomials P_0, ..., P_5 on [-1, 1]."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 600)
fig, ax = plt.subplots(figsize=(8, 4.8))
for n in range(6):
    ax.plot(x, eval_legendre(n, x), label=f"$P_{n}$")
ax.axhline(0, color="gray", lw=0.8)
ax.set_xlim(-1, 1)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("x")
ax.set_title("Legendre polynomials")
ax.legend(ncol=3)
ax.grid(alpha=0.3)
fig.tight_layout()
