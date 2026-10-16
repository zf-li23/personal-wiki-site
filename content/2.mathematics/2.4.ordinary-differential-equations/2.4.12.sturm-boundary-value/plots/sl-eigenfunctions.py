"""First eigenfunctions of two Dirichlet Sturm-Liouville problems."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
x = np.linspace(0, np.pi, 400)
for n in range(1, 5):
    ax.plot(x, np.sin(n * x), color=f"C{n - 1}", lw=1.6, label=f"n = {n}, lambda = {n * n}")
ax.axhline(0, color="0.5", lw=0.8)
ax.set_xlim(0, np.pi)
ax.set_title("y'' + lambda y = 0,  y(0) = y(pi) = 0")
ax.set_xlabel("x")
ax.legend(loc="lower left", fontsize=8)

# -((1 + x) y')' = lambda y on (0, 1), Dirichlet; finite differences
N = 800
h = 1.0 / N
xi = np.linspace(h, 1 - h, N - 1)
p_half = 1 + np.linspace(h / 2, 1 - h / 2, N)  # p at midpoints
diag = (p_half[:-1] + p_half[1:]) / h**2
off = -p_half[1:-1] / h**2
vals, vecs = eigh_tridiagonal(diag, off, select="i", select_range=(0, 3))
ax = axes[1]
xx = np.concatenate([[0], xi, [1]])
for n in range(4):
    v = np.concatenate([[0], vecs[:, n], [0]])
    v = v / np.max(np.abs(v))
    if v[1] < 0:  # start upward, like sin(n x)
        v = -v
    ax.plot(xx, v, color=f"C{n}", lw=1.6, label=f"n = {n + 1}, lambda = {vals[n]:.1f}")
ax.axhline(0, color="0.5", lw=0.8)
ax.set_xlim(0, 1)
ax.set_title("-((1 + x) y')' = lambda y,  y(0) = y(1) = 0")
ax.set_xlabel("x")
ax.legend(loc="lower left", fontsize=8)

fig.tight_layout()
