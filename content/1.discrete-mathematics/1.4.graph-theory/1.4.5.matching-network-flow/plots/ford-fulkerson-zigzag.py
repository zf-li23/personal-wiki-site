# A bad choice of augmenting paths for Ford-Fulkerson: alternating between s-a-b-t and
# s-b-a-t (which uses a-b backwards) raises the flow by 1 per round, 200 rounds in all;
# Edmonds-Karp takes the two shortest paths s-a-t and s-b-t and is done in two rounds.
import wikigraph as G

C = 100
cap = {("s", "a"): C, ("s", "b"): C, ("a", "b"): 1, ("a", "t"): C, ("b", "t"): C}
pos = {"s": (0, 1.2), "a": (2, 2.4), "b": (2, 0), "t": (4, 1.2)}
offset = {("s", "a"): (-0.35, 0.2), ("s", "b"): (-0.35, -0.2), ("a", "b"): (0.3, 0),
          ("a", "t"): (0.35, 0.2), ("b", "t"): (0.35, -0.2)}
rounds = [
    ("round 1: s-a-b-t, $\\delta$ = 1", {("s", "a"): 1, ("a", "b"): 1, ("b", "t"): 1},
     {("s", "a"): G.RED, ("a", "b"): G.RED, ("b", "t"): G.RED}),
    ("round 2: s-b-a-t, $\\delta$ = 1", {("s", "a"): 1, ("s", "b"): 1, ("a", "t"): 1, ("b", "t"): 1},
     {("s", "b"): G.RED, ("a", "b"): G.VIOLET, ("a", "t"): G.RED}),
    ("Edmonds-Karp: s-a-t, s-b-t", {("s", "a"): C, ("s", "b"): C, ("a", "t"): C, ("b", "t"): C},
     {("s", "a"): G.RED, ("a", "t"): G.RED, ("s", "b"): G.BLUE, ("b", "t"): G.BLUE}),
]
fig, axes = G.panels(3, 4.0, 2.4, titles=[r[0] for r in rounds])
for ax, (_, flow, hl) in zip(axes, rounds):
    G.draw(ax, pos, list(cap), directed=True, highlight=hl)
    for (u, v), c in cap.items():
        (x0, y0), (x1, y1) = pos[u], pos[v]
        dx, dy = offset[u, v]
        ax.text((x0 + x1) / 2 + dx, (y0 + y1) / 2 + dy, f"{flow.get((u, v), 0)}/{c}",
                fontsize=G.FONT - 1, ha="center", va="center", color=hl.get((u, v), G.INK))
