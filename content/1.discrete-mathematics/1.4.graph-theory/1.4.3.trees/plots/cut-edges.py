# Cut edges (red) are exactly the edges that lie on no cycle (Theorem 3.1.1)
import wikigraph as G

pos = {"a": (0, 0.2), "b": (0, 1.8), "c": (1.2, 1.0), "d": (2.6, 1.0), "e": (3.6, 1.9), "f": (3.6, 0.1),
       "g": (4.9, 0.1), "h": (4.9, 1.9)}
edges = [("a", "b"), ("b", "c"), ("c", "a"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "d"), ("f", "g"),
         ("e", "h")]
bridges = [("c", "d"), ("f", "g"), ("e", "h")]
fig, ax = G.canvas(4.9, 1.9)
G.draw(ax, pos, edges, highlight={e: G.RED for e in bridges})
G.caption(ax, (0.4, -0.35), "cycle abc")
G.caption(ax, (3.3, -0.35), "cycle def")
