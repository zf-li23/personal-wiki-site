# Vertex and edge connectivity of standard graphs
import wikigraph as G

fig, axes = G.panels(5, 2.4, 2.4, scale=0.75, titles=[r"$K_5$: $\kappa=\lambda=4$", r"tree: $\kappa=\lambda=1$", r"$C_6$: $\kappa=\lambda=2$", r"$K_{2,3}$: $\kappa=\lambda=2$", r"Petersen: $\kappa=\lambda=3$"])

c = (1.2, 1.2)
k5 = G.circle(range(1, 6), radius=1.1, center=c)
G.draw(axes[0], k5, [(i, j) for i in range(1, 6) for j in range(i + 1, 6)], labels=False)

tree = {1: (1.2, 2.3), 2: (0.4, 1.3), 3: (2.0, 1.3), 4: (0.0, 0.2), 5: (0.8, 0.2), 6: (2.0, 0.2)}
G.draw(axes[1], tree, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)], labels=False, highlight={2: G.RED, 1: G.RED, 3: G.RED})

c6 = G.circle(range(6), radius=1.1, center=c)
G.draw(axes[2], c6, [(i, (i + 1) % 6) for i in range(6)], labels=False)

k23 = {"u1": (0.6, 2.0), "u2": (1.8, 2.0), "w1": (0.0, 0.3), "w2": (1.2, 0.3), "w3": (2.4, 0.3)}
G.draw(axes[3], k23, [(u, w) for u in ("u1", "u2") for w in ("w1", "w2", "w3")], labels=False,
       vertex_color={"u1": G.BLUE, "u2": G.BLUE})

outer = G.circle(range(5), radius=1.15, center=c)
inner = G.circle(range(5, 10), radius=0.55, center=c)
pet = {**outer, **inner}
pet_edges = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
G.draw(axes[4], pet, pet_edges, labels=False, radius=0.15)
