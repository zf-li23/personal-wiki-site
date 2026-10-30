import wikigraph as G

titles = ["undirected graph", "directed graph", "mixed graph", "multigraph with a loop"]
fig, axes = G.panels(4, 2.4, 2.6, titles=titles)
pos = {"a": (0, 0), "b": (2.4, 0), "c": (2.4, 1.9), "d": (0, 1.9)}
G.draw(axes[0], pos, [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")])
G.draw(axes[1], pos, [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c")], directed=True)
# a mixed graph: two undirected edges drawn on their own, directed arcs on top
G.draw(axes[2], pos, [("a", "b"), ("c", "d")])
G.draw(axes[2], pos, [("b", "c"), ("d", "a"), ("a", "c")], directed=True)
G.draw(axes[3], pos, [("a", "b"), ("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("d", "a"), ("d", "a"),
                      ("c", "c")], highlight={("c", "c"): G.RED, ("d", "a"): G.BLUE})
