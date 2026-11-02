"""Twin data analysed as two independent groups and as pairs."""

import numpy as np
import matplotlib.pyplot as plt

drug1 = np.array([3, 3, 4, 8, 3, 2, 9, 5, 4, 7])
drug2 = np.array([3, 5, 3, 8, 2, 4, 9, 4, 5, 6])
n = len(drug1)
rng = np.random.default_rng(0)

fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2), sharey=True)
ax = axes[0]
for k, (y, c) in enumerate([(drug1, "C0"), (drug2, "C1")]):
    x = k + rng.uniform(-0.08, 0.08, n)
    ax.scatter(x, y, s=40, color=c, zorder=3)
    ax.hlines(y.mean(), k - 0.25, k + 0.25, color=c, lw=2)
ax.set_xticks([0, 1], ["drug 1", "drug 2"])
ax.set_xlim(-0.6, 1.6)
ax.set_ylabel("response")
ax.set_title("Unpaired view: s_p = 2.32, t = -0.10 (df 18)", fontsize=10)
ax.grid(alpha=0.3)

ax = axes[1]
for j in range(n):
    ax.plot([0, 1], [drug1[j], drug2[j]], color="gray", lw=1, zorder=1)
    ax.text(-0.07, drug1[j], str(j + 1), ha="right", va="center", fontsize=7)
ax.scatter(np.zeros(n), drug1, s=40, color="C0", zorder=3)
ax.scatter(np.ones(n), drug2, s=40, color="C1", zorder=3)
ax.set_xticks([0, 1], ["drug 1", "drug 2"])
ax.set_xlim(-0.6, 1.6)
ax.set_title("Paired view: s_d = 1.20, t = -0.26 (df 9)", fontsize=10)
ax.grid(alpha=0.3)
fig.tight_layout()
