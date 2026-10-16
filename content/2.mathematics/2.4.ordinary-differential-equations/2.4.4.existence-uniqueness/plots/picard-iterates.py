"""Picard iterates for y' = y, y(0) = 1: partial sums of the exponential series."""

import math

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 500)
fig, ax = plt.subplots(figsize=(7, 4.8))
ax.plot(x, np.exp(x), color="k", lw=2.6, alpha=0.75, label="exact solution e^x")
for n in range(5):
    phi = sum(x ** k / math.factorial(k) for k in range(n + 1))
    ax.plot(x, phi, lw=1.6, color=f"C{n}", label=f"phi_{n}")
ax.plot([0], [1], "o", color="C3", ms=6)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Picard iteration for y' = y, y(0) = 1")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
