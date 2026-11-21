"""Dairy cow crossover experiment: milk yield of each cow over the three periods, labelled by diet."""

import matplotlib.pyplot as plt

# (diet, period, cow, yield); cows 1-3 form square 1 and cows 4-6 square 2
rows = [("A", 1, 1, 38), ("B", 1, 2, 109), ("C", 1, 3, 124), ("A", 1, 4, 86), ("B", 1, 5, 75),
        ("C", 1, 6, 101), ("B", 2, 1, 25), ("C", 2, 2, 86), ("A", 2, 3, 72), ("C", 2, 4, 76),
        ("A", 2, 5, 35), ("B", 2, 6, 63), ("C", 3, 1, 15), ("A", 3, 2, 39), ("B", 3, 3, 27),
        ("B", 3, 4, 46), ("C", 3, 5, 34), ("A", 3, 6, 1)]
markers = {"A": "o", "B": "s", "C": "^"}
colors = {"A": "C0", "B": "C1", "C": "C2"}

fig, axes = plt.subplots(1, 2, figsize=(9.5, 4), sharey=True)
for sq, ax in zip([1, 2], axes):
    cows = [1, 2, 3] if sq == 1 else [4, 5, 6]
    for cow in cows:
        pts = sorted((p, y, d) for d, p, c, y in rows if c == cow)
        ax.plot([p for p, _, _ in pts], [y for _, y, _ in pts], color="gray", lw=1, alpha=0.6)
        ax.annotate(f"cow {cow}", (1, pts[0][1]), xytext=(-8, 0), textcoords="offset points",
                    ha="right", va="center", fontsize=8)
        for p, y, d in pts:
            ax.scatter(p, y, marker=markers[d], color=colors[d], s=55, zorder=3)
    ax.set_xticks([1, 2, 3])
    ax.set_xlim(0.4, 3.3)
    ax.set_xlabel("period")
    ax.set_title(f"square {sq}")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("milk yield")
for d in "ABC":
    axes[1].scatter([], [], marker=markers[d], color=colors[d], label=f"diet {d}")
axes[1].legend(loc="upper right")
fig.tight_layout()
