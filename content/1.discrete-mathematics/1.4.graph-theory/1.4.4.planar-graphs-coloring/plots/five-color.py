# The two cases of the five color theorem (Theorem 4.5.2): v has five neighbours coloured 1-5.
# Left: the 1-3 chain from v1 misses v3, so swapping 1 and 3 on it frees colour 1 for v.
# Right: a 1-3 chain joins v1 to v3; with v it forms a cycle that separates v2 from v4,
# so the 2-4 chain from v2 cannot reach v4, and swapping 2 and 4 on it frees colour 2.
import math

import wikigraph as G

C = [G.BLUE, G.RED, G.GREEN, G.AMBER, G.VIOLET]  # colours 1-5
fig, (a, b) = G.panels(2, 4.6, 4.4, titles=["case 1: swap colors 1, 3 on the chain from $v_1$",
                                             "case 2: swap colors 2, 4 on the chain from $v_2$"])
pos = {"v": (2.3, 2.0)}
for k in range(5):
    t = math.radians(90 + 72 * k)
    pos[f"v{k + 1}"] = (2.3 + 1.2 * math.cos(t), 2.0 + 1.2 * math.sin(t))
star = [("v", f"v{k}") for k in range(1, 6)]
fill = {f"v{k + 1}": C[k] for k in range(5)}
TEX = {"v": "$v$"} | {f"v{k}": f"$v_{k}$" for k in range(1, 6)}

# case 1: a short 1-3 chain v1 - x - y that does not reach v3
p1 = pos | {"x": (3.3, 4.0), "y": (4.4, 3.6)}
chain1 = [("v1", "x"), ("x", "y")]
G.draw(a, p1, star + chain1, vertex_color=fill | {"x": C[2], "y": C[0]},
       highlight={e: G.BLUE for e in chain1}, vertex_labels=TEX | {"x": "", "y": ""})
a.text(2.3, -0.25, "after the swap $v_1$ has color 3; give $v$ color 1", ha="center", fontsize=G.FONT)

# case 2: a 1-3 chain v1 - p - q - v3 around v2, and a 2-4 chain v2 - r trapped inside
p2 = pos | {"p": (0.25, 3.9), "q": (-0.05, 1.6), "r": (0.6, 2.95)}
chain13 = [("v1", "p"), ("p", "q"), ("q", "v3")]
chain24 = [("v2", "r")]
G.draw(b, p2, star + chain13 + chain24, vertex_color=fill | {"p": C[2], "q": C[0], "r": C[3]},
       highlight={e: G.BLUE for e in chain13} | {e: G.RED for e in chain24} | {("v", "v1"): G.BLUE, ("v", "v3"): G.BLUE},
       vertex_labels=TEX | {"p": "", "q": "", "r": ""})
b.text(2.3, -0.25, "the blue cycle separates $v_2$ from $v_4$", ha="center", fontsize=G.FONT)
