import math
import matplotlib.pyplot as plt
import wikigraph as G

pos = {"c": (0, 1.0), "a": (1.4, 2.0), "b": (1.4, 0), "d": (2.8, 2.0), "e": (2.8, 0), "f": (4.2, 1.0)}
arcs = [("c", "a"), ("c", "b"), ("a", "d"), ("b", "d"), ("b", "e"), ("d", "f"), ("e", "f")]

# Kahn's algorithm, always removing the alphabetically smallest source
indeg = {v: sum(1 for _, w in arcs if w == v) for v in pos}
order, snapshots = [], []
while len(order) < len(pos):
    snapshots.append(dict(indeg))
    u = min(v for v in pos if v not in order and indeg[v] == 0)
    order.append(u)
    for x, w in arcs:
        if x == u:
            indeg[w] -= 1

fig, axes = plt.subplots(2, 3, figsize=(9.0, 4.4))
for step, ax in enumerate(axes.flat):
    ax.set_xlim(-0.5, 4.7)
    ax.set_ylim(-0.7, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    done = order[:step]
    rest = {v: p for v, p in pos.items() if v not in done}
    left = [(u, v) for u, v in arcs if u in rest and v in rest]
    deg = snapshots[step]
    src = order[step]
    G.draw(ax, rest, left, directed=True, highlight={src: G.RED},
           )
    for v, (x, y) in rest.items():
        G.caption(ax, (x, y + (0.4 if y > 0.5 else -0.4)), f"in {deg[v]}", size=8)
    ax.set_title(f"step {step + 1}: output {src}" + ("" if not done else f"  (done: {' '.join(done)})"), fontsize=9)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.93, wspace=0.05, hspace=0.2)

# the resulting order on a line: every arc points to the right
fig2, ax = G.canvas(7.5, 1.4)
lpos = {v: (1.5 * i, 0.2) for i, v in enumerate(order)}
for u, v in arcs:
    (x0, y0), (x1, y1) = lpos[u], lpos[v]
    span = (x1 - x0) / 1.5
    rad = 0 if span == 1 else -0.5
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=1,
                arrowprops=dict(arrowstyle="-|>", color=G.INK, lw=1.3, shrinkA=13, shrinkB=13,
                                connectionstyle=f"arc3,rad={rad}"))
G.draw(ax, lpos, [])
G.caption(ax, (3.75, -0.35), "topological order " + ", ".join(order), size=9)
