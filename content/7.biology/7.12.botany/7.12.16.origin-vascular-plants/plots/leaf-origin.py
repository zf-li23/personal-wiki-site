"""Origin of microphylls and megaphylls (schematic). Top: longitudinal sections of a stem with (A) a
microphyll on a protostele (no leaf gap, one vein) and (B) a megaphyll on a siphonostele (leaf gap above
the trace, branched veins). Bottom: (C) the enation theory, (D) the sterilization theory and (E) the
telome theory of the megaphyll."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(31, 17)
XF, XE = P.fill("xylem"), P.edge("xylem")
GF, GE = P.mix(P.surface(), P.fill("parenchyma"), 0.35), P.edge("parenchyma")
LF, LE = P.mix(P.surface(), P.fill("plant"), 0.45), P.edge("plant")
SP, SPE = P.fill("animal"), P.edge("animal")


def rect(x, y, w, h, fc, ec, z=3):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=0.8, zorder=z))


def poly(pts, fc, ec, z=4, lw=0.8):
    ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, lw=lw, zorder=z, joinstyle="round"))


def line(p, q, c, w=1.2, z=6):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=w, zorder=z, solid_capstyle="round")


# ---- A microphyll
bio.panel(ax, "A", (0.3, 16.8)); bio.label(ax, (4.6, 16.4), "Microphyll: protostele, no leaf gap", size="normal", bold=True)
x0 = 3.0
rect(x0, 9.4, 2.4, 6.2, GF, GE)
rect(x0 + 0.85, 9.4, 0.7, 6.2, XF, XE, z=4)
poly([(x0 + 2.4, 12.0), (x0 + 5.0, 13.6), (x0 + 5.2, 13.9), (x0 + 2.4, 12.8)], LF, LE)
line((x0 + 1.55, 11.6), (x0 + 2.4, 12.35), XE, 1.6)
line((x0 + 2.4, 12.35), (x0 + 5.0, 13.7), XE, 1.2)
bio.callout(ax, (x0 + 3.6, 13.05), (x0 + 5.6, 11.4), "single vein")
bio.callout(ax, (x0 + 1.2, 14.6), (x0 - 1.5, 14.9), "protostele")
bio.callout(ax, (x0 + 1.6, 11.7), (x0 - 1.5, 11.0), "leaf trace, no gap")

# ---- B megaphyll
bio.panel(ax, "B", (13.0, 16.8)); bio.label(ax, (19.0, 16.4), "Megaphyll: siphonostele with a leaf gap", size="normal", bold=True)
x0 = 15.6
rect(x0, 9.4, 3.0, 6.2, GF, GE)
rect(x0 + 0.5, 9.4, 0.45, 6.2, XF, XE, z=4)
rect(x0 + 2.05, 9.4, 0.45, 2.6, XF, XE, z=4)
rect(x0 + 2.05, 13.6, 0.45, 2.0, XF, XE, z=4)
bio.callout(ax, (x0 + 2.27, 12.9), (x0 - 1.6, 13.4), "leaf gap (parenchyma)")
bio.callout(ax, (x0 + 1.5, 15.0), (x0 - 1.6, 15.3), "pith")
poly([(x0 + 3.0, 11.9), (x0 + 5.0, 12.2), (x0 + 8.0, 14.6), (x0 + 8.4, 15.6), (x0 + 6.0, 15.4), (x0 + 3.0, 12.9)], LF, LE)
line((x0 + 2.5, 11.9), (x0 + 3.6, 12.4), XE, 1.6)
for a, L in ((22, 4.2), (35, 3.6), (48, 3.0)):
    q = (x0 + 3.6 + L * np.cos(np.radians(a)), 12.4 + L * np.sin(np.radians(a)))
    line((x0 + 3.6, 12.4), q, XE, 1.0)
    line(q, (q[0] + 0.6 * np.cos(np.radians(a + 20)), q[1] + 0.6 * np.sin(np.radians(a + 20))), XE, 0.7)
    line(q, (q[0] + 0.6 * np.cos(np.radians(a - 20)), q[1] + 0.6 * np.sin(np.radians(a - 20))), XE, 0.7)
bio.callout(ax, (x0 + 6.6, 14.0), (x0 + 9.4, 12.2), "branched veins")

ax.plot([0.3, 30.7], [8.6, 8.6], color=P.muted(), lw=0.5, ls=(0, (3, 3)))


def axis(x, y0, y1, w=0.5):
    rect(x - w / 2, y0, w, y1 - y0, GF, GE, z=3)
    rect(x - 0.08, y0, 0.16, y1 - y0, XF, XE, z=4)


# ---- C enation
bio.panel(ax, "C", (0.3, 8.2)); bio.label(ax, (5.2, 7.8), "Enation theory", size="normal", bold=True)
for i, (stage, t) in enumerate([(0, "spine-like enation"), (1, "trace to base\n(Asteroxylon)"), (2, "vein in the leaf\n(Baragwanathia)")]):
    x = 1.6 + i * 3.4
    axis(x, 1.6, 6.6)
    for y in (2.6, 4.3, 6.0):
        poly([(x + 0.25, y - 0.2), (x + 1.5, y + 0.35), (x + 0.25, y + 0.2)], LF, LE)
        if stage >= 1:
            line((x + 0.05, y - 0.35), (x + 0.25, y), XE, 1.0)
        if stage == 2:
            line((x + 0.25, y), (x + 1.35, y + 0.3), XE, 0.9)
    bio.label(ax, (x + 0.5, 0.9), t, size="tiny")
    if i < 2:
        bio.arrow(ax, (x + 1.8, 4.3), (x + 2.9, 4.3), kind="process", color=P.muted())

# ---- D sterilization
bio.panel(ax, "D", (11.2, 8.2)); bio.label(ax, (15.6, 7.8), "Sterilization theory", size="normal", bold=True)
for i in range(2):
    x = 12.6 + i * 4.4
    axis(x, 1.6, 6.6)
    for k, y in enumerate((2.4, 3.6, 4.8, 6.0)):
        s = 1 if k % 2 == 0 else -1
        if i == 0 or k % 2 == 1:
            line((x, y), (x + s * 0.5, y + 0.2), LE, 1.0)
            ax.add_patch(Ellipse((x + s * 0.78, y + 0.28), 0.55, 0.38, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=6))
        else:
            poly([(x + s * 0.25, y - 0.15), (x + s * 1.6, y + 0.45), (x + s * 0.25, y + 0.15)], LF, LE)
    bio.label(ax, (x, 0.9), ["lateral sporangia\n(zosterophylls)", "some sporangia\nbecome leaves"][i], size="tiny")
bio.arrow(ax, (14.0, 4.3), (16.0, 4.3), kind="process", color=P.muted())

# ---- E telome theory of the megaphyll
bio.panel(ax, "E", (20.6, 8.2)); bio.label(ax, (25.6, 7.8), "Telome theory of the megaphyll", size="normal", bold=True)


def dich(p, ang, L, d, w, tips):
    q = (p[0] + L * np.cos(np.radians(ang)), p[1] + L * np.sin(np.radians(ang)))
    line(p, q, LE, w, z=5)
    if d == 0:
        tips.append(q)
        return
    for s in (-1, 1):
        dich(q, ang + s * 24, L * 0.75, d - 1, max(0.7, w * 0.8), tips)


labels = ["side branch system", "overtopped, planated", "webbed: lamina"]
for i in range(3):
    x = 21.6 + i * 3.2
    tips = []
    if i == 0:
        for s in (-1, 1):
            dich((x, 1.8), 90 + s * 10, 1.4, 3, 1.4, tips)
        line((x, 1.6), (x, 1.8), LE, 1.4)
    else:
        dich((x, 1.8), 72, 1.4, 3, 1.4, tips)
        if i == 2:
            b = np.array([x, 1.8])
            tips = sorted(tips, key=lambda q: np.arctan2(q[1] - b[1], q[0] - b[0]))
            poly(np.array([b] + [np.array(q) for q in tips]), LF, LE, z=3)
    bio.label(ax, (x + 0.5, 0.9), labels[i], size="tiny")
    if i < 2:
        bio.arrow(ax, (x + 1.5, 2.4), (x + 2.5, 2.4), kind="process", color=P.muted())
