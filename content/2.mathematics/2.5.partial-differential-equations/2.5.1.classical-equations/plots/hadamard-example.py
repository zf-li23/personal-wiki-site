"""Hadamard's example: Cauchy data sin(nx)/n for the Laplace equation and the growth of the solution."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = np.linspace(0, 2 * np.pi, 1000)
for i, n in enumerate([2, 5, 10]):
    ax1.plot(x, np.sin(n * x) / n, color=f"C{i}", lw=1.5, label=f"n = {n}")
ax1.set_xlim(0, 2 * np.pi)
ax1.set_xlabel("x")
ax1.set_ylabel("u_y(x, 0)")
ax1.set_title("Cauchy data sin(nx)/n tend to 0")
ax1.legend(loc="upper right", fontsize=9)

n = np.arange(1, 31)
for i, y in enumerate([0.5, 1.0, 2.0]):
    ax2.semilogy(n, np.sinh(n * y) / n**2, "o-", ms=3, color=f"C{i}", lw=1.3, label=f"y = {y}")
ax2.semilogy(n, 1 / n, "--", color="0.5", lw=1.3, label="size of data 1/n")
ax2.set_xlabel("n")
ax2.set_ylabel("max |u_n(x, y)|")
ax2.set_title("Solution amplitude sinh(ny)/n^2")
ax2.legend(loc="upper left", fontsize=9)

fig.tight_layout()
