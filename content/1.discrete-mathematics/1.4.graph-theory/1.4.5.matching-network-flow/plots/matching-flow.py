# The bipartite graph of Example 5.1.1 as a flow network with unit capacities (Section 5.9):
# an integral maximum flow of value 4 (red arcs carry flow 1) is the maximum matching.
import wikigraph as G

X = [f"x{i}" for i in range(1, 6)]
Y = [f"y{i}" for i in range(1, 6)]
ADJ = {"x1": ["y1", "y2"], "x2": ["y1"], "x3": ["y2", "y3", "y4", "y5"], "x4": ["y3"], "x5": ["y1"]}
matching = [("x1", "y2"), ("x2", "y1"), ("x3", "y4"), ("x4", "y3")]
pos = {x: (1.5, 4.4 - 1.1 * i) for i, x in enumerate(X)} | {y: (4.0, 4.4 - 1.1 * i) for i, y in enumerate(Y)}
pos |= {"s": (0.0, 2.2), "t": (5.5, 2.2)}
arcs = [("s", x) for x in X] + [(x, y) for x in X for y in ADJ[x]] + [(y, "t") for y in Y]
used = {u for e in matching for u in e}
hl = {e: G.RED for e in matching} | {("s", x): G.RED for x in X if x in used} | \
     {(y, "t"): G.RED for y in Y if y in used}
fig, ax = G.canvas(5.5, 4.4, scale=0.8)
G.draw(ax, pos, arcs, directed=True, highlight=hl, vertex_labels={v: f"${v[0]}_{v[1]}$" for v in X + Y},
       width=1.1)
