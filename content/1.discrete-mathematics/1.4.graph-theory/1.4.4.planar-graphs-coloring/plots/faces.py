# Faces of the plane graph of Example 4.1.1 and their boundary lengths.
import wikigraph as G

TEX = {f"v{i}": f"$v_{i}$" for i in range(1, 6)}

pos = {"v1": (0, 0), "v2": (2.2, 0), "v3": (2.2, 2.2), "v4": (0, 2.2), "v5": (3.5, 3.0)}
edges = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v1"), ("v1", "v3"), ("v3", "v5")]
fig, ax = G.canvas(5.4, 3.4)
G.draw(ax, pos, edges, highlight={("v3", "v5"): G.RED}, vertex_labels=TEX)
ax.text(1.5, 0.65, "$f_1$", fontsize=13, color=G.BLUE, ha="center", va="center")
ax.text(0.7, 1.55, "$f_2$", fontsize=13, color=G.BLUE, ha="center", va="center")
ax.text(3.6, 1.0, "$f_0$ (outer face)", fontsize=12, color=G.BLUE, ha="left", va="center")
ax.text(3.6, 0.35, "boundary lengths 3, 3, 4 + 2 = 6", fontsize=10, ha="left")
ax.text(3.6, -0.2, "sum 12 = 2m (cut edge counted twice)", fontsize=10, ha="left")
