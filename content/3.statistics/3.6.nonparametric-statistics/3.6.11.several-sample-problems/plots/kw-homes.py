"""Pooled ranks of home prices in three villages, with mean ranks and the Kruskal-Wallis statistic."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

groups = {"A": [139, 145, 171], "B": [151, 163, 188, 197], "C": [199, 250, 360]}
vals = np.concatenate([np.array(v, float) for v in groups.values()])
ranks = stats.rankdata(vals)
N = len(vals)
H, p = stats.kruskal(*groups.values())

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
start = 0
for i, (name, v) in enumerate(groups.items()):
    r = ranks[start:start + len(v)]
    axes[0].scatter(v, np.full(len(v), i), s=60, color=f"C{i}")
    axes[1].scatter(r, np.full(len(v), i), s=60, color=f"C{i}")
    axes[1].plot([r.mean()] * 2, [i - 0.3, i + 0.3], color=f"C{i}", lw=3)
    axes[1].text(r.mean(), i + 0.35, f"mean rank {r.mean():.2f}", ha="center", fontsize=9)
    start += len(v)
axes[1].axvline((N + 1) / 2, color="gray", ls=":", label="(N + 1) / 2 = 5.5")
for ax in axes:
    ax.set_yticks(range(3))
    ax.set_yticklabels([f"village {k}" for k in groups])
    ax.set_ylim(-0.6, 2.8)
    ax.grid(alpha=0.3, axis="x")
axes[0].set_xlabel("price (thousand pounds)")
axes[0].set_title("Raw prices")
axes[1].set_xlabel("pooled rank")
axes[1].set_title(f"Ranks: H = {H:.3f}, chi-squared p = {p:.3f}")
axes[1].legend(frameon=False, loc="lower right", fontsize=9)
fig.tight_layout()
