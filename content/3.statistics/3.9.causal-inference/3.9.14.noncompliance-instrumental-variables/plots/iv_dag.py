"""Causal graphs for unobserved confounding, an instrument, and a violated exclusion restriction."""

import wikigraph as G

pos = {"Z": (0.0, 0.8), "W": (1.6, 0.8), "Y": (3.2, 0.8), "U": (2.4, 2.1)}
fig, axes = G.panels(3, 3.2, 2.1, titles=[
    "Unobserved confounder U",
    "Randomized instrument Z",
    "Exclusion restriction violated",
])
grey = {"U": G.GREY}

G.draw(axes[0], {k: pos[k] for k in "WYU"}, [("W", "Y"), ("U", "W"), ("U", "Y")],
       directed=True, vertex_color=grey, dashed=[("U", "W"), ("U", "Y")])
G.draw(axes[1], pos, [("Z", "W"), ("W", "Y"), ("U", "W"), ("U", "Y")],
       directed=True, vertex_color=grey, dashed=[("U", "W"), ("U", "Y")],
       highlight={("Z", "W"): G.BLUE})
G.draw(axes[2], pos, [("Z", "W"), ("W", "Y"), ("U", "W"), ("U", "Y")],
       directed=True, vertex_color=grey, dashed=[("U", "W"), ("U", "Y")])
G.curve(axes[2], [pos["Z"], (1.6, 0.05), pos["Y"]], colour=G.RED, directed=True)
