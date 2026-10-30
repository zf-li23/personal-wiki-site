# Menger's theorem: three internally disjoint x-y paths and a vertex cut of size three
import wikigraph as G

pos = {"x": (0, 1.2), "a": (1.3, 2.4), "b": (1.3, 1.2), "c": (1.3, 0), "d": (2.7, 2.4), "e": (2.7, 1.2),
       "f": (2.7, 0), "y": (4.0, 1.2)}
edges = [("x", "a"), ("x", "b"), ("x", "c"), ("a", "d"), ("b", "e"), ("c", "f"), ("d", "y"), ("e", "y"), ("f", "y"),
         ("a", "b"), ("c", "e"), ("d", "e"), ("b", "f")]
paths = [("x", "a", "d", "y"), ("x", "b", "e", "y"), ("x", "c", "f", "y")]

fig, (ax1, ax2) = G.panels(2, 4.0, 2.4, titles=["three internally disjoint x-y paths", "the vertex cut {a, b, c}"])
hl = {}
for p, colour in zip(paths, (G.BLUE, G.GREEN, G.AMBER)):
    for u, v in zip(p, p[1:]):
        hl[(u, v)] = colour
G.draw(ax1, pos, edges, highlight=hl, vertex_color={"x": G.VIOLET, "y": G.VIOLET})
cut = {"a", "b", "c"}
G.draw(ax2, pos, edges, highlight={v: G.RED for v in cut}, vertex_color={**{v: G.RED for v in cut}, "x": G.VIOLET, "y": G.VIOLET},
       dashed=[e for e in edges if cut & set(e)])
