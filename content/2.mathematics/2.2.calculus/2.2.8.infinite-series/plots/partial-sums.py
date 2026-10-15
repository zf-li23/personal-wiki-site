"""Partial sums of three series, and a rearrangement of the alternating harmonic
series that converges to half of its sum."""

import numpy as np
import matplotlib.pyplot as plt

N = 60
n = np.arange(1, N + 1)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))

ax = axes[0]
ax.plot(n, np.cumsum(1 / n), "o-", markersize=2.5, linewidth=1, color="C0",
        label=r"$\sum 1/n$ (diverges like $\ln n$)")
ax.plot(n, np.log(n) + 0.5772, color="C0", linewidth=0.8, linestyle=":")
ax.plot(n, np.cumsum(1 / n**2), "o-", markersize=2.5, linewidth=1, color="C2",
        label=r"$\sum 1/n^2 \to \pi^2/6$")
ax.axhline(np.pi**2 / 6, color="C2", linewidth=0.8, linestyle="--")
alt = np.cumsum((-1.0) ** (n - 1) / n)
ax.plot(n, alt, "o-", markersize=2.5, linewidth=1, color="C1",
        label=r"$\sum (-1)^{n-1}/n \to \ln 2$")
ax.axhline(np.log(2), color="C1", linewidth=0.8, linestyle="--")
ax.set_xlabel(r"$n$")
ax.set_ylabel(r"partial sum $S_n$")
ax.set_title("Partial sums", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(True, alpha=0.3)

ax = axes[1]
terms = []
odd, even = 1, 2
while len(terms) < 3 * N:
    terms += [1 / odd, -1 / even, -1 / (even + 2)]
    odd += 2
    even += 4
m = np.arange(1, len(terms) + 1)
ax.plot(np.arange(1, 3 * N + 1), np.cumsum((-1.0) ** (np.arange(1, 3 * N + 1) - 1) / np.arange(1, 3 * N + 1)),
        linewidth=1, color="C1", label=r"$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \to \ln 2$")
ax.plot(m, np.cumsum(terms), linewidth=1, color="C4",
        label=r"$1 - \frac{1}{2} - \frac{1}{4} + \frac{1}{3} - \frac{1}{6} - \frac{1}{8} + \cdots \to \frac{1}{2}\ln 2$")
ax.axhline(np.log(2), color="C1", linewidth=0.8, linestyle="--")
ax.axhline(np.log(2) / 2, color="C4", linewidth=0.8, linestyle="--")
ax.set_xlabel("number of terms")
ax.set_title("Rearranging a conditionally convergent series changes its sum", fontsize=10)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
