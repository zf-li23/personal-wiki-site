import wikigraph as G

pos = {"a": (0, 2.0), "b": (2.4, 2.0), "c": (2.4, 0), "d": (0, 0)}
E = [("a", "b", 1), ("b", "c", 3), ("c", "d", 3), ("d", "a", 2), ("b", "d", 5)]
fig, axes = G.panels(2, 2.4, 2.0, margin=0.6,
                     titles=["odd vertices b and d", "duplicate the shortest b-d path b a d"])
G.draw(axes[0], pos, E, weights=True, highlight={"b": G.RED, "d": G.RED})
dup = [("a", "b", 1), ("d", "a", 2)]
G.draw(axes[1], pos, E + dup, weights=True, highlight={("a", "b"): G.RED, ("d", "a"): G.RED})
