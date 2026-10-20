"""Three samples with the same mean and SD: a bar chart of means hides what the points show."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

dark = sum(to_rgb(plt.rcParams["figure.facecolor"])) < 1.5
COLORS = ["#3987e5", "#d95926", "#199e70"] if dark else ["#2a78d6", "#eb6834", "#1baf7a"]

rng = np.random.default_rng(0)
n = 30
raw = [
    rng.normal(0, 1, n),                                   # unimodal
    np.r_[rng.normal(-1, 0.25, n // 2), rng.normal(1, 0.25, n - n // 2)],  # two subpopulations
    np.r_[rng.normal(0, 0.3, n - 2), [3.5, 4.5]],          # two outliers
]
# Standardize every sample to mean 5 and SD 1.
groups = [5 + (x - x.mean()) / x.std(ddof=1) for x in raw]
labels = ["A", "B", "C"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.4), sharey=True, layout="constrained")

means = [g.mean() for g in groups]
sems = [g.std(ddof=1) / np.sqrt(n) for g in groups]
ax1.bar(range(3), means, yerr=sems, color=COLORS, width=0.6, capsize=6)
ax1.set_title("Bar of means $\\pm$ SEM", fontsize=10)
ax1.set_ylabel("Expression (a.u.)")

ax2.boxplot(groups, positions=range(3), widths=0.5, showfliers=False)
for i, (g, c) in enumerate(zip(groups, COLORS)):
    ax2.scatter(i + rng.uniform(-0.15, 0.15, g.size), g, color=c, s=14, alpha=0.8, zorder=3)
ax2.set_title("Every observation, with a box plot", fontsize=10)

for ax in (ax1, ax2):
    ax.set_xticks(range(3), labels)
    ax.set_xlabel("Cell population")
    ax.spines[["top", "right"]].set_visible(False)
ax1.set_ylim(0, 10)
