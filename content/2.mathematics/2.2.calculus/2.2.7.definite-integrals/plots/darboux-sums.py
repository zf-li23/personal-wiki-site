"""Lower and upper Darboux sums of f(x) = x^2 on [0, 1] for uniform partitions.
The gap between them is the sum of oscillation times width, which tends to 0."""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2
xs = np.linspace(0, 1, 400)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
for ax, n in zip(axes, [4, 8, 16]):
    edges = np.linspace(0, 1, n + 1)
    left, right = edges[:-1], edges[1:]
    lower, upper = f(left), f(right)  # f is increasing on [0, 1]
    ax.bar(left, upper, width=1 / n, align="edge", color="C1", alpha=0.35,
           edgecolor="C1", linewidth=0.8, label="upper sum")
    ax.bar(left, lower, width=1 / n, align="edge", color="C0", alpha=0.55,
           edgecolor="C0", linewidth=0.8, label="lower sum")
    ax.plot(xs, f(xs), color="black", linewidth=1.6)
    s, S = np.sum(lower) / n, np.sum(upper) / n
    ax.set_title(rf"$n = {n}$:  $s = {s:.4f}$,  $S = {S:.4f}$", fontsize=10)
    ax.set_xlabel(r"$x$")
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)
axes[0].set_ylabel(r"$y = x^2$")
axes[0].legend(loc="upper left", fontsize=8)
fig.suptitle(r"Darboux sums of $x^2$ on $[0,1]$: $S - s = 1/n \to 0$, both tend to $1/3$")
fig.tight_layout()
