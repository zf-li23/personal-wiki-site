# Seedling types, three stages each (soil line = ground surface). (A) Epigeal germination of bean
# (Phaseolus vulgaris): the hypocotyl elongates as a hook and pulls the cotyledons above ground.
# (B) Hypogeal germination of pea (Pisum sativum): the cotyledons stay in the seed below ground; the
# epicotyl elongates and forms the hook. (C) Hypogeal germination of a grass (maize, Zea mays): the
# scutellum stays in the grain; the coleorhiza is pierced by the primary root, seminal roots arise from
# the scutellar node, the mesocotyl lifts the coleoptile to the surface and the first leaf emerges
# through the pore at the coleoptile tip.
import math

import numpy as np
from matplotlib.patches import PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
R = PM.ROLE
fig, ax = bio.canvas(30.0, 24.0)


def patch(pts, role, lw=0.8, z=6):
    pts = np.asarray(pts, float)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=P.fill(R.get(role, role)),
                           edgecolor=P.edge(R.get(role, role)), lw=lw, joinstyle="round", zorder=z))


def tube(c, w0, w1):
    c = np.asarray(c, float)
    d = np.gradient(c, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None] + 1e-12
    n = np.c_[-d[:, 1], d[:, 0]]
    w = np.linspace(w0, w1, len(c))[:, None] / 2
    return np.vstack([c + n * w, (c - n * w)[::-1]])


def curve(pts, n=40):
    pts = np.asarray(pts, float)
    t = np.linspace(0, 1, len(pts))
    tt = np.linspace(0, 1, n)
    return np.c_[np.interp(tt, t, pts[:, 0]), np.interp(tt, t, pts[:, 1])]


def soil(x0, x1, y, depth):
    ax.add_patch(Polygon([(x0, y - depth), (x1, y - depth), (x1, y), (x0, y)], closed=True,
                         facecolor=P.mix(P.surface(), P.fill(R["soil"]), 0.4), edgecolor="none", zorder=1))
    ax.plot([x0, x1], [y, y], color=P.edge(R["soil"]), lw=1.0, zorder=2)


def root(start, length, n=3, sg0=1, lw=1.4):
    main = curve([start, (start[0] + 0.1, start[1] - length * 0.5), (start[0] - 0.05, start[1] - length)], 30)
    ax.plot(main[:, 0], main[:, 1], color=P.edge(R["root"]), lw=lw, zorder=4, solid_capstyle="round")
    for k in range(n):
        p = main[int((0.3 + 0.5 * k / max(1, n - 1)) * 29)]
        sg = sg0 if k % 2 == 0 else -sg0
        L = length * 0.3
        lat = curve([p, (p[0] + sg * L * 0.6, p[1] - L * 0.3), (p[0] + sg * L, p[1] - L * 0.6)], 15)
        ax.plot(lat[:, 0], lat[:, 1], color=P.edge(R["root"]), lw=lw * 0.6, zorder=4)
    return main[-1]


def grain(c):
    g = bio.smooth_closed([(0, 0.55), (0.42, 0.35), (0.5, -0.1), (0.3, -0.5), (0.0, -0.6), (-0.3, -0.5), (-0.5, -0.1),
                           (-0.42, 0.35)], n=120) * 0.9 + c
    patch(g, "pericarp", z=5)
    e = bio.smooth_closed([(-0.05, 0.3), (0.12, 0.1), (0.12, -0.35), (-0.05, -0.45), (-0.2, -0.1)], n=80) * 0.9 + c
    patch(e, "scutellum", z=5.5)
    return g


rows = [("A", "Epigeal germination (bean)", 19.4), ("B", "Hypogeal germination (pea)", 11.4),
        ("C", "Hypogeal germination of a grass (maize)", 3.4)]
X = [5.0, 12.0, 19.0]
for letter, title, g in rows:
    bio.panel(ax, letter, (0.2, g + 4.4))
    bio.label(ax, (13.0, g + 3.9), title, size="normal", bold=True)
    for k in range(2):
        bio.arrow(ax, (X[k] + 2.2, g + 1.4), (X[k] + 4.2, g + 1.4), kind="process", color=P.muted())
    bio.label(ax, (22.6, g + 0.2), "soil surface", size="tiny", color=P.muted(), ha="left")

# A and B: legume templates
for kind, g in (("epigeal", 19.4), ("hypogeal", 11.4)):
    s = [PM.germination(ax, (x, g), 4.4, kind=kind, stage=st) for x, st in zip(X, (1, 2, 3))]
    bio.callout(ax, s[0]["radicle"], (2.2, g - 2.2), "Radicle", size="small")
    if kind == "epigeal":
        bio.callout(ax, s[1]["hypocotyl"], (9.6, g + 3.0), "Hypocotyl hook", size="small")
        PM.callouts(ax, [(s[2]["leaves"], "First leaves", "right"), (s[2]["epicotyl"], "Epicotyl", "right"),
                         (s[2]["cotyledons"], "Cotyledons", "right"), (s[2]["hypocotyl"], "Hypocotyl", "right"),
                         (s[2]["root"], "Primary root", "right")], right=23.6, gap=0.55)
    else:
        bio.callout(ax, s[1]["epicotyl"], (9.6, g + 3.0), "Epicotyl hook", size="small")
        PM.callouts(ax, [(s[2]["leaves"], "First leaves", "right"), (s[2]["epicotyl"], "Epicotyl", "right"),
                         (s[2]["seed"], "Cotyledons (in seed)", "right"), (s[2]["root"], "Primary root", "right")],
                    right=23.6, gap=0.55)

# C: maize, drawn natively
g = 3.4
for x in X:
    soil(x - 1.85, x + 1.85, g, 2.9)
depth = 0.9
# stage 1: coleorhiza pierced by the radicle
c1 = np.array([X[0], g - depth])
grain(c1)
patch(tube(curve([(X[0] - 0.05, g - depth - 0.45), (X[0] - 0.1, g - depth - 0.75)], 10), 0.34, 0.28), "pericarp", z=6)
tip1 = root((X[0] - 0.1, g - depth - 0.75), 0.6, n=0, lw=1.8)
# stage 2: primary root, seminal roots, mesocotyl and coleoptile reaching the surface
c2 = np.array([X[1], g - depth])
grain(c2)
root((X[1] - 0.1, g - depth - 0.5), 1.1, n=3)
for sg in (-1, 1):
    sem = curve([(X[1] - 0.05, g - depth - 0.35), (X[1] + sg * 0.6, g - depth - 0.7), (X[1] + sg * 1.0, g - depth - 1.4)], 20)
    ax.plot(sem[:, 0], sem[:, 1], color=P.edge(R["root"]), lw=1.1, zorder=4)
meso2 = curve([(X[1] - 0.05, g - depth + 0.4), (X[1], g - 0.35)], 10)
patch(tube(meso2, 0.16, 0.16), "plant", z=6)
cole2 = curve([(X[1], g - 0.35), (X[1], g + 0.25)], 10)
patch(tube(cole2, 0.22, 0.08), "coleoptile", z=6.5)
# stage 3: coleoptile above ground, first leaf through its pore, crown roots beginning
c3 = np.array([X[2], g - depth])
grain(c3)
r3 = root((X[2] - 0.1, g - depth - 0.5), 1.4, n=4)
for sg in (-1, 1):
    sem = curve([(X[2] - 0.05, g - depth - 0.35), (X[2] + sg * 0.8, g - depth - 0.8), (X[2] + sg * 1.3, g - depth - 1.4)], 20)
    ax.plot(sem[:, 0], sem[:, 1], color=P.edge(R["root"]), lw=1.1, zorder=4)
meso3 = curve([(X[2] - 0.05, g - depth + 0.4), (X[2], g - 0.15)], 10)
patch(tube(meso3, 0.16, 0.16), "plant", z=6)
for sg in (-1, 1):  # first nodal (crown) roots at the coleoptile node
    cr = curve([(X[2], g - 0.15), (X[2] + sg * 0.5, g - 0.45), (X[2] + sg * 0.8, g - 0.95)], 15)
    ax.plot(cr[:, 0], cr[:, 1], color=P.edge(R["root"]), lw=1.0, zorder=4, ls=(0, (2, 1)))
cole3 = curve([(X[2], g - 0.15), (X[2], g + 0.9)], 10)
patch(tube(cole3, 0.24, 0.1), "coleoptile", z=6.5)
leaf = curve([(X[2], g + 0.75), (X[2] + 0.05, g + 1.6), (X[2] + 0.35, g + 2.4), (X[2] + 0.9, g + 2.9)], 30)
patch(tube(leaf, 0.2, 0.04), "plant", z=7)
bio.callout(ax, tip1, (2.2, g - 2.2), "Primary root", size="small")
bio.callout(ax, (X[0] - 0.08, g - depth - 0.55), (2.2, g - 1.4), "Coleorhiza", size="small")
bio.callout(ax, (X[0] + 0.3, g - depth + 0.2), (2.2, g + 1.0), "Grain (scutellum inside)", size="small")
bio.callout(ax, (X[1] + 0.02, g + 0.1), (9.6, g + 2.6), "Coleoptile", size="small")
PM.callouts(ax, [((X[2] + 0.5, g + 2.6), "First leaf", "right"), ((X[2] + 0.08, g + 0.5), "Coleoptile", "right"),
                 ((X[2] + 0.07, g - 0.6), "Mesocotyl", "right"), ((X[2] + 0.6, g - 0.65), "Crown roots", "right"),
                 ((X[2] + 1.2, g - depth - 1.25), "Seminal roots", "right"), (tuple(r3), "Primary root", "right")],
            right=23.6, gap=0.55)
