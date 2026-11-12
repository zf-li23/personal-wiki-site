"""Apposition and superposition compound eyes (schematic sections, not to scale). In an apposition eye (A) each
ommatidium is optically isolated by screening pigment, and its lens and crystalline cone focus light from a small
angle onto the rhabdom directly beneath. In a superposition eye (B) a wide clear zone separates the cones from the
retina; parallel rays from one point in the visual field enter many facets and are bent by the cones so that they
converge on a single rhabdom, which makes the eye far more sensitive in dim light.
"""

import numpy as np
from matplotlib.patches import Polygon, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.0)

LENS = P.fill("highlight")
CONE = P.light("highlight")
PIG = P.mix(P.ink(), P.surface(), 0.35)
RHAB = P.fill("rna")
RAY = P.edge("dna")


def eye(cx, cy, R, superposition):
    """Draw a fan of ommatidia on a circle of radius R around (cx, cy); return their angles."""
    angs = np.radians(np.linspace(72, 108, 7))
    r_lens, r_cone = R, R - 0.55
    r_ret0 = R - (2.0 if not superposition else 4.2)
    r_ret1 = r_ret0 - 1.4
    # retina band and basement membrane
    ax.add_patch(Wedge((cx, cy), r_ret0 + 0.05, 69, 111, width=r_ret0 - r_ret1 + 0.1, facecolor=P.light("neuron"),
                       edgecolor=P.edge("neuron"), lw=0.8, zorder=2))
    if superposition:
        ax.add_patch(Wedge((cx, cy), r_cone - 1.25, 69, 111, width=(r_cone - 1.25) - r_ret0 - 0.05,
                           facecolor=P.surface(), edgecolor=P.muted(), lw=0.5, zorder=2, ls=(0, (3, 3))))
    for a in angs:
        u = np.array([np.cos(a), np.sin(a)])
        t = np.array([-u[1], u[0]])
        p = lambda r, w: (cx + r * u[0] + w * t[0], cy + r * u[1] + w * t[1])
        # corneal lens
        ax.add_patch(Polygon([p(r_lens + 0.15, -0.55), p(r_lens + 0.15, 0.55), p(r_lens - 0.35, 0.5), p(r_lens - 0.35, -0.5)],
                             closed=True, facecolor=LENS, edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
        # crystalline cone
        ax.add_patch(Polygon([p(r_cone + 0.2, -0.45), p(r_cone + 0.2, 0.45), p(r_cone - 1.2, 0.12), p(r_cone - 1.2, -0.12)],
                             closed=True, facecolor=CONE, edgecolor=P.edge("highlight"), lw=0.7, zorder=6))
        # screening pigment between neighbours
        for w in (-0.55, 0.55):
            ax.plot(*zip(p(r_cone + 0.2, w), p(r_cone - 1.2, w * 0.7)), color=PIG, lw=3.0, zorder=5, solid_capstyle="butt")
            if not superposition:
                ax.plot(*zip(p(r_cone - 1.2, w * 0.7), p(r_ret1, w * 0.6)), color=PIG, lw=3.0, zorder=5, solid_capstyle="butt")
        if not superposition:
            ax.plot(*zip(p(r_cone - 1.2, 0), p(r_ret0, 0)), color=P.edge("highlight"), lw=1.2, zorder=6)
        # rhabdom
        ax.add_patch(Polygon([p(r_ret0, -0.12), p(r_ret0, 0.12), p(r_ret1, 0.12), p(r_ret1, -0.12)], closed=True,
                             facecolor=RHAB, edgecolor=P.edge("rna"), lw=0.7, zorder=7))
    return angs, r_lens, r_cone, r_ret0, r_ret1


# A: apposition
bio.panel(ax, "A", (0.3, 11.7))
bio.label(ax, (6.3, 11.35), "Apposition eye", size="title", bold=True)
cx, cy, R = 6.3, -2.6, 12.6
angs, rl, rc, r0, r1 = eye(cx, cy, R, False)
a = angs[3]
u = np.array([np.cos(a), np.sin(a)])
t = np.array([-u[1], u[0]])
for w in (-0.4, 0.0, 0.4):
    start = np.array([cx, cy]) + (rl + 1.3) * u + w * t
    lens = np.array([cx, cy]) + (rl + 0.1) * u + w * t
    tip = np.array([cx, cy]) + (rc - 1.2) * u
    ax.plot([start[0], lens[0], tip[0]], [start[1], lens[1], tip[1]], color=RAY, lw=1.3, zorder=9)
bio.callout(ax, (cx + (rl + 0.05) * np.cos(angs[1]), cy + (rl + 0.05) * np.sin(angs[1])), (11.0, 11.0), "Corneal lens", size="small")
bio.callout(ax, (cx + (rc - 0.6) * np.cos(angs[1]), cy + (rc - 0.6) * np.sin(angs[1])), (11.4, 9.6), "Crystalline cone", size="small")
bio.callout(ax, (cx + (rc - 0.5) * np.cos(angs[6]) + 0.62, cy + (rc - 0.5) * np.sin(angs[6])), (0.6, 9.8), "Screening pigment", size="small")
bio.callout(ax, (cx + (r0 - 0.7) * np.cos(angs[1]), cy + (r0 - 0.7) * np.sin(angs[1])), (11.4, 7.4), "Rhabdom", size="small")
bio.label(ax, (6.3, 5.3), "Each rhabdom receives light\nonly through its own facet", size="small", color=P.muted())
bio.label(ax, (6.3, 4.2), "Day-active insects, many crustaceans", size="small", italic=False)

# B: superposition
bio.panel(ax, "B", (13.3, 11.7))
bio.label(ax, (19.5, 11.35), "Superposition eye", size="title", bold=True)
cx, cy, R = 19.5, -2.6, 12.6
angs, rl, rc, r0, r1 = eye(cx, cy, R, True)
target = np.array([cx, cy]) + (r0 - 0.1) * np.array([0.0, 1.0])
for a in angs[1:-1]:
    u = np.array([np.cos(a), np.sin(a)])
    start = np.array([cx, cy]) + (rl + 1.3) * u
    start = np.array([start[0] * 0 + cx + (rl) * np.cos(a), cy + rl * np.sin(a) + 1.3])
    lens = np.array([cx + rl * np.cos(a), cy + rl * np.sin(a)])
    cone = np.array([cx + (rc - 1.2) * np.cos(a), cy + (rc - 1.2) * np.sin(a)])
    ax.plot([lens[0], lens[0]], [lens[1] + 1.3, lens[1]], color=RAY, lw=1.1, zorder=9)
    ax.plot([lens[0], cone[0], target[0]], [lens[1], cone[1], target[1]], color=RAY, lw=1.1, zorder=9)
bio.callout(ax, (cx + (r0 + 0.9) * np.cos(angs[6]) + 0.3, cy + (r0 + 0.9) * np.sin(angs[6])), (14.0, 7.8), "Clear zone", size="small")
bio.callout(ax, (target[0] + 0.1, target[1] - 0.4), (24.6, 6.6), "Rhabdom receiving\nlight from many facets", size="small")
bio.label(ax, (19.5, 3.3), "Parallel rays from one point converge on one rhabdom", size="small", color=P.muted())
bio.label(ax, (19.5, 2.5), "Moths, many beetles, krill and decapod crustaceans", size="small")
