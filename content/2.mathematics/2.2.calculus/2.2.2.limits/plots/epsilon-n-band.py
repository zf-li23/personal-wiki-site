"""The epsilon-N definition: a_n = 1 + (-1)^n / n stays in the band (1 - eps, 1 + eps) for n > N."""

import numpy as np
import matplotlib.pyplot as plt

A = 1.0
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
n = np.arange(1, 41)
a = A + (-1.0) ** n / n

for ax, eps in zip(axes, (0.3, 0.12)):
    N = int(np.floor(1 / eps))
    inside = n > N
    ax.axhspan(A - eps, A + eps, color="C0", alpha=0.15)
    ax.axhline(A, color="C0", lw=1)
    ax.axvline(N + 0.5, color="C3", lw=1, ls="--")
    ax.plot(n[~inside], a[~inside], "o", color="C1", ms=5, label="$n \\leq N$")
    ax.plot(n[inside], a[inside], "o", color="C0", ms=5, label="$n > N$")
    ax.text(N + 1, 0.12, f"$N = {N}$", color="C3", fontsize=10)
    ax.set_title(f"$\\varepsilon = {eps}$: only finitely many terms outside the band", fontsize=11)
    ax.set_xlabel("$n$")
    ax.set_ylim(-0.1, 1.65)
    ax.legend(loc="upper right", fontsize=9)
axes[0].set_ylabel("$a_n = 1 + (-1)^n / n$")
fig.tight_layout()
