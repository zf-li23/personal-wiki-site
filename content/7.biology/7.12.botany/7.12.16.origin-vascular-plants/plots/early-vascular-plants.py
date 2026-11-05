"""Early vascular plants, schematic reconstructions (not to one scale): Cooksonia, Rhynia, Zosterophyllum,
Asteroxylon, Baragwanathia and Psilophyton. Coloured bands below mark the lineages: stem-group vascular
plants, the lycophyte lineage and the euphyllophyte lineage."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 13.6)
AX, AXE = P.fill("plant"), P.edge("plant")
SP, SPE = P.fill("animal"), P.edge("animal")
GROUND = 2.6


def seg(p, q, w):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=AXE, lw=w, solid_capstyle="round", zorder=5)


def spor(xy, ang, a, b, shape="ellipse"):
    if shape == "kidney":
        ax.add_patch(Ellipse(xy, a, b, angle=ang, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=7))
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        ax.plot([xy[0] - d[0] * a * 0.45, xy[0] + d[0] * a * 0.45], [xy[1] - d[1] * a * 0.45, xy[1] + d[1] * a * 0.45],
                color=SPE, lw=0.6, zorder=8)
    else:
        ax.add_patch(Ellipse(xy, a, b, angle=ang, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=7))


def dich(p, ang, L, depth, w, spread=24, tip=None, shrink=0.78, rng=None, unequal=0.0):
    a = np.radians(ang)
    q = (p[0] + L * np.cos(a), p[1] + L * np.sin(a))
    seg(p, q, w)
    if depth == 0:
        if tip:
            tip(q, ang)
        return
    for s in (-1, 1):
        f = 1.0 + (unequal if s > 0 else -unequal)
        jit = rng.uniform(-5, 5) if rng is not None else 0
        dich(q, ang + s * spread + jit, L * shrink * f, depth - 1, max(0.8, w * 0.8), spread, tip, shrink, rng, unequal)


def ground(x0, x1):
    ax.plot([x0, x1], [GROUND, GROUND], color=P.muted(), lw=0.9, zorder=3)


def rhizome(x0, x1, rhizoids=True, roots=False):
    seg((x0, GROUND - 0.25), (x1, GROUND - 0.25), 2.4)
    for x in np.linspace(x0 + 0.2, x1 - 0.2, 7):
        if rhizoids:
            ax.plot([x, x - 0.08], [GROUND - 0.3, GROUND - 0.65], color=P.muted(), lw=0.6, zorder=4)
        if roots:
            dich((x, GROUND - 0.3), -90 + np.sin(x) * 15, 0.35, 2, 1.0, spread=28)


def head(x, t, sub):
    bio.label(ax, (x, 12.9), t, size="normal", bold=True, italic=True)
    bio.label(ax, (x, 12.35), sub, size="tiny", color=P.muted())


xs = [2.6, 7.9, 13.2, 18.5, 23.8, 29.1]
for i, L in enumerate("ABCDEF"):
    bio.panel(ax, L, (xs[i] - 2.5, 13.4))
rng = np.random.default_rng(2)

# A Cooksonia
x = xs[0]; ground(x - 2, x + 2)
for dx in (-0.6, 0.5):
    dich((x + dx, GROUND), 90, 2.6, 2, 2.0, spread=17, shrink=0.8, rng=rng,
         tip=lambda q, a: ax.add_patch(Polygon([(q[0] - 0.05, q[1]), (q[0] - 0.28, q[1] + 0.34), (q[0] + 0.28, q[1] + 0.34),
                                                 (q[0] + 0.05, q[1])], closed=True, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=7)))
head(x, "Cooksonia", "Mid Silurian to Early Devonian; a few cm")

# B Rhynia
x = xs[1]; ground(x - 2.2, x + 2.2); rhizome(x - 2.0, x + 2.0)
for dx in (-1.1, 0.0, 1.0):
    dich((x + dx, GROUND - 0.2), 90, 2.8, 2, 2.2, spread=13, shrink=0.85, rng=rng,
         tip=lambda q, a: spor((q[0], q[1] + 0.32), a, 0.7, 0.26))
seg((x + 0.0, 4.6), (x + 0.5, 5.3), 1.2); spor((x + 0.66, 5.55), 50, 0.45, 0.2)
head(x, "Rhynia", "Rhynie chert, ~407 Ma; ~20 cm")

# C Zosterophyllum
x = xs[2]; ground(x - 2.2, x + 2.2); rhizome(x - 2.0, x + 2.0)
for dx, h in ((-1.0, 6.4), (0.1, 7.6), (1.1, 6.0)):
    seg((x + dx, GROUND - 0.2), (x + dx, GROUND + h), 2.2)
    for k in range(7):
        y = GROUND + h * (0.55 + 0.065 * k)
        s = 1 if k % 2 == 0 else -1
        seg((x + dx, y), (x + dx + s * 0.22, y + 0.1), 0.9)
        spor((x + dx + s * 0.42, y + 0.16), 0, 0.42, 0.3, "kidney")
seg((x - 1.0, GROUND + 0.4), (x - 1.45, GROUND + 0.75), 1.4)
seg((x - 1.45, GROUND + 0.75), (x - 1.45, GROUND + 1.6), 1.4)
head(x, "Zosterophyllum", "Late Silurian to Devonian; lateral sporangia")

# D Asteroxylon
x = xs[3]; ground(x - 2.2, x + 2.2); rhizome(x - 1.8, x + 1.8, rhizoids=False, roots=True)


def leafy(p, ang, L, depth, w):
    a = np.radians(ang)
    q = (p[0] + L * np.cos(a), p[1] + L * np.sin(a))
    seg(p, q, w)
    for t in np.linspace(0.05, 0.95, int(L * 7)):
        c = (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        for s in (-1, 1):
            e = np.radians(ang + s * 55)
            ax.plot([c[0], c[0] + 0.22 * np.cos(e)], [c[1], c[1] + 0.22 * np.sin(e)], color=AXE, lw=0.6, zorder=5)
    if depth:
        for s in (-1, 1):
            leafy(q, ang + s * 22, L * 0.7, depth - 1, w * 0.8)


leafy((x - 0.3, GROUND - 0.2), 92, 3.2, 2, 2.6)
leafy((x + 0.9, GROUND - 0.2), 86, 2.4, 2, 2.0)
for y in (6.4, 7.0):
    spor((x - 0.05, y), 0, 0.34, 0.26, "kidney")
head(x, "Asteroxylon", "Rhynie chert; enations without veins")

# E Baragwanathia
x = xs[4]; ground(x - 2.2, x + 2.2)
for dx, ang in ((-0.4, 95), (0.6, 82)):
    a = np.radians(ang)
    p = (x + dx, GROUND)
    q = (p[0] + 6.2 * np.cos(a), p[1] + 6.2 * np.sin(a))
    seg(p, q, 3.2)
    for t in np.linspace(0.04, 0.98, 30):
        c = (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        for s in (-1, 1):
            e = np.radians(ang + s * 40)
            ax.plot([c[0], c[0] + 0.75 * np.cos(e)], [c[1], c[1] + 0.75 * np.sin(e)], color=AXE, lw=0.7, zorder=4)
spor((x - 0.38, 5.0), 0, 0.3, 0.22, "kidney")
head(x, "Baragwanathia", "Late Silurian, Australia; microphylls")

# F Psilophyton
x = xs[5]; ground(x - 2.2, x + 2.2); rhizome(x - 1.8, x + 1.8)
seg((x, GROUND - 0.2), (x, GROUND + 7.4), 2.8)


def fertile(q, a):
    for s in (-1, 1):
        spor((q[0] + s * 0.07, q[1] - 0.25), 90, 0.5, 0.14)


for k, y in enumerate(np.linspace(GROUND + 1.6, GROUND + 6.8, 6)):
    s = 1 if k % 2 == 0 else -1
    dich((x, y), 90 - s * 55, 0.8, 2, 1.4, spread=26, shrink=0.75, rng=rng,
         tip=fertile if k >= 3 else lambda q, a: ax.plot([q[0]], [q[1]], marker="o", ms=1.5, color=AXE, zorder=6))
for y in np.linspace(GROUND + 0.4, GROUND + 3.0, 7):
    for s in (-1, 1):
        ax.plot([x, x + s * 0.18], [y, y + 0.12], color=AXE, lw=0.8, zorder=5)
head(x, "Psilophyton", "Early-Mid Devonian; main axis and side branches")

# lineage bands
bands = [(xs[0] - 2.4, xs[1] + 2.4, "neutral", "Stem-group vascular plants (rhyniophytes)"),
         (xs[2] - 2.4, xs[4] + 2.4, "plant", "Lycophyte lineage: lateral, kidney-shaped sporangia"),
         (xs[5] - 2.4, xs[5] + 2.4, "bract", "Euphyllophyte lineage")]
for x0, x1, tok, t in bands:
    ax.add_patch(Polygon([(x0, 0.4), (x1, 0.4), (x1, 1.2), (x0, 1.2)], facecolor=P.mix(P.surface(), P.fill(tok), 0.25), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, ((x0 + x1) / 2, 0.8), t, size="small")
