# Prim's algorithm on Example 3.7.1 from vertex a: the chosen set U (shaded) grows by the lightest crossing edge
import matplotlib.pyplot as plt
import wikigraph as G

pos = {"a": (0, 1), "b": (1.5, 2), "c": (3, 2), "d": (4.5, 1), "e": (3, 0), "f": (1.5, 0)}
edges = [("a", "b", 4), ("a", "f", 2), ("b", "f", 5), ("b", "c", 6), ("c", "f", 1), ("c", "e", 3),
         ("e", "f", 8), ("c", "d", 7), ("d", "e", 9)]

fig, axes = plt.subplots(2, 3, figsize=(8.6, 3.6))
U, tree = {"a"}, []
for k, ax in enumerate(axes.flat):
    ax.set_xlim(-0.4, 4.9)
    ax.set_ylim(-0.4, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    crossing = [e for e in edges if (e[0] in U) != (e[1] in U)]
    hl = {e: G.BLUE for e in tree}
    if crossing:
        u, v, w = min(crossing, key=lambda e: e[2])
        hl[(u, v)] = G.RED
        title = f"step {k + 1}: add {u}{v} ({w})"
    else:
        title = f"done: weight {sum(e[2] for e in edges if (e[0], e[1]) in tree)}"
    G.draw(ax, pos, edges, weights=True, highlight=hl, edge_color=G.GREY,
           dashed=[e for e in crossing if (e[0], e[1]) != (u, v)] if crossing else [],
           vertex_color={x: G.AMBER for x in U})
    ax.set_title(title, fontsize=G.FONT)
    if crossing:
        tree.append((u, v))
        U |= {u, v}
fig.subplots_adjust(0.01, 0.01, 0.99, 0.93, wspace=0.05, hspace=0.2)
