"""Sample paths of the running mean of fair-coin tosses, with the band p +- 0.03."""

import numpy as np
import matplotlib.pyplot as plt

p, eps, n_max, paths = 0.5, 0.03, 2000, 20
n = np.arange(1, n_max + 1)
x = np.random.binomial(1, p, size=(paths, n_max))
means = np.cumsum(x, axis=1) / n

fig, ax = plt.subplots(figsize=(8, 4.5))
for m in means:
    ax.plot(n, m, lw=0.8, alpha=0.7)
ax.axhline(p, color="black", lw=1.2)
ax.axhline(p + eps, color="black", lw=1.0, ls="--")
ax.axhline(p - eps, color="black", lw=1.0, ls="--")
ax.set_xscale("log")
ax.set_ylim(0, 1)
ax.set_xlabel("n (log scale)")
ax.set_ylabel("M_n = (X_1 + ... + X_n) / n")
ax.set_title("Running means of Ber(0.5): 20 sample paths and the band 0.5 +- 0.03")
ax.grid(alpha=0.3)
fig.tight_layout()
