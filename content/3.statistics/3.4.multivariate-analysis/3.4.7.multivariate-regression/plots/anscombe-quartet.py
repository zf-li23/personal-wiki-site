"""Anscombe's quartet (1973): the same least squares fit for four very different data sets."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], float)
data = [
    (x, np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])),
    (x, np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])),
    (x, np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])),
    (np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], float), np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])),
]
fig, axes = plt.subplots(2, 2, figsize=(9, 7), sharex=True, sharey=True)
grid = np.linspace(2, 20, 2)
for k, (ax, (xx, yy)) in enumerate(zip(axes.flat, data), start=1):
    b, a = np.polyfit(xx, yy, 1)
    r2 = np.corrcoef(xx, yy)[0, 1] ** 2
    ax.plot(xx, yy, "o", color="C0")
    ax.plot(grid, a + b * grid, color="C3", lw=1.5)
    ax.set_title(f"data set {k}:  y = {a:.2f} + {b:.3f} x,  R^2 = {r2:.2f}", fontsize=10)
    ax.grid(alpha=0.3)
for ax in axes[1]:
    ax.set_xlabel("x")
for ax in axes[:, 0]:
    ax.set_ylabel("y")
fig.tight_layout()
