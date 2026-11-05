"""Tracheary elements (schematic, longitudinal views; secondary wall green, primary wall pale). A: a
tracheid: one long cell with tapering, overlapping ends and bordered pits; water passes from tracheid to
tracheid through the pit membranes. B to F: vessel elements with the five patterns of secondary
thickening, in the order in which they mature in an organ: annular (rings), helical (spiral), scalariform
(ladder-like), reticulate (net) and pitted (a continuous wall interrupted by pits). Annular and helical
elements can still be stretched by the growing organ (protoxylem); the others cannot (metaxylem and
secondary xylem). G to I: perforation plates at the end walls joining vessel elements into a vessel:
simple (one large opening, usually transverse), scalariform (several parallel openings, on an oblique end
wall) and foraminate (many small round openings, as in Ephedra).
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(29.0, 12.4)
SW, PW = "plant", "cell_wall"
EC = P.edge(SW)


def title(x, t, sub=None):
    bio.label(ax, (x, 11.75), t, size="small")
    if sub:
        bio.label(ax, (x, 11.25), sub, size="tiny", color=P.muted())


def element(x, w, y0, y1, z=2):
    ax.add_patch(Polygon([(x - w / 2, y0), (x + w / 2, y0), (x + w / 2, y1), (x - w / 2, y1)], closed=True,
                         facecolor=P.light(PW), edgecolor=P.edge(PW), lw=1.0, zorder=z))


Y0, Y1 = 1.4, 10.6
# A tracheid with tapering ends and bordered pits
bio.panel(ax, "A", (0.1, 12.3))
x = 1.8
pts = [(x, Y1), (x + 0.55, Y1 - 1.6), (x + 0.55, Y0 + 1.6), (x, Y0), (x - 0.55, Y0 + 1.6), (x - 0.55, Y1 - 1.6)]
ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(SW), edgecolor=EC, lw=1.1, zorder=3))
for yy in np.arange(Y0 + 1.2, Y1 - 1.0, 0.62):
    ax.add_patch(Ellipse((x, yy), 0.42, 0.34, facecolor=P.light(SW), edgecolor=EC, lw=0.7, zorder=4))
    ax.add_patch(Ellipse((x, yy), 0.1, 0.22, angle=0, facecolor=P.fill("extracellular"), edgecolor=EC, lw=0.5, zorder=5))
title(x, "Tracheid", "bordered pits")

# B-F vessel elements, two elements per column joined by a simple perforation
specs = [("B", 5.0, "Annular"), ("C", 8.0, "Helical"), ("D", 11.0, "Scalariform"), ("E", 14.0, "Reticulate"), ("F", 17.0, "Pitted")]
W = 1.4
for letter, x, name in specs:
    bio.panel(ax, letter, (x - 1.2, 12.3))
    title(x, name)
    ym = (Y0 + Y1) / 2
    for a, b in ((Y0, ym - 0.05), (ym + 0.05, Y1)):
        element(x, W, a, b)
    # rims of the perforation (a simple plate between the two elements)
    for yy in (ym - 0.05, ym + 0.05):
        for s in (-1, 1):
            ax.plot([x + s * W / 2, x + s * W * 0.32], [yy, yy], color=EC, lw=2.0, zorder=5)
    xl, xr = x - W / 2, x + W / 2
    if name == "Annular":
        for yy in np.arange(Y0 + 0.4, Y1 - 0.2, 0.95):
            ax.add_patch(Ellipse((x, yy), W, 0.22, fill=False, edgecolor=EC, lw=2.4, zorder=4))
    elif name == "Helical":
        t = np.linspace(Y0 + 0.1, Y1 - 0.1, 900)
        xs = x + W / 2 * np.sin(2 * math.pi * (t - Y0) / 0.75)
        front = np.cos(2 * math.pi * (t - Y0) / 0.75) > 0
        ax.plot(np.where(front, xs, np.nan), t + 0.12 * np.cos(2 * math.pi * (t - Y0) / 0.75), color=EC, lw=2.4, zorder=4)
    elif name == "Scalariform":
        for yy in np.arange(Y0 + 0.2, Y1 - 0.1, 0.28):
            ax.add_patch(FancyBboxPatch((xl, yy), W, 0.15, boxstyle="round,pad=0,rounding_size=0.05", facecolor=P.fill(SW), edgecolor=EC, lw=0.6, zorder=4))
    elif name == "Reticulate":
        rng = np.random.default_rng(4)
        ax.add_patch(Polygon([(xl, Y0), (xr, Y0), (xr, Y1), (xl, Y1)], closed=True, facecolor=P.fill(SW), edgecolor=EC, lw=0.8, zorder=3.5))
        for yy in np.arange(Y0 + 0.3, Y1 - 0.3, 0.6):
            for xx in np.linspace(xl + 0.25, xr - 0.25, 3):
                xx2 = xx + rng.uniform(-0.08, 0.08)
                ax.add_patch(Ellipse((xx2, yy + rng.uniform(-0.1, 0.1)), 0.32, 0.42, angle=rng.uniform(-30, 30),
                                     facecolor=P.light(PW), edgecolor=EC, lw=0.6, zorder=4))
    else:  # pitted
        ax.add_patch(Polygon([(xl, Y0), (xr, Y0), (xr, Y1), (xl, Y1)], closed=True, facecolor=P.fill(SW), edgecolor=EC, lw=0.8, zorder=3.5))
        for j, yy in enumerate(np.arange(Y0 + 0.3, Y1 - 0.2, 0.36)):
            for xx in np.linspace(xl + 0.25, xr - 0.25, 4)[(j % 2):: 1][:3 + (j % 2 == 0)]:
                xx2 = xx + (0.1 if j % 2 else 0)
                if xx2 > xr - 0.18:
                    continue
                ax.add_patch(Ellipse((xx2, yy), 0.26, 0.2, facecolor=P.light(SW), edgecolor=EC, lw=0.5, zorder=4))
                ax.add_patch(Ellipse((xx2, yy), 0.13, 0.06, facecolor=P.fill("extracellular"), edgecolor="none", zorder=5))
    # the earlier types cover the pale primary wall only partly
bio.label(ax, (6.5, 0.7), "protoxylem: extensible", size="tiny", color=P.muted())
bio.label(ax, (14.0, 0.7), "metaxylem and secondary xylem", size="tiny", color=P.muted())
ax.plot([4.2, 8.8], [1.05, 1.05], color=P.muted(), lw=0.8, zorder=2)
ax.plot([10.2, 17.8], [1.05, 1.05], color=P.muted(), lw=0.8, zorder=2)
bio.callout(ax, (17.0 + 0.5, 6.0), (18.6, 4.0), "Simple perforation", size="tiny")

# G-I perforation plates
bio.panel(ax, "G", (19.6, 12.3))
bio.label(ax, (24.5, 11.75), "Perforation plates", size="small")
xs_ = (21.2, 24.5, 27.8)
names = ("simple", "scalariform", "foraminate")
for x, nm in zip(xs_, names):
    yb, yt = 3.0, 9.0
    if nm == "scalariform":
        ya, yb2 = 5.0, 7.0      # oblique end wall
    else:
        ya, yb2 = 5.9, 6.1
    lower = [(x - 1.0, yb), (x + 1.0, yb), (x + 1.0, ya), (x - 1.0, yb2)]
    upper = [(x - 1.0, yb2 + 0.1), (x + 1.0, ya + 0.1), (x + 1.0, yt), (x - 1.0, yt)]
    for poly in (lower, upper):
        ax.add_patch(Polygon(poly, closed=True, facecolor=P.fill(SW), edgecolor=EC, lw=1.0, zorder=3))
    # face of the end wall seen obliquely: an ellipse with the openings
    cy = (ya + yb2) / 2 + 0.05
    if nm == "simple":
        ax.add_patch(Ellipse((x, cy), 2.0, 0.9, facecolor=P.fill(SW), edgecolor=EC, lw=1.0, zorder=4))
        ax.add_patch(Ellipse((x, cy), 1.6, 0.66, facecolor=P.fill("extracellular"), edgecolor=EC, lw=0.8, zorder=5))
    elif nm == "scalariform":
        plate = [(x - 1.0, yb2), (x + 1.0, ya), (x + 1.0, ya + 0.1), (x - 1.0, yb2 + 0.1)]
        ang = math.degrees(math.atan2(ya - yb2, 2.0))
        ax.add_patch(Ellipse((x, cy), 2.3, 1.1, angle=ang, facecolor=P.fill(SW), edgecolor=EC, lw=1.0, zorder=4))
        for k in np.linspace(-0.85, 0.85, 7):
            p = np.array([x, cy]) + k * np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            ax.add_patch(Ellipse(p, 0.16, 0.8, angle=ang, facecolor=P.fill("extracellular"), edgecolor=EC, lw=0.5, zorder=5))
    else:
        ax.add_patch(Ellipse((x, cy), 2.0, 0.9, facecolor=P.fill(SW), edgecolor=EC, lw=1.0, zorder=4))
        rng = np.random.default_rng(5)
        for k in range(14):
            a = rng.uniform(0, 2 * math.pi)
            r = math.sqrt(rng.uniform(0, 1))
            ax.add_patch(Circle((x + 0.75 * r * math.cos(a), cy + 0.3 * r * math.sin(a)), 0.07, facecolor=P.fill("extracellular"), edgecolor=EC, lw=0.4, zorder=5))
    bio.label(ax, (x, 2.3), nm, size="tiny")
bio.label(ax, (27.8, 1.75), "(Ephedra)", size="tiny", italic=True, color=P.muted())
bio.label(ax, (24.5, 1.75), "oblique end wall", size="tiny", color=P.muted())
bio.label(ax, (21.2, 1.75), "transverse end wall", size="tiny", color=P.muted())
