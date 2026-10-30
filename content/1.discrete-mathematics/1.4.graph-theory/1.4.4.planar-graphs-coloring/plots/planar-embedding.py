# K4 drawn with a crossing and as a plane graph: planar is a property of the graph,
# plane refers to one crossing-free drawing.
import wikigraph as G

TEX = {f"v{i}": f"$v_{i}$" for i in range(1, 6)}

edges = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v1"), ("v1", "v3"), ("v2", "v4")]
fig, (a, b) = G.panels(2, 2.6, 2.4, titles=["a drawing of K4 with one crossing", "a plane embedding of K4"])
square = {"v1": (0.3, 0.2), "v2": (2.3, 0.2), "v3": (2.3, 2.2), "v4": (0.3, 2.2)}
G.draw(a, square, edges, highlight={("v1", "v3"): G.RED, ("v2", "v4"): G.RED}, vertex_labels=TEX)
plane = {"v1": (0.0, 0.0), "v2": (2.6, 0.0), "v3": (1.3, 2.3), "v4": (1.3, 0.8)}
G.draw(b, plane, edges, highlight={("v1", "v3"): G.BLUE, ("v2", "v4"): G.BLUE}, vertex_labels=TEX)
