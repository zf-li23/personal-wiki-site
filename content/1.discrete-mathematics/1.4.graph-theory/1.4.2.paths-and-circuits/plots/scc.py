import wikigraph as G

pos = {"a": (0, 1.6), "b": (1.3, 1.6), "c": (0.65, 0.4), "d": (2.9, 1.6), "e": (4.2, 1.6), "f": (3.55, 0.4),
       "g": (2.0, -0.8), "h": (3.4, -0.8)}
arcs = [("a", "b"), ("b", "c"), ("c", "a"), ("b", "d"), ("d", "e"), ("e", "f"), ("f", "d"), ("c", "g"),
        ("g", "h"), ("h", "g"), ("f", "h")]
comp = {"a": 0, "b": 0, "c": 0, "d": 1, "e": 1, "f": 1, "g": 2, "h": 2}
colours = [G.BLUE, G.RED, G.GREEN]
hl = {v: colours[k] for v, k in comp.items()}
hl.update({(u, v): colours[comp[u]] for u, v in arcs if comp[u] == comp[v]})
fig, axes = G.panels(2, 4.2, 2.4, titles=["strongly connected components", "condensation (a DAG)"])
for ax in axes:
    ax.set_ylim(-1.2, 2.1)
G.draw(axes[0], pos, arcs, directed=True, highlight=hl)
cpos = {"C1": (0.6, 1.4), "C2": (3.6, 1.4), "C3": (2.1, -0.6)}
G.draw(axes[1], cpos, [("C1", "C2"), ("C1", "C3"), ("C2", "C3")], directed=True, radius=0.34,
       vertex_color={"C1": G.BLUE, "C2": G.RED, "C3": G.GREEN},
       vertex_labels={"C1": "abc", "C2": "def", "C3": "gh"})
