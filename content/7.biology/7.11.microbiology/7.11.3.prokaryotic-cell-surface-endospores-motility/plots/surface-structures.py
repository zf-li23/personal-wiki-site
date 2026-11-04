"""Surface structures of a Gram-negative bacterium (capsule, fimbriae, sex pilus, type IV pilus,
flagella) and, inset, an archaeal hamus with prickles and a three-pronged terminal hook."""
import numpy as np
from matplotlib.patches import Ellipse, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(27, 12)
cx, cy, L, W = 9.0, 6.6, 7.0, 2.6
# capsule halo
ax.add_patch(Ellipse((cx, cy), L + 1.3, W + 1.3, facecolor=P.light("lipid_head"), edgecolor=P.edge("lipid_head"),
                     lw=1.0, ls="--", zorder=3))
M.bacillus(ax, (cx, cy), L, W, token="bacterium", zorder=6)
# fimbriae: short straight lines normal to the outline
rng = np.random.default_rng(2)
for t in np.linspace(0, 2 * np.pi, 46, endpoint=False):
    x = cx + (L / 2) * np.cos(t)
    y = cy + (W / 2) * np.sin(t)
    nx, ny = np.cos(t) / (L / 2), np.sin(t) / (W / 2)
    n = np.hypot(nx, ny)
    nx, ny = nx / n, ny / n
    ln = 0.95 + rng.uniform(-0.1, 0.1)
    ax.plot([x, x + ln * nx], [y, y + ln * ny], color=P.edge("protein"), lw=0.8, zorder=5)
    ax.plot([x + ln * nx], [y + ln * ny], "o", ms=2.2, color=P.fill("protein"), markeredgecolor=P.edge("protein"),
            markeredgewidth=0.4, zorder=5)
# flagella from the right pole and the top side
M.flagellum(ax, (cx + L / 2 - 0.05, cy + 0.2), 0.15, length=4.2, amplitude=0.25, waves=3.0, zorder=4)
M.flagellum(ax, (cx + 1.2, cy + W / 2 - 0.05), 1.25, length=3.6, amplitude=0.25, waves=2.6, zorder=4)
# sex pilus to a recipient cell at the upper left
M.bacillus(ax, (2.3, 10.6), 2.6, 1.1, angle=15, token="neutral", zorder=6)
ax.plot([cx - 2.4, 3.3], [cy + W / 2 - 0.2, 10.15], color=P.edge("dna"), lw=2.0, zorder=5)
# type IV pilus to a surface below, with a retraction arrow
ax.add_patch(Rectangle((0.5, 0.6), 17.5, 0.6, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=2))
bio.label(ax, (16.6, 0.9), "surface", size="tiny", color=P.muted())
x0 = cx - L / 2 + 0.6
ax.plot([x0, x0 - 1.8], [cy - W / 2 + 0.2, 1.25], color=P.edge("enzyme"), lw=1.6, zorder=5)
bio.arrow(ax, (x0 - 0.9, 1.9), (x0 + 0.0, 4.1), kind="process", color=P.edge("enzyme"))
bio.label(ax, (x0 + 0.5, 2.6), "retraction", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (cx - 0.8, cy), "Gram-negative rod", size="small", color=P.on_fill(), zorder=12)
# callouts
c = 18.4
bio.callout(ax, (cx + 1.0, cy - W / 2 - 0.6), (13.6, 2.4), "Capsule")
bio.callout(ax, (cx + 2.6, cy - W / 2 - 0.15), (14.6, 3.2), "Fimbriae (adhesins at tips)")
bio.callout(ax, (cx + L / 2 + 2.5, cy + 0.4), (c - 1.0, cy + 1.6), "Flagellum")
bio.callout(ax, (5.0, 9.2), (6.4, 11.4), "Sex pilus")
bio.callout(ax, (2.3, 10.6 + 0.6), (1.0, 11.7), "Recipient cell")
bio.callout(ax, (x0 - 1.0, 3.0), (1.2, 3.6), "Type IV pilus:\nattaches, retracts")
# inset: hamus
ix, iy = 21.5, 3.0
bio.label(ax, (22.9, 11.4), "Archaeal hamus (inset)", size="small", bold=True)
ax.add_patch(Rectangle((19.2, 1.2), 7.4, 9.6, facecolor="none", edgecolor=P.muted(), lw=0.8, zorder=2))
ys = np.linspace(iy, 9.6, 40)
xs = ix + 0.15 * np.sin(ys * 2.2)
ax.plot(xs, ys, color=P.edge("enzyme"), lw=1.6, zorder=6)
for k in range(2, 34, 4):
    for s in (-1, 1):
        ax.plot([xs[k], xs[k] + s * 0.35], [ys[k], ys[k] + 0.25], color=P.edge("enzyme"), lw=1.0, zorder=6)
for ang in (-35, 0, 35):
    a = np.deg2rad(ang - 90)
    tip = (ix + 0.8 * np.cos(a), iy + 0.8 * np.sin(a) + 0.2)
    ax.plot([ix, tip[0]], [iy, tip[1]], color=P.edge("enzyme"), lw=1.6, zorder=6)
    ax.plot([tip[0], tip[0] + 0.25 * np.sign(ang + 0.01)], [tip[1], tip[1] + 0.3], color=P.edge("enzyme"), lw=1.4,
            zorder=6)
bio.callout(ax, (xs[14] + 0.35, ys[14] + 0.25), (23.4, 6.6), "prickles")
bio.callout(ax, (ix + 0.45, iy - 0.4), (23.4, 2.0), "grappling hook")
bio.label(ax, (ix, 10.2), "to cell", size="tiny", color=P.muted())
