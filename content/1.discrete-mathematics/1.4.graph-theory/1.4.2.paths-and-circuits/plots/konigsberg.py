import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import wikigraph as G

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9.0, 3.4))
# schematic map: river (blue band), the island A, land masses B (north), C (south), D (east)
ax0.set_xlim(0, 6)
ax0.set_ylim(0, 4)
ax0.set_aspect("equal")
ax0.axis("off")
ax0.add_patch(Rectangle((0, 1.4), 4.2, 1.2, color=G.BLUE, alpha=0.25, lw=0))
ax0.add_patch(Rectangle((4.2, 0.3), 0.8, 3.4, color=G.BLUE, alpha=0.25, lw=0))
ax0.add_patch(Ellipse((2.0, 2.0), 1.8, 0.8, facecolor="white", edgecolor=G.INK, lw=1))
for (x, y), name in [((2.0, 2.0), "A"), ((2.0, 3.3), "B"), ((2.0, 0.7), "C"), ((5.5, 2.0), "D")]:
    ax0.text(x, y, name, ha="center", va="center", fontsize=12)
bridges = [(1.4, 2.35, 1.4, 2.65), (2.6, 2.35, 2.6, 2.65), (1.4, 1.65, 1.4, 1.35), (2.6, 1.65, 2.6, 1.35),
           (2.9, 2.0, 4.25, 2.0), (4.1, 3.1, 5.1, 3.1), (4.1, 0.9, 5.1, 0.9)]
for x0, y0, x1, y1 in bridges:
    ax0.plot([x0, x1], [y0, y1], color=G.AMBER, lw=5, solid_capstyle="butt")
ax0.set_title("seven bridges (schematic)", fontsize=10)

ax1.set_xlim(-0.6, 3.6)
ax1.set_ylim(-0.6, 3.0)
ax1.set_aspect("equal")
ax1.axis("off")
pos = {"A": (1.0, 1.2), "B": (1.0, 2.6), "C": (1.0, -0.2), "D": (3.2, 1.2)}
edges = [("A", "B"), ("A", "B"), ("A", "C"), ("A", "C"), ("A", "D"), ("B", "D"), ("C", "D")]
G.draw(ax1, pos, edges, highlight={v: G.RED for v in pos})
for v, d in {"A": 5, "B": 3, "C": 3, "D": 3}.items():
    x, y = pos[v]
    G.caption(ax1, (x + 0.15, y - 0.45) if v == "D" else (x - 0.65, y), f"$d={d}$", size=9)
ax1.set_title("the multigraph: four odd vertices", fontsize=10)
fig.tight_layout()
