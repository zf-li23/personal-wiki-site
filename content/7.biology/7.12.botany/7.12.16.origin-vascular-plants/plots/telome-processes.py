"""Zimmermann's telome theory: the five elementary processes (schematic). Green: sterile telomes; orange:
sporangia. A: the ancestral, equally dichotomous axis. B: overtopping. C: planation. D: syngenesis
(webbing): a lamina with dichotomous veins. E: reduction to a single-veined appendage. F: recurvation of a
fertile telome truss, giving an Equisetum-like sporangiophore."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33, 11.5)
AXE, AXF = P.edge("plant"), P.fill("plant")
SP, SPE = P.fill("animal"), P.edge("animal")


def seg(p, q, w, color=None, ls="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color or AXE, lw=w, solid_capstyle="round", zorder=5, ls=ls)


def spor(q, ang):
    ax.add_patch(Ellipse((q[0] + 0.25 * np.cos(np.radians(ang)), q[1] + 0.25 * np.sin(np.radians(ang))), 0.55, 0.24, angle=ang,
                         facecolor=SP, edgecolor=SPE, lw=0.8, zorder=7))


def dich(p, ang, L, depth, w, spread, fertile=False, tips=None, shrink=0.75, color=None):
    a = np.radians(ang)
    q = (p[0] + L * np.cos(a), p[1] + L * np.sin(a))
    seg(p, q, w, color)
    if depth == 0:
        if fertile:
            spor(q, ang)
        if tips is not None:
            tips.append(q)
        return
    for s in (-1, 1):
        dich(q, ang + s * spread, L * shrink, depth - 1, max(0.8, w * 0.75), spread, fertile, tips, shrink, color)


def head(x, letter, t):
    bio.panel(ax, letter, (x - 2.6, 11.2))
    bio.label(ax, (x, 10.7), t, size="normal", bold=True)


xs = [2.8, 8.2, 13.6, 19.0, 24.4, 29.8]
BASE = 1.0
# A ancestral
x = xs[0]; head(x, "A", "Ancestral axis")
dich((x, BASE), 90, 2.4, 3, 2.6, 22, fertile=True)
bio.label(ax, (x, 0.4), "equal dichotomy; terminal sporangia", size="tiny", color=P.muted())

# B overtopping
x = xs[1]; head(x, "B", "Overtopping")
seg((x, BASE), (x, BASE + 8.4), 2.6)
for k, y in enumerate((2.4, 4.6, 6.8)):
    s = 1 if k % 2 == 0 else -1
    dich((x, BASE + y), 90 - s * 50, 1.0, 2, 1.6, 30, shrink=0.8)
bio.label(ax, (x, 0.4), "main axis and side branches", size="tiny", color=P.muted())

# C planation: side systems drawn in one plane (fan); out-of-plane parts in B are now flat
x = xs[2]; head(x, "C", "Planation")
seg((x - 1.2, BASE), (x - 1.2, BASE + 8.4), 2.6)
dich((x - 1.2, BASE + 3.0), 50, 1.5, 3, 1.6, 24, shrink=0.78)
dich((x - 1.2, BASE + 6.0), 55, 1.2, 3, 1.4, 24, shrink=0.78)
bio.label(ax, (x, 0.4), "side branch system in one plane", size="tiny", color=P.muted())

# D webbing
x = xs[3]; head(x, "D", "Syngenesis (webbing)")
seg((x - 1.2, BASE), (x - 1.2, BASE + 8.4), 2.6)
for y0, L in ((2.4, 1.25), (5.8, 1.05)):
    tips = []
    dich((x - 1.2, BASE + y0), 52, L, 3, 1.3, 24, tips=tips, shrink=0.78)
    b = np.array([x - 1.2, BASE + y0])
    tips = sorted(tips, key=lambda q: np.arctan2(q[1] - b[1], q[0] - b[0]))
    a = np.radians(52)
    pts = [b + 0.6 * L * np.array([np.cos(a - 0.5), np.sin(a - 0.5)])]
    pts += [np.array(q) + 0.12 * (np.array(q) - b) / np.linalg.norm(np.array(q) - b) for q in tips]
    pts += [b + 0.6 * L * np.array([np.cos(a + 0.5), np.sin(a + 0.5)])]
    pts = np.array([b] + pts)
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.mix(P.surface(), P.fill("plant"), 0.45), edgecolor=AXE, lw=1.0, zorder=3, joinstyle="round"))
bio.label(ax, (x, 0.4), "lamina between the telomes: a megaphyll", size="tiny", color=P.muted())

# E reduction
x = xs[4]; head(x, "E", "Reduction")
seg((x, BASE), (x, BASE + 8.4), 2.6)
for k, y in enumerate(np.linspace(2.0, 8.0, 7)):
    s = 1 if k % 2 == 0 else -1
    yy = BASE + y
    ax.add_patch(Polygon([(x, yy - 0.15), (x + s * 1.1, yy + 0.5), (x + s * 1.2, yy + 0.62), (x + s * 1.0, yy + 0.55), (x, yy + 0.15)],
                         closed=True, facecolor=P.mix(P.surface(), P.fill("plant"), 0.45), edgecolor=AXE, lw=0.8, zorder=4))
    seg((x, yy), (x + s * 1.05, yy + 0.52), 0.8)
bio.label(ax, (x, 0.4), "one telome left: single-veined leaf", size="tiny", color=P.muted())

# F recurvation
x = xs[5]; head(x, "F", "Recurvation")
seg((x, BASE), (x, BASE + 8.4), 2.6)
for y in (3.0, 6.0):
    yy = BASE + y
    stalk = (x + 1.2, yy)
    seg((x, yy), stalk, 1.6)
    seg((stalk[0], stalk[1] - 1.1), (stalk[0], stalk[1] + 1.1), 1.8)  # peltate shield in side view
    for s in (-1, 1):
        t = np.linspace(0, np.pi * 0.9, 20)
        cx, cy = stalk[0], stalk[1] + s * 1.1
        arc = np.c_[cx + 0.0 * t, cy + 0 * t]
        q = (cx - 0.55, cy - s * 0.25)
        seg((cx, cy), (cx - 0.3, cy + s * 0.25), 1.2)
        seg((cx - 0.3, cy + s * 0.25), q, 1.2)
        spor(q, 180 + s * 30)
bio.arrow(ax, (x + 1.8, BASE + 7.6), (x + 1.35, BASE + 6.9), kind="process")
bio.label(ax, (x + 1.85, BASE + 7.9), "sporangia point to the axis", size="tiny", ha="center")
bio.label(ax, (x, 0.4), "Equisetum-like sporangiophore", size="tiny", color=P.muted())

