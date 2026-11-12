# Extraembryonic membranes and blastokinesis of a hemimetabolous insect egg (schematic longitudinal sections,
# anterior to the left, ventral side of the egg at the bottom). 1 blastoderm with ventral germ anlage;
# 2 amniotic folds grow over the germ band; 3 anatrepsis: the germ band sinks into the yolk tail first;
# 4 segmented germ band with limb buds, reversed; 5 katatrepsis: return to the ventral surface;
# 6 dorsal closure, serosa contracted into the dorsal organ.
import numpy as np
from matplotlib.patches import Ellipse
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 13.5)
RX, RY = 3.4, 1.7
GB, AM, SE = "ectoderm", "positive", "negative"


def egg(c, serosa=True, yolk=True):
    ax.add_patch(Ellipse(c, 2 * RX, 2 * RY, facecolor=P.fill("ovule") if yolk else "none", edgecolor=P.edge("neutral"), lw=1.4, zorder=3))
    if serosa:
        ax.add_patch(Ellipse(c, 2 * RX - 0.25, 2 * RY - 0.25, facecolor="none", edgecolor=P.edge(SE), lw=1.1, zorder=6))


def band(pts, lw=6, z=7, buds=0, bud_dir=1):
    pts = np.asarray(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill(GB), lw=lw, solid_capstyle="round", zorder=z)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(GB), lw=0.6, zorder=z + 1)
    if buds:
        idx = np.linspace(len(pts) * 0.18, len(pts) * 0.55, buds).astype(int)
        for i in idx:
            a, b = pts[max(i - 1, 0)], pts[min(i + 1, len(pts) - 1)]
            t = (b - a) / np.linalg.norm(b - a)
            n = np.array([-t[1], t[0]]) * bud_dir
            ax.plot([pts[i, 0], pts[i, 0] + 0.45 * n[0]], [pts[i, 1], pts[i, 1] + 0.45 * n[1]], color=P.edge(GB), lw=2.2,
                    solid_capstyle="round", zorder=z + 1)


def arc(c, t0, t1, sx=1.0, sy=1.0, n=60):
    t = np.linspace(t0, t1, n)
    return np.c_[c[0] + RX * sx * np.cos(t), c[1] + RY * sy * np.sin(t)]


cents = [(4.2, 10.0), (13.5, 10.0), (22.8, 10.0), (4.2, 4.2), (13.5, 4.2), (22.8, 4.2)]
titles = ["1  Blastoderm, germ anlage", "2  Amniotic folds", "3  Anatrepsis", "4  Reversed germ band",
          "5  Katatrepsis", "6  Dorsal closure"]
for c, t in zip(cents, titles):
    bio.label(ax, (c[0], c[1] + RY + 0.55), t, size="small", bold=True)

# 1
c = cents[0]
egg(c, serosa=False)
ax.add_patch(Ellipse(c, 2 * RX - 0.22, 2 * RY - 0.22, facecolor="none", edgecolor=P.edge("vesicle"), lw=1.2, zorder=6))
band(arc(c, np.radians(235), np.radians(305), 0.9, 0.86), lw=8)
bio.callout(ax, (c[0], c[1] - RY * 0.85), (c[0] + 2.3, c[1] - 2.5), "Germ anlage", size="tiny")
bio.callout(ax, (c[0] - RX * 0.66, c[1] + RY * 0.62), (c[0] - 3.2, c[1] + 2.0), "Blastoderm", size="tiny")
bio.callout(ax, (c[0] + 0.5, c[1] + 0.4), (c[0] + 2.2, c[1] + 2.0), "Yolk", size="tiny")

# 2
c = cents[1]
egg(c, serosa=False)
g = arc(c, np.radians(232), np.radians(308), 0.88, 0.8)
band(g, lw=8)
ax.add_patch(Ellipse(c, 2 * RX - 0.22, 2 * RY - 0.22, facecolor="none", edgecolor=P.edge(SE), lw=1.1, zorder=6))
for side in (0, -1):
    p = g[side]
    q = g[len(g) // 2 + (-8 if side == 0 else 8)]
    m = (p + q) / 2 + np.array([0, -0.35])
    ax.plot([p[0], m[0], q[0]], [p[1] - 0.05, m[1], q[1] - 0.25], color=P.edge(AM), lw=1.1, zorder=9)
bio.callout(ax, (c[0] - 0.6, c[1] - 1.45), (c[0] - 3.4, c[1] - 2.6), "Amniotic folds", size="tiny")
bio.callout(ax, (c[0] + RX * 0.9, c[1] + 0.3), (c[0] + 3.3, c[1] + 2.0), "Serosa", size="tiny")

# 3 anatrepsis
c = cents[2]
egg(c)
t = np.linspace(0, 1, 60)
pts = np.c_[c[0] - 1.6 + 2.4 * t, c[1] - 1.25 + 1.6 * np.sin(np.pi * t * 0.55) * t]
band(pts, lw=7)
ax.plot(pts[:, 0], pts[:, 1] - 0.32, color=P.edge(AM), lw=1.0, zorder=9)
bio.arrow(ax, (c[0] + 0.3, c[1] - 0.1), (c[0] + 0.9, c[1] + 0.45), kind="process", head=0.15)
bio.callout(ax, (c[0] - 0.4, c[1] - 1.05), (c[0] - 3.4, c[1] - 2.6), "Amnion", size="tiny")
bio.label(ax, (c[0] + 1.6, c[1] - 0.9), "tail first", size="tiny", color=P.muted())

# 4 reversed germ band (ventral side of the embryo faces the dorsal side of the egg)
c = cents[3]
egg(c)
pts = arc(c, np.radians(150), np.radians(30), 0.55, 0.3)
band(pts, lw=8, buds=5, bud_dir=-1)
ax.plot(pts[:, 0], pts[:, 1] + 0.32, color=P.edge(AM), lw=1.0, zorder=9)
bio.callout(ax, (c[0] - 1.0, c[1] + 0.85), (c[0] - 3.4, c[1] + 2.0), "Limb buds (facing egg dorsum)", size="tiny")

# 5 katatrepsis
c = cents[4]
egg(c)
t = np.linspace(-0.2, 1.25, 80)
pts = arc(c, np.pi * (1.0 + 0.0 * t), np.pi, 1, 1)
pts = np.c_[c[0] + RX * 0.82 * np.cos(np.pi / 2 - np.pi * t), c[1] + RY * 0.72 * np.sin(np.pi / 2 - np.pi * t)]
band(pts, lw=7)
bio.arrow(ax, (c[0] - 0.8, c[1] + 1.5), (c[0] + 2.1, c[1] + 1.0), kind="process", bend=-0.2, head=0.16)
bio.arrow(ax, (c[0] + 2.4, c[1] - 0.9), (c[0] - 0.4, c[1] - 1.5), kind="process", bend=-0.2, head=0.16)
bio.label(ax, (c[0] - 0.6, c[1]), "membranes ruptured", size="tiny", color=P.muted())

# 6 dorsal closure
c = cents[5]
egg(c, serosa=False)
body = arc(c, np.radians(195), np.radians(345), 0.88, 0.8)
band(body, lw=12, buds=0)
for x in np.linspace(c[0] - 1.6, c[0] + 0.6, 6):
    ax.plot([x, x - 0.1], [c[1] - RY * 0.62, c[1] - RY * 0.62 - 0.22], color=P.edge(GB), lw=2.0, zorder=9)
side = arc(c, np.radians(195), np.radians(160), 0.88, 0.8)
ax.plot(*arc(c, np.radians(-15), np.radians(195), 0.82, 0.7).T, color=P.edge(GB), lw=2.0, ls=(0, (3, 2)), zorder=7)
ax.add_patch(Ellipse((c[0] + 0.3, c[1] + RY * 0.72), 0.6, 0.35, facecolor=P.fill(SE), edgecolor=P.edge(SE), lw=0.8, zorder=9))
bio.callout(ax, (c[0] + 0.3, c[1] + RY * 0.72), (c[0] + 3.0, c[1] + 2.1), "Dorsal organ (serosa)", size="tiny")
bio.callout(ax, (c[0] - 1.2, c[1] + 1.0), (c[0] - 3.4, c[1] + 2.1), "Body wall closing", size="tiny")
bio.callout(ax, (c[0] - 0.3, c[1] - RY * 0.95), (c[0] - 3.2, c[1] - 2.5), "Legs (ventral)", size="tiny")
for c in cents:
    bio.label(ax, (c[0] - RX - 0.15, c[1]), "A", size="tiny", color=P.muted(), ha="right")
    bio.label(ax, (c[0] + RX + 0.15, c[1]), "P", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (13.5, 0.6), "Egg orientation: anterior (A) left, posterior (P) right, ventral down. Blue: embryo (germ band); green: amnion; red: serosa; orange (1): blastoderm",
          size="tiny", color=P.muted())
