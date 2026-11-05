"""Cell lineage of the male gametophyte of Pinus. The microspore divides unequally four times: first and
second prothallial cells (vegetative, soon degenerate) are cut off; the antheridial initial divides into the
tube cell and the generative cell. The pollen is shed at this four-celled stage. After pollination the
generative cell divides into a stalk cell and a body cell, and about a year later the body cell divides into
two non-motile sperm. Right: the shed pollen grain with its two air sacs."""
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 13)

nodes = {
    "ms": (2.0, 9.0, "Microspore", "anther"),
    "p1": (6.0, 11.2, "1st prothallial cell", "neutral"),
    "e": (6.0, 7.2, "Embryonal cell", "anther"),
    "p2": (10.2, 9.2, "2nd prothallial cell", "neutral"),
    "a": (10.2, 5.4, "Antheridial initial", "anther"),
    "t": (14.4, 7.4, "Tube cell", "receptor"),
    "g": (14.4, 3.6, "Generative cell", "dna"),
    "s": (18.4, 5.4, "Stalk cell", "neutral"),
    "b": (18.4, 1.8, "Body cell", "dna"),
}
for k, (x, y, t, tok) in nodes.items():
    bio.box(ax, (x, y), 3.3, 1.0, token=tok, text=t, size="small")
edges = [("ms", "p1"), ("ms", "e"), ("e", "p2"), ("e", "a"), ("a", "t"), ("a", "g"), ("g", "s"), ("g", "b")]
for a, b in edges:
    xa, ya = nodes[a][:2]
    xb, yb = nodes[b][:2]
    bio.arrow(ax, (xa + 1.7, ya), (xb - 1.7, yb), kind="process")
for x, y in ((21.3, 2.5), (21.3, 1.1)):
    bio.arrow(ax, (20.1, 1.8), (x - 0.75, y), kind="process")
    bio.box(ax, (x + 0.4, y), 2.2, 0.75, token="dna", text="Sperm", size="small")
for k in ("p1", "p2"):
    x, y = nodes[k][:2]
    bio.label(ax, (x, y - 0.8), "degenerates", size="tiny", color=P.muted())

# phases
for x0, x1, t in ((0.3, 16.2, "In the pollen sac (before shedding): 4-celled pollen"),
                  (16.4, 20.2, "After pollination"), (20.4, 23.0, "c. 1 year later")):
    ax.plot([x0, x1], [12.6, 12.6], color=P.edge("anther"), lw=2.0, solid_capstyle="butt")
    bio.label(ax, ((x0 + x1) / 2, 12.15), t, size="small", color=P.muted())

# pollen grain at shedding
cx, cy = 23.6, 8.0
for sgn in (-1, 1):
    ax.add_patch(Ellipse((cx + sgn * 1.0, cy - 0.25), 1.3, 1.5, facecolor=P.light("anther"), edgecolor=P.edge("anther"), lw=0.9,
                         zorder=6))
ax.add_patch(Ellipse((cx, cy), 1.9, 1.6, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.1, zorder=7))
for dx in (-0.5, -0.25):
    ax.add_patch(Ellipse((cx + dx, cy + 0.55), 0.2, 0.35, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.5, zorder=8))
ax.add_patch(Circle((cx + 0.1, cy + 0.4), 0.22, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, zorder=8))
ax.add_patch(Circle((cx + 0.2, cy - 0.25), 0.32, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=8))
bio.callout(ax, (cx - 1.2, cy - 0.5), (cx - 1.4, cy - 2.0), "air sac")
bio.callout(ax, (cx - 0.4, cy + 0.6), (cx - 1.2, cy + 2.0), "prothallial cells")
bio.callout(ax, (cx + 0.2, cy + 0.5), (cx + 1.0, cy + 2.0), "generative")
bio.callout(ax, (cx + 0.4, cy - 0.35), (cx + 1.3, cy - 2.0), "tube cell")
bio.label(ax, (cx, cy + 3.0), "Shed pollen grain", size="normal", bold=True)
