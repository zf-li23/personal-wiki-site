"""Running means for N(0,1) samples converge to 0; for standard Cauchy samples they do not."""

import numpy as np
import matplotlib.pyplot as plt

n_max, paths = 10000, 5
n = np.arange(1, n_max + 1)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
for ax, (name, sampler) in zip(axes, [
    ("N(0, 1)", np.random.standard_normal),
    ("standard Cauchy", np.random.standard_cauchy),
]):
    for _ in range(paths):
        ax.plot(n, np.cumsum(sampler(n_max)) / n, lw=0.9)
    ax.axhline(0, color="black", lw=1.0)
    ax.set_xscale("log")
    ax.set_ylim(-4, 4)
    ax.set_xlabel("n (log scale)")
    ax.set_title(f"running mean, {name} samples")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("sample mean")
fig.tight_layout()
