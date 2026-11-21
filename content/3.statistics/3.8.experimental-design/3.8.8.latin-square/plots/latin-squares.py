"""A 4 x 4 Latin square, an orthogonal mate, and their superposition (a Graeco-Latin square)."""

import matplotlib.pyplot as plt

latin = ["ABCD", "BADC", "CDAB", "DCBA"]
greek = [[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1]]
gsym = [r"$\alpha$", r"$\beta$", r"$\gamma$", r"$\delta$"]
colors = ["C0", "C1", "C2", "C3"]

fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.8))
titles = ["Latin square (treatments)", "Orthogonal mate (Greek letters)",
          "Superposition: each pair once"]
for n, ax in enumerate(axes):
    for i in range(4):
        for k in range(4):
            x, y = k, 3 - i
            if n == 0:
                c = colors["ABCD".index(latin[i][k])]
                label = latin[i][k]
            elif n == 1:
                c = colors[greek[i][k]]
                label = gsym[greek[i][k]]
            else:
                c = None
                label = latin[i][k] + " " + gsym[greek[i][k]]
            if c is not None:
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=c, alpha=0.35, lw=0))
            ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=False, ec="black", lw=1))
            ax.text(x + 0.5, y + 0.5, label, ha="center", va="center", fontsize=13)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.set_xticks([0.5, 1.5, 2.5, 3.5])
    ax.set_xticklabels(["1", "2", "3", "4"])
    ax.set_yticks([3.5, 2.5, 1.5, 0.5])
    ax.set_yticklabels(["1", "2", "3", "4"])
    ax.set_xlabel("column")
    ax.set_ylabel("row")
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(titles[n], fontsize=10)
fig.tight_layout()
