"""Theil-Sen and least squares lines for 30 points from y = 2 + 0.8 x + N(0, 1),
of which the 3 with the largest x are replaced by gross errors."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
n = 30
x = np.sort(rng.uniform(0, 10, n))
y = 2 + 0.8 * x + rng.normal(0, 1, n)
y_bad = y.copy()
y_bad[-3:] = rng.normal(0.5, 0.5, 3)          # contamination at high x


def theil_sen(x, y):
    i, j = np.triu_indices(len(x), k=1)
    keep = x[j] != x[i]
    slope = np.median((y[j] - y[i])[keep] / (x[j] - x[i])[keep])
    return np.median(y - slope * x), slope


xx = np.array([0, 10])
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0), sharey=True)
for ax, data, title in [(axes[0], y, "A. clean data"), (axes[1], y_bad, "B. 3 of 30 points replaced")]:
    b1, b0 = np.polyfit(x, data, 1)
    a, b = theil_sen(x, data)
    ax.plot(x, data, "o", color="0.45", ms=4)
    if data is y_bad:
        ax.plot(x[-3:], data[-3:], "o", color="C3", ms=5, label="gross errors")
    ax.plot(xx, 2 + 0.8 * xx, color="0.2", ls=":", lw=1.2, label="true line")
    ax.plot(xx, b0 + b1 * xx, color="C0", lw=1.8, label=f"least squares, slope {b1:.2f}")
    ax.plot(xx, a + b * xx, color="C1", lw=1.8, label=f"Theil-Sen, slope {b:.2f}")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("x")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper left")
axes[0].set_ylabel("y")
fig.tight_layout()
