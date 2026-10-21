"""Transistor-level CMOS gates: inverter, 2-input NAND and 2-input NOR.
pMOS transistors (bubble on the gate) form the pull-up network to VDD,
nMOS transistors form the pull-down network to GND; the two networks are duals."""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

FG = plt.rcParams["text.color"]


def line(ax, *pts):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=FG, lw=1.3, solid_capstyle="round")


def dot(ax, p):
    ax.plot(*p, "o", color=FG, ms=4)


def text(ax, p, s, **kw):
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    kw.setdefault("fontsize", 10)
    ax.text(p[0], p[1], s, color=FG, **kw)


def mos(ax, x, y, kind, name):
    """Channel at x, centred on y. Returns (top, bottom, gate) terminals."""
    line(ax, (x, y - 0.3), (x, y + 0.3))
    line(ax, (x, y + 0.22), (x + 0.3, y + 0.22), (x + 0.3, y + 0.5))
    line(ax, (x, y - 0.22), (x + 0.3, y - 0.22), (x + 0.3, y - 0.5))
    line(ax, (x - 0.1, y - 0.25), (x - 0.1, y + 0.25))
    if kind == "p":
        r = 0.06
        ax.add_patch(Circle((x - 0.1 - r, y), r, facecolor="none", edgecolor=FG, lw=1.3))
        line(ax, (x - 0.6, y), (x - 0.1 - 2 * r, y))
    else:
        line(ax, (x - 0.6, y), (x - 0.1, y))
    text(ax, (x + 0.55, y), name, fontsize=9)
    return (x + 0.3, y + 0.5), (x + 0.3, y - 0.5), (x - 0.6, y)


def rail(ax, x0, x1, y, name):
    line(ax, (x0, y), (x1, y))
    text(ax, ((x0 + x1) / 2, y + 0.18 if name == "VDD" else y - 0.2), name, fontsize=9)


fig, axes = plt.subplots(1, 3, figsize=(10, 4.4))

# inverter
ax = axes[0]
tp, bp, gp = mos(ax, 0, 1.0, "p", "P")
tn, bn, gn = mos(ax, 0, -0.6, "n", "N")
rail(ax, -0.2, 0.8, 1.5, "VDD")
rail(ax, -0.2, 0.8, -1.1, "GND")
line(ax, bp, tn)
dot(ax, (0.3, 0.2))
line(ax, (0.3, 0.2), (1.0, 0.2))
text(ax, (1.2, 0.2), "Y")
line(ax, gp, (-0.9, 1.0), (-0.9, -0.6), gn)
dot(ax, (-0.9, 0.2))
line(ax, (-1.3, 0.2), (-0.9, 0.2))
text(ax, (-1.5, 0.2), "A")
ax.set_title(r"inverter  $Y = \overline{A}$", fontsize=10)

# NAND2: pMOS in parallel, nMOS in series
ax = axes[1]
t1, b1, g1 = mos(ax, -0.9, 1.4, "p", "P1")
t2, b2, g2 = mos(ax, 0.8, 1.4, "p", "P2")
rail(ax, -0.8, 1.3, 1.9, "VDD")
line(ax, b1, (b1[0], 0.7), (b2[0], 0.7), b2)
t3, b3, g3 = mos(ax, 0.1, 0.1, "n", "N1")
t4, b4, g4 = mos(ax, 0.1, -0.9, "n", "N2")
line(ax, (t3[0], 0.7), t3)
dot(ax, (t3[0], 0.7))
line(ax, b3, t4)
rail(ax, -0.2, 0.8, -1.4, "GND")
line(ax, (b2[0], 0.7), (1.6, 0.7))
dot(ax, (b2[0], 0.7))
text(ax, (1.8, 0.7), "Y")
text(ax, (g1[0] - 0.15, g1[1]), "A", ha="right")
text(ax, (g2[0] - 0.15, g2[1]), "B", ha="right")
text(ax, (g3[0] - 0.15, g3[1]), "A", ha="right")
text(ax, (g4[0] - 0.15, g4[1]), "B", ha="right")
ax.set_title(r"NAND  $Y = \overline{AB}$", fontsize=10)

# NOR2: pMOS in series, nMOS in parallel
ax = axes[2]
t1, b1, g1 = mos(ax, 0.1, 1.6, "p", "P1")
t2, b2, g2 = mos(ax, 0.1, 0.6, "p", "P2")
rail(ax, -0.2, 0.8, 2.1, "VDD")
line(ax, b1, t2)
t3, b3, g3 = mos(ax, -0.9, -0.6, "n", "N1")
t4, b4, g4 = mos(ax, 0.8, -0.6, "n", "N2")
line(ax, b2, (b2[0], -0.05))
line(ax, (t3[0], -0.05), (t4[0], -0.05))
line(ax, (t3[0], -0.05), t3)
line(ax, (t4[0], -0.05), t4)
dot(ax, (b2[0], -0.05))
rail(ax, -0.8, 1.3, -1.1, "GND")
line(ax, (t4[0], -0.05), (1.6, -0.05))
dot(ax, (t4[0], -0.05))
text(ax, (1.8, -0.05), "Y")
text(ax, (g1[0] - 0.15, g1[1]), "A", ha="right")
text(ax, (g2[0] - 0.15, g2[1]), "B", ha="right")
text(ax, (g3[0] - 0.15, g3[1]), "A", ha="right")
text(ax, (g4[0] - 0.15, g4[1]), "B", ha="right")
ax.set_title(r"NOR  $Y = \overline{A + B}$", fontsize=10)

for ax in axes:
    ax.set_xlim(-2.0, 2.1)
    ax.set_ylim(-1.6, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
