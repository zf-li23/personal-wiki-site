"""Chain, fork and collider: which paths are open with and without conditioning on the middle node."""

import wikigraph as G

pos = {"X": (0.0, 0.0), "Y": (1.2, 0.0), "Z": (2.4, 0.0)}
names = {v: f"${v}$" for v in pos}
structures = [
    ("chain", [("X", "Y"), ("Y", "Z")]),
    ("fork", [("Y", "X"), ("Y", "Z")]),
    ("collider", [("X", "Y"), ("Z", "Y")]),
]
open_marginal = {"chain": True, "fork": True, "collider": False}
titles = [f"{name}: {'open' if open_marginal[name] else 'blocked'}" for name, _ in structures]
titles += [f"{name} given $Y$: {'blocked' if open_marginal[name] else 'open'}" for name, _ in structures]
fig, axes = G.grid(2, 3, 2.4, 0.5, titles=titles)
for row in range(2):
    for col, (name, edges) in enumerate(structures):
        ax = axes[3 * row + col]
        is_open = open_marginal[name] != (row == 1)
        colour = G.RED if is_open else G.GREY
        G.draw(ax, pos, edges, directed=True, vertex_labels=names, edge_color=colour,
               vertex_color={"Y": G.GREY} if row == 1 else None)
