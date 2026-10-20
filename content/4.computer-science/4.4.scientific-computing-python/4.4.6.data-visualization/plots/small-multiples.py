"""Eight expression time courses: one crowded panel versus small multiples (synthetic data)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

dark = sum(to_rgb(plt.rcParams["figure.facecolor"])) < 1.5
HIGHLIGHT = "#3987e5" if dark else "#2a78d6"
CONTEXT = "0.35" if dark else "0.82"

rng = np.random.default_rng(0)
t = np.linspace(0, 24, 25)
shapes = [
    np.sin(2 * np.pi * t / 24),                 # circadian
    np.sin(2 * np.pi * (t - 6) / 24),           # circadian, phase-shifted
    np.tanh((t - 8) / 3),                       # early induction
    np.tanh((t - 16) / 3),                      # late induction
    -np.tanh((t - 10) / 4),                     # repression
    np.exp(-((t - 6) ** 2) / 8) * 2 - 0.5,      # transient pulse
    np.zeros_like(t),                           # flat
    0.08 * (t - 12),                            # slow drift
]
genes = [f"gene {k + 1}" for k in range(len(shapes))]
y = np.array(shapes) + rng.normal(0, 0.15, (len(shapes), t.size))

fig = plt.figure(figsize=(11, 3.8), layout="constrained")
left, right = fig.subfigures(1, 2, width_ratios=[1, 2])

ax = left.subplots()
for k in range(len(genes)):
    ax.plot(t, y[k], linewidth=1.5, color=plt.get_cmap("tab10")(k), label=genes[k])
ax.legend(fontsize=7, ncols=2, loc="lower left")
ax.set_xlabel("Time (h)")
ax.set_ylabel("log expression (centred)")
ax.set_title("All genes in one panel", fontsize=10)

grid = right.subplots(2, 4, sharex=True, sharey=True)
for k, ax in enumerate(grid.flat):
    for j in range(len(genes)):
        if j != k:
            ax.plot(t, y[j], color=CONTEXT, linewidth=0.8)
    ax.plot(t, y[k], color=HIGHLIGHT, linewidth=2)
    ax.set_title(genes[k], fontsize=9)
    ax.set_xticks([0, 12, 24])
for ax in grid[1]:
    ax.set_xlabel("Time (h)")
right.suptitle("Small multiples: shared axes, one gene highlighted per panel", fontsize=10)
