# Greedy coloring of the crown graph (K4,4 minus a perfect matching, Example 4.6.1):
# the order x1, y1, x2, y2, ... uses four colors, the order x1, ..., x4, y1, ..., y4 only two.
import wikigraph as G

C = [G.BLUE, G.RED, G.GREEN, G.AMBER]
xs, ys = [f"x{i}" for i in range(1, 5)], [f"y{i}" for i in range(1, 5)]
edges = [(x, y) for x in xs for y in ys if x[1] != y[1]]
pos = {x: (1.2 * i, 2.0) for i, x in enumerate(xs)} | {y: (1.2 * i, 0.0) for i, y in enumerate(ys)}
TEX = {v: f"${v[0]}_{v[1]}$" for v in xs + ys}


def greedy(order):
    colour = {}
    for v in order:
        used = {colour[u] for e in edges for u in e if v in e and u != v and u in colour}
        colour[v] = min(c for c in range(len(order)) if c not in used)
    return colour


orders = [[v for pair in zip(xs, ys) for v in pair], xs + ys]
fig, axes = G.panels(2, 3.6, 2.0, titles=["order $x_1, y_1, x_2, y_2, \\dots$: 4 colors",
                                           "order $x_1, \\dots, x_4, y_1, \\dots, y_4$: 2 colors"])
for ax, order in zip(axes, orders):
    colour = greedy(order)
    G.draw(ax, pos, edges, vertex_color={v: C[c] for v, c in colour.items()}, vertex_labels=TEX, width=1.0)
