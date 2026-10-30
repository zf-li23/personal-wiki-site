# The graph K4 - e (top left) and its eight spanning trees
from itertools import combinations

import matplotlib.pyplot as plt
import wikigraph as G

pos = {"v1": (1, 2), "v2": (0, 1), "v3": (1, 0), "v4": (2, 1)}
names = {v: f"$v_{v[1]}$" for v in pos}
edges = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v1"), ("v1", "v3")]
triangles = [{("v1", "v2"), ("v2", "v3"), ("v1", "v3")}, {("v1", "v3"), ("v3", "v4"), ("v4", "v1")}]
trees = [t for t in combinations(edges, 3) if set(t) not in triangles]

fig, axes = plt.subplots(3, 3, figsize=(6.3, 6.6))
for ax in axes.flat:
    ax.set_xlim(-0.4, 2.4)
    ax.set_ylim(-0.4, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
G.draw(axes[0, 0], pos, edges, vertex_labels=names)
axes[0, 0].set_title("G = K4 - e", fontsize=G.FONT)
for k, (ax, t) in enumerate(zip(axes.flat[1:], trees), start=1):
    G.draw(ax, pos, edges, highlight={e: G.BLUE for e in t}, dashed=[e for e in edges if e not in t],
           edge_color=G.GREY, vertex_labels=names)
    ax.set_title(f"tree {k}", fontsize=G.FONT)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.95, wspace=0.05, hspace=0.15)
