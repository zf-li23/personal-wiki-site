# A map of six countries (a centre surrounded by a ring of five) and its dual graph, the wheel W5.
# The odd ring needs three colours and the centre touches all of them, so four colours are needed.
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import wikigraph as G

colours = [G.BLUE, G.RED, G.GREEN, G.AMBER]
ring = [0, 1, 0, 1, 2]  # colours of the five ring countries; the centre gets colour 3
fig, (a, b) = plt.subplots(1, 2, figsize=(8.4, 4.2))
for ax in (a, b):
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
fig.subplots_adjust(0.01, 0.01, 0.99, 0.9, wspace=0.05)
a.set_title("a map colored with four colors", fontsize=G.FONT)
b.set_title("its dual graph (the wheel $W_5$)", fontsize=G.FONT)
for k, c in enumerate(ring):
    a.add_patch(Wedge((0, 0), 2.3, 90 + 72 * k, 162 + 72 * k, width=1.3, facecolor=colours[c],
                      alpha=0.45, edgecolor=G.INK, lw=G.EDGE))
a.add_patch(Circle((0, 0), 1.0, facecolor=colours[3], alpha=0.45, edgecolor=G.INK, lw=G.EDGE))

pos = {"c": (0.0, 0.0)}
for k in range(5):
    t = math.radians(126 + 72 * k)
    pos[f"r{k}"] = (1.65 * math.cos(t), 1.65 * math.sin(t))
edges = [("c", f"r{k}") for k in range(5)] + [(f"r{k}", f"r{(k + 1) % 5}") for k in range(5)]
fill = {"c": colours[3]} | {f"r{k}": colours[c] for k, c in enumerate(ring)}
for ax in (a, b):
    G.draw(ax, pos, edges, vertex_color=fill, labels=False,
           edge_color=G.INK if ax is b else G.GREY, width=G.EDGE if ax is b else 1.0)
