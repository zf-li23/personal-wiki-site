# A directed graph and its three arborescences rooted at v1 (Example 3.3.4)
import wikigraph as G

pos = {"v1": (1.0, 1.8), "v2": (0, 0), "v3": (2.0, 0)}
names = {v: f"$v_{v[1]}$" for v in pos}
arcs = [("v1", "v2"), ("v1", "v3"), ("v2", "v3"), ("v3", "v2")]
trees = [[("v1", "v2"), ("v1", "v3")], [("v1", "v2"), ("v2", "v3")], [("v1", "v3"), ("v3", "v2")]]
fig, axes = G.panels(4, 2.0, 1.8, titles=["directed graph G", "arborescence 1", "arborescence 2",
                                          "arborescence 3"])
G.draw(axes[0], pos, arcs, directed=True, vertex_labels=names, vertex_color={"v1": G.VIOLET})
for ax, t in zip(axes[1:], trees):
    G.draw(ax, pos, t, directed=True, highlight={e: G.BLUE for e in t}, vertex_labels=names,
           vertex_color={"v1": G.VIOLET})
