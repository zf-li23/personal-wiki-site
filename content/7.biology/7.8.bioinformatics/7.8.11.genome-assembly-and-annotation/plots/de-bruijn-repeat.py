# Abstract de Bruijn graphs: a unique stretch is a chain, a repeated (k-1)-mer joins two chains.
import wikigraph as G

fig, (a, b) = G.panels(2, 6.0, 2.4, titles=["A  unique sequence", "B  a repeated (k-1)-mer"])

chain = {f"v{i}": (1.0 * i - 0.5, 1.2) for i in range(1, 7)}
G.draw(a, chain, [(f"v{i}", f"v{i+1}") for i in range(1, 6)], directed=True,
       highlight={(f"v{i}", f"v{i+1}"): G.BLUE for i in range(1, 6)})
G.caption(a, (3.0, 0.3), "every vertex: in-degree 1, out-degree 1")

pos = {"a": (0.4, 2.1), "b": (0.4, 0.3), "x": (1.7, 2.1), "y": (1.7, 0.3), "R": (3.0, 1.2),
       "u": (4.3, 2.1), "w": (4.3, 0.3), "c": (5.6, 2.1), "d": (5.6, 0.3)}
edges = [("a", "x"), ("x", "R"), ("b", "y"), ("y", "R"), ("R", "u"), ("u", "c"), ("R", "w"), ("w", "d")]
G.draw(b, pos, edges, directed=True,
       highlight={("a", "x"): G.BLUE, ("x", "R"): G.BLUE, ("b", "y"): G.GREEN, ("y", "R"): G.GREEN,
                  ("R", "u"): G.AMBER, ("u", "c"): G.AMBER, ("R", "w"): G.VIOLET, ("w", "d"): G.VIOLET},
       vertex_color={"R": G.RED})
G.caption(b, (3.0, -0.3), "R: in-degree 2, out-degree 2")
