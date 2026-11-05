"""Embryo development in shepherd's purse (Capsella bursa-pastoris), schematic, micropylar end down.
A two-celled stage (small apical cell, large vacuolate basal cell); B quadrant stage on a filament of
suspensor cells; C octant (two tiers of four cells); D globular embryo with protoderm and the hypophysis
at the top of the suspensor; E heart stage with two cotyledon primordia, the shoot apex between them and
procambium inside; F torpedo stage; G mature embryo curved like a horseshoe, suspensor degenerated.
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(31.0, 8.4)
EMB, COT, SUS, HYP, SAM = "carbohydrate", "plant", "neutral", "positive", "highlight"


def patch(pts, tok, lw=0.9, z=6, fill=None):
    pts = np.asarray(pts, float)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fill or P.fill(tok),
                           edgecolor=P.edge(tok), lw=lw, joinstyle="round", zorder=z))


def tube(points, w0, w1=None, n=80):
    """Closed outline around a smooth centre line with a width tapering from w0 to w1."""
    p = np.asarray(points, float)
    t = np.linspace(0, 1, len(p))
    s = np.linspace(0, 1, n)
    c = np.c_[np.interp(s, t, p[:, 0]), np.interp(s, t, p[:, 1])]
    for _ in range(3):  # smooth the polyline
        c[1:-1] = 0.25 * c[:-2] + 0.5 * c[1:-1] + 0.25 * c[2:]
    d = np.gradient(c, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None] + 1e-12
    nr = np.c_[-d[:, 1], d[:, 0]]
    w = np.linspace(w0, w0 if w1 is None else w1, n)[:, None] / 2
    tip = c[-1] + d[-1] * w[-1, 0] * 0.9
    return np.vstack([c + nr * w, [tip], (c - nr * w)[::-1]])


def suspensor(x, y0, n, w=0.34, h=0.3, big=(0.95, 0.95)):
    """Large basal cell at y0 and a filament of n cells above; returns the top y."""
    ax.add_patch(Ellipse((x, y0), big[0], big[1], facecolor=P.light(SUS), edgecolor=P.edge(SUS), lw=0.9, zorder=6))
    y = y0 + big[1] / 2
    for _ in range(n):
        patch([(x - w / 2, y), (x + w / 2, y), (x + w / 2, y + h), (x - w / 2, y + h)], SUS, lw=0.7, z=6,
              fill=P.light(SUS))
        y += h
    return y


def cell_lines(segs, tok=EMB, lw=0.7):
    for a, b in segs:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(tok), lw=lw, zorder=8)


def stage(x, letter, text):
    bio.label(ax, (x, 0.45), f"{letter}  {text}", size="normal", bold=False)


Y0 = 1.55
# A: two-celled
x = 1.9
ax.add_patch(Ellipse((x, Y0 + 0.55), 0.95, 1.2, facecolor=P.light(SUS), edgecolor=P.edge(SUS), lw=0.9, zorder=6))
ax.add_patch(Circle((x, Y0 + 1.45), 0.33, facecolor=P.fill(EMB), edgecolor=P.edge(EMB), lw=0.9, zorder=7))
ax.add_patch(Circle((x, Y0 + 1.45), 0.09, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=8))
ax.add_patch(Circle((x + 0.15, Y0 + 0.75), 0.1, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=8))
bio.callout(ax, (x + 0.3, Y0 + 1.55), (x + 0.75, Y0 + 2.6), "Apical cell")
bio.callout(ax, (x + 0.4, Y0 + 0.35), (x + 0.95, Y0 - 0.15), "Basal cell")
bio.arrow(ax, (x - 0.95, Y0 + 1.1), (x - 0.95, Y0 - 0.25), kind="process", color=P.muted(), lw=0.9)
bio.label(ax, (x - 1.15, Y0 + 0.45), "micropyle", size="tiny", color=P.muted(), rotation=90)
stage(x, "A", "Two-celled")

# B: quadrant on a suspensor
x = 6.0
top = suspensor(x, Y0 + 0.3, 3)
c = (x, top + 0.42)
ax.add_patch(Circle(c, 0.44, facecolor=P.fill(EMB), edgecolor=P.edge(EMB), lw=0.9, zorder=7))
cell_lines([((x, c[1] - 0.44), (x, c[1] + 0.44))])
bio.callout(ax, (x + 0.17, Y0 + 1.25), (x + 1.0, Y0 + 0.5), "Suspensor")
bio.callout(ax, (x + 0.3, c[1] + 0.2), (x + 0.9, c[1] + 1.0), "Quadrant")
stage(x, "B", "Quadrant")

# C: octant
x = 10.0
top = suspensor(x, Y0 + 0.3, 4)
r = 0.58
c = (x, top + r - 0.05)
ax.add_patch(Circle(c, r, facecolor=P.fill(EMB), edgecolor=P.edge(EMB), lw=0.9, zorder=7))
cell_lines([((x, c[1] - r), (x, c[1] + r)), ((x - r, c[1]), (x + r, c[1]))])
bio.callout(ax, (x + 0.3, c[1] + 0.3), (x + 1.0, c[1] + 1.1), "Upper tier")
bio.callout(ax, (x + 0.35, c[1] - 0.3), (x + 1.05, c[1] - 0.6), "Lower tier")
stage(x, "C", "Octant")

# D: globular with protoderm and hypophysis
x = 14.2
top = suspensor(x, Y0 + 0.3, 3)
r = 0.95
c = np.array([x, top + 0.14 + r])
ax.add_patch(Circle(c, r, facecolor=P.fill(EMB), edgecolor=P.edge(EMB), lw=0.9, zorder=7))
ax.add_patch(Circle(c, r * 0.72, facecolor="none", edgecolor=P.edge(EMB), lw=0.6, zorder=8))
for a in np.linspace(0, 2 * np.pi, 15, endpoint=False):
    u = np.array([np.cos(a), np.sin(a)])
    cell_lines([(c + u * r * 0.72, c + u * r)], lw=0.6)
cell_lines([((x, c[1] - r * 0.72), (x, c[1] + r * 0.72)), ((x - r * 0.72, c[1]), (x + r * 0.72, c[1])),
            ((x - 0.48, c[1] + 0.48), (x + 0.48, c[1] - 0.48))], lw=0.5)
hy = [(x - 0.2, top - 0.02), (x + 0.2, top - 0.02), (x + 0.24, top + 0.2), (x - 0.24, top + 0.2)]
patch(hy, HYP, lw=0.7, z=9)
bio.callout(ax, (x + 0.85, c[1] + 0.35), (x + 1.45, c[1] + 1.35), "Protoderm")
bio.callout(ax, (x + 0.2, top + 0.1), (x + 1.25, Y0 + 0.75), "Hypophysis")
stage(x, "D", "Globular")

# E: heart stage
x = 18.6
top = suspensor(x, Y0 + 0.3, 2)
b = top + 0.05
heart = [(x - 0.25, b), (x - 0.75, b + 0.35), (x - 1.05, b + 1.0), (x - 1.05, b + 1.75), (x - 0.75, b + 2.3), (x - 0.4, b + 2.35),
         (x - 0.12, b + 1.95), (x, b + 1.8), (x + 0.12, b + 1.95), (x + 0.4, b + 2.35), (x + 0.75, b + 2.3),
         (x + 1.05, b + 1.75), (x + 1.05, b + 1.0), (x + 0.75, b + 0.35), (x + 0.25, b)]
patch(bio.smooth_closed(heart, n=200), EMB, z=7)
for sgn in (-1, 1):
    lobe = [(x + sgn * 0.12, b + 1.95), (x + sgn * 0.4, b + 2.35), (x + sgn * 0.75, b + 2.3), (x + sgn * 1.05, b + 1.75),
            (x + sgn * 0.95, b + 1.45), (x + sgn * 0.45, b + 1.55)]
    patch(bio.smooth_closed(lobe, n=120), COT, lw=0.7, z=8)
ax.add_patch(Ellipse((x, b + 1.78), 0.3, 0.18, facecolor=P.fill(SAM), edgecolor=P.edge(SAM), lw=0.7, zorder=9))
ax.plot([x, x], [b + 0.25, b + 1.55], color=P.edge("xylem"), lw=1.3, ls=(0, (3, 2)), zorder=9)
for sgn in (-1, 1):
    ax.plot([x, x + sgn * 0.6], [b + 1.5, b + 1.95], color=P.edge("xylem"), lw=1.1, ls=(0, (3, 2)), zorder=9)
bio.callout(ax, (x + 0.75, b + 2.2), (x + 1.55, b + 3.0), "Cotyledon primordium")
bio.callout(ax, (x + 0.1, b + 1.8), (x + 1.65, b + 2.35), "Shoot apex")
bio.callout(ax, (x + 0.02, b + 0.9), (x + 1.6, b + 0.75), "Procambium")
stage(x, "E", "Heart")

# F: torpedo stage
x = 23.0
top = suspensor(x, Y0 + 0.3, 1, big=(0.75, 0.7))
b = top
axis = tube([(x, b), (x, b + 1.0), (x, b + 2.0)], 1.0, 0.95)
patch(axis, EMB, z=7)
for sgn in (-1, 1):
    cot = tube([(x + sgn * 0.25, b + 1.85), (x + sgn * 0.35, b + 3.0), (x + sgn * 0.42, b + 4.4)], 0.5, 0.36)
    patch(cot, COT, lw=0.8, z=8)
ax.add_patch(Ellipse((x, b + 2.02), 0.26, 0.15, facecolor=P.fill(SAM), edgecolor=P.edge(SAM), lw=0.6, zorder=9))
ax.plot([x, x], [b + 0.2, b + 1.85], color=P.edge("xylem"), lw=1.3, ls=(0, (3, 2)), zorder=9)
for sgn in (-1, 1):
    ax.plot([x, x + sgn * 0.3, x + sgn * 0.4], [b + 1.85, b + 2.6, b + 4.0], color=P.edge("xylem"), lw=1.0,
            ls=(0, (3, 2)), zorder=9)
bio.callout(ax, (x + 0.45, b + 3.6), (x + 1.3, b + 4.5), "Cotyledons")
bio.callout(ax, (x + 0.45, b + 1.0), (x + 1.3, b + 1.3), "Hypocotyl")
stage(x, "F", "Torpedo")

# G: mature, bent embryo
x = 28.4
b = Y0 + 0.2
axis = tube([(x - 0.55, b), (x - 0.6, b + 1.5), (x - 0.5, b + 3.0), (x - 0.25, b + 3.9)], 0.62, 0.8)
patch(axis, EMB, z=7)
cot = tube([(x - 0.45, b + 3.55), (x - 0.05, b + 4.35), (x + 0.3, b + 4.5), (x + 0.7, b + 4.1), (x + 0.75, b + 2.8), (x + 0.6, b + 1.5)], 0.7, 0.5)
patch(cot, COT, lw=0.8, z=8)
ax.add_patch(Ellipse((x - 0.2, b + 3.95), 0.22, 0.14, angle=40, facecolor=P.fill(SAM), edgecolor=P.edge(SAM), lw=0.6,
                     zorder=9))
ax.add_patch(Ellipse((x - 0.55, b + 0.12), 0.42, 0.25, facecolor=P.fill(HYP), edgecolor=P.edge(HYP), lw=0.6, zorder=8))
bio.callout(ax, (x + 0.85, b + 3.0), (x + 1.5, b + 4.6), "Cotyledons")
bio.callout(ax, (x - 0.12, b + 4.0), (x - 1.3, b + 5.0), "Plumule")
bio.callout(ax, (x - 0.85, b + 2.2), (x - 1.75, b + 3.2), "Hypocotyl")
bio.callout(ax, (x - 0.75, b + 0.15), (x - 1.75, b - 0.35), "Radicle")
stage(x, "G", "Mature")
