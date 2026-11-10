"""The same 40 observations in four histograms: two bin widths and two bin origins."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([6.1, 4.7, 4.1, 4.6, 6.0, 5.5, 4.6, 5.8, 5.6, 5.0,
              5.9, 4.9, 3.9, 4.9, 4.0, 3.1, 4.9, 6.1, 3.1, 4.3,
              4.9, 6.0, 1.4, 3.9, 6.1, 5.3, 2.7, 6.9, 5.2, 3.8,
              8.2, 8.5, 8.1, 4.9, 8.4, 8.4, 7.3, 3.4, 10.7, 4.7])

settings = [(2.0, 0.0), (2.0, 1.0), (0.5, 0.0), (0.5, 0.25)]
fig, axes = plt.subplots(2, 2, figsize=(9.0, 5.6), sharex=True)
for ax, (width, origin) in zip(axes.ravel(), settings):
    edges = np.arange(origin - width, 12 + width, width)
    ax.hist(x, bins=edges, density=True, color="C0", alpha=0.6, edgecolor="C0")
    ax.plot(x, np.full_like(x, -0.01), "|", color="0.3", ms=8)
    ax.set_title(f"bin width {width:g}, origin {origin:g}", fontsize=10)
    ax.set_xlim(0, 12)
    ax.grid(alpha=0.3)
for ax in axes[1]:
    ax.set_xlabel("x")
for ax in axes[:, 0]:
    ax.set_ylabel("density")
fig.tight_layout()
