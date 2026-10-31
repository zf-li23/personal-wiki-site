# Optimality with several tasks: Pareto fronts in trait space (Shoval and colleagues 2012).
# A: two traits, two tasks whose performances decline with the Euclidean distance from an archetype
# (Gaussian performance functions of different widths). Of 3000 random phenotypes, those not dominated
# by any other (better in both tasks) lie on the segment between the archetypes. B: three tasks with
# three archetypes: the Pareto-optimal phenotypes (computed by exhaustive comparison) fill the triangle
# whose vertices are the archetypes, which is why trait data of related species often fall in triangles.
# C: in performance space the front of panel B is the boundary of what is achievable: a gain in one task
# costs another.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def pareto_mask(F):
    """True for rows of F (performances, larger is better) not dominated by any other row."""
    n = F.shape[0]
    keep = np.ones(n, bool)
    for i in range(n):
        if not keep[i]:
            continue
        dom = np.all(F >= F[i], axis=1) & np.any(F > F[i], axis=1)
        if dom.any():
            keep[i] = False
    return keep


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
X = rng.uniform(-1, 2, (3000, 2))
arch2 = np.array([[0, 0], [1.2, 0.8]])
F2 = np.stack([np.exp(-np.sum((X - a) ** 2, 1) / (2 * w**2)) for a, w in zip(arch2, (0.5, 0.9))], 1)
m2 = pareto_mask(F2)
ax = axs[0]
ax.scatter(*X[~m2].T, s=3, color=P.muted(), alpha=0.35, lw=0, label="dominated")
ax.scatter(*X[m2].T, s=10, color=charts.line("negative"), lw=0, label="Pareto optimal")
ax.plot(*arch2.T, "*", ms=14, color=charts.line("atp"), label="archetypes")
ax.set_aspect("equal")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "trait 1", "trait 2")
charts.title(ax, "A   Two tasks: a line")

arch3 = np.array([[0, 0], [1.5, 0.2], [0.6, 1.4]])
F3 = np.stack([np.exp(-np.sum((X - a) ** 2, 1) / (2 * 0.6**2)) for a in arch3], 1)
m3 = pareto_mask(F3)
ax = axs[1]
ax.scatter(*X[~m3].T, s=3, color=P.muted(), alpha=0.35, lw=0)
ax.scatter(*X[m3].T, s=8, color=charts.line("enzyme"), lw=0)
ax.fill(*arch3.T, facecolor="none", edgecolor=P.ink(), lw=0.8, ls="--")
ax.plot(*arch3.T, "*", ms=14, color=charts.line("atp"))
for a, lab in zip(arch3, ("task 1", "task 2", "task 3")):
    ax.text(a[0], a[1] - 0.18, lab, ha="center", fontsize=7.5, color=P.ink())
ax.set_aspect("equal")
charts.style_axes(ax, "trait 1", "trait 2")
charts.title(ax, "B   Three tasks: a triangle")

ax = axs[2]
ax.scatter(F3[~m3, 0], F3[~m3, 1], s=3, color=P.muted(), alpha=0.35, lw=0)
sc = ax.scatter(F3[m3, 0], F3[m3, 1], s=8, c=F3[m3, 2], cmap="viridis", lw=0)
cb = fig.colorbar(sc, ax=ax, fraction=0.05)
cb.set_label("performance in task 3", fontsize=7.5, color=P.ink())
cb.ax.tick_params(labelsize=7, colors=P.ink())
charts.style_axes(ax, "performance in task 1", "performance in task 2")
charts.title(ax, "C   The front in performance space")
fig.tight_layout()
