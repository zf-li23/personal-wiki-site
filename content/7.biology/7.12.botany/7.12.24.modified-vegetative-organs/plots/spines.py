"""Four origins of plant spines (schematic, stems in longitudinal view with the vascular strand drawn as a
green band). A: thorn (modified axillary branch, hawthorn type) in the axil of a leaf, the vascular strand
continues into it; B: leaf spine (barberry type), a three-pronged spine in the position of a leaf, its axil
bearing a short shoot with ordinary leaves; C: stipular spines (black locust type), a pair at the base of
a pinnately compound leaf; D: prickles (rose type), outgrowths of the epidermis and cortex scattered along
the stem without vascular connection.
"""

import math

import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(28.0, 11.0)
SW = 0.55  # stem width
VT = "plant"
ST = "animal"


def stem(x, y0, y1):
    ax.add_patch(Polygon([(x - SW / 2, y0), (x + SW / 2, y0), (x + SW / 2, y1), (x - SW / 2, y1)], closed=True,
                         facecolor=P.fill(ST), edgecolor=P.edge(ST), lw=1.0, zorder=4))
    ax.plot([x, x], [y0 + 0.05, y1 - 0.05], color=P.fill(VT), lw=3.0, zorder=4.5, solid_capstyle="butt")


def spike(base, angle, length, width, vascular=True, curve=0.0, token=ST, z=4.2):
    a = math.radians(angle)
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    b = np.asarray(base, float)
    tip = b + u * length + v * curve
    pts = [b + v * width / 2, tip, b - v * width / 2]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.0, zorder=z,
                         joinstyle="round"))
    if vascular:
        ax.plot([b[0] - u[0] * 0.25, b[0] + u[0] * length * 0.6], [b[1] - u[1] * 0.25, b[1] + u[1] * length * 0.6],
                color=P.fill(VT), lw=2.0, zorder=z + 0.1, solid_capstyle="round")
    return tip


titles = ["Thorn (branch)", "Leaf spine", "Stipular spines", "Prickles"]
xs = [3.2, 10.2, 17.2, 24.2]
for k, (x, t) in enumerate(zip(xs, titles)):
    bio.panel(ax, "ABCD"[k], (x - 3.0, 10.8))
    bio.label(ax, (x - 2.35, 10.77), t, size="title", ha="left", va="top")
    stem(x, 0.6, 9.6)

# A thorn in a leaf axil
x = xs[0]
B.leaf(ax, (x - SW / 2, 4.0), 2.8, 150, shape="ovate", petiole=0.6, margin="serrate", secondaries=5)
tip = spike((x - SW / 2 + 0.05, 4.35), 118, 2.6, 0.42)
B.leaf(ax, (x + SW / 2, 7.4), 2.6, 30, shape="ovate", petiole=0.6, margin="serrate", secondaries=5)
bio.callout(ax, tip, (x - 2.6, 8.6), "Thorn in leaf axil", size="small")
bio.callout(ax, (x, 2.0), (x - 2.6, 1.2), "Vascular strand", size="small")

# B leaf spine (three prongs) with a short shoot in its axil
x = xs[1]
for y in (3.0, 7.0):
    side = 1 if y < 5 else -1
    base = (x + side * SW / 2, y)
    ang = 0 if side > 0 else 180
    for d in (-35, 0, 35):
        spike(base, ang + d, 1.7, 0.22, vascular=(d == 0))
    # short shoot with a rosette of small leaves above the spine
    sx = base[0] + side * 0.35
    ax.plot([sx, sx + side * 0.25], [y + 0.15, y + 0.6], color=P.edge(ST), lw=3.0, zorder=4.4)
    for a in (55, 90, 125):
        B.leaf(ax, (sx + side * 0.25, y + 0.6), 0.9, a, shape="obovate", petiole=0.1, secondaries=3, zorder=6)
bio.callout(ax, (x + SW / 2 + 1.6, 3.0), (x + 2.4, 1.4), "Leaf spine", size="small")
bio.callout(ax, (x + 0.85, 4.1), (x + 2.4, 5.0), "Short shoot in axil", size="small")

# C stipular spines at the base of a compound leaf
x = xs[2]
for y, side in ((3.4, 1), (7.0, -1)):
    base = np.array([x + side * SW / 2, y])
    ang = 40 if side > 0 else 140
    B.compound_leaf(ax, tuple(base), 3.4, ang, kind="imparipinnate", leaflets=3)
    for d in (-55, 55):
        spike(base, ang + d, 1.2, 0.24)
bio.callout(ax, (x + SW / 2 + 0.25, 3.4 - 0.65), (x + 2.3, 1.4), "Stipular spine", size="small")
bio.callout(ax, (x + 1.4, 4.6), (x + 2.6, 9.4), "Compound leaf", size="small")

# D prickles scattered on the stem, no vascular connection
x = xs[3]
rng = np.random.default_rng(4)
for k, y in enumerate(np.linspace(1.4, 9.0, 8)):
    side = 1 if k % 2 == 0 else -1
    yy = y + rng.uniform(-0.3, 0.3)
    spike((x + side * SW / 2 * 0.9, yy), (100 if side < 0 else 80) + side * -60, 0.75, 0.55, vascular=False,
          curve=-0.18 * side, z=4.6)
B.leaf(ax, (x + SW / 2, 6.0), 2.4, 30, shape="elliptic", petiole=0.6, margin="serrate", secondaries=5)
bio.callout(ax, (x + SW / 2 + 0.3, 1.5), (x + 2.2, 0.8), "Prickle", size="small")
bio.callout(ax, (x, 4.3), (x + 2.2, 3.4), "No vascular trace", size="small")
