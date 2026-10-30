import wikigraph as G

pos = {"v1": (0, 1.0), "v2": (1.8, 2.0), "v3": (1.8, 0), "v4": (3.6, 1.0)}
names = {v: f"$v_{v[1]}$" for v in pos}
edges = [("v1", "v2", "$e_1$"), ("v1", "v3", "$e_2$"), ("v2", "v3", "$e_3$"), ("v3", "v4", "$e_4$"),
         ("v4", "v2", "$e_5$")]
fig, axes = G.panels(2, 3.6, 2.0, titles=["directed graph D", "underlying graph, with degrees"])
G.draw(axes[0], pos, edges, directed=True, weights=True, vertex_labels=names, label_offset=0.22)
G.draw(axes[1], pos, [e[:2] for e in edges], vertex_labels=names)
deg = {"v1": 2, "v2": 3, "v3": 3, "v4": 2}
shift = {"v1": (0, -0.45), "v2": (0.6, 0.1), "v3": (0.6, -0.1), "v4": (0, -0.45)}
for v, d in deg.items():
    x, y = pos[v]
    dx, dy = shift[v]
    G.caption(axes[1], (x + dx, y + dy), f"$d={d}$", size=9)
