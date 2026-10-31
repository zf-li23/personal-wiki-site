# The Szilard engine: one molecule in a box in contact with a heat bath at temperature T, run by a demon with a
# one-bit memory.
# 1. The molecule moves freely through the whole box; the memory is in its reset (standard) state 0.
# 2. A partition is inserted in the middle (no work), and the demon measures on which side the molecule is,
#    recording L or R in its memory.
# 3. Knowing the side, the demon couples the partition, now a piston, to a load on the correct side; the
#    one-molecule gas expands isothermally from V/2 to V and lifts the load by W = kBT ln 2, drawing the same
#    heat Q = kBT ln 2 from the bath.
# 4. To close the cycle the memory must be returned to 0. By Landauer's principle this erasure dissipates at least
#    kBT ln 2 of heat into the bath, so that over the whole cycle no net work is extracted from a single bath.
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.6, 6.6)
W, H = 3.2, 2.2
xs = [0.6, 5.1, 9.6, 15.0]
y0 = 2.0


def chamber(x, partition=None, gas_left=None, gas_right=None):
    # bath underneath
    ax.add_patch(FancyBboxPatch((x - 0.15, y0 - 0.55), W + 0.3, 0.42, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=2))
    bio.label(ax, (x + W / 2, y0 - 0.34), "heat bath, T", size="tiny", color=P.on_fill())
    ax.add_patch(Rectangle((x, y0), W, H, facecolor=P.light("neutral") if not P.is_dark() else P.surface(),
                           edgecolor=P.ink(), lw=1.3, zorder=3))
    if gas_left is not None:
        a, b = gas_left
        ax.add_patch(Rectangle((x + a, y0), b - a, H, facecolor=P.fill("highlight"), alpha=0.35, lw=0, zorder=3.5))
    if partition is not None:
        ax.add_patch(Rectangle((x + partition - 0.06, y0), 0.12, H, facecolor=P.edge("neutral"),
                               edgecolor=P.ink(), lw=0.7, zorder=6))


def molecule(x, y):
    ax.add_patch(Circle((x, y), 0.17, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=8))


def memory(x, text, tok):
    bio.box(ax, (x + W / 2, 5.25), 1.3, 0.55, token=tok, text=text, size="small", radius=0.12)
    bio.label(ax, (x + W / 2 - 0.95, 5.25), "memory", size="tiny", ha="right", color=P.muted())


# 1 free molecule
chamber(xs[0])
molecule(xs[0] + 1.0, y0 + 1.3)
for dx, dy in ((0.5, 0.4), (-0.4, 0.35), (0.35, -0.5)):
    bio.arrow(ax, (xs[0] + 1.0, y0 + 1.3), (xs[0] + 1.0 + dx, y0 + 1.3 + dy), kind="process", lw=0.8,
              color=P.muted(), head=0.12, shrink=0.2)
memory(xs[0], "0", "neutral")
bio.label(ax, (xs[0] + W / 2, 6.25), "1  One molecule fills V", size="small", bold=True)

# 2 insert partition and measure
chamber(xs[1], partition=W / 2)
molecule(xs[1] + 0.8, y0 + 0.9)
memory(xs[1], "L", "dna")
bio.arrow(ax, (xs[1] + 0.8, y0 + 1.2), (xs[1] + W / 2, 4.9), kind="link", dashed=True, color=P.muted(), lw=0.8)
bio.label(ax, (xs[1] + W / 2, 6.25), "2  Insert partition, measure", size="small", bold=True)
bio.label(ax, (xs[1] + 2.45, y0 + 1.1), "V/2", size="small", color=P.muted())

# 3 isothermal expansion lifts a load
chamber(xs[2], partition=2.4, gas_left=(0, 2.4))
molecule(xs[2] + 1.3, y0 + 1.5)
bio.arrow(ax, (xs[2] + 2.5, y0 + 1.1), (xs[2] + 3.1, y0 + 1.1), kind="process", lw=1.2, head=0.16)
# pulley and load
ax.plot([xs[2] + 2.4, xs[2] + 2.4, xs[2] + W + 0.45], [y0 + H, y0 + H + 0.35, y0 + H + 0.35], color=P.ink(), lw=0.9)
ax.plot([xs[2] + W + 0.45, xs[2] + W + 0.45], [y0 + H + 0.35, y0 + 0.9], color=P.ink(), lw=0.9)
ax.add_patch(Rectangle((xs[2] + W + 0.2, y0 + 0.45), 0.5, 0.45, facecolor=P.fill("protein"), edgecolor=P.edge("protein"),
                       lw=0.9, zorder=6))
bio.arrow(ax, (xs[2] + W + 0.95, y0 + 0.4), (xs[2] + W + 0.95, y0 + 1.15), kind="process", lw=1.0, head=0.14)
bio.label(ax, (xs[2] + W + 1.12, y0 + 0.8), "W =\nkBT ln 2", size="tiny", ha="left")
bio.arrow(ax, (xs[2] + 1.0, y0 - 0.6), (xs[2] + 1.0, y0 + 0.1), kind="process", color=P.edge("negative"), lw=1.2,
          head=0.16)
bio.label(ax, (xs[2] + 1.15, y0 - 0.95), "Q = kBT ln 2 in", size="tiny", ha="left")
memory(xs[2], "L", "dna")
bio.label(ax, (xs[2] + W / 2, 6.25), "3  Expand from V/2 to V", size="small", bold=True)

# 4 reset the memory
chamber(xs[3])
molecule(xs[3] + 2.2, y0 + 0.8)
memory(xs[3], "L → 0", "highlight")
bio.arrow(ax, (xs[3] + W / 2 + 0.7, 5.1), (xs[3] + W + 0.3, y0 - 0.3), kind="process", color=P.edge("negative"),
          lw=1.2, head=0.16, dashed=True, bend=0.3)
bio.label(ax, (xs[3] + W + 0.5, 3.9), "erasure:\nQ ≥ kBT ln 2\nto the bath", size="tiny", ha="left")
bio.label(ax, (xs[3] + W / 2, 6.25), "4  Reset the memory", size="small", bold=True)

for a, b in zip(xs[:-1], xs[1:]):
    bio.arrow(ax, (a + W + 0.2 + (0.6 if a == xs[2] else 0), y0 + H / 2 + 0.9), (b - 0.2, y0 + H / 2 + 0.9),
              kind="process", lw=1.0, head=0.16, color=P.muted())
bio.label(ax, (9.0, 0.35), "Net over one cycle: work kBT ln 2 out, at least kBT ln 2 dissipated at erasure; no violation "
                           "of the second law", size="small", color=P.ink())
