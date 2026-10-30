# A tree (leaves shaded), a forest, and a graph that is not a tree because it contains a cycle
import wikigraph as G

fig, (ax1, ax2, ax3) = G.panels(3, 3.2, 2.2, titles=["a tree: 7 vertices, 6 edges", "a forest (two trees)",
                                                      "not a tree: contains a cycle"])
pos = {"a": (1.6, 2.2), "b": (0.6, 1.1), "c": (1.6, 1.1), "d": (2.6, 1.1), "e": (0, 0), "f": (1.2, 0), "g": (2.6, 0)}
tree = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f"), ("d", "g")]
leaves = {"c", "e", "f", "g"}
G.draw(ax1, pos, tree, vertex_color={v: G.GREEN for v in leaves})

pos2 = {"a": (0.4, 2.0), "b": (0, 0.9), "c": (0.9, 0.9), "d": (0.9, 0), "e": (2.2, 2.0), "f": (1.9, 0.9),
        "g": (2.8, 0.9), "h": (3.1, 0)}
forest = [("a", "b"), ("a", "c"), ("c", "d"), ("e", "f"), ("e", "g"), ("g", "h")]
G.draw(ax2, pos2, forest)

pos3 = {"a": (0.4, 2.0), "b": (2.4, 2.0), "c": (2.4, 0.4), "d": (0.4, 0.4), "e": (3.2, 1.2), "f": (1.4, 1.2)}
edges3 = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("b", "e"), ("a", "f")]
G.draw(ax3, pos3, edges3, highlight={("a", "b"): G.RED, ("b", "c"): G.RED, ("c", "d"): G.RED, ("d", "a"): G.RED})
