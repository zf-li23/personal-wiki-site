"""Columns of the unitary DFT matrix F_n: sampled complex exponentials of
increasing frequency, which form an orthonormal basis of C^n."""

import numpy as np
import matplotlib.pyplot as plt

n = 16
j = np.arange(n)
F = np.exp(2j * np.pi * np.outer(j, j) / n) / np.sqrt(n)

s = np.linspace(0, n, 400)
fig, axes = plt.subplots(2, 2, figsize=(11, 5.6), sharex=True, sharey=True)
for ax, k in zip(axes.flat, [0, 1, 2, 5]):
    col = F[:, k]
    ax.plot(s, np.cos(2 * np.pi * k * s / n) / np.sqrt(n), color="C0", linewidth=0.9, alpha=0.5)
    ax.plot(s, np.sin(2 * np.pi * k * s / n) / np.sqrt(n), color="C1", linewidth=0.9, alpha=0.5)
    ax.plot(j, col.real, "o", color="C0", markersize=5, label="real part")
    ax.plot(j, col.imag, "s", color="C1", markersize=4, label="imaginary part")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.set_title(rf"column $k = {k}$: entries $\omega_{{{n}}}^{{{k}j}} / \sqrt{{{n}}}$", fontsize=10)
    ax.grid(True, alpha=0.3)
for ax in axes[1]:
    ax.set_xlabel(r"index $j$")
axes[0, 0].legend(fontsize=8, loc="lower left")
fig.suptitle(rf"Orthonormal basis given by the columns of $F_{{{n}}}$")
fig.tight_layout()
