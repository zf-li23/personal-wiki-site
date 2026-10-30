# K5 and K3,3, each drawn with a single crossing: removing the red edge leaves a plane graph.
import numpy as np
import wikigraph as G

fig, (a, b) = G.panels(2, 4.0, 3.6, titles=["$K_5$: m = 10 > 3n - 6 = 9", "$K_{3,3}$: m = 9 > 2n - 4 = 8"])

# K5: a plane K4 (1, 2, 3, 4) plus vertex 5 inside the face 1-2-4; only edge 5-3 crosses.
p5 = {"1": (0.0, 0.0), "2": (4.0, 0.0), "3": (2.0, 3.5), "4": (2.3, 1.6), "5": (1.45, 0.55)}
k5 = [(u, v) for i, u in enumerate("12345") for v in "12345"[i + 1:]]
G.draw(a, p5, k5, highlight={("3", "5"): G.RED})

# K3,3 on a hexagon (A = a1, a2, a3; B = b1, b2, b3): two long diagonals inside cross,
# the third goes around the outside.
names = ["a1", "b1", "a2", "b2", "a3", "b3"]
hexagon = G.circle(names, radius=1.5, center=(2.0, 1.7), start=90)
inner = [("a1", "b2"), ("b1", "a3")]
ring = [(names[i], names[(i + 1) % 6]) for i in range(6)]
TEX = {v: f"${v[0]}_{v[1]}$" for v in names}
G.draw(b, hexagon, ring + inner, highlight={("b1", "a3"): G.RED},
       vertex_color={v: G.BLUE for v in names if v[0] == "a"}, vertex_labels=TEX)
# outer diagonal b3-a2, drawn as an arc around the top of the hexagon
cx, cy = 2.0, 1.7
theta = np.radians(np.linspace(30, 210, 120))
r = 1.5 + 0.55 * np.sin(theta - np.radians(30))
xs, ys = cx + r * np.cos(theta), cy + r * np.sin(theta)
keep = [np.hypot(x - hexagon[v][0], y - hexagon[v][1]) > 0.22 for x, y in zip(xs, ys) for v in ["b3"]]
keep = np.array(keep) & np.array([np.hypot(x - hexagon["a2"][0], y - hexagon["a2"][1]) > 0.22 for x, y in zip(xs, ys)])
b.plot(xs[keep], ys[keep], color=G.INK, lw=G.EDGE, zorder=2)
