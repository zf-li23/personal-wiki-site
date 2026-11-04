"""Pasteur's swan-necked flask experiment in three panels: preparing the neck, sterile broth with dust
trapped in the bend, and contamination after the broth touches the bend."""
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 10)


def flask(cx, broth_tok, tilt=False, neck_cut=False):
    """Round-bottomed flask at x=cx with a long S-shaped neck; returns the bend point."""
    t = np.linspace(0, 2 * np.pi, 200)
    r = 1.6
    cy = 2.4
    # bulb outline (open at top-left for the neck)
    bulb = np.c_[cx + r * np.cos(t), cy + r * np.sin(t)]
    # broth fill: circle segment below level
    lev = cy + (0.25 if not tilt else 0.1)
    inside = bulb[bulb[:, 1] <= lev]
    ang = np.linspace(np.arcsin((lev - cy) / r), np.pi - np.arcsin((lev - cy) / r), 2)
    seg = np.vstack([inside[np.argsort(np.arctan2(inside[:, 1] - cy, inside[:, 0] - cx))]])
    th = np.linspace(np.pi - np.arcsin((lev - cy) / r), 2 * np.pi + np.arcsin((lev - cy) / r), 120)
    seg = np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]
    ax.add_patch(PathPatch(Path(np.vstack([seg, seg[:1]]), closed=True), facecolor=P.fill(broth_tok),
                           edgecolor="none", zorder=3))
    ax.add_patch(PathPatch(Path(np.vstack([bulb, bulb[:1]]), closed=True), facecolor="none",
                           edgecolor=P.ink(), lw=1.6, zorder=5))
    # neck: from top of bulb, up, then a long downward bend and up again (swan neck)
    x0, y0 = cx - 0.3, cy + r - 0.02
    pts = np.array([[x0, y0], [x0 - 0.2, y0 + 1.2], [x0 - 0.9, y0 + 2.4], [x0 - 2.0, y0 + 2.2],
                    [x0 - 2.6, y0 + 1.2], [x0 - 3.1, y0 + 1.0], [x0 - 3.6, y0 + 1.6], [x0 - 3.9, y0 + 3.0]])
    if neck_cut:
        pts = pts[:3]
    from scipy.interpolate import make_interp_spline
    s = np.linspace(0, 1, len(pts))
    spl = make_interp_spline(s, pts, k=min(3, len(pts) - 1))
    c = spl(np.linspace(0, 1, 200))
    ax.plot(c[:, 0], c[:, 1], color=P.ink(), lw=4.5, solid_capstyle="round", zorder=4)
    ax.plot(c[:, 0], c[:, 1], color=P.surface(), lw=2.6, solid_capstyle="round", zorder=4.5)
    bend = spl(0.69) if not neck_cut else None
    return c, bend


def dust(points, seed):
    rng = np.random.default_rng(seed)
    for x, y in points:
        for _ in range(7):
            ax.plot(x + rng.normal(0, 0.09), y + rng.normal(0, 0.06), "o", ms=3.4, color=P.edge("bacterium"),
                    zorder=6)


# A: drawing out the neck
bio.panel(ax, "A", (0.2, 9.8))
c, bend = flask(5.0, "extracellular")
bio.label(ax, (4.8, 9.4), "Nonsterile broth; neck drawn out\nand bent in a flame", size="small")
# flame under the neck
tt = np.linspace(0, 2 * np.pi, 80)
fx, fy = bend[0], bend[1] - 1.25
flame = np.c_[fx + 0.32 * np.sin(tt) * (1 - 0.5 * (1 + np.cos(tt)) / 2), fy + 0.55 * np.cos(tt) - 0.1 * np.cos(2 * tt)]
flame = np.c_[fx + 0.3 * np.sin(tt) * np.abs(np.sin(tt / 2)) ** 0.6, fy + 0.45 * np.cos(tt)]
ax.add_patch(PathPatch(Path(np.vstack([flame, flame[:1]]), closed=True), facecolor=P.fill("highlight"),
                       edgecolor=P.edge("highlight"), lw=0.8, zorder=7))
bio.label(ax, (fx, fy - 0.85), "flame", size="tiny", color=P.muted())
rng0 = np.random.default_rng(7)
for _ in range(14):
    a, rr = rng0.uniform(np.pi * 1.05, np.pi * 1.95), rng0.uniform(0.1, 1.45)
    ax.plot(5.0 + rr * np.cos(a), 2.6 + rr * np.sin(a) * 0.95, "o", ms=2.0, color=P.edge("bacterium"), zorder=6)
# B: sterilized
bio.panel(ax, "B", (9.2, 9.8))
c, bend = flask(14.0, "cytoplasm")
dust([bend], 1)
bio.callout(ax, bend + np.array([0, -0.15]), (bend[0] - 0.2, bend[1] - 2.0), "dust and microbes\ntrapped in bend")
bio.label(ax, (13.8, 9.4), "Broth boiled; air re-enters on cooling;\nbroth stays sterile indefinitely", size="small")
bio.label(ax, (14.0, 0.25), "clear", size="small", color=P.muted())
# C: tipped or neck broken -> contamination
bio.panel(ax, "C", (18.2, 9.8))
c, bend = flask(23.2, "bacterium")
rng = np.random.default_rng(3)
for _ in range(40):
    a, rr = rng.uniform(np.pi * 1.05, np.pi * 1.95), rng.uniform(0.1, 1.45)
    ax.plot(23.2 + rr * np.cos(a), 2.4 + 0.2 + rr * np.sin(a) * 0.95, "o", ms=2.0, color=P.edge("bacterium"),
            zorder=6)
dust([bend], 2)
bio.arrow(ax, (bend[0] + 0.3, bend[1] - 0.3), (22.0, 3.0), kind="process", bend=-0.25)
bio.label(ax, (bend[0] - 0.2, bend[1] - 2.0), "microbes washed\ninto the broth", size="tiny", color=P.muted())
bio.label(ax, (22.8, 9.4), "Flask tipped: broth washes the bend\n(or neck broken off)", size="small")
bio.label(ax, (23.2, 0.25), "turbid within days", size="small", color=P.muted())
