"""Spectral norm of A^k for three 2x2 matrices: the spectral radius decides the
limit, while non-normality can cause a large transient growth first."""

import numpy as np
import matplotlib.pyplot as plt

cases = [
    (np.array([[0.9, 0.0], [0.0, 0.5]]), r"normal, $\rho(A) = 0.9$"),
    (np.array([[0.9, 4.0], [0.0, 0.5]]), r"non-normal, $\rho(A) = 0.9$"),
    (np.array([[1.05, 0.0], [0.0, 0.3]]), r"normal, $\rho(A) = 1.05$"),
]

k = np.arange(0, 61)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for A, label in cases:
    norms = [np.linalg.norm(np.linalg.matrix_power(A, j), 2) for j in k]
    ax.semilogy(k, norms, marker="o", markersize=2.5, linewidth=1.4, label=label)
ax.axhline(1.0, linewidth=0.8, linestyle="--", color="gray")
ax.set_xlabel(r"$k$")
ax.set_ylabel(r"$\|A^k\|_2$")
ax.set_title("Powers of a matrix and its spectral radius")
ax.legend()
fig.tight_layout()
