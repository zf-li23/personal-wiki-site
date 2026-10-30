"""Positioning and induction of the limb.

A: chick embryo (dorsal view, anterior up; schematic) with somites; Tbx5 in the wing-field lateral plate, Tbx4 in the
leg field; an FGF bead in the flank induces an extra bud, Tbx5 anteriorly and Tbx4 posteriorly.
B: regulatory network of limb initiation (open arrows activation, bars inhibition).
C: phase plane of the mutual-activation model (Example 31.3.1) with a = 2.5, K = 1, s = 0: nullclines, flow
field, two stable states (open: off; filled: on) and the saddle.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(30.0, 13.0)

# A: embryo ------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 12.8))
x0 = 4.2
top, bot = 11.8, 1.0
body = bio.smooth_closed(np.array([(x0, top + 0.3), (x0 + 1.5, top - 1.0), (x0 + 1.9, 6.5), (x0 + 1.7, 2.0), (x0 + 0.6, bot),
                                   (x0 - 0.6, bot), (x0 - 1.7, 2.0), (x0 - 1.9, 6.5), (x0 - 1.5, top - 1.0)]), 220)
bio.shape(ax, body, "neutral", lw=0.9, zorder=2)
ax.patches[-1].set_facecolor(P.mix(P.fill("neutral"), P.surface(), 0.6))
ax.add_patch(FancyBboxPatch((x0 - 0.18, 1.6), 0.36, 9.6, boxstyle="round,pad=0,rounding_size=0.15",
                            facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=4))
ys = np.linspace(9.6, 2.6, 26)
for i, y in enumerate(ys):
    for s in (-1, 1):
        ax.add_patch(FancyBboxPatch((x0 + s * 0.3 - (0.42 if s < 0 else 0), y - 0.12), 0.42, 0.24,
                                    boxstyle="round,pad=0,rounding_size=0.06", facecolor=P.fill("mesoderm"),
                                    edgecolor=P.edge("mesoderm"), lw=0.5, zorder=4))
    if (i + 13) % 5 == 0:
        bio.label(ax, (x0 - 2.3, y), str(i + 13), size="tiny", color=P.muted(), ha="right")
bio.label(ax, (x0 - 2.3, 10.2), "Somite", size="tiny", color=P.muted(), ha="right")


def lp(y0, y1, tok):
    for s in (-1, 1):
        ax.add_patch(FancyBboxPatch((x0 + s * 1.05 - (0.55 if s < 0 else 0), y1), 0.55, y0 - y1,
                                    boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                    lw=0.7, zorder=3))


yw0, yw1 = ys[2], ys[7]      # somites 15-20
yl0, yl1 = ys[13], ys[19]    # somites 26-32
lp(yw0 + 0.1, yw1 - 0.1, "channel")
lp(yl0 + 0.1, yl1 - 0.1, "receptor")
# induced bud in the right flank
yb = (yw1 + yl0) / 2
ax.add_patch(Ellipse((x0 + 1.95, yb), 0.9, 1.25, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.7, zorder=5))
ax.add_patch(Ellipse((x0 + 1.95, yb - 0.32), 0.9, 0.6, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.7, zorder=5.1))
ax.add_patch(Circle((x0 + 1.25, yb), 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
bio.callout(ax, (x0 + 1.25, yb), (x0 + 3.4, yb + 1.0), "FGF bead")
bio.callout(ax, (x0 + 2.3, yb + 0.3), (x0 + 3.4, yb + 0.5), "Tbx5 (wing-like)")
bio.callout(ax, (x0 + 2.3, yb - 0.45), (x0 + 3.4, yb - 1.0), "Tbx4 (leg-like)")
bio.callout(ax, (x0 + 1.6, (yw0 + yw1) / 2), (x0 + 3.4, (yw0 + yw1) / 2 + 0.9), "Wing field: Tbx5")
bio.callout(ax, (x0 + 1.6, (yl0 + yl1) / 2), (x0 + 3.4, (yl0 + yl1) / 2 - 0.3), "Leg field: Tbx4, Pitx1")
bio.label(ax, (x0, top + 0.75), "Anterior", size="tiny", color=P.muted())

# B: network ------------------------------------------------------------------------------------
bio.panel(ax, "B", (10.8, 12.8))
N = {"hox": (12.6, 10.6, "Hox code", "neutral"), "ra": (16.2, 10.6, "RA (somites)", "highlight"),
     "f8t": (19.8, 10.6, "Fgf8 (trunk)", "negative"), "tbx5": (14.4, 8.2, "Tbx5", "channel"),
     "wnt2b": (14.4, 5.9, "Wnt2b", "positive"), "f10": (17.8, 5.9, "Fgf10", "mesoderm"),
     "wnt3": (17.8, 2.6, "Wnt3", "positive"), "f8": (21.2, 2.6, "Fgf8 (AER)", "ectoderm")}
for k, (x, y, t, tk) in N.items():
    bio.box(ax, (x, y), 2.6, 0.95, tk, t, size="small")


def edge(a, b, kind="activation", bend=0.0):
    (xa, ya), (xb, yb2) = N[a][:2], N[b][:2]
    v = np.array([xb - xa, yb2 - ya])
    v /= np.hypot(*v)
    sa = np.array([xa, ya]) + v * np.array([1.35, 0.55])
    sb = np.array([xb, yb2]) - v * np.array([1.35, 0.55])
    bio.arrow(ax, tuple(sa), tuple(sb), kind=kind, bend=bend, lw=1.1)


edge("hox", "tbx5")
edge("ra", "f8t", "inhibition")
edge("f8t", "tbx5", "inhibition", bend=0.15)
edge("tbx5", "wnt2b")
edge("wnt2b", "f10")
edge("f10", "tbx5", bend=0.2)
edge("f10", "wnt3")
edge("wnt3", "f8")
edge("f8", "f10", bend=0.25)
bio.label(ax, (11.6, 4.3), "Mesenchyme", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (11.6, 1.4), "Ectoderm", size="tiny", color=P.muted(), ha="left")
ax.plot([11.4, 23.0], [4.0, 4.0], color=P.muted(), lw=0.7, ls=(0, (3, 2)))

# C: phase plane ------------------------------------------------------------------------------------
bio.panel(ax, "C", (23.4, 12.8))
pa = C.axes_at(ax, (24.6, 1.6, 5.0, 10.2))
a, K = 2.5, 1.0
u = np.linspace(0, 3, 300)
pa.plot(u, a * u**2 / (K**2 + u**2), color=Q.line_color("ectoderm"), lw=1.8, label="ẇ = 0")
pa.plot(a * u**2 / (K**2 + u**2), u, color=Q.line_color("mesoderm"), lw=1.8, label="u̇ = 0")
U, W = np.meshgrid(np.linspace(0.05, 2.9, 14), np.linspace(0.05, 2.9, 14))
du = a * W**2 / (K**2 + W**2) - U
dw = a * U**2 / (K**2 + U**2) - W
nrm = np.hypot(du, dw) + 1e-9
pa.quiver(U, W, du / nrm, dw / nrm, color=P.muted(), scale=28, width=0.004)
pa.plot([0], [0], "o", ms=7, mfc=P.surface(), mec=P.ink(), mew=1.2, zorder=5)
pa.plot([0.5], [0.5], "o", ms=6, mfc=P.surface(), mec=P.muted(), mew=1.0, zorder=5)
pa.plot([2], [2], "o", ms=7, color=P.ink(), zorder=5)
pa.text(0.12, 0.05, "off", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.text(0.6, 0.42, "saddle", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.text(2.1, 1.92, "on (limb)", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.set_xlim(0, 3)
pa.set_ylim(0, 3)
pa.set_aspect("equal")
C.style_axes(pa, "Fgf10 signal u", "Fgf8 signal w")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
