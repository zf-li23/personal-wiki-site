"""The sprinkler network before and after the intervention do(X3 = On)."""

import wikigraph as G

pos = {"X1": (1.0, 3.0), "X2": (2.0, 2.0), "X3": (0.0, 2.0), "X4": (1.0, 1.0), "X5": (1.0, 0.0)}
names = {v: f"$X_{v[1]}$" for v in pos}
notes = {"X1": ("season", (0.0, 0.42)), "X2": ("rain", (0.62, 0.0)), "X3": ("sprinkler", (0.0, -0.42)),
         "X4": ("wet", (0.55, 0.0)), "X5": ("slippery", (0.75, 0.0))}
arcs = [("X1", "X2"), ("X1", "X3"), ("X2", "X4"), ("X3", "X4"), ("X4", "X5")]
fig, axes = G.panels(2, 3.0, 3.4, titles=["causal Bayesian network", "after do($X_3$ = On)"])
G.draw(axes[0], pos, arcs, directed=True, vertex_labels=names, vertex_notes=notes)
cut = [a for a in arcs if a != ("X1", "X3")]
notes_do = dict(notes, X3=("sprinkler = On", (0.0, -0.42)))
G.draw(axes[1], pos, cut, directed=True, vertex_labels=names, vertex_notes=notes_do,
       vertex_color={"X3": G.BLUE})
