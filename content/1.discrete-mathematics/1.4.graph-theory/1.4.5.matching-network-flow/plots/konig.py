# Konig's theorem on Example 5.1.1: the biadjacency matrix, a maximum matching (circled entries,
# four of them in distinct rows and columns) and a minimum cover (row x3, columns y1, y2, y3).
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import wikigraph as G

X = [f"x{i}" for i in range(1, 6)]
Y = [f"y{i}" for i in range(1, 6)]
ADJ = {"x1": ["y1", "y2"], "x2": ["y1"], "x3": ["y2", "y3", "y4", "y5"], "x4": ["y3"], "x5": ["y1"]}
matching = {("x1", "y2"), ("x2", "y1"), ("x3", "y4"), ("x4", "y3")}
rows, cols = {"x3"}, {"y1", "y2", "y3"}

fig, ax = plt.subplots(figsize=(3.6, 3.4))
ax.set_xlim(-0.8, 5.2)
ax.set_ylim(-0.2, 5.8)
ax.set_aspect("equal")
ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1)
for i, x in enumerate(X):
    r = 4 - i  # row x1 at the top
    ax.text(-0.4, r + 0.5, f"${x[0]}_{x[1]}$", ha="center", va="center", fontsize=G.FONT)
    if x in rows:
        ax.add_patch(Rectangle((0, r), 5, 1, facecolor=G.AMBER, alpha=0.3, lw=0))
    for j, y in enumerate(Y):
        if i == 0:
            ax.text(j + 0.5, 5.4, f"${y[0]}_{y[1]}$", ha="center", va="center", fontsize=G.FONT)
            if y in cols:
                ax.add_patch(Rectangle((j, 0), 1, 5, facecolor=G.AMBER, alpha=0.3, lw=0))
        ax.add_patch(Rectangle((j, r), 1, 1, fill=False, edgecolor=G.GREY, lw=0.6))
        ax.text(j + 0.5, r + 0.5, "1" if y in ADJ[x] else "0", ha="center", va="center",
                fontsize=G.FONT, color=G.INK if y in ADJ[x] else G.GREY)
        if (x, y) in matching:
            ax.add_patch(Circle((j + 0.5, r + 0.5), 0.33, fill=False, edgecolor=G.BLUE, lw=1.8))
