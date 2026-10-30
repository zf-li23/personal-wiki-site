# Edmonds-Karp on the network of Example 5.7.1. Each panel is one round: the breadth-first
# labels (u+ or u-, delta_v), the shortest flow augmenting path (forward edges red, the backward
# edge violet) and the flows f/c after augmenting. Last panel: no label reaches t; the labeled
# set S gives the minimum cut (cut edges red).
from collections import deque

import matplotlib.pyplot as plt
import wikigraph as G

cap = {("s", "a"): 2, ("s", "c"): 6, ("a", "b"): 9, ("a", "d"): 6, ("c", "b"): 4,
       ("c", "d"): 1, ("b", "t"): 2, ("d", "t"): 9}
pos = {"s": (0, 1.5), "a": (2, 3), "c": (2, 0), "b": (4.6, 3), "d": (4.6, 0), "t": (6.6, 1.5)}
where = {("a", "d"): 0.25, ("c", "b"): 0.25}  # label position along the crossing diagonals
flow = {e: 0 for e in cap}


def bfs():
    label, queue = {"s": ("", float("inf"))}, deque(["s"])
    while queue:
        u = queue.popleft()
        for v in sorted(set(pos) - label.keys()):
            if (u, v) in cap and flow[u, v] < cap[u, v]:
                label[v] = (u + "+", min(label[u][1], cap[u, v] - flow[u, v]))
            elif (v, u) in cap and flow[v, u] > 0:
                label[v] = (u + "-", min(label[u][1], flow[v, u]))
            else:
                continue
            queue.append(v)
    return label


def show(ax, title, label, highlight, fill):
    ax.set_xlim(-0.5, 7.1)
    ax.set_ylim(-0.6, 3.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=G.FONT)
    G.draw(ax, pos, list(cap), directed=True, highlight=highlight, vertex_color=fill)
    for (u, v), c in cap.items():
        t = where.get((u, v), 0.5)
        (x0, y0), (x1, y1) = pos[u], pos[v]
        ax.text(x0 + t * (x1 - x0), y0 + t * (y1 - y0) + 0.22, f"{flow[u, v]}/{c}", fontsize=G.FONT - 1,
                ha="center", va="center", color=highlight.get((u, v), G.INK))
    for v, (src, d) in label.items():
        if v != "s":
            x, y = pos[v]
            ax.text(x, y + (0.42 if y > 1 else -0.42), f"(${src[0]}^{src[1]}$, {d})", ha="center", va="center",
                    fontsize=G.FONT - 1, color=G.GREEN)


fig, axes = plt.subplots(2, 2, figsize=(10.0, 6.4))
fig.subplots_adjust(0.01, 0.01, 0.99, 0.95, wspace=0.04, hspace=0.12)
for ax in axes.flat[:3]:
    label = bfs()
    path, v = [], "t"
    while v != "s":
        u, sign = label[v][0][:-1], label[v][0][-1]
        path.append((u, v, sign))
        v = u
    delta = label["t"][1]
    hl = {}
    for u, v, sign in path:
        if sign == "+":
            flow[u, v] += delta
            hl[(u, v)] = G.RED
        else:
            flow[v, u] -= delta
            hl[(v, u)] = G.VIOLET
    walk = "-".join(["s"] + [p[1] for p in reversed(path)])
    show(ax, f"augment along {walk}, $\\delta$ = {delta}", label, hl, {})
label = bfs()
cut = {e: G.RED for e in cap if e[0] in label and e[1] not in label}
show(axes.flat[3], "min cut S = {s, b, c}: capacity 2 + 1 + 2 = 5", label, cut,
     {v: G.AMBER for v in label})
