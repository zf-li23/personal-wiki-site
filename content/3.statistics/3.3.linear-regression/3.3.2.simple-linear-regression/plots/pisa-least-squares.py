"""Least squares fit to the Leaning Tower of Pisa data, with the residuals drawn as vertical segments."""

import numpy as np
import matplotlib.pyplot as plt

year = np.arange(75, 88, dtype=float)
lean = np.array([642, 644, 656, 667, 673, 688, 696, 698, 713, 717, 725, 742, 757], dtype=float)

sxx = np.sum((year - year.mean()) ** 2)
b1 = np.sum((year - year.mean()) * (lean - lean.mean())) / sxx
b0 = lean.mean() - b1 * year.mean()
fitted = b0 + b1 * year
sse = np.sum((lean - fitted) ** 2)

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.vlines(year, fitted, lean, color="C1", lw=1.5, label="residuals e_i = Y_i - Y_hat_i")
ax.plot(year, lean, "o", color="C0", ms=6, label="observed lean", zorder=3)
grid = np.linspace(74.5, 87.5, 2)
ax.plot(grid, b0 + b1 * grid, color="C3", lw=2, label=f"Y_hat = {b0:.2f} + {b1:.4f} X")
k = 7
ax.annotate(f"e_82 = {lean[k] - fitted[k]:.1f}", xy=(year[k], (lean[k] + fitted[k]) / 2), xytext=(year[k] + 0.6, lean[k] - 22),
            arrowprops=dict(arrowstyle="->", lw=1), fontsize=9)
ax.set_xlabel("year (19xx)")
ax.set_ylabel("lean (0.1 mm above 2.9 m)")
ax.set_title(f"Leaning Tower of Pisa: SSE = {sse:.1f}, MSE = {sse / 11:.2f}", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
