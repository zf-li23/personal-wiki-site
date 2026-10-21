"""Gantt charts of a small batch queue on 8 cores, without and with backfill."""

import matplotlib.pyplot as plt

# job: (first core, number of cores, start hour, end hour) under each policy
schedules = {
    "Priority order only": {
        "A": (0, 6, 0, 4), "B": (0, 8, 4, 6), "C": (6, 2, 6, 9), "D": (0, 2, 6, 12),
    },
    "With backfill": {
        "A": (0, 6, 0, 4), "C": (6, 2, 0, 3), "B": (0, 8, 4, 6), "D": (0, 2, 6, 12),
    },
}
colors = {"A": "C7", "B": "C0", "C": "C2", "D": "C1"}

fig, axes = plt.subplots(2, 1, figsize=(7.5, 4.8), sharex=True)
for ax, (title, jobs) in zip(axes, schedules.items()):
    for name, (core, ncores, start, end) in jobs.items():
        ax.broken_barh([(start, end - start)], (core, ncores),
                       facecolors=colors[name], edgecolor="black", linewidth=0.8, alpha=0.85)
        ax.text((start + end) / 2, core + ncores / 2, name, ha="center", va="center",
                fontsize=11, fontweight="bold", color="white")
    ax.axvline(4, color="0.5", ls="--", lw=0.8)
    ax.set_ylim(0, 8)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_ylabel("cores")
    ax.set_title(title, fontsize=11)
    ax.grid(True, axis="x", alpha=0.3)
axes[-1].set_xlim(0, 12.5)
axes[-1].set_xticks(range(0, 13, 2))
axes[-1].set_xlabel("time (hours)")
fig.tight_layout()
