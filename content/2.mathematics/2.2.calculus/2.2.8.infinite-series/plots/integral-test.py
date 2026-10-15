"""Integral test: for decreasing f, the terms f(n) are rectangles squeezed
around the area under y = f(x), so S_n - u_1 <= int_1^n f <= S_{n-1}."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 3.9), sharey=True)
x = np.linspace(1, 9, 400)
for ax, p in zip(axes, [1.0, 2.0]):
    f = lambda t: t ** -p
    k = np.arange(1, 9)
    ax.bar(k, f(k), width=1, align="edge", color="C1", alpha=0.3, edgecolor="C1",
           label=r"$u_k$ on $[k, k+1]$: $\sum_{k=1}^{n} u_k \geq \int_1^{n+1} f$")
    ax.bar(k[:-1] + 1, f(k[:-1] + 1), width=-1, align="edge", color="C0", alpha=0.45,
           edgecolor="C0", label=r"$u_k$ on $[k-1, k]$: $\sum_{k=2}^{n} u_k \leq \int_1^{n} f$")
    ax.plot(x, f(x), color="black", linewidth=1.6, label=rf"$f(x) = x^{{-{p:g}}}$")
    verdict = "diverge" if p <= 1 else "converge"
    ax.set_title(rf"$p = {p:g}$: $\int_1^{{+\infty}} x^{{-p}}\,\mathrm{{d}}x$ and $\sum n^{{-p}}$ both {verdict}",
                 fontsize=10)
    ax.set_xlabel(r"$x$")
    ax.set_xlim(1, 9)
    ax.grid(True, alpha=0.3)
axes[0].legend(fontsize=8)
fig.tight_layout()
