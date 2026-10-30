# Why general graphs need blossoms: the augmenting path r s b c1 c2 c3 c4 w runs around the odd
# cycle b c1 c2 c3 c4, so a search that reaches c4 directly from b misses it. Shrinking the
# blossom to a single vertex B leaves the augmenting path r s B w.
import math

import wikigraph as G

pos = {"r": (0, 1.2), "s": (1.2, 1.2), "b": (2.4, 1.2)}
for k, v in enumerate(["c1", "c2", "c3", "c4"]):
    t = math.radians(180 + 72 * (k + 1))
    pos[v] = (3.45 + 1.05 * math.cos(t), 1.2 + 1.05 * math.sin(t))
pos["w"] = (pos["c4"][0] + 1.3, pos["c4"][1] + 0.3)
M = [("s", "b"), ("c1", "c2"), ("c3", "c4")]
edges = [("r", "s"), ("s", "b"), ("b", "c1"), ("c1", "c2"), ("c2", "c3"), ("c3", "c4"), ("c4", "b"), ("c4", "w")]
path = [("r", "s"), ("b", "c1"), ("c2", "c3"), ("c4", "w")]
TEX = {v: (f"$c_{v[1]}$" if v[0] == "c" else f"${v}$") for v in pos}
fig, (a, b) = G.panels(2, 5.6, 2.4, titles=["blossom with base b (matching blue)", "after shrinking the blossom"])
G.draw(a, pos, edges, highlight={e: G.BLUE for e in M} | {e: G.RED for e in path},
       vertex_color={"r": G.GREY, "w": G.GREY}, vertex_labels=TEX)
small = {"r": (0.6, 1.2), "s": (2.0, 1.2), "B": (3.4, 1.2), "w": (4.8, 1.2)}
G.draw(b, small, [("r", "s"), ("s", "B"), ("B", "w")],
       highlight={("s", "B"): G.BLUE, ("r", "s"): G.RED, ("B", "w"): G.RED},
       vertex_color={"r": G.GREY, "w": G.GREY, "B": G.VIOLET}, vertex_labels={v: f"${v}$" for v in small})
