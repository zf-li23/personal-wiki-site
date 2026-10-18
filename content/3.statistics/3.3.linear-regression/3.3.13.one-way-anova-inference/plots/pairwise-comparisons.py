"""Simultaneous 95% intervals for pairwise differences of the cereal means by four methods."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats

data = [[11, 17, 16, 14, 15], [12, 10, 15, 19, 11], [23, 20, 18, 17], [27, 33, 22, 26, 28]]
data = [np.array(v, float) for v in data]
r = len(data)
n = np.array([len(v) for v in data])
means = np.array([v.mean() for v in data])
nT = n.sum()
df = nT - r
s = np.sqrt(sum(((v - v.mean()) ** 2).sum() for v in data) / df)
pairs = list(itertools.combinations(range(r), 2))
g = len(pairs)
alpha = 0.05
methods = {
    "LSD": stats.t.ppf(1 - alpha / 2, df),
    "Bonferroni": stats.t.ppf(1 - alpha / (2 * g), df),
    "Tukey": stats.studentized_range.ppf(1 - alpha, r, df) / np.sqrt(2),
    "Scheffe": np.sqrt((r - 1) * stats.f.ppf(1 - alpha, r - 1, df)),
}

fig, ax = plt.subplots(figsize=(9, 5.6))
offsets = np.linspace(-0.3, 0.3, len(methods))
for m, ((name, tc), off) in enumerate(zip(methods.items(), offsets)):
    for k, (i, j) in enumerate(pairs):
        d = means[j] - means[i]
        h = tc * s * np.sqrt(1 / n[i] + 1 / n[j])
        y = k + off
        sig = abs(d) > h
        ax.plot([d - h, d + h], [y, y], color=f"C{m}", lw=2.0, ls="-" if sig else ":")
        ax.plot(d, y, "o", color=f"C{m}", ms=4)
ax.axvline(0, color="gray", lw=1)
ax.set_yticks(range(g))
ax.set_yticklabels([f"mu{j + 1} - mu{i + 1}" for i, j in pairs])
ax.invert_yaxis()
ax.set_xlabel("difference of means (cases sold)")
ax.set_title("Pairwise comparisons: solid = excludes 0, dotted = includes 0")
handles = [Line2D([0], [0], color=f"C{m}", lw=2.0) for m in range(len(methods))]
labels = [f"{name} (t_c = {tc:.2f})" for name, tc in methods.items()]
ax.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=4, frameon=False)
ax.grid(alpha=0.3, axis="x")
fig.tight_layout()
