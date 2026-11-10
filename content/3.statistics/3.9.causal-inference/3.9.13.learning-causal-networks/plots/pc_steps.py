"""The PC algorithm on five variables: true DAG, skeleton, v-structure, and the final CPDAG."""

import wikigraph as G

pos = {"1": (1.0, 3.0), "2": (0.0, 2.0), "3": (2.0, 2.0), "4": (1.0, 1.0), "5": (1.6, 0.0)}
names = {v: f"$X_{v}$" for v in pos}
dag = [("1", "2"), ("1", "3"), ("2", "4"), ("3", "4"), ("3", "5"), ("4", "5")]
titles = ["true DAG", "step 1: skeleton", "step 2: v-structure", "step 3: Meek rules (CPDAG)"]
fig, axes = G.panels(4, 2.0, 3.0, titles=titles)

G.draw(axes[0], pos, dag, directed=True, vertex_labels=names)
G.draw(axes[1], pos, dag, vertex_labels=names)

undirected = [("1", "2"), ("1", "3"), ("3", "5"), ("4", "5")]
G.draw(axes[2], pos, undirected, vertices=False)
G.draw(axes[2], pos, [("2", "4"), ("3", "4")], directed=True, vertex_labels=names,
       highlight={("2", "4"): G.RED, ("3", "4"): G.RED})

G.draw(axes[3], pos, [("1", "2"), ("1", "3")], vertices=False)
G.draw(axes[3], pos, [("2", "4"), ("3", "4"), ("4", "5"), ("3", "5")], directed=True, vertex_labels=names,
       highlight={("4", "5"): G.BLUE, ("3", "5"): G.BLUE})
