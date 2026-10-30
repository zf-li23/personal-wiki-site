import wikigraph as G

pos = {"v": (1.5, 1.0), "a": (0, 2.0), "b": (0, 0), "c": (3.0, 2.0), "d": (3.0, 0), "e": (1.5, 2.4)}
arcs = [("a", "v"), ("b", "v"), ("v", "c"), ("v", "d"), ("e", "v"), ("v", "e"), ("a", "e")]
fig, ax = G.canvas(3.0, 2.4)
G.draw(ax, pos, arcs, directed=True,
       highlight={"c": G.BLUE, "d": G.BLUE, "a": G.RED, "b": G.RED, "e": G.VIOLET})
G.caption(ax, (3.0, 1.0), "out-neighbors", size=9)
G.caption(ax, (0.0, 1.0), "in-neighbors", size=9)
G.caption(ax, (0.55, 2.55), "both", size=9)
