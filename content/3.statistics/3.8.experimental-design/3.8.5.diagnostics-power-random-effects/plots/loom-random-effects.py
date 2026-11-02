"""Fabric strength on four randomly chosen looms: within-loom and between-loom variation."""

import numpy as np
import matplotlib.pyplot as plt

y = np.array([[98, 97, 99, 96], [91, 90, 93, 92], [96, 95, 97, 95], [95, 96, 99, 98]], float)
a, n = y.shape
grand = y.mean()
ms_tr = n * ((y.mean(1) - grand) ** 2).sum() / (a - 1)
ms_e = ((y - y.mean(1, keepdims=True)) ** 2).sum() / (a * (n - 1))
s_tau = np.sqrt((ms_tr - ms_e) / n)
s_e = np.sqrt(ms_e)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
for i in range(a):
    jitter = np.linspace(-0.12, 0.12, n)
    ax.scatter(i + 1 + jitter, y[i], s=26, color="C0", zorder=3)
    ax.hlines(y[i].mean(), i + 0.7, i + 1.3, color="C0", lw=2)
    ax.annotate("", xy=(i + 1.38, y[i].mean() + s_e), xytext=(i + 1.38, y[i].mean() - s_e),
                arrowprops=dict(arrowstyle="<->", color="C2", lw=1.2))
ax.axhline(grand, color="C1", ls="--", lw=1.5, label=f"grand mean {grand:.2f}")
ax.axhspan(grand - s_tau, grand + s_tau, color="C1", alpha=0.12,
           label=f"grand mean +/- sigma_tau hat ({s_tau:.2f})")
ax.plot([], [], color="C2", lw=1.2, label=f"loom mean +/- sigma hat ({s_e:.2f})")
ax.set_xticks(range(1, a + 1))
ax.set_xticklabels([f"loom {i}" for i in range(1, a + 1)])
ax.set_ylabel("strength")
ax.set_title("Fiber strength: ICC = 0.79")
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
