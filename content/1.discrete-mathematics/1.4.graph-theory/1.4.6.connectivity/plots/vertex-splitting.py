# From vertex-disjoint paths to unit flows: every inner vertex v becomes an arc v_in -> v_out of capacity 1
import wikigraph as G

und = {"x": (0, 1), "u": (1.4, 2), "v": (1.4, 0), "y": (2.8, 1)}
fig, (ax1, ax2) = G.panels(2, 5.6, 2.0, titles=["undirected graph", r"network: arcs $v_{in} \to v_{out}$ have capacity 1, all others $\infty$"])
G.draw(ax1, {k: (x + 1.4, y) for k, (x, y) in und.items()}, [("x", "u"), ("x", "v"), ("u", "v"), ("u", "y"), ("v", "y")])

pos = {"x": (0, 1), "ui": (1.6, 2), "uo": (3.0, 2), "vi": (1.6, 0), "vo": (3.0, 0), "y": (4.6, 1)}
names = {"x": "x", "y": "y", "ui": "$u_{in}$", "uo": "$u_{out}$", "vi": "$v_{in}$", "vo": "$v_{out}$"}
arcs = [("x", "ui"), ("x", "vi"), ("ui", "uo", 1), ("vi", "vo", 1),
        ("uo", "vi"), ("vo", "ui"), ("uo", "y"), ("vo", "y")]
G.draw(ax2, pos, arcs, directed=True, weights=True, vertex_labels=names, radius=0.34,
       highlight={("ui", "uo"): G.RED, ("vi", "vo"): G.RED})
