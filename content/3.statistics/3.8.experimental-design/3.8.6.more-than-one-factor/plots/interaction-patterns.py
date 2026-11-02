"""Four schematic interaction plots for a 2 x 2 factorial."""

import matplotlib.pyplot as plt

x = [1, 2]
cases = [
    ("No interaction: parallel lines", [10, 20], [16, 26]),
    ("Interaction, same direction", [10, 14], [16, 30]),
    ("Interaction, crossing lines", [10, 22], [20, 12]),
    ("Interaction only, no main effects", [10, 20], [20, 10]),
]
fig, axes = plt.subplots(1, 4, figsize=(14, 3.6), sharey=True)
for ax, (title, b1, b2) in zip(axes, cases):
    ax.plot(x, b1, "o-", lw=1.8, label="B = low")
    ax.plot(x, b2, "s--", lw=1.8, label="B = high")
    ax.set_xticks(x)
    ax.set_xticklabels(["A low", "A high"])
    ax.set_xlim(0.7, 2.3)
    ax.set_ylim(5, 34)
    ax.set_title(title, fontsize=10)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("mean response")
axes[0].legend(loc="upper left", fontsize=8)
fig.tight_layout()
