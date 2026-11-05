"""Sieve tubes and companion cells of an angiosperm (schematic). A: longitudinal section. Mature
sieve-tube elements are living but have lost their nucleus, vacuole and most organelles; a parietal layer
of cytoplasm keeps mitochondria, plastids and smooth ER, and P-protein lies along the walls. The end walls
are sieve plates whose pores are lined with callose; sieve areas on the side walls connect the element
with its companion cell, a narrow cell with a large nucleus and dense cytoplasm that arose from the same
mother cell. B: an injured or dormant sieve tube: P-protein is swept against the sieve plate and callose
builds up into a pad (callus) that closes the pores. C: transverse section: the sieve plate in face view,
with the companion cell beside it. D: a compound sieve plate (several sieve areas on an oblique end
wall), as in many woody plants. E: ontogeny: an unequal longitudinal division of one mother cell gives the
sieve-tube element and its companion cell(s).
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 12.6)
WALL, CC, PP, CAL = "cell_wall", "nucleus", "protein", "carbohydrate"


def rect(x0, y0, x1, y1, tk, lw=1.0, z=2):
    ax.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], closed=True, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=lw, zorder=z))


def sieve_plate(x0, x1, y, pores=5, callus=False, z=5):
    w = (x1 - x0)
    ax.plot([x0, x1], [y, y], color=P.edge(WALL), lw=3.2, zorder=z)
    for k in range(pores):
        xx = x0 + (k + 0.5) * w / pores
        ax.add_patch(Polygon([(xx - 0.09, y - 0.09), (xx + 0.09, y - 0.09), (xx + 0.09, y + 0.09), (xx - 0.09, y + 0.09)], closed=True,
                             facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=z + 0.1))
        for s in (-1, 1):
            ax.plot([xx + s * 0.11, xx + s * 0.11], [y - 0.13, y + 0.13], color=P.edge(CAL), lw=1.6, zorder=z + 0.2)
    if callus:
        ax.add_patch(Ellipse(((x0 + x1) / 2, y + 0.18), w * 0.95, 0.38, facecolor=P.fill(CAL), edgecolor=P.edge(CAL), lw=0.9, zorder=z + 0.3))
        ax.add_patch(Ellipse(((x0 + x1) / 2, y - 0.18), w * 0.95, 0.38, facecolor=P.fill(CAL), edgecolor=P.edge(CAL), lw=0.9, zorder=z + 0.3))


def sieve_element(x0, x1, y0, y1, injured=False):
    rect(x0, y0, x1, y1, WALL, z=2)
    rect(x0 + 0.12, y0 + 0.06, x1 - 0.12, y1 - 0.06, "cytoplasm", lw=0.6, z=3)
    # parietal cytoplasm: plastids and mitochondria along the walls; P-protein strands
    rng = np.random.default_rng(int(x0 * 10 + y0))
    for yy in np.linspace(y0 + 0.4, y1 - 0.4, 4):
        for xx in (x0 + 0.25, x1 - 0.25):
            ax.add_patch(Circle((xx, yy + rng.uniform(-0.1, 0.1)), 0.09, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.5, zorder=4))
    if not injured:
        for xx in (x0 + 0.42, x1 - 0.42):
            t = np.linspace(y0 + 0.3, y1 - 0.3, 40)
            ax.plot(xx + 0.05 * np.sin(t * 7), t, color=P.edge(PP), lw=1.0, zorder=4)


# ---------------- A: longitudinal section
bio.panel(ax, "A", (0.1, 12.5))
bio.label(ax, (0.8, 12.45), "Longitudinal", size="small", ha="left", va="top")
X0, X1 = 1.6, 3.6
ys = (1.0, 4.6, 8.2, 11.8)
for a, b in zip(ys, ys[1:]):
    sieve_element(X0, X1, a, b)
for y in ys[1:-1]:
    sieve_plate(X0 + 0.12, X1 - 0.12, y)
# companion cells beside each element
for a, b in zip(ys, ys[1:]):
    rect(X1, a + 0.15, X1 + 0.75, b - 0.15, WALL, z=2)
    rect(X1 + 0.08, a + 0.22, X1 + 0.67, b - 0.22, CC, lw=0.6, z=3)
    ax.add_patch(Ellipse((X1 + 0.375, (a + b) / 2), 0.42, 0.9, facecolor=P.edge(CC), edgecolor="none", zorder=4))
    # sieve areas / branched plasmodesmata in the common wall
    for yy in np.linspace(a + 0.6, b - 0.6, 4):
        ax.plot([X1 - 0.06, X1 + 0.1], [yy, yy], color=P.edge("membrane"), lw=1.0, zorder=5)
bio.callout(ax, (2.6, ys[1]), (6.0, 7.3), "Sieve plate (pores lined with callose)", size="tiny")
bio.callout(ax, (X0 + 0.25, 9.6), (6.0, 11.2), "Plastid, mitochondria (parietal)", size="tiny")
bio.callout(ax, (X0 + 0.42, 6.4), (6.0, 6.4), "P-protein", size="tiny")
bio.callout(ax, (X1 + 0.375, 10.0), (6.0, 10.3), "Companion cell (nucleus)", size="tiny")
bio.callout(ax, (X1 + 0.02, 2.8), (6.0, 2.4), "Plasmodesmata / sieve areas", size="tiny")
bio.callout(ax, (2.6, 3.0), (6.0, 1.4), "Sieve-tube element (no nucleus)", size="tiny")

# ---------------- B: injured: callus and P-protein plug
bio.panel(ax, "B", (11.6, 12.5))
bio.label(ax, (12.3, 12.45), "Injured", size="small", ha="left", va="top")
X0b, X1b = 12.4, 14.4
sieve_element(X0b, X1b, 4.6, 8.2, injured=True)
sieve_element(X0b, X1b, 8.2, 11.8, injured=True)
sieve_plate(X0b + 0.12, X1b - 0.12, 8.2, callus=True)
plug = Polygon([(X0b + 0.3, 8.6), (X1b - 0.3, 8.6), (X1b - 0.6, 10.2), (X0b + 0.6, 10.2)], closed=True,
               facecolor=P.fill(PP), edgecolor=P.edge(PP), lw=0.8, zorder=6)
ax.add_patch(plug)
bio.callout(ax, ((X0b + X1b) / 2, 9.6), (16.6, 10.6), "P-protein plug", size="tiny")
bio.callout(ax, (X1b - 0.4, 8.0), (16.6, 7.8), "Callose pad (callus)", size="tiny")

# ---------------- C: transverse section, sieve plate in face view
bio.panel(ax, "C", (11.6, 4.3))
bio.label(ax, (12.3, 4.25), "Transverse", size="small", ha="left", va="top")
c = np.array([13.6, 1.9])
hexa = [c + 1.25 * np.array([math.cos(math.radians(60 * k)), math.sin(math.radians(60 * k))]) for k in range(6)]
ax.add_patch(Polygon(hexa, closed=True, facecolor=P.fill(WALL), edgecolor=P.edge(WALL), lw=1.0, zorder=2))
ax.add_patch(Polygon([c + (h - c) * 0.88 for h in hexa], closed=True, facecolor=P.light(WALL), edgecolor=P.edge(WALL), lw=0.6, zorder=3))
for r_, n in ((0.0, 1), (0.42, 6), (0.8, 10)):
    for k in range(n):
        a = 2 * math.pi * k / max(n, 1) + 0.3
        p = c + r_ * np.array([math.cos(a), math.sin(a)])
        ax.add_patch(Circle(p, 0.13, facecolor=P.fill(CAL), edgecolor=P.edge(CAL), lw=0.6, zorder=4))
        ax.add_patch(Circle(p, 0.07, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=5))
cc = c + np.array([1.55, -0.7])
ax.add_patch(Ellipse(cc, 0.75, 0.6, facecolor=P.fill(CC), edgecolor=P.edge(WALL), lw=1.0, zorder=3))
ax.add_patch(Circle(cc, 0.16, facecolor=P.edge(CC), edgecolor="none", zorder=4))
bio.callout(ax, c + np.array([0.42, 0.0]), (16.6, 3.4), "Sieve pore", size="tiny")
bio.callout(ax, cc, (16.6, 0.6), "Companion cell", size="tiny")

# ---------------- D: compound sieve plate
bio.panel(ax, "D", (19.0, 12.5))
bio.label(ax, (19.7, 12.45), "Compound plate", size="small", ha="left", va="top")
x0, x1 = 20.0, 22.0
ax.add_patch(Polygon([(x0, 5.5), (x1, 5.5), (x1, 8.6), (x0, 10.6)], closed=True, facecolor=P.light(WALL), edgecolor=P.edge(WALL), lw=1.0, zorder=2))
ax.add_patch(Polygon([(x0, 10.75), (x1, 8.75), (x1, 11.8), (x0, 11.8)], closed=True, facecolor=P.light(WALL), edgecolor=P.edge(WALL), lw=1.0, zorder=2))
for k in range(5):
    t = (k + 0.5) / 5
    p = np.array([x0, 10.68]) + t * np.array([x1 - x0, 8.68 - 10.68])
    ax.add_patch(Ellipse(p, 0.5, 0.3, angle=-45, facecolor=P.fill(CAL), edgecolor=P.edge(CAL), lw=0.6, zorder=4))
    for d in (-0.1, 0.1):
        ax.add_patch(Circle(p + np.array([d, d * -1]), 0.035, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=5))
bio.callout(ax, (x0 + 1.0, 9.68), (23.0, 10.9), "Sieve areas", size="tiny")
bio.label(ax, (21.0, 4.9), "oblique end wall", size="tiny", color=P.muted())

# ---------------- E: ontogeny
bio.panel(ax, "E", (19.0, 4.3))
bio.label(ax, (19.7, 4.25), "Origin", size="small", ha="left", va="top")
for i, (x, split) in enumerate(((20.2, False), (22.4, True), (24.8, True))):
    rect(x, 0.6, x + 1.3, 3.4, WALL, z=2)
    if split:
        ax.plot([x + 0.95, x + 0.95], [0.6, 3.4], color=P.edge(WALL), lw=1.4, zorder=4)
        rect(x + 0.98, 0.68, x + 1.25, 3.32, CC, lw=0.5, z=3)
        ax.add_patch(Ellipse((x + 1.11, 2.0), 0.16, 0.45, facecolor=P.edge(CC), edgecolor="none", zorder=4))
        if i == 2:
            ax.add_patch(Circle((x + 0.47, 2.0), 0.0001, color="none"))
        else:
            ax.add_patch(Ellipse((x + 0.47, 2.0), 0.4, 0.55, facecolor=P.fill(CC), edgecolor=P.edge(CC), lw=0.6, zorder=4))
    else:
        ax.add_patch(Ellipse((x + 0.65, 2.0), 0.5, 0.65, facecolor=P.fill(CC), edgecolor=P.edge(CC), lw=0.6, zorder=4))
    if i < 2:
        bio.arrow(ax, (x + 1.45, 2.0), (x + 2.05 if i == 0 else x + 2.25, 2.0), kind="process")
bio.label(ax, (20.85, 0.15), "mother cell", size="tiny", color=P.muted())
bio.label(ax, (23.05, 0.15), "unequal division", size="tiny", color=P.muted())
bio.label(ax, (25.45, 0.15), "nucleus lost", size="tiny", color=P.muted())
