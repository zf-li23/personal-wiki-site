"""Partition of the total deviation Y_i - Y_bar into Y_i - Y_hat_i and Y_hat_i - Y_bar (Toluca data)."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 30, 50, 90, 70, 60, 120, 80, 100, 50, 40, 70, 90, 20, 110, 100, 30, 50, 90, 110, 30, 90, 40, 80, 70], float)
y = np.array([399, 121, 221, 376, 361, 224, 546, 352, 353, 157, 160, 252, 389, 113, 435, 420, 212, 268, 377, 421, 273,
              468, 244, 342, 323], float)
sxx = np.sum((x - x.mean()) ** 2)
b1 = np.sum((x - x.mean()) * (y - y.mean())) / sxx
b0 = y.mean() - b1 * x.mean()
ybar = y.mean()
fitted = b0 + b1 * x
ssto = np.sum((y - ybar) ** 2)
sse = np.sum((y - fitted) ** 2)
ssr = np.sum((fitted - ybar) ** 2)

pick = [0, 1]   # the lots (80, 399) and (30, 121)
g = np.linspace(15, 125, 2)
titles = [f"(a) Y_i - Y_bar: SSTO = {ssto:.0f}", f"(b) Y_i - Y_hat_i: SSE = {sse:.0f}", f"(c) Y_hat_i - Y_bar: SSR = {ssr:.0f}"]
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
for k, ax in enumerate(axes):
    ax.plot(x, y, "o", color="C0", ms=4, alpha=0.35)
    ax.axhline(ybar, color="gray", lw=1, ls="--")
    if k > 0:
        ax.plot(g, b0 + b1 * g, color="black", lw=1.5)
    for i in pick:
        ax.plot(x[i], y[i], "o", color="C0", ms=7)
        if k == 0:
            ax.vlines(x[i], ybar, y[i], color="C3", lw=2.5)
        elif k == 1:
            ax.vlines(x[i], fitted[i], y[i], color="C1", lw=2.5)
            ax.plot(x[i], fitted[i], "s", color="black", ms=5)
        else:
            ax.vlines(x[i], ybar, fitted[i], color="C2", lw=2.5)
            ax.plot(x[i], fitted[i], "s", color="black", ms=5)
    ax.set_title(titles[k], fontsize=10)
    ax.set_xlabel("lot size")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("work hours")
axes[0].annotate("Y_bar", xy=(122, ybar), xytext=(100, ybar - 60), fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))
fig.tight_layout()
