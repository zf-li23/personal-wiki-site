# Cut vertices, a bridge and the block decomposition of one graph
import wikigraph as G

pos = {"a": (0, 0), "b": (0, 1.6), "c": (1.2, 0.8), "d": (2.6, 0.8),
       "e": (3.4, 1.6), "f": (4.2, 0.8), "g": (3.4, 0), "h": (5.4, 1.6), "i": (5.4, 0)}
edges = [("a", "b"), ("b", "c"), ("c", "a"), ("c", "d"),
         ("d", "e"), ("e", "f"), ("f", "g"), ("g", "d"),
         ("f", "h"), ("h", "i"), ("i", "f")]
blocks = [["a", "b", "c"], ["c", "d"], ["d", "e", "f", "g"], ["f", "h", "i"]]
colours = [G.BLUE, G.RED, G.GREEN, G.AMBER]

fig, (ax1, ax2) = G.panels(2, 5.4, 1.6, titles=["cut vertices c, d, f and the bridge cd", "the four blocks"])
G.draw(ax1, pos, edges, highlight={"c": G.RED, "d": G.RED, "f": G.RED, ("c", "d"): G.RED})

# Exploded view: every block is shifted away from the centre so that shared cut vertices split
shift = [(-0.6, 0), (0, 0), (0.6, 0), (1.2, 0)]
for block, colour, (dx, dy) in zip(blocks, colours, shift):
    sub = {f"{v}{len(block)}": (pos[v][0] + dx, pos[v][1] + dy) for v in block}
    names = {f"{v}{len(block)}": v for v in block}
    sub_edges = [(f"{u}{len(block)}", f"{v}{len(block)}") for u, v in edges if u in block and v in block]
    G.draw(ax2, sub, sub_edges, edge_color=colour, vertex_labels=names)
ax2.set_xlim(-0.9, 6.9)
