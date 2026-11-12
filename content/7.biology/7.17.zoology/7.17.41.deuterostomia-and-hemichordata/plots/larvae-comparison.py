# Tornaria (Enteropneusta) and bipinnaria (Asteroidea), schematic ventral views: one looped
# circumoral ciliary band around the mouth field, a through-gut and an anterior coelom with a hydropore.
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon, Ellipse

P = bio.P
fig, ax = bio.canvas(22.0, 10.0)
CIL = P.edge("positive")


def outline(c, rx, ry, k=0, a=0.0, phase=0.0, n=400):
    t = np.linspace(0, 2 * np.pi, n)
    r = 1 + a * np.cos(k * t + phase)
    return np.c_[c[0] + rx * r * np.cos(t), c[1] + ry * r * np.sin(t)]


def body(pts, token="ectoderm", z=3):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.light(token), edgecolor=P.edge(token), lw=1.0, zorder=z))


def band(pts, lw=2.6, z=8):
    ax.plot(pts[:, 0], pts[:, 1], color=CIL, lw=lw, zorder=z, solid_capstyle="round")


def gut(cx, cy, z=5):
    # oesophagus from the mouth, stomach, intestine to the anus at the posterior pole
    ax.add_patch(Polygon(np.r_[[(cx - 0.18, cy - 0.3), (cx - 0.12, cy + 0.6), (cx + 0.12, cy + 0.6), (cx + 0.18, cy - 0.3)]],
                         closed=True, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8, zorder=z))
    ax.add_patch(Ellipse((cx, cy + 0.95), 1.3, 1.0, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8, zorder=z))
    t = np.linspace(0, 1, 40)
    path = np.c_[cx + 0.45 + 0.35 * np.sin(np.pi * t) - 0.45 * t, cy + 0.6 - 2.55 * t]
    ax.plot(path[:, 0], path[:, 1], color=P.edge("endoderm"), lw=5.0, zorder=z - 0.2, solid_capstyle="round")
    ax.plot(path[:, 0], path[:, 1], color=P.fill("endoderm"), lw=3.4, zorder=z - 0.1, solid_capstyle="round")


# ---------------------------------------------------------------- A: tornaria
bio.panel(ax, "A", (0.3, 9.7))
bio.label(ax, (5.0, 9.4), "Tornaria (acorn worm)", size="normal", bold=True)
cx, cy = 5.0, 4.6
body(outline((cx, cy), 3.0, 3.6))
loop = outline((cx, cy + 0.4), 2.4, 2.6, k=8, a=0.09, phase=np.pi / 2)
band(loop)
ax.add_patch(Ellipse((cx, cy - 2.85), 4.6, 0.5, facecolor="none", edgecolor=CIL, lw=4.0, zorder=7))  # telotroch
gut(cx, cy - 0.6)
ax.add_patch(Ellipse((cx, cy - 0.65), 0.55, 0.32, facecolor=P.surface(), edgecolor=P.edge("endoderm"), lw=0.9, zorder=9))
ax.add_patch(Ellipse((cx + 0.15, cy + 1.75), 0.9, 0.55, facecolor=P.fill("coelom"), edgecolor=P.edge("coelom"), lw=0.8, zorder=6))
ax.plot([cx + 0.45, cx + 1.0, cx + 1.25], [cy + 1.9, cy + 2.7, cy + 3.15], color=P.edge("coelom"), lw=1.0, zorder=6)
ax.add_patch(Ellipse((cx, cy + 3.45), 0.8, 0.35, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=8))
for dx in (-0.2, 0.2):
    ax.add_patch(Ellipse((cx + dx, cy + 3.45), 0.13, 0.13, facecolor=P.ink(), edgecolor="none", zorder=9))
ax.plot([cx, cx], [cy + 3.6, cy + 4.1], color=P.muted(), lw=0.9, zorder=8)
C = bio.callout
C(ax, (cx, cy + 3.5), (1.3, 9.0), "Apical plate, eyespots")
C(ax, (cx - 2.4, cy + 0.9), (0.4, 6.6), "Circumoral band")
C(ax, (cx, cy - 0.65), (0.4, 3.2), "Mouth")
C(ax, (cx - 0.5, cy + 0.4), (0.8, 4.9), "Stomach")
C(ax, (cx + 0.15, cy + 1.75), (9.4, 7.2), "Protocoel")
C(ax, (cx + 1.25, cy + 3.15), (9.0, 8.6), "Hydropore")
C(ax, (cx + 2.2, cy - 2.85), (9.3, 1.6), "Telotroch")
C(ax, (cx, cy - 2.55), (5.0, 0.3), "Anus")

# ---------------------------------------------------------------- B: bipinnaria
bio.panel(ax, "B", (11.6, 9.7))
bio.label(ax, (16.6, 9.4), "Bipinnaria (sea star)", size="normal", bold=True)
cx, cy = 16.6, 4.6
body(outline((cx, cy), 3.0, 3.6, k=6, a=0.14, phase=np.pi / 2))
pre = outline((cx, cy + 2.7), 1.3, 0.6, k=4, a=0.12)
band(pre)
post = outline((cx, cy - 0.45), 2.5, 2.0, k=6, a=0.12, phase=np.pi / 2)
band(post)
gut(cx, cy - 0.6)
ax.add_patch(Ellipse((cx, cy - 0.65), 0.55, 0.32, facecolor=P.surface(), edgecolor=P.edge("endoderm"), lw=0.9, zorder=9))
for sgn in (-1, 1):
    ax.add_patch(Ellipse((cx + sgn * 0.95, cy + 0.35), 0.5, 1.2, angle=sgn * 15, facecolor=P.fill("coelom"),
                         edgecolor=P.edge("coelom"), lw=0.8, zorder=6))
ax.plot([cx - 0.95, cx - 1.2, cx - 1.35], [cy + 0.95, cy + 1.5, cy + 2.0], color=P.edge("coelom"), lw=1.0, zorder=6)
C(ax, (cx, cy + 3.3), (12.4, 9.0), "Preoral loop")
C(ax, (cx + 2.4, cy - 0.9), (21.4, 3.4), "Postoral band")
C(ax, (cx, cy - 0.65), (21.4, 2.0), "Mouth")
C(ax, (cx + 0.95, cy + 0.35), (21.2, 6.4), "Coelomic sacs")
C(ax, (cx - 1.35, cy + 2.0), (12.2, 7.4), "Hydropore")
C(ax, (cx, cy - 2.55), (16.6, 0.3), "Anus")
C(ax, (cx - 0.6, cy + 0.4), (12.2, 4.6), "Stomach")
